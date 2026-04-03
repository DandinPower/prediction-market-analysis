import csv
import json
import shutil
from pathlib import Path
from typing import Any

from preprocessing.config import TRADE_HEADERS


def ensure_parent_dir(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)


def read_json(path: Path) -> Any:
    if not path.exists():
        raise FileNotFoundError(f"File does not exist: {path}")
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


def write_json(path: Path, data: Any) -> None:
    ensure_parent_dir(path)
    with open(path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def iter_trade_csv_files(trades_folder: Path) -> list[Path]:
    if not trades_folder.exists():
        raise FileNotFoundError(f"Trades folder does not exist: {trades_folder}")
    return sorted(trades_folder.glob("*.csv"), key=lambda item: item.name)


def clear_directory(path: Path) -> None:
    if not path.exists():
        return
    for item in sorted(path.iterdir(), key=lambda entry: entry.name):
        if item.is_dir():
            shutil.rmtree(item)
        else:
            item.unlink()


def save_mapped_markets(markets: list[dict[str, Any]], output_folder: Path) -> None:
    output_folder.mkdir(parents=True, exist_ok=True)

    for market in markets:
        market_id = str(market["id"])
        market_folder = output_folder / market_id
        market_folder.mkdir(parents=True, exist_ok=True)

        yes_trades_path = market_folder / "yes.csv"
        no_trades_path = market_folder / "no.csv"

        with open(yes_trades_path, "w", encoding="utf-8", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=TRADE_HEADERS)
            writer.writeheader()
            writer.writerows(market["yes_trades"])

        with open(no_trades_path, "w", encoding="utf-8", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=TRADE_HEADERS)
            writer.writeheader()
            writer.writerows(market["no_trades"])

        metadata_exclude_trades = {
            key: value
            for key, value in market.items()
            if key not in ["yes_trades", "no_trades"]
        }
        write_json(market_folder / "metadata.json", metadata_exclude_trades)
