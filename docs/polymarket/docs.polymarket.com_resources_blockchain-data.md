---
url: "https://docs.polymarket.com/resources/blockchain-data"
title: "Blockchain Data Resources - Polymarket Documentation"
---

[Skip to main content](https://docs.polymarket.com/resources/blockchain-data#content-area)

[Polymarket Documentation home page![light logo](https://mintcdn.com/polymarket-292d1b1b/ZibMe6Tli_amZald/logo/light.svg?fit=max&auto=format&n=ZibMe6Tli_amZald&q=85&s=9f9bd559f02181495794661ef6426c0f)![dark logo](https://mintcdn.com/polymarket-292d1b1b/ZibMe6Tli_amZald/logo/dark.svg?fit=max&auto=format&n=ZibMe6Tli_amZald&q=85&s=13abc6754579a3475368ea99d0f5a241)](https://docs.polymarket.com/)

![US](https://d3gk2c5xim1je2.cloudfront.net/flags/US.svg)

English

Search...

Ctrl KAsk AI

Search...

Navigation

Resources

Blockchain Data Resources

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

- [Data](https://docs.polymarket.com/resources/blockchain-data#data)
- [Goldsky](https://docs.polymarket.com/resources/blockchain-data#goldsky)
- [Dune](https://docs.polymarket.com/resources/blockchain-data#dune)
- [Allium](https://docs.polymarket.com/resources/blockchain-data#allium)
- [Dashboards](https://docs.polymarket.com/resources/blockchain-data#dashboards)
- [Community Dashboards](https://docs.polymarket.com/resources/blockchain-data#community-dashboards)

Polymarket data that lands on the blockchain, such as trades, balances, positions, and redeems, is available through various on-chain analytics platforms and blockchain data providers. Polymarket also provides its own APIs and WebSockets. See the [API Endpoints reference](https://docs.polymarket.com/quickstart/reference/endpoints) for more information.The purpose of this page is to serve as a public good for Polymarket builders, researches, and analysts alike.

* * *

## [​](https://docs.polymarket.com/resources/blockchain-data\#data)  Data

### [​](https://docs.polymarket.com/resources/blockchain-data\#goldsky)  Goldsky

[Goldsky](https://docs.goldsky.com/chains/polymarket) provides real-time streaming pipelines for Polymarket on-chain activity (i.e. trades, balances, positions, etc…) into your own database/data warehouse.Goldsky also partnered with [ClickHouse](https://clickhouse.com/) to create [CryptoHouse](https://crypto.clickhouse.com/), where you can query Polymarket on-chain data using SQL.

### [​](https://docs.polymarket.com/resources/blockchain-data\#dune)  Dune

[Dune](https://dune.com/) is a blockchain analytics platform that has Polymarket on-chain activity (i.e. trades, balances, positions, etc…). Query Polymarket data using SQL, create custom dashboards, and more.Here are a few simple queries to get started:

| Query | Description | Link |
| --- | --- | --- |
| Volume | Notional Volume and Maker & Taker USDC Volume | [View Dune Query](https://dune.com/queries/6545441) |
| TVL | USDC locked in Polymarket smart contracts | [View Dune Query](https://dune.com/queries/6588784) |
| Open Interest | Estimated market open interest, and over time | [View Dune Query](https://dune.com/queries/6555478) |

### [​](https://docs.polymarket.com/resources/blockchain-data\#allium)  Allium

[Allium](https://docs.allium.so/historical-data/predictions) is a blockchain analytics platform that has Polymarket on-chain activity (i.e. trades, balances, positions, etc…). Query Polymarket data using SQL, create custom dashboards, and more.—

## [​](https://docs.polymarket.com/resources/blockchain-data\#dashboards)  Dashboards

Third-party blockchain analytics platforms that aggregate and visualize Polymarket data:

![7s2FxV2K_400x400](https://pbs.twimg.com/profile_images/1651677302634483712/7s2FxV2K_400x400.jpg)

[**Blockworks**](https://blockworks.com/analytics/polymarket)

![2XeO9mPb_400x400](https://pbs.twimg.com/profile_images/1896982195723546624/2XeO9mPb_400x400.png)

[**Artemis**](https://app.artemisanalytics.com/asset/polymarket?from=assets)

![qq80s3hx_400x400](https://pbs.twimg.com/profile_images/1986458079248986112/qq80s3hx_400x400.jpg)

[**Dune**](https://dune.com/discover/content/popular?q=polymarket&resource-type=dashboards)

![rAeLzZqs_400x400](https://pbs.twimg.com/profile_images/1915756547705036800/rAeLzZqs_400x400.jpg)

[**DeFiLlama**](https://defillama.com/protocol/polymarket)

![9babG7Df_400x400](https://pbs.twimg.com/profile_images/1944749695525425152/9babG7Df_400x400.jpg)

[**The Block**](https://www.theblock.co/data/decentralized-finance/prediction-markets-and-betting)

![SMum_RcQ_400x400](https://pbs.twimg.com/profile_images/1594678659222306817/SMum_RcQ_400x400.jpg)

[**Token Terminal**](https://tokenterminal.com/explorer/projects/polymarket)

![UEwR3lHt_400x400](https://pbs.twimg.com/profile_images/1778926940407132160/UEwR3lHt_400x400.jpg)

[**Allium**](https://predictions.allium.so/)

### [​](https://docs.polymarket.com/resources/blockchain-data\#community-dashboards)  Community Dashboards

Community-created Dune dashboards of Polymarket on-chain analytics:

| Dashboard | Created By | Link |
| --- | --- | --- |
| Polymarket Overview | [@datadashboards](https://x.com/datadashboards) | [View Dashboard](https://dune.com/datadashboards/polymarket-overview) |
| Polymarket Volume, OI, Markets, Addresses and TVL | [@hildobby](https://x.com/hildobby) | [View Dashboard](https://dune.com/hildobby/polymarket) |
| Polymarket Historical Accuracy | [@alexmccullaaa](https://x.com/alexmccullaaa) | [View Dashboard](https://dune.com/alexmccullough/how-accurate-is-polymarket) |
| Polymarket Builders Dashboard | [@defioasis](https://x.com/defioasis) | [View Dashboard](https://dune.com/gateresearch/pmbuilders) |

Was this page helpful?

YesNo

[Contract Addresses\\
\\
Previous](https://docs.polymarket.com/resources/contract-addresses) [Error Codes\\
\\
Next](https://docs.polymarket.com/resources/error-codes)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.

Suggestions

How do I connect to WebSocket streams?What's required to place my first order?How do I find and fetch market data?