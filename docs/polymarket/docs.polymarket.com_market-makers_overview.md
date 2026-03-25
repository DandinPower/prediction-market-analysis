---
url: "https://docs.polymarket.com/market-makers/overview"
title: "Overview - Polymarket Documentation"
---

[Skip to main content](https://docs.polymarket.com/market-makers/overview#content-area)

[Polymarket Documentation home page![light logo](https://mintcdn.com/polymarket-292d1b1b/ZibMe6Tli_amZald/logo/light.svg?fit=max&auto=format&n=ZibMe6Tli_amZald&q=85&s=9f9bd559f02181495794661ef6426c0f)![dark logo](https://mintcdn.com/polymarket-292d1b1b/ZibMe6Tli_amZald/logo/dark.svg?fit=max&auto=format&n=ZibMe6Tli_amZald&q=85&s=13abc6754579a3475368ea99d0f5a241)](https://docs.polymarket.com/)

![US](https://d3gk2c5xim1je2.cloudfront.net/flags/US.svg)

English

Search...

Ctrl KAsk AI

Search...

Navigation

Market Makers

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

- [Getting Started](https://docs.polymarket.com/market-makers/overview#getting-started)
- [Quick Reference](https://docs.polymarket.com/market-makers/overview#quick-reference)
- [What Is in This Section](https://docs.polymarket.com/market-makers/overview#what-is-in-this-section)
- [Risks](https://docs.polymarket.com/market-makers/overview#risks)
- [Support](https://docs.polymarket.com/market-makers/overview#support)

A Market Maker (MM) on Polymarket is a trader who provides liquidity to prediction markets by continuously posting bid and ask orders. By laying the spread, market makers enable other users to trade efficiently while earning the spread as compensation for the risk they take.Market makers are essential to Polymarket’s ecosystem — they provide liquidity across markets, tighten spreads for better user experience, enable price discovery through continuous quoting, and absorb trading flow from retail and institutional users.

**Not a Market Maker?** If you’re building an application that routes orders
for your users, see the [Builder Program](https://docs.polymarket.com/builders/overview) instead.

* * *

## [​](https://docs.polymarket.com/market-makers/overview\#getting-started)  Getting Started

1

[Navigate to header](https://docs.polymarket.com/market-makers/overview#)

Complete Setup

Deploy wallets, fund with USDC.e, and set token approvals. See the [Getting\\
Started](https://docs.polymarket.com/market-makers/getting-started) guide.

2

[Navigate to header](https://docs.polymarket.com/market-makers/overview#)

Connect to Data Feeds

WebSocket for real-time orderbook updates, Gamma API for market metadata.
See [Market Data](https://docs.polymarket.com/market-data/overview).

3

[Navigate to header](https://docs.polymarket.com/market-makers/overview#)

Start Quoting

Post orders via the CLOB REST API. See [Trading](https://docs.polymarket.com/market-makers/trading).

* * *

## [​](https://docs.polymarket.com/market-makers/overview\#quick-reference)  Quick Reference

| Action | Tool | Documentation |
| --- | --- | --- |
| Deposit USDC.e | Bridge API | [Bridge](https://docs.polymarket.com/trading/bridge/deposit) |
| Approve tokens | Relayer Client | [Getting Started](https://docs.polymarket.com/market-makers/getting-started) |
| Post limit orders | CLOB REST API | [Create Orders](https://docs.polymarket.com/trading/orders/create) |
| Monitor orderbook | WebSocket | [WebSocket](https://docs.polymarket.com/market-data/websocket/overview) |
| Split USDC.e to tokens | CTF / Relayer | [Inventory](https://docs.polymarket.com/market-makers/inventory) |
| Merge tokens to USDC.e | CTF / Relayer | [Inventory](https://docs.polymarket.com/market-makers/inventory) |

* * *

## [​](https://docs.polymarket.com/market-makers/overview\#what-is-in-this-section)  What Is in This Section

[**Getting Started** \\
\\
Deposits, token approvals, wallet deployment, API keys](https://docs.polymarket.com/market-makers/getting-started)

[**Trading** \\
\\
Quoting best practices, strategies, and risk controls](https://docs.polymarket.com/market-makers/trading)

[**Inventory Management** \\
\\
Split, merge, and redeem outcome tokens](https://docs.polymarket.com/market-makers/inventory)

[**Liquidity Rewards** \\
\\
Earn rewards for providing liquidity](https://docs.polymarket.com/market-makers/liquidity-rewards)

## [​](https://docs.polymarket.com/market-makers/overview\#risks)  Risks

Be careful with spread management — if your bid price is higher than your ask
price (a “negative spread” or “crossed market”), you will lose money on every
fill. Always validate your quote prices before submission.

## [​](https://docs.polymarket.com/market-makers/overview\#support)  Support

For market maker onboarding and support, contact [support@polymarket.com](mailto:support@polymarket.com).

Was this page helpful?

YesNo

[Deposit Status\\
\\
Previous](https://docs.polymarket.com/trading/bridge/status) [Getting Started\\
\\
Next](https://docs.polymarket.com/market-makers/getting-started)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.

Suggestions

How do I connect to WebSocket streams?What's required to place my first order?How do I find and fetch market data?