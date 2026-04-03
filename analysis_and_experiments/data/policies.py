from typing import Any


def market_filter_policy(market: dict[str, Any]) -> bool:
    """Keep markets with enough trade activity."""
    return int(market.get("yes_trade_count", 0)) > 500


def btc_market_filter_policy(market: dict[str, Any]) -> bool:
    """Keep active BTC/USDT markets with enough YES-side trade activity."""
    if not market_filter_policy(market):
        return False
    description = str(market.get("description", ""))
    return "btc" in description.lower() or "bitcoin" in description.lower()


def trade_filter_policy(trade: dict[str, Any]) -> bool:
    """Keep meaningful BUY trades below near-certain pricing."""
    return (
        str(trade.get("side", "")) == "BUY"
        and float(trade.get("price", 0.0)) < 0.98
        and float(trade.get("total_usdc", 0.0)) > 2.0
    )
