---
url: "https://docs.polymarket.com/trading/fees"
title: "Fees - Polymarket Documentation"
---

[Skip to main content](https://docs.polymarket.com/trading/fees#content-area)

[Polymarket Documentation home page![light logo](https://mintcdn.com/polymarket-292d1b1b/ZibMe6Tli_amZald/logo/light.svg?fit=max&auto=format&n=ZibMe6Tli_amZald&q=85&s=9f9bd559f02181495794661ef6426c0f)![dark logo](https://mintcdn.com/polymarket-292d1b1b/ZibMe6Tli_amZald/logo/dark.svg?fit=max&auto=format&n=ZibMe6Tli_amZald&q=85&s=13abc6754579a3475368ea99d0f5a241)](https://docs.polymarket.com/)

![US](https://d3gk2c5xim1je2.cloudfront.net/flags/US.svg)

English

Search...

Ctrl KAsk AI

Search...

Navigation

Trading

Fees

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

- [Fee-Free Markets](https://docs.polymarket.com/trading/fees#fee-free-markets)
- [Markets With Fees](https://docs.polymarket.com/trading/fees#markets-with-fees)
- [Fee Structure](https://docs.polymarket.com/trading/fees#fee-structure)
- [Fee Table](https://docs.polymarket.com/trading/fees#fee-table)
- [Fee Precision](https://docs.polymarket.com/trading/fees#fee-precision)
- [Identifying Fee-Enabled Markets](https://docs.polymarket.com/trading/fees#identifying-fee-enabled-markets)
- [Fee Handling for API Users](https://docs.polymarket.com/trading/fees#fee-handling-for-api-users)
- [Using the SDK](https://docs.polymarket.com/trading/fees#using-the-sdk)
- [Using the REST API](https://docs.polymarket.com/trading/fees#using-the-rest-api)
- [Next Steps](https://docs.polymarket.com/trading/fees#next-steps)

Polymarket does not charge fees on most markets. However, certain markets have taker fees enabled to fund the [Maker Rebates Program](https://docs.polymarket.com/market-makers/maker-rebates).

* * *

## [​](https://docs.polymarket.com/trading/fees\#fee-free-markets)  Fee-Free Markets

The vast majority of Polymarket markets have **no trading fees**:

- No fees to deposit or withdraw USDC (though intermediaries like Coinbase or MoonPay may charge their own fees)
- No fees to trade shares

* * *

## [​](https://docs.polymarket.com/trading/fees\#markets-with-fees)  Markets With Fees

The following market types charge a small taker fee on each trade. These fees are collected and redistributed daily to market makers as rebates, incentivizing deeper liquidity and tighter spreads.

- **All crypto markets**
- **NCAAB (college basketball) markets**
- **Serie A markets**

Fees apply only to markets deployed on or after the activation date. Pre-existing markets are unaffected. Markets with fees enabled have `feesEnabled` set to `true` on the market object.

### [​](https://docs.polymarket.com/trading/fees\#fee-structure)  Fee Structure

Fees are calculated using the following formula:

Copy

Ask AI

```
fee = C × p × feeRate × (p × (1 - p))^exponent
```

Where **C** = number of shares traded and **p** = price of the shares. The fee parameters differ by market type:

| Parameter | Sports (NCAAB, Serie A) | Crypto |
| --- | --- | --- |
| Fee Rate | 0.0175 | 0.25 |
| Exponent | 1 | 2 |
| Maker Rebate % | 25% | 20% |

Taker fees are calculated in USDC and vary based on the share price. However, fees are collected in shares on buy orders and USDC on sell orders. The effective rate **peaks at 50%** probability and decreases symmetrically toward the extremes.

Fee Curves

### Fee Curves

Effective fee rate (%) by share price for 100 shares

Two curves showing effective taker fee rates by share price. The 5-Min & 15-Min Crypto curve peaks at 1.56% at price 0.50. The Sports (NCAAB, Serie A) curve peaks at 0.44% at price 0.50. Both curves decrease symmetrically toward 0% at the extremes.

Crypto

Sports

(NCAAB, Serie A)

0.00.20.40.60.81.01.21.4

[Download image](https://datawrapper.dwcdn.net/qTzMH/full.png) Created with [Datawrapper](https://www.datawrapper.de/_/qTzMH)

### [​](https://docs.polymarket.com/trading/fees\#fee-table)  Fee Table

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

### [​](https://docs.polymarket.com/trading/fees\#fee-precision)  Fee Precision

Fees are rounded to 4 decimal places. The smallest fee charged is **0.0001 USDC**. Anything smaller rounds to zero, so very small trades near the extremes may incur no fee at all.

* * *

## [​](https://docs.polymarket.com/trading/fees\#identifying-fee-enabled-markets)  Identifying Fee-Enabled Markets

Markets with fees have `feesEnabled` set to `true` on the market object. You can also query the fee-rate endpoint to check any specific market. See the [API Reference](https://docs.polymarket.com/api-reference/introduction) for full endpoint documentation.

Copy

Ask AI

```
GET https://clob.polymarket.com/fee-rate?token_id={token_id}
```

* * *

## [​](https://docs.polymarket.com/trading/fees\#fee-handling-for-api-users)  Fee Handling for API Users

### [​](https://docs.polymarket.com/trading/fees\#using-the-sdk)  Using the SDK

The official CLOB clients **automatically handle fees** for you — they fetch the fee rate and include it in the signed order payload.

[**TypeScript** \\
\\
npm install @polymarket/clob-client@latest](https://github.com/Polymarket/clob-client)

[**Python** \\
\\
pip install —upgrade py-clob-client](https://github.com/Polymarket/py-clob-client)

[**Rust** \\
\\
cargo add polymarket-client-sdk](https://github.com/Polymarket/rs-clob-client)

**What the client does automatically:**

1. Fetches the fee rate for the market’s token ID
2. Includes `feeRateBps` in the order structure
3. Signs the order with the fee rate included

**You don’t need to do anything extra.** Your orders will work on fee-enabled markets.

### [​](https://docs.polymarket.com/trading/fees\#using-the-rest-api)  Using the REST API

If you’re calling the REST API directly or building your own order signing, you must manually include the fee rate in your signed order payload.**Step 1:** Fetch the fee rate for the token ID before creating your order:

Copy

Ask AI

```
GET https://clob.polymarket.com/fee-rate?token_id={token_id}
```

See the [fee-rate API Reference](https://docs.polymarket.com/api-reference/introduction) for full response details. Fee-enabled markets return a non-zero value; fee-free markets return `0`.**Step 2:** Add the `feeRateBps` field to your order object. This value is part of the signed payload — the CLOB validates your signature against it.

Copy

Ask AI

```
{
  "salt": "12345",
  "maker": "0x...",
  "signer": "0x...",
  "taker": "0x...",
  "tokenId": "71321045679252212594626385532706912750332728571942532289631379312455583992563",
  "makerAmount": "50000000",
  "takerAmount": "100000000",
  "expiration": "0",
  "nonce": "0",
  "feeRateBps": "1000",
  "side": "0",
  "signatureType": 2,
  "signature": "0x..."
}
```

**Step 3:** Sign and submit:

1. Include `feeRateBps` in the order object **before signing**
2. Sign the complete order
3. POST to the order endpoint

Always fetch `fee_rate_bps` dynamically — do not hardcode. The fee rate varies
by market type and may change over time. You only need to pass `feeRateBps`.

* * *

## [​](https://docs.polymarket.com/trading/fees\#next-steps)  Next Steps

[**Maker Rebates Program** \\
\\
Learn how taker fees fund daily USDC rebates for liquidity providers.](https://docs.polymarket.com/market-makers/maker-rebates)

[**Place Orders** \\
\\
Start placing orders on Polymarket.](https://docs.polymarket.com/trading/quickstart)

Was this page helpful?

YesNo

[Builder Methods\\
\\
Previous](https://docs.polymarket.com/trading/clients/builder) [Gasless Transactions\\
\\
Next](https://docs.polymarket.com/trading/gasless)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.

Suggestions

How do I connect to WebSocket streams?What's required to place my first order?How do I find and fetch market data?