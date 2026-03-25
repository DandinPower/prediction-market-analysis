---
url: "https://docs.polymarket.com/cn/concepts/resolution"
title: "判定 - Polymarket Documentation"
---

[跳转到主要内容](https://docs.polymarket.com/cn/concepts/resolution#content-area)

[Polymarket Documentation home page![light logo](https://mintcdn.com/polymarket-292d1b1b/ZibMe6Tli_amZald/logo/light.svg?fit=max&auto=format&n=ZibMe6Tli_amZald&q=85&s=9f9bd559f02181495794661ef6426c0f)![dark logo](https://mintcdn.com/polymarket-292d1b1b/ZibMe6Tli_amZald/logo/dark.svg?fit=max&auto=format&n=ZibMe6Tli_amZald&q=85&s=13abc6754579a3475368ea99d0f5a241)](https://docs.polymarket.com/cn)

![CN](https://d3gk2c5xim1je2.cloudfront.net/flags/CN.svg)

简体中文

搜索...

Ctrl K询问AI

搜索...

Navigation

核心概念

判定

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

- [判定规则](https://docs.polymarket.com/cn/concepts/resolution#%E5%88%A4%E5%AE%9A%E8%A7%84%E5%88%99)
- [判定之后](https://docs.polymarket.com/cn/concepts/resolution#%E5%88%A4%E5%AE%9A%E4%B9%8B%E5%90%8E)
- [兑换代币](https://docs.polymarket.com/cn/concepts/resolution#%E5%85%91%E6%8D%A2%E4%BB%A3%E5%B8%81)
- [补充说明](https://docs.polymarket.com/cn/concepts/resolution#%E8%A1%A5%E5%85%85%E8%AF%B4%E6%98%8E)
- [判定时间线](https://docs.polymarket.com/cn/concepts/resolution#%E5%88%A4%E5%AE%9A%E6%97%B6%E9%97%B4%E7%BA%BF)
- [合约地址](https://docs.polymarket.com/cn/concepts/resolution#%E5%90%88%E7%BA%A6%E5%9C%B0%E5%9D%80)
- [相关资源](https://docs.polymarket.com/cn/concepts/resolution#%E7%9B%B8%E5%85%B3%E8%B5%84%E6%BA%90)
- [下一步](https://docs.polymarket.com/cn/concepts/resolution#%E4%B8%8B%E4%B8%80%E6%AD%A5)

当事件的结果明确后，市场进入 **判定** 阶段。判定确定哪个结果获胜，获胜代币的持有者可以按每个 $1 进行兑换。失败的代币变得一文不值。Polymarket 使用 **UMA Optimistic Oracle** 进行去中心化、无许可的判定。任何人都可以提议一个结果，任何人也可以在认为结果有误时发起争议。

![](https://mintcdn.com/polymarket-292d1b1b/FOMte3ewbG-LVy3k/images/core-concepts/resolution-lifecycle.png?fit=max&auto=format&n=FOMte3ewbG-LVy3k&q=85&s=6726569af3efd6f4fda54528c8eb0d0a)![](https://mintcdn.com/polymarket-292d1b1b/FOMte3ewbG-LVy3k/images/dark/core-concepts/resolution-lifecycle.png?fit=max&auto=format&n=FOMte3ewbG-LVy3k&q=85&s=36e91c655f7f50b18dea3a23b44f8c23)

## [​](https://docs.polymarket.com/cn/concepts/resolution\#%E5%88%A4%E5%AE%9A%E8%A7%84%E5%88%99)  判定规则

每个市场都有预设的判定规则，规定了以下内容：

- **判定来源** — 结果的认定依据（例如，官方公告、特定网站）
- **截止日期** — 市场可以进行判定的时间
- **边界情况** — 模糊情况的处理方式

交易前请务必阅读判定规则。市场标题描述了问题，但 **规则** 才决定如何判定。

1

[Navigate to header](https://docs.polymarket.com/cn/concepts/resolution#)

提议

任何人都可以通过以下步骤提议判定结果：

1. 选择获胜的结果
2. 缴纳保证金（通常为 $750 USDC.e）
3. 向 UMA Oracle 提交提议

如果提议正确且无人争议，提议者可取回保证金并获得奖励。

如果提议结果不正确或过早提交，你将失去全部保证金。只有在你确信结果并了解流程的情况下才进行提议。

2

[Navigate to header](https://docs.polymarket.com/cn/concepts/resolution#)

质疑期

提议提交后，有一个 **2 小时的质疑期**，任何人都可以对结果发起争议。

- **如果无争议**：提议被接受，市场完成判定
- **如果有争议**：进入新一轮提议。如果第二次提议也被争议，判定将升级至 UMA 的 DVM（数据验证机制）进行代币持有者投票

判定有三种可能的流程：

1. **无争议** — 提议后直接判定（最快，约 2 小时）
2. **一次争议** — 提议、质疑、二次提议、判定（第二次提议被接受）
3. **两次争议** — 提议、质疑、二次提议、二次质疑、通过 DVM 投票判定

3

[Navigate to header](https://docs.polymarket.com/cn/concepts/resolution#)

争议 \- 如被质疑

发起争议的步骤：

1. 缴纳反对保证金（与提议者金额相同，通常 $750）
2. 争议触发新一轮提议，若已在第二轮则触发辩论期

在 **24-48 小时的辩论期** 内，参与者可以在 UMA 的 Discord 频道（`#evidence-rationale` 和 `#voting-discussion`）提交证据。

4

[Navigate to header](https://docs.polymarket.com/cn/concepts/resolution#)

UMA 投票

辩论期结束后，UMA 代币持有者对正确结果进行投票。投票过程大约需要 48 小时。

| 结果 | 处理方式 | 保证金分配 |
| --- | --- | --- |
| **提议者胜出** | 接受原始提议 | 提议者取回保证金 \+ 争议方保证金的一半 |
| **争议方胜出** | 提议被否决，需要新的提议 | 争议方取回保证金 \+ 提议者保证金的一半 |
| **为时过早** | 事件尚未结束 | 争议方取回保证金 \+ 提议者保证金的一半 |
| **未知/50-50** | 两个结果均不适用（罕见） | 市场按 50/50 判定——每个代币可兑换 $0.50；争议方取回保证金 + 提议者保证金的一半 |

## [​](https://docs.polymarket.com/cn/concepts/resolution\#%E5%88%A4%E5%AE%9A%E4%B9%8B%E5%90%8E)  判定之后

市场判定完成后：

- **交易停止** — 该市场的代币不再可买卖
- **获胜代币** 可按每个 $1.00 兑换
- **失败代币** 变得一文不值（$0.00）

### [​](https://docs.polymarket.com/cn/concepts/resolution\#%E5%85%91%E6%8D%A2%E4%BB%A3%E5%B8%81)  兑换代币

判定完成后，调用 CTF 合约的 `redeemPositions` 函数，将获胜代币兑换为 USDC.e。合约会销毁你的代币并返还相应的抵押品。

复制

询问AI

```
100 个获胜代币 → $100 USDC.e
```

## [​](https://docs.polymarket.com/cn/concepts/resolution\#%E8%A1%A5%E5%85%85%E8%AF%B4%E6%98%8E)  补充说明

在少数情况下，交易开始后出现未预见的情况，需要对规则进行补充说明。Polymarket 可能会发布\*\*“补充说明”\*\*更新，提议者和投票者在判定时应将其纳入考量。补充说明的特点：

- 不能改变问题的根本意图
- 通过公告板合约在链上发布
- UMA 投票者在处理争议时应参考这些说明

如果你认为需要补充说明，请在 [Polymarket\\
Discord](https://discord.com/invite/polymarket) 的 `#market-review` 频道提出请求。

## [​](https://docs.polymarket.com/cn/concepts/resolution\#%E5%88%A4%E5%AE%9A%E6%97%B6%E9%97%B4%E7%BA%BF)  判定时间线

| 阶段 | 时长 |
| --- | --- |
| 质疑期 | 2 小时 |
| 辩论期（如有争议） | 24-48 小时 |
| UMA 投票（如有争议） | 约 48 小时 |

**无争议判定**：提议后约 2 小时**有争议判定**：总计 4-6 天

## [​](https://docs.polymarket.com/cn/concepts/resolution\#%E5%90%88%E7%BA%A6%E5%9C%B0%E5%9D%80)  合约地址

| 合约 | 地址 | 网络 |
| --- | --- | --- |
| **UmaCtfAdapter v3.0** | `0x157Ce2d672854c848c9b79C49a8Cc6cc89176a49` | Polygon Mainnet |
| **UmaCtfAdapter v2.0** | `0x6A9D222616C90FcA5754cd1333cFD9b7fb6a4F74` | Polygon Mainnet |
| **UmaCtfAdapter v1.0** | `0xCB1822859cEF82Cd2Eb4E6276C7916e692995130` | Polygon Mainnet |

## [​](https://docs.polymarket.com/cn/concepts/resolution\#%E7%9B%B8%E5%85%B3%E8%B5%84%E6%BA%90)  相关资源

- [UMA Oracle 门户](https://oracle.uma.xyz/) — 查看并参与提议
- [UMA 文档](https://docs.uma.xyz/) — 了解 Optimistic Oracle 的更多信息
- [Polymarket Discord](https://discord.com/invite/polymarket) — 讨论判定结果和请求补充说明
- [UmaCtfAdapter 源代码](https://github.com/Polymarket/uma-ctf-adapter) — 智能合约源码
- [UmaCtfAdapter 审计报告](https://github.com/Polymarket/uma-ctf-adapter/blob/main/audit/Polymarket_UMA_Optimistic_Oracle_Adapter_Audit.pdf) — 安全审计报告

## [​](https://docs.polymarket.com/cn/concepts/resolution\#%E4%B8%8B%E4%B8%80%E6%AD%A5)  下一步

[**持仓与代币** \\
\\
了解判定后如何兑换获胜代币。](https://docs.polymarket.com/concepts/positions-tokens)

[**市场与事件** \\
\\
了解市场的组织结构。](https://docs.polymarket.com/concepts/markets-events)

此页面对您有帮助吗？

是否

[订单生命周期\\
\\
上一页](https://docs.polymarket.com/cn/concepts/order-lifecycle) [概览\\
\\
下一页](https://docs.polymarket.com/cn/market-data/overview)

Ctrl+I

助手

AI生成的回答可能包含错误。

![](https://mintcdn.com/polymarket-292d1b1b/FOMte3ewbG-LVy3k/images/core-concepts/resolution-lifecycle.png?w=840&fit=max&auto=format&n=FOMte3ewbG-LVy3k&q=85&s=24bff0e4be1cc3925c8022751d08331f)

![](https://mintcdn.com/polymarket-292d1b1b/FOMte3ewbG-LVy3k/images/dark/core-concepts/resolution-lifecycle.png?w=840&fit=max&auto=format&n=FOMte3ewbG-LVy3k&q=85&s=46354d72ab1341abb004e10cfff79ae6)