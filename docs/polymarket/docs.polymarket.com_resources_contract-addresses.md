---
url: "https://docs.polymarket.com/resources/contract-addresses"
title: "Contract Addresses - Polymarket Documentation"
---

[Skip to main content](https://docs.polymarket.com/resources/contract-addresses#content-area)

[Polymarket Documentation home page![light logo](https://mintcdn.com/polymarket-292d1b1b/ZibMe6Tli_amZald/logo/light.svg?fit=max&auto=format&n=ZibMe6Tli_amZald&q=85&s=9f9bd559f02181495794661ef6426c0f)![dark logo](https://mintcdn.com/polymarket-292d1b1b/ZibMe6Tli_amZald/logo/dark.svg?fit=max&auto=format&n=ZibMe6Tli_amZald&q=85&s=13abc6754579a3475368ea99d0f5a241)](https://docs.polymarket.com/)

![US](https://d3gk2c5xim1je2.cloudfront.net/flags/US.svg)

English

Search...

Ctrl KAsk AI

Search...

Navigation

Resources

Contract Addresses

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

- [Core Trading Contracts](https://docs.polymarket.com/resources/contract-addresses#core-trading-contracts)
- [Token Contracts](https://docs.polymarket.com/resources/contract-addresses#token-contracts)
- [Wallet Factory Contracts](https://docs.polymarket.com/resources/contract-addresses#wallet-factory-contracts)
- [Resolution Contracts](https://docs.polymarket.com/resources/contract-addresses#resolution-contracts)
- [Liquidity](https://docs.polymarket.com/resources/contract-addresses#liquidity)
- [Source Code](https://docs.polymarket.com/resources/contract-addresses#source-code)
- [Usage in Code](https://docs.polymarket.com/resources/contract-addresses#usage-in-code)

All Polymarket contracts are deployed on **Polygon mainnet** (Chain ID: 137). This is the single source of truth for all contract addresses used across the platform.

* * *

## [​](https://docs.polymarket.com/resources/contract-addresses\#core-trading-contracts)  Core Trading Contracts

| Contract | Address | Description |
| --- | --- | --- |
| CTF Exchange | [`0x4bFb41d5B3570DeFd03C39a9A4D8dE6Bd8B8982E`](https://polygonscan.com/address/0x4bFb41d5B3570DeFd03C39a9A4D8dE6Bd8B8982E) | Standard market order matching and settlement |
| Neg Risk CTF Exchange | [`0xC5d563A36AE78145C45a50134d48A1215220f80a`](https://polygonscan.com/address/0xC5d563A36AE78145C45a50134d48A1215220f80a) | Order matching for [neg risk](https://docs.polymarket.com/advanced/neg-risk) (multi-outcome) markets |
| Neg Risk Adapter | [`0xd91E80cF2E7be2e162c6513ceD06f1dD0dA35296`](https://polygonscan.com/address/0xd91E80cF2E7be2e162c6513ceD06f1dD0dA35296) | Converts No tokens between outcomes in neg risk markets |
| Conditional Tokens (CTF) | [`0x4D97DCd97eC945f40cF65F87097ACe5EA0476045`](https://polygonscan.com/address/0x4D97DCd97eC945f40cF65F87097ACe5EA0476045) | ERC1155 token storage — split, merge, and redeem operations |

* * *

## [​](https://docs.polymarket.com/resources/contract-addresses\#token-contracts)  Token Contracts

| Contract | Address | Description |
| --- | --- | --- |
| USDC.e (Bridged USDC) | [`0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174`](https://polygonscan.com/address/0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174) | Collateral token used for all Polymarket trading (6 decimals) |

* * *

## [​](https://docs.polymarket.com/resources/contract-addresses\#wallet-factory-contracts)  Wallet Factory Contracts

| Contract | Address | Description |
| --- | --- | --- |
| Gnosis Safe Factory | [`0xaacfeea03eb1561c4e67d661e40682bd20e3541b`](https://polygonscan.com/address/0xaacfeea03eb1561c4e67d661e40682bd20e3541b) | Deploys Safe wallets |
| Polymarket Proxy Factory | [`0xaB45c5A4B0c941a2F231C04C3f49182e1A254052`](https://polygonscan.com/address/0xaB45c5A4B0c941a2F231C04C3f49182e1A254052) | Deploys proxy wallets |

* * *

## [​](https://docs.polymarket.com/resources/contract-addresses\#resolution-contracts)  Resolution Contracts

| Contract | Address | Description |
| --- | --- | --- |
| UMA Adapter | [`0x6A9D222616C90FcA5754cd1333cFD9b7fb6a4F74`](https://polygonscan.com/address/0x6A9D222616C90FcA5754cd1333cFD9b7fb6a4F74) | Adapter connecting Polymarket to the UMA Optimistic Oracle |
| UMA Optimistic Oracle | [`0xCB1822859cEF82Cd2Eb4E6276C7916e692995130`](https://polygonscan.com/address/0xCB1822859cEF82Cd2Eb4E6276C7916e692995130) | Handles market resolution proposals and disputes |

* * *

## [​](https://docs.polymarket.com/resources/contract-addresses\#liquidity)  Liquidity

| Contract | Address | Description |
| --- | --- | --- |
| Uniswap v3 USDC.e/USDC Pool | [`0xd36ec33c8bed5a9f7b6630855f1533455b98a418`](https://polygonscan.com/address/0xd36ec33c8bed5a9f7b6630855f1533455b98a418) | Used for USDC.e ↔ USDC conversion during withdrawals |

* * *

## [​](https://docs.polymarket.com/resources/contract-addresses\#source-code)  Source Code

[**CTF Exchange** \\
\\
Order matching and settlement contracts](https://github.com/Polymarket/ctf-exchange)

[**Conditional Tokens** \\
\\
Gnosis Conditional Token Framework (ERC1155)](https://github.com/gnosis/conditional-tokens-contracts)

* * *

## [​](https://docs.polymarket.com/resources/contract-addresses\#usage-in-code)  Usage in Code

TypeScript

Python

Rust

Copy

Ask AI

```
const ADDRESSES = {
  USDC_E: "0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174",
  CTF: "0x4D97DCd97eC945f40cF65F87097ACe5EA0476045",
  CTF_EXCHANGE: "0x4bFb41d5B3570DeFd03C39a9A4D8dE6Bd8B8982E",
  NEG_RISK_CTF_EXCHANGE: "0xC5d563A36AE78145C45a50134d48A1215220f80a",
};
```

Was this page helpful?

YesNo

[Tiers\\
\\
Previous](https://docs.polymarket.com/builders/tiers) [Blockchain Data Resources\\
\\
Next](https://docs.polymarket.com/resources/blockchain-data)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.

Suggestions

How do I connect to WebSocket streams?What's required to place my first order?How do I find and fetch market data?