---
url: "https://docs.polymarket.com/trading/orders/cancel"
title: "Cancel Order - Polymarket Documentation"
---

[Skip to main content](https://docs.polymarket.com/trading/orders/cancel#content-area)

[Polymarket Documentation home page![light logo](https://mintcdn.com/polymarket-292d1b1b/ZibMe6Tli_amZald/logo/light.svg?fit=max&auto=format&n=ZibMe6Tli_amZald&q=85&s=9f9bd559f02181495794661ef6426c0f)![dark logo](https://mintcdn.com/polymarket-292d1b1b/ZibMe6Tli_amZald/logo/dark.svg?fit=max&auto=format&n=ZibMe6Tli_amZald&q=85&s=13abc6754579a3475368ea99d0f5a241)](https://docs.polymarket.com/)

![US](https://d3gk2c5xim1je2.cloudfront.net/flags/US.svg)

English

Search...

Ctrl KAsk AI

Search...

Navigation

Orders

Cancel Order

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

  - [Overview](https://docs.polymarket.com/trading/orders/overview)
  - [Create Order](https://docs.polymarket.com/trading/orders/create)
  - [Cancel Order](https://docs.polymarket.com/trading/orders/cancel)
  - [Order Attribution](https://docs.polymarket.com/trading/orders/attribution)
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

- [Cancel a Single Order](https://docs.polymarket.com/trading/orders/cancel#cancel-a-single-order)
- [Cancel Multiple Orders](https://docs.polymarket.com/trading/orders/cancel#cancel-multiple-orders)
- [Cancel All Orders](https://docs.polymarket.com/trading/orders/cancel#cancel-all-orders)
- [Cancel by Market](https://docs.polymarket.com/trading/orders/cancel#cancel-by-market)
- [Onchain Cancellation](https://docs.polymarket.com/trading/orders/cancel#onchain-cancellation)
- [Querying Orders](https://docs.polymarket.com/trading/orders/cancel#querying-orders)
- [Get a Single Order](https://docs.polymarket.com/trading/orders/cancel#get-a-single-order)
- [Get Open Orders](https://docs.polymarket.com/trading/orders/cancel#get-open-orders)
- [OpenOrder Object](https://docs.polymarket.com/trading/orders/cancel#openorder-object)
- [Trade History](https://docs.polymarket.com/trading/orders/cancel#trade-history)
- [Trade Object](https://docs.polymarket.com/trading/orders/cancel#trade-object)
- [Order Scoring](https://docs.polymarket.com/trading/orders/cancel#order-scoring)
- [Next Steps](https://docs.polymarket.com/trading/orders/cancel#next-steps)

All cancel endpoints require [L2 authentication](https://docs.polymarket.com/trading/overview#authentication). The response always includes `canceled` (list of cancelled order IDs) and `not_canceled` (map of order IDs to failure reasons).

* * *

## [​](https://docs.polymarket.com/trading/orders/cancel\#cancel-a-single-order)  Cancel a Single Order

TypeScript

Python

Rust

REST

Copy

Ask AI

```
const resp = await client.cancelOrder("0xb816482a...");
console.log(resp);
// { canceled: ["0xb816482a..."], not_canceled: {} }
```

* * *

## [​](https://docs.polymarket.com/trading/orders/cancel\#cancel-multiple-orders)  Cancel Multiple Orders

TypeScript

Python

Rust

REST

Copy

Ask AI

```
const resp = await client.cancelOrders(["0xb816482a...", "0xc927593b..."]);
```

* * *

## [​](https://docs.polymarket.com/trading/orders/cancel\#cancel-all-orders)  Cancel All Orders

Cancel every open order across all markets:

TypeScript

Python

Rust

REST

Copy

Ask AI

```
const resp = await client.cancelAll();
```

* * *

## [​](https://docs.polymarket.com/trading/orders/cancel\#cancel-by-market)  Cancel by Market

Cancel all orders for a specific market, optionally filtered to a single token. Both `market` and `asset_id` are optional — omit both to cancel all orders.

TypeScript

Python

Rust

REST

Copy

Ask AI

```
const resp = await client.cancelMarketOrders({
  market: "0xbd31dc8a...", // optional: condition ID
  asset_id: "52114319501245...", // optional: specific token
});
```

* * *

## [​](https://docs.polymarket.com/trading/orders/cancel\#onchain-cancellation)  Onchain Cancellation

If the API is unavailable, you can cancel orders directly on the [Exchange contract](https://github.com/Polymarket/ctf-exchange/tree/main/src) by calling `cancelOrder(Order order)` onchain. Pass the full order struct that was signed when placing the order.Use the `CTFExchange` or `NegRiskCTFExchange` contract depending on the market type. See [Contract Addresses](https://docs.polymarket.com/resources/contract-addresses) for addresses.This is a fallback mechanism — API cancellation is instant while onchain cancellation requires a transaction.

* * *

## [​](https://docs.polymarket.com/trading/orders/cancel\#querying-orders)  Querying Orders

### [​](https://docs.polymarket.com/trading/orders/cancel\#get-a-single-order)  Get a Single Order

TypeScript

Python

Rust

Copy

Ask AI

```
const order = await client.getOrder("0xb816482a...");
console.log(order.status, order.size_matched);
```

### [​](https://docs.polymarket.com/trading/orders/cancel\#get-open-orders)  Get Open Orders

Retrieve all open orders, optionally filtered by market or token:

TypeScript

Python

Rust

Copy

Ask AI

```
// All open orders
const orders = await client.getOpenOrders();

// Filtered by market
const marketOrders = await client.getOpenOrders({
  market: "0xbd31dc8a...",
});

// Filtered by token
const tokenOrders = await client.getOpenOrders({
  asset_id: "52114319501245...",
});
```

### [​](https://docs.polymarket.com/trading/orders/cancel\#openorder-object)  OpenOrder Object

| Field | Type | Description |
| --- | --- | --- |
| `id` | string | Order ID |
| `status` | string | Current order status |
| `market` | string | Condition ID |
| `asset_id` | string | Token ID |
| `side` | string | `BUY` or `SELL` |
| `original_size` | string | Size at placement |
| `size_matched` | string | Amount filled |
| `price` | string | Limit price |
| `outcome` | string | Human-readable outcome (e.g., “Yes”, “No”) |
| `order_type` | string | Order type (GTC, GTD, FOK, FAK) |
| `maker_address` | string | Funder address |
| `owner` | string | API key of the order owner |
| `associate_trades` | string\[\] | Trade IDs this order has been included in |
| `expiration` | string | Unix expiration timestamp (`0` if none) |
| `created_at` | string | Unix creation timestamp |

* * *

## [​](https://docs.polymarket.com/trading/orders/cancel\#trade-history)  Trade History

When an order is matched, it creates a trade. Trades progress through these statuses:

| Status | Terminal | Description |
| --- | --- | --- |
| `MATCHED` | No | Matched and sent for onchain submission |
| `MINED` | No | Mined on the chain, no finality yet |
| `CONFIRMED` | Yes | Achieved finality — trade successful |
| `RETRYING` | No | Transaction failed — being retried |
| `FAILED` | Yes | Failed permanently |

TypeScript

Python

Rust

Copy

Ask AI

```
// All trades
const trades = await client.getTrades();

// Filtered by market
const marketTrades = await client.getTrades({
  market: "0xbd31dc8a...",
});
```

Additional filter parameters: `id`, `maker_address`, `asset_id`, `before`, `after`.The Rust SDK uses cursor-based pagination via the `next_cursor` parameter:

TypeScript

Python

Rust

Copy

Ask AI

```
const page = await client.getTradesPaginated({ market: "0xbd31dc8a..." });
console.log(page.trades, page.count); // trades array + total count
```

### [​](https://docs.polymarket.com/trading/orders/cancel\#trade-object)  Trade Object

| Field | Type | Description |
| --- | --- | --- |
| `id` | string | Trade ID |
| `taker_order_id` | string | Taker order hash |
| `market` | string | Condition ID |
| `asset_id` | string | Token ID |
| `side` | string | `BUY` or `SELL` |
| `size` | string | Trade size |
| `price` | string | Execution price |
| `fee_rate_bps` | string | Fee rate in basis points |
| `status` | string | Trade status (see table above) |
| `match_time` | string | Unix timestamp when matched |
| `last_update` | string | Unix timestamp of last status change |
| `outcome` | string | Human-readable outcome (e.g., “Yes”) |
| `maker_address` | string | Maker’s funder address |
| `owner` | string | API key of the trade owner |
| `transaction_hash` | string | Onchain transaction hash |
| `bucket_index` | number | Index for trade reconciliation |
| `trader_side` | string | `TAKER` or `MAKER` |
| `maker_orders` | MakerOrder\[\] | Maker orders that filled this trade |

A single trade can be split across multiple onchain transactions due to gas
limits. Use `bucket_index` and `match_time` to reconcile related transactions
back to a single logical trade.

* * *

## [​](https://docs.polymarket.com/trading/orders/cancel\#order-scoring)  Order Scoring

Check if your resting orders are eligible for [maker rebates](https://docs.polymarket.com/market-makers/maker-rebates) scoring:

TypeScript

Python

Rust

Copy

Ask AI

```
// Single order
const scoring = await client.isOrderScoring({ orderId: "0x..." });

// Multiple orders
const batch = await client.areOrdersScoring({
  orderIds: ["0x...", "0x..."],
});
```

* * *

## [​](https://docs.polymarket.com/trading/orders/cancel\#next-steps)  Next Steps

[**Order Attribution** \\
\\
Attribute orders to your builder account for volume credit](https://docs.polymarket.com/trading/orders/attribution)

[**Fees** \\
\\
Understand fee structures and maker rebates](https://docs.polymarket.com/trading/fees)

Was this page helpful?

YesNo

[Create Order\\
\\
Previous](https://docs.polymarket.com/trading/orders/create) [Order Attribution\\
\\
Next](https://docs.polymarket.com/trading/orders/attribution)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.

Suggestions

How do I connect to WebSocket streams?What's required to place my first order?How do I find and fetch market data?