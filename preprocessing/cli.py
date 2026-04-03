import argparse
from datetime import datetime, timezone
from pathlib import Path

from preprocessing.config import (
    DEFAULT_END_DATE_MAX,
    DEFAULT_END_DATE_MIN,
    DEFAULT_LIMIT,
    DEFAULT_MAPPED_MARKETS_FOLDER,
    DEFAULT_MARKETS_METADATA_PATH,
    DEFAULT_START_DATE_MIN,
    DEFAULT_TIMEOUT_SECONDS,
    DEFAULT_TRADE_COUNT_THRESHOLD,
    DEFAULT_TRADES_FOLDER,
    FetchConfig,
    MatchConfig,
    VisualizeConfig,
)
from preprocessing.fetch import fetch_all_finished_markets, post_process_markets
from preprocessing.io import write_json
from preprocessing.match import run_match
from preprocessing.visualize import run_visualization


def _format_datetime(value: datetime) -> str:
    return value.astimezone(timezone.utc).isoformat().replace("+00:00", "Z")


def _parse_datetime(value: str) -> datetime:
    normalized = value.replace("Z", "+00:00")
    parsed = datetime.fromisoformat(normalized)
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=timezone.utc)
    return parsed


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Preprocessing pipeline CLI.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    fetch_parser = subparsers.add_parser("fetch", help="Fetch finished market metadata.")
    fetch_parser.add_argument(
        "--start-date-min",
        type=_parse_datetime,
        default=DEFAULT_START_DATE_MIN,
        help=f"Min market start date (default: {_format_datetime(DEFAULT_START_DATE_MIN)}).",
    )
    fetch_parser.add_argument(
        "--end-date-min",
        type=_parse_datetime,
        default=DEFAULT_END_DATE_MIN,
        help=f"Min market end date (default: {_format_datetime(DEFAULT_END_DATE_MIN)}).",
    )
    fetch_parser.add_argument(
        "--end-date-max",
        type=_parse_datetime,
        default=DEFAULT_END_DATE_MAX,
        help=f"Max market end date (default: {_format_datetime(DEFAULT_END_DATE_MAX)}).",
    )
    fetch_parser.add_argument(
        "--limit",
        type=int,
        default=DEFAULT_LIMIT,
        help=f"Page size for pagination (default: {DEFAULT_LIMIT}).",
    )
    fetch_parser.add_argument(
        "--timeout-seconds",
        type=int,
        default=DEFAULT_TIMEOUT_SECONDS,
        help=f"HTTP timeout seconds (default: {DEFAULT_TIMEOUT_SECONDS}).",
    )
    fetch_parser.add_argument(
        "--output-path",
        type=Path,
        default=DEFAULT_MARKETS_METADATA_PATH,
        help=f"Output path for market metadata JSON (default: {DEFAULT_MARKETS_METADATA_PATH}).",
    )

    match_parser = subparsers.add_parser("match", help="Map trades into each market folder.")
    match_parser.add_argument(
        "--metadata-path",
        type=Path,
        default=DEFAULT_MARKETS_METADATA_PATH,
        help=f"Path to all market metadata JSON (default: {DEFAULT_MARKETS_METADATA_PATH}).",
    )
    match_parser.add_argument(
        "--trades-folder",
        type=Path,
        default=DEFAULT_TRADES_FOLDER,
        help=f"Folder containing trade CSV files (default: {DEFAULT_TRADES_FOLDER}).",
    )
    match_parser.add_argument(
        "--output-folder",
        type=Path,
        default=DEFAULT_MAPPED_MARKETS_FOLDER,
        help=f"Output mapped markets folder (default: {DEFAULT_MAPPED_MARKETS_FOLDER}).",
    )
    match_parser.add_argument(
        "--trade-count-threshold",
        type=int,
        default=DEFAULT_TRADE_COUNT_THRESHOLD,
        help=(
            "Keep markets whose trade_count is strictly greater than this threshold "
            f"(default: {DEFAULT_TRADE_COUNT_THRESHOLD})."
        ),
    )
    match_parser.add_argument(
        "--no-clean-output-folder",
        action="store_true",
        help="Do not clear output folder before writing mapped markets.",
    )

    visualize_parser = subparsers.add_parser(
        "visualize",
        help="Generate per-market price history and trade-count distribution plots.",
    )
    visualize_parser.add_argument(
        "--mapped-markets-folder",
        type=Path,
        default=DEFAULT_MAPPED_MARKETS_FOLDER,
        help=f"Mapped markets folder (default: {DEFAULT_MAPPED_MARKETS_FOLDER}).",
    )
    visualize_parser.add_argument(
        "--visualization-output-folder",
        type=Path,
        default=DEFAULT_MAPPED_MARKETS_FOLDER,
        help=(
            "Folder for visualization outputs "
            f"(default: {DEFAULT_MAPPED_MARKETS_FOLDER})."
        ),
    )

    prepare_parser = subparsers.add_parser(
        "prepare",
        help="Run full pipeline: fetch -> match -> visualize.",
    )
    prepare_parser.add_argument(
        "--start-date-min",
        type=_parse_datetime,
        default=DEFAULT_START_DATE_MIN,
        help=f"Min market start date (default: {_format_datetime(DEFAULT_START_DATE_MIN)}).",
    )
    prepare_parser.add_argument(
        "--end-date-min",
        type=_parse_datetime,
        default=DEFAULT_END_DATE_MIN,
        help=f"Min market end date (default: {_format_datetime(DEFAULT_END_DATE_MIN)}).",
    )
    prepare_parser.add_argument(
        "--end-date-max",
        type=_parse_datetime,
        default=DEFAULT_END_DATE_MAX,
        help=f"Max market end date (default: {_format_datetime(DEFAULT_END_DATE_MAX)}).",
    )
    prepare_parser.add_argument(
        "--limit",
        type=int,
        default=DEFAULT_LIMIT,
        help=f"Page size for pagination (default: {DEFAULT_LIMIT}).",
    )
    prepare_parser.add_argument(
        "--timeout-seconds",
        type=int,
        default=DEFAULT_TIMEOUT_SECONDS,
        help=f"HTTP timeout seconds (default: {DEFAULT_TIMEOUT_SECONDS}).",
    )
    prepare_parser.add_argument(
        "--metadata-path",
        type=Path,
        default=DEFAULT_MARKETS_METADATA_PATH,
        help=f"Output path for market metadata JSON (default: {DEFAULT_MARKETS_METADATA_PATH}).",
    )
    prepare_parser.add_argument(
        "--trades-folder",
        type=Path,
        default=DEFAULT_TRADES_FOLDER,
        help=f"Folder containing trade CSV files (default: {DEFAULT_TRADES_FOLDER}).",
    )
    prepare_parser.add_argument(
        "--output-folder",
        type=Path,
        default=DEFAULT_MAPPED_MARKETS_FOLDER,
        help=f"Output mapped markets folder (default: {DEFAULT_MAPPED_MARKETS_FOLDER}).",
    )
    prepare_parser.add_argument(
        "--trade-count-threshold",
        type=int,
        default=DEFAULT_TRADE_COUNT_THRESHOLD,
        help=(
            "Keep markets whose trade_count is strictly greater than this threshold "
            f"(default: {DEFAULT_TRADE_COUNT_THRESHOLD})."
        ),
    )
    prepare_parser.add_argument(
        "--no-clean-output-folder",
        action="store_true",
        help="Do not clear output folder before writing mapped markets.",
    )
    prepare_parser.add_argument(
        "--visualization-output-folder",
        type=Path,
        default=DEFAULT_MAPPED_MARKETS_FOLDER,
        help=(
            "Folder for visualization outputs "
            f"(default: {DEFAULT_MAPPED_MARKETS_FOLDER})."
        ),
    )

    return parser


