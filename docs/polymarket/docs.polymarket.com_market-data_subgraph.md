---
url: "https://docs.polymarket.com/market-data/subgraph"
title: "Subgraph - Polymarket Documentation"
---

[Skip to main content](https://docs.polymarket.com/market-data/subgraph#content-area)

[Polymarket Documentation home page![light logo](https://mintcdn.com/polymarket-292d1b1b/ZibMe6Tli_amZald/logo/light.svg?fit=max&auto=format&n=ZibMe6Tli_amZald&q=85&s=9f9bd559f02181495794661ef6426c0f)![dark logo](https://mintcdn.com/polymarket-292d1b1b/ZibMe6Tli_amZald/logo/dark.svg?fit=max&auto=format&n=ZibMe6Tli_amZald&q=85&s=13abc6754579a3475368ea99d0f5a241)](https://docs.polymarket.com/)

![US](https://d3gk2c5xim1je2.cloudfront.net/flags/US.svg)

English

Search...

Ctrl KAsk AI

Search...

Navigation

Market Data

Subgraph

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

- [Available Subgraphs](https://docs.polymarket.com/market-data/subgraph#available-subgraphs)
- [Querying](https://docs.polymarket.com/market-data/subgraph#querying)
- [Schema Reference](https://docs.polymarket.com/market-data/subgraph#schema-reference)
- [Positions](https://docs.polymarket.com/market-data/subgraph#positions)
- [Orders](https://docs.polymarket.com/market-data/subgraph#orders)
- [Activity](https://docs.polymarket.com/market-data/subgraph#activity)
- [Open Interest](https://docs.polymarket.com/market-data/subgraph#open-interest)
- [PNL](https://docs.polymarket.com/market-data/subgraph#pnl)
- [Source Code](https://docs.polymarket.com/market-data/subgraph#source-code)

Polymarket’s subgraphs provide indexed onchain data via GraphQL. Use them to query positions, volume, liquidity data, orders, activity, and market data.

## [​](https://docs.polymarket.com/market-data/subgraph\#available-subgraphs)  Available Subgraphs

| Subgraph | Description | Endpoint |
| --- | --- | --- |
| **Positions** | User token balances | [GraphQL Playground](https://api.goldsky.com/api/public/project_cl6mb8i9h0003e201j6li0diw/subgraphs/positions-subgraph/0.0.7/gn) |
| **Orders** | Order book and trade events | [GraphQL Playground](https://api.goldsky.com/api/public/project_cl6mb8i9h0003e201j6li0diw/subgraphs/orderbook-subgraph/0.0.1/gn) |
| **Activity** | Splits, merges, redemptions | [GraphQL Playground](https://api.goldsky.com/api/public/project_cl6mb8i9h0003e201j6li0diw/subgraphs/activity-subgraph/0.0.4/gn) |
| **Open Interest** | Market and global OI | [GraphQL Playground](https://api.goldsky.com/api/public/project_cl6mb8i9h0003e201j6li0diw/subgraphs/oi-subgraph/0.0.6/gn) |
| **PNL** | User position P&L | [GraphQL Playground](https://api.goldsky.com/api/public/project_cl6mb8i9h0003e201j6li0diw/subgraphs/pnl-subgraph/0.0.14/gn) |

Subgraphs are hosted by [Goldsky](https://goldsky.com/). Each endpoint includes
an interactive GraphQL playground for exploring the schema.

## [​](https://docs.polymarket.com/market-data/subgraph\#querying)  Querying

Send GraphQL queries via POST request to any subgraph endpoint.

Copy

Ask AI

```
curl -X POST \
  https://api.goldsky.com/api/public/project_cl6mb8i9h0003e201j6li0diw/subgraphs/orderbook-subgraph/0.0.1/gn \
  -H "Content-Type: application/json" \
  -d '{
    "query": "query MyQuery { orderbooks { id tradesQuantity } }"
  }'
```

## [​](https://docs.polymarket.com/market-data/subgraph\#schema-reference)  Schema Reference

### [​](https://docs.polymarket.com/market-data/subgraph\#positions)  Positions

| Query | Description |
| --- | --- |
| `userBalance` / `userBalances` | User token balances |
| `netUserBalance` / `netUserBalances` | Aggregated net balances |
| `tokenIdCondition` / `tokenIdConditions` | Token ID to condition mappings |
| `condition` / `conditions` | Market conditions |

### [​](https://docs.polymarket.com/market-data/subgraph\#orders)  Orders

| Query | Description |
| --- | --- |
| `marketData` / `marketDatas` | Market-level data |
| `orderFilledEvent` / `orderFilledEvents` | Order fill events |
| `ordersMatchedEvent` / `ordersMatchedEvents` | Order match events |
| `orderbook` / `orderbooks` | Orderbook state |
| `ordersMatchedGlobal` / `ordersMatchedGlobals` | Global match statistics |

### [​](https://docs.polymarket.com/market-data/subgraph\#activity)  Activity

| Query | Description |
| --- | --- |
| `split` / `splits` | USDC to token splits |
| `merge` / `merges` | Token to USDC merges |
| `redemption` / `redemptions` | Position redemptions |
| `negRiskConversion` / `negRiskConversions` | Neg risk conversions |
| `negRiskEvent` / `negRiskEvents` | Neg risk event data |
| `fixedProductMarketMaker` / `fixedProductMarketMakers` | FPMM data |
| `position` / `positions` | Position records |
| `condition` / `conditions` | Market conditions |

### [​](https://docs.polymarket.com/market-data/subgraph\#open-interest)  Open Interest

| Query | Description |
| --- | --- |
| `condition` / `conditions` | Market conditions |
| `negRiskEvent` / `negRiskEvents` | Neg risk event data |
| `marketOpenInterest` / `marketOpenInterests` | Per-market open interest |
| `globalOpenInterest` / `globalOpenInterests` | Global open interest |

### [​](https://docs.polymarket.com/market-data/subgraph\#pnl)  PNL

| Query | Description |
| --- | --- |
| `userPosition` / `userPositions` | User position P&L data |
| `negRiskEvent` / `negRiskEvents` | Neg risk event data |
| `condition` / `conditions` | Market conditions |
| `fpmm` / `fpmms` | Fixed product market maker data |

## [​](https://docs.polymarket.com/market-data/subgraph\#source-code)  Source Code

The subgraph is open source. Review the schema and mappings on GitHub:

[**polymarket-subgraph** \\
\\
View source code, schema definitions, and deployment configuration.](https://github.com/Polymarket/polymarket-subgraph)

Was this page helpful?

YesNo

[Fetching Markets\\
\\
Previous](https://docs.polymarket.com/market-data/fetching-markets) [Overview\\
\\
Next](https://docs.polymarket.com/trading/overview)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.

Suggestions

How do I connect to WebSocket streams?What's required to place my first order?How do I find and fetch market data?