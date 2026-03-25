---
url: "https://docs.polymarket.com/advanced/neg-risk"
title: "Negative Risk Markets - Polymarket Documentation"
---

[Skip to main content](https://docs.polymarket.com/advanced/neg-risk#content-area)

[Polymarket Documentation home page![light logo](https://mintcdn.com/polymarket-292d1b1b/ZibMe6Tli_amZald/logo/light.svg?fit=max&auto=format&n=ZibMe6Tli_amZald&q=85&s=9f9bd559f02181495794661ef6426c0f)![dark logo](https://mintcdn.com/polymarket-292d1b1b/ZibMe6Tli_amZald/logo/dark.svg?fit=max&auto=format&n=ZibMe6Tli_amZald&q=85&s=13abc6754579a3475368ea99d0f5a241)](https://docs.polymarket.com/)

![US](https://d3gk2c5xim1je2.cloudfront.net/flags/US.svg)

English

Search...

Ctrl KAsk AI

Search...

Navigation

Trading

Negative Risk Markets

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

- [How It Works](https://docs.polymarket.com/advanced/neg-risk#how-it-works)
- [Example](https://docs.polymarket.com/advanced/neg-risk#example)
- [Identifying Neg Risk Markets](https://docs.polymarket.com/advanced/neg-risk#identifying-neg-risk-markets)
- [Contract Addresses](https://docs.polymarket.com/advanced/neg-risk#contract-addresses)
- [Augmented Negative Risk](https://docs.polymarket.com/advanced/neg-risk#augmented-negative-risk)
- [How Placeholders Work](https://docs.polymarket.com/advanced/neg-risk#how-placeholders-work)
- [Trading Rules for Augmented Neg Risk](https://docs.polymarket.com/advanced/neg-risk#trading-rules-for-augmented-neg-risk)
- [Identifying Augmented Neg Risk](https://docs.polymarket.com/advanced/neg-risk#identifying-augmented-neg-risk)
- [Technical Details](https://docs.polymarket.com/advanced/neg-risk#technical-details)
- [Conversion Mechanics](https://docs.polymarket.com/advanced/neg-risk#conversion-mechanics)
- [Resources](https://docs.polymarket.com/advanced/neg-risk#resources)
- [Next Steps](https://docs.polymarket.com/advanced/neg-risk#next-steps)

**Negative risk** is a mechanism for multi-outcome events where only one outcome can win. It enables capital-efficient trading by allowing positions across all outcomes within an event to be related through a **conversion** operation.

## [​](https://docs.polymarket.com/advanced/neg-risk\#how-it-works)  How It Works

In a standard multi-outcome event, each market is independent. If you want to bet against one outcome, you must buy that outcome’s No tokens—but those No tokens have no relationship to the other outcomes.Negative risk changes this. In a neg risk event:

- A **No share** in any market can be converted into **1 Yes share in every other market**
- This conversion happens through the Neg Risk Adapter contract

### [​](https://docs.polymarket.com/advanced/neg-risk\#example)  Example

Consider an event: “Who will win the 2024 Presidential Election?” with three outcomes:

| Outcome | Your Position |
| --- | --- |
| Trump | — |
| Harris | — |
| Other | 1 No |

With negative risk, that 1 No on “Other” can be converted into:

| Outcome | After Conversion |
| --- | --- |
| Trump | 1 Yes |
| Harris | 1 Yes |
| Other | — |

This is capital-efficient because betting against one outcome is economically equivalent to betting _for_ all other outcomes.

## [​](https://docs.polymarket.com/advanced/neg-risk\#identifying-neg-risk-markets)  Identifying Neg Risk Markets

The Gamma API includes a `negRisk` boolean on events and markets:

Copy

Ask AI

```
{
  "id": "123",
  "title": "Who will win the 2024 Presidential Election?",
  "negRisk": true,
  "markets": [...]
}
```

When placing orders on neg risk markets, you must specify this in your order options:

Copy

Ask AI

```
const response = await client.createAndPostOrder(
  {
    tokenID: "TOKEN_ID",
    price: 0.5,
    size: 100,
    side: Side.BUY,
  },
  {
    tickSize: "0.01",
    negRisk: true, // Required for neg risk markets
  },
);
```

## [​](https://docs.polymarket.com/advanced/neg-risk\#contract-addresses)  Contract Addresses

Neg risk markets use different contracts than standard markets:See [Contract Addresses](https://docs.polymarket.com/resources/contract-addresses) for the Neg Risk Adapter and Neg Risk CTF Exchange addresses.

## [​](https://docs.polymarket.com/advanced/neg-risk\#augmented-negative-risk)  Augmented Negative Risk

Standard negative risk requires the complete set of outcomes to be known at market creation. But sometimes new outcomes emerge after trading begins (e.g., a new candidate enters a race).**Augmented negative risk** solves this with:

| Outcome Type | Description |
| --- | --- |
| **Named outcomes** | Known outcomes (e.g., “Trump”, “Harris”) |
| **Placeholder outcomes** | Reserved slots that can be clarified later (e.g., “Person A”) |
| **Explicit Other** | Catches any outcome not explicitly named |

### [​](https://docs.polymarket.com/advanced/neg-risk\#how-placeholders-work)  How Placeholders Work

1. Event launches with named outcomes + placeholders + “Other”
2. When a new outcome emerges, a placeholder is clarified via the bulletin board
3. The “Other” definition narrows as placeholders are assigned

### [​](https://docs.polymarket.com/advanced/neg-risk\#trading-rules-for-augmented-neg-risk)  Trading Rules for Augmented Neg Risk

Only trade on **named outcomes**. Placeholder outcomes should be ignored until
they are named or until resolution occurs. The Polymarket UI does not display
unnamed outcomes.

- If the correct outcome at resolution is not named, the market resolves to “Other”
- The “Other” outcome’s definition changes as placeholders are clarified—avoid trading it directly

### [​](https://docs.polymarket.com/advanced/neg-risk\#identifying-augmented-neg-risk)  Identifying Augmented Neg Risk

An event is augmented neg risk when both flags are true:

Copy

Ask AI

```
{
  "enableNegRisk": true,
  "negRiskAugmented": true
}
```

The Gamma API includes a boolean field `negRisk` on events and markets, which indicates whether the event uses negative risk. For augmented neg risk events, an additional `enableNegRisk` field is also `true`. When placing orders, the SDK option is always `negRisk: true` / `neg_risk: True` regardless of whether the market is standard or augmented neg risk.

## [​](https://docs.polymarket.com/advanced/neg-risk\#technical-details)  Technical Details

### [​](https://docs.polymarket.com/advanced/neg-risk\#conversion-mechanics)  Conversion Mechanics

The conversion operation is atomic and happens through the Neg Risk Adapter:

1. You hold 1 No token for Outcome A
2. Call the convert function on the adapter
3. You receive 1 Yes token for every other outcome in the event

## [​](https://docs.polymarket.com/advanced/neg-risk\#resources)  Resources

- [Neg Risk Adapter Source Code](https://github.com/Polymarket/neg-risk-ctf-adapter)
- [Gamma API Documentation](https://docs.polymarket.com/market-data/overview)

## [​](https://docs.polymarket.com/advanced/neg-risk\#next-steps)  Next Steps

[**Markets & Events** \\
\\
Understand how multi-market events are structured.](https://docs.polymarket.com/concepts/markets-events)

[**Positions & Tokens** \\
\\
Learn about token operations like split, merge, and redeem.](https://docs.polymarket.com/concepts/positions-tokens)

Was this page helpful?

YesNo

[Gasless Transactions\\
\\
Previous](https://docs.polymarket.com/trading/gasless) [Matching Engine Restarts\\
\\
Next](https://docs.polymarket.com/trading/matching-engine)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.

Suggestions

How do I connect to WebSocket streams?What's required to place my first order?How do I find and fetch market data?