def _run_fetch(config: FetchConfig) -> None:
    markets = fetch_all_finished_markets(config)
    markets = post_process_markets(markets)
    write_json(config.output_path, markets)
    print(
        f"Successfully fetched {len(markets)} finished markets and "
        f"saved to {config.output_path}"
    )


def _run_match(config: MatchConfig) -> None:
    run_match(config)


def _run_visualize(config: VisualizeConfig) -> None:
    run_visualization(config)


def main() -> None:
    args = _build_parser().parse_args()

    if args.command == "fetch":
        _run_fetch(
            FetchConfig(
                start_date_min=args.start_date_min,
                end_date_min=args.end_date_min,
                end_date_max=args.end_date_max,
                limit=args.limit,
                timeout_seconds=args.timeout_seconds,
                output_path=args.output_path,
            )
        )
        return

    if args.command == "match":
        _run_match(
            MatchConfig(
                metadata_path=args.metadata_path,
                trades_folder=args.trades_folder,
                output_folder=args.output_folder,
                trade_count_threshold=args.trade_count_threshold,
                clean_output_folder=not args.no_clean_output_folder,
            )
        )
        return

    if args.command == "visualize":
        _run_visualize(
            VisualizeConfig(
                mapped_markets_folder_path=args.mapped_markets_folder,
                visualization_output_folder_path=args.visualization_output_folder,
            )
        )
        return

    if args.command == "prepare":
        fetch_config = FetchConfig(
            start_date_min=args.start_date_min,
            end_date_min=args.end_date_min,
            end_date_max=args.end_date_max,
            limit=args.limit,
            timeout_seconds=args.timeout_seconds,
            output_path=args.metadata_path,
        )
        match_config = MatchConfig(
            metadata_path=args.metadata_path,
            trades_folder=args.trades_folder,
            output_folder=args.output_folder,
            trade_count_threshold=args.trade_count_threshold,
            clean_output_folder=not args.no_clean_output_folder,
        )
        visualize_config = VisualizeConfig(
            mapped_markets_folder_path=args.output_folder,
            visualization_output_folder_path=args.visualization_output_folder,
        )

        print("[prepare] Step 1/3: fetch")
        _run_fetch(fetch_config)
        print("[prepare] Step 2/3: match")
        _run_match(match_config)
        print("[prepare] Step 3/3: visualize")
        _run_visualize(visualize_config)
        return

    raise ValueError(f"Unsupported command: {args.command}")


if __name__ == "__main__":
    main()
