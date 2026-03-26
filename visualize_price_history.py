import json
import csv

from typing import Any
from pathlib import Path

import matplotlib.pyplot as plt

MAPPED_MARKETS_FOLDER_PATH = Path("mapped_markets")
VISUALIZATION_OUTPUT_FOLDER_PATH = Path("visualization_output")


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

def load_market_and_trades(market_folder: Path) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    """
    Load the market metadata and (filtered) yes trades from the specified market folder.
    Args:
        market_folder: The Path object representing the folder of the market, which should contain "metadata.json" and "yes.csv" files.
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

    return market, yes_trades

def visualization(mapped_markets_folder_path: Path, visualization_output_folder_path: Path) -> None:
    def _visualize_yes_price_history_for_market(market: dict[str, Any], trades: list[dict[str, Any]], output_dir: Path) -> None:
        """
        Visualize the price history of yes trades for a given market.
        Args:
            market: A dictionary containing the market metadata.
            trades: A list of dictionaries, each containing information about a "Yes" trade.
            output_dir: The Path object representing the directory where the visualization will be saved.
        """ 
        output_dir.mkdir(parents=True, exist_ok=True)
        prices = [float(trade["price"]) for trade in trades]
        trades_index = list(range(len(prices)))
        
        plt.figure(figsize=(10, 6))
        plt.plot(trades_index, prices, label="Yes Trades", marker='o')
        plt.xlabel("Timestamp")
        plt.ylabel("Price")
        plt.title(f"Price History for Market: {market['id']}")
        plt.legend()
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig(output_dir / "yes_price_history_final.png")
        plt.close()


    def _visualize_yes_trades_histogram(trade_count_statistics: list[int], output_dir: Path) -> None:
        """
        Visualize the histogram of yes trades for a given market.
        Args:
            trade_count_statistics: A list of integers representing the count of yes trades for each market.
            output_dir: The Path object representing the directory where the visualization will be saved.
        """ 
        output_dir.mkdir(parents=True, exist_ok=True)
        plt.figure(figsize=(10, 6))
        plt.hist(trade_count_statistics, bins=20, edgecolor='black')
        plt.xlabel("Number of Yes Trades (after filtering)")
        plt.ylabel("Number of Markets")
        plt.title("Distribution of Yes Trade Counts Across Markets")
        plt.tight_layout()
        plt.savefig(output_dir / "yes_trade_count_distribution.png")
        plt.close()


    loaded_markets = []
    loaded_market_id_to_trades = {}
    loaded_market_id_to_folder = {}

    for market_folder in mapped_markets_folder_path.iterdir():
        if market_folder.is_dir():
            market, trades = load_market_and_trades(market_folder)

            if not market_filter_policy(market):
                continue

            loaded_markets.append(market)
            loaded_market_id_to_trades[market["id"]] = trades
            loaded_market_id_to_folder[market["id"]] = visualization_output_folder_path / market["id"]

    trade_count_statistics = []
    for market in loaded_markets:
        trades = loaded_market_id_to_trades[market["id"]]
        market_folder = loaded_market_id_to_folder[market["id"]]
        _visualize_yes_price_history_for_market(market, trades, market_folder)        

        trade_count_statistics.append(len(trades))
    
    _visualize_yes_trades_histogram(trade_count_statistics, visualization_output_folder_path)


if __name__ == "__main__":
    VISUALIZATION_OUTPUT_FOLDER_PATH.mkdir(parents=True, exist_ok=True)
    visualization(mapped_markets_folder_path=MAPPED_MARKETS_FOLDER_PATH, visualization_output_folder_path=VISUALIZATION_OUTPUT_FOLDER_PATH)