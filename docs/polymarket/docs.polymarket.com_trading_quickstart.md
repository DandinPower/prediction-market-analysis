---
url: "https://docs.polymarket.com/trading/quickstart"
title: "Quickstart - Polymarket Documentation"
---

[Skip to main content](https://docs.polymarket.com/trading/quickstart#content-area)

[Polymarket Documentation home page![light logo](https://mintcdn.com/polymarket-292d1b1b/ZibMe6Tli_amZald/logo/light.svg?fit=max&auto=format&n=ZibMe6Tli_amZald&q=85&s=9f9bd559f02181495794661ef6426c0f)![dark logo](https://mintcdn.com/polymarket-292d1b1b/ZibMe6Tli_amZald/logo/dark.svg?fit=max&auto=format&n=ZibMe6Tli_amZald&q=85&s=13abc6754579a3475368ea99d0f5a241)](https://docs.polymarket.com/)

![US](https://d3gk2c5xim1je2.cloudfront.net/flags/US.svg)

English

Search...

Ctrl KAsk AI

Search...

Navigation

Trading

Quickstart

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

- [Troubleshooting](https://docs.polymarket.com/trading/quickstart#troubleshooting)
- [Next Steps](https://docs.polymarket.com/trading/quickstart#next-steps)

This guide walks you through placing an order on Polymarket end-to-end.

1

[Navigate to header](https://docs.polymarket.com/trading/quickstart#)

Install the SDK

TypeScript

Python

Rust

Copy

Ask AI

```
npm install @polymarket/clob-client ethers@5
```

2

[Navigate to header](https://docs.polymarket.com/trading/quickstart#)

Set Up Your Client

Derive your API credentials and initialize the trading client. This example uses an EOA wallet (type `0`) — your wallet pays its own gas and acts as the funder:

TypeScript

Python

Rust

Copy

Ask AI

```
import { ClobClient } from "@polymarket/clob-client";
import { Wallet } from "ethers"; // v5.8.0

const HOST = "https://clob.polymarket.com";
const CHAIN_ID = 137; // Polygon mainnet
const signer = new Wallet(process.env.PRIVATE_KEY);

// Derive API credentials
const tempClient = new ClobClient(HOST, CHAIN_ID, signer);
const apiCreds = await tempClient.createOrDeriveApiKey();

// Initialize trading client
const client = new ClobClient(
  HOST,
  CHAIN_ID,
  signer,
  apiCreds,
  0, // EOA
  signer.address,
);
```

If you have a Polymarket.com account, your funds are in a proxy wallet — use
signature type `1` or `2` instead. See [Signature\\
Types](https://docs.polymarket.com/trading/overview#signature-types) for details.

Before trading, your funder address needs **USDC.e** (for buying outcome
tokens) and **POL** (for gas, if using EOA type `0`). Proxy wallet users
(types `1` and `2`) can use Polymarket’s gasless relayer instead.

3

[Navigate to header](https://docs.polymarket.com/trading/quickstart#)

Place an Order

Get a token ID from the [Markets API](https://docs.polymarket.com/market-data/fetching-markets), then create and submit your order:

TypeScript

Python

Rust

Copy

Ask AI

```
import { Side, OrderType } from "@polymarket/clob-client";

const response = await client.createAndPostOrder(
  {
    tokenID: "YOUR_TOKEN_ID",
    price: 0.5,
    size: 10,
    side: Side.BUY,
  },
  {
    tickSize: "0.01",
    negRisk: false, // Set to true for multi-outcome markets
  },
  OrderType.GTC,
);

console.log("Order ID:", response.orderID);
console.log("Status:", response.status);
```

Look up a market’s `tickSize` and `negRisk` values using the SDK’s
`getTickSize()` and `getNegRisk()` methods, or from the market object returned
by the API.

4

[Navigate to header](https://docs.polymarket.com/trading/quickstart#)

Check Your Orders

TypeScript

Python

Rust

Copy

Ask AI

```
// View all open orders
const openOrders = await client.getOpenOrders();
console.log(`You have ${openOrders.length} open orders`);

// View your trade history
const trades = await client.getTrades();
console.log(`You've made ${trades.length} trades`);

// Cancel an order
await client.cancelOrder(response.orderID);
```

* * *

## [​](https://docs.polymarket.com/trading/quickstart\#troubleshooting)  Troubleshooting

L2 AUTH NOT AVAILABLE - Invalid Signature

Wrong private key, signature type, or funder address for the derived API credentials.

- Check that `signatureType` matches your account type (`0`, `1`, or `2`)
- Ensure `funder` is correct for your wallet type
- Re-derive credentials with `createOrDeriveApiKey()` if unsure

Order rejected - insufficient balance

Your funder address doesn’t have enough tokens:

- **BUY orders**: need USDC.e in your funder address
- **SELL orders**: need outcome tokens in your funder address
- Ensure you have more USDC.e than what’s committed in open orders

Order rejected - insufficient allowance

You need to approve the Exchange contract to spend your tokens. This is
typically done through the Polymarket UI on your first trade, or using the CTF
contract’s `setApprovalForAll()` method.

What is my funder address

Your funder address is the wallet where your funds are held:

- **EOA (type 0)**: Your wallet address directly
- **Proxy wallet (type 1 or 2)**: Go to [polymarket.com/settings](https://polymarket.com/settings) and look for the wallet address in the profile dropdown

If the proxy wallet doesn’t exist, log into Polymarket.com first (it’s deployed on first login).

Blocked by Cloudflare or Geoblock

You’re trying to place a trade from a restricted region. See [Geographic Restrictions](https://docs.polymarket.com/api-reference/geoblock) for details.

* * *

## [​](https://docs.polymarket.com/trading/quickstart\#next-steps)  Next Steps

[**Create Orders** \\
\\
Order types, tick sizes, and error handling](https://docs.polymarket.com/trading/orders/create)

[**Order Attribution** \\
\\
Attribute orders to your builder account for volume credit](https://docs.polymarket.com/trading/orders/attribution)

Was this page helpful?

YesNo

[Overview\\
\\
Previous](https://docs.polymarket.com/trading/overview) [Orderbook\\
\\
Next](https://docs.polymarket.com/trading/orderbook)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.

Suggestions

How do I connect to WebSocket streams?What's required to place my first order?How do I find and fetch market data?