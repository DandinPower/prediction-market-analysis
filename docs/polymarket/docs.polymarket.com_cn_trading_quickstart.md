---
url: "https://docs.polymarket.com/cn/trading/quickstart"
title: "快速开始 - Polymarket Documentation"
---

[跳转到主要内容](https://docs.polymarket.com/cn/trading/quickstart#content-area)

[Polymarket Documentation home page![light logo](https://mintcdn.com/polymarket-292d1b1b/ZibMe6Tli_amZald/logo/light.svg?fit=max&auto=format&n=ZibMe6Tli_amZald&q=85&s=9f9bd559f02181495794661ef6426c0f)![dark logo](https://mintcdn.com/polymarket-292d1b1b/ZibMe6Tli_amZald/logo/dark.svg?fit=max&auto=format&n=ZibMe6Tli_amZald&q=85&s=13abc6754579a3475368ea99d0f5a241)](https://docs.polymarket.com/cn)

![CN](https://d3gk2c5xim1je2.cloudfront.net/flags/CN.svg)

简体中文

搜索...

Ctrl K询问AI

搜索...

Navigation

交易

快速开始

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

- [问题排查](https://docs.polymarket.com/cn/trading/quickstart#%E9%97%AE%E9%A2%98%E6%8E%92%E6%9F%A5)
- [下一步](https://docs.polymarket.com/cn/trading/quickstart#%E4%B8%8B%E4%B8%80%E6%AD%A5)

本指南将带你完整体验在 Polymarket 上下达订单的全过程。

1

[Navigate to header](https://docs.polymarket.com/cn/trading/quickstart#)

安装 SDK

TypeScript

Python

复制

询问AI

```
npm install @polymarket/clob-client ethers@5
```

2

[Navigate to header](https://docs.polymarket.com/cn/trading/quickstart#)

设置你的客户端

生成你的 API 凭证并初始化交易客户端。本示例使用 EOA 钱包(类型 `0`)——你的钱包支付自己的 gas 费用并充当资金账户:

TypeScript

Python

复制

询问AI

```
import { ClobClient } from "@polymarket/clob-client";
import { Wallet } from "ethers"; // v5.8.0

const HOST = "https://clob.polymarket.com";
const CHAIN_ID = 137; // Polygon mainnet
const signer = new Wallet(process.env.PRIVATE_KEY);

// Derive API credentials
const tempClient = new ClobClient(HOST, CHAIN_ID, signer);
const apiCreds = await tempClient.createOrDeriveApiKey();

// Initialize trading client
const client = new ClobClient(
  HOST,
  CHAIN_ID,
  signer,
  apiCreds,
  0, // EOA
  signer.address,
);
```

如果你有 Polymarket.com 账户,你的资金在代理钱包中——请改用签名类型 `1` 或 `2`。详情请见 [签名类型](https://docs.polymarket.com/trading/overview#signature-types)。

在交易之前,你的资金账户地址需要 **USDC.e**(用于购买结果代币)和 **POL**(用于 gas,如果使用 EOA 类型 `0`)。代理钱包用户(类型 `1` 和 `2`)可以改用 Polymarket 的无 gas 中继器。

3

[Navigate to header](https://docs.polymarket.com/cn/trading/quickstart#)

下达订单

从 [Markets API](https://docs.polymarket.com/market-data/fetching-markets) 获取代币 ID,然后创建并提交你的订单:

TypeScript

Python

复制

询问AI

```
import { Side, OrderType } from "@polymarket/clob-client";

const response = await client.createAndPostOrder(
  {
    tokenID: "YOUR_TOKEN_ID",
    price: 0.5,
    size: 10,
    side: Side.BUY,
  },
  {
    tickSize: "0.01",
    negRisk: false, // Set to true for multi-outcome markets
  },
  OrderType.GTC,
);

console.log("Order ID:", response.orderID);
console.log("Status:", response.status);
```

使用 SDK 的 `getTickSize()` 和 `getNegRisk()` 方法,或从 API 返回的市场对象中查询市场的 `tickSize` 和 `negRisk` 值。

4

[Navigate to header](https://docs.polymarket.com/cn/trading/quickstart#)

查看你的订单

TypeScript

Python

复制

询问AI

```
// View all open orders
const openOrders = await client.getOpenOrders();
console.log(`You have ${openOrders.length} open orders`);

// View your trade history
const trades = await client.getTrades();
console.log(`You've made ${trades.length} trades`);

// Cancel an order
await client.cancelOrder(response.orderID);
```

* * *

## [​](https://docs.polymarket.com/cn/trading/quickstart\#%E9%97%AE%E9%A2%98%E6%8E%92%E6%9F%A5)  问题排查

L2 AUTH NOT AVAILABLE - Invalid Signature

生成的 API 凭证使用了错误的私钥、签名类型或资金账户地址。

- 检查 `signatureType` 是否与你的账户类型匹配(`0`、`1` 或 `2`)
- 确保 `funder` 与你的钱包类型正确对应
- 如果不确定,请使用 `createOrDeriveApiKey()` 重新生成凭证

Order rejected - insufficient balance

你的资金账户地址没有足够的代币:

- **买单(BUY)**: 需要在资金账户地址中有 USDC.e
- **卖单(SELL)**: 需要在资金账户地址中有结果代币
- 确保你的 USDC.e 余额大于未完成订单中已锁定的金额

Order rejected - insufficient allowance

你需要批准 Exchange 合约使用你的代币。这通常在你首次交易时通过 Polymarket UI 完成,或使用 CTF 合约的 `setApprovalForAll()` 方法完成。

什么是我的资金账户地址

你的资金账户地址是持有你资金的钱包:

- **EOA(类型 0)**: 直接是你的钱包地址
- **代理钱包(类型 1 或 2)**: 前往 [polymarket.com/settings](https://polymarket.com/settings) 在个人资料下拉菜单中查找钱包地址

如果代理钱包不存在,请先登录 Polymarket.com(钱包在首次登录时部署)。

Blocked by Cloudflare or Geoblock

你正在尝试从受限制的地区下达交易。详情请见 [地理限制](https://docs.polymarket.com/api-reference/geoblock)。

* * *

## [​](https://docs.polymarket.com/cn/trading/quickstart\#%E4%B8%8B%E4%B8%80%E6%AD%A5)  下一步

[**创建订单** \\
\\
订单类型、价格精度和错误处理](https://docs.polymarket.com/trading/orders/create)

[**订单归属** \\
\\
将订单归属到你的构建者账户以获得交易量积分](https://docs.polymarket.com/trading/orders/attribution)

此页面对您有帮助吗？

是否

[概述\\
\\
上一页](https://docs.polymarket.com/cn/trading/overview) [Orderbook\\
\\
下一页](https://docs.polymarket.com/cn/trading/orderbook)

Ctrl+I

助手

AI生成的回答可能包含错误。