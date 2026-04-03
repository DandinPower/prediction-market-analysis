import json
from datetime import datetime, timezone
from typing import Any

import requests

from preprocessing.config import FetchConfig

GAMMA_BASE_URL = "https://gamma-api.polymarket.com"


def _to_iso_z(value: datetime) -> str:
    return value.astimezone(timezone.utc).isoformat().replace("+00:00", "Z")


def _parse_iso_datetime(value: str) -> datetime:
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def fetch_all_finished_markets(config: FetchConfig) -> list[dict[str, Any]]:
    if config.limit <= 0:
        raise ValueError("limit must be > 0")

    end_date_min_iso = _to_iso_z(config.end_date_min)
    end_date_max_iso = _to_iso_z(config.end_date_max)

    markets: list[dict[str, Any]] = []
    offset = 0

    session = requests.Session()

    while True:
        response = session.get(
            f"{GAMMA_BASE_URL}/markets",
            params={
                "closed": "true",
                "limit": config.limit,
                "offset": offset,
                "end_date_min": end_date_min_iso,
                "end_date_max": end_date_max_iso,
            },
            timeout=config.timeout_seconds,
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
            if _parse_iso_datetime(str(market["startDate"])) > config.start_date_min
        ]
        markets.extend(filtered_page)

        print(
            f"fetched: {len(page)} markets and keep: {len(filtered_page)} "
            f"from offset={offset}, total keep: {len(markets)}"
        )
        offset += len(page)

    return markets


def post_process_markets(markets: list[dict[str, Any]]) -> list[dict[str, Any]]:
    post_processed_markets: list[dict[str, Any]] = []

    for market in markets:
        outcome_prices = json.loads(str(market["outcomePrices"]))
        if not isinstance(outcome_prices, list) or len(outcome_prices) < 2:
            print(
                f"Unexpected outcomePrices format for market id: {market['id']}. "
                "Skipping this market."
            )
            continue

        first = str(outcome_prices[0])
        second = str(outcome_prices[1])

        if first == "0" and second == "1":
            market["outcome"] = "no"
        elif first == "1" and second == "0":
            market["outcome"] = "yes"
        else:
            print(
                f"Unexpected outcomePrices: {outcome_prices} "
                f"for market id: {market['id']}. Skipping this market."
            )
            continue

        post_processed_markets.append(market)

    print(f"Post processed markets: {len(post_processed_markets)} / {len(markets)}")
    return post_processed_markets
