---
url: "https://docs.polymarket.com/trading/ctf/split"
title: "Split Tokens - Polymarket Documentation"
---

[Skip to main content](https://docs.polymarket.com/trading/ctf/split#content-area)

[Polymarket Documentation home page![light logo](https://mintcdn.com/polymarket-292d1b1b/ZibMe6Tli_amZald/logo/light.svg?fit=max&auto=format&n=ZibMe6Tli_amZald&q=85&s=9f9bd559f02181495794661ef6426c0f)![dark logo](https://mintcdn.com/polymarket-292d1b1b/ZibMe6Tli_amZald/logo/dark.svg?fit=max&auto=format&n=ZibMe6Tli_amZald&q=85&s=13abc6754579a3475368ea99d0f5a241)](https://docs.polymarket.com/)

![US](https://d3gk2c5xim1je2.cloudfront.net/flags/US.svg)

English

Search...

Ctrl KAsk AI

Search...

Navigation

CTF Tokens

Split Tokens

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

  - [Conditional Token Framework](https://docs.polymarket.com/trading/ctf/overview)
  - [Split Tokens](https://docs.polymarket.com/trading/ctf/split)
  - [Merge Tokens](https://docs.polymarket.com/trading/ctf/merge)
  - [Redeem Tokens](https://docs.polymarket.com/trading/ctf/redeem)
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

- [Prerequisites](https://docs.polymarket.com/trading/ctf/split#prerequisites)
- [How It Works](https://docs.polymarket.com/trading/ctf/split#how-it-works)
- [Function Parameters](https://docs.polymarket.com/trading/ctf/split#function-parameters)
- [Next Steps](https://docs.polymarket.com/trading/ctf/split#next-steps)

**Splitting** converts USDC.e collateral into a full (position) set of outcome tokens. For every $1 USDC.e you split, you receive 1 Yes token and 1 No token.

Copy

Ask AI

```
$100 USDC.e → 100 Yes tokens + 100 No tokens
```

## [​](https://docs.polymarket.com/trading/ctf/split\#prerequisites)  Prerequisites

Before splitting, ensure you have:

1. **USDC.e balance** on Polygon
2. **USDC.e approval** for the CTF contract to spend your tokens
3. **Condition ID** of the market — the condition must already be prepared on the CTF contract (via `prepareCondition`)

If the partition is trivial, invalid, or refers to more slots than the
condition is prepared with, the transaction will revert.

## [​](https://docs.polymarket.com/trading/ctf/split\#how-it-works)  How It Works

1. You approve the CTF contract to spend your USDC.e
2. You call `splitPosition()` with the amount and market details
3. The CTF contract transfers USDC.e from your wallet and mints both outcome tokens

The operation is atomic — if any step fails, the entire transaction reverts.

## [​](https://docs.polymarket.com/trading/ctf/split\#function-parameters)  Function Parameters

[​](https://docs.polymarket.com/trading/ctf/split#param-collateral-token)

collateralToken

IERC20

USDC.e (Bridged USDC) contract address: `0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174`

[​](https://docs.polymarket.com/trading/ctf/split#param-parent-collection-id)

parentCollectionId

bytes32

Always `0x0000...0000` (32 zero bytes) for Polymarket markets

[​](https://docs.polymarket.com/trading/ctf/split#param-condition-id)

conditionId

bytes32

The market’s condition ID, available from the Markets API

[​](https://docs.polymarket.com/trading/ctf/split#param-partition)

partition

uint\[\]

Array of index sets: `[1, 2]` for binary markets (Yes = 1, No = 2)

[​](https://docs.polymarket.com/trading/ctf/split#param-amount)

amount

uint256

The amount of collateral or stake to split. Also the number of full sets to
receive.

## [​](https://docs.polymarket.com/trading/ctf/split\#next-steps)  Next Steps

[**Merge Tokens** \\
\\
Convert token pairs back to USDC.e](https://docs.polymarket.com/trading/ctf/merge)

[**Trade on Orderbook** \\
\\
Place orders using your newly split tokens](https://docs.polymarket.com/trading/orders/create)

Was this page helpful?

YesNo

[Conditional Token Framework\\
\\
Previous](https://docs.polymarket.com/trading/ctf/overview) [Merge Tokens\\
\\
Next](https://docs.polymarket.com/trading/ctf/merge)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.

Suggestions

How do I connect to WebSocket streams?What's required to place my first order?How do I find and fetch market data?