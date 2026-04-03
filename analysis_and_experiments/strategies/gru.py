from copy import deepcopy
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Callable

import torch
import torch.nn as nn
from sklearn.model_selection import StratifiedKFold

from analysis_and_experiments.data import load_filtered_markets_with_trades
from analysis_and_experiments.evaluation import (
    calculate_average_margin_of_victory,
    evaluate_binary_metrics,
)
from analysis_and_experiments.plotting import (
    save_confusion_matrix_plot,
    save_train_val_metric_plot,
    save_roc_plot,
)
from analysis_and_experiments.strategies.common import (
    FoldResult,
    RunResult,
    average_binary_metrics,
)

CLASSIFICATION_THRESHOLD = 0.5


@dataclass
class CandleStick:
    open_price: float
    close_price: float
    low_price: float
    high_price: float
    total_volume: float
    weighted_average_price: float


@dataclass
class GRUTrainingHistory:
    train_loss: list[float]
    train_accuracy: list[float]
    val_loss: list[float]
    val_accuracy: list[float]


def get_candlestick_data_from_trades(
    trades: list[dict[str, Any]],
    interval_trade: int,
) -> list[CandleStick]:
    candlesticks: list[CandleStick] = []
    for start_index in range(0, len(trades), interval_trade):
        interval_trades = trades[start_index : start_index + interval_trade]
        if not interval_trades:
            continue

        open_price = float(interval_trades[0]["price"])
        close_price = float(interval_trades[-1]["price"])
        low_price = min(float(trade["price"]) for trade in interval_trades)
        high_price = max(float(trade["price"]) for trade in interval_trades)
        total_volume = sum(float(trade["total_usdc"]) for trade in interval_trades)
        if total_volume <= 0:
            raise ValueError("Total volume must be > 0 to calculate weighted_average_price.")

        weighted_average_price = (
            sum(float(trade["price"]) * float(trade["total_usdc"]) for trade in interval_trades)
            / total_volume
        )
        candlesticks.append(
            CandleStick(
                open_price=open_price,
                close_price=close_price,
                low_price=low_price,
                high_price=high_price,
                total_volume=total_volume,
                weighted_average_price=weighted_average_price,
            )
        )
    return candlesticks


