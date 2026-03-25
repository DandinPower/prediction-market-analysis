---
url: "https://docs.polymarket.com/trading/ctf/redeem"
title: "Redeem Tokens - Polymarket Documentation"
---

[Skip to main content](https://docs.polymarket.com/trading/ctf/redeem#content-area)

[Polymarket Documentation home page![light logo](https://mintcdn.com/polymarket-292d1b1b/ZibMe6Tli_amZald/logo/light.svg?fit=max&auto=format&n=ZibMe6Tli_amZald&q=85&s=9f9bd559f02181495794661ef6426c0f)![dark logo](https://mintcdn.com/polymarket-292d1b1b/ZibMe6Tli_amZald/logo/dark.svg?fit=max&auto=format&n=ZibMe6Tli_amZald&q=85&s=13abc6754579a3475368ea99d0f5a241)](https://docs.polymarket.com/)

![US](https://d3gk2c5xim1je2.cloudfront.net/flags/US.svg)

English

Search...

Ctrl KAsk AI

Search...

Navigation

CTF Tokens

Redeem Tokens

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

- [When to Redeem](https://docs.polymarket.com/trading/ctf/redeem#when-to-redeem)
- [How Resolution Works](https://docs.polymarket.com/trading/ctf/redeem#how-resolution-works)
- [Prerequisites](https://docs.polymarket.com/trading/ctf/redeem#prerequisites)
- [Function Parameters](https://docs.polymarket.com/trading/ctf/redeem#function-parameters)
- [Payout Mechanics](https://docs.polymarket.com/trading/ctf/redeem#payout-mechanics)
- [Next Steps](https://docs.polymarket.com/trading/ctf/redeem#next-steps)

**Redeeming** converts winning outcome tokens into USDC.e after a market resolves. Each winning token is worth exactly 1.00—thelosingtokenisworth1.00 — the losing token is worth 1.00—thelosingtokenisworth0.

Copy

Ask AI

```
Market resolves YES:
  100 Yes tokens → $100 USDC.e
  100 No tokens  → $0
```

## [​](https://docs.polymarket.com/trading/ctf/redeem\#when-to-redeem)  When to Redeem

Redemption is only available **after a market resolves**. Once the oracle reports the outcome:

- **Winning tokens** can be redeemed for $1.00 USDC.e each
- **Losing tokens** are worth $0 and produce no payout

You can redeem at any time after resolution — there’s no deadline. Your
winning tokens will always be redeemable.

## [​](https://docs.polymarket.com/trading/ctf/redeem\#how-resolution-works)  How Resolution Works

1. The market’s end condition is met (event occurs, date passes, etc.)
2. The UMA Adapter oracle reports the outcome via `reportPayouts()`
3. The CTF contract records the payout vector
4. Redemption becomes available for winning tokens

## [​](https://docs.polymarket.com/trading/ctf/redeem\#prerequisites)  Prerequisites

Before redeeming:

1. **Market must be resolved** — check the market’s `resolved` status
2. **Hold winning tokens** — only the winning outcome can be redeemed
3. **Know the condition ID** — required for the redemption call

## [​](https://docs.polymarket.com/trading/ctf/redeem\#function-parameters)  Function Parameters

[​](https://docs.polymarket.com/trading/ctf/redeem#param-collateral-token)

collateralToken

IERC20

USDC.e (Bridged USDC) contract address: `0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174`

[​](https://docs.polymarket.com/trading/ctf/redeem#param-parent-collection-id)

parentCollectionId

bytes32

Always `0x0000...0000` (32 zero bytes) for Polymarket markets

[​](https://docs.polymarket.com/trading/ctf/redeem#param-condition-id)

conditionId

bytes32

The market’s condition ID

[​](https://docs.polymarket.com/trading/ctf/redeem#param-index-sets)

indexSets

uint\[\]

Array of index sets to redeem: `[1, 2]` redeems both outcomes (only winning
pays)

Redemption burns your entire token balance for the condition — there is no
amount parameter.

## [​](https://docs.polymarket.com/trading/ctf/redeem\#payout-mechanics)  Payout Mechanics

The CTF uses a **payout vector** to determine redemption values:

| Outcome | Payout Vector | Redemption |
| --- | --- | --- |
| Yes wins | `[1, 0]` | Yes = 1,No=1, No = 1,No=0 |
| No wins | `[0, 1]` | Yes = 0,No=0, No = 0,No=1 |

When you call `redeemPositions()`:

- Your token balance is multiplied by the payout
- Winning tokens are burned
- USDC.e is transferred to your wallet
- Losing tokens are burned as well, but produce a $0 payout

## [​](https://docs.polymarket.com/trading/ctf/redeem\#next-steps)  Next Steps

[**CTF Overview** \\
\\
Learn more about the Conditional Token Framework](https://docs.polymarket.com/trading/ctf/overview)

[**Resolution Process** \\
\\
Understand how markets are resolved](https://docs.polymarket.com/concepts/resolution)

Was this page helpful?

YesNo

[Merge Tokens\\
\\
Previous](https://docs.polymarket.com/trading/ctf/merge) [Overview\\
\\
Next](https://docs.polymarket.com/market-data/websocket/overview)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.

Suggestions

How do I connect to WebSocket streams?What's required to place my first order?How do I find and fetch market data?