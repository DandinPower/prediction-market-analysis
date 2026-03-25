---
url: "https://docs.polymarket.com/trading/overview"
title: "Overview - Polymarket Documentation"
---

[Skip to main content](https://docs.polymarket.com/trading/overview#content-area)

[Polymarket Documentation home page![light logo](https://mintcdn.com/polymarket-292d1b1b/ZibMe6Tli_amZald/logo/light.svg?fit=max&auto=format&n=ZibMe6Tli_amZald&q=85&s=9f9bd559f02181495794661ef6426c0f)![dark logo](https://mintcdn.com/polymarket-292d1b1b/ZibMe6Tli_amZald/logo/dark.svg?fit=max&auto=format&n=ZibMe6Tli_amZald&q=85&s=13abc6754579a3475368ea99d0f5a241)](https://docs.polymarket.com/)

![US](https://d3gk2c5xim1je2.cloudfront.net/flags/US.svg)

English

Search...

Ctrl KAsk AI

Search...

Navigation

Trading

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

On this page

- [Authentication](https://docs.polymarket.com/trading/overview#authentication)
- [Signature Types](https://docs.polymarket.com/trading/overview#signature-types)
- [Initialize the Trading Client](https://docs.polymarket.com/trading/overview#initialize-the-trading-client)
- [REST API Headers](https://docs.polymarket.com/trading/overview#rest-api-headers)
- [Client Methods](https://docs.polymarket.com/trading/overview#client-methods)
- [What Is in This Section](https://docs.polymarket.com/trading/overview#what-is-in-this-section)

Polymarket’s CLOB (Central Limit Order Book) is a hybrid-decentralized trading system — offchain order matching with onchain settlement via the [Exchange contract](https://github.com/Polymarket/ctf-exchange/tree/main/src) ( [audited by Chainsecurity](https://github.com/Polymarket/ctf-exchange/blob/main/audit/ChainSecurity_Polymarket_Exchange_audit.pdf)). All trading is non-custodial. Orders are [EIP-712](https://eips.ethereum.org/EIPS/eip-712) signed messages, and matched trades settle atomically on Polygon. The operator cannot set prices or execute unauthorized trades — users can always cancel orders onchain independently.We recommend using the open-source SDK clients, which handle order signing, authentication, and submission:

[**TypeScript Client** \\
\\
npm install @polymarket/clob-client](https://github.com/Polymarket/clob-client)

[**Python Client** \\
\\
pip install py-clob-client](https://github.com/Polymarket/py-clob-client)

[**Rust Client** \\
\\
cargo add polymarket-client-sdk](https://github.com/Polymarket/rs-clob-client)

You can also use the REST API directly, but you’ll need to manage [EIP-712\\
order\\
signing](https://github.com/Polymarket/clob-client/blob/main/src/signing/eip712.ts)
and [HMAC authentication\\
headers](https://github.com/Polymarket/clob-client/blob/main/src/signing/hmac.ts)
yourself. See [REST API Headers](https://docs.polymarket.com/trading/overview#rest-api-headers) below.

* * *

## [​](https://docs.polymarket.com/trading/overview\#authentication)  Authentication

The CLOB uses two levels of authentication:

| Level | Method | Purpose |
| --- | --- | --- |
| **L1** | EIP-712 signature (private key) | Create or derive API credentials |
| **L2** | HMAC-SHA256 (API credentials) | Place orders, cancel orders, query trades |

You use your private key once to derive **L2 credentials** (API key, secret, passphrase), which authenticate all subsequent trading requests.

TypeScript

Python

Rust

Copy

Ask AI

```
import { ClobClient } from "@polymarket/clob-client";
import { Wallet } from "ethers"; // v5.8.0

const signer = new Wallet(process.env.PRIVATE_KEY);

// Derive L2 API credentials
const tempClient = new ClobClient("https://clob.polymarket.com", 137, signer);
const apiCreds = await tempClient.createOrDeriveApiKey();
```

* * *

## [​](https://docs.polymarket.com/trading/overview\#signature-types)  Signature Types

When initializing the trading client, you must specify your wallet’s **signature type** and **funder address**:

| Wallet Type | ID | When to Use | Funder Address |
| --- | --- | --- | --- |
| **EOA** | `0` | Standalone wallet — you pay your own gas (POL for gas) | Your EOA wallet address |
| **POLY\_PROXY** | `1` | Polymarket account via Magic Link (email/Google login). Requires [exported private key](https://polymarket.com/settings) from Polymarket.com | Your proxy wallet address |
| **GNOSIS\_SAFE** | `2` | Polymarket account via browser wallet (MetaMask, Rabby) or embedded wallet (Privy, Turnkey). Most common type | Your proxy wallet address |

If you have a Polymarket.com account, your funds are in a proxy wallet visible
in the profile dropdown. Use type `1` or `2`. Type `0` is for standalone EOA
wallets only.

### [​](https://docs.polymarket.com/trading/overview\#initialize-the-trading-client)  Initialize the Trading Client

TypeScript

Python

Rust

Copy

Ask AI

```
const client = new ClobClient(
  "https://clob.polymarket.com",
  137,
  signer,
  apiCreds,
  2, // GNOSIS_SAFE
  "0x...", // Your proxy wallet address
);
```

* * *

## [​](https://docs.polymarket.com/trading/overview\#rest-api-headers)  REST API Headers

If you’re using the REST API directly (without the SDK), you need to attach authentication headers to each request.**L1 Headers** — for creating or deriving API credentials:

| Header | Description |
| --- | --- |
| `POLY_ADDRESS` | Your wallet address |
| `POLY_SIGNATURE` | EIP-712 signature |
| `POLY_TIMESTAMP` | Unix timestamp |
| `POLY_NONCE` | Request nonce |

**L2 Headers** — for all trading operations (orders, cancellations, queries):

| Header | Description |
| --- | --- |
| `POLY_ADDRESS` | Your wallet address |
| `POLY_SIGNATURE` | HMAC-SHA256 signature of the request |
| `POLY_TIMESTAMP` | Unix timestamp |
| `POLY_API_KEY` | Your API key |
| `POLY_PASSPHRASE` | Your API passphrase |

Even with L2 authentication, methods that create orders still require the
user’s private key for EIP-712 order payload signing. L2 credentials
authenticate the request, but the order itself must be signed by the key.

* * *

## [​](https://docs.polymarket.com/trading/overview\#client-methods)  Client Methods

[**Public Methods** \\
\\
Market data, orderbooks, prices, and spreads — no auth required.](https://docs.polymarket.com/trading/clients/public)

[**L1 Methods** \\
\\
Sign orders and derive API credentials with your private key.](https://docs.polymarket.com/trading/clients/l1)

[**L2 Methods** \\
\\
Place orders, cancel orders, query trades, and manage notifications.](https://docs.polymarket.com/trading/clients/l2)

[**Builder Methods** \\
\\
Track attributed trades and manage builder credentials.](https://docs.polymarket.com/trading/clients/builder)

* * *

## [​](https://docs.polymarket.com/trading/overview\#what-is-in-this-section)  What Is in This Section

[**Quickstart** \\
\\
Place your first order end-to-end](https://docs.polymarket.com/trading/quickstart)

[**Orderbook** \\
\\
Reading the orderbook, prices, spreads, and midpoints](https://docs.polymarket.com/trading/orderbook)

[**Orders** \\
\\
Order types, tick sizes, creating, cancelling, and querying orders](https://docs.polymarket.com/trading/orders/create)

[**Fees** \\
\\
Fee structure, fee-enabled markets, and maker rebates](https://docs.polymarket.com/trading/fees)

[**Gasless Transactions** \\
\\
Execute onchain operations without paying gas](https://docs.polymarket.com/trading/gasless)

[**CTF Tokens** \\
\\
Split, merge, and redeem outcome tokens](https://docs.polymarket.com/trading/ctf/overview)

[**Bridge** \\
\\
Deposit and withdraw funds across chains](https://docs.polymarket.com/trading/bridge/deposit)

Was this page helpful?

YesNo

[Subgraph\\
\\
Previous](https://docs.polymarket.com/market-data/subgraph) [Quickstart\\
\\
Next](https://docs.polymarket.com/trading/quickstart)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.

Suggestions

How do I connect to WebSocket streams?What's required to place my first order?How do I find and fetch market data?