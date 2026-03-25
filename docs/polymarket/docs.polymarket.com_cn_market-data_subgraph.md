---
url: "https://docs.polymarket.com/cn/market-data/subgraph"
title: "Subgraph - Polymarket Documentation"
---

[跳转到主要内容](https://docs.polymarket.com/cn/market-data/subgraph#content-area)

[Polymarket Documentation home page![light logo](https://mintcdn.com/polymarket-292d1b1b/ZibMe6Tli_amZald/logo/light.svg?fit=max&auto=format&n=ZibMe6Tli_amZald&q=85&s=9f9bd559f02181495794661ef6426c0f)![dark logo](https://mintcdn.com/polymarket-292d1b1b/ZibMe6Tli_amZald/logo/dark.svg?fit=max&auto=format&n=ZibMe6Tli_amZald&q=85&s=13abc6754579a3475368ea99d0f5a241)](https://docs.polymarket.com/cn)

![CN](https://d3gk2c5xim1je2.cloudfront.net/flags/CN.svg)

简体中文

搜索...

Ctrl K询问AI

搜索...

Navigation

市场数据

Subgraph

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

- [可用的 Subgraph](https://docs.polymarket.com/cn/market-data/subgraph#%E5%8F%AF%E7%94%A8%E7%9A%84-subgraph)
- [查询方式](https://docs.polymarket.com/cn/market-data/subgraph#%E6%9F%A5%E8%AF%A2%E6%96%B9%E5%BC%8F)
- [Schema 参考](https://docs.polymarket.com/cn/market-data/subgraph#schema-%E5%8F%82%E8%80%83)
- [Positions](https://docs.polymarket.com/cn/market-data/subgraph#positions)
- [Orders](https://docs.polymarket.com/cn/market-data/subgraph#orders)
- [Activity](https://docs.polymarket.com/cn/market-data/subgraph#activity)
- [Open Interest](https://docs.polymarket.com/cn/market-data/subgraph#open-interest)
- [PNL](https://docs.polymarket.com/cn/market-data/subgraph#pnl)
- [源代码](https://docs.polymarket.com/cn/market-data/subgraph#%E6%BA%90%E4%BB%A3%E7%A0%81)

Polymarket 的 Subgraph 通过 GraphQL 提供索引化的链上数据。你可以用它们查询持仓、交易量、流动性数据、订单、活动和市场数据。

## [​](https://docs.polymarket.com/cn/market-data/subgraph\#%E5%8F%AF%E7%94%A8%E7%9A%84-subgraph)  可用的 Subgraph

| Subgraph | 说明 | 端点 |
| --- | --- | --- |
| **Positions** | 用户代币余额 | [GraphQL Playground](https://api.goldsky.com/api/public/project_cl6mb8i9h0003e201j6li0diw/subgraphs/positions-subgraph/0.0.7/gn) |
| **Orders** | 订单簿和交易事件 | [GraphQL Playground](https://api.goldsky.com/api/public/project_cl6mb8i9h0003e201j6li0diw/subgraphs/orderbook-subgraph/0.0.1/gn) |
| **Activity** | 拆分、合并、兑换操作 | [GraphQL Playground](https://api.goldsky.com/api/public/project_cl6mb8i9h0003e201j6li0diw/subgraphs/activity-subgraph/0.0.4/gn) |
| **Open Interest** | 市场和全局未平仓合约 | [GraphQL Playground](https://api.goldsky.com/api/public/project_cl6mb8i9h0003e201j6li0diw/subgraphs/oi-subgraph/0.0.6/gn) |
| **PNL** | 用户持仓盈亏 | [GraphQL Playground](https://api.goldsky.com/api/public/project_cl6mb8i9h0003e201j6li0diw/subgraphs/pnl-subgraph/0.0.14/gn) |

Subgraph 由 [Goldsky](https://goldsky.com/) 托管。每个端点都包含交互式 GraphQL Playground，方便你探索数据结构。

## [​](https://docs.polymarket.com/cn/market-data/subgraph\#%E6%9F%A5%E8%AF%A2%E6%96%B9%E5%BC%8F)  查询方式

向任意 Subgraph 端点发送 POST 请求即可执行 GraphQL 查询。

复制

询问AI

```
curl -X POST \
  https://api.goldsky.com/api/public/project_cl6mb8i9h0003e201j6li0diw/subgraphs/orderbook-subgraph/0.0.1/gn \
  -H "Content-Type: application/json" \
  -d '{
    "query": "query MyQuery { orderbooks { id tradesQuantity } }"
  }'
```

## [​](https://docs.polymarket.com/cn/market-data/subgraph\#schema-%E5%8F%82%E8%80%83)  Schema 参考

### [​](https://docs.polymarket.com/cn/market-data/subgraph\#positions)  Positions

| 查询 | 说明 |
| --- | --- |
| `userBalance` / `userBalances` | 用户代币余额 |
| `netUserBalance` / `netUserBalances` | 聚合净余额 |
| `tokenIdCondition` / `tokenIdConditions` | Token ID 与条件的映射 |
| `condition` / `conditions` | 市场条件 |

### [​](https://docs.polymarket.com/cn/market-data/subgraph\#orders)  Orders

| 查询 | 说明 |
| --- | --- |
| `marketData` / `marketDatas` | 市场级别数据 |
| `orderFilledEvent` / `orderFilledEvents` | 订单成交事件 |
| `ordersMatchedEvent` / `ordersMatchedEvents` | 订单撮合事件 |
| `orderbook` / `orderbooks` | 订单簿状态 |
| `ordersMatchedGlobal` / `ordersMatchedGlobals` | 全局撮合统计 |

### [​](https://docs.polymarket.com/cn/market-data/subgraph\#activity)  Activity

| 查询 | 说明 |
| --- | --- |
| `split` / `splits` | USDC 拆分为代币 |
| `merge` / `merges` | 代币合并为 USDC |
| `redemption` / `redemptions` | 持仓兑换 |
| `negRiskConversion` / `negRiskConversions` | Neg risk 转换 |
| `negRiskEvent` / `negRiskEvents` | Neg risk 事件数据 |
| `fixedProductMarketMaker` / `fixedProductMarketMakers` | FPMM 数据 |
| `position` / `positions` | 持仓记录 |
| `condition` / `conditions` | 市场条件 |

### [​](https://docs.polymarket.com/cn/market-data/subgraph\#open-interest)  Open Interest

| 查询 | 说明 |
| --- | --- |
| `condition` / `conditions` | 市场条件 |
| `negRiskEvent` / `negRiskEvents` | Neg risk 事件数据 |
| `marketOpenInterest` / `marketOpenInterests` | 单市场未平仓合约 |
| `globalOpenInterest` / `globalOpenInterests` | 全局未平仓合约 |

### [​](https://docs.polymarket.com/cn/market-data/subgraph\#pnl)  PNL

| 查询 | 说明 |
| --- | --- |
| `userPosition` / `userPositions` | 用户持仓盈亏数据 |
| `negRiskEvent` / `negRiskEvents` | Neg risk 事件数据 |
| `condition` / `conditions` | 市场条件 |
| `fpmm` / `fpmms` | Fixed product market maker 数据 |

## [​](https://docs.polymarket.com/cn/market-data/subgraph\#%E6%BA%90%E4%BB%A3%E7%A0%81)  源代码

Subgraph 是开源的。你可以在 GitHub 上查看 schema 和映射：

[**polymarket-subgraph** \\
\\
查看源代码、schema 定义和部署配置。](https://github.com/Polymarket/polymarket-subgraph)

此页面对您有帮助吗？

是否

[获取市场数据\\
\\
上一页](https://docs.polymarket.com/cn/market-data/fetching-markets) [概述\\
\\
下一页](https://docs.polymarket.com/cn/trading/overview)

Ctrl+I

助手

AI生成的回答可能包含错误。