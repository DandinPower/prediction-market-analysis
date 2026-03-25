---
url: "https://docs.polymarket.com/api-reference/geoblock"
title: "Geographic Restrictions - Polymarket Documentation"
---

[Skip to main content](https://docs.polymarket.com/api-reference/geoblock#content-area)

[Polymarket Documentation home page![light logo](https://mintcdn.com/polymarket-292d1b1b/ZibMe6Tli_amZald/logo/light.svg?fit=max&auto=format&n=ZibMe6Tli_amZald&q=85&s=9f9bd559f02181495794661ef6426c0f)![dark logo](https://mintcdn.com/polymarket-292d1b1b/ZibMe6Tli_amZald/logo/dark.svg?fit=max&auto=format&n=ZibMe6Tli_amZald&q=85&s=13abc6754579a3475368ea99d0f5a241)](https://docs.polymarket.com/)

![US](https://d3gk2c5xim1je2.cloudfront.net/flags/US.svg)

English

Search...

Ctrl KAsk AI

Search...

Navigation

Overview

Geographic Restrictions

[Documentation](https://docs.polymarket.com/) [API Reference](https://docs.polymarket.com/api-reference/introduction)

##### Overview

- [Introduction](https://docs.polymarket.com/api-reference/introduction)
- [Authentication](https://docs.polymarket.com/api-reference/authentication)
- [Rate Limits](https://docs.polymarket.com/api-reference/rate-limits)
- [Clients & SDKs](https://docs.polymarket.com/api-reference/clients-sdks)
- [Geographic Restrictions](https://docs.polymarket.com/api-reference/geoblock)

##### Events

- [GET\\
\\
List events](https://docs.polymarket.com/api-reference/events/list-events)
- [GET\\
\\
Get event by id](https://docs.polymarket.com/api-reference/events/get-event-by-id)
- [GET\\
\\
Get event by slug](https://docs.polymarket.com/api-reference/events/get-event-by-slug)
- [GET\\
\\
Get event tags](https://docs.polymarket.com/api-reference/events/get-event-tags)

##### Markets

- [GET\\
\\
List markets](https://docs.polymarket.com/api-reference/markets/list-markets)
- [GET\\
\\
Get market by id](https://docs.polymarket.com/api-reference/markets/get-market-by-id)
- [GET\\
\\
Get market by slug](https://docs.polymarket.com/api-reference/markets/get-market-by-slug)
- [GET\\
\\
Get market tags by id](https://docs.polymarket.com/api-reference/markets/get-market-tags-by-id)
- [GET\\
\\
Get top holders for markets](https://docs.polymarket.com/api-reference/core/get-top-holders-for-markets)
- [GET\\
\\
Get open interest](https://docs.polymarket.com/api-reference/misc/get-open-interest)
- [GET\\
\\
Get live volume for an event](https://docs.polymarket.com/api-reference/misc/get-live-volume-for-an-event)

##### Orderbook & Pricing

- [GET\\
\\
Get order book](https://docs.polymarket.com/api-reference/market-data/get-order-book)
- [POST\\
\\
Get order books (request body)](https://docs.polymarket.com/api-reference/market-data/get-order-books-request-body)
- [GET\\
\\
Get market price](https://docs.polymarket.com/api-reference/market-data/get-market-price)
- [GET\\
\\
Get market prices (query parameters)](https://docs.polymarket.com/api-reference/market-data/get-market-prices-query-parameters)
- [POST\\
\\
Get market prices (request body)](https://docs.polymarket.com/api-reference/market-data/get-market-prices-request-body)
- [GET\\
\\
Get midpoint price](https://docs.polymarket.com/api-reference/data/get-midpoint-price)
- [GET\\
\\
Get midpoint prices (query parameters)](https://docs.polymarket.com/api-reference/market-data/get-midpoint-prices-query-parameters)
- [POST\\
\\
Get midpoint prices (request body)](https://docs.polymarket.com/api-reference/market-data/get-midpoint-prices-request-body)
- [GET\\
\\
Get spread](https://docs.polymarket.com/api-reference/market-data/get-spread)
- [POST\\
\\
Get spreads](https://docs.polymarket.com/api-reference/market-data/get-spreads)
- [GET\\
\\
Get last trade price](https://docs.polymarket.com/api-reference/market-data/get-last-trade-price)
- [GET\\
\\
Get last trade prices (query parameters)](https://docs.polymarket.com/api-reference/market-data/get-last-trade-prices-query-parameters)
- [POST\\
\\
Get last trade prices (request body)](https://docs.polymarket.com/api-reference/market-data/get-last-trade-prices-request-body)
- [GET\\
\\
Get prices history](https://docs.polymarket.com/api-reference/markets/get-prices-history)
- [GET\\
\\
Get fee rate](https://docs.polymarket.com/api-reference/market-data/get-fee-rate)
- [GET\\
\\
Get fee rate by path parameter](https://docs.polymarket.com/api-reference/market-data/get-fee-rate-by-path-parameter)
- [GET\\
\\
Get tick size](https://docs.polymarket.com/api-reference/market-data/get-tick-size)
- [GET\\
\\
Get tick size by path parameter](https://docs.polymarket.com/api-reference/market-data/get-tick-size-by-path-parameter)
- [GET\\
\\
Get server time](https://docs.polymarket.com/api-reference/data/get-server-time)

##### Orders

- [POST\\
\\
Post a new order](https://docs.polymarket.com/api-reference/trade/post-a-new-order)
- [DEL\\
\\
Cancel single order](https://docs.polymarket.com/api-reference/trade/cancel-single-order)
- [GET\\
\\
Get single order by ID](https://docs.polymarket.com/api-reference/trade/get-single-order-by-id)
- [POST\\
\\
Post multiple orders](https://docs.polymarket.com/api-reference/trade/post-multiple-orders)
- [GET\\
\\
Get user orders](https://docs.polymarket.com/api-reference/trade/get-user-orders)
- [DEL\\
\\
Cancel multiple orders](https://docs.polymarket.com/api-reference/trade/cancel-multiple-orders)
- [DEL\\
\\
Cancel all orders](https://docs.polymarket.com/api-reference/trade/cancel-all-orders)
- [DEL\\
\\
Cancel orders for a market](https://docs.polymarket.com/api-reference/trade/cancel-orders-for-a-market)
- [GET\\
\\
Get order scoring status](https://docs.polymarket.com/api-reference/trade/get-order-scoring-status)
- [POST\\
\\
Send heartbeat](https://docs.polymarket.com/api-reference/trade/send-heartbeat)

##### Trades

- [GET\\
\\
Get trades](https://docs.polymarket.com/api-reference/trade/get-trades)
- [GET\\
\\
Get builder trades](https://docs.polymarket.com/api-reference/trade/get-builder-trades)

##### CLOB Markets

- [GET\\
\\
Get simplified markets](https://docs.polymarket.com/api-reference/markets/get-simplified-markets)
- [GET\\
\\
Get sampling markets](https://docs.polymarket.com/api-reference/markets/get-sampling-markets)
- [GET\\
\\
Get sampling simplified markets](https://docs.polymarket.com/api-reference/markets/get-sampling-simplified-markets)

##### Rebates

- [GET\\
\\
Get current rebated fees for a maker](https://docs.polymarket.com/api-reference/rebates/get-current-rebated-fees-for-a-maker)

##### Rewards

- [GET\\
\\
Get current active rewards configurations](https://docs.polymarket.com/api-reference/rewards/get-current-active-rewards-configurations)
- [GET\\
\\
Get raw rewards for a specific market](https://docs.polymarket.com/api-reference/rewards/get-raw-rewards-for-a-specific-market)
- [GET\\
\\
Get multiple markets with rewards](https://docs.polymarket.com/api-reference/rewards/get-multiple-markets-with-rewards)
- [GET\\
\\
Get earnings for user by date](https://docs.polymarket.com/api-reference/rewards/get-earnings-for-user-by-date)
- [GET\\
\\
Get total earnings for user by date](https://docs.polymarket.com/api-reference/rewards/get-total-earnings-for-user-by-date)
- [GET\\
\\
Get reward percentages for user](https://docs.polymarket.com/api-reference/rewards/get-reward-percentages-for-user)
- [GET\\
\\
Get user earnings and markets configuration](https://docs.polymarket.com/api-reference/rewards/get-user-earnings-and-markets-configuration)

##### Profile

- [GET\\
\\
Get public profile by wallet address](https://docs.polymarket.com/api-reference/profiles/get-public-profile-by-wallet-address)
- [GET\\
\\
Get current positions for a user](https://docs.polymarket.com/api-reference/core/get-current-positions-for-a-user)
- [GET\\
\\
Get closed positions for a user](https://docs.polymarket.com/api-reference/core/get-closed-positions-for-a-user)
- [GET\\
\\
Get user activity](https://docs.polymarket.com/api-reference/core/get-user-activity)
- [GET\\
\\
Get total value of a user's positions](https://docs.polymarket.com/api-reference/core/get-total-value-of-a-users-positions)
- [GET\\
\\
Get trades for a user or markets](https://docs.polymarket.com/api-reference/core/get-trades-for-a-user-or-markets)
- [GET\\
\\
Get total markets a user has traded](https://docs.polymarket.com/api-reference/misc/get-total-markets-a-user-has-traded)
- [GET\\
\\
Get positions for a market](https://docs.polymarket.com/api-reference/core/get-positions-for-a-market)
- [GET\\
\\
Download an accounting snapshot (ZIP of CSVs)](https://docs.polymarket.com/api-reference/misc/download-an-accounting-snapshot-zip-of-csvs)

##### Leaderboard

- [GET\\
\\
Get trader leaderboard rankings](https://docs.polymarket.com/api-reference/core/get-trader-leaderboard-rankings)

##### Builders

- [GET\\
\\
Get aggregated builder leaderboard](https://docs.polymarket.com/api-reference/builders/get-aggregated-builder-leaderboard)
- [GET\\
\\
Get daily builder volume time-series](https://docs.polymarket.com/api-reference/builders/get-daily-builder-volume-time-series)

##### Search

- [GET\\
\\
Search markets, events, and profiles](https://docs.polymarket.com/api-reference/search/search-markets-events-and-profiles)

##### Tags

- [GET\\
\\
List tags](https://docs.polymarket.com/api-reference/tags/list-tags)
- [GET\\
\\
Get tag by id](https://docs.polymarket.com/api-reference/tags/get-tag-by-id)
- [GET\\
\\
Get tag by slug](https://docs.polymarket.com/api-reference/tags/get-tag-by-slug)
- [GET\\
\\
Get related tags (relationships) by tag id](https://docs.polymarket.com/api-reference/tags/get-related-tags-relationships-by-tag-id)
- [GET\\
\\
Get related tags (relationships) by tag slug](https://docs.polymarket.com/api-reference/tags/get-related-tags-relationships-by-tag-slug)
- [GET\\
\\
Get tags related to a tag id](https://docs.polymarket.com/api-reference/tags/get-tags-related-to-a-tag-id)
- [GET\\
\\
Get tags related to a tag slug](https://docs.polymarket.com/api-reference/tags/get-tags-related-to-a-tag-slug)

##### Series

- [GET\\
\\
List series](https://docs.polymarket.com/api-reference/series/list-series)
- [GET\\
\\
Get series by id](https://docs.polymarket.com/api-reference/series/get-series-by-id)

##### Comments

- [GET\\
\\
List comments](https://docs.polymarket.com/api-reference/comments/list-comments)
- [GET\\
\\
Get comments by comment id](https://docs.polymarket.com/api-reference/comments/get-comments-by-comment-id)
- [GET\\
\\
Get comments by user address](https://docs.polymarket.com/api-reference/comments/get-comments-by-user-address)

##### Sports

- [GET\\
\\
Get sports metadata information](https://docs.polymarket.com/api-reference/sports/get-sports-metadata-information)
- [GET\\
\\
Get valid sports market types](https://docs.polymarket.com/api-reference/sports/get-valid-sports-market-types)
- [GET\\
\\
List teams](https://docs.polymarket.com/api-reference/sports/list-teams)

##### Bridge

- [GET\\
\\
Get supported assets](https://docs.polymarket.com/api-reference/bridge/get-supported-assets)
- [POST\\
\\
Create deposit addresses](https://docs.polymarket.com/api-reference/bridge/create-deposit-addresses)
- [POST\\
\\
Get a quote](https://docs.polymarket.com/api-reference/bridge/get-a-quote)
- [GET\\
\\
Get transaction status](https://docs.polymarket.com/api-reference/bridge/get-transaction-status)
- [POST\\
\\
Create withdrawal addresses](https://docs.polymarket.com/api-reference/bridge/create-withdrawal-addresses)

##### Relayer

- [POST\\
\\
Submit a transaction](https://docs.polymarket.com/api-reference/relayer/submit-a-transaction)
- [GET\\
\\
Get a transaction by ID](https://docs.polymarket.com/api-reference/relayer/get-a-transaction-by-id)
- [GET\\
\\
Get recent transactions for a user](https://docs.polymarket.com/api-reference/relayer/get-recent-transactions-for-a-user)
- [GET\\
\\
Get current nonce for a user](https://docs.polymarket.com/api-reference/relayer/get-current-nonce-for-a-user)
- [GET\\
\\
Get relayer address and nonce](https://docs.polymarket.com/api-reference/relayer/get-relayer-address-and-nonce)
- [GET\\
\\
Check if a safe is deployed](https://docs.polymarket.com/api-reference/relayer/check-if-a-safe-is-deployed)
- [GET\\
\\
Get all relayer API keys](https://docs.polymarket.com/api-reference/relayer-api-keys/get-all-relayer-api-keys)

##### WebSocket

- [WSS\\
\\
Market Channel](https://docs.polymarket.com/api-reference/wss/market)
- [WSS\\
\\
User Channel](https://docs.polymarket.com/api-reference/wss/user)
- [WSS\\
\\
Sports Channel](https://docs.polymarket.com/api-reference/wss/sports)

On this page

- [Geoblock Endpoint](https://docs.polymarket.com/api-reference/geoblock#geoblock-endpoint)
- [Response](https://docs.polymarket.com/api-reference/geoblock#response)
- [Blocked Countries](https://docs.polymarket.com/api-reference/geoblock#blocked-countries)
- [Blocked Regions](https://docs.polymarket.com/api-reference/geoblock#blocked-regions)
- [Blocking Logic](https://docs.polymarket.com/api-reference/geoblock#blocking-logic)
- [Server Infrastructure](https://docs.polymarket.com/api-reference/geoblock#server-infrastructure)
- [Usage Examples](https://docs.polymarket.com/api-reference/geoblock#usage-examples)
- [Why These Restrictions](https://docs.polymarket.com/api-reference/geoblock#why-these-restrictions)
- [Next Steps](https://docs.polymarket.com/api-reference/geoblock#next-steps)

Polymarket restricts order placement from certain geographic locations due to regulatory requirements and compliance with international sanctions. Before placing orders, builders should verify the location.

Orders submitted from blocked regions will be rejected. Implement geoblock
checks in your application to provide users with appropriate feedback before
they attempt to trade.

* * *

## [​](https://docs.polymarket.com/api-reference/geoblock\#geoblock-endpoint)  Geoblock Endpoint

Check the geographic eligibility of the requesting IP address:

Copy

Ask AI

```
GET https://polymarket.com/api/geoblock
```

This endpoint is on `polymarket.com`, not the API servers.

### [​](https://docs.polymarket.com/api-reference/geoblock\#response)  Response

Copy

Ask AI

```
{
  "blocked": true,
  "ip": "203.0.113.42",
  "country": "US",
  "region": "NY"
}
```

| Field | Type | Description |
| --- | --- | --- |
| `blocked` | boolean | Whether the user is blocked from placing orders |
| `ip` | string | Detected IP address |
| `country` | string | ISO 3166-1 alpha-2 country code |
| `region` | string | Region/state code |

* * *

## [​](https://docs.polymarket.com/api-reference/geoblock\#blocked-countries)  Blocked Countries

The following countries are restricted from placing orders on Polymarket. Countries marked as **close-only** can close existing positions but cannot open new ones:

| Country Code | Country Name | Status |
| --- | --- | --- |
| AU | Australia | Blocked |
| BE | Belgium | Blocked |
| BY | Belarus | Blocked |
| BI | Burundi | Blocked |
| CF | Central African Republic | Blocked |
| CD | Congo (Kinshasa) | Blocked |
| CU | Cuba | Blocked |
| DE | Germany | Blocked |
| ET | Ethiopia | Blocked |
| FR | France | Blocked |
| GB | United Kingdom | Blocked |
| IR | Iran | Blocked |
| IQ | Iraq | Blocked |
| IT | Italy | Blocked |
| KP | North Korea | Blocked |
| LB | Lebanon | Blocked |
| LY | Libya | Blocked |
| MM | Myanmar | Blocked |
| NI | Nicaragua | Blocked |
| NL | Netherlands | Blocked |
| PL | Poland | Close-only |
| RU | Russia | Blocked |
| SG | Singapore | Close-only |
| SO | Somalia | Blocked |
| SS | South Sudan | Blocked |
| SD | Sudan | Blocked |
| SY | Syria | Blocked |
| TH | Thailand | Close-only |
| TW | Taiwan | Close-only |
| UM | United States Minor Outlying Islands | Blocked |
| US | United States | Blocked |
| VE | Venezuela | Blocked |
| YE | Yemen | Blocked |
| ZW | Zimbabwe | Blocked |

* * *

## [​](https://docs.polymarket.com/api-reference/geoblock\#blocked-regions)  Blocked Regions

In addition to fully blocked countries, the following specific regions within otherwise accessible countries are also restricted:

| Country | Region | Region Code |
| --- | --- | --- |
| Canada (CA) | Ontario | ON |
| Ukraine (UA) | Crimea | 43 |
| Ukraine (UA) | Donetsk | 14 |
| Ukraine (UA) | Luhansk | 09 |

* * *

## [​](https://docs.polymarket.com/api-reference/geoblock\#blocking-logic)  Blocking Logic

The geoblocking system includes:

1. **OFAC-Sanctioned Countries**: Countries sanctioned by the U.S. Office of Foreign Assets Control (OFAC)
2. **Additional Regulatory Restrictions**: Countries added for specific regulatory compliance reasons

* * *

## [​](https://docs.polymarket.com/api-reference/geoblock\#server-infrastructure)  Server Infrastructure

- **Primary Servers**: eu-west-2
- **Closest Non-Georestricted Region**: eu-west-1

* * *

## [​](https://docs.polymarket.com/api-reference/geoblock\#usage-examples)  Usage Examples

- TypeScript

- Python

- Rust


Copy

Ask AI

```
interface GeoblockResponse {
  blocked: boolean;
  ip: string;
  country: string;
  region: string;
}

async function checkGeoblock(): Promise<GeoblockResponse> {
  const response = await fetch("https://polymarket.com/api/geoblock");
  return response.json();
}

// Usage
const geo = await checkGeoblock();

if (geo.blocked) {
  console.log(`Trading not available in ${geo.country}`);
} else {
  console.log("Trading available");
}
```

Copy

Ask AI

```
import requests

def check_geoblock() -> dict:
    response = requests.get("https://polymarket.com/api/geoblock")
    return response.json()

# Usage
geo = check_geoblock()

if geo["blocked"]:
    print(f"Trading not available in {geo['country']}")
else:
    print("Trading available")
```

Copy

Ask AI

```
use polymarket_client_sdk::clob::Client;

let client = Client::default();
let geo = client.check_geoblock().await?;

if geo.blocked {
    println!("Trading not available in {}", geo.country);
} else {
    println!("Trading available");
}
```

* * *

## [​](https://docs.polymarket.com/api-reference/geoblock\#why-these-restrictions)  Why These Restrictions

Geographic restrictions are implemented to ensure compliance with:

- International sanctions and embargoes
- Local financial regulations
- Gambling and prediction market laws
- Anti-money laundering (AML) requirements
- Know Your Customer (KYC) regulations

If you believe you are incorrectly restricted or have questions about geographic availability, please contact [Polymarket Support](https://polymarket.com/support).

* * *

## [​](https://docs.polymarket.com/api-reference/geoblock\#next-steps)  Next Steps

[**Authentication** \\
\\
Learn how to authenticate trading requests.](https://docs.polymarket.com/api-reference/authentication)

[**Place Orders** \\
\\
Start placing orders (from eligible regions).](https://docs.polymarket.com/trading/quickstart)

Was this page helpful?

YesNo

[Clients & SDKs\\
\\
Previous](https://docs.polymarket.com/api-reference/clients-sdks) [List events\\
\\
Next](https://docs.polymarket.com/api-reference/events/list-events)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.

Suggestions

How do I connect to WebSocket streams?What's required to place my first order?How do I find and fetch market data?