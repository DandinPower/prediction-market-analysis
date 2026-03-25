---
url: "https://docs.polymarket.com/cn/market-data/fetching-markets"
title: "获取市场数据 - Polymarket Documentation"
---

[跳转到主要内容](https://docs.polymarket.com/cn/market-data/fetching-markets#content-area)

[Polymarket Documentation home page![light logo](https://mintcdn.com/polymarket-292d1b1b/ZibMe6Tli_amZald/logo/light.svg?fit=max&auto=format&n=ZibMe6Tli_amZald&q=85&s=9f9bd559f02181495794661ef6426c0f)![dark logo](https://mintcdn.com/polymarket-292d1b1b/ZibMe6Tli_amZald/logo/dark.svg?fit=max&auto=format&n=ZibMe6Tli_amZald&q=85&s=13abc6754579a3475368ea99d0f5a241)](https://docs.polymarket.com/cn)

![CN](https://d3gk2c5xim1je2.cloudfront.net/flags/CN.svg)

简体中文

搜索...

Ctrl K询问AI

搜索...

Navigation

市场数据

获取市场数据

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

- [按 Slug 查询](https://docs.polymarket.com/cn/market-data/fetching-markets#%E6%8C%89-slug-%E6%9F%A5%E8%AF%A2)
- [如何提取 Slug](https://docs.polymarket.com/cn/market-data/fetching-markets#%E5%A6%82%E4%BD%95%E6%8F%90%E5%8F%96-slug)
- [示例](https://docs.polymarket.com/cn/market-data/fetching-markets#%E7%A4%BA%E4%BE%8B)
- [按标签查询](https://docs.polymarket.com/cn/market-data/fetching-markets#%E6%8C%89%E6%A0%87%E7%AD%BE%E6%9F%A5%E8%AF%A2)
- [查看可用标签](https://docs.polymarket.com/cn/market-data/fetching-markets#%E6%9F%A5%E7%9C%8B%E5%8F%AF%E7%94%A8%E6%A0%87%E7%AD%BE)
- [按标签筛选](https://docs.polymarket.com/cn/market-data/fetching-markets#%E6%8C%89%E6%A0%87%E7%AD%BE%E7%AD%9B%E9%80%89)
- [其他标签筛选选项](https://docs.polymarket.com/cn/market-data/fetching-markets#%E5%85%B6%E4%BB%96%E6%A0%87%E7%AD%BE%E7%AD%9B%E9%80%89%E9%80%89%E9%A1%B9)
- [获取所有活跃市场](https://docs.polymarket.com/cn/market-data/fetching-markets#%E8%8E%B7%E5%8F%96%E6%89%80%E6%9C%89%E6%B4%BB%E8%B7%83%E5%B8%82%E5%9C%BA)
- [关键参数](https://docs.polymarket.com/cn/market-data/fetching-markets#%E5%85%B3%E9%94%AE%E5%8F%82%E6%95%B0)
- [分页](https://docs.polymarket.com/cn/market-data/fetching-markets#%E5%88%86%E9%A1%B5)
- [最佳实践](https://docs.polymarket.com/cn/market-data/fetching-markets#%E6%9C%80%E4%BD%B3%E5%AE%9E%E8%B7%B5)
- [下一步](https://docs.polymarket.com/cn/market-data/fetching-markets#%E4%B8%8B%E4%B8%80%E6%AD%A5)

事件和市场接口均支持分页。详情请参阅 [分页](https://docs.polymarket.com/cn/market-data/fetching-markets#%E5%88%86%E9%A1%B5) 部分。

获取市场数据有三种主要策略，各自适合不同的使用场景：

1. **按 Slug 查询** — 适合获取已知的特定市场或事件
2. **按标签查询** — 适合按分类或体育项目筛选市场
3. **通过事件接口** — 获取所有活跃市场的最高效方式

* * *

## [​](https://docs.polymarket.com/cn/market-data/fetching-markets\#%E6%8C%89-slug-%E6%9F%A5%E8%AF%A2)  按 Slug 查询

\*\*适用场景：\*\*需要获取你已知的特定市场或事件。获取单个市场或事件的最佳方式是使用其唯一的 slug 标识符。slug 可以直接在 Polymarket 前端的 URL 中找到。

### [​](https://docs.polymarket.com/cn/market-data/fetching-markets\#%E5%A6%82%E4%BD%95%E6%8F%90%E5%8F%96-slug)  如何提取 Slug

从任意 Polymarket URL 中，slug 是 `/event/` 后面的路径段：

复制

询问AI

```
https://polymarket.com/event/fed-decision-in-october
                                ↑
                      Slug: fed-decision-in-october
```

### [​](https://docs.polymarket.com/cn/market-data/fetching-markets\#%E7%A4%BA%E4%BE%8B)  示例

复制

询问AI

```
# 通过 slug 获取事件（查询参数方式）
curl "https://gamma-api.polymarket.com/events?slug=fed-decision-in-october"

# 或使用路径接口
curl "https://gamma-api.polymarket.com/events/slug/fed-decision-in-october"
```

复制

询问AI

```
# 通过 slug 获取市场（查询参数方式）
curl "https://gamma-api.polymarket.com/markets?slug=fed-decision-in-october"

# 或使用路径接口
curl "https://gamma-api.polymarket.com/markets/slug/fed-decision-in-october"
```

* * *

## [​](https://docs.polymarket.com/cn/market-data/fetching-markets\#%E6%8C%89%E6%A0%87%E7%AD%BE%E6%9F%A5%E8%AF%A2)  按标签查询

\*\*适用场景：\*\*需要按分类、体育项目或主题筛选市场。标签提供了对市场进行分类和筛选的方式。你可以先发现可用标签，然后使用它们进行筛选。

### [​](https://docs.polymarket.com/cn/market-data/fetching-markets\#%E6%9F%A5%E7%9C%8B%E5%8F%AF%E7%94%A8%E6%A0%87%E7%AD%BE)  查看可用标签

**通用标签：**`GET /tags`（Gamma API）**体育标签和元数据：**`GET /sports`（Gamma API）`/sports` 接口返回体育项目的元数据，包括标签 ID、图片、判定来源和系列信息。

### [​](https://docs.polymarket.com/cn/market-data/fetching-markets\#%E6%8C%89%E6%A0%87%E7%AD%BE%E7%AD%9B%E9%80%89)  按标签筛选

获取标签 ID 后，在事件和市场接口中使用 `tag_id` 参数：

复制

询问AI

```
# 获取特定标签的事件
curl "https://gamma-api.polymarket.com/events?tag_id=100381&limit=10&active=true&closed=false"
```

### [​](https://docs.polymarket.com/cn/market-data/fetching-markets\#%E5%85%B6%E4%BB%96%E6%A0%87%E7%AD%BE%E7%AD%9B%E9%80%89%E9%80%89%E9%A1%B9)  其他标签筛选选项

你还可以：

- 使用 `related_tags=true` 包含关联标签的市场
- 使用 `exclude_tag_id` 排除特定标签

复制

询问AI

```
# 包含关联标签
curl "https://gamma-api.polymarket.com/events?tag_id=100381&related_tags=true&active=true&closed=false"
```

* * *

## [​](https://docs.polymarket.com/cn/market-data/fetching-markets\#%E8%8E%B7%E5%8F%96%E6%89%80%E6%9C%89%E6%B4%BB%E8%B7%83%E5%B8%82%E5%9C%BA)  获取所有活跃市场

\*\*适用场景：\*\*需要获取所有可用的活跃市场，通常用于综合分析或市场发现。最高效的方法是使用事件接口加上 `active=true&closed=false`，因为事件包含其关联的市场。

复制

询问AI

```
curl "https://gamma-api.polymarket.com/events?active=true&closed=false&limit=100"
```

### [​](https://docs.polymarket.com/cn/market-data/fetching-markets\#%E5%85%B3%E9%94%AE%E5%8F%82%E6%95%B0)  关键参数

| 参数 | 说明 |
| --- | --- |
| `order` | 排序字段（`volume_24hr`、`volume`、`liquidity`、`start_date`、`end_date`、`competitive`、`closed_time`） |
| `ascending` | 排序方向（`true` 为升序，`false` 为降序），默认：`false` |
| `active` | 按活跃状态筛选（`true` 为当前可交易的事件） |
| `closed` | 按已关闭状态筛选 |
| `limit` | 每页返回的结果数 |
| `offset` | 分页跳过的结果数 |

复制

询问AI

```
# 获取交易量最高的活跃事件
curl "https://gamma-api.polymarket.com/events?active=true&closed=false&order=volume_24hr&ascending=false&limit=100"
```

* * *

## [​](https://docs.polymarket.com/cn/market-data/fetching-markets\#%E5%88%86%E9%A1%B5)  分页

所有列表接口都支持通过 `limit` 和 `offset` 参数进行分页：

复制

询问AI

```
# 第 1 页：前 50 条结果
curl "https://gamma-api.polymarket.com/events?active=true&closed=false&limit=50&offset=0"

# 第 2 页：接下来 50 条结果
curl "https://gamma-api.polymarket.com/events?active=true&closed=false&limit=50&offset=50"

# 第 3 页：再接下来 50 条结果
curl "https://gamma-api.polymarket.com/events?active=true&closed=false&limit=50&offset=100"
```

* * *

## [​](https://docs.polymarket.com/cn/market-data/fetching-markets\#%E6%9C%80%E4%BD%B3%E5%AE%9E%E8%B7%B5)  最佳实践

1. \*\*查询单个市场：\*\*使用 slug 方式直接查找
2. \*\*按分类浏览：\*\*使用标签筛选以减少 API 调用次数
3. \*\*完整的市场发现：\*\*使用事件接口配合分页
4. **除非需要历史数据，否则始终加上 `active=true&closed=false`**
5. **优先使用事件接口**——事件包含其关联市场，可以减少 API 调用次数

* * *

## [​](https://docs.polymarket.com/cn/market-data/fetching-markets\#%E4%B8%8B%E4%B8%80%E6%AD%A5)  下一步

[**API 参考** \\
\\
完整的接口文档，包含参数和响应结构。](https://docs.polymarket.com/api-reference/introduction)

[**Subgraph** \\
\\
通过 Polymarket Subgraph 直接查询链上数据。](https://docs.polymarket.com/market-data/subgraph)

此页面对您有帮助吗？

是否

[概览\\
\\
上一页](https://docs.polymarket.com/cn/market-data/overview) [Subgraph\\
\\
下一页](https://docs.polymarket.com/cn/market-data/subgraph)

Ctrl+I

助手

AI生成的回答可能包含错误。