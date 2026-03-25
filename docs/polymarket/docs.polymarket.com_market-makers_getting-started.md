---
url: "https://docs.polymarket.com/market-makers/getting-started"
title: "Getting Started - Polymarket Documentation"
---

[Skip to main content](https://docs.polymarket.com/market-makers/getting-started#content-area)

[Polymarket Documentation home page![light logo](https://mintcdn.com/polymarket-292d1b1b/ZibMe6Tli_amZald/logo/light.svg?fit=max&auto=format&n=ZibMe6Tli_amZald&q=85&s=9f9bd559f02181495794661ef6426c0f)![dark logo](https://mintcdn.com/polymarket-292d1b1b/ZibMe6Tli_amZald/logo/dark.svg?fit=max&auto=format&n=ZibMe6Tli_amZald&q=85&s=13abc6754579a3475368ea99d0f5a241)](https://docs.polymarket.com/)

![US](https://d3gk2c5xim1je2.cloudfront.net/flags/US.svg)

English

Search...

Ctrl KAsk AI

Search...

Navigation

Market Makers

Getting Started

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

- [Using the Bridge API](https://docs.polymarket.com/market-makers/getting-started#using-the-bridge-api)
- [EOA](https://docs.polymarket.com/market-makers/getting-started#eoa)
- [Safe Wallet](https://docs.polymarket.com/market-makers/getting-started#safe-wallet)
- [Required Approvals](https://docs.polymarket.com/market-makers/getting-started#required-approvals)
- [Contract Addresses](https://docs.polymarket.com/market-makers/getting-started#contract-addresses)
- [Approve via Relayer Client](https://docs.polymarket.com/market-makers/getting-started#approve-via-relayer-client)
- [Next Steps](https://docs.polymarket.com/market-makers/getting-started#next-steps)

Before you can start market making, you need to complete these one-time setup steps — deposit USDC.e to Polygon, deploy a wallet, approve tokens for trading, and generate API credentials.

1

[Navigate to header](https://docs.polymarket.com/market-makers/getting-started#)

Deposit USDC.e

Market makers need USDC.e on Polygon to fund their trading operations.

| Method | Best For | Documentation |
| --- | --- | --- |
| Bridge API | Automated deposits from other chains | [Bridge Deposit](https://docs.polymarket.com/trading/bridge/deposit) |
| Direct Polygon transfer | Already have USDC.e on Polygon | N/A |
| Cross-chain bridge | Large deposits from Ethereum | [Supported Assets](https://docs.polymarket.com/trading/bridge/supported-assets) |

### [​](https://docs.polymarket.com/market-makers/getting-started\#using-the-bridge-api)  Using the Bridge API

Copy

Ask AI

```
// Get deposit addresses for your Polymarket wallet
const deposit = await fetch("https://bridge.polymarket.com/deposit", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({
    address: "YOUR_POLYMARKET_WALLET_ADDRESS",
  }),
});

// Returns deposit addresses for EVM, SVM, and BTC networks
const addresses = await deposit.json();
// Send USDC to the appropriate address for your source chain
```

2

[Navigate to header](https://docs.polymarket.com/market-makers/getting-started#)

Deploy a Wallet

### [​](https://docs.polymarket.com/market-makers/getting-started\#eoa)  EOA

Standard Ethereum wallet. You pay for all onchain transactions (approvals, splits, merges, trade execution).

### [​](https://docs.polymarket.com/market-makers/getting-started\#safe-wallet)  Safe Wallet

Gnosis Safe-based wallet deployed via Polymarket’s relayer. Benefits:

- **Gasless transactions** — Polymarket pays gas fees for onchain operations
- **Contract wallet** — Enables advanced features like batched transactions

Deploy a Safe wallet using the Relayer Client:

TypeScript

Python

Copy

Ask AI

```
import { RelayClient, RelayerTxType } from "@polymarket/builder-relayer-client";

const client = new RelayClient(
  "https://relayer-v2.polymarket.com/",
  137, // Polygon mainnet
  signer,
  builderConfig,
  RelayerTxType.SAFE,
);

// Deploy the Safe wallet
const response = await client.deploy();
const result = await response.wait();
console.log("Safe Address:", result?.proxyAddress);
```

See [Gasless Transactions](https://docs.polymarket.com/trading/gasless) for full Relayer Client setup
including local and remote signing configurations.

3

[Navigate to header](https://docs.polymarket.com/market-makers/getting-started#)

Approve Tokens

Before trading, you must approve the exchange contracts to spend your tokens.

### [​](https://docs.polymarket.com/market-makers/getting-started\#required-approvals)  Required Approvals

| Token | Spender | Purpose |
| --- | --- | --- |
| USDC.e | CTF Contract | Split USDC.e into outcome tokens |
| CTF (outcome tokens) | CTF Exchange | Trade outcome tokens |
| CTF (outcome tokens) | Neg Risk CTF Exchange | Trade neg-risk market tokens |

### [​](https://docs.polymarket.com/market-makers/getting-started\#contract-addresses)  Contract Addresses

Copy

Ask AI

```
const ADDRESSES = {
  USDCe: "0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174",
  CTF: "0x4D97DCd97eC945f40cF65F87097ACe5EA0476045",
  CTF_EXCHANGE: "0x4bFb41d5B3570DeFd03C39a9A4D8dE6Bd8B8982E",
  NEG_RISK_CTF_EXCHANGE: "0xC5d563A36AE78145C45a50134d48A1215220f80a",
  NEG_RISK_ADAPTER: "0xd91E80cF2E7be2e162c6513ceD06f1dD0dA35296",
};
```

### [​](https://docs.polymarket.com/market-makers/getting-started\#approve-via-relayer-client)  Approve via Relayer Client

TypeScript

Python

Copy

Ask AI

```
import { ethers } from "ethers";
import { Interface } from "ethers/lib/utils";

const erc20Interface = new Interface([\
  "function approve(address spender, uint256 amount) returns (bool)",\
]);

// Approve USDCe for CTF contract
const approveTx = {
  to: ADDRESSES.USDCe,
  data: erc20Interface.encodeFunctionData("approve", [\
    ADDRESSES.CTF,\
    ethers.constants.MaxUint256,\
  ]),
  value: "0",
};

const response = await client.execute([approveTx], "Approve USDCe for CTF");
await response.wait();
```

4

[Navigate to header](https://docs.polymarket.com/market-makers/getting-started#)

Generate API Credentials

To place orders and access authenticated endpoints, you need L2 API credentials derived from your wallet.

TypeScript

Python

Rust

Copy

Ask AI

```
import { ClobClient } from "@polymarket/clob-client";

const client = new ClobClient("https://clob.polymarket.com", 137, signer);

// Derive API credentials from your wallet
const credentials = await client.createOrDeriveApiKey();
console.log("API Key:", credentials.key);
console.log("Secret:", credentials.secret);
console.log("Passphrase:", credentials.passphrase);
```

See [Authentication](https://docs.polymarket.com/trading/overview#authentication) for full details on signature types and REST API headers.

* * *

## [​](https://docs.polymarket.com/market-makers/getting-started\#next-steps)  Next Steps

[**Trading** \\
\\
Post limit orders and manage quotes](https://docs.polymarket.com/market-makers/trading)

[**Market Data** \\
\\
Connect to real-time market data](https://docs.polymarket.com/market-data/overview)

Was this page helpful?

YesNo

[Overview\\
\\
Previous](https://docs.polymarket.com/market-makers/overview) [Maker Rebates Program\\
\\
Next](https://docs.polymarket.com/market-makers/maker-rebates)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.

Suggestions

How do I connect to WebSocket streams?What's required to place my first order?How do I find and fetch market data?