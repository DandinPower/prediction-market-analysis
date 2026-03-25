---
url: "https://docs.polymarket.com/cn/trading/gasless"
title: "免 Gas 交易 - Polymarket Documentation"
---

[跳转到主要内容](https://docs.polymarket.com/cn/trading/gasless#content-area)

[Polymarket Documentation home page![light logo](https://mintcdn.com/polymarket-292d1b1b/ZibMe6Tli_amZald/logo/light.svg?fit=max&auto=format&n=ZibMe6Tli_amZald&q=85&s=9f9bd559f02181495794661ef6426c0f)![dark logo](https://mintcdn.com/polymarket-292d1b1b/ZibMe6Tli_amZald/logo/dark.svg?fit=max&auto=format&n=ZibMe6Tli_amZald&q=85&s=13abc6754579a3475368ea99d0f5a241)](https://docs.polymarket.com/cn)

![CN](https://d3gk2c5xim1je2.cloudfront.net/flags/CN.svg)

简体中文

搜索...

Ctrl K询问AI

搜索...

Navigation

交易

免 Gas 交易

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

- [工作原理](https://docs.polymarket.com/cn/trading/gasless#%E5%B7%A5%E4%BD%9C%E5%8E%9F%E7%90%86)
- [覆盖范围](https://docs.polymarket.com/cn/trading/gasless#%E8%A6%86%E7%9B%96%E8%8C%83%E5%9B%B4)
- [身份验证](https://docs.polymarket.com/cn/trading/gasless#%E8%BA%AB%E4%BB%BD%E9%AA%8C%E8%AF%81)
- [使用 Builder API Keys](https://docs.polymarket.com/cn/trading/gasless#%E4%BD%BF%E7%94%A8-builder-api-keys)
- [使用 Relayer API Keys](https://docs.polymarket.com/cn/trading/gasless#%E4%BD%BF%E7%94%A8-relayer-api-keys)
- [前置要求](https://docs.polymarket.com/cn/trading/gasless#%E5%89%8D%E7%BD%AE%E8%A6%81%E6%B1%82)
- [安装](https://docs.polymarket.com/cn/trading/gasless#%E5%AE%89%E8%A3%85)
- [客户端设置](https://docs.polymarket.com/cn/trading/gasless#%E5%AE%A2%E6%88%B7%E7%AB%AF%E8%AE%BE%E7%BD%AE)
- [钱包类型](https://docs.polymarket.com/cn/trading/gasless#%E9%92%B1%E5%8C%85%E7%B1%BB%E5%9E%8B)
- [执行交易](https://docs.polymarket.com/cn/trading/gasless#%E6%89%A7%E8%A1%8C%E4%BA%A4%E6%98%93)
- [代币授权](https://docs.polymarket.com/cn/trading/gasless#%E4%BB%A3%E5%B8%81%E6%8E%88%E6%9D%83)
- [兑换仓位](https://docs.polymarket.com/cn/trading/gasless#%E5%85%91%E6%8D%A2%E4%BB%93%E4%BD%8D)
- [批量交易](https://docs.polymarket.com/cn/trading/gasless#%E6%89%B9%E9%87%8F%E4%BA%A4%E6%98%93)
- [交易状态](https://docs.polymarket.com/cn/trading/gasless#%E4%BA%A4%E6%98%93%E7%8A%B6%E6%80%81)
- [合约地址](https://docs.polymarket.com/cn/trading/gasless#%E5%90%88%E7%BA%A6%E5%9C%B0%E5%9D%80)
- [资源](https://docs.polymarket.com/cn/trading/gasless#%E8%B5%84%E6%BA%90)
- [下一步](https://docs.polymarket.com/cn/trading/gasless#%E4%B8%8B%E4%B8%80%E6%AD%A5)

Polymarket 的 **Relayer Client** 为你的用户提供免 gas 交易功能。用户无需持有 POL 来支付 gas 费，Polymarket 的基础设施会支付所有交易费用。这创造了一种无缝体验，用户只需要 USDC.e 就能交易。

## [​](https://docs.polymarket.com/cn/trading/gasless\#%E5%B7%A5%E4%BD%9C%E5%8E%9F%E7%90%86)  工作原理

relayer 充当交易赞助者：

1. 你的应用创建一笔交易
2. 用户用私钥签名
3. 你的应用将交易发送到 Polymarket 的 relayer
4. relayer 将交易提交到链上并支付 gas 费
5. 交易从用户钱包执行

免 gas 交易需要使用 **Builder API Keys** 或 **Relayer API Keys** 进行身份验证。

## [​](https://docs.polymarket.com/cn/trading/gasless\#%E8%A6%86%E7%9B%96%E8%8C%83%E5%9B%B4)  覆盖范围

Polymarket 为通过 relayer 路由的所有操作支付 gas：

| 操作 | 说明 |
| --- | --- |
| **Wallet deployment** | 为新用户部署 Safe 或 Proxy 钱包 |
| **Token approvals** | 授权合约使用 USDC.e 或结果代币 |
| **CTF operations** | 拆分、合并和兑换仓位 |
| **Transfers** | 在地址之间转移代币 |

## [​](https://docs.polymarket.com/cn/trading/gasless\#%E8%BA%AB%E4%BB%BD%E9%AA%8C%E8%AF%81)  身份验证

Relayer 支持两种身份验证方式。选择适合你用例的方式。

### [​](https://docs.polymarket.com/cn/trading/gasless\#%E4%BD%BF%E7%94%A8-builder-api-keys)  使用 Builder API Keys

Builder API Keys 适用于 [Builder Program](https://docs.polymarket.com/builders/overview) 成员。通过 HMAC-SHA256 签名 header 进行身份验证，使用 relayer SDK 时需要此方式。所有请求必须包含以下 header：

| Header | 说明 |
| --- | --- |
| `POLY_BUILDER_API_KEY` | 你的 Builder API key |
| `POLY_BUILDER_TIMESTAMP` | Unix 时间戳 |
| `POLY_BUILDER_PASSPHRASE` | 你的 Builder passphrase |
| `POLY_BUILDER_SIGNATURE` | HMAC-SHA256 签名 |

当你通过 `BuilderConfig` 提供凭证时，SDK 会自动处理 header 生成。

### [​](https://docs.polymarket.com/cn/trading/gasless\#%E4%BD%BF%E7%94%A8-relayer-api-keys)  使用 Relayer API Keys

Relayer API Keys 适用于做市商以及需要更简单方式的用户，无需 HMAC 签名。你可以在 Polymarket 网站的 **Settings > API Keys** 中创建。请求中需要包含以下 header：

| Header | 说明 |
| --- | --- |
| `RELAYER_API_KEY` | 你的 Relayer API key |
| `RELAYER_API_KEY_ADDRESS` | 拥有该 key 的地址 |

复制

询问AI

```
RELAYER_API_KEY: <your-api-key>
RELAYER_API_KEY_ADDRESS: 0xC7A2e308Efa0E5424220299Af2d85f05fa51eD2e
```

如果你想直接使用 Relayer API Key 而不使用 SDK，请参阅 [Relayer API Reference](https://docs.polymarket.com/api-reference)。

## [​](https://docs.polymarket.com/cn/trading/gasless\#%E5%89%8D%E7%BD%AE%E8%A6%81%E6%B1%82)  前置要求

使用 relayer 之前，你需要：

| 要求 | 来源 |
| --- | --- |
| Builder API 凭证 **或** Relayer API key | [Builder Profile](https://polymarket.com/settings?tab=builder) 或 [Settings > API Keys](https://polymarket.com/settings?tab=api-keys) |
| 用户的私钥或签名器 | 你的钱包集成 |
| USDC.e 余额 | 用于交易（不是用于 gas） |

## [​](https://docs.polymarket.com/cn/trading/gasless\#%E5%AE%89%E8%A3%85)  安装

npm

pip

复制

询问AI

```
npm install @polymarket/builder-relayer-client @polymarket/builder-signing-sdk
```

## [​](https://docs.polymarket.com/cn/trading/gasless\#%E5%AE%A2%E6%88%B7%E7%AB%AF%E8%AE%BE%E7%BD%AE)  客户端设置

使用你的签名配置初始化 relayer 客户端：

- 本地签名

- 远程签名


当你的后端安全地处理所有交易时，使用本地签名。

TypeScript

Python

复制

询问AI

```
import { createWalletClient, http, Hex } from "viem";
import { privateKeyToAccount } from "viem/accounts";
import { polygon } from "viem/chains";
import { RelayClient } from "@polymarket/builder-relayer-client";
import { BuilderConfig } from "@polymarket/builder-signing-sdk";

const account = privateKeyToAccount(process.env.PRIVATE_KEY as Hex);
const wallet = createWalletClient({
  account,
  chain: polygon,
  transport: http(process.env.RPC_URL),
});

const builderConfig = new BuilderConfig({
  localBuilderCreds: {
    key: process.env.POLY_BUILDER_API_KEY!,
    secret: process.env.POLY_BUILDER_SECRET!,
    passphrase: process.env.POLY_BUILDER_PASSPHRASE!,
  },
});

const client = new RelayClient(
  "https://relayer-v2.polymarket.com/",
  137,
  wallet,
  builderConfig,
);
```

使用远程签名将凭证保存在你控制的安全服务器上。**你的签名服务器** 接收请求详情并返回身份验证 header：

Server (TypeScript)

Server (Python)

复制

询问AI

```
import {
  buildHmacSignature,
  BuilderApiKeyCreds,
} from "@polymarket/builder-signing-sdk";

const BUILDER_CREDENTIALS: BuilderApiKeyCreds = {
  key: process.env.POLY_BUILDER_API_KEY!,
  secret: process.env.POLY_BUILDER_SECRET!,
  passphrase: process.env.POLY_BUILDER_PASSPHRASE!,
};

// POST /sign endpoint
export async function handleSignRequest(request) {
  const { method, path, body } = await request.json();
  const timestamp = Date.now().toString();

  const signature = buildHmacSignature(
    BUILDER_CREDENTIALS.secret,
    parseInt(timestamp),
    method,
    path,
    body,
  );

  return {
    POLY_BUILDER_SIGNATURE: signature,
    POLY_BUILDER_TIMESTAMP: timestamp,
    POLY_BUILDER_API_KEY: BUILDER_CREDENTIALS.key,
    POLY_BUILDER_PASSPHRASE: BUILDER_CREDENTIALS.passphrase,
  };
}
```

**你的客户端** 指向你的签名服务器：

Client (TypeScript)

Client (Python)

复制

询问AI

```
import { RelayClient } from "@polymarket/builder-relayer-client";
import { BuilderConfig } from "@polymarket/builder-signing-sdk";

const builderConfig = new BuilderConfig({
  remoteBuilderConfig: {
    url: "https://your-server.com/sign",
  },
});

const client = new RelayClient(
  "https://relayer-v2.polymarket.com/",
  137,
  wallet,
  builderConfig,
);
```

永远不要在客户端代码中暴露 Builder API 凭证。使用环境变量或密钥管理器。

## [​](https://docs.polymarket.com/cn/trading/gasless\#%E9%92%B1%E5%8C%85%E7%B1%BB%E5%9E%8B)  钱包类型

初始化客户端时选择钱包类型：

| 类型 | 部署方式 | 最适用于 |
| --- | --- | --- |
| **Safe** | 在首次交易前调用 `deploy()` | 大多数 builder 集成 |
| **Proxy** | 首次交易时自动部署 | Magic Link 用户 |

Safe Wallet (TypeScript)

Safe Wallet (Python)

Proxy Wallet (TypeScript)

Proxy Wallet (Python)

复制

询问AI

```
import { RelayClient, RelayerTxType } from "@polymarket/builder-relayer-client";

const client = new RelayClient(
  "https://relayer-v2.polymarket.com/",
  137,
  wallet,
  builderConfig,
  RelayerTxType.SAFE,
);

// Deploy before first transaction
const response = await client.deploy();
const result = await response.wait();
console.log("Safe Address:", result?.proxyAddress);
```

## [​](https://docs.polymarket.com/cn/trading/gasless\#%E6%89%A7%E8%A1%8C%E4%BA%A4%E6%98%93)  执行交易

使用 `execute` 方法通过 relayer 发送交易：

复制

询问AI

```
interface Transaction {
  to: string; // Target contract address
  data: string; // Encoded function call
  value: string; // POL to send (usually "0")
}

const response = await client.execute(transactions, "Description");
const result = await response.wait();
```

### [​](https://docs.polymarket.com/cn/trading/gasless\#%E4%BB%A3%E5%B8%81%E6%8E%88%E6%9D%83)  代币授权

授权合约使用代币：

TypeScript

Python

复制

询问AI

```
import { encodeFunctionData, maxUint256 } from "viem";

const USDC = "0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174";
const CTF = "0x4D97DCd97eC945f40cF65F87097ACe5EA0476045";

const approveTx = {
  to: USDC,
  data: encodeFunctionData({
    abi: [\
      {\
        name: "approve",\
        type: "function",\
        inputs: [\
          { name: "spender", type: "address" },\
          { name: "amount", type: "uint256" },\
        ],\
        outputs: [{ type: "bool" }],\
      },\
    ],
    functionName: "approve",
    args: [CTF, maxUint256],
  }),
  value: "0",
};

const response = await client.execute([approveTx], "Approve USDC.e for CTF");
await response.wait();
```

### [​](https://docs.polymarket.com/cn/trading/gasless\#%E5%85%91%E6%8D%A2%E4%BB%93%E4%BD%8D)  兑换仓位

市场判定后，将获胜代币兑换为 USDC.e：

TypeScript

Python

复制

询问AI

```
import { encodeFunctionData } from "viem";

const redeemTx = {
  to: CTF_ADDRESS,
  data: encodeFunctionData({
    abi: [\
      {\
        name: "redeemPositions",\
        type: "function",\
        inputs: [\
          { name: "collateralToken", type: "address" },\
          { name: "parentCollectionId", type: "bytes32" },\
          { name: "conditionId", type: "bytes32" },\
          { name: "indexSets", type: "uint256[]" },\
        ],\
        outputs: [],\
      },\
    ],
    functionName: "redeemPositions",
    args: [collateralToken, parentCollectionId, conditionId, indexSets],
  }),
  value: "0",
};

const response = await client.execute([redeemTx], "Redeem positions");
await response.wait();
```

### [​](https://docs.polymarket.com/cn/trading/gasless\#%E6%89%B9%E9%87%8F%E4%BA%A4%E6%98%93)  批量交易

在单次调用中原子性地执行多个操作：

TypeScript

Python

复制

询问AI

```
const approveTx = {
  to: USDC,
  data: encodeFunctionData({
    abi: erc20Abi,
    functionName: "approve",
    args: [CTF, maxUint256],
  }),
  value: "0",
};

const transferTx = {
  to: USDC,
  data: encodeFunctionData({
    abi: erc20Abi,
    functionName: "transfer",
    args: [recipientAddress, parseUnits("50", 6)],
  }),
  value: "0",
};

// Both execute atomically
const response = await client.execute(
  [approveTx, transferTx],
  "Approve and transfer",
);
await response.wait();
```

批量处理可以减少延迟，并确保所有交易要么全部成功，要么全部失败。

## [​](https://docs.polymarket.com/cn/trading/gasless\#%E4%BA%A4%E6%98%93%E7%8A%B6%E6%80%81)  交易状态

通过这些状态跟踪交易进度：

| 状态 | 终态 | 说明 |
| --- | --- | --- |
| `STATE_NEW` | 否 | relayer 已收到交易 |
| `STATE_EXECUTED` | 否 | 已提交到链上 |
| `STATE_MINED` | 否 | 已打包进区块 |
| `STATE_CONFIRMED` | 是 | 成功确认 |
| `STATE_FAILED` | 是 | 永久失败 |
| `STATE_INVALID` | 是 | 被拒绝为无效 |

## [​](https://docs.polymarket.com/cn/trading/gasless\#%E5%90%88%E7%BA%A6%E5%9C%B0%E5%9D%80)  合约地址

所有 Polymarket 智能合约地址详见 [合约地址](https://docs.polymarket.com/resources/contract-addresses)。

## [​](https://docs.polymarket.com/cn/trading/gasless\#%E8%B5%84%E6%BA%90)  资源

- [Builder Relayer Client (TypeScript)](https://github.com/Polymarket/builder-relayer-client)
- [Builder Relayer Client (Python)](https://github.com/Polymarket/py-builder-relayer-client)
- [Builder Signing SDK (TypeScript)](https://github.com/Polymarket/builder-signing-sdk)
- [Builder Signing SDK (Python)](https://github.com/Polymarket/py-builder-signing-sdk)

## [​](https://docs.polymarket.com/cn/trading/gasless\#%E4%B8%8B%E4%B8%80%E6%AD%A5)  下一步

[**Negative Risk Markets** \\
\\
了解多结果事件的资本高效交易。](https://docs.polymarket.com/advanced/neg-risk)

[**Positions & Tokens** \\
\\
理解拆分、合并和兑换等代币操作。](https://docs.polymarket.com/concepts/positions-tokens)

此页面对您有帮助吗？

是否

[费用\\
\\
上一页](https://docs.polymarket.com/cn/trading/fees) [Negative Risk 市场\\
\\
下一页](https://docs.polymarket.com/cn/advanced/neg-risk)

Ctrl+I

助手

AI生成的回答可能包含错误。