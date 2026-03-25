---
url: "https://docs.polymarket.com/concepts/markets-events"
title: "Markets & Events - Polymarket Documentation"
---

[Skip to main content](https://docs.polymarket.com/concepts/markets-events#content-area)

[Polymarket Documentation home page![light logo](https://mintcdn.com/polymarket-292d1b1b/ZibMe6Tli_amZald/logo/light.svg?fit=max&auto=format&n=ZibMe6Tli_amZald&q=85&s=9f9bd559f02181495794661ef6426c0f)![dark logo](https://mintcdn.com/polymarket-292d1b1b/ZibMe6Tli_amZald/logo/dark.svg?fit=max&auto=format&n=ZibMe6Tli_amZald&q=85&s=13abc6754579a3475368ea99d0f5a241)](https://docs.polymarket.com/)

![US](https://d3gk2c5xim1je2.cloudfront.net/flags/US.svg)

English

Search...

Ctrl KAsk AI

Search...

Navigation

Core Concepts

Markets & Events

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

- [Markets](https://docs.polymarket.com/concepts/markets-events#markets)
- [Market Example](https://docs.polymarket.com/concepts/markets-events#market-example)
- [Events](https://docs.polymarket.com/concepts/markets-events#events)
- [Single-Market Events](https://docs.polymarket.com/concepts/markets-events#single-market-events)
- [Multi-Market Events](https://docs.polymarket.com/concepts/markets-events#multi-market-events)
- [Identifying Markets](https://docs.polymarket.com/concepts/markets-events#identifying-markets)
- [Sports Markets](https://docs.polymarket.com/concepts/markets-events#sports-markets)
- [Next Steps](https://docs.polymarket.com/concepts/markets-events#next-steps)

Every prediction on Polymarket is structured around two core concepts: **markets** and **events**. Understanding how they relate is essential for building on the platform.

![](https://mintcdn.com/polymarket-292d1b1b/FOMte3ewbG-LVy3k/images/core-concepts/event-market.png?fit=max&auto=format&n=FOMte3ewbG-LVy3k&q=85&s=4c62bd08a405868307cdd6799b368ca5)![](https://mintcdn.com/polymarket-292d1b1b/FOMte3ewbG-LVy3k/images/dark/core-concepts/event-market.png?fit=max&auto=format&n=FOMte3ewbG-LVy3k&q=85&s=2eb5c9b0f8a2afe52bc2e717b7b796a2)

## [​](https://docs.polymarket.com/concepts/markets-events\#markets)  Markets

A **market** is the fundamental tradable unit on Polymarket. Each market represents a single binary question with Yes/No outcomes.

![](https://mintcdn.com/polymarket-292d1b1b/FOMte3ewbG-LVy3k/images/core-concepts/event.png?fit=max&auto=format&n=FOMte3ewbG-LVy3k&q=85&s=0c9a264aec9a22ce5a20c4cc7980806d)![](https://mintcdn.com/polymarket-292d1b1b/FOMte3ewbG-LVy3k/images/dark/core-concepts/event.png?fit=max&auto=format&n=FOMte3ewbG-LVy3k&q=85&s=912e41bebfe8c1a43ef53b89685ca3d2)

Every market has:

| Identifier | Description |
| --- | --- |
| **Condition ID** | Unique identifier for the market’s condition in the CTF contracts |
| **Question ID** | Hash of the market question used for resolution |
| **Token IDs** | ERC1155 token IDs used for trading on the CLOB — one for Yes, one for No |

Markets can only be traded via the CLOB if `enableOrderBook` is `true`. Some
markets may exist onchain but not be available for order book trading.

### [​](https://docs.polymarket.com/concepts/markets-events\#market-example)  Market Example

A simple market might be:

> **“Will Bitcoin reach $150,000 by December 2026?”**

This creates two outcome tokens:

- **Yes token** \- Redeemable for `$1` if Bitcoin reaches `$150k`
- **No token** \- Redeemable for `$1` if Bitcoin doesn’t reach `$100k`

## [​](https://docs.polymarket.com/concepts/markets-events\#events)  Events

An **event** is a container that groups one or more related markets together. Events provide organizational structure and enable multi-outcome predictions.

### [​](https://docs.polymarket.com/concepts/markets-events\#single-market-events)  Single-Market Events

When an event contains just one market, it creates a simple market pair. The event and market are essentially equivalent.

Copy

Ask AI

```
Event: Will Bitcoin reach $100,000 by December 2024?
└── Market: Will Bitcoin reach $100,000 by December 2024? (Yes/No)
```

### [​](https://docs.polymarket.com/concepts/markets-events\#multi-market-events)  Multi-Market Events

When an event contains two or more markets, it creates a grouped market pair. This enables mutually exclusive multi-outcome predictions.

Copy

Ask AI

```
Event: Who will win the 2024 Presidential Election?
├── Market: Donald Trump? (Yes/No)
├── Market: Joe Biden? (Yes/No)
├── Market: Kamala Harris? (Yes/No)
└── Market: Other? (Yes/No)
```

## [​](https://docs.polymarket.com/concepts/markets-events\#identifying-markets)  Identifying Markets

Every market and event has a unique **slug** that appears in the Polymarket URL:

Copy

Ask AI

```
https://polymarket.com/event/fed-decision-in-october
                              └── slug: fed-decision-in-october
```

You can use slugs to fetch specific markets or events from the API:

Copy

Ask AI

```
# Fetch event by slug
curl "https://gamma-api.polymarket.com/events?slug=fed-decision-in-october"
```

## [​](https://docs.polymarket.com/concepts/markets-events\#sports-markets)  Sports Markets

Specifically for sports markets, outstanding limit orders are **automatically cancelled** once the game begins, clearing the order book at the official start time. However, game start times can shift — if a game starts earlier than scheduled, orders may not be cleared in time. Always monitor your orders closely around game start times.

* * *

## [​](https://docs.polymarket.com/concepts/markets-events\#next-steps)  Next Steps

[**Prices & Orderbook** \\
\\
Learn how prices are determined and how the order book works.](https://docs.polymarket.com/concepts/prices-orderbook)

[**Fetching Market Data** \\
\\
Start querying markets and events from the API.](https://docs.polymarket.com/market-data/overview)

Was this page helpful?

YesNo

[Quickstart\\
\\
Previous](https://docs.polymarket.com/quickstart) [Prices & Orderbook\\
\\
Next](https://docs.polymarket.com/concepts/prices-orderbook)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.

Suggestions

How do I connect to WebSocket streams?What's required to place my first order?How do I find and fetch market data?

![](https://mintcdn.com/polymarket-292d1b1b/FOMte3ewbG-LVy3k/images/core-concepts/event-market.png?w=840&fit=max&auto=format&n=FOMte3ewbG-LVy3k&q=85&s=603c382f66e84f9020d45cd43ac59ea4)

![](https://mintcdn.com/polymarket-292d1b1b/FOMte3ewbG-LVy3k/images/dark/core-concepts/event-market.png?w=840&fit=max&auto=format&n=FOMte3ewbG-LVy3k&q=85&s=420de664532386a57e674c37e2475f45)

![](https://mintcdn.com/polymarket-292d1b1b/FOMte3ewbG-LVy3k/images/core-concepts/event.png?w=840&fit=max&auto=format&n=FOMte3ewbG-LVy3k&q=85&s=1afd89af327cef04f03a0c085a4a0ef5)

![](https://mintcdn.com/polymarket-292d1b1b/FOMte3ewbG-LVy3k/images/dark/core-concepts/event.png?w=840&fit=max&auto=format&n=FOMte3ewbG-LVy3k&q=85&s=71d440db449638eec0f3b8a5d80bef13)