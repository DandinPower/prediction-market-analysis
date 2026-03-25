---
url: "https://docs.polymarket.com/market-data/websocket/rtds"
title: "Real-Time Data Socket - Polymarket Documentation"
---

[Skip to main content](https://docs.polymarket.com/market-data/websocket/rtds#content-area)

[Polymarket Documentation home page![light logo](https://mintcdn.com/polymarket-292d1b1b/ZibMe6Tli_amZald/logo/light.svg?fit=max&auto=format&n=ZibMe6Tli_amZald&q=85&s=9f9bd559f02181495794661ef6426c0f)![dark logo](https://mintcdn.com/polymarket-292d1b1b/ZibMe6Tli_amZald/logo/dark.svg?fit=max&auto=format&n=ZibMe6Tli_amZald&q=85&s=13abc6754579a3475368ea99d0f5a241)](https://docs.polymarket.com/)

![US](https://d3gk2c5xim1je2.cloudfront.net/flags/US.svg)

English

Search...

Ctrl KAsk AI

Search...

Navigation

WebSocket

Real-Time Data Socket

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

- [Endpoint](https://docs.polymarket.com/market-data/websocket/rtds#endpoint)
- [Subscribing](https://docs.polymarket.com/market-data/websocket/rtds#subscribing)
- [Message Structure](https://docs.polymarket.com/market-data/websocket/rtds#message-structure)
- [Crypto Prices](https://docs.polymarket.com/market-data/websocket/rtds#crypto-prices)
- [Binance Source](https://docs.polymarket.com/market-data/websocket/rtds#binance-source)
- [Chainlink Source](https://docs.polymarket.com/market-data/websocket/rtds#chainlink-source)
- [Price Payload Fields](https://docs.polymarket.com/market-data/websocket/rtds#price-payload-fields)
- [Supported Symbols](https://docs.polymarket.com/market-data/websocket/rtds#supported-symbols)
- [Comments](https://docs.polymarket.com/market-data/websocket/rtds#comments)
- [Subscribe](https://docs.polymarket.com/market-data/websocket/rtds#subscribe)
- [Message Types](https://docs.polymarket.com/market-data/websocket/rtds#message-types)
- [comment\_created](https://docs.polymarket.com/market-data/websocket/rtds#comment_created)
- [Comment Payload Fields](https://docs.polymarket.com/market-data/websocket/rtds#comment-payload-fields)
- [Profile Object Fields](https://docs.polymarket.com/market-data/websocket/rtds#profile-object-fields)
- [Comment Hierarchy](https://docs.polymarket.com/market-data/websocket/rtds#comment-hierarchy)
- [Troubleshooting](https://docs.polymarket.com/market-data/websocket/rtds#troubleshooting)

The Polymarket Real-Time Data Socket (RTDS) is a WebSocket-based streaming service that provides real-time updates for **comments** and **crypto prices**.

[**TypeScript client** \\
\\
Official RTDS TypeScript client (`real-time-data-client`).](https://github.com/Polymarket/real-time-data-client)

## [​](https://docs.polymarket.com/market-data/websocket/rtds\#endpoint)  Endpoint

Copy

Ask AI

```
wss://ws-live-data.polymarket.com
```

Some user-specific streams may require `gamma_auth` with your wallet address.

## [​](https://docs.polymarket.com/market-data/websocket/rtds\#subscribing)  Subscribing

Send a JSON message to subscribe to data streams:

Copy

Ask AI

```
{
  "action": "subscribe",
  "subscriptions": [\
    {\
      "topic": "topic_name",\
      "type": "message_type",\
      "filters": "optional_filter_string",\
      "gamma_auth": {\
        "address": "wallet_address"\
      }\
    }\
  ]
}
```

To unsubscribe, send the same structure with `"action": "unsubscribe"`.Subscriptions can be added, removed, and modified without disconnecting. Send `PING` messages every 5 seconds to maintain the connection.

Only the subscription types documented below are supported.

## [​](https://docs.polymarket.com/market-data/websocket/rtds\#message-structure)  Message Structure

All messages follow this structure:

Copy

Ask AI

```
{
  "topic": "string",
  "type": "string",
  "timestamp": "number",
  "payload": "object"
}
```

| Field | Type | Description |
| --- | --- | --- |
| `topic` | string | The subscription topic (e.g., `crypto_prices`, `comments`) |
| `type` | string | The message type/event (e.g., `update`, `reaction_created`) |
| `timestamp` | number | Unix timestamp in milliseconds when the message was sent |
| `payload` | object | Event-specific data object |

## [​](https://docs.polymarket.com/market-data/websocket/rtds\#crypto-prices)  Crypto Prices

Real-time cryptocurrency price data from two sources: **Binance** and **Chainlink**. No authentication required.

### [​](https://docs.polymarket.com/market-data/websocket/rtds\#binance-source)  Binance Source

Subscribe to all symbols:

Copy

Ask AI

```
{
  "action": "subscribe",
  "subscriptions": [\
    {\
      "topic": "crypto_prices",\
      "type": "update"\
    }\
  ]
}
```

Subscribe to specific symbols with a comma-separated filter:

Copy

Ask AI

```
{
  "action": "subscribe",
  "subscriptions": [\
    {\
      "topic": "crypto_prices",\
      "type": "update",\
      "filters": "solusdt,btcusdt,ethusdt"\
    }\
  ]
}
```

Symbols use lowercase concatenated format (e.g., `solusdt`, `btcusdt`).**Solana price update:**

Copy

Ask AI

```
{
  "topic": "crypto_prices",
  "type": "update",
  "timestamp": 1753314064237,
  "payload": {
    "symbol": "solusdt",
    "timestamp": 1753314064213,
    "value": 189.55
  }
}
```

**Bitcoin price update:**

Copy

Ask AI

```
{
  "topic": "crypto_prices",
  "type": "update",
  "timestamp": 1753314088421,
  "payload": {
    "symbol": "btcusdt",
    "timestamp": 1753314088395,
    "value": 67234.50
  }
}
```

### [​](https://docs.polymarket.com/market-data/websocket/rtds\#chainlink-source)  Chainlink Source

**Trading 15m Crypto Markets?** Get a sponsored Chainlink API key with onboarding support from Chainlink. Fill out [this form](https://pm-ds-request.streams.chain.link/).

Subscribe to all symbols:

Copy

Ask AI

```
{
  "action": "subscribe",
  "subscriptions": [\
    {\
      "topic": "crypto_prices_chainlink",\
      "type": "*",\
      "filters": ""\
    }\
  ]
}
```

Subscribe to a specific symbol with a JSON filter:

Copy

Ask AI

```
{
  "action": "subscribe",
  "subscriptions": [\
    {\
      "topic": "crypto_prices_chainlink",\
      "type": "*",\
      "filters": "{\"symbol\":\"eth/usd\"}"\
    }\
  ]
}
```

Symbols use slash-separated format (e.g., `eth/usd`, `btc/usd`).**Ethereum price update:**

Copy

Ask AI

```
{
  "topic": "crypto_prices_chainlink",
  "type": "update",
  "timestamp": 1753314064237,
  "payload": {
    "symbol": "eth/usd",
    "timestamp": 1753314064213,
    "value": 3456.78
  }
}
```

**Bitcoin price update:**

Copy

Ask AI

```
{
  "topic": "crypto_prices_chainlink",
  "type": "update",
  "timestamp": 1753314088421,
  "payload": {
    "symbol": "btc/usd",
    "timestamp": 1753314088395,
    "value": 67234.50
  }
}
```

### [​](https://docs.polymarket.com/market-data/websocket/rtds\#price-payload-fields)  Price Payload Fields

| Field | Type | Description |
| --- | --- | --- |
| `symbol` | string | Trading pair symbol. **Binance**: lowercase concatenated (e.g., `solusdt`, `btcusdt`). **Chainlink**: slash-separated (e.g., `eth/usd`, `btc/usd`) |
| `timestamp` | number | When the price was recorded, in Unix milliseconds |
| `value` | number | Current price value in the quote currency |

### [​](https://docs.polymarket.com/market-data/websocket/rtds\#supported-symbols)  Supported Symbols

**Binance Source** — lowercase concatenated format:

- `btcusdt` — Bitcoin to USDT
- `ethusdt` — Ethereum to USDT
- `solusdt` — Solana to USDT
- `xrpusdt` — XRP to USDT

**Chainlink Source** — slash-separated format:

- `btc/usd` — Bitcoin to USD
- `eth/usd` — Ethereum to USD
- `sol/usd` — Solana to USD
- `xrp/usd` — XRP to USD

## [​](https://docs.polymarket.com/market-data/websocket/rtds\#comments)  Comments

Real-time comment events on the Polymarket platform, including new comments, replies, reactions, and removals. May require Gamma authentication for user-specific data.

### [​](https://docs.polymarket.com/market-data/websocket/rtds\#subscribe)  Subscribe

Copy

Ask AI

```
{
  "action": "subscribe",
  "subscriptions": [\
    {\
      "topic": "comments",\
      "type": "comment_created"\
    }\
  ]
}
```

### [​](https://docs.polymarket.com/market-data/websocket/rtds\#message-types)  Message Types

| Type | Description |
| --- | --- |
| `comment_created` | A user creates a new comment or reply |
| `comment_removed` | A comment is removed or deleted |
| `reaction_created` | A user adds a reaction to a comment |
| `reaction_removed` | A reaction is removed from a comment |

### [​](https://docs.polymarket.com/market-data/websocket/rtds\#comment_created)  comment\_created

Emitted when a user posts a new comment or replies to an existing one.

Copy

Ask AI

```
{
  "topic": "comments",
  "type": "comment_created",
  "timestamp": 1753454975808,
  "payload": {
    "body": "That's a good point about the definition.",
    "createdAt": "2025-07-25T14:49:35.801298Z",
    "id": "1763355",
    "parentCommentID": "1763325",
    "parentEntityID": 18396,
    "parentEntityType": "Event",
    "profile": {
      "baseAddress": "0xce533188d53a16ed580fd5121dedf166d3482677",
      "displayUsernamePublic": true,
      "name": "salted.caramel",
      "proxyWallet": "0x4ca749dcfa93c87e5ee23e2d21ff4422c7a4c1ee",
      "pseudonym": "Adored-Disparity"
    },
    "reactionCount": 0,
    "replyAddress": "0x0bda5d16f76cd1d3485bcc7a44bc6fa7db004cdd",
    "reportCount": 0,
    "userAddress": "0xce533188d53a16ed580fd5121dedf166d3482677"
  }
}
```

A reply to the above comment — note `parentCommentID` references the parent:

Copy

Ask AI

```
{
  "topic": "comments",
  "type": "comment_created",
  "timestamp": 1753454985123,
  "payload": {
    "body": "I agree, the resolution criteria should be clearer.",
    "createdAt": "2025-07-25T14:49:45.120000Z",
    "id": "1763356",
    "parentCommentID": "1763355",
    "parentEntityID": 18396,
    "parentEntityType": "Event",
    "profile": {
      "baseAddress": "0x1234567890abcdef1234567890abcdef12345678",
      "displayUsernamePublic": true,
      "name": "trader",
      "proxyWallet": "0x9876543210fedcba9876543210fedcba98765432",
      "pseudonym": "Bright-Analysis"
    },
    "reactionCount": 0,
    "replyAddress": "0x0bda5d16f76cd1d3485bcc7a44bc6fa7db004cdd",
    "reportCount": 0,
    "userAddress": "0x1234567890abcdef1234567890abcdef12345678"
  }
}
```

### [​](https://docs.polymarket.com/market-data/websocket/rtds\#comment-payload-fields)  Comment Payload Fields

| Field | Type | Description |
| --- | --- | --- |
| `body` | string | The text content of the comment |
| `createdAt` | string | ISO 8601 timestamp when the comment was created |
| `id` | string | Unique identifier for this comment |
| `parentCommentID` | string | ID of the parent comment if this is a reply (null for top-level comments) |
| `parentEntityID` | number | ID of the parent entity (event, market, etc.) |
| `parentEntityType` | string | Type of parent entity (`Event`, `Market`) |
| `profile` | object | Profile information of the comment author |
| `reactionCount` | number | Current number of reactions on this comment |
| `replyAddress` | string | Polygon address for replies (may differ from userAddress) |
| `reportCount` | number | Current number of reports on this comment |
| `userAddress` | string | Polygon address of the comment author |

### [​](https://docs.polymarket.com/market-data/websocket/rtds\#profile-object-fields)  Profile Object Fields

| Field | Type | Description |
| --- | --- | --- |
| `baseAddress` | string | User profile address |
| `displayUsernamePublic` | boolean | Whether the username is displayed publicly |
| `name` | string | User’s display name |
| `proxyWallet` | string | Proxy wallet address used for transactions |
| `pseudonym` | string | Generated pseudonym for the user |

### [​](https://docs.polymarket.com/market-data/websocket/rtds\#comment-hierarchy)  Comment Hierarchy

Comments support nested threading:

- **Top-level comments**: `parentCommentID` is null or empty
- **Reply comments**: `parentCommentID` contains the ID of the parent comment
- All comments are associated with a `parentEntityID` and `parentEntityType` (`Event` or `Market`)

## [​](https://docs.polymarket.com/market-data/websocket/rtds\#troubleshooting)  Troubleshooting

Connection drops unexpectedly

Send `PING` messages every 5 seconds to keep the connection alive. Connection errors will trigger automatic reconnection attempts.

Not receiving messages after subscribing

Verify your subscription message is valid JSON with the correct `action`, `topic`, and `type` fields. Invalid subscription messages may result in connection closure.

Authentication failures

If subscribing to user-specific streams, ensure your `gamma_auth` object includes a valid wallet `address`. Authentication failures will prevent subscription to protected topics.

Was this page helpful?

YesNo

[Sports WebSocket\\
\\
Previous](https://docs.polymarket.com/market-data/websocket/sports) [Deposit\\
\\
Next](https://docs.polymarket.com/trading/bridge/deposit)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.

Suggestions

How do I connect to WebSocket streams?What's required to place my first order?How do I find and fetch market data?