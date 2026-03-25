---
url: "https://docs.polymarket.com/market-makers/maker-rebates"
title: "Maker Rebates Program - Polymarket Documentation"
---

[Skip to main content](https://docs.polymarket.com/market-makers/maker-rebates#content-area)

[Polymarket Documentation home page![light logo](https://mintcdn.com/polymarket-292d1b1b/ZibMe6Tli_amZald/logo/light.svg?fit=max&auto=format&n=ZibMe6Tli_amZald&q=85&s=9f9bd559f02181495794661ef6426c0f)![dark logo](https://mintcdn.com/polymarket-292d1b1b/ZibMe6Tli_amZald/logo/dark.svg?fit=max&auto=format&n=ZibMe6Tli_amZald&q=85&s=13abc6754579a3475368ea99d0f5a241)](https://docs.polymarket.com/)

![US](https://d3gk2c5xim1je2.cloudfront.net/flags/US.svg)

English

Search...

Ctrl KAsk AI

Search...

Navigation

Market Makers

Maker Rebates Program

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

- [Why Maker Rebates](https://docs.polymarket.com/market-makers/maker-rebates#why-maker-rebates)
- [How Maker Rebates Work](https://docs.polymarket.com/market-makers/maker-rebates#how-maker-rebates-work)
- [Eligibility](https://docs.polymarket.com/market-makers/maker-rebates#eligibility)
- [Payment](https://docs.polymarket.com/market-makers/maker-rebates#payment)
- [Funding](https://docs.polymarket.com/market-makers/maker-rebates#funding)
- [Fee-Curve Weighted Rebates](https://docs.polymarket.com/market-makers/maker-rebates#fee-curve-weighted-rebates)
- [Taker Fee Structure](https://docs.polymarket.com/market-makers/maker-rebates#taker-fee-structure)
- [Fee Table](https://docs.polymarket.com/market-makers/maker-rebates#fee-table)
- [Fee Precision](https://docs.polymarket.com/market-makers/maker-rebates#fee-precision)
- [Which Markets Are Eligible](https://docs.polymarket.com/market-makers/maker-rebates#which-markets-are-eligible)
- [FAQ](https://docs.polymarket.com/market-makers/maker-rebates#faq)
- [Next Steps](https://docs.polymarket.com/market-makers/maker-rebates#next-steps)

Polymarket has enabled taker fees on **all crypto markets**, **NCAAB (college basketball)**, and **Serie A** markets. These fees fund a **Maker Rebates** program that pays daily USDC rebates to liquidity providers.

* * *

## [​](https://docs.polymarket.com/market-makers/maker-rebates\#why-maker-rebates)  Why Maker Rebates

Sports markets benefit from the same dynamics as crypto markets. When liquidity is deeper:

- Spreads tend to be tighter
- Price impact is lower
- Fills are more reliable
- Markets are more resilient during volatility

Maker Rebates incentivize **consistent, competitive quoting** so everyone gets a better trading experience.

* * *

## [​](https://docs.polymarket.com/market-makers/maker-rebates\#how-maker-rebates-work)  How Maker Rebates Work

- **Paid daily in USDC:** Rebates are calculated and distributed every day.
- **Performance-based:** You earn based on the share of liquidity you provided that actually got taken.

### [​](https://docs.polymarket.com/market-makers/maker-rebates\#eligibility)  Eligibility

Place orders that add liquidity to the book and get filled (i.e., your liquidity is taken by another trader).

### [​](https://docs.polymarket.com/market-makers/maker-rebates\#payment)  Payment

Rebates are paid daily in USDC, directly to your wallet.

* * *

## [​](https://docs.polymarket.com/market-makers/maker-rebates\#funding)  Funding

Maker Rebates are funded by taker fees collected in eligible markets. A percentage of these fees are redistributed to makers who keep the markets liquid. The rebate percentage differs by market type.

| Market Type | Period | Maker Rebate | Distribution Method |
| --- | --- | --- | --- |
| 15-Min Crypto | Jan 19, 2026+ | 20% | Fee-curve weighted |
| 5-Min Crypto | Feb 12, 2026+ | 20% | Fee-curve weighted |
| Sports (NCAAB, Serie A) | Feb 18, 2026+ | 25% | Fee-curve weighted |
| 1H, 4H, Daily, Weekly Crypto | Mar 6, 2026+ | 20% | Fee-curve weighted |

Polymarket collects taker fees in eligible markets (all crypto markets, NCAAB,
and Serie A). The rebate percentage is at the sole discretion of Polymarket
and may change over time.

* * *

## [​](https://docs.polymarket.com/market-makers/maker-rebates\#fee-curve-weighted-rebates)  Fee-Curve Weighted Rebates

Rebates are distributed using the **same formula as taker fees**. This ensures makers are rewarded proportionally to the fee value their liquidity generates.For each filled maker order:

Copy

Ask AI

```
fee_equivalent = C × p × feeRate × (p × (1 - p))^exponent
```

Where **C** = number of shares traded and **p** = price of the shares. The fee parameters differ by market type:

| Parameter | Sports (NCAAB, Serie A) | Crypto |
| --- | --- | --- |
| Fee Rate | 0.0175 | 0.25 |
| Exponent | 1 | 2 |

Your daily rebate:

Copy

Ask AI

```
rebate = (your_fee_equivalent / total_fee_equivalent) * rebate_pool
```

Totals are calculated per market, so you only compete with other makers in the same market.

* * *

## [​](https://docs.polymarket.com/market-makers/maker-rebates\#taker-fee-structure)  Taker Fee Structure

Taker fees are calculated in USDC and vary based on the share price. However, fees are collected in shares on buy orders and USDC on sell orders. Fees are highest at 50% probability and lowest at the extremes (near 0% or 100%).

Fee Curves

### Fee Curves

Effective fee rate (%) by share price for 100 shares

Two curves showing effective taker fee rates by share price. The 5-Min & 15-Min Crypto curve peaks at 1.56% at price 0.50. The Sports (NCAAB, Serie A) curve peaks at 0.44% at price 0.50. Both curves decrease symmetrically toward 0% at the extremes.

Crypto

Sports

(NCAAB, Serie A)

0.00.20.40.60.81.01.21.4

[Download image](https://datawrapper.dwcdn.net/qTzMH/full.png) Created with [Datawrapper](https://www.datawrapper.de/_/qTzMH)

### [​](https://docs.polymarket.com/market-makers/maker-rebates\#fee-table)  Fee Table

- Crypto

- Sports - NCAAB and Serie A


| Price | Trade Value | Fee (USDC) | Effective Rate |
| --- | --- | --- | --- |
| $0.01 | $1 | $0.00 | 0.00% |
| $0.05 | $5 | $0.003 | 0.06% |
| $0.10 | $10 | $0.02 | 0.20% |
| $0.15 | $15 | $0.06 | 0.41% |
| $0.20 | $20 | $0.13 | 0.64% |
| $0.25 | $25 | $0.22 | 0.88% |
| $0.30 | $30 | $0.33 | 1.10% |
| $0.35 | $35 | $0.45 | 1.29% |
| $0.40 | $40 | $0.58 | 1.44% |
| $0.45 | $45 | $0.69 | 1.53% |
| $0.50 | $50 | $0.78 | **1.56%** |
| $0.55 | $55 | $0.84 | 1.53% |
| $0.60 | $60 | $0.86 | 1.44% |
| $0.65 | $65 | $0.84 | 1.29% |
| $0.70 | $70 | $0.77 | 1.10% |
| $0.75 | $75 | $0.66 | 0.88% |
| $0.80 | $80 | $0.51 | 0.64% |
| $0.85 | $85 | $0.35 | 0.41% |
| $0.90 | $90 | $0.18 | 0.20% |
| $0.95 | $95 | $0.05 | 0.06% |
| $0.99 | $99 | $0.00 | 0.00% |

The maximum effective fee rate is **1.56%** at 50% probability. Fees decrease symmetrically toward both extremes.

| Price | Trade Value | Fee (USDC) | Effective Rate |
| --- | --- | --- | --- |
| $0.01 | $1 | $0.00 | 0.02% |
| $0.05 | $5 | $0.00 | 0.08% |
| $0.10 | $10 | $0.02 | 0.16% |
| $0.15 | $15 | $0.03 | 0.22% |
| $0.20 | $20 | $0.06 | 0.28% |
| $0.25 | $25 | $0.08 | 0.33% |
| $0.30 | $30 | $0.11 | 0.37% |
| $0.35 | $35 | $0.14 | 0.40% |
| $0.40 | $40 | $0.17 | 0.42% |
| $0.45 | $45 | $0.19 | 0.43% |
| $0.50 | $50 | $0.22 | **0.44%** |
| $0.55 | $55 | $0.24 | 0.43% |
| $0.60 | $60 | $0.25 | 0.42% |
| $0.65 | $65 | $0.26 | 0.40% |
| $0.70 | $70 | $0.26 | 0.37% |
| $0.75 | $75 | $0.25 | 0.33% |
| $0.80 | $80 | $0.22 | 0.28% |
| $0.85 | $85 | $0.19 | 0.22% |
| $0.90 | $90 | $0.14 | 0.16% |
| $0.95 | $95 | $0.08 | 0.08% |
| $0.99 | $99 | $0.02 | 0.02% |

The maximum effective fee rate is **0.44%** at 50% probability. Fees decrease symmetrically toward both extremes.

### [​](https://docs.polymarket.com/market-makers/maker-rebates\#fee-precision)  Fee Precision

Fees are rounded to 4 decimal places. The smallest fee charged is 0.0001 USDC. Anything smaller rounds to zero, so very small trades near the extremes may incur no fee at all.

* * *

## [​](https://docs.polymarket.com/market-makers/maker-rebates\#which-markets-are-eligible)  Which Markets Are Eligible

The following market types have taker fees enabled and are eligible for maker rebates:

- **All crypto markets**
- **NCAAB (college basketball) markets**
- **Serie A markets**

Fees apply only to markets deployed on or after the activation date. Pre-existing markets are unaffected. Markets with fees enabled have `feesEnabled` set to `true` on the market object.

All other markets remain fee-free.

* * *

## [​](https://docs.polymarket.com/market-makers/maker-rebates\#faq)  FAQ

How do I qualify for maker rebates

Place orders that add liquidity to the book and get filled (i.e., your
liquidity is taken by another trader).

When are rebates paid

Daily, in USDC.

How are rebates calculated

Rebates are proportional to your share of executed maker liquidity in each
eligible market. Totals are calculated per market, so you only compete with
other makers in the same market.

Where does the rebate pool come from

Taker fees collected in eligible markets are allocated to the maker rebate
pool and distributed daily.

Which markets have fees enabled

All crypto markets, NCAAB, and Serie A markets. Fees only apply to markets deployed on or after the
activation date.

Is Polymarket charging fees on all markets

No. Fees apply only to crypto markets, NCAAB, and Serie A markets. All other
markets remain fee-free.

* * *

## [​](https://docs.polymarket.com/market-makers/maker-rebates\#next-steps)  Next Steps

[**Fee Structure** \\
\\
Full fee handling guide for SDK and REST API users.](https://docs.polymarket.com/trading/fees)

[**Place Orders** \\
\\
Start placing orders on Polymarket.](https://docs.polymarket.com/trading/quickstart)

Was this page helpful?

YesNo

[Getting Started\\
\\
Previous](https://docs.polymarket.com/market-makers/getting-started) [Liquidity Rewards\\
\\
Next](https://docs.polymarket.com/market-makers/liquidity-rewards)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.

Suggestions

How do I connect to WebSocket streams?What's required to place my first order?How do I find and fetch market data?