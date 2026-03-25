---
url: "https://docs.polymarket.com/market-data/websocket/market-channel"
title: "Market Channel - Polymarket Documentation"
---

[Skip to main content](https://docs.polymarket.com/market-data/websocket/market-channel#content-area)

[Polymarket Documentation home page![light logo](https://mintcdn.com/polymarket-292d1b1b/ZibMe6Tli_amZald/logo/light.svg?fit=max&auto=format&n=ZibMe6Tli_amZald&q=85&s=9f9bd559f02181495794661ef6426c0f)![dark logo](https://mintcdn.com/polymarket-292d1b1b/ZibMe6Tli_amZald/logo/dark.svg?fit=max&auto=format&n=ZibMe6Tli_amZald&q=85&s=13abc6754579a3475368ea99d0f5a241)](https://docs.polymarket.com/)

![US](https://d3gk2c5xim1je2.cloudfront.net/flags/US.svg)

English

Search...

Ctrl KAsk AI

Search...

Navigation

WebSocket

Market Channel

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

- [Endpoint](https://docs.polymarket.com/market-data/websocket/market-channel#endpoint)
- [Subscription](https://docs.polymarket.com/market-data/websocket/market-channel#subscription)
- [Message Types](https://docs.polymarket.com/market-data/websocket/market-channel#message-types)
- [book](https://docs.polymarket.com/market-data/websocket/market-channel#book)
- [price\_change](https://docs.polymarket.com/market-data/websocket/market-channel#price_change)
- [tick\_size\_change](https://docs.polymarket.com/market-data/websocket/market-channel#tick_size_change)
- [last\_trade\_price](https://docs.polymarket.com/market-data/websocket/market-channel#last_trade_price)
- [best\_bid\_ask](https://docs.polymarket.com/market-data/websocket/market-channel#best_bid_ask)
- [new\_market](https://docs.polymarket.com/market-data/websocket/market-channel#new_market)
- [market\_resolved](https://docs.polymarket.com/market-data/websocket/market-channel#market_resolved)

Public channel for market data updates (level 2 price data). Subscribe with asset IDs to receive orderbook snapshots, price changes, trade executions, and market events.

## [​](https://docs.polymarket.com/market-data/websocket/market-channel\#endpoint)  Endpoint

Copy

Ask AI

```
wss://ws-subscriptions-clob.polymarket.com/ws/market
```

## [​](https://docs.polymarket.com/market-data/websocket/market-channel\#subscription)  Subscription

Copy

Ask AI

```
{
  "assets_ids": ["<token_id_1>", "<token_id_2>"],
  "type": "market",
  "custom_feature_enabled": true
}
```

Set `custom_feature_enabled: true` to receive `best_bid_ask`, `new_market`, and `market_resolved` events.

## [​](https://docs.polymarket.com/market-data/websocket/market-channel\#message-types)  Message Types

Each message includes an `event_type` field identifying the type.

### [​](https://docs.polymarket.com/market-data/websocket/market-channel\#book)  book

Emitted when first subscribed to a market and when there is a trade that affects the book.

Copy

Ask AI

```
{
  "event_type": "book",
  "asset_id": "65818619657568813474341868652308942079804919287380422192892211131408793125422",
  "market": "0xbd31dc8a20211944f6b70f31557f1001557b59905b7738480ca09bd4532f84af",
  "bids": [\
    { "price": ".48", "size": "30" },\
    { "price": ".49", "size": "20" },\
    { "price": ".50", "size": "15" }\
  ],
  "asks": [\
    { "price": ".52", "size": "25" },\
    { "price": ".53", "size": "60" },\
    { "price": ".54", "size": "10" }\
  ],
  "timestamp": "123456789000",
  "hash": "0x0...."
}
```

### [​](https://docs.polymarket.com/market-data/websocket/market-channel\#price_change)  price\_change

Emitted when a new order is placed or an order is cancelled.

Copy

Ask AI

```
{
  "market": "0x5f65177b394277fd294cd75650044e32ba009a95022d88a0c1d565897d72f8f1",
  "price_changes": [\
    {\
      "asset_id": "71321045679252212594626385532706912750332728571942532289631379312455583992563",\
      "price": "0.5",\
      "size": "200",\
      "side": "BUY",\
      "hash": "56621a121a47ed9333273e21c83b660cff37ae50",\
      "best_bid": "0.5",\
      "best_ask": "1"\
    },\
    {\
      "asset_id": "52114319501245915516055106046884209969926127482827954674443846427813813222426",\
      "price": "0.5",\
      "size": "200",\
      "side": "SELL",\
      "hash": "1895759e4df7a796bf4f1c5a5950b748306923e2",\
      "best_bid": "0",\
      "best_ask": "0.5"\
    }\
  ],
  "timestamp": "1757908892351",
  "event_type": "price_change"
}
```

A `size` of `"0"` means the price level has been removed from the book.

### [​](https://docs.polymarket.com/market-data/websocket/market-channel\#tick_size_change)  tick\_size\_change

Emitted when the minimum tick size of a market changes. This happens when the book’s price reaches the limits: price > 0.96 or price < 0.04.

Copy

Ask AI

```
{
  "event_type": "tick_size_change",
  "asset_id": "65818619657568813474341868652308942079804919287380422192892211131408793125422",
  "market": "0xbd31dc8a20211944f6b70f31557f1001557b59905b7738480ca09bd4532f84af",
  "old_tick_size": "0.01",
  "new_tick_size": "0.001",
  "timestamp": "100000000"
}
```

### [​](https://docs.polymarket.com/market-data/websocket/market-channel\#last_trade_price)  last\_trade\_price

Emitted when a maker and taker order is matched, creating a trade event.

Copy

Ask AI

```
{
  "asset_id": "114122071509644379678018727908709560226618148003371446110114509806601493071694",
  "event_type": "last_trade_price",
  "fee_rate_bps": "0",
  "market": "0x6a67b9d828d53862160e470329ffea5246f338ecfffdf2cab45211ec578b0347",
  "price": "0.456",
  "side": "BUY",
  "size": "219.217767",
  "timestamp": "1750428146322"
}
```

### [​](https://docs.polymarket.com/market-data/websocket/market-channel\#best_bid_ask)  best\_bid\_ask

Requires `custom_feature_enabled: true`.

Emitted when the best bid or ask prices for a market change.

Copy

Ask AI

```
{
  "event_type": "best_bid_ask",
  "market": "0x0005c0d312de0be897668695bae9f32b624b4a1ae8b140c49f08447fcc74f442",
  "asset_id": "85354956062430465315924116860125388538595433819574542752031640332592237464430",
  "best_bid": "0.73",
  "best_ask": "0.77",
  "spread": "0.04",
  "timestamp": "1766789469958"
}
```

### [​](https://docs.polymarket.com/market-data/websocket/market-channel\#new_market)  new\_market

Requires `custom_feature_enabled: true`.

Emitted when a new market is created.

Copy

Ask AI

```
{
  "id": "1031769",
  "question": "Will NVIDIA (NVDA) close above $240 end of January?",
  "market": "0x311d0c4b6671ab54af4970c06fcf58662516f5168997bdda209ec3db5aa6b0c1",
  "slug": "nvda-above-240-on-january-30-2026",
  "description": "This market will resolve to \"Yes\" if the official closing price...",
  "assets_ids": [\
    "76043073756653678226373981964075571318267289248134717369284518995922789326425",\
    "31690934263385727664202099278545688007799199447969475608906331829650099442770"\
  ],
  "outcomes": ["Yes", "No"],
  "event_message": {
    "id": "125819",
    "ticker": "nvda-above-in-january-2026",
    "slug": "nvda-above-in-january-2026",
    "title": "Will NVIDIA (NVDA) close above ___ end of January?",
    "description": "This market will resolve to \"Yes\" if the official closing price..."
  },
  "timestamp": "1766790415550",
  "event_type": "new_market"
}
```

### [​](https://docs.polymarket.com/market-data/websocket/market-channel\#market_resolved)  market\_resolved

Requires `custom_feature_enabled: true`.

Emitted when a market is resolved.

Copy

Ask AI

```
{
  "id": "1031769",
  "question": "Will NVIDIA (NVDA) close above $240 end of January?",
  "market": "0x311d0c4b6671ab54af4970c06fcf58662516f5168997bdda209ec3db5aa6b0c1",
  "slug": "nvda-above-240-on-january-30-2026",
  "description": "This market will resolve to \"Yes\" if the official closing price...",
  "assets_ids": [\
    "76043073756653678226373981964075571318267289248134717369284518995922789326425",\
    "31690934263385727664202099278545688007799199447969475608906331829650099442770"\
  ],
  "outcomes": ["Yes", "No"],
  "winning_asset_id": "76043073756653678226373981964075571318267289248134717369284518995922789326425",
  "winning_outcome": "Yes",
  "event_message": {
    "id": "125819",
    "ticker": "nvda-above-in-january-2026",
    "slug": "nvda-above-in-january-2026",
    "title": "Will NVIDIA (NVDA) close above ___ end of January?",
    "description": "This market will resolve to \"Yes\" if the official closing price..."
  },
  "timestamp": "1766790415550",
  "event_type": "market_resolved"
}
```

Was this page helpful?

YesNo

[Overview\\
\\
Previous](https://docs.polymarket.com/market-data/websocket/overview) [User Channel\\
\\
Next](https://docs.polymarket.com/market-data/websocket/user-channel)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.

Suggestions

How do I connect to WebSocket streams?What's required to place my first order?How do I find and fetch market data?