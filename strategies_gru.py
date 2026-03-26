import csv
import json

from copy import deepcopy
from dataclasses import dataclass
from typing import Any
from pathlib import Path

import torch
import torch.nn as nn

MAPPED_MARKETS_FOLDER_PATH = Path("mapped_markets")
DESIRED_NUM_CANDLESTICKS = 40
TRUNCATE_AND_KEEP_RATIO = 0.33
VAL_RATIO = 0.2

@dataclass
class CandleStick:
    open_price: float
    close_price: float
    low_price: float
    high_price: float
    total_volume: float
    weighted_average_price: float

def market_filter_policy(market: dict[str, Any]) -> bool:
        """
        Define the market filter policy for markets to be visualized.
        Args:
            market: A dictionary containing the market metadata.
        Returns:
            A boolean indicating whether the market should be visualized based on the defined criteria.
        """
        return market["yes_trade_count"] > 500
    
def trade_filter_policy(trade: dict[str, Any]) -> bool:
    """
    Define the trade filter policy for trades to be visualized.
    Args:
        trade: A dictionary containing trade information, which should include "side", "price", and "total_usdc" keys.
    Returns:
        A boolean indicating whether the market should be visualized based on the defined criteria.
    """
    return trade["side"] == "BUY" and float(trade["price"]) < 0.98 and float(trade["total_usdc"]) > 2.0

def load_market_and_trades(market_folder: Path, truncate_and_keep_ratio: float) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    """
    Load the market metadata and (filtered) yes trades from the specified market folder.
    Args:
        market_folder: The Path object representing the folder of the market, which should contain "metadata.json" and "yes.csv" files.
        truncate_and_keep_ratio: The ratio of trades to be kept after truncating the trades list. For example, if truncate_and_keep_ratio is 0.5, only the first 50% of the trades will be kept after filtering with trade_filter_policy.
    Returns
        A tuple containing the market metadata dictionary and a list of yes trade dictionaries.
    """
    market_metadata_path = market_folder / "metadata.json"
    with open(market_metadata_path, "r", encoding="utf-8") as f:
        market = json.load(f)

    yes_trades_path = market_folder / "yes.csv"
    yes_trades = []
    with open(yes_trades_path, "r", encoding="utf-8") as csvfile:
        csvreader = csv.DictReader(csvfile)
        for row in csvreader:
            if trade_filter_policy(row):
                yes_trades.append(row)

    truncate_length = int(len(yes_trades) * truncate_and_keep_ratio)
    yes_trades = yes_trades[:truncate_length]

    return market, yes_trades


def get_candlestick_data_from_trades(trades: list[dict[str, Any]], interval_trade: int) -> list[CandleStick]:
    """
    Get the candlestick data from the list of trades based on the specified interval.
    Args:
        trades: A list of trade dictionaries.
        interval_trade: The number of trades to be included in each candlestick.
    Returns:
        A list of CandleStick objects representing the candlestick data.
    """
    candlesticks = []
    for i in range(0, len(trades), interval_trade):
        interval_trades = trades[i:i+interval_trade]
        if not interval_trades:
            continue
        open_price = float(interval_trades[0]["price"])
        close_price = float(interval_trades[-1]["price"])
        low_price = min(float(trade["price"]) for trade in interval_trades)
        high_price = max(float(trade["price"]) for trade in interval_trades)
        total_volume = sum(float(trade["total_usdc"]) for trade in interval_trades)

        if total_volume <= 0:
            raise ValueError("Total volume must be greater than 0 to calculate weighted average price.")
        weighted_average_price = sum(float(trade["price"]) * float(trade["total_usdc"]) for trade in interval_trades) / total_volume
        candlestick = CandleStick(
            open_price=open_price,
            close_price=close_price,
            low_price=low_price,
            high_price=high_price,
            total_volume=total_volume,
            weighted_average_price=weighted_average_price
        )
        candlesticks.append(candlestick)

    return candlesticks


