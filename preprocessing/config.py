from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

DEFAULT_START_DATE_MIN = datetime.fromisoformat("2025-12-25T00:00:00+00:00")
DEFAULT_END_DATE_MIN = datetime.fromisoformat("2025-12-25T00:00:00+00:00")
DEFAULT_END_DATE_MAX = datetime.fromisoformat("2025-12-31T23:59:59+00:00")

DEFAULT_MARKETS_METADATA_PATH = Path("datasets/metadata/all_markets_metadata.json")
DEFAULT_TRADES_FOLDER = Path("datasets/trades")
DEFAULT_MAPPED_MARKETS_FOLDER = Path("datasets/mapped_markets")

DEFAULT_LIMIT = 500
DEFAULT_TIMEOUT_SECONDS = 30
DEFAULT_TRADE_COUNT_THRESHOLD = 1

TRADE_HEADERS = [
    "block_number",
    "timestamp",
    "tx_hash",
    "wallet",
    "side",
    "tokens",
    "price",
    "total_usdc",
]


@dataclass(frozen=True)
class FetchConfig:
    start_date_min: datetime = DEFAULT_START_DATE_MIN
    end_date_min: datetime = DEFAULT_END_DATE_MIN
    end_date_max: datetime = DEFAULT_END_DATE_MAX
    limit: int = DEFAULT_LIMIT
    timeout_seconds: int = DEFAULT_TIMEOUT_SECONDS
    output_path: Path = DEFAULT_MARKETS_METADATA_PATH


@dataclass(frozen=True)
class MatchConfig:
    metadata_path: Path = DEFAULT_MARKETS_METADATA_PATH
    trades_folder: Path = DEFAULT_TRADES_FOLDER
    output_folder: Path = DEFAULT_MAPPED_MARKETS_FOLDER
    trade_count_threshold: int = DEFAULT_TRADE_COUNT_THRESHOLD
    clean_output_folder: bool = True


@dataclass(frozen=True)
class VisualizeConfig:
    mapped_markets_folder_path: Path = DEFAULT_MAPPED_MARKETS_FOLDER
    visualization_output_folder_path: Path = DEFAULT_MAPPED_MARKETS_FOLDER
