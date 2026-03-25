---
url: "https://docs.polymarket.com/market-data/overview"
title: "Overview - Polymarket Documentation"
---

[Skip to main content](https://docs.polymarket.com/market-data/overview#content-area)

[Polymarket Documentation home page![light logo](https://mintcdn.com/polymarket-292d1b1b/ZibMe6Tli_amZald/logo/light.svg?fit=max&auto=format&n=ZibMe6Tli_amZald&q=85&s=9f9bd559f02181495794661ef6426c0f)![dark logo](https://mintcdn.com/polymarket-292d1b1b/ZibMe6Tli_amZald/logo/dark.svg?fit=max&auto=format&n=ZibMe6Tli_amZald&q=85&s=13abc6754579a3475368ea99d0f5a241)](https://docs.polymarket.com/)

![US](https://d3gk2c5xim1je2.cloudfront.net/flags/US.svg)

English

Search...

Ctrl KAsk AI

Search...

Navigation

Market Data

Overview

[Documentation](https://docs.polymarket.com/) [API Reference](https://docs.polymarket.com/api-reference/introduction)

![https://raw.githubusercontent.com/suhailkakar/demo/refs/heads/main/book.svg](https://raw.githubusercontent.com/suhailkakar/demo/refs/heads/main/book.svg)

##### Getting Started

- [Overview](https://docs.polymarket.com/)
- [Polymarket 101](https://docs.polymarket.com/polymarket-101)
- [Quickstart](https://docs.polymarket.com/quickstart)

![https://mintlify.s3.us-west-1.amazonaws.com/polymarket-292d1b1b/images/icons/nav/layers.svg](https://mintlify.s3.us-west-1.amazonaws.com/polymarket-292d1b1b/images/icons/nav/layers.svg)

##### Core Concepts

- [Markets & Events](https://docs.polymarket.com/concepts/markets-events)
- [Prices & Orderbook](https://docs.polymarket.com/concepts/prices-orderbook)
- [Positions & Tokens](https://docs.polymarket.com/concepts/positions-tokens)
- [Order Lifecycle](https://docs.polymarket.com/concepts/order-lifecycle)
- [Resolution](https://docs.polymarket.com/concepts/resolution)

![https://mintlify.s3.us-west-1.amazonaws.com/polymarket-292d1b1b/images/icons/nav/paper.svg](https://mintlify.s3.us-west-1.amazonaws.com/polymarket-292d1b1b/images/icons/nav/paper.svg)

##### Market Data

- [Overview](https://docs.polymarket.com/market-data/overview)
- [Fetching Markets](https://docs.polymarket.com/market-data/fetching-markets)
- [Subgraph](https://docs.polymarket.com/market-data/subgraph)

![https://mintlify.s3.us-west-1.amazonaws.com/polymarket-292d1b1b/images/icons/nav/chart.svg](https://mintlify.s3.us-west-1.amazonaws.com/polymarket-292d1b1b/images/icons/nav/chart.svg)

##### Trading

- [Overview](https://docs.polymarket.com/trading/overview)
- [Quickstart](https://docs.polymarket.com/trading/quickstart)
- [Orderbook](https://docs.polymarket.com/trading/orderbook)
- Orders

- Client Reference

- [Fees](https://docs.polymarket.com/trading/fees)
- [Gasless Transactions](https://docs.polymarket.com/trading/gasless)
- [Negative Risk Markets](https://docs.polymarket.com/advanced/neg-risk)
- [Matching Engine Restarts](https://docs.polymarket.com/trading/matching-engine)
- CTF Tokens

- WebSocket

- Bridge


![https://mintlify.s3.us-west-1.amazonaws.com/polymarket-292d1b1b/images/icons/nav/histogram.svg](https://mintlify.s3.us-west-1.amazonaws.com/polymarket-292d1b1b/images/icons/nav/histogram.svg)

##### Market Makers

- [Overview](https://docs.polymarket.com/market-makers/overview)
- [Getting Started](https://docs.polymarket.com/market-makers/getting-started)
- [Maker Rebates Program](https://docs.polymarket.com/market-makers/maker-rebates)
- [Liquidity Rewards](https://docs.polymarket.com/market-makers/liquidity-rewards)
- Operations


![https://mintlify.s3.us-west-1.amazonaws.com/polymarket-292d1b1b/images/icons/nav/trophy.svg](https://mintlify.s3.us-west-1.amazonaws.com/polymarket-292d1b1b/images/icons/nav/trophy.svg)

##### Builder Program

- [Builder Program](https://docs.polymarket.com/builders/overview)
- [API Keys](https://docs.polymarket.com/builders/api-keys)
- [Tiers](https://docs.polymarket.com/builders/tiers)

![https://mintlify.s3.us-west-1.amazonaws.com/polymarket-292d1b1b/images/icons/nav/book-search.svg](https://mintlify.s3.us-west-1.amazonaws.com/polymarket-292d1b1b/images/icons/nav/book-search.svg)

##### Resources

- [Contract Addresses](https://docs.polymarket.com/resources/contract-addresses)
- [Blockchain Data Resources](https://docs.polymarket.com/resources/blockchain-data)
- [Error Codes](https://docs.polymarket.com/resources/error-codes)

On this page

- [Data Model](https://docs.polymarket.com/market-data/overview#data-model)
- [Single-Market Events vs Multi-Market Events](https://docs.polymarket.com/market-data/overview#single-market-events-vs-multi-market-events)
- [Outcomes and Prices](https://docs.polymarket.com/market-data/overview#outcomes-and-prices)
- [Available Data](https://docs.polymarket.com/market-data/overview#available-data)
- [Gamma API - Events Markets and Discovery](https://docs.polymarket.com/market-data/overview#gamma-api-events-markets-and-discovery)
- [CLOB API - Prices and Orderbooks](https://docs.polymarket.com/market-data/overview#clob-api-prices-and-orderbooks)
- [Data API - Positions Trades and Analytics](https://docs.polymarket.com/market-data/overview#data-api-positions-trades-and-analytics)
- [Next Steps](https://docs.polymarket.com/market-data/overview#next-steps)

All market data is available through public REST endpoints. No API key, no authentication, no wallet required.

Copy

Ask AI

```
curl "https://gamma-api.polymarket.com/events?limit=5"
```

* * *

## [​](https://docs.polymarket.com/market-data/overview\#data-model)  Data Model

Polymarket structures data using two organizational models. The most fundamental element is always markets—events simply provide additional organization.

1

[Navigate to header](https://docs.polymarket.com/market-data/overview#)

Event

A top-level object representing a question (e.g., “Who will win the 2024
Presidential Election?”). Contains one or more markets.

2

[Navigate to header](https://docs.polymarket.com/market-data/overview#)

Market

A specific tradable binary outcome within an event. Maps to a pair of CLOB
token IDs, a market address, a question ID, and a condition ID.

### [​](https://docs.polymarket.com/market-data/overview\#single-market-events-vs-multi-market-events)  Single-Market Events vs Multi-Market Events

| Type | Example |
| --- | --- |
| Single-market event | ”Will Bitcoin reach $100k?” → 1 market (Yes/No) |
| Multi-market event | ”Where will Barron Trump attend College?” → Markets for Georgetown, NYU, UPenn, Harvard, Other |

### [​](https://docs.polymarket.com/market-data/overview\#outcomes-and-prices)  Outcomes and Prices

Each market has `outcomes` and `outcomePrices` arrays that map 1:1. Prices represent implied probabilities:

Copy

Ask AI

```
{
  "outcomes": "[\"Yes\", \"No\"]",
  "outcomePrices": "[\"0.20\", \"0.80\"]"
}
// Index 0: "Yes" → 0.20 (20% probability)
// Index 1: "No" → 0.80 (80% probability)
```

Markets can be traded via the CLOB if `enableOrderBook` is `true`.

* * *

## [​](https://docs.polymarket.com/market-data/overview\#available-data)  Available Data

Endpoints are split across three APIs. See the [API Reference](https://docs.polymarket.com/api-reference/introduction) for full endpoint documentation with parameters and response schemas.

### [​](https://docs.polymarket.com/market-data/overview\#gamma-api-events-markets-and-discovery)  Gamma API - Events Markets and Discovery

| Endpoint | Description |
| --- | --- |
| `GET /events` | List events with filtering and pagination |
| `GET /events/{id}` | Get a single event by ID |
| `GET /markets` | List markets with filtering and pagination |
| `GET /markets/{id}` | Get a single market by ID |
| `GET /public-search` | Search across events, markets, and profiles |
| `GET /tags` | Ranked tags/categories |
| `GET /series` | Series (grouped events) |
| `GET /sports` | Sports metadata |
| `GET /teams` | Teams |

### [​](https://docs.polymarket.com/market-data/overview\#clob-api-prices-and-orderbooks)  CLOB API - Prices and Orderbooks

| Endpoint | Description |
| --- | --- |
| `GET /price` | Price for a single token |
| `GET /prices` | Prices for multiple tokens |
| `GET /book` | Order book for a token |
| `POST /books` | Order books for multiple tokens |
| `GET /prices-history` | Historical price data for a token |
| `GET /midpoint` | Midpoint price for a token |
| `GET /spread` | Spread for a token |

### [​](https://docs.polymarket.com/market-data/overview\#data-api-positions-trades-and-analytics)  Data API - Positions Trades and Analytics

| Endpoint | Description |
| --- | --- |
| `GET /positions?user={address}` | Current positions for a user |
| `GET /closed-positions?user={address}` | Closed positions for a user |
| `GET /activity?user={address}` | Onchain activity for a user |
| `GET /value?user={address}` | Total position value |
| `GET /oi` | Open interest for a market |
| `GET /holders` | Top holders of a market |
| `GET /trades` | Trade history |

* * *

## [​](https://docs.polymarket.com/market-data/overview\#next-steps)  Next Steps

[**Fetching Markets** \\
\\
Three strategies for discovering and querying markets.](https://docs.polymarket.com/market-data/fetching-markets)

[**API Reference** \\
\\
Full endpoint documentation with parameters and response schemas.](https://docs.polymarket.com/api-reference/introduction)

Was this page helpful?

YesNo

[Resolution\\
\\
Previous](https://docs.polymarket.com/concepts/resolution) [Fetching Markets\\
\\
Next](https://docs.polymarket.com/market-data/fetching-markets)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.

Suggestions

How do I connect to WebSocket streams?What's required to place my first order?How do I find and fetch market data?