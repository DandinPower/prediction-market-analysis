---
url: "https://docs.polymarket.com/trading/gasless"
title: "Gasless Transactions - Polymarket Documentation"
---

[Skip to main content](https://docs.polymarket.com/trading/gasless#content-area)

[Polymarket Documentation home page![light logo](https://mintcdn.com/polymarket-292d1b1b/ZibMe6Tli_amZald/logo/light.svg?fit=max&auto=format&n=ZibMe6Tli_amZald&q=85&s=9f9bd559f02181495794661ef6426c0f)![dark logo](https://mintcdn.com/polymarket-292d1b1b/ZibMe6Tli_amZald/logo/dark.svg?fit=max&auto=format&n=ZibMe6Tli_amZald&q=85&s=13abc6754579a3475368ea99d0f5a241)](https://docs.polymarket.com/)

![US](https://d3gk2c5xim1je2.cloudfront.net/flags/US.svg)

English

Search...

Ctrl KAsk AI

Search...

Navigation

Trading

Gasless Transactions

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

- [How It Works](https://docs.polymarket.com/trading/gasless#how-it-works)
- [What Is Covered](https://docs.polymarket.com/trading/gasless#what-is-covered)
- [Authentication](https://docs.polymarket.com/trading/gasless#authentication)
- [Using Builder API Keys](https://docs.polymarket.com/trading/gasless#using-builder-api-keys)
- [Using Relayer API Keys](https://docs.polymarket.com/trading/gasless#using-relayer-api-keys)
- [Prerequisites](https://docs.polymarket.com/trading/gasless#prerequisites)
- [Installation](https://docs.polymarket.com/trading/gasless#installation)
- [Client Setup](https://docs.polymarket.com/trading/gasless#client-setup)
- [Wallet Types](https://docs.polymarket.com/trading/gasless#wallet-types)
- [Executing Transactions](https://docs.polymarket.com/trading/gasless#executing-transactions)
- [Token Approval](https://docs.polymarket.com/trading/gasless#token-approval)
- [Redeem Positions](https://docs.polymarket.com/trading/gasless#redeem-positions)
- [Batch Transactions](https://docs.polymarket.com/trading/gasless#batch-transactions)
- [Transaction States](https://docs.polymarket.com/trading/gasless#transaction-states)
- [Contract Addresses](https://docs.polymarket.com/trading/gasless#contract-addresses)
- [Resources](https://docs.polymarket.com/trading/gasless#resources)
- [Next Steps](https://docs.polymarket.com/trading/gasless#next-steps)

Polymarket’s **Relayer Client** enables gasless transactions for your users. Instead of requiring users to hold POL for gas, Polymarket’s infrastructure pays all transaction fees. This creates a seamless experience where users only need USDC.e to trade.

## [​](https://docs.polymarket.com/trading/gasless\#how-it-works)  How It Works

The relayer acts as a transaction sponsor:

1. Your app creates a transaction
2. The user signs it with their private key
3. Your app sends it to Polymarket’s relayer
4. The relayer submits it onchain and pays the gas fee
5. The transaction executes from the user’s wallet

Gasless transactions require authentication with **Builder API Keys** or **Relayer API Keys**.

## [​](https://docs.polymarket.com/trading/gasless\#what-is-covered)  What Is Covered

Polymarket pays gas for all operations routed through the relayer:

| Operation | Description |
| --- | --- |
| **Wallet deployment** | Deploy Safe or Proxy wallets for new users |
| **Token approvals** | Approve contracts to spend USDC.e or outcome tokens |
| **CTF operations** | Split, merge, and redeem positions |
| **Transfers** | Move tokens between addresses |

## [​](https://docs.polymarket.com/trading/gasless\#authentication)  Authentication

The relayer supports two authentication methods. Choose the one that fits your use case.

### [​](https://docs.polymarket.com/trading/gasless\#using-builder-api-keys)  Using Builder API Keys

Builder API Keys are for [Builder Program](https://docs.polymarket.com/builders/overview) members. They authenticate via HMAC-SHA256 signed headers and are required to use the relayer SDKs.All requests must include these headers:

| Header | Description |
| --- | --- |
| `POLY_BUILDER_API_KEY` | Your Builder API key |
| `POLY_BUILDER_TIMESTAMP` | Unix timestamp |
| `POLY_BUILDER_PASSPHRASE` | Your Builder passphrase |
| `POLY_BUILDER_SIGNATURE` | HMAC-SHA256 signature |

The SDKs handle header generation automatically when you provide your credentials via `BuilderConfig`.

### [​](https://docs.polymarket.com/trading/gasless\#using-relayer-api-keys)  Using Relayer API Keys

Relayer API Keys are for market makers and anyone who needs a simpler alternative. You can create them from [Settings > API Keys](https://polymarket.com/settings?tab=api-keys) on the Polymarket website.Include these headers with your requests:

| Header | Description |
| --- | --- |
| `RELAYER_API_KEY` | Your Relayer API key |
| `RELAYER_API_KEY_ADDRESS` | The address that owns the key |

If you want to use the Relayer API Key directly without the SDK, see the [Relayer API Reference](https://docs.polymarket.com/api-reference/relayer).

## [​](https://docs.polymarket.com/trading/gasless\#prerequisites)  Prerequisites

Before using the relayer, you need:

| Requirement | Source |
| --- | --- |
| Builder API credentials **or** Relayer API key | [Builder Profile](https://polymarket.com/settings?tab=builder) or [Settings > API Keys](https://polymarket.com/settings?tab=api-keys) |
| User’s private key or signer | Your wallet integration |
| USDC.e balance | For trading (not for gas) |

> The below section is for the Builder SDKs only. If you want to use the Relayer API Key directly without the SDK, see the [Relayer API Reference](https://docs.polymarket.com/api-reference/relayer).

## [​](https://docs.polymarket.com/trading/gasless\#installation)  Installation

npm

pip

Copy

Ask AI

```
npm install @polymarket/builder-relayer-client @polymarket/builder-signing-sdk
```

## [​](https://docs.polymarket.com/trading/gasless\#client-setup)  Client Setup

Initialize the relayer client with your signing configuration:

- Local Signing

- Remote Signing


Use local signing when your backend handles all transactions securely.

TypeScript

Python

Copy

Ask AI

```
import { createWalletClient, http, Hex } from "viem";
import { privateKeyToAccount } from "viem/accounts";
import { polygon } from "viem/chains";
import { RelayClient } from "@polymarket/builder-relayer-client";
import { BuilderConfig } from "@polymarket/builder-signing-sdk";

const account = privateKeyToAccount(process.env.PRIVATE_KEY as Hex);
const wallet = createWalletClient({
  account,
  chain: polygon,
  transport: http(process.env.RPC_URL),
});

const builderConfig = new BuilderConfig({
  localBuilderCreds: {
    key: process.env.POLY_BUILDER_API_KEY!,
    secret: process.env.POLY_BUILDER_SECRET!,
    passphrase: process.env.POLY_BUILDER_PASSPHRASE!,
  },
});

const client = new RelayClient(
  "https://relayer-v2.polymarket.com/",
  137,
  wallet,
  builderConfig,
);
```

Use remote signing to keep credentials on a secure server you control.**Your signing server** receives request details and returns authentication headers:

Server (TypeScript)

Server (Python)

Copy

Ask AI

```
import {
  buildHmacSignature,
  BuilderApiKeyCreds,
} from "@polymarket/builder-signing-sdk";

const BUILDER_CREDENTIALS: BuilderApiKeyCreds = {
  key: process.env.POLY_BUILDER_API_KEY!,
  secret: process.env.POLY_BUILDER_SECRET!,
  passphrase: process.env.POLY_BUILDER_PASSPHRASE!,
};

// POST /sign endpoint
export async function handleSignRequest(request) {
  const { method, path, body } = await request.json();
  const timestamp = Date.now().toString();

  const signature = buildHmacSignature(
    BUILDER_CREDENTIALS.secret,
    parseInt(timestamp),
    method,
    path,
    body,
  );

  return {
    POLY_BUILDER_SIGNATURE: signature,
    POLY_BUILDER_TIMESTAMP: timestamp,
    POLY_BUILDER_API_KEY: BUILDER_CREDENTIALS.key,
    POLY_BUILDER_PASSPHRASE: BUILDER_CREDENTIALS.passphrase,
  };
}
```

**Your client** points to your signing server:

Client (TypeScript)

Client (Python)

Copy

Ask AI

```
import { RelayClient } from "@polymarket/builder-relayer-client";
import { BuilderConfig } from "@polymarket/builder-signing-sdk";

const builderConfig = new BuilderConfig({
  remoteBuilderConfig: {
    url: "https://your-server.com/sign",
  },
});

const client = new RelayClient(
  "https://relayer-v2.polymarket.com/",
  137,
  wallet,
  builderConfig,
);
```

Never expose Builder API credentials in client-side code. Use environment
variables or a secrets manager.

## [​](https://docs.polymarket.com/trading/gasless\#wallet-types)  Wallet Types

Choose a wallet type when initializing the client:

| Type | Deployment | Best For |
| --- | --- | --- |
| **Safe** | Call `deploy()` before first transaction | Most builder integrations |
| **Proxy** | Auto-deploys on first transaction | Magic Link users |

Safe Wallet (TypeScript)

Safe Wallet (Python)

Proxy Wallet (TypeScript)

Proxy Wallet (Python)

Copy

Ask AI

```
import { RelayClient, RelayerTxType } from "@polymarket/builder-relayer-client";

const client = new RelayClient(
  "https://relayer-v2.polymarket.com/",
  137,
  wallet,
  builderConfig,
  RelayerTxType.SAFE,
);

// Deploy before first transaction
const response = await client.deploy();
const result = await response.wait();
console.log("Safe Address:", result?.proxyAddress);
```

## [​](https://docs.polymarket.com/trading/gasless\#executing-transactions)  Executing Transactions

Use the `execute` method to send transactions through the relayer:

Copy

Ask AI

```
interface Transaction {
  to: string; // Target contract address
  data: string; // Encoded function call
  value: string; // POL to send (usually "0")
}

const response = await client.execute(transactions, "Description");
const result = await response.wait();
```

### [​](https://docs.polymarket.com/trading/gasless\#token-approval)  Token Approval

Approve contracts to spend tokens:

TypeScript

Python

Copy

Ask AI

```
import { encodeFunctionData, maxUint256 } from "viem";

const USDC = "0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174";
const CTF = "0x4D97DCd97eC945f40cF65F87097ACe5EA0476045";

const approveTx = {
  to: USDC,
  data: encodeFunctionData({
    abi: [\
      {\
        name: "approve",\
        type: "function",\
        inputs: [\
          { name: "spender", type: "address" },\
          { name: "amount", type: "uint256" },\
        ],\
        outputs: [{ type: "bool" }],\
      },\
    ],
    functionName: "approve",
    args: [CTF, maxUint256],
  }),
  value: "0",
};

const response = await client.execute([approveTx], "Approve USDC.e for CTF");
await response.wait();
```

### [​](https://docs.polymarket.com/trading/gasless\#redeem-positions)  Redeem Positions

Exchange winning tokens for USDC.e after market resolution:

TypeScript

Python

Copy

Ask AI

```
import { encodeFunctionData } from "viem";

const redeemTx = {
  to: CTF_ADDRESS,
  data: encodeFunctionData({
    abi: [\
      {\
        name: "redeemPositions",\
        type: "function",\
        inputs: [\
          { name: "collateralToken", type: "address" },\
          { name: "parentCollectionId", type: "bytes32" },\
          { name: "conditionId", type: "bytes32" },\
          { name: "indexSets", type: "uint256[]" },\
        ],\
        outputs: [],\
      },\
    ],
    functionName: "redeemPositions",
    args: [collateralToken, parentCollectionId, conditionId, indexSets],
  }),
  value: "0",
};

const response = await client.execute([redeemTx], "Redeem positions");
await response.wait();
```

### [​](https://docs.polymarket.com/trading/gasless\#batch-transactions)  Batch Transactions

Execute multiple operations atomically in a single call:

TypeScript

Python

Copy

Ask AI

```
const approveTx = {
  to: USDC,
  data: encodeFunctionData({
    abi: erc20Abi,
    functionName: "approve",
    args: [CTF, maxUint256],
  }),
  value: "0",
};

const transferTx = {
  to: USDC,
  data: encodeFunctionData({
    abi: erc20Abi,
    functionName: "transfer",
    args: [recipientAddress, parseUnits("50", 6)],
  }),
  value: "0",
};

// Both execute atomically
const response = await client.execute(
  [approveTx, transferTx],
  "Approve and transfer",
);
await response.wait();
```

Batching reduces latency and ensures all transactions succeed or fail
together.

## [​](https://docs.polymarket.com/trading/gasless\#transaction-states)  Transaction States

Track transaction progress through these states:

| State | Terminal | Description |
| --- | --- | --- |
| `STATE_NEW` | No | Transaction received by relayer |
| `STATE_EXECUTED` | No | Submitted onchain |
| `STATE_MINED` | No | Included in a block |
| `STATE_CONFIRMED` | Yes | Finalized successfully |
| `STATE_FAILED` | Yes | Failed permanently |
| `STATE_INVALID` | Yes | Rejected as invalid |

## [​](https://docs.polymarket.com/trading/gasless\#contract-addresses)  Contract Addresses

See [Contract Addresses](https://docs.polymarket.com/resources/contract-addresses) for all Polymarket smart contract addresses on Polygon.

## [​](https://docs.polymarket.com/trading/gasless\#resources)  Resources

- [Builder Relayer Client (TypeScript)](https://github.com/Polymarket/builder-relayer-client)
- [Builder Relayer Client (Python)](https://github.com/Polymarket/py-builder-relayer-client)
- [Builder Signing SDK (TypeScript)](https://github.com/Polymarket/builder-signing-sdk)
- [Builder Signing SDK (Python)](https://github.com/Polymarket/py-builder-signing-sdk)

## [​](https://docs.polymarket.com/trading/gasless\#next-steps)  Next Steps

[**Negative Risk Markets** \\
\\
Learn about capital-efficient trading for multi-outcome events.](https://docs.polymarket.com/advanced/neg-risk)

[**Positions & Tokens** \\
\\
Understand token operations like split, merge, and redeem.](https://docs.polymarket.com/concepts/positions-tokens)

Was this page helpful?

YesNo

[Fees\\
\\
Previous](https://docs.polymarket.com/trading/fees) [Negative Risk Markets\\
\\
Next](https://docs.polymarket.com/advanced/neg-risk)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.

Suggestions

How do I connect to WebSocket streams?What's required to place my first order?How do I find and fetch market data?