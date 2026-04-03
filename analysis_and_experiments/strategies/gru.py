from copy import deepcopy
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Callable

import torch
import torch.nn as nn

from analysis_and_experiments.data import load_filtered_markets_with_trades
from analysis_and_experiments.evaluation import (
    calculate_average_margin_of_victory,
    evaluate_binary_metrics,
)
from analysis_and_experiments.plotting import save_roc_plot
from analysis_and_experiments.strategies.common import RunResult

CLASSIFICATION_THRESHOLD = 0.5


@dataclass
class CandleStick:
    open_price: float
    close_price: float
    low_price: float
    high_price: float
    total_volume: float
    weighted_average_price: float


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


def prepare_data_for_gru_training(
    loaded_markets: list[dict[str, Any]],
    market_id_to_candlestick_data: dict[str, list[CandleStick]],
    *,
    val_ratio: float,
    seed: int,
) -> tuple[torch.Tensor, torch.Tensor, torch.Tensor, torch.Tensor]:
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
) -> tuple[nn.GRU, nn.Linear]:
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

        gru_model.eval()
        with torch.no_grad():
            val_output, _ = gru_model(X_val)
            val_last_hidden_state = val_output[:, -1, :]
            val_logits = linear_layer(val_last_hidden_state)
            val_predicted = (torch.sigmoid(val_logits) > CLASSIFICATION_THRESHOLD).long()
            val_correct = (val_predicted == y_val).sum().item()
            val_total = y_val.size(0)
            val_accuracy = val_correct / val_total

        if val_accuracy > best_val_accuracy:
            best_val_accuracy = val_accuracy
            best_gru_model_state = deepcopy(gru_model.state_dict())
            best_linear_layer_state = deepcopy(linear_layer.state_dict())

        if (epoch + 1) % 10 == 0:
            print(
                f"Epoch [{epoch + 1}/{num_epochs}], Loss: {loss.item():.4f}, "
                f"Train Acc: {train_correct / train_total:.4f}, Val Acc: {val_correct / val_total:.4f}"
            )

    print(f"Loading best model state with Val Accuracy: {best_val_accuracy:.4f}")
    gru_model.load_state_dict(best_gru_model_state)
    linear_layer.load_state_dict(best_linear_layer_state)
    return gru_model, linear_layer


def _predict_probabilities(gru_model: nn.Module, linear_layer: nn.Module, X: torch.Tensor) -> list[float]:
    gru_model.eval()
    with torch.no_grad():
        output, _ = gru_model(X)
        last_hidden_state = output[:, -1, :]
        logits = linear_layer(last_hidden_state)
        probabilities = torch.sigmoid(logits).squeeze(1).detach().cpu().numpy().tolist()
        return [float(value) for value in probabilities]


def run_gru_experiment_on_ratio(
    mapped_market_folder_path: Path,
    truncate_and_keep_ratio: float,
    *,
    preset: str,
    desired_num_candlesticks: int = 40,
    market_policy: Callable[[dict[str, Any]], bool] | None = None,
    val_ratio: float = 0.2,
    seed: int = 42,
    roc_output_dir: Path,
) -> RunResult:
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

    X_train, y_train, X_val, y_val = prepare_data_for_gru_training(
        loaded_markets,
        loaded_market_id_to_candlestick_data,
        val_ratio=val_ratio,
        seed=seed,
    )

    print(
        f"Prepared GRU data for ratio={truncate_and_keep_ratio:.2f}, candles={desired_num_candlesticks}. "
        f"X_train={tuple(X_train.shape)}, X_val={tuple(X_val.shape)}"
    )

    gru_model, linear_layer = gru_training(
        X_train,
        y_train,
        X_val,
        y_val,
        seed=seed,
    )

    y_prob_train = _predict_probabilities(gru_model, linear_layer, X_train)
    y_prob_val = _predict_probabilities(gru_model, linear_layer, X_val)

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

    reference_prices = [float(value) for value in X_val[:, -1, 5].detach().cpu().tolist()]
    average_margin_of_victory = calculate_average_margin_of_victory(y_prob_val, reference_prices)

    roc_file_name = (
        f"{preset}_ratio_{truncate_and_keep_ratio:.2f}_candles_{desired_num_candlesticks}.png"
    )
    roc_plot_path = save_roc_plot(
        output_path=roc_output_dir / roc_file_name,
        title=(
            f"GRU ROC (preset={preset}, ratio={truncate_and_keep_ratio:.2f}, "
            f"candles={desired_num_candlesticks})"
        ),
        roc_fpr=val_metrics.roc_fpr,
        roc_tpr=val_metrics.roc_tpr,
        auc=val_metrics.auc,
        dpi=300,
    )

    return RunResult(
        preset=preset,
        strategy="gru",
        truncate_and_keep_ratio=truncate_and_keep_ratio,
        desired_num_candlesticks=desired_num_candlesticks,
        train_metrics=train_metrics,
        val_metrics=val_metrics,
        average_margin_of_victory=average_margin_of_victory,
        roc_plot_path=roc_plot_path,
    )
