import json
import csv

from pathlib import Path    
from typing import Any

ALL_MARKETS_METADATA_DUMP_PATH = Path("all_markets_metadata.json")
MARKET_TRADE_COUNT_THRESHOLD = 1
TRADES_FOLDER = "trades"
RESULT_FOLDER = "mapped_markets"

def load_markets_metadata() -> tuple[dict[str, Any], list[Any]]:
    """
    Load markets metadata from the JSON dump file and initialize the token to market mapping.
    Returns:
        token_to_market: A dictionary mapping token IDs to their corresponding market metadata.
        markets: A list of market metadata dictionaries.
    """
    if not ALL_MARKETS_METADATA_DUMP_PATH.exists():
        print(f"Error: {ALL_MARKETS_METADATA_DUMP_PATH} does not exist. Please run fetch_all_finished_markets.py first to fetch and save the markets metadata.")
        return
    
    with open(ALL_MARKETS_METADATA_DUMP_PATH, "r", encoding="utf-8") as f:
        markets = json.load(f)
    print(f"Loaded {len(markets)} markets from {ALL_MARKETS_METADATA_DUMP_PATH}")

    token_to_market = {}
    for market in markets:
        market["trade_count"] = 0
        market["yes_trade_count"] = 0
        market["no_trade_count"] = 0
        market["yes_trades"] = []
        market["no_trades"] = []
        clob_token_ids = json.loads(market["clobTokenIds"])
        yes_token_id = clob_token_ids[0]
        no_token_id = clob_token_ids[1]
        token_to_market[yes_token_id] = market
        token_to_market[no_token_id] = market

    return token_to_market, markets


def map_markets_and_trades(token_to_market: dict[str, Any], markets: list[Any], trades_folder: str) -> list[Any]:
    """
    Map markets metadata with their corresponding trades by matching token IDs. Only keeps markets that larger than MARKET_TRADE_COUNT_THRESHOLD trades.
    Args:
        token_to_market: A dictionary mapping token IDs to their corresponding market metadata.
        markets: A list of market metadata dictionaries.
        trades_folder: The folder path where the trade CSV files are located.
    Returns:
        A list of market metadata dictionaries that have been enriched with their corresponding trades and filtered by the
        MARKET_TRADE_COUNT_THRESHOLD. Each market dictionary will have "yes_trades" and "no_trades" keys containing lists of trade information dictionaries. Each trade information dictionary contains block_number, timestamp, tx_hash, wallet, side, tokens, price, and total_usdc.
    """
    for trade_file_path in Path(trades_folder).glob("*.csv"):
        with open(trade_file_path, mode="r", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                token_id = row["token_id"]
                if token_id in token_to_market:
                    market = token_to_market[token_id]
                    trade_info = {
                        "block_number": row["block_number"],
                        "timestamp": row["timestamp"],
                        "tx_hash": row["tx_hash"],
                        "wallet": row["wallet"],
                        "side": row["side"],
                        "tokens": row["tokens"],
                        "price": row["price"],
                        "total_usdc": row["total_usdc"]
                    }
                    clob_token_ids = json.loads(market["clobTokenIds"])
                    yes_token_id = clob_token_ids[0]
                    no_token_id = clob_token_ids[1]
                    if yes_token_id == token_id:
                        market["yes_trades"].append(trade_info)
                        market["yes_trade_count"] += 1
                    elif no_token_id == token_id:
                        market["no_trades"].append(trade_info)
                        market["no_trade_count"] += 1
                    else:
                        print(f"Should not happen: token_id {token_id} not found in market's clobTokenIds")
                    market["trade_count"] += 1
    
    filtered_mapped_markets = [market for market in markets if market["trade_count"] > MARKET_TRADE_COUNT_THRESHOLD]
    print(f"Found {len(filtered_mapped_markets)} / {len(markets)} markets with at least {MARKET_TRADE_COUNT_THRESHOLD} trade.")
    
    # sort trades in each market by timestamp
    for market in filtered_mapped_markets:
        market["yes_trades"].sort(key=lambda x: x["timestamp"])
        market["no_trades"].sort(key=lambda x: x["timestamp"])
    
    return filtered_mapped_markets


def save_mapped_markets_to_csv(mapped_markets: list[Any], output_folder: str) -> None:
    output_folder_path = Path(output_folder)
    output_folder_path.mkdir(parents=True, exist_ok=True)

    headers = ["block_number", "timestamp", "tx_hash", "wallet", "side", "tokens", "price", "total_usdc"]

    for market in mapped_markets:
        market_id = market["id"]
        market_folder = output_folder_path / str(market_id)
        market_folder.mkdir(parents=True, exist_ok=True)

        yes_trades_path = market_folder / "yes.csv"
        no_trades_path = market_folder / "no.csv"

        with open(yes_trades_path, "w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=headers)
            writer.writeheader()
            writer.writerows(market["yes_trades"])
        
        with open(no_trades_path, "w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=headers)
            writer.writeheader()
            writer.writerows(market["no_trades"])

        metadata_exclude_trades = {k: v for k, v in market.items() if k not in ["yes_trades", "no_trades"]}
        with open(market_folder / "metadata.json", "w", encoding="utf-8") as f:
            json.dump(metadata_exclude_trades, f, indent=4, ensure_ascii=False)

    print(f"Successfully saved trades for {len(mapped_markets)} markets to {output_folder}")


def cleanup_result_folder(result_folder: str) -> None:
    result_folder_path = Path(result_folder)
    if result_folder_path.exists():
        for item in result_folder_path.glob("*"):
            if item.is_dir():
                for sub_item in item.glob("*"):
                    sub_item.unlink()
                item.rmdir()
            else:
                item.unlink()

def main():
    cleanup_result_folder(RESULT_FOLDER)
    token_to_market, markets = load_markets_metadata()
    filtered_mapped_markets = map_markets_and_trades(token_to_market, markets, trades_folder=TRADES_FOLDER)
    save_mapped_markets_to_csv(filtered_mapped_markets, output_folder=RESULT_FOLDER)

if __name__ == "__main__":
    main()