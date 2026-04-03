from datetime import datetime
from pathlib import Path
from typing import Any, Callable

import torch
from xgboost import XGBClassifier

from analysis_and_experiments.data import load_filtered_markets_with_trades
from analysis_and_experiments.evaluation import (
    calculate_average_margin_of_victory,
    evaluate_binary_metrics,
)
from analysis_and_experiments.plotting import save_confusion_matrix_plot, save_roc_plot
from analysis_and_experiments.strategies.common import RunResult

CLASSIFICATION_THRESHOLD = 0.5
REFERENCE_PRICE_FEATURE = "rolling_vwap_last"

XGB_PARAMS: dict[str, Any] = {
    "objective": "binary:logistic",
    "eval_metric": "logloss",
    "random_state": 42,
    "n_estimators": 300,
    "learning_rate": 0.05,
    "max_depth": 4,
    "subsample": 0.9,
    "colsample_bytree": 0.9,
}


def _safe_mean(values: list[float]) -> float:
    if not values:
        return 0.0
    return float(sum(values) / len(values))


def _safe_variance(values: list[float]) -> float:
    if len(values) < 2:
        return 0.0
    mean = _safe_mean(values)
    return float(sum((value - mean) ** 2 for value in values) / len(values))


def _safe_std(values: list[float]) -> float:
    return float(_safe_variance(values) ** 0.5)


def _linear_slope(values: list[float]) -> float:
    if len(values) < 2:
        return 0.0

    x_values = list(range(len(values)))
    x_mean = _safe_mean(x_values)
    y_mean = _safe_mean(values)
    numerator = sum((x - x_mean) * (y - y_mean) for x, y in zip(x_values, values, strict=True))
    denominator = sum((x - x_mean) ** 2 for x in x_values)
    if denominator == 0:
        return 0.0
    return float(numerator / denominator)


def _parse_trade_arrays(
    trades: list[dict[str, Any]],
) -> tuple[list[float], list[float], list[float], list[str], list[str]]:
    prices = [float(trade["price"]) for trade in trades]
    volumes = [float(trade["total_usdc"]) for trade in trades]
    tokens = [float(trade["tokens"]) for trade in trades]
    sides = [str(trade["side"]) for trade in trades]
    wallets = [str(trade["wallet"]) for trade in trades]
    return prices, volumes, tokens, sides, wallets


def _calculate_duration_seconds(trades: list[dict[str, Any]]) -> float:
    if len(trades) < 2:
        return 0.0
    first_ts = datetime.fromisoformat(str(trades[0]["timestamp"]))
    last_ts = datetime.fromisoformat(str(trades[-1]["timestamp"]))
    duration = (last_ts - first_ts).total_seconds()
    return float(max(duration, 0.0))


def _rolling_volume_weighted_prices(prices: list[float], volumes: list[float], window: int) -> list[float]:
    if window < 1:
        raise ValueError("window must be >= 1")

    rolling_values: list[float] = []
    for end_index in range(len(prices)):
        start_index = max(0, end_index - window + 1)
        window_prices = prices[start_index : end_index + 1]
        window_volumes = volumes[start_index : end_index + 1]

        volume_sum = float(sum(window_volumes))
        if volume_sum > 0:
            weighted_price = sum(
                price * volume
                for price, volume in zip(window_prices, window_volumes, strict=True)
            ) / volume_sum
        else:
            weighted_price = _safe_mean(window_prices)
        rolling_values.append(float(weighted_price))

    return rolling_values


