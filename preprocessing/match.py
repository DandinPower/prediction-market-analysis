import csv
import json
from pathlib import Path
from typing import Any

from preprocessing.config import MatchConfig
from preprocessing.io import clear_directory, iter_trade_csv_files, read_json, save_mapped_markets

TokenToMarketSide = dict[str, tuple[dict[str, Any], str]]


def load_markets_metadata(metadata_path: Path) -> tuple[TokenToMarketSide, list[dict[str, Any]]]:
    raw = read_json(metadata_path)
    if not isinstance(raw, list):
        raise TypeError(f"Expected list in metadata JSON: {metadata_path}")

    markets: list[dict[str, Any]] = raw
    print(f"Loaded {len(markets)} markets from {metadata_path}")

    token_to_market_side: TokenToMarketSide = {}
    for market in markets:
        market["trade_count"] = 0
        market["yes_trade_count"] = 0
        market["no_trade_count"] = 0
        market["yes_trades"] = []
        market["no_trades"] = []

        clob_token_ids = json.loads(str(market["clobTokenIds"]))
        if not isinstance(clob_token_ids, list) or len(clob_token_ids) < 2:
            raise ValueError(f"Invalid clobTokenIds for market id {market.get('id')}")

        yes_token_id = str(clob_token_ids[0])
        no_token_id = str(clob_token_ids[1])
        token_to_market_side[yes_token_id] = (market, "yes")
        token_to_market_side[no_token_id] = (market, "no")

    return token_to_market_side, markets


def map_markets_and_trades(
    token_to_market_side: TokenToMarketSide,
    markets: list[dict[str, Any]],
    trades_folder: Path,
    trade_count_threshold: int,
) -> list[dict[str, Any]]:
    for trade_file_path in iter_trade_csv_files(trades_folder):
        with open(trade_file_path, mode="r", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                token_id = str(row.get("token_id", ""))
                hit = token_to_market_side.get(token_id)
                if hit is None:
                    continue

                market, side_key = hit
                trade_info = {
                    "block_number": row.get("block_number", ""),
                    "timestamp": row.get("timestamp", ""),
                    "tx_hash": row.get("tx_hash", ""),
                    "wallet": row.get("wallet", ""),
                    "side": row.get("side", ""),
                    "tokens": row.get("tokens", ""),
                    "price": row.get("price", ""),
                    "total_usdc": row.get("total_usdc", ""),
                }

                if side_key == "yes":
                    market["yes_trades"].append(trade_info)
                    market["yes_trade_count"] += 1
                else:
                    market["no_trades"].append(trade_info)
                    market["no_trade_count"] += 1

                market["trade_count"] += 1

    filtered_mapped_markets = [
        market for market in markets if int(market["trade_count"]) > trade_count_threshold
    ]
    print(
        f"Found {len(filtered_mapped_markets)} / {len(markets)} markets "
        f"with at least {trade_count_threshold} trade."
    )

    for market in filtered_mapped_markets:
        market["yes_trades"].sort(key=lambda trade: str(trade["timestamp"]))
        market["no_trades"].sort(key=lambda trade: str(trade["timestamp"]))

    return filtered_mapped_markets


def run_match(config: MatchConfig) -> list[dict[str, Any]]:
    if config.clean_output_folder:
        clear_directory(config.output_folder)

    token_to_market_side, markets = load_markets_metadata(config.metadata_path)
    filtered_mapped_markets = map_markets_and_trades(
        token_to_market_side,
        markets,
        config.trades_folder,
        config.trade_count_threshold,
    )
    save_mapped_markets(filtered_mapped_markets, output_folder=config.output_folder)
    print(
        f"Successfully saved trades for {len(filtered_mapped_markets)} markets "
        f"to {config.output_folder}"
    )
    return filtered_mapped_markets
