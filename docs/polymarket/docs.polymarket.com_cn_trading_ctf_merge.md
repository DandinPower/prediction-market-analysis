---
url: "https://docs.polymarket.com/cn/trading/ctf/merge"
title: "合并代币 - Polymarket Documentation"
---

[跳转到主要内容](https://docs.polymarket.com/cn/trading/ctf/merge#content-area)

[Polymarket Documentation home page![light logo](https://mintcdn.com/polymarket-292d1b1b/ZibMe6Tli_amZald/logo/light.svg?fit=max&auto=format&n=ZibMe6Tli_amZald&q=85&s=9f9bd559f02181495794661ef6426c0f)![dark logo](https://mintcdn.com/polymarket-292d1b1b/ZibMe6Tli_amZald/logo/dark.svg?fit=max&auto=format&n=ZibMe6Tli_amZald&q=85&s=13abc6754579a3475368ea99d0f5a241)](https://docs.polymarket.com/cn)

![CN](https://d3gk2c5xim1je2.cloudfront.net/flags/CN.svg)

简体中文

搜索...

Ctrl K询问AI

搜索...

Navigation

CTF 代币

合并代币

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

  - [Conditional Token Framework](https://docs.polymarket.com/cn/trading/ctf/overview)
  - [拆分代币](https://docs.polymarket.com/cn/trading/ctf/split)
  - [合并代币](https://docs.polymarket.com/cn/trading/ctf/merge)
  - [兑换代币](https://docs.polymarket.com/cn/trading/ctf/redeem)
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

- [前置要求](https://docs.polymarket.com/cn/trading/ctf/merge#%E5%89%8D%E7%BD%AE%E8%A6%81%E6%B1%82)
- [工作原理](https://docs.polymarket.com/cn/trading/ctf/merge#%E5%B7%A5%E4%BD%9C%E5%8E%9F%E7%90%86)
- [函数参数](https://docs.polymarket.com/cn/trading/ctf/merge#%E5%87%BD%E6%95%B0%E5%8F%82%E6%95%B0)
- [下一步](https://docs.polymarket.com/cn/trading/ctf/merge#%E4%B8%8B%E4%B8%80%E6%AD%A5)

**合并** 是拆分的逆操作——它将完整的结果代币集合转换回 USDC.e 抵押品。每合并 1 个 Yes 代币和 1 个 No 代币,你会收到 $1 USDC.e。该条件必须已通过 `prepareCondition` 在 CTF 合约上准备好。

复制

询问AI

```
100 Yes tokens + 100 No tokens → $100 USDC.e
```

## [​](https://docs.polymarket.com/cn/trading/ctf/merge\#%E5%89%8D%E7%BD%AE%E8%A6%81%E6%B1%82)  前置要求

在合并之前,你需要:

1. **相等数量** 的 Yes 和 No 代币
2. 市场的 **Condition ID**
3. 交易所需的 **足够 gas**

## [​](https://docs.polymarket.com/cn/trading/ctf/merge\#%E5%B7%A5%E4%BD%9C%E5%8E%9F%E7%90%86)  工作原理

1. 你调用 `mergePositions()`,传入金额和市场详情
2. 完整集合中每个仓位的一个单位被销毁,换取 1 个抵押品单位
3. CTF 合约将 USDC.e 释放回你的钱包

该操作是原子性的——如果你没有足够的两种代币,交易将回滚。

## [​](https://docs.polymarket.com/cn/trading/ctf/merge\#%E5%87%BD%E6%95%B0%E5%8F%82%E6%95%B0)  函数参数

[​](https://docs.polymarket.com/cn/trading/ctf/merge#param-collateral-token)

collateralToken

IERC20

USDC.e (Bridged USDC) 合约地址: `0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174`

[​](https://docs.polymarket.com/cn/trading/ctf/merge#param-parent-collection-id)

parentCollectionId

bytes32

对于 Polymarket 市场,始终为 `0x0000...0000`(32 个零字节)

[​](https://docs.polymarket.com/cn/trading/ctf/merge#param-condition-id)

conditionId

bytes32

市场的 condition ID,可从 Markets API 获取

[​](https://docs.polymarket.com/cn/trading/ctf/merge#param-partition)

partition

uint\[\]

索引集合数组:二元市场使用 `[1, 2]`

[​](https://docs.polymarket.com/cn/trading/ctf/merge#param-amount)

amount

uint256

要合并的完整集合数量。也是将收到的抵押品数量。

## [​](https://docs.polymarket.com/cn/trading/ctf/merge\#%E4%B8%8B%E4%B8%80%E6%AD%A5)  下一步

[**兑换代币** \\
\\
判定后将获胜代币兑换为 USDC.e](https://docs.polymarket.com/trading/ctf/redeem)

[**CTF 概述** \\
\\
了解更多关于 Conditional Token Framework 的信息](https://docs.polymarket.com/trading/ctf/overview)

此页面对您有帮助吗？

是否

[拆分代币\\
\\
上一页](https://docs.polymarket.com/cn/trading/ctf/split) [兑换代币\\
\\
下一页](https://docs.polymarket.com/cn/trading/ctf/redeem)

Ctrl+I

助手

AI生成的回答可能包含错误。