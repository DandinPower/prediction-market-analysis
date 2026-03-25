---
url: "https://docs.polymarket.com/market-makers/trading"
title: "Trading - Polymarket Documentation"
---

[Skip to main content](https://docs.polymarket.com/market-makers/trading#content-area)

[Polymarket Documentation home page![light logo](https://mintcdn.com/polymarket-292d1b1b/ZibMe6Tli_amZald/logo/light.svg?fit=max&auto=format&n=ZibMe6Tli_amZald&q=85&s=9f9bd559f02181495794661ef6426c0f)![dark logo](https://mintcdn.com/polymarket-292d1b1b/ZibMe6Tli_amZald/logo/dark.svg?fit=max&auto=format&n=ZibMe6Tli_amZald&q=85&s=13abc6754579a3475368ea99d0f5a241)](https://docs.polymarket.com/)

![US](https://d3gk2c5xim1je2.cloudfront.net/flags/US.svg)

English

Search...

Ctrl KAsk AI

Search...

Navigation

Operations

Trading

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

  - [Trading](https://docs.polymarket.com/market-makers/trading)
  - [Inventory Management](https://docs.polymarket.com/market-makers/inventory)

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

- [Two-Sided Quoting](https://docs.polymarket.com/market-makers/trading#two-sided-quoting)
- [Batch Orders](https://docs.polymarket.com/market-makers/trading#batch-orders)
- [Choosing Order Types](https://docs.polymarket.com/market-makers/trading#choosing-order-types)
- [Time-Limited Quotes with GTD](https://docs.polymarket.com/market-makers/trading#time-limited-quotes-with-gtd)
- [Managing Orders](https://docs.polymarket.com/market-makers/trading#managing-orders)
- [Cancelling](https://docs.polymarket.com/market-makers/trading#cancelling)
- [Monitoring Open Orders](https://docs.polymarket.com/market-makers/trading#monitoring-open-orders)
- [Tick Sizes](https://docs.polymarket.com/market-makers/trading#tick-sizes)
- [Fees](https://docs.polymarket.com/market-makers/trading#fees)
- [Best Practices](https://docs.polymarket.com/market-makers/trading#best-practices)
- [Quote Management](https://docs.polymarket.com/market-makers/trading#quote-management)
- [Latency](https://docs.polymarket.com/market-makers/trading#latency)
- [Risk Controls](https://docs.polymarket.com/market-makers/trading#risk-controls)
- [Next Steps](https://docs.polymarket.com/market-makers/trading#next-steps)

Market makers interact with Polymarket through the CLOB API — posting two-sided quotes, managing inventory across markets, and rebalancing positions. The SDK clients handle order signing and submission, so you can focus on strategy.

This page covers MM-specific workflows and best practices. For full order
mechanics, see [Create Orders](https://docs.polymarket.com/trading/orders/create) and [Cancel\\
Orders](https://docs.polymarket.com/trading/orders/cancel).

* * *

## [​](https://docs.polymarket.com/market-makers/trading\#two-sided-quoting)  Two-Sided Quoting

The core market making workflow is posting a bid and ask around your fair value. Use `createAndPostOrder` to place each side:

TypeScript

Python

Rust

Copy

Ask AI

```
import { ClobClient, Side, OrderType } from "@polymarket/clob-client";

const client = new ClobClient(
  "https://clob.polymarket.com",
  137,
  wallet,
  credentials,
  signatureType,
  funder,
);

// Bid at 0.48
const bid = await client.createAndPostOrder({
  tokenID: "3409705850427531082723332342151729...",
  side: Side.BUY,
  price: 0.48,
  size: 1000,
  orderType: OrderType.GTC,
});

// Ask at 0.52
const ask = await client.createAndPostOrder({
  tokenID: "3409705850427531082723332342151729...",
  side: Side.SELL,
  price: 0.52,
  size: 1000,
  orderType: OrderType.GTC,
});
```

### [​](https://docs.polymarket.com/market-makers/trading\#batch-orders)  Batch Orders

For tighter spreads across multiple levels, use `postOrders` to submit up to 15 orders in a single request:

TypeScript

Python

Rust

Copy

Ask AI

```
const orders = await Promise.all([\
  client.createOrder({ tokenID, side: Side.BUY, price: 0.48, size: 500 }),\
  client.createOrder({ tokenID, side: Side.BUY, price: 0.47, size: 500 }),\
  client.createOrder({ tokenID, side: Side.SELL, price: 0.52, size: 500 }),\
  client.createOrder({ tokenID, side: Side.SELL, price: 0.53, size: 500 }),\
]);

const response = await client.postOrders(
  orders.map((order) => ({ order, orderType: OrderType.GTC })),
);
```

Batching reduces latency by submitting multiple quotes in a single request.
Always prefer `postOrders()` over multiple individual `createAndPostOrder()`
calls.

* * *

## [​](https://docs.polymarket.com/market-makers/trading\#choosing-order-types)  Choosing Order Types

| Type | Behavior | When to Use |
| --- | --- | --- |
| **GTC** | Rests on the book until filled or cancelled | Default for passive quoting |
| **GTD** | Auto-expires at a specified time | Expire quotes before known events |
| **FOK** | Must fill entirely and immediately, or cancel | Aggressive rebalancing — all or nothing |
| **FAK** | Fills what’s available immediately, cancels rest | Rebalancing where partial fills are OK |

**GTC** and **GTD** are your primary tools for passive market making — they rest on the book at your specified price. **FOK** and **FAK** are for rebalancing inventory against resting liquidity.

### [​](https://docs.polymarket.com/market-makers/trading\#time-limited-quotes-with-gtd)  Time-Limited Quotes with GTD

Auto-expire quotes before known events like market close or resolution:

TypeScript

Python

Rust

Copy

Ask AI

```
// Expire in 1 hour
const expiringOrder = await client.createOrder({
  tokenID,
  side: Side.BUY,
  price: 0.5,
  size: 1000,
  orderType: OrderType.GTD,
  expiration: Math.floor(Date.now() / 1000) + 3600,
});
```

* * *

## [​](https://docs.polymarket.com/market-makers/trading\#managing-orders)  Managing Orders

### [​](https://docs.polymarket.com/market-makers/trading\#cancelling)  Cancelling

Cancel individual orders, by market, or everything at once:

TypeScript

Python

Rust

Copy

Ask AI

```
await client.cancelOrder(orderId); // Single order
await client.cancelOrders(orderIds); // Multiple orders
await client.cancelMarketOrders(conditionId); // All orders in a market
await client.cancelAll(); // Everything
```

See [Cancel Orders](https://docs.polymarket.com/trading/orders/cancel) for full details including onchain cancellation.

### [​](https://docs.polymarket.com/market-makers/trading\#monitoring-open-orders)  Monitoring Open Orders

TypeScript

Python

Rust

Copy

Ask AI

```
const order = await client.getOrder(orderId);

const orders = await client.getOpenOrders({
  market: "0xbd31dc8a...",
  asset_id: "52114319501245...",
});
```

* * *

## [​](https://docs.polymarket.com/market-makers/trading\#tick-sizes)  Tick Sizes

Your order price must conform to the market’s tick size, or it will be rejected. Look it up with the SDK before quoting:

TypeScript

Python

Rust

Copy

Ask AI

```
const tickSize = await client.getTickSize(tokenID);
// Returns: "0.1" | "0.01" | "0.001" | "0.0001"
```

* * *

## [​](https://docs.polymarket.com/market-makers/trading\#fees)  Fees

Most markets have **zero fees** for both makers and takers. However, the following market types have taker fees:

- **All crypto markets**
- **Select sports markets** (e.g., NCAAB, Serie A)

Fees apply only to markets deployed on or after the activation date. Pre-existing markets are unaffected. Markets with fees enabled have `feesEnabled` set to `true` on the market object.

See [Fees](https://docs.polymarket.com/trading/fees) for the full fee schedule and calculation details.

* * *

## [​](https://docs.polymarket.com/market-makers/trading\#best-practices)  Best Practices

### [​](https://docs.polymarket.com/market-makers/trading\#quote-management)  Quote Management

- **Quote both sides** — Post bids and asks to earn maximum [liquidity rewards](https://docs.polymarket.com/market-makers/liquidity-rewards)
- **Skew on inventory** — Adjust quote prices based on your current position to manage exposure
- **Cancel stale quotes** — Pull orders immediately when market conditions change
- **Use GTD for events** — Auto-expire quotes before known catalysts to avoid stale exposure

### [​](https://docs.polymarket.com/market-makers/trading\#latency)  Latency

- **Batch orders** — Use `postOrders()` to submit multiple quotes in a single request
- **WebSocket for data** — Subscribe to real-time feeds instead of polling REST endpoints

### [​](https://docs.polymarket.com/market-makers/trading\#risk-controls)  Risk Controls

- **Size limits** — Check token balances before quoting and don’t exceed your available inventory
- **Price guards** — Validate prices against the book midpoint and reject outliers
- **Kill switch** — Call `cancelAll()` immediately on errors or position breaches
- **Monitor fills** — Subscribe to the WebSocket user channel for real-time fill notifications

* * *

## [​](https://docs.polymarket.com/market-makers/trading\#next-steps)  Next Steps

[**Inventory** \\
\\
Split, merge, and redeem outcome tokens](https://docs.polymarket.com/market-makers/inventory)

[**Liquidity Rewards** \\
\\
Earn rewards for providing two-sided liquidity](https://docs.polymarket.com/market-makers/liquidity-rewards)

[**Create Orders** \\
\\
Full order creation reference with all options](https://docs.polymarket.com/trading/orders/create)

Was this page helpful?

YesNo

[Liquidity Rewards\\
\\
Previous](https://docs.polymarket.com/market-makers/liquidity-rewards) [Inventory Management\\
\\
Next](https://docs.polymarket.com/market-makers/inventory)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.

Suggestions

How do I connect to WebSocket streams?What's required to place my first order?How do I find and fetch market data?