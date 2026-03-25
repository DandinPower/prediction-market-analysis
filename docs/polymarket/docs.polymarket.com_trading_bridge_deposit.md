---
url: "https://docs.polymarket.com/trading/bridge/deposit"
title: "Deposit - Polymarket Documentation"
---

[Skip to main content](https://docs.polymarket.com/trading/bridge/deposit#content-area)

[Polymarket Documentation home page![light logo](https://mintcdn.com/polymarket-292d1b1b/ZibMe6Tli_amZald/logo/light.svg?fit=max&auto=format&n=ZibMe6Tli_amZald&q=85&s=9f9bd559f02181495794661ef6426c0f)![dark logo](https://mintcdn.com/polymarket-292d1b1b/ZibMe6Tli_amZald/logo/dark.svg?fit=max&auto=format&n=ZibMe6Tli_amZald&q=85&s=13abc6754579a3475368ea99d0f5a241)](https://docs.polymarket.com/)

![US](https://d3gk2c5xim1je2.cloudfront.net/flags/US.svg)

English

Search...

Ctrl KAsk AI

Search...

Navigation

Bridge

Deposit

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

  - [Deposit](https://docs.polymarket.com/trading/bridge/deposit)
  - [Supported Assets](https://docs.polymarket.com/trading/bridge/supported-assets)
  - [Quote](https://docs.polymarket.com/trading/bridge/quote)
  - [Withdraw](https://docs.polymarket.com/trading/bridge/withdraw)
  - [Deposit Status](https://docs.polymarket.com/trading/bridge/status)

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

- [How It Works](https://docs.polymarket.com/trading/bridge/deposit#how-it-works)
- [Create Deposit Addresses](https://docs.polymarket.com/trading/bridge/deposit#create-deposit-addresses)
- [Address Types](https://docs.polymarket.com/trading/bridge/deposit#address-types)
- [Deposit Flow](https://docs.polymarket.com/trading/bridge/deposit#deposit-flow)
- [USDC vs USDC.e](https://docs.polymarket.com/trading/bridge/deposit#usdc-vs-usdc-e)
- [Large Deposits](https://docs.polymarket.com/trading/bridge/deposit#large-deposits)
- [Minimum Deposits](https://docs.polymarket.com/trading/bridge/deposit#minimum-deposits)
- [Deposit Recovery](https://docs.polymarket.com/trading/bridge/deposit#deposit-recovery)
- [Next Steps](https://docs.polymarket.com/trading/bridge/deposit#next-steps)

Polymarket uses **USDC.e** (Bridged USDC) on Polygon as collateral for all trading. The Bridge API lets you deposit assets from Ethereum, Solana, Bitcoin, and other chains—they’re automatically converted to USDC.e on Polygon.

## [​](https://docs.polymarket.com/trading/bridge/deposit\#how-it-works)  How It Works

1. Request deposit addresses for your Polymarket wallet
2. Send assets to the appropriate address for your source chain
3. Assets are bridged and swapped to USDC.e automatically
4. USDC.e is credited to your wallet for trading

## [​](https://docs.polymarket.com/trading/bridge/deposit\#create-deposit-addresses)  Create Deposit Addresses

Generate unique deposit addresses linked to your Polymarket wallet. See the [Bridge API Reference](https://docs.polymarket.com/api-reference/introduction) for full request and response schemas.

Copy

Ask AI

```
curl -X POST https://bridge.polymarket.com/deposit \
  -H "Content-Type: application/json" \
  -d '{"address": "0x56687bf447db6ffa42ffe2204a05edaa20f55839"}'
```

### [​](https://docs.polymarket.com/trading/bridge/deposit\#address-types)  Address Types

| Address | Use For |
| --- | --- |
| `evm` | Ethereum, Arbitrum, Base, Optimism, and other EVM chains |
| `svm` | Solana |
| `btc` | Bitcoin |
| `tvm` | Tron |

Each address is unique to your wallet. Only send assets from supported chains
to the correct address type.

## [​](https://docs.polymarket.com/trading/bridge/deposit\#deposit-flow)  Deposit Flow

1

[Navigate to header](https://docs.polymarket.com/trading/bridge/deposit#)

Get Your Deposit Address

Call `POST /deposit` with your Polymarket wallet address to get deposit
addresses.

2

[Navigate to header](https://docs.polymarket.com/trading/bridge/deposit#)

Check Supported Assets

Verify your token is supported and meets the minimum deposit amount via
`/supported-assets`.

3

[Navigate to header](https://docs.polymarket.com/trading/bridge/deposit#)

Send Assets

Transfer tokens to the appropriate deposit address from your source chain.

4

[Navigate to header](https://docs.polymarket.com/trading/bridge/deposit#)

Track Status

Monitor your deposit progress using `/status/{address}`.

## [​](https://docs.polymarket.com/trading/bridge/deposit\#usdc-vs-usdc-e)  USDC vs USDC.e

You can deposit either USDC (native) or USDC.e (bridged) to your Polymarket wallet. If you deposit native USDC, you will be prompted to “activate funds,” which swaps it to USDC.e via the lowest-fee Uniswap pool (less than 10bp slippage).

## [​](https://docs.polymarket.com/trading/bridge/deposit\#large-deposits)  Large Deposits

For deposits over $50,000 originating from a chain other than Polygon, we recommend using a third-party bridge to minimize slippage:

- [DeBridge](https://app.debridge.finance/)
- [Across](https://app.across.to/bridge)
- [Portal](https://portalbridge.com/)

Bridge directly to your Polymarket USDC (Polygon) deposit address. Polymarket is not affiliated with or responsible for any third-party bridge.

## [​](https://docs.polymarket.com/trading/bridge/deposit\#minimum-deposits)  Minimum Deposits

Each asset has a minimum deposit amount. Deposits below the minimum will not be processed. Check `/supported-assets` for current minimums.

## [​](https://docs.polymarket.com/trading/bridge/deposit\#deposit-recovery)  Deposit Recovery

If you deposited the wrong token on Ethereum or Polygon, use these tools to recover your funds:

- **Ethereum deposits**: [recovery.polymarket.com](https://recovery.polymarket.com/)
- **Polygon deposits**: [matic-recovery.polymarket.com](https://matic-recovery.polymarket.com/)

Sending unsupported tokens may cause **irrecoverable loss**. Always verify
your token is listed in [Supported Assets](https://docs.polymarket.com/trading/bridge/supported-assets)
before depositing.

## [​](https://docs.polymarket.com/trading/bridge/deposit\#next-steps)  Next Steps

[**Supported Assets** \\
\\
See all supported chains and tokens with minimum amounts.](https://docs.polymarket.com/trading/bridge/supported-assets)

[**Check Status** \\
\\
Track your deposit progress through completion.](https://docs.polymarket.com/trading/bridge/status)

Was this page helpful?

YesNo

[Real-Time Data Socket\\
\\
Previous](https://docs.polymarket.com/market-data/websocket/rtds) [Supported Assets\\
\\
Next](https://docs.polymarket.com/trading/bridge/supported-assets)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.

Suggestions

How do I connect to WebSocket streams?What's required to place my first order?How do I find and fetch market data?