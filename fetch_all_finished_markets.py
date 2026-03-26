import json

from typing import Any
from datetime import datetime
from pathlib import Path

import requests

GAMMA_BASE_URL = "https://gamma-api.polymarket.com"
CLOB_BASE_URL = "https://clob.polymarket.com"

START_DATE_MIN = datetime.fromisoformat("2025-12-25T00:00:00+00:00")
END_DATE_MIN = datetime.fromisoformat("2025-12-25T00:00:00+00:00")
END_DATE_MAX = datetime.fromisoformat("2025-12-31T23:59:59+00:00")

LIMIMT = 500
TIMEOUT = 30

ALL_MARKETS_METADATA_DUMP_PATH = Path("all_markets_metadata.json")
ALL_MARKETS_METADATA_DUMP_PATH.parent.mkdir(parents=True, exist_ok=True)
  
def fetch_all_finished_markets(start_date_min: datetime, end_date_min: datetime, end_date_max: datetime, limit: int = 500, timeout: int = 30) -> list[dict[str, Any]]:
    """Fetch all finished markets from Polymarket Gamma API under the given date range.
    Args:
        start_date_min: Minimum start date for filtering markets (inclusive)
        end_date_min: Minimum end date for filtering markets (inclusive)
        end_date_max: Maximum end date for filtering markets (inclusive)
        limit: Page size for pagination (default: 500)
        timeout: HTTP timeout in seconds (default: 30)
    Returns:
        A list of market dictionaries that are finished and fall within the specified date range.
    """
    if limit <= 0:
        raise ValueError("limit must be > 0")

    session = requests.Session()
    markets: list[dict[str, Any]] = []
    offset = 0
    end_date_min_iso = end_date_min.isoformat().replace("+00:00", "Z")
    end_date_max_iso = end_date_max.isoformat().replace("+00:00", "Z")  
    while True:
        response = session.get(
            f"{GAMMA_BASE_URL}/markets",
            params={
                "closed": "true", 
                "limit": limit,
                "offset": offset,
                "end_date_min": end_date_min_iso, 
                "end_date_max": end_date_max_iso
            },
            timeout=timeout,
        )
        
        response.raise_for_status()
        
        page = response.json()
        if not isinstance(page, list):
            raise TypeError("Unexpected response: expected a list of markets")
        if not page:
            break
        
        filtered_page = [
            market
            for market in page
            if datetime.fromisoformat(market["startDate"].replace("Z", "+00:00")) > start_date_min
        ]
        markets.extend(filtered_page)
        print(f"fetched: {len(page)} markets and keep: {len(filtered_page)} from offset={offset}, total keep: {len(markets)}")
        offset += len(page)

    return markets


def post_process_markets(markets: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """
    Post process the fetched markets.
    1. Get the outcome based on outcomePrices: if outcomePrices is [0, 1], then outcome is "no"; if outcomePrices is [1, 0], then outcome is "yes". If outcomePrices is neither of them, raise an error.
    2. (Optional) Add more post processing steps if needed in the future.
    """
    # Get the outcome based on outcomePrices
    post_processed_markets = []
    for market in markets:
        is_valid_market = True
        outcome_prices = json.loads(market["outcomePrices"])
        if outcome_prices[0] == '0':
            market["outcome"] = "no"
        elif outcome_prices[0] == '1':
            market["outcome"] = "yes"
        else:
            print(f"Unexpected outcomePrices: {outcome_prices} for market id: {market['id']}, Skipping this market.")
            is_valid_market = False
        
        if is_valid_market:
            post_processed_markets.append(market)
    
    print(f"Post processed markets: {len(post_processed_markets)} / {len(markets)}")
    return post_processed_markets

def main() -> None:
    markets = fetch_all_finished_markets(start_date_min=START_DATE_MIN, end_date_min=END_DATE_MIN, end_date_max=END_DATE_MAX, limit=LIMIMT, timeout=TIMEOUT)
    markets = post_process_markets(markets)

    with open(ALL_MARKETS_METADATA_DUMP_PATH, "w", encoding="utf-8") as f:
        json.dump(markets, f, indent=4, ensure_ascii=False)

    print(f"Successfully fetched {len(markets)} finished markets and saved to {ALL_MARKETS_METADATA_DUMP_PATH}")
   
if __name__ == "__main__":
    main()
