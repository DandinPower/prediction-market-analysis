from pathlib import Path

import matplotlib.pyplot as plt

from analysis_and_experiments.data import load_market_and_trades, market_filter_policy
from preprocessing.config import VisualizeConfig


def _visualize_yes_price_history_for_market(
    market: dict[str, object],
    trades: list[dict[str, object]],
    output_dir: Path,
) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    prices = [float(trade["price"]) for trade in trades]
    trade_index = list(range(len(prices)))

    plt.figure(figsize=(10, 6))
    plt.plot(trade_index, prices, label="Yes Trades", marker="o")
    plt.xlabel("Timestamp")
    plt.ylabel("Price")
    plt.title(f"Price History for Market: {market['id']}")
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(output_dir / "yes_price_history_final.png")
    plt.close()


def _visualize_yes_trades_histogram(trade_count_statistics: list[int], output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    plt.figure(figsize=(10, 6))
    plt.hist(trade_count_statistics, bins=20, edgecolor="black")
    plt.xlabel("Number of Yes Trades (after filtering)")
    plt.ylabel("Number of Markets")
    plt.title("Distribution of Yes Trade Counts Across Markets")
    plt.tight_layout()
    plt.savefig(output_dir / "yes_trade_count_distribution.png", dpi=300)
    plt.close()


def run_visualization(config: VisualizeConfig) -> None:
    loaded_markets: list[dict[str, object]] = []
    loaded_market_id_to_trades: dict[str, list[dict[str, object]]] = {}
    loaded_market_id_to_folder: dict[str, Path] = {}

    for market_folder in sorted(config.mapped_markets_folder_path.iterdir(), key=lambda item: item.name):
        if not market_folder.is_dir():
            continue

        market, trades = load_market_and_trades(market_folder, truncate_and_keep_ratio=1.0)
        if not market_filter_policy(market):
            continue

        market_id = str(market["id"])
        loaded_markets.append(market)
        loaded_market_id_to_trades[market_id] = trades
        loaded_market_id_to_folder[market_id] = config.visualization_output_folder_path / market_id

    trade_count_statistics: list[int] = []
    for market in loaded_markets:
        market_id = str(market["id"])
        trades = loaded_market_id_to_trades[market_id]
        market_folder = loaded_market_id_to_folder[market_id]
        _visualize_yes_price_history_for_market(market, trades, market_folder)
        trade_count_statistics.append(len(trades))

    _visualize_yes_trades_histogram(
        trade_count_statistics,
        config.visualization_output_folder_path,
    )
