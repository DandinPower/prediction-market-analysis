---
url: "https://docs.polymarket.com/cn/concepts/order-lifecycle"
title: "订单生命周期 - Polymarket Documentation"
---

[跳转到主要内容](https://docs.polymarket.com/cn/concepts/order-lifecycle#content-area)

[Polymarket Documentation home page![light logo](https://mintcdn.com/polymarket-292d1b1b/ZibMe6Tli_amZald/logo/light.svg?fit=max&auto=format&n=ZibMe6Tli_amZald&q=85&s=9f9bd559f02181495794661ef6426c0f)![dark logo](https://mintcdn.com/polymarket-292d1b1b/ZibMe6Tli_amZald/logo/dark.svg?fit=max&auto=format&n=ZibMe6Tli_amZald&q=85&s=13abc6754579a3475368ea99d0f5a241)](https://docs.polymarket.com/cn)

![CN](https://d3gk2c5xim1je2.cloudfront.net/flags/CN.svg)

简体中文

搜索...

Ctrl K询问AI

搜索...

Navigation

核心概念

订单生命周期

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

- [订单运作方式](https://docs.polymarket.com/cn/concepts/order-lifecycle#%E8%AE%A2%E5%8D%95%E8%BF%90%E4%BD%9C%E6%96%B9%E5%BC%8F)
- [订单类型](https://docs.polymarket.com/cn/concepts/order-lifecycle#%E8%AE%A2%E5%8D%95%E7%B1%BB%E5%9E%8B)
- [Post-Only 订单](https://docs.polymarket.com/cn/concepts/order-lifecycle#post-only-%E8%AE%A2%E5%8D%95)
- [订单状态](https://docs.polymarket.com/cn/concepts/order-lifecycle#%E8%AE%A2%E5%8D%95%E7%8A%B6%E6%80%81)
- [交易状态](https://docs.polymarket.com/cn/concepts/order-lifecycle#%E4%BA%A4%E6%98%93%E7%8A%B6%E6%80%81)
- [Maker 与 Taker](https://docs.polymarket.com/cn/concepts/order-lifecycle#maker-%E4%B8%8E-taker)
- [取消订单](https://docs.polymarket.com/cn/concepts/order-lifecycle#%E5%8F%96%E6%B6%88%E8%AE%A2%E5%8D%95)
- [下单前提条件](https://docs.polymarket.com/cn/concepts/order-lifecycle#%E4%B8%8B%E5%8D%95%E5%89%8D%E6%8F%90%E6%9D%A1%E4%BB%B6)
- [下一步](https://docs.polymarket.com/cn/concepts/order-lifecycle#%E4%B8%8B%E4%B8%80%E6%AD%A5)

Polymarket 上的每笔交易都遵循一个特定的生命周期。订单在链下创建，由运营方撮合，最终通过智能合约在链上结算。这种混合架构兼具中心化撮合的速度和区块链结算的安全性。

![](https://mintcdn.com/polymarket-292d1b1b/FOMte3ewbG-LVy3k/images/core-concepts/order-lifecycle.png?fit=max&auto=format&n=FOMte3ewbG-LVy3k&q=85&s=4db07008193421bfe359afe44b5f604e)![](https://mintcdn.com/polymarket-292d1b1b/FOMte3ewbG-LVy3k/images/dark/core-concepts/order-lifecycle.png?fit=max&auto=format&n=FOMte3ewbG-LVy3k&q=85&s=5a0f3eba2f20c44471bae05c0670de4a)

## [​](https://docs.polymarket.com/cn/concepts/order-lifecycle\#%E8%AE%A2%E5%8D%95%E8%BF%90%E4%BD%9C%E6%96%B9%E5%BC%8F)  订单运作方式

Polymarket 上所有订单都是 **限价单**。限价单指定你愿意支付（或接受）的价格和交易数量。

“市价单”本质上是一种价格设定为可立即与最优挂单成交的限价单。

订单是 **EIP712 签名消息**。下单时，你用私钥签署一个结构化消息。这个签名授权 Exchange 合约代你执行交易——而无需接管你的资金。

## [​](https://docs.polymarket.com/cn/concepts/order-lifecycle\#%E8%AE%A2%E5%8D%95%E7%B1%BB%E5%9E%8B)  订单类型

| 类型 | 行为 | 适用场景 |
| --- | --- | --- |
| **GTC** | Good Till Cancelled — 挂单直到成交或被取消 | 标准限价单 |
| **GTD** | Good Till Date — 到指定时间自动过期 | 有时效的订单 |
| **FOK** | Fill Or Kill — 全部成交或立即取消 | 要求全额成交 |
| **FAK** | Fill And Kill — 成交可成交的部分，取消剩余 | 接受部分成交 |

### [​](https://docs.polymarket.com/cn/concepts/order-lifecycle\#post-only-%E8%AE%A2%E5%8D%95)  Post-Only 订单

Post-Only 订单只会作为挂单存在。如果 Post-Only 订单会立即成交（穿越价差），则会被拒绝而非执行。这保证你始终是 maker，而非 taker。

1

[Navigate to header](https://docs.polymarket.com/cn/concepts/order-lifecycle#)

创建与签名

你的客户端创建一个包含以下内容的订单对象：

- Token ID（你要交易的结果）
- 方向（买入或卖出）
- 价格和数量
- 过期时间
- Nonce（防重放保护）

你用私钥对订单进行签名，生成 EIP712 签名。

2

[Navigate to header](https://docs.polymarket.com/cn/concepts/order-lifecycle#)

提交至 CLOB

签名后的订单被提交到中央限价订单簿（CLOB）运营方。运营方会验证：

- 签名有效性
- 余额是否充足
- 是否设置了必要的授权（allowance）
- 价格是否满足最小价格单位要求

3

[Navigate to header](https://docs.polymarket.com/cn/concepts/order-lifecycle#)

撮合或挂单

**如果订单可成交**（你的买价 ≥ 最低卖价，或你的卖价 ≤ 最高买价），则立即与挂单撮合成交。**如果订单不可立即成交**，则挂在订单簿上等待对手方。订单将保持挂单状态直到：

- 其他订单与之匹配
- 你取消订单
- 订单过期（仅限 GTD 订单）

4

[Navigate to header](https://docs.polymarket.com/cn/concepts/order-lifecycle#)

结算

订单撮合后，运营方将交易提交到区块链。Exchange 合约会：

- 验证双方签名
- 将代币从卖方转给买方
- 将 USDC.e 从买方转给卖方

结算是 **原子性** 的——要么整笔交易成功，要么什么都不发生。

5

[Navigate to header](https://docs.polymarket.com/cn/concepts/order-lifecycle#)

确认

交易在 Polygon 上达成最终性。你的代币余额更新，交易记录出现在你的历史中。

## [​](https://docs.polymarket.com/cn/concepts/order-lifecycle\#%E8%AE%A2%E5%8D%95%E7%8A%B6%E6%80%81)  订单状态

下单后，订单会进入以下状态之一：

| 状态 | 说明 |
| --- | --- |
| `live` | 订单挂在订单簿上 |
| `matched` | 订单立即成交 |
| `delayed` | 可成交订单进入 3 秒撮合延迟（体育市场） |
| `unmatched` | 可成交订单在延迟期结束后未成交，被放入订单簿 |

## [​](https://docs.polymarket.com/cn/concepts/order-lifecycle\#%E4%BA%A4%E6%98%93%E7%8A%B6%E6%80%81)  交易状态

撮合后，交易经历以下状态：

| 状态 | 是否终态 | 说明 |
| --- | --- | --- |
| `MATCHED` | 否 | 已撮合，发送至执行器进行链上提交 |
| `MINED` | 否 | 交易已被区块链打包 |
| `CONFIRMED` | 是 | 交易达成最终性，执行成功 |
| `RETRYING` | 否 | 交易失败，正在重试 |
| `FAILED` | 是 | 交易永久失败 |

## [​](https://docs.polymarket.com/cn/concepts/order-lifecycle\#maker-%E4%B8%8E-taker)  Maker 与 Taker

| 角色 | 说明 | 触发条件 |
| --- | --- | --- |
| **Maker** | 为订单簿提供流动性 | 你的订单挂单后被其他订单成交 |
| **Taker** | 从订单簿获取流动性 | 你的订单立即与挂单成交 |

价格改善始终有利于 taker。如果你挂买单出价 `$0.55`，与挂卖单价格 `$0.52` 成交，你实际支付 `$0.52`。

## [​](https://docs.polymarket.com/cn/concepts/order-lifecycle\#%E5%8F%96%E6%B6%88%E8%AE%A2%E5%8D%95)  取消订单

你可以在订单被撮合之前随时取消：

- **通过 API** — 通过 CLOB API 取消（即时生效）
- **链上取消** — 直接在 Exchange 合约上取消（API 不可用时的备选方案）

已部分成交的部分无法取消——只能取消未成交的部分。

## [​](https://docs.polymarket.com/cn/concepts/order-lifecycle\#%E4%B8%8B%E5%8D%95%E5%89%8D%E6%8F%90%E6%9D%A1%E4%BB%B6)  下单前提条件

下单前请确保满足以下条件：

| 要求 | 说明 |
| --- | --- |
| **余额** | 足够的 USDC.e（买入时）或代币（卖出时） |
| **授权** | 已授权 Exchange 合约使用你的资产 |
| **API 凭证** | 认证接口所需的有效 API 密钥 |

订单数量受你的可用余额限制，需扣除现有挂单占用的金额。maxOrderSize=balance−∑(openOrderSize−filledAmount)\\text{maxOrderSize} = \\text{balance} - \\sum(\\text{openOrderSize} - \\text{filledAmount})maxOrderSize=balance−∑(openOrderSize−filledAmount)

## [​](https://docs.polymarket.com/cn/concepts/order-lifecycle\#%E4%B8%8B%E4%B8%80%E6%AD%A5)  下一步

[**判定** \\
\\
了解市场如何判定以及获胜代币如何兑换。](https://docs.polymarket.com/concepts/resolution)

[**交易指南** \\
\\
按照分步指南开始下单交易。](https://docs.polymarket.com/trading/overview)

此页面对您有帮助吗？

是否

[持仓与代币\\
\\
上一页](https://docs.polymarket.com/cn/concepts/positions-tokens) [判定\\
\\
下一页](https://docs.polymarket.com/cn/concepts/resolution)

Ctrl+I

助手

AI生成的回答可能包含错误。

![](https://mintcdn.com/polymarket-292d1b1b/FOMte3ewbG-LVy3k/images/core-concepts/order-lifecycle.png?w=840&fit=max&auto=format&n=FOMte3ewbG-LVy3k&q=85&s=2e31c345d92dcce72a824361c1522ab5)

![](https://mintcdn.com/polymarket-292d1b1b/FOMte3ewbG-LVy3k/images/dark/core-concepts/order-lifecycle.png?w=840&fit=max&auto=format&n=FOMte3ewbG-LVy3k&q=85&s=9e81f0b099ce605683d7c0fcca2d2006)