def extract_market_features(
    market: dict[str, Any],
    trades: list[dict[str, Any]],
    *,
    vwap_window: int = 4,
    whale_top_k: int = 10,
) -> dict[str, float]:
    _ = market
    if vwap_window < 1:
        raise ValueError("vwap_window must be >= 1")
    if whale_top_k < 1:
        raise ValueError("whale_top_k must be >= 1")
    if not trades:
        return {}

    prices, volumes, tokens, sides, wallets = _parse_trade_arrays(trades)
    rolling_weighted_prices = _rolling_volume_weighted_prices(prices, volumes, vwap_window)

    duration_seconds = _calculate_duration_seconds(trades)
    trades_per_minute = float(len(trades) / (duration_seconds / 60.0)) if duration_seconds > 0 else 0.0

    wallet_to_net_tokens: dict[str, float] = {}
    for wallet, side, token_count in zip(wallets, sides, tokens, strict=True):
        direction = 1.0 if side == "BUY" else -1.0
        wallet_to_net_tokens[wallet] = wallet_to_net_tokens.get(wallet, 0.0) + direction * token_count

    positive_net_holdings = [value for value in wallet_to_net_tokens.values() if value > 0]
    positive_net_holdings.sort(reverse=True)
    total_positive_holdings = float(sum(positive_net_holdings))

    if total_positive_holdings > 0:
        top1_share = float(positive_net_holdings[0] / total_positive_holdings)
        topk_share = float(sum(positive_net_holdings[:whale_top_k]) / total_positive_holdings)
        whale_hhi = float(sum((value / total_positive_holdings) ** 2 for value in positive_net_holdings))
    else:
        top1_share = 0.0
        topk_share = 0.0
        whale_hhi = 0.0

    features = {
        "price_latest": float(prices[-1]),
        "price_min": float(min(prices)),
        "price_max": float(max(prices)),
        "price_range": float(max(prices) - min(prices)),
        "price_mean": _safe_mean(prices),
        "price_std": _safe_std(prices),
        "price_var": _safe_variance(prices),
        "volume_total_usdc": float(sum(volumes)),
        "volume_latest_usdc": float(volumes[-1]),
        "volume_mean_usdc": _safe_mean(volumes),
        "volume_std_usdc": _safe_std(volumes),
        "volume_var_usdc": _safe_variance(volumes),
        "volume_max_usdc": float(max(volumes)),
        "trade_count": float(len(trades)),
        "duration_seconds": duration_seconds,
        "trades_per_minute": trades_per_minute,
        "rolling_vwap_last": float(rolling_weighted_prices[-1]),
        "rolling_vwap_mean": _safe_mean(rolling_weighted_prices),
        "rolling_vwap_std": _safe_std(rolling_weighted_prices),
        "rolling_vwap_min": float(min(rolling_weighted_prices)),
        "rolling_vwap_max": float(max(rolling_weighted_prices)),
        "rolling_vwap_slope": _linear_slope(rolling_weighted_prices),
        "whale_top1_share": top1_share,
        "whale_topk_share": topk_share,
        "whale_hhi": whale_hhi,
    }
    return features


def build_tabular_feature_matrix(
    loaded_markets: list[dict[str, Any]],
    market_id_to_trades: dict[str, list[dict[str, Any]]],
    *,
    vwap_window: int = 4,
    whale_top_k: int = 10,
) -> tuple[torch.Tensor, torch.Tensor, list[str], list[str]]:
    rows: list[list[float]] = []
    labels: list[int] = []
    kept_market_ids: list[str] = []
    feature_names: list[str] = []

    for market in loaded_markets:
        market_id = str(market["id"])
        trades = market_id_to_trades.get(market_id, [])
        feature_map = extract_market_features(
            market,
            trades,
            vwap_window=vwap_window,
            whale_top_k=whale_top_k,
        )

        if not feature_map:
            continue

        if not feature_names:
            feature_names = list(feature_map.keys())
        elif feature_names != list(feature_map.keys()):
            raise ValueError("Feature key order mismatch across markets.")

        rows.append([float(feature_map[name]) for name in feature_names])
        labels.append(1 if str(market["outcome"]).lower() == "yes" else 0)
        kept_market_ids.append(market_id)

    if not rows:
        raise ValueError("No valid market rows were generated for tabular features.")

    X = torch.tensor(rows, dtype=torch.float32)
    y = torch.tensor(labels, dtype=torch.long).unsqueeze(1)
    return X, y, feature_names, kept_market_ids


