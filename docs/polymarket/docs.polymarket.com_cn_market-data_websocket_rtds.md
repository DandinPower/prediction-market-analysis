---
url: "https://docs.polymarket.com/cn/market-data/websocket/rtds"
title: "Real-Time Data Socket - Polymarket Documentation"
---

[跳转到主要内容](https://docs.polymarket.com/cn/market-data/websocket/rtds#content-area)

[Polymarket Documentation home page![light logo](https://mintcdn.com/polymarket-292d1b1b/ZibMe6Tli_amZald/logo/light.svg?fit=max&auto=format&n=ZibMe6Tli_amZald&q=85&s=9f9bd559f02181495794661ef6426c0f)![dark logo](https://mintcdn.com/polymarket-292d1b1b/ZibMe6Tli_amZald/logo/dark.svg?fit=max&auto=format&n=ZibMe6Tli_amZald&q=85&s=13abc6754579a3475368ea99d0f5a241)](https://docs.polymarket.com/cn)

![CN](https://d3gk2c5xim1je2.cloudfront.net/flags/CN.svg)

简体中文

搜索...

Ctrl K询问AI

搜索...

Navigation

WebSocket

Real-Time Data Socket

[文档](https://docs.polymarket.com/cn) [API 参考](https://docs.polymarket.com/cn/api-reference/introduction)

![https://raw.githubusercontent.com/suhailkakar/demo/refs/heads/main/book.svg](https://raw.githubusercontent.com/suhailkakar/demo/refs/heads/main/book.svg)

##### 入门指南

- [概览](https://docs.polymarket.com/cn)
- [Polymarket 101](https://docs.polymarket.com/cn/polymarket-101)
- [快速入门](https://docs.polymarket.com/cn/quickstart)

![https://mintlify.s3.us-west-1.amazonaws.com/polymarket-292d1b1b/images/icons/nav/layers.svg](https://mintlify.s3.us-west-1.amazonaws.com/polymarket-292d1b1b/images/icons/nav/layers.svg)

##### 核心概念

- [市场与事件](https://docs.polymarket.com/cn/concepts/markets-events)
- [价格与订单簿](https://docs.polymarket.com/cn/concepts/prices-orderbook)
- [持仓与代币](https://docs.polymarket.com/cn/concepts/positions-tokens)
- [订单生命周期](https://docs.polymarket.com/cn/concepts/order-lifecycle)
- [判定](https://docs.polymarket.com/cn/concepts/resolution)

![https://mintlify.s3.us-west-1.amazonaws.com/polymarket-292d1b1b/images/icons/nav/paper.svg](https://mintlify.s3.us-west-1.amazonaws.com/polymarket-292d1b1b/images/icons/nav/paper.svg)

##### 市场数据

- [概览](https://docs.polymarket.com/cn/market-data/overview)
- [获取市场数据](https://docs.polymarket.com/cn/market-data/fetching-markets)
- [Subgraph](https://docs.polymarket.com/cn/market-data/subgraph)

![https://mintlify.s3.us-west-1.amazonaws.com/polymarket-292d1b1b/images/icons/nav/chart.svg](https://mintlify.s3.us-west-1.amazonaws.com/polymarket-292d1b1b/images/icons/nav/chart.svg)

##### 交易

- [概述](https://docs.polymarket.com/cn/trading/overview)
- [快速开始](https://docs.polymarket.com/cn/trading/quickstart)
- [Orderbook](https://docs.polymarket.com/cn/trading/orderbook)
- 订单

- [费用](https://docs.polymarket.com/cn/trading/fees)
- [免 Gas 交易](https://docs.polymarket.com/cn/trading/gasless)
- [Negative Risk 市场](https://docs.polymarket.com/cn/advanced/neg-risk)
- [撮合引擎重启](https://docs.polymarket.com/cn/trading/matching-engine)
- CTF 代币

- WebSocket

  - [概述](https://docs.polymarket.com/cn/market-data/websocket/overview)
  - [Market 频道](https://docs.polymarket.com/cn/market-data/websocket/market-channel)
  - [User Channel](https://docs.polymarket.com/cn/market-data/websocket/user-channel)
  - [Sports WebSocket](https://docs.polymarket.com/cn/market-data/websocket/sports)
  - [Real-Time Data Socket](https://docs.polymarket.com/cn/market-data/websocket/rtds)
- 跨链桥


![https://mintlify.s3.us-west-1.amazonaws.com/polymarket-292d1b1b/images/icons/nav/histogram.svg](https://mintlify.s3.us-west-1.amazonaws.com/polymarket-292d1b1b/images/icons/nav/histogram.svg)

##### 做市商

- [概述](https://docs.polymarket.com/cn/market-makers/overview)
- [入门指南](https://docs.polymarket.com/cn/market-makers/getting-started)
- [Maker 返利计划](https://docs.polymarket.com/cn/market-makers/maker-rebates)
- [流动性奖励](https://docs.polymarket.com/cn/market-makers/liquidity-rewards)
- 操作


![https://mintlify.s3.us-west-1.amazonaws.com/polymarket-292d1b1b/images/icons/nav/trophy.svg](https://mintlify.s3.us-west-1.amazonaws.com/polymarket-292d1b1b/images/icons/nav/trophy.svg)

##### 构建者计划

- [构建者计划](https://docs.polymarket.com/cn/builders/overview)
- [API Keys](https://docs.polymarket.com/cn/builders/api-keys)
- [Tiers](https://docs.polymarket.com/cn/builders/tiers)

![https://mintlify.s3.us-west-1.amazonaws.com/polymarket-292d1b1b/images/icons/nav/book-search.svg](https://mintlify.s3.us-west-1.amazonaws.com/polymarket-292d1b1b/images/icons/nav/book-search.svg)

##### 资源

- [合约地址](https://docs.polymarket.com/cn/resources/contract-addresses)
- [错误码](https://docs.polymarket.com/cn/resources/error-codes)

在此页面

- [端点](https://docs.polymarket.com/cn/market-data/websocket/rtds#%E7%AB%AF%E7%82%B9)
- [订阅](https://docs.polymarket.com/cn/market-data/websocket/rtds#%E8%AE%A2%E9%98%85)
- [消息结构](https://docs.polymarket.com/cn/market-data/websocket/rtds#%E6%B6%88%E6%81%AF%E7%BB%93%E6%9E%84)
- [加密货币价格](https://docs.polymarket.com/cn/market-data/websocket/rtds#%E5%8A%A0%E5%AF%86%E8%B4%A7%E5%B8%81%E4%BB%B7%E6%A0%BC)
- [Binance 来源](https://docs.polymarket.com/cn/market-data/websocket/rtds#binance-%E6%9D%A5%E6%BA%90)
- [Chainlink 来源](https://docs.polymarket.com/cn/market-data/websocket/rtds#chainlink-%E6%9D%A5%E6%BA%90)
- [价格 Payload 字段](https://docs.polymarket.com/cn/market-data/websocket/rtds#%E4%BB%B7%E6%A0%BC-payload-%E5%AD%97%E6%AE%B5)
- [支持的交易对](https://docs.polymarket.com/cn/market-data/websocket/rtds#%E6%94%AF%E6%8C%81%E7%9A%84%E4%BA%A4%E6%98%93%E5%AF%B9)
- [评论](https://docs.polymarket.com/cn/market-data/websocket/rtds#%E8%AF%84%E8%AE%BA)
- [订阅](https://docs.polymarket.com/cn/market-data/websocket/rtds#%E8%AE%A2%E9%98%85-2)
- [消息类型](https://docs.polymarket.com/cn/market-data/websocket/rtds#%E6%B6%88%E6%81%AF%E7%B1%BB%E5%9E%8B)
- [comment\_created](https://docs.polymarket.com/cn/market-data/websocket/rtds#comment_created)
- [评论 Payload 字段](https://docs.polymarket.com/cn/market-data/websocket/rtds#%E8%AF%84%E8%AE%BA-payload-%E5%AD%97%E6%AE%B5)
- [Profile 对象字段](https://docs.polymarket.com/cn/market-data/websocket/rtds#profile-%E5%AF%B9%E8%B1%A1%E5%AD%97%E6%AE%B5)
- [评论层级结构](https://docs.polymarket.com/cn/market-data/websocket/rtds#%E8%AF%84%E8%AE%BA%E5%B1%82%E7%BA%A7%E7%BB%93%E6%9E%84)
- [故障排除](https://docs.polymarket.com/cn/market-data/websocket/rtds#%E6%95%85%E9%9A%9C%E6%8E%92%E9%99%A4)

Polymarket Real-Time Data Socket (RTDS) 是一个基于 WebSocket 的流式服务，提供 **评论** 和 **加密货币价格** 的实时更新。

[**TypeScript client** \\
\\
官方 RTDS TypeScript 客户端 (`real-time-data-client`)。](https://github.com/Polymarket/real-time-data-client)

## [​](https://docs.polymarket.com/cn/market-data/websocket/rtds\#%E7%AB%AF%E7%82%B9)  端点

复制

询问AI

```
wss://ws-live-data.polymarket.com
```

某些用户特定的流可能需要使用你的钱包地址进行 `gamma_auth` 身份验证。

## [​](https://docs.polymarket.com/cn/market-data/websocket/rtds\#%E8%AE%A2%E9%98%85)  订阅

发送 JSON 消息来订阅数据流:

复制

询问AI

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

要取消订阅，发送相同结构的消息，将 `"action"` 改为 `"unsubscribe"`。你可以在不断开连接的情况下添加、删除和修改订阅。每 5 秒发送一次 `PING` 消息以维持连接。

仅支持下文记录的订阅类型。

## [​](https://docs.polymarket.com/cn/market-data/websocket/rtds\#%E6%B6%88%E6%81%AF%E7%BB%93%E6%9E%84)  消息结构

所有消息都遵循以下结构:

复制

询问AI

```
{
  "topic": "string",
  "type": "string",
  "timestamp": "number",
  "payload": "object"
}
```

| 字段 | 类型 | 描述 |
| --- | --- | --- |
| `topic` | string | 订阅主题(例如 `crypto_prices`、`comments`) |
| `type` | string | 消息类型/事件(例如 `update`、`reaction_created`) |
| `timestamp` | number | 消息发送时的 Unix 时间戳(毫秒) |
| `payload` | object | 特定于事件的数据对象 |

## [​](https://docs.polymarket.com/cn/market-data/websocket/rtds\#%E5%8A%A0%E5%AF%86%E8%B4%A7%E5%B8%81%E4%BB%B7%E6%A0%BC)  加密货币价格

来自两个来源的实时加密货币价格数据: **Binance** 和 **Chainlink**。无需身份验证。

### [​](https://docs.polymarket.com/cn/market-data/websocket/rtds\#binance-%E6%9D%A5%E6%BA%90)  Binance 来源

订阅所有交易对:

复制

询问AI

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

使用逗号分隔的过滤器订阅特定交易对:

复制

询问AI

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

交易对使用小写连接格式(例如 `solusdt`、`btcusdt`)。**Solana 价格更新:**

复制

询问AI

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

**Bitcoin 价格更新:**

复制

询问AI

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

### [​](https://docs.polymarket.com/cn/market-data/websocket/rtds\#chainlink-%E6%9D%A5%E6%BA%90)  Chainlink 来源

**正在交易 15 分钟加密货币市场？** 获取由 Chainlink 赞助的 Chainlink API 密钥，并获得入门支持。填写 [此表单](https://pm-ds-request.streams.chain.link/)。

订阅所有交易对:

复制

询问AI

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

使用 JSON 过滤器订阅特定交易对:

复制

询问AI

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

交易对使用斜杠分隔格式(例如 `eth/usd`、`btc/usd`)。**Ethereum 价格更新:**

复制

询问AI

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

**Bitcoin 价格更新:**

复制

询问AI

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

### [​](https://docs.polymarket.com/cn/market-data/websocket/rtds\#%E4%BB%B7%E6%A0%BC-payload-%E5%AD%97%E6%AE%B5)  价格 Payload 字段

| 字段 | 类型 | 描述 |
| --- | --- | --- |
| `symbol` | string | 交易对符号。 **Binance**: 小写连接(例如 `solusdt`、`btcusdt`)。 **Chainlink**: 斜杠分隔(例如 `eth/usd`、`btc/usd`) |
| `timestamp` | number | 价格记录时间，Unix 毫秒时间戳 |
| `value` | number | 计价货币中的当前价格值 |

### [​](https://docs.polymarket.com/cn/market-data/websocket/rtds\#%E6%94%AF%E6%8C%81%E7%9A%84%E4%BA%A4%E6%98%93%E5%AF%B9)  支持的交易对

**Binance 来源** — 小写连接格式:

- `btcusdt` — Bitcoin 对 USDT
- `ethusdt` — Ethereum 对 USDT
- `solusdt` — Solana 对 USDT
- `xrpusdt` — XRP 对 USDT

**Chainlink 来源** — 斜杠分隔格式:

- `btc/usd` — Bitcoin 对 USD
- `eth/usd` — Ethereum 对 USD
- `sol/usd` — Solana 对 USD
- `xrp/usd` — XRP 对 USD

## [​](https://docs.polymarket.com/cn/market-data/websocket/rtds\#%E8%AF%84%E8%AE%BA)  评论

Polymarket 平台上的实时评论事件，包括新评论、回复、反应和删除。某些用户特定数据可能需要 Gamma 身份验证。

### [​](https://docs.polymarket.com/cn/market-data/websocket/rtds\#%E8%AE%A2%E9%98%85-2)  订阅

复制

询问AI

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

### [​](https://docs.polymarket.com/cn/market-data/websocket/rtds\#%E6%B6%88%E6%81%AF%E7%B1%BB%E5%9E%8B)  消息类型

| 类型 | 描述 |
| --- | --- |
| `comment_created` | 用户创建新评论或回复 |
| `comment_removed` | 评论被移除或删除 |
| `reaction_created` | 用户对评论添加反应 |
| `reaction_removed` | 反应从评论中移除 |

### [​](https://docs.polymarket.com/cn/market-data/websocket/rtds\#comment_created)  comment\_created

当用户发布新评论或回复现有评论时触发。

复制

询问AI

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

对上述评论的回复 — 注意 `parentCommentID` 引用了父评论:

复制

询问AI

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

### [​](https://docs.polymarket.com/cn/market-data/websocket/rtds\#%E8%AF%84%E8%AE%BA-payload-%E5%AD%97%E6%AE%B5)  评论 Payload 字段

| 字段 | 类型 | 描述 |
| --- | --- | --- |
| `body` | string | 评论的文本内容 |
| `createdAt` | string | 评论创建时的 ISO 8601 时间戳 |
| `id` | string | 此评论的唯一标识符 |
| `parentCommentID` | string | 如果这是回复，则为父评论的 ID(顶级评论为 null) |
| `parentEntityID` | number | 父实体(事件、市场等)的 ID |
| `parentEntityType` | string | 父实体的类型(`Event`、`Market`) |
| `profile` | object | 评论作者的个人资料信息 |
| `reactionCount` | number | 此评论当前的反应数量 |
| `replyAddress` | string | 用于回复的 Polygon 地址(可能与 userAddress 不同) |
| `reportCount` | number | 此评论当前的举报数量 |
| `userAddress` | string | 评论作者的 Polygon 地址 |

### [​](https://docs.polymarket.com/cn/market-data/websocket/rtds\#profile-%E5%AF%B9%E8%B1%A1%E5%AD%97%E6%AE%B5)  Profile 对象字段

| 字段 | 类型 | 描述 |
| --- | --- | --- |
| `baseAddress` | string | 用户资料地址 |
| `displayUsernamePublic` | boolean | 用户名是否公开显示 |
| `name` | string | 用户的显示名称 |
| `proxyWallet` | string | 用于交易的代理钱包地址 |
| `pseudonym` | string | 为用户生成的假名 |

### [​](https://docs.polymarket.com/cn/market-data/websocket/rtds\#%E8%AF%84%E8%AE%BA%E5%B1%82%E7%BA%A7%E7%BB%93%E6%9E%84)  评论层级结构

评论支持嵌套分层:

- **顶级评论**: `parentCommentID` 为 null 或为空
- **回复评论**: `parentCommentID` 包含父评论的 ID
- 所有评论都与 `parentEntityID` 和 `parentEntityType`(`Event` 或 `Market`)关联

## [​](https://docs.polymarket.com/cn/market-data/websocket/rtds\#%E6%95%85%E9%9A%9C%E6%8E%92%E9%99%A4)  故障排除

连接意外断开

每 5 秒发送一次 `PING` 消息以保持连接活跃。连接错误将触发自动重连尝试。

订阅后未收到消息

验证你的订阅消息是否为有效的 JSON，并包含正确的 `action`、`topic` 和 `type` 字段。无效的订阅消息可能导致连接关闭。

身份验证失败

如果订阅用户特定的流，请确保你的 `gamma_auth` 对象包含有效的钱包 `address`。身份验证失败将阻止订阅受保护的主题。

此页面对您有帮助吗？

是否

[Sports WebSocket\\
\\
上一页](https://docs.polymarket.com/cn/market-data/websocket/sports) [充值\\
\\
下一页](https://docs.polymarket.com/cn/trading/bridge/deposit)

Ctrl+I

助手

AI生成的回答可能包含错误。