---
url: "https://docs.polymarket.com/market-data/websocket/user-channel"
title: "User Channel - Polymarket Documentation"
---

[Skip to main content](https://docs.polymarket.com/market-data/websocket/user-channel#content-area)

[Polymarket Documentation home page![light logo](https://mintcdn.com/polymarket-292d1b1b/ZibMe6Tli_amZald/logo/light.svg?fit=max&auto=format&n=ZibMe6Tli_amZald&q=85&s=9f9bd559f02181495794661ef6426c0f)![dark logo](https://mintcdn.com/polymarket-292d1b1b/ZibMe6Tli_amZald/logo/dark.svg?fit=max&auto=format&n=ZibMe6Tli_amZald&q=85&s=13abc6754579a3475368ea99d0f5a241)](https://docs.polymarket.com/)

![US](https://d3gk2c5xim1je2.cloudfront.net/flags/US.svg)

English

Search...

Ctrl KAsk AI

Search...

Navigation

WebSocket

User Channel

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

  - [Overview](https://docs.polymarket.com/market-data/websocket/overview)
  - [Market Channel](https://docs.polymarket.com/market-data/websocket/market-channel)
  - [User Channel](https://docs.polymarket.com/market-data/websocket/user-channel)
  - [Sports WebSocket](https://docs.polymarket.com/market-data/websocket/sports)
  - [Real-Time Data Socket](https://docs.polymarket.com/market-data/websocket/rtds)
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

- [Endpoint](https://docs.polymarket.com/market-data/websocket/user-channel#endpoint)
- [Authentication](https://docs.polymarket.com/market-data/websocket/user-channel#authentication)
- [Message Types](https://docs.polymarket.com/market-data/websocket/user-channel#message-types)
- [trade](https://docs.polymarket.com/market-data/websocket/user-channel#trade)
- [Trade Statuses](https://docs.polymarket.com/market-data/websocket/user-channel#trade-statuses)
- [order](https://docs.polymarket.com/market-data/websocket/user-channel#order)

Authenticated channel for updates related to your orders and trades, filtered by API key.

## [​](https://docs.polymarket.com/market-data/websocket/user-channel\#endpoint)  Endpoint

Copy

Ask AI

```
wss://ws-subscriptions-clob.polymarket.com/ws/user
```

## [​](https://docs.polymarket.com/market-data/websocket/user-channel\#authentication)  Authentication

Include API credentials in your subscription message:

Copy

Ask AI

```
{
  "auth": {
    "apiKey": "your-api-key",
    "secret": "your-api-secret",
    "passphrase": "your-passphrase"
  },
  "markets": ["0x1234...condition_id"],
  "type": "user"
}
```

Never expose your API credentials in client-side code. Use the user channel
only from server environments.

## [​](https://docs.polymarket.com/market-data/websocket/user-channel\#message-types)  Message Types

Each message includes a `type` field identifying the event.

### [​](https://docs.polymarket.com/market-data/websocket/user-channel\#trade)  trade

Emitted when:

- A market order is matched (`MATCHED`)
- A limit order for the user is included in a trade (`MATCHED`)
- Subsequent status changes for the trade (`MINED`, `CONFIRMED`, `RETRYING`, `FAILED`)

Copy

Ask AI

```
{
  "asset_id": "52114319501245915516055106046884209969926127482827954674443846427813813222426",
  "event_type": "trade",
  "id": "28c4d2eb-bbea-40e7-a9f0-b2fdb56b2c2e",
  "last_update": "1672290701",
  "maker_orders": [\
    {\
      "asset_id": "52114319501245915516055106046884209969926127482827954674443846427813813222426",\
      "matched_amount": "10",\
      "order_id": "0xff354cd7ca7539dfa9c28d90943ab5779a4eac34b9b37a757d7b32bdfb11790b",\
      "outcome": "YES",\
      "owner": "9180014b-33c8-9240-a14b-bdca11c0a465",\
      "price": "0.57"\
    }\
  ],
  "market": "0xbd31dc8a20211944f6b70f31557f1001557b59905b7738480ca09bd4532f84af",
  "matchtime": "1672290701",
  "outcome": "YES",
  "owner": "9180014b-33c8-9240-a14b-bdca11c0a465",
  "price": "0.57",
  "side": "BUY",
  "size": "10",
  "status": "MATCHED",
  "taker_order_id": "0x06bc63e346ed4ceddce9efd6b3af37c8f8f440c92fe7da6b2d0f9e4ccbc50c42",
  "timestamp": "1672290701",
  "trade_owner": "9180014b-33c8-9240-a14b-bdca11c0a465",
  "type": "TRADE"
}
```

#### [​](https://docs.polymarket.com/market-data/websocket/user-channel\#trade-statuses)  Trade Statuses

Copy

Ask AI

```
MATCHED → MINED → CONFIRMED
    ↓        ↑
RETRYING ───┘
    ↓
  FAILED
```

| Status | Terminal | Description |
| --- | --- | --- |
| `MATCHED` | No | Trade has been matched and sent to the executor service by the operator |
| `MINED` | No | Trade observed to be mined into the chain, no finality threshold established |
| `CONFIRMED` | Yes | Trade has achieved strong probabilistic finality and was successful |
| `RETRYING` | No | Trade transaction has failed (revert or reorg) and is being retried/resubmitted by the operator |
| `FAILED` | Yes | Trade has failed and is not being retried |

### [​](https://docs.polymarket.com/market-data/websocket/user-channel\#order)  order

Emitted when:

- An order is placed (`PLACEMENT`)
- An order is updated — some of it is matched (`UPDATE`)
- An order is cancelled (`CANCELLATION`)

Copy

Ask AI

```
{
  "asset_id": "52114319501245915516055106046884209969926127482827954674443846427813813222426",
  "associate_trades": null,
  "event_type": "order",
  "id": "0xff354cd7ca7539dfa9c28d90943ab5779a4eac34b9b37a757d7b32bdfb11790b",
  "market": "0xbd31dc8a20211944f6b70f31557f1001557b59905b7738480ca09bd4532f84af",
  "order_owner": "9180014b-33c8-9240-a14b-bdca11c0a465",
  "original_size": "10",
  "outcome": "YES",
  "owner": "9180014b-33c8-9240-a14b-bdca11c0a465",
  "price": "0.57",
  "side": "SELL",
  "size_matched": "0",
  "timestamp": "1672290687",
  "type": "PLACEMENT"
}
```

Was this page helpful?

YesNo

[Market Channel\\
\\
Previous](https://docs.polymarket.com/market-data/websocket/market-channel) [Sports WebSocket\\
\\
Next](https://docs.polymarket.com/market-data/websocket/sports)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.

Suggestions

How do I connect to WebSocket streams?What's required to place my first order?How do I find and fetch market data?