def get_expected_candlestick_interval(num_trades: int, desired_num_candlesticks: int) -> int:
    """
    Get the expected candlestick interval based on the total number of trades and the desired number of candlesticks.
    Args:
        num_trades: The total number of trades.
        desired_num_candlesticks: The desired number of candlesticks to be generated.
    """
    return max(1, num_trades // desired_num_candlesticks)


def prepare_data_for_gru_training(loaded_markets: list[dict[str, Any]], loaded_market_id_to_candlestick_data: dict[str, list[CandleStick]], val_ratio: float) -> tuple[torch.Tensor, torch.Tensor, torch.Tensor, torch.Tensor]:
    """
    Prepare X data (markets x num_candlesticks x features) and y data (markets x 1) for GRU model training. The features for each candlestick are include open_price, close_price, low_price, high_price, total_volume(normalized 0~1 for each market), and weighted_average_price. The label is the market outcome: 1 for "yes" and 0 for "no". The GRU model will be trained to predict the market outcome based on the candlestick data.
    Args:
        loaded_markets: A list of market metadata dictionaries that have been loaded and filtered based on the market_filter_policy.
        loaded_market_id_to_candlestick_data: A dictionary mapping market IDs to their corresponding list of CandleStick data.
        val_ratio: The ratio of the dataset to be used for validation. The training will be performed on (1 - val_ratio) of the data, and the remaining val_ratio of the data will be used for validation.
    Returns:
        A tuple containing the training X tensor, training y tensor, validation X tensor, and validation y tensor.
    """
    X = []
    y = []
    for market in loaded_markets:
        market_id = market["id"]
        candlestick_data = loaded_market_id_to_candlestick_data[market_id]
        market_X = []
        for candlestick in candlestick_data:
            market_X.append([
                candlestick.open_price,
                candlestick.close_price,
                candlestick.low_price,
                candlestick.high_price,
                candlestick.total_volume,
                candlestick.weighted_average_price
            ])
        X.append(market_X)
        y.append(1 if market["outcome"] == "yes" else 0)

    # truncate the candlestick data to the minimum length among all markets to ensure the same shape for X tensor
    min_candlestick_length = min(len(market_X) for market_X in X)
    X = [market_X[:min_candlestick_length] for market_X in X]
    X_tensor = torch.tensor(X, dtype=torch.float32)
    
    # normalize total_volume for each market
    for i in range(X_tensor.shape[0]):
        total_volume = X_tensor[i, :, 4]
        max_volume = torch.max(total_volume)
        min_volume = torch.min(total_volume)
        if max_volume < min_volume:
            raise ValueError("max_volume should be greater than or equal to min_volume for normalization.")
        X_tensor[i, :, 4] = (total_volume - min_volume) / (max_volume - min_volume) 
    
    y_tensor = torch.tensor(y, dtype=torch.long).unsqueeze(1)
    
    train_size = int((1 - val_ratio) * X_tensor.shape[0])
    X_train, y_train = X_tensor[:train_size], y_tensor[:train_size]
    X_val, y_val = X_tensor[train_size:], y_tensor[train_size:]

    return X_train, y_train, X_val, y_val


def gru_training(X_train: torch.Tensor, y_train: torch.Tensor, X_val: torch.Tensor, y_val: torch.Tensor) -> tuple[torch.nn.Module, torch.nn.Module]:
    """
    Train a GRU model to predict the market outcome based on the candlestick data.
    Args:
        X_train: The training X tensor with shape (num_markets x num_candlesticks x num_features).
        y_train: The training y tensor with shape (num_markets x 1).
        X_val: The validation X tensor with shape (num_markets x num_candlesticks x num_features).
        y_val: The validation y tensor with shape (num_markets x 1).
    Returns:
        The trained GRU model and the linear layer used for output.
    """
    feature_size = X_train.shape[2]
    hidden_size = 64
    num_layers = 2
    output_size = 1
    gru_model = nn.GRU(input_size=feature_size, hidden_size=hidden_size, num_layers=num_layers, batch_first=True)
    linear_layer = nn.Linear(hidden_size, output_size)
    criterion = nn.BCEWithLogitsLoss()
    optimizer = torch.optim.Adam(list(gru_model.parameters()) + list(linear_layer.parameters()), lr=0.001)
    num_epochs = 100

    best_gru_model_state = gru_model.state_dict()
    best_linear_layer_state = linear_layer.state_dict()
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
        if (epoch + 1) % 10 == 0:
            # show train acc
            predicted = (torch.sigmoid(logits) > 0.5).long()
            correct = (predicted == y_train).sum().item()
            total = y_train.size(0)    
            # show val acc
            gru_model.eval()
            with torch.no_grad():
                val_output, _ = gru_model(X_val)
                val_last_hidden_state = val_output[:, -1, :]
                val_logits = linear_layer(val_last_hidden_state)
                val_predicted = (torch.sigmoid(val_logits) > 0.5).long()
                val_correct = (val_predicted == y_val).sum().item()
                val_total = y_val.size(0)

                val_accuracy = val_correct / val_total
                if val_accuracy > best_val_accuracy:
                    best_val_accuracy = val_accuracy
                    best_gru_model_state = deepcopy(gru_model.state_dict())
                    best_linear_layer_state = deepcopy(linear_layer.state_dict())
            
            print(f"Epoch [{epoch+1}/{num_epochs}], Loss: {loss.item():.4f}, Train Acc: {correct/total:.4f}, Val Acc: {val_correct/val_total:.4f}")    

    print(f"Loading best model state with Val Accuracy: {best_val_accuracy:.4f}")
    gru_model.load_state_dict(best_gru_model_state), linear_layer.load_state_dict(best_linear_layer_state)

    return gru_model, linear_layer


def calculate_margin_of_victory(gru_model: torch.nn.Module, linear_layer: torch.nn.Module, X: torch.Tensor, y: torch.Tensor) -> float:
    """
    Calculate the margin of victory for the validation markets based on the trained GRU model. The margin of victory is defined as the difference between the predicted probability of the winning outcome and the predicted probability of the losing outcome, weighted by the weighted average price of the last candlestick. A higher margin of victory indicates a stronger confidence in the prediction and a potentially more profitable trade.
    If the weighted average price of the last candlestick is 0.95, that means the winning margin is 1-0.95=0.05, and if the GRU model predicts the winning outcome with a probability of 0.9, that means the expected margin of victory is 0.9 * 0.05 = 0.045 and the loss will be 0.1 * 0.95 = 0.095, so the net margin of victory will be 0.045 - 0.095 = -0.05, which means it's not a good trade. On the other hand, if the GRU model predicts the winning outcome with a probability of 0.99, that means the expected margin of victory is 0.99 * 0.05 = 0.0495 and the loss will be 0.01 * 0.95 = 0.0095, so the net margin of victory will be 0.0495 - 0.0095 = 0.04, which means it's a good trade.
    Args:
        gru_model: The trained GRU model.
        linear_layer: The linear layer used for output in the GRU model.
        X: The validation X tensor with shape (num_markets x num_candlesticks x num_features).
        y: The validation y tensor with shape (num_markets x 1).
    Returns:
        The average margin of victory for the validation markets. if the result is 0.01, that means on average, the expected margin of victory for the validation markets is 1%, which indicates a potentially profitable trading strategy based on the GRU model's predictions.
    """
    gru_model.eval()
    with torch.no_grad():
        output, _ = gru_model(X)
        last_hidden_state = output[:, -1, :]
        logits = linear_layer(last_hidden_state)
        probabilities = torch.sigmoid(logits).squeeze(1)
        predicted_outcomes = (probabilities > 0.5).long()
        correct_predictions = (predicted_outcomes == y.squeeze(1)).sum().item()
        total_predictions = y.size(0)
        accuracy = correct_predictions / total_predictions
        print(f"Validation Accuracy for Margin of Victory Calculation: {accuracy:.4f}")

        # calculate margin of victory
        margin_of_victory = 0.0
        for i in range(X.size(0)):
            last_candlestick_weighted_average_price = X[i, -1, 5].item()
            winning_margin = 1.0 - last_candlestick_weighted_average_price
            expected_margin_of_victory = probabilities[i].item() * winning_margin
            expected_loss = (1 - probabilities[i].item()) * last_candlestick_weighted_average_price
            net_margin_of_victory = expected_margin_of_victory - expected_loss
            margin_of_victory += net_margin_of_victory
        average_margin_of_victory = margin_of_victory / X.size(0)
        print(f"Average Margin of Victory: {average_margin_of_victory:.4f}")
    
    return average_margin_of_victory


def calculate_margin_on_specific_truncate_and_keep_ratio(mapped_market_folder_path: Path, truncate_and_keep_ratio: float) -> float:
    """
    Calculate the margin of victory for a specific truncate_and_keep_ratio. This function is used to find the optimal truncate_and_keep_ratio that can achieve a good balance between winning rate and margin of victory.
    Args:
        mapped_market_folder_path: The Path object representing the folder containing the mapped markets data.
        truncate_and_keep_ratio: The ratio of trades to be kept after truncating the trades list. For example, if truncate_and_keep_ratio is 0.5, only the first 50% of the trades will be kept after filtering with trade_filter_policy.
    Returns:
        The average margin of victory for the validation markets based on the specified truncate_and_keep_ratio.
    """
    loaded_markets = []
    loaded_market_id_to_trades = {}
    original_market_folders = list(mapped_market_folder_path.iterdir())
    for market_folder in original_market_folders:
        if market_folder.is_dir():
            market, yes_trades = load_market_and_trades(market_folder, truncate_and_keep_ratio)
            if market_filter_policy(market):
                loaded_markets.append(market)
                loaded_market_id_to_trades[market["id"]] = yes_trades
    print(f"Loaded {len(loaded_markets)} markets after filtering with market_filter_policy from {len(original_market_folders)} original market folders.")
    
    loaded_market_id_to_candlestick_data = {}
    for market in loaded_markets:
        trades = loaded_market_id_to_trades[market["id"]]
        interval_trade = get_expected_candlestick_interval(len(trades), DESIRED_NUM_CANDLESTICKS)
        loaded_market_id_to_candlestick_data[market["id"]] = get_candlestick_data_from_trades(trades, interval_trade)
        print(f"Market ID: {market['id']} has {len(trades)} trades, using interval_trade={interval_trade} to get candlestick data.")

    X_train, y_train, X_val, y_val = prepare_data_for_gru_training(loaded_markets, loaded_market_id_to_candlestick_data, VAL_RATIO)
    print(f"Prepared data for GRU training. X_train shape: {X_train.shape}, y_train shape: {y_train.shape}, X_val shape: {X_val.shape}, y_val shape: {y_val.shape}.")

    gru_model, linear_layer = gru_training(X_train, y_train, X_val, y_val)

    # calculate the actual margin of victory for each market with the trained GRU model, for those validation markets, we can use 1. predicted results 2. weighted_average_price 3. Actual outcome to calculate the margin of victory. The reasonable result is when we truncate the trades with a larger truncate_and_keep_ratio, the winning rate will be higher but the smaller the margin of victory will be, and when we truncate the trades with a smaller truncate_and_keep_ratio, the winning rate will be lower but the larger the margin of victory will be. So the concept is to find a good balance between winning rate and margin of victory by tuning the truncate_and_keep_ratio.
    margin_of_victory = calculate_margin_of_victory(gru_model, linear_layer, X_val, y_val)
    return margin_of_victory

if __name__ == "__main__":
    truncate_and_keep_ratios = [0.33, 0.5, 0.67, 0.8, 0.95]
    for truncate_and_keep_ratio in truncate_and_keep_ratios:
        print(f"Calculating margin of victory for truncate_and_keep_ratio={truncate_and_keep_ratio}...")
        margin_of_victory = calculate_margin_on_specific_truncate_and_keep_ratio(MAPPED_MARKETS_FOLDER_PATH, truncate_and_keep_ratio)
        print(f"Margin of Victory for truncate_and_keep_ratio={truncate_and_keep_ratio}: {margin_of_victory:.4f}")
    
