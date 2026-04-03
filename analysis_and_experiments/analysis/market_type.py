import argparse
import json
import re
from dataclasses import dataclass
from pathlib import Path

from analysis_and_experiments.data import market_filter_policy

MAPPED_MARKETS_FOLDER_PATH = Path("datasets/mapped_markets")
MARKET_TYPES = ("crypto_bitcoin", "crypto_other", "nfl", "nba", "cfb", "others")

NFL_PATTERN = re.compile(r"\bnfl\b", flags=re.IGNORECASE)
NBA_PATTERN = re.compile(r"\bnba\b", flags=re.IGNORECASE)
CFB_PATTERN = re.compile(r"\bcfb\b", flags=re.IGNORECASE)
UP_PATTERN = re.compile(r"\bup\b", flags=re.IGNORECASE)
DOWN_PATTERN = re.compile(r"\bdown\b", flags=re.IGNORECASE)
BITCOIN_PATTERN = re.compile(r"\b(bitcoin|btc)\b", flags=re.IGNORECASE)


@dataclass
class MarketTypeAnalysisResult:
    total_market_folders: int
    filtered_market_count: int
    type_counts: dict[str, int]
    type_ratios: dict[str, float]
    market_ids_by_type: dict[str, list[str]]


def _safe_ratio(count: int, total: int) -> float:
    if total <= 0:
        return 0.0
    return float(count / total)


def _load_market_metadata(market_folder: Path) -> dict[str, object]:
    metadata_path = market_folder / "metadata.json"
    with open(metadata_path, "r", encoding="utf-8") as file:
        return json.load(file)


def _classify_market_type_from_description(description: str) -> str:
    if NFL_PATTERN.search(description):
        return "nfl"
    if NBA_PATTERN.search(description):
        return "nba"
    if CFB_PATTERN.search(description):
        return "cfb"
    if UP_PATTERN.search(description) and DOWN_PATTERN.search(description):
        if BITCOIN_PATTERN.search(description):
            return "crypto_bitcoin"
        return "crypto_other"
    return "others"


def analyze_market_type(
    mapped_market_folder_path: Path,
    apply_market_filter: bool,
) -> MarketTypeAnalysisResult:
    original_market_folders = list(mapped_market_folder_path.iterdir())
    market_ids_by_type = {market_type: [] for market_type in MARKET_TYPES}

    for market_folder in original_market_folders:
        if not market_folder.is_dir():
            continue

        metadata_path = market_folder / "metadata.json"
        if not metadata_path.exists():
            continue

        market = _load_market_metadata(market_folder)
        if apply_market_filter and not market_filter_policy(market):
            continue

        description = str(market.get("description", ""))
        market_type = _classify_market_type_from_description(description)
        market_id = str(market.get("id", market_folder.name))
        market_ids_by_type[market_type].append(market_id)

    filtered_market_count = sum(len(ids) for ids in market_ids_by_type.values())
    type_counts = {market_type: len(ids) for market_type, ids in market_ids_by_type.items()}
    type_ratios = {
        market_type: _safe_ratio(count, filtered_market_count)
        for market_type, count in type_counts.items()
    }

    return MarketTypeAnalysisResult(
        total_market_folders=len(original_market_folders),
        filtered_market_count=filtered_market_count,
        type_counts=type_counts,
        type_ratios=type_ratios,
        market_ids_by_type=market_ids_by_type,
    )


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Cluster markets by description rules: nfl, nba, cfb, crypto_bitcoin "
            "(contains both 'Up' and 'Down', and contains 'Bitcoin' or 'BTC'), "
            "crypto_other (contains both 'Up' and 'Down' but not Bitcoin/BTC), and others."
        )
    )
    parser.add_argument(
        "--mapped-markets-folder-path",
        type=Path,
        default=MAPPED_MARKETS_FOLDER_PATH,
        help=f"Path to mapped market folders (default: {MAPPED_MARKETS_FOLDER_PATH}).",
    )
    parser.add_argument(
        "--disable-market-filter",
        action="store_true",
        help="Disable market_filter_policy. By default the same market policy is applied.",
    )
    parser.add_argument(
        "--output-json-path",
        type=Path,
        default=None,
        help="Optional path to save clustered market IDs as JSON.",
    )
    return parser


def _print_result(result: MarketTypeAnalysisResult) -> None:
    print("\n=== Market Type Analysis ===")
    print(f"Original market folders: {result.total_market_folders}")
    print(f"Analyzed markets: {result.filtered_market_count}")
    print(
        "Type counts | "
        f"crypto_bitcoin={result.type_counts['crypto_bitcoin']}, "
        f"crypto_other={result.type_counts['crypto_other']}, "
        f"nfl={result.type_counts['nfl']}, "
        f"nba={result.type_counts['nba']}, "
        f"cfb={result.type_counts['cfb']}, "
        f"others={result.type_counts['others']}"
    )
    print(
        "Type ratios | "
        f"crypto_bitcoin={result.type_ratios['crypto_bitcoin']:.4f}, "
        f"crypto_other={result.type_ratios['crypto_other']:.4f}, "
        f"nfl={result.type_ratios['nfl']:.4f}, "
        f"nba={result.type_ratios['nba']:.4f}, "
        f"cfb={result.type_ratios['cfb']:.4f}, "
        f"others={result.type_ratios['others']:.4f}"
    )


def _save_clusters(output_json_path: Path, result: MarketTypeAnalysisResult) -> None:
    output_json_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_json_path, "w", encoding="utf-8") as file:
        json.dump(result.market_ids_by_type, file, indent=2)
    print(f"Saved clusters to: {output_json_path}")


def main() -> None:
    args = _build_parser().parse_args()
    result = analyze_market_type(
        mapped_market_folder_path=args.mapped_markets_folder_path,
        apply_market_filter=not args.disable_market_filter,
    )
    _print_result(result)

    if args.output_json_path is not None:
        _save_clusters(args.output_json_path, result)


if __name__ == "__main__":
    main()