def get_expected_candlestick_interval(num_trades: int, desired_num_candlesticks: int) -> int:
    return max(1, num_trades // desired_num_candlesticks)


def build_gru_dataset(
    loaded_markets: list[dict[str, Any]],
    market_id_to_candlestick_data: dict[str, list[CandleStick]],
) -> tuple[torch.Tensor, torch.Tensor]:
    X: list[list[list[float]]] = []
    y: list[int] = []
    for market in loaded_markets:
        market_id = str(market["id"])
        candlestick_data = market_id_to_candlestick_data[market_id]
        market_X = [
            [
                candlestick.open_price,
                candlestick.close_price,
                candlestick.low_price,
                candlestick.high_price,
                candlestick.total_volume,
                candlestick.weighted_average_price,
            ]
            for candlestick in candlestick_data
        ]
        X.append(market_X)
        y.append(1 if str(market.get("outcome", "")).lower() == "yes" else 0)

    min_candlestick_length = min(len(market_X) for market_X in X)
    X = [market_X[:min_candlestick_length] for market_X in X]
    X_tensor = torch.tensor(X, dtype=torch.float32)

    # Normalize volume feature market-by-market.
    for sample_index in range(X_tensor.shape[0]):
        total_volume = X_tensor[sample_index, :, 4]
        max_volume = torch.max(total_volume)
        min_volume = torch.min(total_volume)
        if max_volume == min_volume:
            X_tensor[sample_index, :, 4] = 0.0
        else:
            X_tensor[sample_index, :, 4] = (total_volume - min_volume) / (max_volume - min_volume)

    y_tensor = torch.tensor(y, dtype=torch.long).unsqueeze(1)
    return X_tensor, y_tensor


def _split_by_indices(
    X: torch.Tensor,
    y: torch.Tensor,
    train_indices: torch.Tensor,
    val_indices: torch.Tensor,
) -> tuple[torch.Tensor, torch.Tensor, torch.Tensor, torch.Tensor]:
    X_train = X[train_indices]
    y_train = y[train_indices]
    X_val = X[val_indices]
    y_val = y[val_indices]
    return X_train, y_train, X_val, y_val


def prepare_data_for_gru_training(
    loaded_markets: list[dict[str, Any]],
    market_id_to_candlestick_data: dict[str, list[CandleStick]],
    *,
    val_ratio: float,
    seed: int,
) -> tuple[torch.Tensor, torch.Tensor, torch.Tensor, torch.Tensor]:
    X_tensor, y_tensor = build_gru_dataset(
        loaded_markets,
        market_id_to_candlestick_data,
    )

    generator = torch.Generator().manual_seed(seed)
    shuffled_indices = torch.randperm(X_tensor.shape[0], generator=generator)
    X_shuffled = X_tensor[shuffled_indices]
    y_shuffled = y_tensor[shuffled_indices]

    train_size = int((1 - val_ratio) * X_shuffled.shape[0])
    if train_size <= 0 or train_size >= X_shuffled.shape[0]:
        raise ValueError(
            f"Invalid split with val_ratio={val_ratio} for dataset size={X_shuffled.shape[0]}."
        )

    X_train, y_train = X_shuffled[:train_size], y_shuffled[:train_size]
    X_val, y_val = X_shuffled[train_size:], y_shuffled[train_size:]
    return X_train, y_train, X_val, y_val


def gru_training(
    X_train: torch.Tensor,
    y_train: torch.Tensor,
    X_val: torch.Tensor,
    y_val: torch.Tensor,
    *,
    seed: int,
) -> tuple[nn.GRU, nn.Linear, GRUTrainingHistory]:
    torch.manual_seed(seed)

    feature_size = X_train.shape[2]
    hidden_size = 32
    num_layers = 2
    output_size = 1

    gru_model = nn.GRU(
        input_size=feature_size,
        hidden_size=hidden_size,
        num_layers=num_layers,
        batch_first=True,
    )
    linear_layer = nn.Linear(hidden_size, output_size)

    criterion = nn.BCEWithLogitsLoss()
    optimizer = torch.optim.Adam(list(gru_model.parameters()) + list(linear_layer.parameters()), lr=0.001)
    num_epochs = 200

    best_gru_model_state = deepcopy(gru_model.state_dict())
    best_linear_layer_state = deepcopy(linear_layer.state_dict())
    best_val_accuracy = 0.0
    train_loss_history: list[float] = []
    train_accuracy_history: list[float] = []
    val_loss_history: list[float] = []
    val_accuracy_history: list[float] = []

    for epoch in range(num_epochs):
        gru_model.train()
        optimizer.zero_grad()
        output, _ = gru_model(X_train)
        last_hidden_state = output[:, -1, :]
        logits = linear_layer(last_hidden_state)
        loss = criterion(logits, y_train.float())
        loss.backward()
        optimizer.step()

        predicted = (torch.sigmoid(logits) > CLASSIFICATION_THRESHOLD).long()
        train_correct = (predicted == y_train).sum().item()
        train_total = y_train.size(0)
        train_loss = float(loss.item())
        train_accuracy = float(train_correct / train_total)

        gru_model.eval()
        with torch.no_grad():
            val_output, _ = gru_model(X_val)
            val_last_hidden_state = val_output[:, -1, :]
            val_logits = linear_layer(val_last_hidden_state)
            val_loss = float(criterion(val_logits, y_val.float()).item())
            val_predicted = (torch.sigmoid(val_logits) > CLASSIFICATION_THRESHOLD).long()
            val_correct = (val_predicted == y_val).sum().item()
            val_total = y_val.size(0)
            val_accuracy = val_correct / val_total

        train_loss_history.append(train_loss)
        train_accuracy_history.append(train_accuracy)
        val_loss_history.append(val_loss)
        val_accuracy_history.append(float(val_accuracy))

        if val_accuracy > best_val_accuracy:
            best_val_accuracy = val_accuracy
            best_gru_model_state = deepcopy(gru_model.state_dict())
            best_linear_layer_state = deepcopy(linear_layer.state_dict())

        if (epoch + 1) % 10 == 0:
            print(
                f"Epoch [{epoch + 1}/{num_epochs}], "
                f"Train Loss: {train_loss:.4f}, Train Acc: {train_accuracy:.4f}, "
                f"Val Loss: {val_loss:.4f}, Val Acc: {val_correct / val_total:.4f}"
            )

    print(f"Loading best model state with Val Accuracy: {best_val_accuracy:.4f}")
    gru_model.load_state_dict(best_gru_model_state)
    linear_layer.load_state_dict(best_linear_layer_state)
    return (
        gru_model,
        linear_layer,
        GRUTrainingHistory(
            train_loss=train_loss_history,
            train_accuracy=train_accuracy_history,
            val_loss=val_loss_history,
            val_accuracy=val_accuracy_history,
        ),
    )


def _predict_probabilities(gru_model: nn.Module, linear_layer: nn.Module, X: torch.Tensor) -> list[float]:
    gru_model.eval()
    with torch.no_grad():
        output, _ = gru_model(X)
        last_hidden_state = output[:, -1, :]
        logits = linear_layer(last_hidden_state)
        probabilities = torch.sigmoid(logits).squeeze(1).detach().cpu().numpy().tolist()
        return [float(value) for value in probabilities]


def _validate_cv_folds(y: torch.Tensor, cv_folds: int) -> None:
    if cv_folds < 2:
        raise ValueError(f"cv_folds must be >= 2 when CV is enabled, got {cv_folds}.")

    labels = y.detach().cpu().squeeze(1)
    class_counts = torch.bincount(labels, minlength=2)
    min_class_count = int(torch.min(class_counts).item())
    if min_class_count < cv_folds:
        raise ValueError(
            "Invalid cv_folds: smallest class count is "
            f"{min_class_count}, but cv_folds={cv_folds}. "
            "Reduce --cv-folds or disable CV."
        )


def _average_histories(histories: list[GRUTrainingHistory]) -> GRUTrainingHistory:
    if not histories:
        raise ValueError("histories cannot be empty.")

    num_epochs = len(histories[0].train_loss)
    for history in histories:
        if len(history.train_loss) != num_epochs:
            raise ValueError("All history objects must share the same train_loss length.")
        if len(history.train_accuracy) != num_epochs:
            raise ValueError("All history objects must share the same train_accuracy length.")
        if len(history.val_loss) != num_epochs:
            raise ValueError("All history objects must share the same val_loss length.")
        if len(history.val_accuracy) != num_epochs:
            raise ValueError("All history objects must share the same val_accuracy length.")

    return GRUTrainingHistory(
        train_loss=[
            float(sum(history.train_loss[epoch] for history in histories) / len(histories))
            for epoch in range(num_epochs)
        ],
        train_accuracy=[
            float(sum(history.train_accuracy[epoch] for history in histories) / len(histories))
            for epoch in range(num_epochs)
        ],
        val_loss=[
            float(sum(history.val_loss[epoch] for history in histories) / len(histories))
            for epoch in range(num_epochs)
        ],
        val_accuracy=[
            float(sum(history.val_accuracy[epoch] for history in histories) / len(histories))
            for epoch in range(num_epochs)
        ],
    )


def run_gru_experiment_on_ratio(
    mapped_market_folder_path: Path,
    truncate_and_keep_ratio: float,
    *,
    preset: str,
    desired_num_candlesticks: int = 40,
    market_policy: Callable[[dict[str, Any]], bool] | None = None,
    val_ratio: float = 0.2,
    seed: int = 42,
    use_cross_validation: bool = True,
    cv_folds: int = 5,
    roc_output_dir: Path,
    train_val_curves_output_dir: Path | None = None,
    confusion_matrix_output_dir: Path | None = None,
) -> RunResult:
    if train_val_curves_output_dir is None:
        train_val_curves_output_dir = roc_output_dir.parent.parent / "training_curves" / "gru"
    if confusion_matrix_output_dir is None:
        confusion_matrix_output_dir = roc_output_dir.parent.parent / "confusion_matrix" / "gru"

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

    loaded_market_id_to_candlestick_data: dict[str, list[CandleStick]] = {}
    for market in loaded_markets:
        market_id = str(market["id"])
        trades = loaded_market_id_to_trades[market_id]
        interval_trade = get_expected_candlestick_interval(len(trades), desired_num_candlesticks)
        loaded_market_id_to_candlestick_data[market_id] = get_candlestick_data_from_trades(
            trades,
            interval_trade,
        )

    X, y = build_gru_dataset(
        loaded_markets,
        loaded_market_id_to_candlestick_data,
    )

    fold_results: list[FoldResult] = []
    y_true_train: list[int]
    y_prob_train: list[float]
    y_true_val: list[int]
    y_prob_val: list[float]
    average_margin_of_victory: float
    training_history: GRUTrainingHistory
    train_metrics: Any
    val_metrics: Any

    if use_cross_validation:
        _validate_cv_folds(y, cv_folds)
        y_labels = y.detach().cpu().squeeze(1).numpy()
        splitter = StratifiedKFold(n_splits=cv_folds, shuffle=True, random_state=seed)

        fold_histories: list[GRUTrainingHistory] = []
        train_metrics_per_fold = []
        all_train_true: list[int] = []
        all_train_prob: list[float] = []
        all_val_true: list[int] = []
        all_val_prob: list[float] = []
        all_val_reference_prices: list[float] = []

        for fold_index, (train_idx_np, val_idx_np) in enumerate(
            splitter.split(X.detach().cpu().numpy(), y_labels),
            start=1,
        ):
            train_indices = torch.tensor(train_idx_np, dtype=torch.long)
            val_indices = torch.tensor(val_idx_np, dtype=torch.long)
            X_train, y_train_tensor, X_val, y_val_tensor = _split_by_indices(
                X,
                y,
                train_indices,
                val_indices,
            )

            print(
                f"Prepared GRU CV fold {fold_index}/{cv_folds} for ratio={truncate_and_keep_ratio:.2f}, "
                f"candles={desired_num_candlesticks}. X_train={tuple(X_train.shape)}, X_val={tuple(X_val.shape)}"
            )

            gru_model, linear_layer, fold_history = gru_training(
                X_train,
                y_train_tensor,
                X_val,
                y_val_tensor,
                seed=seed,
            )
            fold_histories.append(fold_history)

            fold_prob_train = _predict_probabilities(gru_model, linear_layer, X_train)
            fold_prob_val = _predict_probabilities(gru_model, linear_layer, X_val)

            fold_train_metrics = evaluate_binary_metrics(
                y_train_tensor,
                fold_prob_train,
                classification_threshold=CLASSIFICATION_THRESHOLD,
            )
            fold_val_metrics = evaluate_binary_metrics(
                y_val_tensor,
                fold_prob_val,
                classification_threshold=CLASSIFICATION_THRESHOLD,
            )
            train_metrics_per_fold.append(fold_train_metrics)

            fold_reference_prices = [float(value) for value in X_val[:, -1, 5].detach().cpu().tolist()]
            fold_margin = calculate_average_margin_of_victory(fold_prob_val, fold_reference_prices)

            fold_results.append(
                FoldResult(
                    fold_index=fold_index,
                    train_size=int(y_train_tensor.shape[0]),
                    val_size=int(y_val_tensor.shape[0]),
                    train_metrics=fold_train_metrics,
                    val_metrics=fold_val_metrics,
                    average_margin_of_victory=fold_margin,
                )
            )

            all_train_true.extend(
                int(value) for value in y_train_tensor.detach().cpu().squeeze(1).tolist()
            )
            all_train_prob.extend(fold_prob_train)
            all_val_true.extend(int(value) for value in y_val_tensor.detach().cpu().squeeze(1).tolist())
            all_val_prob.extend(fold_prob_val)
            all_val_reference_prices.extend(fold_reference_prices)

            print(
                f"GRU CV fold {fold_index}/{cv_folds} completed. "
                f"train={y_train_tensor.shape[0]}, val={y_val_tensor.shape[0]}"
            )

        y_true_train = all_train_true
        y_prob_train = all_train_prob
        y_true_val = all_val_true
        y_prob_val = all_val_prob
        average_margin_of_victory = calculate_average_margin_of_victory(
            all_val_prob,
            all_val_reference_prices,
        )

        training_history = _average_histories(fold_histories)
        train_metrics = average_binary_metrics(train_metrics_per_fold)
        val_metrics = evaluate_binary_metrics(
            torch.tensor(all_val_true, dtype=torch.long).unsqueeze(1),
            all_val_prob,
            classification_threshold=CLASSIFICATION_THRESHOLD,
        )
        file_suffix = f"_cv{cv_folds}"
        cv_enabled = True
        run_cv_folds: int | None = cv_folds
    else:
        X_train, y_train_tensor, X_val, y_val_tensor = prepare_data_for_gru_training(
            loaded_markets,
            loaded_market_id_to_candlestick_data,
            val_ratio=val_ratio,
            seed=seed,
        )
        print(
            f"Prepared GRU data for ratio={truncate_and_keep_ratio:.2f}, candles={desired_num_candlesticks}. "
            f"X_train={tuple(X_train.shape)}, X_val={tuple(X_val.shape)}"
        )

        gru_model, linear_layer, training_history = gru_training(
            X_train,
            y_train_tensor,
            X_val,
            y_val_tensor,
            seed=seed,
        )

        y_prob_train = _predict_probabilities(gru_model, linear_layer, X_train)
        y_prob_val = _predict_probabilities(gru_model, linear_layer, X_val)
        y_true_train = [int(value) for value in y_train_tensor.detach().cpu().squeeze(1).tolist()]
        y_true_val = [int(value) for value in y_val_tensor.detach().cpu().squeeze(1).tolist()]

        train_metrics = evaluate_binary_metrics(
            y_train_tensor,
            y_prob_train,
            classification_threshold=CLASSIFICATION_THRESHOLD,
        )
        val_metrics = evaluate_binary_metrics(
            y_val_tensor,
            y_prob_val,
            classification_threshold=CLASSIFICATION_THRESHOLD,
        )

        reference_prices = [float(value) for value in X_val[:, -1, 5].detach().cpu().tolist()]
        average_margin_of_victory = calculate_average_margin_of_victory(y_prob_val, reference_prices)
        fold_results = [
            FoldResult(
                fold_index=1,
                train_size=int(y_train_tensor.shape[0]),
                val_size=int(y_val_tensor.shape[0]),
                train_metrics=train_metrics,
                val_metrics=val_metrics,
                average_margin_of_victory=average_margin_of_victory,
            )
        ]
        file_suffix = ""
        cv_enabled = False
        run_cv_folds = None

    roc_file_name = (
        f"{preset}_ratio_{truncate_and_keep_ratio:.2f}_candles_{desired_num_candlesticks}{file_suffix}.png"
    )
    roc_plot_path = save_roc_plot(
        output_path=roc_output_dir / roc_file_name,
        title=(
            f"GRU ROC (preset={preset}, ratio={truncate_and_keep_ratio:.2f}, "
            f"candles={desired_num_candlesticks}, mode={'cv' if use_cross_validation else 'single'})"
        ),
        roc_fpr=val_metrics.roc_fpr,
        roc_tpr=val_metrics.roc_tpr,
        auc=val_metrics.auc,
        dpi=300,
    )

    curve_suffix = file_suffix
    loss_curve_file_name = (
        f"{preset}_ratio_{truncate_and_keep_ratio:.2f}_candles_{desired_num_candlesticks}{curve_suffix}_loss.png"
    )
    accuracy_curve_file_name = (
        f"{preset}_ratio_{truncate_and_keep_ratio:.2f}_candles_{desired_num_candlesticks}{curve_suffix}_accuracy.png"
    )
    loss_curve_plot_path = save_train_val_metric_plot(
        output_path=train_val_curves_output_dir / loss_curve_file_name,
        title=(
            f"GRU Train/Val Loss (preset={preset}, ratio={truncate_and_keep_ratio:.2f}, "
            f"candles={desired_num_candlesticks}, mode={'cv' if use_cross_validation else 'single'})"
        ),
        metric_name="Loss",
        train_values=training_history.train_loss,
        val_values=training_history.val_loss,
        dpi=300,
    )
    accuracy_curve_plot_path = save_train_val_metric_plot(
        output_path=train_val_curves_output_dir / accuracy_curve_file_name,
        title=(
            f"GRU Train/Val Accuracy (preset={preset}, ratio={truncate_and_keep_ratio:.2f}, "
            f"candles={desired_num_candlesticks}, mode={'cv' if use_cross_validation else 'single'})"
        ),
        metric_name="Accuracy",
        train_values=training_history.train_accuracy,
        val_values=training_history.val_accuracy,
        y_limit=(0.0, 1.0),
        dpi=300,
    )

    y_pred_train = [1 if probability >= CLASSIFICATION_THRESHOLD else 0 for probability in y_prob_train]
    y_pred_val = [1 if probability >= CLASSIFICATION_THRESHOLD else 0 for probability in y_prob_val]

    train_confusion_matrix_file_name = (
        f"{preset}_ratio_{truncate_and_keep_ratio:.2f}_candles_{desired_num_candlesticks}{file_suffix}_train.png"
    )
    val_confusion_matrix_file_name = (
        f"{preset}_ratio_{truncate_and_keep_ratio:.2f}_candles_{desired_num_candlesticks}{file_suffix}_val.png"
    )
    train_confusion_matrix_plot_path = save_confusion_matrix_plot(
        output_path=confusion_matrix_output_dir / train_confusion_matrix_file_name,
        title=(
            f"GRU Train Confusion Matrix (preset={preset}, ratio={truncate_and_keep_ratio:.2f}, "
            f"candles={desired_num_candlesticks}, mode={'cv' if use_cross_validation else 'single'})"
        ),
        y_true=y_true_train,
        y_pred=y_pred_train,
        dpi=300,
    )
    val_confusion_matrix_plot_path = save_confusion_matrix_plot(
        output_path=confusion_matrix_output_dir / val_confusion_matrix_file_name,
        title=(
            f"GRU Val Confusion Matrix (preset={preset}, ratio={truncate_and_keep_ratio:.2f}, "
            f"candles={desired_num_candlesticks}, mode={'cv' if use_cross_validation else 'single'})"
        ),
        y_true=y_true_val,
        y_pred=y_pred_val,
        dpi=300,
    )

    return RunResult(
        preset=preset,
        strategy="gru",
        truncate_and_keep_ratio=truncate_and_keep_ratio,
        desired_num_candlesticks=desired_num_candlesticks,
        cv_enabled=cv_enabled,
        cv_folds=run_cv_folds,
        train_metrics=train_metrics,
        val_metrics=val_metrics,
        average_margin_of_victory=average_margin_of_victory,
        fold_results=fold_results,
        roc_plot_path=roc_plot_path,
        gru_train_curve_plot_path=loss_curve_plot_path,
        gru_val_curve_plot_path=accuracy_curve_plot_path,
        train_confusion_matrix_plot_path=train_confusion_matrix_plot_path,
        val_confusion_matrix_plot_path=val_confusion_matrix_plot_path,
    )
