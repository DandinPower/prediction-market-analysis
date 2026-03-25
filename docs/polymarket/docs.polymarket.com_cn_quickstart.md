---
url: "https://docs.polymarket.com/cn/quickstart"
title: "快速入门 - Polymarket Documentation"
---

[跳转到主要内容](https://docs.polymarket.com/cn/quickstart#content-area)

[Polymarket Documentation home page![light logo](https://mintcdn.com/polymarket-292d1b1b/ZibMe6Tli_amZald/logo/light.svg?fit=max&auto=format&n=ZibMe6Tli_amZald&q=85&s=9f9bd559f02181495794661ef6426c0f)![dark logo](https://mintcdn.com/polymarket-292d1b1b/ZibMe6Tli_amZald/logo/dark.svg?fit=max&auto=format&n=ZibMe6Tli_amZald&q=85&s=13abc6754579a3475368ea99d0f5a241)](https://docs.polymarket.com/cn)

![CN](https://d3gk2c5xim1je2.cloudfront.net/flags/CN.svg)

简体中文

搜索...

Ctrl K询问AI

搜索...

Navigation

入门指南

快速入门

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

- [下一步](https://docs.polymarket.com/cn/quickstart#%E4%B8%8B%E4%B8%80%E6%AD%A5)

几分钟内上手 Polymarket API——获取市场数据并下达你的第一笔订单。

1

[Navigate to header](https://docs.polymarket.com/cn/quickstart#)

获取市场数据

所有数据接口都是公开的，无需 API 密钥或身份验证。使用 markets 接口查找市场并获取其 token ID：

- cURL

- TypeScript

- Python


复制

询问AI

```
curl "https://gamma-api.polymarket.com/markets?active=true&closed=false&limit=1"
```

复制

询问AI

```
const response = await fetch(
  "https://gamma-api.polymarket.com/markets?active=true&closed=false&limit=1"
);
const markets = await response.json();

const market = markets[0];
console.log(market.question);
console.log(market.clobTokenIds);
// ["123456...", "789012..."]  — [Yes token ID, No token ID]
```

复制

询问AI

```
import requests

response = requests.get(
    "https://gamma-api.polymarket.com/markets",
    params={"active": "true", "closed": "false", "limit": 1}
)
markets = response.json()

market = markets[0]
print(market["question"])
print(market["clobTokenIds"])
# ["123456...", "789012..."]  — [Yes token ID, No token ID]
```

从 `clobTokenIds` 中保存一个 token ID——下单时需要用到。第一个 ID 是 Yes 代币，第二个是 No 代币。更多获取方式（如按 slug、标签或事件获取）请参阅 [获取市场数据](https://docs.polymarket.com/market-data/fetching-markets)。

2

[Navigate to header](https://docs.polymarket.com/cn/quickstart#)

安装 SDK

TypeScript

Python

复制

询问AI

```
npm install @polymarket/clob-client ethers@5
```

3

[Navigate to header](https://docs.polymarket.com/cn/quickstart#)

配置客户端

派生 API 凭证并初始化交易客户端：

- TypeScript

- Python


复制

询问AI

```
import { ClobClient } from "@polymarket/clob-client";
import { Wallet } from "ethers"; // v5.8.0

const HOST = "https://clob.polymarket.com";
const CHAIN_ID = 137; // Polygon mainnet
const signer = new Wallet(process.env.PRIVATE_KEY);

// Derive API credentials (L1 → L2 auth)
const tempClient = new ClobClient(HOST, CHAIN_ID, signer);
const apiCreds = await tempClient.createOrDeriveApiKey();

// Initialize trading client
const client = new ClobClient(
  HOST,
  CHAIN_ID,
  signer,
  apiCreds,
  0, // Signature type: 0 = EOA
  signer.address, // Funder address
);
```

复制

询问AI

```
from py_clob_client.client import ClobClient
import os

host = "https://clob.polymarket.com"
chain_id = 137  # Polygon mainnet
private_key = os.getenv("PRIVATE_KEY")

# Derive API credentials (L1 → L2 auth)
temp_client = ClobClient(host, key=private_key, chain_id=chain_id)
api_creds = temp_client.create_or_derive_api_creds()

# Initialize trading client
client = ClobClient(
    host,
    key=private_key,
    chain_id=chain_id,
    creds=api_creds,
    signature_type=0,  # Signature type: 0 = EOA
    funder="YOUR_WALLET_ADDRESS",  # Funder address
)
```

本示例使用 EOA 钱包（签名类型 `0`），由你的钱包自行支付 gas 费。代理钱包用户（类型 `1` 和 `2`）可以使用 Polymarket 的 gasless
relayer。详情请参阅 [身份验证](https://docs.polymarket.com/api-reference/authentication) 中关于签名类型的说明。

交易前，你的 funder 地址需要持有 **USDC.e**（用于购买结果代币）和 **POL**（用于支付 gas 费，仅 EOA 类型 `0` 需要）。

4

[Navigate to header](https://docs.polymarket.com/cn/quickstart#)

下达订单

使用第 1 步获取的 `token_id` 下达限价单：

- TypeScript

- Python


复制

询问AI

```
import { Side, OrderType } from "@polymarket/clob-client";

// Fetch market details to get tick size and neg risk
const market = await client.getMarket("YOUR_CONDITION_ID");
const tickSize = String(market.minimum_tick_size);   // e.g., "0.01"
const negRisk = market.neg_risk;             // e.g., false

const response = await client.createAndPostOrder(
  {
    tokenID: "YOUR_TOKEN_ID", // From Step 1
    price: 0.50,
    size: 10,
    side: Side.BUY,
    orderType: OrderType.GTC,
  },
  {
    tickSize,
    negRisk,
  },
);

console.log("Order ID:", response.orderID);
console.log("Status:", response.status);
```

复制

询问AI

```
from py_clob_client.clob_types import OrderArgs, OrderType
from py_clob_client.order_builder.constants import BUY

# Fetch market details to get tick size and neg risk
market = client.get_market("YOUR_CONDITION_ID")
tick_size = str(market["minimum_tick_size"])   # e.g., "0.01"
neg_risk = market["neg_risk"]             # e.g., False

response = client.create_and_post_order(
    OrderArgs(
        token_id="YOUR_TOKEN_ID",  # From Step 1
        price=0.50,
        size=10,
        side=BUY,
        order_type=OrderType.GTC,
    ),
    options={
        "tick_size": tick_size,
        "neg_risk": neg_risk,
    },
)

print("Order ID:", response["orderID"])
print("Status:", response["status"])
```

* * *

## [​](https://docs.polymarket.com/cn/quickstart\#%E4%B8%8B%E4%B8%80%E6%AD%A5)  下一步

[**身份验证** \\
\\
了解 L1/L2 认证、签名类型和 API 凭证。](https://docs.polymarket.com/api-reference/authentication)

[**交易快速入门** \\
\\
包含订单管理和问题排查的详细交易指南。](https://docs.polymarket.com/trading/quickstart)

[**获取市场数据** \\
\\
按 slug、标签或分类查找市场的策略。](https://docs.polymarket.com/market-data/fetching-markets)

[**核心概念** \\
\\
了解市场、事件、价格和持仓。](https://docs.polymarket.com/concepts/markets-events)

此页面对您有帮助吗？

是否

[Polymarket 101\\
\\
上一页](https://docs.polymarket.com/cn/polymarket-101) [市场与事件\\
\\
下一页](https://docs.polymarket.com/cn/concepts/markets-events)

Ctrl+I

助手

AI生成的回答可能包含错误。