def split_and_scale_tabular_dataset(
    X: torch.Tensor,
    y: torch.Tensor,
    *,
    val_ratio: float,
    seed: int,
) -> tuple[torch.Tensor, torch.Tensor, torch.Tensor, torch.Tensor, dict[str, torch.Tensor]]:
    if X.ndim != 2:
        raise ValueError("X must have shape (num_markets, num_features).")
    if y.ndim != 2 or y.shape[1] != 1:
        raise ValueError("y must have shape (num_markets, 1).")
    if X.shape[0] != y.shape[0]:
        raise ValueError("X and y must have the same first dimension.")
    if not (0.0 < val_ratio < 1.0):
        raise ValueError("val_ratio must be in (0, 1).")
    if X.shape[0] < 2:
        raise ValueError("Need at least 2 samples to split into train/val.")

    num_samples = X.shape[0]
    generator = torch.Generator().manual_seed(seed)
    permutation = torch.randperm(num_samples, generator=generator)

    train_size = int((1.0 - val_ratio) * num_samples)
    train_size = max(1, min(train_size, num_samples - 1))

    train_indices = permutation[:train_size]
    val_indices = permutation[train_size:]

    X_train_raw = X[train_indices]
    y_train = y[train_indices]
    X_val_raw = X[val_indices]
    y_val = y[val_indices]

    mean = X_train_raw.mean(dim=0)
    std = X_train_raw.std(dim=0, unbiased=False)
    safe_std = torch.where(std > 0, std, torch.ones_like(std))

    X_train = (X_train_raw - mean) / safe_std
    X_val = (X_val_raw - mean) / safe_std

    scaler_stats = {
        "mean": mean,
        "std": safe_std,
        "train_indices": train_indices,
        "val_indices": val_indices,
        "X_train_raw": X_train_raw,
        "X_val_raw": X_val_raw,
    }
    return X_train, y_train, X_val, y_val, scaler_stats


def prepare_tabular_dataset(
    mapped_market_folder_path: Path,
    *,
    truncate_and_keep_ratio: float,
    market_policy: Callable[[dict[str, Any]], bool] | None = None,
    val_ratio: float,
    vwap_window: int,
    whale_top_k: int,
    seed: int,
) -> tuple[
    torch.Tensor,
    torch.Tensor,
    torch.Tensor,
    torch.Tensor,
    list[str],
    list[str],
    dict[str, torch.Tensor],
]:
    if market_policy is None:
        loaded_markets, loaded_market_id_to_trades, total_market_folders = load_filtered_markets_with_trades(
            mapped_market_folder_path,
            truncate_and_keep_ratio,
        )
    else:
        loaded_markets, loaded_market_id_to_trades, total_market_folders = load_filtered_markets_with_trades(
            mapped_market_folder_path,
            truncate_and_keep_ratio,
            market_policy=market_policy,
        )
    print(
        f"Loaded {len(loaded_markets)} markets after filtering from {total_market_folders} market folders."
    )

    X, y, feature_names, kept_market_ids = build_tabular_feature_matrix(
        loaded_markets,
        loaded_market_id_to_trades,
        vwap_window=vwap_window,
        whale_top_k=whale_top_k,
    )

    X_train, y_train, X_val, y_val, scaler_stats = split_and_scale_tabular_dataset(
        X,
        y,
        val_ratio=val_ratio,
        seed=seed,
    )
    return X_train, y_train, X_val, y_val, feature_names, kept_market_ids, scaler_stats


