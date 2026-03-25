---
url: "https://docs.polymarket.com/trading/orders/create"
title: "Create Order - Polymarket Documentation"
---

[Skip to main content](https://docs.polymarket.com/trading/orders/create#content-area)

[Polymarket Documentation home page![light logo](https://mintcdn.com/polymarket-292d1b1b/ZibMe6Tli_amZald/logo/light.svg?fit=max&auto=format&n=ZibMe6Tli_amZald&q=85&s=9f9bd559f02181495794661ef6426c0f)![dark logo](https://mintcdn.com/polymarket-292d1b1b/ZibMe6Tli_amZald/logo/dark.svg?fit=max&auto=format&n=ZibMe6Tli_amZald&q=85&s=13abc6754579a3475368ea99d0f5a241)](https://docs.polymarket.com/)

![US](https://d3gk2c5xim1je2.cloudfront.net/flags/US.svg)

English

Search...

Ctrl KAsk AI

Search...

Navigation

Orders

Create Order

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

- [Order Types](https://docs.polymarket.com/trading/orders/create#order-types)
- [Limit Orders](https://docs.polymarket.com/trading/orders/create#limit-orders)
- [Two-Step Sign Then Submit](https://docs.polymarket.com/trading/orders/create#two-step-sign-then-submit)
- [GTD Orders](https://docs.polymarket.com/trading/orders/create#gtd-orders)
- [Market Orders](https://docs.polymarket.com/trading/orders/create#market-orders)
- [One-Step Market Order](https://docs.polymarket.com/trading/orders/create#one-step-market-order)
- [Post-Only Orders](https://docs.polymarket.com/trading/orders/create#post-only-orders)
- [Batch Orders](https://docs.polymarket.com/trading/orders/create#batch-orders)
- [Order Options](https://docs.polymarket.com/trading/orders/create#order-options)
- [Tick Sizes](https://docs.polymarket.com/trading/orders/create#tick-sizes)
- [Negative Risk](https://docs.polymarket.com/trading/orders/create#negative-risk)
- [Prerequisites](https://docs.polymarket.com/trading/orders/create#prerequisites)
- [Advanced Parameters](https://docs.polymarket.com/trading/orders/create#advanced-parameters)
- [Sports Markets](https://docs.polymarket.com/trading/orders/create#sports-markets)
- [Response](https://docs.polymarket.com/trading/orders/create#response)
- [Statuses](https://docs.polymarket.com/trading/orders/create#statuses)
- [Error Messages](https://docs.polymarket.com/trading/orders/create#error-messages)
- [Heartbeat](https://docs.polymarket.com/trading/orders/create#heartbeat)
- [Next Steps](https://docs.polymarket.com/trading/orders/create#next-steps)

All orders on Polymarket are expressed as **limit orders**. Market orders are supported by submitting a limit order with a marketable price — your order executes immediately at the best available price on the book.

The SDK handles EIP-712 signing and submission for you. If you prefer the REST
API directly, see [Authentication](https://docs.polymarket.com/api-reference/authentication) for constructing the
required headers and the [API Reference](https://docs.polymarket.com/api-reference/introduction) for full endpoint
documentation including the raw order object fields and request/response schemas.

* * *

## [​](https://docs.polymarket.com/trading/orders/create\#order-types)  Order Types

| Type | Behavior | Use Case |
| --- | --- | --- |
| **GTC** | Good-Til-Cancelled — rests on the book until filled or cancelled | Default for limit orders |
| **GTD** | Good-Til-Date — active until a specified expiration time | Auto-expire before known events |
| **FOK** | Fill-Or-Kill — must fill immediately and entirely, or cancel | All-or-nothing market orders |
| **FAK** | Fill-And-Kill — fills what’s available immediately, cancels the rest | Partial-fill market orders |

- **GTC** and **GTD** are limit order types — they rest on the book at your specified price.
- **FOK** and **FAK** are market order types — they execute against resting liquidity immediately.

  - **BUY**: specify the dollar amount you want to spend
  - **SELL**: specify the number of shares you want to sell

* * *

## [​](https://docs.polymarket.com/trading/orders/create\#limit-orders)  Limit Orders

The simplest way to place a limit order — create, sign, and submit in one call:

TypeScript

Python

Rust

Copy

Ask AI

```
import { ClobClient, Side, OrderType } from "@polymarket/clob-client";

const response = await client.createAndPostOrder(
  {
    tokenID: "TOKEN_ID",
    price: 0.5,
    size: 10,
    side: Side.BUY,
  },
  {
    tickSize: "0.01",
    negRisk: false,
  },
  OrderType.GTC,
);

console.log("Order ID:", response.orderID);
console.log("Status:", response.status);
```

### [​](https://docs.polymarket.com/trading/orders/create\#two-step-sign-then-submit)  Two-Step Sign Then Submit

For more control, you can separate signing from submission. This is useful for batch orders or custom submission logic:

TypeScript

Python

Rust

Copy

Ask AI

```
// Step 1: Create and sign locally
const signedOrder = await client.createOrder(
  {
    tokenID: "TOKEN_ID",
    price: 0.5,
    size: 10,
    side: Side.BUY,
  },
  { tickSize: "0.01", negRisk: false },
);

// Step 2: Submit to the CLOB
const response = await client.postOrder(signedOrder, OrderType.GTC);
```

* * *

## [​](https://docs.polymarket.com/trading/orders/create\#gtd-orders)  GTD Orders

GTD orders auto-expire at a specified time. Useful for quoting around known events.

TypeScript

Python

Rust

Copy

Ask AI

```
// Expire in 1 hour (+ 60s security threshold buffer)
const expiration = Math.floor(Date.now() / 1000) + 60 + 3600;

const response = await client.createAndPostOrder(
  {
    tokenID: "TOKEN_ID",
    price: 0.5,
    size: 10,
    side: Side.BUY,
    expiration,
  },
  { tickSize: "0.01", negRisk: false },
  OrderType.GTD,
);
```

There is a security threshold of one minute on GTD expiration. To set an
effective lifetime of N seconds, use `now + 60 + N`. For example, for a
30-second effective lifetime, set the expiration to `now + 60 + 30`.

* * *

## [​](https://docs.polymarket.com/trading/orders/create\#market-orders)  Market Orders

Market orders execute immediately against resting liquidity using FOK or FAK types:

TypeScript

Python

Rust

Copy

Ask AI

```
import { Side, OrderType } from "@polymarket/clob-client";

// FOK BUY: spend exactly $100 or cancel entirely
const buyOrder = await client.createMarketOrder(
  {
    tokenID: "TOKEN_ID",
    side: Side.BUY,
    amount: 100, // dollar amount
    price: 0.5, // worst-price limit (slippage protection)
  },
  { tickSize: "0.01", negRisk: false },
);
await client.postOrder(buyOrder, OrderType.FOK);

// FOK SELL: sell exactly 200 shares or cancel entirely
const sellOrder = await client.createMarketOrder(
  {
    tokenID: "TOKEN_ID",
    side: Side.SELL,
    amount: 200, // number of shares
    price: 0.45, // worst-price limit (slippage protection)
  },
  { tickSize: "0.01", negRisk: false },
);
await client.postOrder(sellOrder, OrderType.FOK);
```

- **FOK** — fill entirely or cancel the whole order
- **FAK** — fill what’s available, cancel the rest

The `price` field on market orders acts as a **worst-price limit** (slippage protection), not a target execution price.

### [​](https://docs.polymarket.com/trading/orders/create\#one-step-market-order)  One-Step Market Order

For convenience, `createAndPostMarketOrder` handles creation, signing, and submission in one call:

TypeScript

Python

Rust

Copy

Ask AI

```
const response = await client.createAndPostMarketOrder(
  {
    tokenID: "TOKEN_ID",
    side: Side.BUY,
    amount: 100,
    price: 0.5,
  },
  { tickSize: "0.01", negRisk: false },
  OrderType.FOK,
);
```

* * *

## [​](https://docs.polymarket.com/trading/orders/create\#post-only-orders)  Post-Only Orders

Post-only orders guarantee you’re always the maker. If the order would match immediately (cross the spread), it’s rejected instead of executed.

TypeScript

Python

Rust

Copy

Ask AI

```
const response = await client.postOrder(signedOrder, OrderType.GTC, true);
```

- Only works with **GTC** and **GTD** order types
- Rejected if combined with FOK or FAK

* * *

## [​](https://docs.polymarket.com/trading/orders/create\#batch-orders)  Batch Orders

Place up to **15 orders** in a single request:

TypeScript

Python

Rust

Copy

Ask AI

```
import { OrderType, Side, PostOrdersArgs } from "@polymarket/clob-client";

const orders: PostOrdersArgs[] = [\
  {\
    order: await client.createOrder(\
      {\
        tokenID: "TOKEN_ID",\
        price: 0.48,\
        side: Side.BUY,\
        size: 500,\
      },\
      { tickSize: "0.01", negRisk: false },\
    ),\
    orderType: OrderType.GTC,\
  },\
  {\
    order: await client.createOrder(\
      {\
        tokenID: "TOKEN_ID",\
        price: 0.52,\
        side: Side.SELL,\
        size: 500,\
      },\
      { tickSize: "0.01", negRisk: false },\
    ),\
    orderType: OrderType.GTC,\
  },\
];

const response = await client.postOrders(orders);
```

* * *

## [​](https://docs.polymarket.com/trading/orders/create\#order-options)  Order Options

Every order requires two market-specific options: `tickSize` and `negRisk`. For details on signature types (`0` = EOA, `1` = POLY\_PROXY, `2` = GNOSIS\_SAFE), see [Authentication](https://docs.polymarket.com/api-reference/authentication#signature-types-and-funder).

### [​](https://docs.polymarket.com/trading/orders/create\#tick-sizes)  Tick Sizes

Your order price must conform to the market’s tick size, or the order is rejected.

| Tick Size | Precision | Example Prices |
| --- | --- | --- |
| `0.1` | 1 decimal | 0.1, 0.2, 0.5 |
| `0.01` | 2 decimals | 0.01, 0.50, 0.99 |
| `0.001` | 3 decimals | 0.001, 0.500, 0.999 |
| `0.0001` | 4 decimals | 0.0001, 0.5000, 0.9999 |

TypeScript

Python

Rust

Copy

Ask AI

```
const tickSize = await client.getTickSize("TOKEN_ID");
```

### [​](https://docs.polymarket.com/trading/orders/create\#negative-risk)  Negative Risk

Multi-outcome events (3+ outcomes) use the Neg Risk CTF Exchange. Pass `negRisk: true` for these markets.

TypeScript

Python

Rust

Copy

Ask AI

```
const isNegRisk = await client.getNegRisk("TOKEN_ID");
```

Both values are also available on the market object: `minimum_tick_size` and
`neg_risk`. In Rust, the order builder auto-fetches both — you don’t need to look them up manually.

* * *

## [​](https://docs.polymarket.com/trading/orders/create\#prerequisites)  Prerequisites

Before placing an order, your funder address must have approved the Exchange contract to spend the relevant tokens:

- **BUY orders**: USDC.e allowance >= spending amount
- **SELL orders**: conditional token allowance >= selling amount

Order size is limited by your available balance minus amounts reserved by existing open orders:maxOrderSize=balance−∑(openOrderSize−filledAmount)\\text{maxOrderSize} = \\text{balance} - \\sum(\\text{openOrderSize} - \\text{filledAmount})maxOrderSize=balance−∑(openOrderSize−filledAmount)

Orders are continuously monitored for validity — balances, allowances, and
onchain cancellations are tracked in real time. Any maker caught intentionally
abusing these checks will be blacklisted.

### [​](https://docs.polymarket.com/trading/orders/create\#advanced-parameters)  Advanced Parameters

These optional fields can be passed in the `UserOrder` object for fine-grained control:

| Parameter | Type | Description |
| --- | --- | --- |
| `feeRateBps` | number | Fee rate in basis points (default: market rate) |
| `nonce` | number | Custom nonce for order uniqueness |
| `taker` | string | Restrict the order to a specific taker address |

### [​](https://docs.polymarket.com/trading/orders/create\#sports-markets)  Sports Markets

Sports markets have additional behaviors:

- Outstanding limit orders are **automatically cancelled** once the game begins, clearing the entire order book at the official start time
- Marketable orders have a **3-second placement delay** before matching
- Game start times can shift — monitor your orders closely, as they may not be cleared if the start time changes unexpectedly

* * *

## [​](https://docs.polymarket.com/trading/orders/create\#response)  Response

A successful order placement returns:

Copy

Ask AI

```
{
  "success": true,
  "errorMsg": "",
  "orderID": "0xabc123...",
  "takingAmount": "",
  "makingAmount": "",
  "status": "live",
  "transactionsHashes": [],
  "tradeIDs": []
}
```

### [​](https://docs.polymarket.com/trading/orders/create\#statuses)  Statuses

| Status | Description |
| --- | --- |
| `live` | Order resting on the book |
| `matched` | Order matched immediately with a resting order |
| `delayed` | Marketable order subject to a matching delay |
| `unmatched` | Marketable but failed to delay — placement still successful |

### [​](https://docs.polymarket.com/trading/orders/create\#error-messages)  Error Messages

| Error | Description |
| --- | --- |
| `INVALID_ORDER_MIN_TICK_SIZE` | Price doesn’t conform to the market’s tick size |
| `INVALID_ORDER_MIN_SIZE` | Order size below the minimum threshold |
| `INVALID_ORDER_DUPLICATED` | Identical order already placed |
| `INVALID_ORDER_NOT_ENOUGH_BALANCE` | Insufficient balance or allowance |
| `INVALID_ORDER_EXPIRATION` | Expiration timestamp is in the past |
| `INVALID_POST_ONLY_ORDER_TYPE` | Post-only used with FOK/FAK |
| `INVALID_POST_ONLY_ORDER` | Post-only order would cross the book |
| `FOK_ORDER_NOT_FILLED_ERROR` | FOK order couldn’t be fully filled |
| `INVALID_ORDER_ERROR` | System error inserting the order |
| `EXECUTION_ERROR` | System error executing the trade |
| `ORDER_DELAYED` | Order match delayed due to market conditions |
| `DELAYING_ORDER_ERROR` | System error while delaying the order |
| `MARKET_NOT_READY` | Market not yet accepting orders |

* * *

## [​](https://docs.polymarket.com/trading/orders/create\#heartbeat)  Heartbeat

The heartbeat endpoint maintains session liveness. If a valid heartbeat is not received within **10 seconds** (with a 5-second buffer), **all open orders are cancelled**.

TypeScript

Python

Rust

Copy

Ask AI

```
let heartbeatId = "";
setInterval(async () => {
  const resp = await client.postHeartbeat(heartbeatId);
  heartbeatId = resp.heartbeat_id;
}, 5000);
```

- Include the most recent `heartbeat_id` in each request. Use an empty string for the first request.
- If you send an expired ID, the server responds with `400` and the correct ID. Update and retry.

* * *

## [​](https://docs.polymarket.com/trading/orders/create\#next-steps)  Next Steps

[**Cancel Orders** \\
\\
Cancel single, multiple, or all open orders](https://docs.polymarket.com/trading/orders/cancel)

[**Order Attribution** \\
\\
Attribute orders to your builder account for volume credit](https://docs.polymarket.com/trading/orders/attribution)

Was this page helpful?

YesNo

[Overview\\
\\
Previous](https://docs.polymarket.com/trading/orders/overview) [Cancel Order\\
\\
Next](https://docs.polymarket.com/trading/orders/cancel)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.

Suggestions

How do I connect to WebSocket streams?What's required to place my first order?How do I find and fetch market data?