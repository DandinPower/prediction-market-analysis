import csv
import json
from pathlib import Path
from typing import Any, Callable

from .policies import market_filter_policy, trade_filter_policy

TradePolicy = Callable[[dict[str, Any]], bool]
MarketPolicy = Callable[[dict[str, Any]], bool]


def load_market_and_trades(
    market_folder: Path,
    truncate_and_keep_ratio: float,
    *,
    trade_policy: TradePolicy = trade_filter_policy,
) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    """Load market metadata and filtered YES trades from one mapped market folder."""
    if not (0.0 < truncate_and_keep_ratio <= 1.0):
        raise ValueError("truncate_and_keep_ratio must be in (0, 1].")

    market_metadata_path = market_folder / "metadata.json"
    with open(market_metadata_path, "r", encoding="utf-8") as file:
        market = json.load(file)

    yes_trades_path = market_folder / "yes.csv"
    yes_trades: list[dict[str, Any]] = []
    with open(yes_trades_path, "r", encoding="utf-8") as csvfile:
        csv_reader = csv.DictReader(csvfile)
        for row in csv_reader:
            if trade_policy(row):
                yes_trades.append(row)

    truncate_length = int(len(yes_trades) * truncate_and_keep_ratio)
    yes_trades = yes_trades[:truncate_length]

    return market, yes_trades


def load_filtered_markets_with_trades(
    mapped_market_folder_path: Path,
    truncate_and_keep_ratio: float,
    *,
    market_policy: MarketPolicy = market_filter_policy,
    trade_policy: TradePolicy = trade_filter_policy,
) -> tuple[list[dict[str, Any]], dict[str, list[dict[str, Any]]], int]:
    """Load mapped markets and return (filtered markets, market_id->trades, total folders)."""
    loaded_markets: list[dict[str, Any]] = []
    market_id_to_trades: dict[str, list[dict[str, Any]]] = {}

    original_market_folders = list(mapped_market_folder_path.iterdir())
    for market_folder in original_market_folders:
        if not market_folder.is_dir():
            continue

        market, yes_trades = load_market_and_trades(
            market_folder,
            truncate_and_keep_ratio,
            trade_policy=trade_policy,
        )
        if market_policy(market):
            market_id = str(market["id"])
            loaded_markets.append(market)
            market_id_to_trades[market_id] = yes_trades

    return loaded_markets, market_id_to_trades, len(original_market_folders)