def run_tabular_experiment_on_ratio(
    mapped_market_folder_path: Path,
    truncate_and_keep_ratio: float,
    *,
    preset: str,
    market_policy: Callable[[dict[str, Any]], bool] | None = None,
    val_ratio: float = 0.2,
    vwap_window: int = 4,
    whale_top_k: int = 10,
    seed: int = 42,
    roc_output_dir: Path,
    confusion_matrix_output_dir: Path | None = None,
) -> RunResult:
    if confusion_matrix_output_dir is None:
        confusion_matrix_output_dir = roc_output_dir.parent.parent / "confusion_matrix" / "tabular"

    X_train, y_train, X_val, y_val, feature_names, _kept_market_ids, scaler_stats = prepare_tabular_dataset(
        mapped_market_folder_path,
        truncate_and_keep_ratio=truncate_and_keep_ratio,
        market_policy=market_policy,
        val_ratio=val_ratio,
        vwap_window=vwap_window,
        whale_top_k=whale_top_k,
        seed=seed,
    )

    print(
        f"Prepared tabular data for ratio={truncate_and_keep_ratio:.2f}. "
        f"X_train={tuple(X_train.shape)}, X_val={tuple(X_val.shape)}, features={len(feature_names)}"
    )

    model = XGBClassifier(**XGB_PARAMS)
    model.fit(X_train.detach().cpu().numpy(), y_train.detach().cpu().squeeze(1).numpy())

    y_prob_train = model.predict_proba(X_train.detach().cpu().numpy())[:, 1].tolist()
    y_prob_val = model.predict_proba(X_val.detach().cpu().numpy())[:, 1].tolist()

    train_metrics = evaluate_binary_metrics(
        y_train,
        y_prob_train,
        classification_threshold=CLASSIFICATION_THRESHOLD,
    )
    val_metrics = evaluate_binary_metrics(
        y_val,
        y_prob_val,
        classification_threshold=CLASSIFICATION_THRESHOLD,
    )

    if REFERENCE_PRICE_FEATURE not in feature_names:
        raise ValueError(f"{REFERENCE_PRICE_FEATURE} not found in feature names.")

    ref_index = feature_names.index(REFERENCE_PRICE_FEATURE)
    X_val_raw = scaler_stats["X_val_raw"]
    reference_prices = [float(value) for value in X_val_raw[:, ref_index].detach().cpu().tolist()]
    average_margin_of_victory = calculate_average_margin_of_victory(y_prob_val, reference_prices)

    roc_file_name = f"{preset}_ratio_{truncate_and_keep_ratio:.2f}.png"
    roc_plot_path = save_roc_plot(
        output_path=roc_output_dir / roc_file_name,
        title=f"Tabular ROC (preset={preset}, ratio={truncate_and_keep_ratio:.2f})",
        roc_fpr=val_metrics.roc_fpr,
        roc_tpr=val_metrics.roc_tpr,
        auc=val_metrics.auc,
        dpi=300,
    )

    y_true_train = [int(value) for value in y_train.detach().cpu().squeeze(1).tolist()]
    y_true_val = [int(value) for value in y_val.detach().cpu().squeeze(1).tolist()]
    y_pred_train = [1 if probability >= CLASSIFICATION_THRESHOLD else 0 for probability in y_prob_train]
    y_pred_val = [1 if probability >= CLASSIFICATION_THRESHOLD else 0 for probability in y_prob_val]

    train_confusion_matrix_file_name = f"{preset}_ratio_{truncate_and_keep_ratio:.2f}_train.png"
    val_confusion_matrix_file_name = f"{preset}_ratio_{truncate_and_keep_ratio:.2f}_val.png"
    train_confusion_matrix_plot_path = save_confusion_matrix_plot(
        output_path=confusion_matrix_output_dir / train_confusion_matrix_file_name,
        title=f"Tabular Train Confusion Matrix (preset={preset}, ratio={truncate_and_keep_ratio:.2f})",
        y_true=y_true_train,
        y_pred=y_pred_train,
        dpi=300,
    )
    val_confusion_matrix_plot_path = save_confusion_matrix_plot(
        output_path=confusion_matrix_output_dir / val_confusion_matrix_file_name,
        title=f"Tabular Val Confusion Matrix (preset={preset}, ratio={truncate_and_keep_ratio:.2f})",
        y_true=y_true_val,
        y_pred=y_pred_val,
        dpi=300,
    )

    return RunResult(
        preset=preset,
        strategy="tabular",
        truncate_and_keep_ratio=truncate_and_keep_ratio,
        desired_num_candlesticks=None,
        train_metrics=train_metrics,
        val_metrics=val_metrics,
        average_margin_of_victory=average_margin_of_victory,
        roc_plot_path=roc_plot_path,
        train_confusion_matrix_plot_path=train_confusion_matrix_plot_path,
        val_confusion_matrix_plot_path=val_confusion_matrix_plot_path,
    )
