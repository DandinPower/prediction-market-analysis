---
url: "https://docs.polymarket.com/cn/market-makers/inventory"
title: "库存管理 - Polymarket Documentation"
---

[跳转到主要内容](https://docs.polymarket.com/cn/market-makers/inventory#content-area)

[Polymarket Documentation home page![light logo](https://mintcdn.com/polymarket-292d1b1b/ZibMe6Tli_amZald/logo/light.svg?fit=max&auto=format&n=ZibMe6Tli_amZald&q=85&s=9f9bd559f02181495794661ef6426c0f)![dark logo](https://mintcdn.com/polymarket-292d1b1b/ZibMe6Tli_amZald/logo/dark.svg?fit=max&auto=format&n=ZibMe6Tli_amZald&q=85&s=13abc6754579a3475368ea99d0f5a241)](https://docs.polymarket.com/cn)

![CN](https://d3gk2c5xim1je2.cloudfront.net/flags/CN.svg)

简体中文

搜索...

Ctrl K询问AI

搜索...

Navigation

操作

库存管理

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

  - [交易](https://docs.polymarket.com/cn/market-makers/trading)
  - [库存管理](https://docs.polymarket.com/cn/market-makers/inventory)

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

- [将 USDC.e 拆分为代币](https://docs.polymarket.com/cn/market-makers/inventory#%E5%B0%86-usdc-e-%E6%8B%86%E5%88%86%E4%B8%BA%E4%BB%A3%E5%B8%81)
- [将代币合并为 USDC.e](https://docs.polymarket.com/cn/market-makers/inventory#%E5%B0%86%E4%BB%A3%E5%B8%81%E5%90%88%E5%B9%B6%E4%B8%BA-usdc-e)
- [判定后兑换](https://docs.polymarket.com/cn/market-makers/inventory#%E5%88%A4%E5%AE%9A%E5%90%8E%E5%85%91%E6%8D%A2)
- [检查判定状态](https://docs.polymarket.com/cn/market-makers/inventory#%E6%A3%80%E6%9F%A5%E5%88%A4%E5%AE%9A%E7%8A%B6%E6%80%81)
- [兑换获胜代币](https://docs.polymarket.com/cn/market-makers/inventory#%E5%85%91%E6%8D%A2%E8%8E%B7%E8%83%9C%E4%BB%A3%E5%B8%81)
- [Negative Risk 市场](https://docs.polymarket.com/cn/market-makers/inventory#negative-risk-%E5%B8%82%E5%9C%BA)
- [库存策略](https://docs.polymarket.com/cn/market-makers/inventory#%E5%BA%93%E5%AD%98%E7%AD%96%E7%95%A5)
- [报价前](https://docs.polymarket.com/cn/market-makers/inventory#%E6%8A%A5%E4%BB%B7%E5%89%8D)
- [交易期间](https://docs.polymarket.com/cn/market-makers/inventory#%E4%BA%A4%E6%98%93%E6%9C%9F%E9%97%B4)
- [判定后](https://docs.polymarket.com/cn/market-makers/inventory#%E5%88%A4%E5%AE%9A%E5%90%8E)
- [批量操作](https://docs.polymarket.com/cn/market-makers/inventory#%E6%89%B9%E9%87%8F%E6%93%8D%E4%BD%9C)
- [下一步](https://docs.polymarket.com/cn/market-makers/inventory#%E4%B8%8B%E4%B8%80%E6%AD%A5)

做市商需要双方的结果代币来报价市场。三个核心库存操作是将 USDC.e **拆分** 为 YES/NO 代币对、将代币对 **合并** 回 USDC.e,以及在判定后 **兑换** 获胜代币——所有操作都通过 Relayer Client 免 gas 执行。

有关条件代币框架工作原理的完整说明,请参阅 [CTF 概述](https://docs.polymarket.com/trading/ctf/overview)。本页重点介绍使用 Relayer Client 的做市商工作流程。

* * *

## [​](https://docs.polymarket.com/cn/market-makers/inventory\#%E5%B0%86-usdc-e-%E6%8B%86%E5%88%86%E4%B8%BA%E4%BB%A3%E5%B8%81)  将 USDC.e 拆分为代币

拆分将 USDC.e 转换为等量的 YES 和 NO 代币——创建你报价市场双方所需的库存。

TypeScript

Python

复制

询问AI

```
import { ethers } from "ethers";
import { Interface } from "ethers/lib/utils";
import { RelayClient, Transaction } from "@polymarket/builder-relayer-client";

const CTF_ADDRESS = "0x4D97DCd97eC945f40cF65F87097ACe5EA0476045";
const USDCe_ADDRESS = "0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174";

const ctfInterface = new Interface([\
  "function splitPosition(address collateralToken, bytes32 parentCollectionId, bytes32 conditionId, uint[] partition, uint amount)",\
]);

// Split $1000 USDCe into YES/NO tokens
const amount = ethers.utils.parseUnits("1000", 6); // USDCe has 6 decimals

const splitTx: Transaction = {
  to: CTF_ADDRESS,
  data: ctfInterface.encodeFunctionData("splitPosition", [\
    USDCe_ADDRESS, // collateralToken\
    ethers.constants.HashZero, // parentCollectionId (always zero for Polymarket)\
    conditionId, // conditionId from market\
    [1, 2], // partition: [YES, NO]\
    amount,\
  ]),
  value: "0",
};

const response = await client.execute([splitTx], "Split USDCe into tokens");
const result = await response.wait();
console.log("Split completed:", result?.transactionHash);
```

拆分 1000 USDC.e 后,你会收到 1000 个 YES 代币和 1000 个 NO 代币。你的 USDC.e 余额减少 1000。

* * *

## [​](https://docs.polymarket.com/cn/market-makers/inventory\#%E5%B0%86%E4%BB%A3%E5%B8%81%E5%90%88%E5%B9%B6%E4%B8%BA-usdc-e)  将代币合并为 USDC.e

合并将等量的 YES 和 NO 代币转换回 USDC.e——适用于减少敞口、退出市场或释放资金。

TypeScript

Python

复制

询问AI

```
const ctfInterface = new Interface([\
  "function mergePositions(address collateralToken, bytes32 parentCollectionId, bytes32 conditionId, uint[] partition, uint amount)",\
]);

// Merge 500 YES + 500 NO back to 500 USDCe
const amount = ethers.utils.parseUnits("500", 6);

const mergeTx: Transaction = {
  to: CTF_ADDRESS,
  data: ctfInterface.encodeFunctionData("mergePositions", [\
    USDCe_ADDRESS,\
    ethers.constants.HashZero,\
    conditionId,\
    [1, 2],\
    amount,\
  ]),
  value: "0",
};

const response = await client.execute([mergeTx], "Merge tokens to USDCe");
await response.wait();
```

合并各 500 个后,你的 YES 和 NO 余额各减少 500,USDC.e 余额增加 500。

* * *

## [​](https://docs.polymarket.com/cn/market-makers/inventory\#%E5%88%A4%E5%AE%9A%E5%90%8E%E5%85%91%E6%8D%A2)  判定后兑换

市场判定后,将获胜代币兑换为 USDC.e。每个获胜代币价值 1——失败代币兑换为1——失败代币兑换为 1——失败代币兑换为0。

### [​](https://docs.polymarket.com/cn/market-makers/inventory\#%E6%A3%80%E6%9F%A5%E5%88%A4%E5%AE%9A%E7%8A%B6%E6%80%81)  检查判定状态

TypeScript

Python

复制

询问AI

```
const market = await clobClient.getMarket(conditionId);
if (market.closed) {
  const winningToken = market.tokens.find((t) => t.winner);
  console.log("Winning outcome:", winningToken?.outcome);
}
```

### [​](https://docs.polymarket.com/cn/market-makers/inventory\#%E5%85%91%E6%8D%A2%E8%8E%B7%E8%83%9C%E4%BB%A3%E5%B8%81)  兑换获胜代币

TypeScript

Python

复制

询问AI

```
const ctfInterface = new Interface([\
  "function redeemPositions(address collateralToken, bytes32 parentCollectionId, bytes32 conditionId, uint[] indexSets)",\
]);

const redeemTx: Transaction = {
  to: CTF_ADDRESS,
  data: ctfInterface.encodeFunctionData("redeemPositions", [\
    USDCe_ADDRESS,\
    ethers.constants.HashZero,\
    conditionId,\
    [1, 2], // Redeem both YES and NO (only winners pay out)\
  ]),
  value: "0",
};

const response = await client.execute([redeemTx], "Redeem winning tokens");
await response.wait();
```

* * *

## [​](https://docs.polymarket.com/cn/market-makers/inventory\#negative-risk-%E5%B8%82%E5%9C%BA)  Negative Risk 市场

多结果市场使用 Neg Risk CTF Exchange。拆分和合并的工作方式相同,但使用不同的合约地址:

复制

询问AI

```
const NEG_RISK_ADAPTER = "0xd91E80cF2E7be2e162c6513ceD06f1dD0dA35296";
const NEG_RISK_CTF_EXCHANGE = "0xC5d563A36AE78145C45a50134d48A1215220f80a";
```

有关多结果代币机制如何不同的详情,请参阅 [Negative Risk 市场](https://docs.polymarket.com/advanced/neg-risk)。

* * *

## [​](https://docs.polymarket.com/cn/market-makers/inventory\#%E5%BA%93%E5%AD%98%E7%AD%96%E7%95%A5)  库存策略

### [​](https://docs.polymarket.com/cn/market-makers/inventory\#%E6%8A%A5%E4%BB%B7%E5%89%8D)  报价前

1. 通过 [Gamma API](https://docs.polymarket.com/market-data/fetching-markets) 检查市场元数据
2. 拆分足够的 USDC.e 以覆盖你的预期报价规模
3. 如果尚未完成,设置代币授权(参见 [入门](https://docs.polymarket.com/market-makers/getting-started))

### [​](https://docs.polymarket.com/cn/market-makers/inventory\#%E4%BA%A4%E6%98%93%E6%9C%9F%E9%97%B4)  交易期间

- 当库存在某一侧失衡时 **倾斜报价**
- **合并多余代币** 以释放资金用于其他市场
- 当任一侧库存不足时 **拆分更多**

### [​](https://docs.polymarket.com/cn/market-makers/inventory\#%E5%88%A4%E5%AE%9A%E5%90%8E)  判定后

1. 取消市场中的所有未成交订单
2. 等待判定完成
3. 兑换获胜代币
4. 合并任何剩余的 YES/NO 代币对

* * *

## [​](https://docs.polymarket.com/cn/market-makers/inventory\#%E6%89%B9%E9%87%8F%E6%93%8D%E4%BD%9C)  批量操作

在单个中继器调用中执行多个库存操作以提高效率:

复制

询问AI

```
const transactions: Transaction[] = [\
  // Split on Market A\
  {\
    to: CTF_ADDRESS,\
    data: ctfInterface.encodeFunctionData("splitPosition", [\
      USDCe_ADDRESS,\
      ethers.constants.HashZero,\
      conditionIdA,\
      [1, 2],\
      ethers.utils.parseUnits("1000", 6),\
    ]),\
    value: "0",\
  },\
  // Split on Market B\
  {\
    to: CTF_ADDRESS,\
    data: ctfInterface.encodeFunctionData("splitPosition", [\
      USDCe_ADDRESS,\
      ethers.constants.HashZero,\
      conditionIdB,\
      [1, 2],\
      ethers.utils.parseUnits("1000", 6),\
    ]),\
    value: "0",\
  },\
];

const response = await client.execute(transactions, "Batch inventory setup");
await response.wait();
```

* * *

## [​](https://docs.polymarket.com/cn/market-makers/inventory\#%E4%B8%8B%E4%B8%80%E6%AD%A5)  下一步

[**CTF 概述** \\
\\
条件代币框架的底层工作原理](https://docs.polymarket.com/trading/ctf/overview)

[**拆分代币** \\
\\
详细的拆分函数参数和前提条件](https://docs.polymarket.com/trading/ctf/split)

[**合并代币** \\
\\
详细的合并函数参数](https://docs.polymarket.com/trading/ctf/merge)

[**免 gas 交易** \\
\\
Relayer Client 设置和配置](https://docs.polymarket.com/trading/gasless)

此页面对您有帮助吗？

是否

[交易\\
\\
上一页](https://docs.polymarket.com/cn/market-makers/trading) [构建者计划\\
\\
下一页](https://docs.polymarket.com/cn/builders/overview)

Ctrl+I

助手

AI生成的回答可能包含错误。