import argparse
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from analysis_and_experiments.data import load_filtered_markets_with_trades

MAPPED_MARKETS_FOLDER_PATH = Path("datasets/mapped_markets")


@dataclass
class OutcomeAnalysisResult:
    truncate_and_keep_ratio: float
    total_market_folders: int
    filtered_market_count: int
    yes_count: int
    no_count: int
    unknown_count: int
    yes_ratio: float
    no_ratio: float
    unknown_ratio: float


def _safe_ratio(count: int, total: int) -> float:
    if total <= 0:
        return 0.0
    return float(count / total)


def _count_outcomes(markets: list[dict[str, Any]]) -> tuple[int, int, int]:
    yes_count = 0
    no_count = 0
    unknown_count = 0

    for market in markets:
        outcome = str(market.get("outcome", "")).strip().lower()
        if outcome == "yes":
            yes_count += 1
        elif outcome == "no":
            no_count += 1
        else:
            unknown_count += 1

    return yes_count, no_count, unknown_count


def analyze_market_outcome_on_ratio(
    mapped_market_folder_path: Path,
    truncate_and_keep_ratio: float,
) -> OutcomeAnalysisResult:
    loaded_markets, _market_id_to_trades, total_market_folders = load_filtered_markets_with_trades(
        mapped_market_folder_path,
        truncate_and_keep_ratio,
    )

    yes_count, no_count, unknown_count = _count_outcomes(loaded_markets)
    filtered_market_count = len(loaded_markets)

    return OutcomeAnalysisResult(
        truncate_and_keep_ratio=truncate_and_keep_ratio,
        total_market_folders=total_market_folders,
        filtered_market_count=filtered_market_count,
        yes_count=yes_count,
        no_count=no_count,
        unknown_count=unknown_count,
        yes_ratio=_safe_ratio(yes_count, filtered_market_count),
        no_ratio=_safe_ratio(no_count, filtered_market_count),
        unknown_ratio=_safe_ratio(unknown_count, filtered_market_count),
    )


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Analyze filtered market outcomes using the same loading/filter policy as "
            "the strategy modules."
        )
    )
    parser.add_argument(
        "--mapped-markets-folder-path",
        type=Path,
        default=MAPPED_MARKETS_FOLDER_PATH,
        help=f"Path to mapped market folders (default: {MAPPED_MARKETS_FOLDER_PATH}).",
    )
    parser.add_argument(
        "--truncate-and-keep-ratio",
        type=float,
        default=0.67,
        help="Trade truncation ratio used by loader (default: 0.67).",
    )
    return parser


def _print_result(result: OutcomeAnalysisResult) -> None:
    print(f"\n=== truncate_and_keep_ratio={result.truncate_and_keep_ratio:.2f} ===")
    print(f"Original market folders: {result.total_market_folders}")
    print(f"Filtered markets: {result.filtered_market_count}")
    print(
        "Outcome counts | "
        f"yes={result.yes_count}, "
        f"no={result.no_count}, "
        f"unknown={result.unknown_count}"
    )
    print(
        "Outcome ratios | "
        f"yes={result.yes_ratio:.4f}, "
        f"no={result.no_ratio:.4f}, "
        f"unknown={result.unknown_ratio:.4f}"
    )


def main() -> None:
    args = _build_parser().parse_args()
    result = analyze_market_outcome_on_ratio(
        mapped_market_folder_path=args.mapped_markets_folder_path,
        truncate_and_keep_ratio=args.truncate_and_keep_ratio,
    )
    _print_result(result)


if __name__ == "__main__":
    main()
