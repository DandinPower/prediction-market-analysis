---
url: "https://docs.polymarket.com/concepts/order-lifecycle"
title: "Order Lifecycle - Polymarket Documentation"
---

[Skip to main content](https://docs.polymarket.com/concepts/order-lifecycle#content-area)

[Polymarket Documentation home page![light logo](https://mintcdn.com/polymarket-292d1b1b/ZibMe6Tli_amZald/logo/light.svg?fit=max&auto=format&n=ZibMe6Tli_amZald&q=85&s=9f9bd559f02181495794661ef6426c0f)![dark logo](https://mintcdn.com/polymarket-292d1b1b/ZibMe6Tli_amZald/logo/dark.svg?fit=max&auto=format&n=ZibMe6Tli_amZald&q=85&s=13abc6754579a3475368ea99d0f5a241)](https://docs.polymarket.com/)

![US](https://d3gk2c5xim1je2.cloudfront.net/flags/US.svg)

English

Search...

Ctrl KAsk AI

Search...

Navigation

Core Concepts

Order Lifecycle

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

- [How Orders Work](https://docs.polymarket.com/concepts/order-lifecycle#how-orders-work)
- [Order Types](https://docs.polymarket.com/concepts/order-lifecycle#order-types)
- [Post-Only Orders](https://docs.polymarket.com/concepts/order-lifecycle#post-only-orders)
- [Order Statuses](https://docs.polymarket.com/concepts/order-lifecycle#order-statuses)
- [Trade Statuses](https://docs.polymarket.com/concepts/order-lifecycle#trade-statuses)
- [Maker vs Taker](https://docs.polymarket.com/concepts/order-lifecycle#maker-vs-taker)
- [Cancellation](https://docs.polymarket.com/concepts/order-lifecycle#cancellation)
- [Requirements](https://docs.polymarket.com/concepts/order-lifecycle#requirements)
- [Next Steps](https://docs.polymarket.com/concepts/order-lifecycle#next-steps)

Every trade on Polymarket follows a specific lifecycle. Orders are created offchain, matched by an operator, and settled onchain through smart contracts. This hybrid approach combines the speed of centralized matching with the security of blockchain settlement.

![](https://mintcdn.com/polymarket-292d1b1b/FOMte3ewbG-LVy3k/images/core-concepts/order-lifecycle.png?fit=max&auto=format&n=FOMte3ewbG-LVy3k&q=85&s=4db07008193421bfe359afe44b5f604e)![](https://mintcdn.com/polymarket-292d1b1b/FOMte3ewbG-LVy3k/images/dark/core-concepts/order-lifecycle.png?fit=max&auto=format&n=FOMte3ewbG-LVy3k&q=85&s=5a0f3eba2f20c44471bae05c0670de4a)

## [​](https://docs.polymarket.com/concepts/order-lifecycle\#how-orders-work)  How Orders Work

All orders on Polymarket are **limit orders**. A limit order specifies the price you’re willing to pay (or accept) and the quantity you want to trade.

“Market orders” are simply limit orders with a price set to execute
immediately against the best available resting orders.

Orders are **EIP712-signed messages**. When you place an order, you sign a structured message with your private key. This signature authorizes the Exchange contract to execute the trade on your behalf—without ever taking custody of your funds.

## [​](https://docs.polymarket.com/concepts/order-lifecycle\#order-types)  Order Types

| Type | Behavior | Use Case |
| --- | --- | --- |
| **GTC** | Good Till Cancelled — rests on book until filled or cancelled | Standard limit orders |
| **GTD** | Good Till Date — auto-expires at specified time | Time-limited orders |
| **FOK** | Fill Or Kill — fill entirely or cancel immediately | All-or-nothing execution |
| **FAK** | Fill And Kill — fill what’s available, cancel the rest | Partial fills acceptable |

### [​](https://docs.polymarket.com/concepts/order-lifecycle\#post-only-orders)  Post-Only Orders

Post-only orders will only rest on the book. If a post-only order would match immediately (cross the spread), it’s rejected instead of executed. This guarantees you’re always the maker, never the taker.

1

[Navigate to header](https://docs.polymarket.com/concepts/order-lifecycle#)

Create and Sign

Your client creates an order object containing:

- Token ID (which outcome you’re trading)
- Side (buy or sell)
- Price and size
- Expiration time
- Nonce (for replay protection)

You sign this order with your private key, creating an EIP712 signature.

2

[Navigate to header](https://docs.polymarket.com/concepts/order-lifecycle#)

Submit to CLOB

The signed order is submitted to the Central Limit Order Book (CLOB) operator. The operator validates:

- Signature is valid
- You have sufficient balance
- You have set the required allowances
- Price meets minimum tick size requirements

3

[Navigate to header](https://docs.polymarket.com/concepts/order-lifecycle#)

Match or Rest

**If the order is marketable** (your buy price ≥ lowest ask, or your sell price ≤ highest bid), it matches immediately against resting orders.**If the order is not marketable**, it rests on the book waiting for a counterparty. It remains open until:

- Another order matches against it
- You cancel it
- It expires (GTD orders only)

4

[Navigate to header](https://docs.polymarket.com/concepts/order-lifecycle#)

Settlement

When orders match, the operator submits the trade to the blockchain. The Exchange contract:

- Verifies both signatures
- Transfers tokens from seller to buyer
- Transfers USDC.e from buyer to seller

Settlement is **atomic**—either the entire trade succeeds or nothing happens.

5

[Navigate to header](https://docs.polymarket.com/concepts/order-lifecycle#)

Confirmation

The trade achieves finality on Polygon. Your token balances update and the trade appears in your history.

## [​](https://docs.polymarket.com/concepts/order-lifecycle\#order-statuses)  Order Statuses

When you place an order, it receives one of these statuses:

| Status | Description |
| --- | --- |
| `live` | Order is resting on the book |
| `matched` | Order matched immediately |
| `delayed` | Marketable order subject to a 3-second matching delay (sports markets) |
| `unmatched` | Marketable order placed on the book after the delay expired without a match |

## [​](https://docs.polymarket.com/concepts/order-lifecycle\#trade-statuses)  Trade Statuses

After matching, trades progress through these statuses:

| Status | Terminal | Description |
| --- | --- | --- |
| `MATCHED` | No | Trade matched, sent to executor for onchain submission |
| `MINED` | No | Transaction mined into the blockchain |
| `CONFIRMED` | Yes | Trade achieved finality, successful |
| `RETRYING` | No | Transaction failed, being retried |
| `FAILED` | Yes | Trade failed permanently |

## [​](https://docs.polymarket.com/concepts/order-lifecycle\#maker-vs-taker)  Maker vs Taker

| Role | Description | When |
| --- | --- | --- |
| **Maker** | Adds liquidity to the book | Your order rests and is later matched |
| **Taker** | Removes liquidity from the book | Your order matches immediately against resting orders |

Price improvement always benefits the taker. If you place a buy order at `$0.55` and it matches against a resting sell at `$0.52`, you pay `$0.52`.

## [​](https://docs.polymarket.com/concepts/order-lifecycle\#cancellation)  Cancellation

You can cancel orders at any time before they’re matched:

- **Via API** — Cancel through the CLOB API (instant)
- **Onchain** — Cancel directly on the Exchange contract (fallback if API is unavailable)

Partial fills cannot be cancelled—only the unfilled portion of an order can be cancelled.

## [​](https://docs.polymarket.com/concepts/order-lifecycle\#requirements)  Requirements

Before placing orders, ensure:

| Requirement | Description |
| --- | --- |
| **Balance** | Sufficient USDC.e (for buys) or tokens (for sells) |
| **Allowance** | Approve the Exchange contract to spend your assets |
| **API Credentials** | Valid API key for authenticated endpoints |

Order size is limited by your available balance minus any amounts reserved by existing open orders.maxOrderSize=balance−∑(openOrderSize−filledAmount)\\text{maxOrderSize} = \\text{balance} - \\sum(\\text{openOrderSize} - \\text{filledAmount})maxOrderSize=balance−∑(openOrderSize−filledAmount)

## [​](https://docs.polymarket.com/concepts/order-lifecycle\#next-steps)  Next Steps

[**Resolution** \\
\\
Learn how markets are resolved and winning tokens redeemed.](https://docs.polymarket.com/concepts/resolution)

[**Trading Guide** \\
\\
Start placing orders with our step-by-step guide.](https://docs.polymarket.com/trading/overview)

Was this page helpful?

YesNo

[Positions & Tokens\\
\\
Previous](https://docs.polymarket.com/concepts/positions-tokens) [Resolution\\
\\
Next](https://docs.polymarket.com/concepts/resolution)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.

Suggestions

How do I connect to WebSocket streams?What's required to place my first order?How do I find and fetch market data?

![](https://mintcdn.com/polymarket-292d1b1b/FOMte3ewbG-LVy3k/images/core-concepts/order-lifecycle.png?w=840&fit=max&auto=format&n=FOMte3ewbG-LVy3k&q=85&s=2e31c345d92dcce72a824361c1522ab5)

![](https://mintcdn.com/polymarket-292d1b1b/FOMte3ewbG-LVy3k/images/dark/core-concepts/order-lifecycle.png?w=840&fit=max&auto=format&n=FOMte3ewbG-LVy3k&q=85&s=9e81f0b099ce605683d7c0fcca2d2006)