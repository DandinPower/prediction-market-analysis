---
url: "https://docs.polymarket.com/"
title: "Overview - Polymarket Documentation"
---

[Skip to main content](https://docs.polymarket.com/#content-area)

[Polymarket Documentation home page![light logo](https://mintcdn.com/polymarket-292d1b1b/ZibMe6Tli_amZald/logo/light.svg?fit=max&auto=format&n=ZibMe6Tli_amZald&q=85&s=9f9bd559f02181495794661ef6426c0f)![dark logo](https://mintcdn.com/polymarket-292d1b1b/ZibMe6Tli_amZald/logo/dark.svg?fit=max&auto=format&n=ZibMe6Tli_amZald&q=85&s=13abc6754579a3475368ea99d0f5a241)](https://docs.polymarket.com/)

![US](https://d3gk2c5xim1je2.cloudfront.net/flags/US.svg)

English

Search...

Ctrl KAsk AI

Search...

Navigation

Getting Started

Overview

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

[🇺🇸Looking for Polymarket US documentation?Visit US Docs →](https://docs.polymarket.us/)

# Polymarket Documentation

Build on the world’s largest prediction market. APIs, SDKs, and tools for prediction market developers.

## Developer Quickstart

Make your first API request in minutes. Learn the basics of the Polymarket platform, fetch market data, place orders, and redeem winning positions.

[Get Started →](https://docs.polymarket.com/quickstart)

TypeScript

Python

Rust

Copy

Ask AI

```
import { ClobClient, Side } from "@polymarket/clob-client";

const client = new ClobClient(host, chainId, signer, creds);

const order = await client.createAndPostOrder(
  { tokenID, price: 0.50, size: 10, side: Side.BUY },
  { tickSize: "0.01", negRisk: false }
);
```

## Get Familiar with Polymarket

Learn the fundamentals, explore our APIs, and start building on the world’s largest prediction market.

[**Quickstart** \\
\\
Set up your environment and make your first API call in minutes.](https://docs.polymarket.com/quickstart)

[**Core Concepts** \\
\\
Understand markets, events, tokens, and how trading works.](https://docs.polymarket.com/concepts/markets-events)

[**API Reference** \\
\\
Explore REST endpoints, WebSocket streams, and authentication.](https://docs.polymarket.com/api-reference/introduction)

[**SDKs** \\
\\
Official Python, TypeScript, and Rust libraries for faster development.](https://docs.polymarket.com/api-reference/clients-sdks)

[![Banner](https://mintcdn.com/polymarket-292d1b1b/FOMte3ewbG-LVy3k/images/banner.png?fit=max&auto=format&n=FOMte3ewbG-LVy3k&q=85&s=d83f2f21e8474e998d8ba0f45810d978)](https://builders.polymarket.com/)

[![](https://docs.polymarket.com/images/icons/medal.svg)\\
**Builder Program** Build apps on Polymarket and earn rewards for driving volume](https://builders.polymarket.com/) [![](https://docs.polymarket.com/images/icons/quiz.svg)\\
**Help Desk** Get support, report issues, and find answers to common questions](https://help.polymarket.com/) [![](https://docs.polymarket.com/images/icons/sensor.svg)\\
**Status** Check API uptime, service health, and incident reports](https://status.polymarket.com/)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.

Suggestions

How do I connect to WebSocket streams?What's required to place my first order?How do I find and fetch market data?

![Banner](https://mintcdn.com/polymarket-292d1b1b/FOMte3ewbG-LVy3k/images/banner.png?w=1650&fit=max&auto=format&n=FOMte3ewbG-LVy3k&q=85&s=121075a6d26595fafb3e82922810fbff)

![](https://docs.polymarket.com/images/icons/medal.svg)

![](https://docs.polymarket.com/images/icons/quiz.svg)

![](https://docs.polymarket.com/images/icons/sensor.svg)