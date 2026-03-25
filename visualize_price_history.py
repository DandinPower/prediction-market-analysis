import json
import csv

from typing import Any
from pathlib import Path

import matplotlib.pyplot as plt

MAPPED_MARKETS_FOLDER_PATH = Path("mapped_markets")

def visualize_price_history(mapped_markets_folder_path: Path) -> None:
    def _visualize_yes_price_history_for_market(market_folder: Path) -> None:
        """
        Visualize the price history of "Yes" trades for a given market by reading the market metadata and yes trades from the specified market folder. The price history is plotted as a line chart with timestamps on the x-axis and prices on the y-axis. The resulting plot is saved as "yes_price_history.png" in the same market folder.
        Args:
            market_folder: The Path object representing the folder of the market, which should contain "metadata.json" and "yes.csv" files.
        """ 
        market_metadata_path = market_folder / "metadata.json"
        with open(market_metadata_path, "r", encoding="utf-8") as f:
            market = json.load(f)

        yes_trades_path = market_folder / "yes.csv"
        yes_trades = []
        with open(yes_trades_path, "r", encoding="utf-8") as csvfile:
            csvreader = csv.DictReader(csvfile)
            for row in csvreader:
                yes_trades.append(row)

        yes_prices = [float(trade["price"]) for trade in yes_trades]
        trades_index = list(range(len(yes_trades)))
        
        plt.figure(figsize=(10, 6))
        plt.plot(trades_index, yes_prices, label="Yes Trades", marker='o')
        plt.xlabel("Timestamp")
        plt.ylabel("Price")
        plt.title(f"Price History for Market: {market['id']}")
        plt.legend()
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig(market_folder / "yes_price_history.png")
        plt.close()

    for market_folder in mapped_markets_folder_path.iterdir():
        if market_folder.is_dir():
            print(f"Visualizing price history for market folder: {market_folder}")
            _visualize_yes_price_history_for_market(market_folder)

if __name__ == "__main__":
    visualize_price_history(mapped_markets_folder_path=MAPPED_MARKETS_FOLDER_PATH)