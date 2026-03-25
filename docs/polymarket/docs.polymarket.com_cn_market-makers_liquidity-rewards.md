---
url: "https://docs.polymarket.com/cn/market-makers/liquidity-rewards"
title: "流动性奖励 - Polymarket Documentation"
---

[跳转到主要内容](https://docs.polymarket.com/cn/market-makers/liquidity-rewards#content-area)

[Polymarket Documentation home page![light logo](https://mintcdn.com/polymarket-292d1b1b/ZibMe6Tli_amZald/logo/light.svg?fit=max&auto=format&n=ZibMe6Tli_amZald&q=85&s=9f9bd559f02181495794661ef6426c0f)![dark logo](https://mintcdn.com/polymarket-292d1b1b/ZibMe6Tli_amZald/logo/dark.svg?fit=max&auto=format&n=ZibMe6Tli_amZald&q=85&s=13abc6754579a3475368ea99d0f5a241)](https://docs.polymarket.com/cn)

![CN](https://d3gk2c5xim1je2.cloudfront.net/flags/CN.svg)

简体中文

搜索...

Ctrl K询问AI

搜索...

Navigation

做市商

流动性奖励

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

- [方法论](https://docs.polymarket.com/cn/market-makers/liquidity-rewards#%E6%96%B9%E6%B3%95%E8%AE%BA)
- [变量](https://docs.polymarket.com/cn/market-makers/liquidity-rewards#%E5%8F%98%E9%87%8F)
- [公式](https://docs.polymarket.com/cn/market-makers/liquidity-rewards#%E5%85%AC%E5%BC%8F)
- [1\. 订单评分函数](https://docs.polymarket.com/cn/market-makers/liquidity-rewards#1-%E8%AE%A2%E5%8D%95%E8%AF%84%E5%88%86%E5%87%BD%E6%95%B0)
- [2\. 第一市场边分数](https://docs.polymarket.com/cn/market-makers/liquidity-rewards#2-%E7%AC%AC%E4%B8%80%E5%B8%82%E5%9C%BA%E8%BE%B9%E5%88%86%E6%95%B0)
- [3\. 第二市场边分数](https://docs.polymarket.com/cn/market-makers/liquidity-rewards#3-%E7%AC%AC%E4%BA%8C%E5%B8%82%E5%9C%BA%E8%BE%B9%E5%88%86%E6%95%B0)
- [4\. 最小分数](https://docs.polymarket.com/cn/market-makers/liquidity-rewards#4-%E6%9C%80%E5%B0%8F%E5%88%86%E6%95%B0)
- [5\. 标准化分数](https://docs.polymarket.com/cn/market-makers/liquidity-rewards#5-%E6%A0%87%E5%87%86%E5%8C%96%E5%88%86%E6%95%B0)
- [6\. 时期分数](https://docs.polymarket.com/cn/market-makers/liquidity-rewards#6-%E6%97%B6%E6%9C%9F%E5%88%86%E6%95%B0)
- [7\. 最终分数](https://docs.polymarket.com/cn/market-makers/liquidity-rewards#7-%E6%9C%80%E7%BB%88%E5%88%86%E6%95%B0)
- [实例演示](https://docs.polymarket.com/cn/market-makers/liquidity-rewards#%E5%AE%9E%E4%BE%8B%E6%BC%94%E7%A4%BA)
- [步骤 2 - 第一边分数](https://docs.polymarket.com/cn/market-makers/liquidity-rewards#%E6%AD%A5%E9%AA%A4-2-%E7%AC%AC%E4%B8%80%E8%BE%B9%E5%88%86%E6%95%B0)
- [步骤 3 - 第二边分数](https://docs.polymarket.com/cn/market-makers/liquidity-rewards#%E6%AD%A5%E9%AA%A4-3-%E7%AC%AC%E4%BA%8C%E8%BE%B9%E5%88%86%E6%95%B0)
- [步骤 4-7](https://docs.polymarket.com/cn/market-makers/liquidity-rewards#%E6%AD%A5%E9%AA%A4-4-7)
- [下一步](https://docs.polymarket.com/cn/market-makers/liquidity-rewards#%E4%B8%8B%E4%B8%80%E6%AD%A5)

通过发布限价挂单，流动性提供者（maker）会自动获得参与 Polymarket 激励计划的资格。奖励每天在 UTC 午夜时分直接分发到 maker 地址。该计划旨在：

- 促进所有市场的流动性
- 鼓励在市场整个生命周期中提供流动性
- 激励在市场中间价附近被动、平衡地报价
- 鼓励交易活动
- 阻止明显的剥削行为

该计划深受 [dYdX 的流动性提供者奖励](https://www.dydx.foundation/blog/liquidity-provider-rewards) 启发。方法论本质上是 dYdX 方法的复制，并针对二元合约市场进行了调整——独立订单簿、无质押机制、修改的订单效用相对深度函数，以及按市场隔离的奖励金额。

* * *

## [​](https://docs.polymarket.com/cn/market-makers/liquidity-rewards\#%E6%96%B9%E6%B3%95%E8%AE%BA)  方法论

流动性提供者根据一个公式获得奖励，该公式奖励市场参与度，提升双边深度（单边订单仍然计分），以及相对于规模截止调整后中间价更紧的价差。每个市场配置一个最大价差和最小规模截止，在此范围内的订单才会被考虑。奖励的平均值由每个参与者在市场 m 中的 Qn 相对份额决定。

### [​](https://docs.polymarket.com/cn/market-makers/liquidity-rewards\#%E5%8F%98%E9%87%8F)  变量

| Variable | Description |
| --- | --- |
| S | 订单位置评分函数 |
| v | 与中间价的最大价差（以美分计） |
| s | 与规模截止调整后中间价的价差 |
| b | 游戏内乘数 |
| m | 市场 |
| m’ | 市场补充（即如果 m = YES，则为 NO） |
| n | 交易者索引 |
| u | 样本索引 |
| c | 缩放因子（目前所有市场均为 3.0） |
| Qne | 样本中第一个订单簿的总分 |
| Qno | 样本中第二个订单簿的总分 |
| Spread% | 市场 m 中订单 n 与中间价的距离（基点或相对值） |
| BidSize | 以份额计价的买单数量 |
| AskSize | 以份额计价的卖单数量 |

* * *

## [​](https://docs.polymarket.com/cn/market-makers/liquidity-rewards\#%E5%85%AC%E5%BC%8F)  公式

### [​](https://docs.polymarket.com/cn/market-makers/liquidity-rewards\#1-%E8%AE%A2%E5%8D%95%E8%AF%84%E5%88%86%E5%87%BD%E6%95%B0)  1\. 订单评分函数

基于调整后中间价和最小合格价差之间位置的订单二次评分规则：S(v,s)=(v−sv)2⋅bS(v,s)= (\\frac{v-s}{v})^2 \\cdot bS(v,s)=(vv−s​)2⋅b

### [​](https://docs.polymarket.com/cn/market-makers/liquidity-rewards\#2-%E7%AC%AC%E4%B8%80%E5%B8%82%E5%9C%BA%E8%BE%B9%E5%88%86%E6%95%B0)  2\. 第一市场边分数

Qone=S(v,Spreadm1)⋅BidSizem1+S(v,Spreadm2)⋅BidSizem2+…Q\_{one}= S(v,Spread\_{m\_1}) \\cdot BidSize\_{m\_1} + S(v,Spread\_{m\_2}) \\cdot BidSize\_{m\_2} + \\dots Qone​=S(v,Spreadm1​​)⋅BidSizem1​​+S(v,Spreadm2​​)⋅BidSizem2​​+…+S(v,Spreadm1′)⋅AskSizem1′+S(v,Spreadm2′)⋅AskSizem2′ \+ S(v, Spread\_{m^\\prime\_1}) \\cdot AskSize\_{m^\\prime\_1} + S(v, Spread\_{m^\\prime\_2}) \\cdot AskSize\_{m^\\prime\_2}+S(v,Spreadm1′​​)⋅AskSizem1′​​+S(v,Spreadm2′​​)⋅AskSizem2′​​

### [​](https://docs.polymarket.com/cn/market-makers/liquidity-rewards\#3-%E7%AC%AC%E4%BA%8C%E5%B8%82%E5%9C%BA%E8%BE%B9%E5%88%86%E6%95%B0)  3\. 第二市场边分数

Qtwo=S(v,Spreadm1)⋅AskSizem1+S(v,Spreadm2)⋅AskSizem2+…Q\_{two}= S(v,Spread\_{m\_1}) \\cdot AskSize\_{m\_1} + S(v,Spread\_{m\_2}) \\cdot AskSize\_{m\_2} + \\dots Qtwo​=S(v,Spreadm1​​)⋅AskSizem1​​+S(v,Spreadm2​​)⋅AskSizem2​​+…+S(v,Spreadm1′)⋅BidSizem1′+S(v,Spreadm2′)⋅BidSizem2′ \+ S(v, Spread\_{m^\\prime\_1}) \\cdot BidSize\_{m^\\prime\_1} + S(v, Spread\_{m^\\prime\_2}) \\cdot BidSize\_{m^\\prime\_2}+S(v,Spreadm1′​​)⋅BidSizem1′​​+S(v,Spreadm2′​​)⋅BidSizem2′​​

### [​](https://docs.polymarket.com/cn/market-makers/liquidity-rewards\#4-%E6%9C%80%E5%B0%8F%E5%88%86%E6%95%B0)  4\. 最小分数

通过取 Qne 和 Qno 的最小值来提升双边流动性，同时仍以降低的比率（除以 c）奖励单边流动性。**如果中间价在 \[0.10, 0.90\] 范围内** ——单边流动性可以计分：Qmin⁡=max⁡(min⁡(Qone,Qtwo),max⁡(Qone/c,Qtwo/c))Q\_{\\min} = \\max(\\min({Q\_{one}, Q\_{two}}), \\max(Q\_{one}/c, Q\_{two}/c))Qmin​=max(min(Qone​,Qtwo​),max(Qone​/c,Qtwo​/c))**如果中间价在 \[0, 0.10) 或 (0.90, 1.0\] 范围内** ——流动性必须是双边的才能计分：Qmin⁡=min⁡(Qone,Qtwo)Q\_{\\min} = \\min({Q\_{one}, Q\_{two}})Qmin​=min(Qone​,Qtwo​)

### [​](https://docs.polymarket.com/cn/market-makers/liquidity-rewards\#5-%E6%A0%87%E5%87%86%E5%8C%96%E5%88%86%E6%95%B0)  5\. 标准化分数

做市商的 Qmin 除以给定样本中所有做市商的 Qmin 总和：Qnormal=Qmin∑n=1N(Qmin)nQ\_{normal} = \\frac{Q\_{min}}{\\sum\_{n=1}^{N}{(Q\_{min})\_n}}Qnormal​=∑n=1N​(Qmin​)n​Qmin​​

### [​](https://docs.polymarket.com/cn/market-makers/liquidity-rewards\#6-%E6%97%B6%E6%9C%9F%E5%88%86%E6%95%B0)  6\. 时期分数

交易者在一个时期中所有样本的 Qnormal 总和：Qepoch=∑u=110,080(Qnormal)uQ\_{epoch} = \\sum\_{u=1}^{10,080}{(Q\_{normal})\_u}Qepoch​=∑u=110,080​(Qnormal​)u​

### [​](https://docs.polymarket.com/cn/market-makers/liquidity-rewards\#7-%E6%9C%80%E7%BB%88%E5%88%86%E6%95%B0)  7\. 最终分数

通过除以给定时期中所有做市商的 Qepoch 总和来标准化 Qepoch。该值乘以市场可用奖励即可得到交易者的奖励：Qfinal=Qepoch∑n=1N(Qepoch)nQ\_{final}=\\frac{Q\_{epoch}}{\\sum\_{n=1}^{N}{(Q\_{epoch})\_n}}Qfinal​=∑n=1N​(Qepoch​)n​Qepoch​​

* * *

## [​](https://docs.polymarket.com/cn/market-makers/liquidity-rewards\#%E5%AE%9E%E4%BE%8B%E6%BC%94%E7%A4%BA)  实例演示

假设调整后的市场中间价为 0.50，m 和 m’ 的最大价差配置均为 3 美分。

### [​](https://docs.polymarket.com/cn/market-makers/liquidity-rewards\#%E6%AD%A5%E9%AA%A4-2-%E7%AC%AC%E4%B8%80%E8%BE%B9%E5%88%86%E6%95%B0)  步骤 2 - 第一边分数

交易者有以下未成交订单：

- 在 m 上以 0.49 价格买入 100Q（价差 = 1 美分）
- 在 m 上以 0.48 价格买入 200Q（价差 = 2 美分）
- 在 m’ 上以 0.51 价格卖出 100Q（价差 = 1 美分）

Qne=((3−1)3)2⋅100+((3−2)3)2⋅200+((3−1)3)2⋅100Q\_{ne} = \\left( \\frac{(3-1)}{3} \\right)^2 \\cdot 100 + \\left( \\frac{(3-2)}{3} \\right)^2 \\cdot 200 + \\left( \\frac{(3-1)}{3} \\right)^2 \\cdot 100Qne​=(3(3−1)​)2⋅100+(3(3−2)​)2⋅200+(3(3−1)​)2⋅100Qne 使用随机采样每分钟计算一次。

### [​](https://docs.polymarket.com/cn/market-makers/liquidity-rewards\#%E6%AD%A5%E9%AA%A4-3-%E7%AC%AC%E4%BA%8C%E8%BE%B9%E5%88%86%E6%95%B0)  步骤 3 - 第二边分数

同一交易者还有：

- 在 m 上以 0.485 价格买入 100Q（价差 = 1.5 美分）
- 在 m’ 上以 0.48 价格买入 100Q（价差 = 2 美分）
- 在 m’ 上以 0.505 价格卖出 200Q（价差 = 0.5 美分）

Qno=((3−1.5)3)2⋅100+((3−2)3)2⋅100+((3−.5)3)2⋅200Q\_{no} = \\left( \\frac{(3-1.5)}{3} \\right)^2 \\cdot 100 + \\left( \\frac{(3-2)}{3} \\right)^2 \\cdot 100 + \\left( \\frac{(3-.5)}{3} \\right)^2 \\cdot 200Qno​=(3(3−1.5)​)2⋅100+(3(3−2)​)2⋅100+(3(3−.5)​)2⋅200Qno 使用随机采样每分钟计算一次。

### [​](https://docs.polymarket.com/cn/market-makers/liquidity-rewards\#%E6%AD%A5%E9%AA%A4-4-7)  步骤 4-7

4. 取 Qne 和 Qno 的最小值（如果中间价在 \[0.10, 0.90\] 范围内则进行单边调整）
5. 对样本中的所有其他做市商进行标准化
6. 对时期中的所有 10,080 个样本求和
7. 再次标准化以获得最终奖励份额

* * *

最低奖励支付金额为 **$1**；低于此金额的奖励将不会支付。

`min_incentive_size` 和 `max_incentive_spread` 都可以通过 CLOB API 和 [Markets API](https://docs.polymarket.com/market-data/fetching-markets) 与完整的市场对象一起获取。时期的奖励分配也可以通过 Markets API 获取。

## [​](https://docs.polymarket.com/cn/market-makers/liquidity-rewards\#%E4%B8%8B%E4%B8%80%E6%AD%A5)  下一步

[**交易** \\
\\
订单输入和报价最佳实践](https://docs.polymarket.com/market-makers/trading)

[**Maker 返利** \\
\\
在 15 分钟加密货币市场上赚取 USDC 返利](https://docs.polymarket.com/market-makers/maker-rebates)

此页面对您有帮助吗？

是否

[Maker 返利计划\\
\\
上一页](https://docs.polymarket.com/cn/market-makers/maker-rebates) [交易\\
\\
下一页](https://docs.polymarket.com/cn/market-makers/trading)

Ctrl+I

助手

AI生成的回答可能包含错误。