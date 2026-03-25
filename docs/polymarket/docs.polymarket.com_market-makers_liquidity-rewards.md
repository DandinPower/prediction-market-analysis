---
url: "https://docs.polymarket.com/market-makers/liquidity-rewards"
title: "Liquidity Rewards - Polymarket Documentation"
---

[Skip to main content](https://docs.polymarket.com/market-makers/liquidity-rewards#content-area)

[Polymarket Documentation home page![light logo](https://mintcdn.com/polymarket-292d1b1b/ZibMe6Tli_amZald/logo/light.svg?fit=max&auto=format&n=ZibMe6Tli_amZald&q=85&s=9f9bd559f02181495794661ef6426c0f)![dark logo](https://mintcdn.com/polymarket-292d1b1b/ZibMe6Tli_amZald/logo/dark.svg?fit=max&auto=format&n=ZibMe6Tli_amZald&q=85&s=13abc6754579a3475368ea99d0f5a241)](https://docs.polymarket.com/)

![US](https://d3gk2c5xim1je2.cloudfront.net/flags/US.svg)

English

Search...

Ctrl KAsk AI

Search...

Navigation

Market Makers

Liquidity Rewards

[Documentation](https://docs.polymarket.com/) [API Reference](https://docs.polymarket.com/api-reference/introduction)

![https://raw.githubusercontent.com/suhailkakar/demo/refs/heads/main/book.svg](https://raw.githubusercontent.com/suhailkakar/demo/refs/heads/main/book.svg)

##### Getting Started

- [Overview](https://docs.polymarket.com/)
- [Polymarket 101](https://docs.polymarket.com/polymarket-101)
- [Quickstart](https://docs.polymarket.com/quickstart)

![https://mintlify.s3.us-west-1.amazonaws.com/polymarket-292d1b1b/images/icons/nav/layers.svg](https://mintlify.s3.us-west-1.amazonaws.com/polymarket-292d1b1b/images/icons/nav/layers.svg)

##### Core Concepts

- [Markets & Events](https://docs.polymarket.com/concepts/markets-events)
- [Prices & Orderbook](https://docs.polymarket.com/concepts/prices-orderbook)
- [Positions & Tokens](https://docs.polymarket.com/concepts/positions-tokens)
- [Order Lifecycle](https://docs.polymarket.com/concepts/order-lifecycle)
- [Resolution](https://docs.polymarket.com/concepts/resolution)

![https://mintlify.s3.us-west-1.amazonaws.com/polymarket-292d1b1b/images/icons/nav/paper.svg](https://mintlify.s3.us-west-1.amazonaws.com/polymarket-292d1b1b/images/icons/nav/paper.svg)

##### Market Data

- [Overview](https://docs.polymarket.com/market-data/overview)
- [Fetching Markets](https://docs.polymarket.com/market-data/fetching-markets)
- [Subgraph](https://docs.polymarket.com/market-data/subgraph)

![https://mintlify.s3.us-west-1.amazonaws.com/polymarket-292d1b1b/images/icons/nav/chart.svg](https://mintlify.s3.us-west-1.amazonaws.com/polymarket-292d1b1b/images/icons/nav/chart.svg)

##### Trading

- [Overview](https://docs.polymarket.com/trading/overview)
- [Quickstart](https://docs.polymarket.com/trading/quickstart)
- [Orderbook](https://docs.polymarket.com/trading/orderbook)
- Orders

- Client Reference

- [Fees](https://docs.polymarket.com/trading/fees)
- [Gasless Transactions](https://docs.polymarket.com/trading/gasless)
- [Negative Risk Markets](https://docs.polymarket.com/advanced/neg-risk)
- [Matching Engine Restarts](https://docs.polymarket.com/trading/matching-engine)
- CTF Tokens

- WebSocket

- Bridge


![https://mintlify.s3.us-west-1.amazonaws.com/polymarket-292d1b1b/images/icons/nav/histogram.svg](https://mintlify.s3.us-west-1.amazonaws.com/polymarket-292d1b1b/images/icons/nav/histogram.svg)

##### Market Makers

- [Overview](https://docs.polymarket.com/market-makers/overview)
- [Getting Started](https://docs.polymarket.com/market-makers/getting-started)
- [Maker Rebates Program](https://docs.polymarket.com/market-makers/maker-rebates)
- [Liquidity Rewards](https://docs.polymarket.com/market-makers/liquidity-rewards)
- Operations


![https://mintlify.s3.us-west-1.amazonaws.com/polymarket-292d1b1b/images/icons/nav/trophy.svg](https://mintlify.s3.us-west-1.amazonaws.com/polymarket-292d1b1b/images/icons/nav/trophy.svg)

##### Builder Program

- [Builder Program](https://docs.polymarket.com/builders/overview)
- [API Keys](https://docs.polymarket.com/builders/api-keys)
- [Tiers](https://docs.polymarket.com/builders/tiers)

![https://mintlify.s3.us-west-1.amazonaws.com/polymarket-292d1b1b/images/icons/nav/book-search.svg](https://mintlify.s3.us-west-1.amazonaws.com/polymarket-292d1b1b/images/icons/nav/book-search.svg)

##### Resources

- [Contract Addresses](https://docs.polymarket.com/resources/contract-addresses)
- [Blockchain Data Resources](https://docs.polymarket.com/resources/blockchain-data)
- [Error Codes](https://docs.polymarket.com/resources/error-codes)

On this page

- [Methodology](https://docs.polymarket.com/market-makers/liquidity-rewards#methodology)
- [Variables](https://docs.polymarket.com/market-makers/liquidity-rewards#variables)
- [Equations](https://docs.polymarket.com/market-makers/liquidity-rewards#equations)
- [1\. Order Scoring Function](https://docs.polymarket.com/market-makers/liquidity-rewards#1-order-scoring-function)
- [2\. First Market Side Score](https://docs.polymarket.com/market-makers/liquidity-rewards#2-first-market-side-score)
- [3\. Second Market Side Score](https://docs.polymarket.com/market-makers/liquidity-rewards#3-second-market-side-score)
- [4\. Minimum Score](https://docs.polymarket.com/market-makers/liquidity-rewards#4-minimum-score)
- [5\. Normalized Score](https://docs.polymarket.com/market-makers/liquidity-rewards#5-normalized-score)
- [6\. Epoch Score](https://docs.polymarket.com/market-makers/liquidity-rewards#6-epoch-score)
- [7\. Final Score](https://docs.polymarket.com/market-makers/liquidity-rewards#7-final-score)
- [Worked Example](https://docs.polymarket.com/market-makers/liquidity-rewards#worked-example)
- [Step 2 - First Side Score](https://docs.polymarket.com/market-makers/liquidity-rewards#step-2-first-side-score)
- [Step 3 - Second Side Score](https://docs.polymarket.com/market-makers/liquidity-rewards#step-3-second-side-score)
- [Steps 4-7](https://docs.polymarket.com/market-makers/liquidity-rewards#steps-4-7)
- [Next Steps](https://docs.polymarket.com/market-makers/liquidity-rewards#next-steps)

By posting resting limit orders, liquidity providers (makers) are automatically eligible for Polymarket’s incentive program. Rewards are distributed directly to maker addresses daily at midnight UTC.The program is designed to:

- Catalyze liquidity across all markets
- Encourage liquidity throughout a market’s entire lifecycle
- Motivate passive, balanced quoting tight to a market’s midpoint
- Encourage trading activity
- Discourage blatantly exploitative behaviors

This program is heavily inspired by [dYdX’s liquidity provider\\
rewards](https://www.dydx.foundation/blog/liquidity-provider-rewards). The
methodology is essentially a copy of dYdX’s approach with adjustments for
binary contract markets — distinct books, no staking mechanic, a modified
order utility-relative depth function, and reward amounts isolated per market.

* * *

## [​](https://docs.polymarket.com/market-makers/liquidity-rewards\#methodology)  Methodology

Liquidity providers are rewarded based on a formula that rewards participation in markets, boosts two-sided depth (single-sided orders still score), and tighter spread vs the size-cutoff-adjusted midpoint. Each market configures a max spread and min size cutoff within which orders are considered. The average of rewards earned is determined by the relative share of each participant’s Qn in market m.

### [​](https://docs.polymarket.com/market-makers/liquidity-rewards\#variables)  Variables

| Variable | Description |
| --- | --- |
| S | Order position scoring function |
| v | Max spread from midpoint (in cents) |
| s | Spread from size-cutoff-adjusted midpoint |
| b | In-game multiplier |
| m | Market |
| m’ | Market complement (i.e. NO if m = YES) |
| n | Trader index |
| u | Sample index |
| c | Scaling factor (currently 3.0 on all markets) |
| Qne | Point total for book one for a sample |
| Qno | Point total for book two for a sample |
| Spread% | Distance from midpoint (bps or relative) for order n in market m |
| BidSize | Share-denominated quantity of bid |
| AskSize | Share-denominated quantity of ask |

* * *

## [​](https://docs.polymarket.com/market-makers/liquidity-rewards\#equations)  Equations

### [​](https://docs.polymarket.com/market-makers/liquidity-rewards\#1-order-scoring-function)  1\. Order Scoring Function

Quadratic scoring rule for an order based on position between the adjusted midpoint and the minimum qualifying spread:S(v,s)=(v−sv)2⋅bS(v,s)= (\\frac{v-s}{v})^2 \\cdot bS(v,s)=(vv−s​)2⋅b

### [​](https://docs.polymarket.com/market-makers/liquidity-rewards\#2-first-market-side-score)  2\. First Market Side Score

Qone=S(v,Spreadm1)⋅BidSizem1+S(v,Spreadm2)⋅BidSizem2+…Q\_{one}= S(v,Spread\_{m\_1}) \\cdot BidSize\_{m\_1} + S(v,Spread\_{m\_2}) \\cdot BidSize\_{m\_2} + \\dots Qone​=S(v,Spreadm1​​)⋅BidSizem1​​+S(v,Spreadm2​​)⋅BidSizem2​​+…+S(v,Spreadm1′)⋅AskSizem1′+S(v,Spreadm2′)⋅AskSizem2′ \+ S(v, Spread\_{m^\\prime\_1}) \\cdot AskSize\_{m^\\prime\_1} + S(v, Spread\_{m^\\prime\_2}) \\cdot AskSize\_{m^\\prime\_2}+S(v,Spreadm1′​​)⋅AskSizem1′​​+S(v,Spreadm2′​​)⋅AskSizem2′​​

### [​](https://docs.polymarket.com/market-makers/liquidity-rewards\#3-second-market-side-score)  3\. Second Market Side Score

Qtwo=S(v,Spreadm1)⋅AskSizem1+S(v,Spreadm2)⋅AskSizem2+…Q\_{two}= S(v,Spread\_{m\_1}) \\cdot AskSize\_{m\_1} + S(v,Spread\_{m\_2}) \\cdot AskSize\_{m\_2} + \\dots Qtwo​=S(v,Spreadm1​​)⋅AskSizem1​​+S(v,Spreadm2​​)⋅AskSizem2​​+…+S(v,Spreadm1′)⋅BidSizem1′+S(v,Spreadm2′)⋅BidSizem2′ \+ S(v, Spread\_{m^\\prime\_1}) \\cdot BidSize\_{m^\\prime\_1} + S(v, Spread\_{m^\\prime\_2}) \\cdot BidSize\_{m^\\prime\_2}+S(v,Spreadm1′​​)⋅BidSizem1′​​+S(v,Spreadm2′​​)⋅BidSizem2′​​

### [​](https://docs.polymarket.com/market-makers/liquidity-rewards\#4-minimum-score)  4\. Minimum Score

Boosts two-sided liquidity by taking the minimum of Qne and Qno, while still rewarding single-sided liquidity at a reduced rate (divided by c).**If midpoint is in range \[0.10, 0.90\]** — single-sided liquidity can score:Qmin⁡=max⁡(min⁡(Qone,Qtwo),max⁡(Qone/c,Qtwo/c))Q\_{\\min} = \\max(\\min({Q\_{one}, Q\_{two}}), \\max(Q\_{one}/c, Q\_{two}/c))Qmin​=max(min(Qone​,Qtwo​),max(Qone​/c,Qtwo​/c))**If midpoint is in range \[0, 0.10) or (0.90, 1.0\]** — liquidity must be double-sided to score:Qmin⁡=min⁡(Qone,Qtwo)Q\_{\\min} = \\min({Q\_{one}, Q\_{two}})Qmin​=min(Qone​,Qtwo​)

### [​](https://docs.polymarket.com/market-makers/liquidity-rewards\#5-normalized-score)  5\. Normalized Score

Qmin of a market maker divided by the sum of all Qmin across market makers in a given sample:Qnormal=Qmin∑n=1N(Qmin)nQ\_{normal} = \\frac{Q\_{min}}{\\sum\_{n=1}^{N}{(Q\_{min})\_n}}Qnormal​=∑n=1N​(Qmin​)n​Qmin​​

### [​](https://docs.polymarket.com/market-makers/liquidity-rewards\#6-epoch-score)  6\. Epoch Score

Sum of all Qnormal for a trader across all samples in an epoch:Qepoch=∑u=110,080(Qnormal)uQ\_{epoch} = \\sum\_{u=1}^{10,080}{(Q\_{normal})\_u}Qepoch​=∑u=110,080​(Qnormal​)u​

### [​](https://docs.polymarket.com/market-makers/liquidity-rewards\#7-final-score)  7\. Final Score

Normalizes Qepoch by dividing by the sum of all market makers’ Qepoch in a given epoch. This value is multiplied by the rewards available for the market to get a trader’s reward:Qfinal=Qepoch∑n=1N(Qepoch)nQ\_{final}=\\frac{Q\_{epoch}}{\\sum\_{n=1}^{N}{(Q\_{epoch})\_n}}Qfinal​=∑n=1N​(Qepoch​)n​Qepoch​​

* * *

## [​](https://docs.polymarket.com/market-makers/liquidity-rewards\#worked-example)  Worked Example

Assume an adjusted market midpoint of 0.50 and a max spread config of 3 cents for both m and m’.

### [​](https://docs.polymarket.com/market-makers/liquidity-rewards\#step-2-first-side-score)  Step 2 - First Side Score

A trader has the following open orders:

- 100Q bid on m @ 0.49 (spread = 1 cent)
- 200Q bid on m @ 0.48 (spread = 2 cents)
- 100Q ask on m’ @ 0.51 (spread = 1 cent)

Qne=((3−1)3)2⋅100+((3−2)3)2⋅200+((3−1)3)2⋅100Q\_{ne} = \\left( \\frac{(3-1)}{3} \\right)^2 \\cdot 100 + \\left( \\frac{(3-2)}{3} \\right)^2 \\cdot 200 + \\left( \\frac{(3-1)}{3} \\right)^2 \\cdot 100Qne​=(3(3−1)​)2⋅100+(3(3−2)​)2⋅200+(3(3−1)​)2⋅100Qne is calculated every minute using random sampling.

### [​](https://docs.polymarket.com/market-makers/liquidity-rewards\#step-3-second-side-score)  Step 3 - Second Side Score

The same trader also has:

- 100Q bid on m @ 0.485 (spread = 1.5 cents)
- 100Q bid on m’ @ 0.48 (spread = 2 cents)
- 200Q ask on m’ @ 0.505 (spread = 0.5 cents)

Qno=((3−1.5)3)2⋅100+((3−2)3)2⋅100+((3−.5)3)2⋅200Q\_{no} = \\left( \\frac{(3-1.5)}{3} \\right)^2 \\cdot 100 + \\left( \\frac{(3-2)}{3} \\right)^2 \\cdot 100 + \\left( \\frac{(3-.5)}{3} \\right)^2 \\cdot 200Qno​=(3(3−1.5)​)2⋅100+(3(3−2)​)2⋅100+(3(3−.5)​)2⋅200Qno is calculated every minute using random sampling.

### [​](https://docs.polymarket.com/market-makers/liquidity-rewards\#steps-4-7)  Steps 4-7

4. Take the minimum of Qne and Qno (with single-sided adjustment if midpoint is in \[0.10, 0.90\])
5. Normalize against all other market makers in the sample
6. Sum across all 10,080 samples in the epoch
7. Normalize again to get final reward share

* * *

The minimum reward payout is **$1**; amounts below this will not be paid.

Both `min_incentive_size` and `max_incentive_spread` can be fetched alongside
full market objects via the CLOB API and [Markets\\
API](https://docs.polymarket.com/market-data/fetching-markets). Reward allocations for an epoch can also
be fetched via the Markets API.

## [​](https://docs.polymarket.com/market-makers/liquidity-rewards\#next-steps)  Next Steps

[**Trading** \\
\\
Order entry and quoting best practices](https://docs.polymarket.com/market-makers/trading)

[**Maker Rebates** \\
\\
Earn USDC rebates on eligible crypto and sports markets](https://docs.polymarket.com/market-makers/maker-rebates)

Was this page helpful?

YesNo

[Maker Rebates Program\\
\\
Previous](https://docs.polymarket.com/market-makers/maker-rebates) [Trading\\
\\
Next](https://docs.polymarket.com/market-makers/trading)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.

Suggestions

How do I connect to WebSocket streams?What's required to place my first order?How do I find and fetch market data?