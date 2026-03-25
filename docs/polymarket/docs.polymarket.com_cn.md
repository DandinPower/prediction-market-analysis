---
url: "https://docs.polymarket.com/cn"
title: "概览 - Polymarket Documentation"
---

[跳转到主要内容](https://docs.polymarket.com/cn#content-area)

[Polymarket Documentation home page![light logo](https://mintcdn.com/polymarket-292d1b1b/ZibMe6Tli_amZald/logo/light.svg?fit=max&auto=format&n=ZibMe6Tli_amZald&q=85&s=9f9bd559f02181495794661ef6426c0f)![dark logo](https://mintcdn.com/polymarket-292d1b1b/ZibMe6Tli_amZald/logo/dark.svg?fit=max&auto=format&n=ZibMe6Tli_amZald&q=85&s=13abc6754579a3475368ea99d0f5a241)](https://docs.polymarket.com/cn)

![CN](https://d3gk2c5xim1je2.cloudfront.net/flags/CN.svg)

简体中文

搜索...

Ctrl K询问AI

搜索...

Navigation

入门指南

概览

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

# Polymarket 开发文档

基于全球最大的预测市场进行构建。为预测市场开发者提供 API、SDK 和工具。

## 开发者快速入门

几分钟内发出你的第一个 API 请求。了解 Polymarket 平台的基础知识，获取市场数据，下单交易，并兑换盈利仓位。

[开始使用 →](https://docs.polymarket.com/quickstart)

TypeScript

Python

复制

询问AI

```
import { ClobClient, Side } from "@polymarket/clob-client";

const client = new ClobClient(host, chainId, signer, creds);

const order = await client.createAndPostOrder(
  { tokenID, price: 0.50, size: 10, side: Side.BUY },
  { tickSize: "0.01", negRisk: false }
);
```

## 了解 Polymarket

学习基础知识，探索我们的 API，并开始在全球最大的预测市场上构建应用。

[**快速入门** \\
\\
设置你的开发环境，几分钟内完成第一个 API 调用。](https://docs.polymarket.com/quickstart)

[**核心概念** \\
\\
了解市场、事件、代币以及交易机制。](https://docs.polymarket.com/concepts/markets-events)

[**API 参考** \\
\\
浏览 REST 端点、WebSocket 数据流和身份验证。](https://docs.polymarket.com/api-reference/introduction)

[**SDK** \\
\\
官方 Python 和 TypeScript 库，加速你的开发。](https://docs.polymarket.com/api-reference/clients-sdks)

[![Banner](https://mintcdn.com/polymarket-292d1b1b/FOMte3ewbG-LVy3k/images/banner.png?fit=max&auto=format&n=FOMte3ewbG-LVy3k&q=85&s=d83f2f21e8474e998d8ba0f45810d978)](https://builders.polymarket.com/)

[![](https://docs.polymarket.com/images/icons/medal.svg)\\
**构建者计划** 在 Polymarket 上构建应用，通过推动交易量获取奖励](https://builders.polymarket.com/) [![](https://docs.polymarket.com/images/icons/quiz.svg)\\
**帮助中心** 获取支持、报告问题、查找常见问题的答案](https://help.polymarket.com/) [![](https://docs.polymarket.com/images/icons/sensor.svg)\\
**服务状态** 查看 API 运行时间、服务健康状况和故障报告](https://status.polymarket.com/)

Ctrl+I

助手

AI生成的回答可能包含错误。

![Banner](https://mintcdn.com/polymarket-292d1b1b/FOMte3ewbG-LVy3k/images/banner.png?w=1650&fit=max&auto=format&n=FOMte3ewbG-LVy3k&q=85&s=121075a6d26595fafb3e82922810fbff)

![](https://docs.polymarket.com/images/icons/medal.svg)

![](https://docs.polymarket.com/images/icons/quiz.svg)

![](https://docs.polymarket.com/images/icons/sensor.svg)