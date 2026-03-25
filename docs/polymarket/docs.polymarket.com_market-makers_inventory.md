---
url: "https://docs.polymarket.com/market-makers/inventory"
title: "Inventory Management - Polymarket Documentation"
---

[Skip to main content](https://docs.polymarket.com/market-makers/inventory#content-area)

[Polymarket Documentation home page![light logo](https://mintcdn.com/polymarket-292d1b1b/ZibMe6Tli_amZald/logo/light.svg?fit=max&auto=format&n=ZibMe6Tli_amZald&q=85&s=9f9bd559f02181495794661ef6426c0f)![dark logo](https://mintcdn.com/polymarket-292d1b1b/ZibMe6Tli_amZald/logo/dark.svg?fit=max&auto=format&n=ZibMe6Tli_amZald&q=85&s=13abc6754579a3475368ea99d0f5a241)](https://docs.polymarket.com/)

![US](https://d3gk2c5xim1je2.cloudfront.net/flags/US.svg)

English

Search...

Ctrl KAsk AI

Search...

Navigation

Operations

Inventory Management

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

  - [Trading](https://docs.polymarket.com/market-makers/trading)
  - [Inventory Management](https://docs.polymarket.com/market-makers/inventory)

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

- [Splitting USDC.e into Tokens](https://docs.polymarket.com/market-makers/inventory#splitting-usdc-e-into-tokens)
- [Merging Tokens to USDC.e](https://docs.polymarket.com/market-makers/inventory#merging-tokens-to-usdc-e)
- [Redeeming After Resolution](https://docs.polymarket.com/market-makers/inventory#redeeming-after-resolution)
- [Check Resolution Status](https://docs.polymarket.com/market-makers/inventory#check-resolution-status)
- [Redeem Winning Tokens](https://docs.polymarket.com/market-makers/inventory#redeem-winning-tokens)
- [Negative Risk Markets](https://docs.polymarket.com/market-makers/inventory#negative-risk-markets)
- [Inventory Strategies](https://docs.polymarket.com/market-makers/inventory#inventory-strategies)
- [Before Quoting](https://docs.polymarket.com/market-makers/inventory#before-quoting)
- [During Trading](https://docs.polymarket.com/market-makers/inventory#during-trading)
- [After Resolution](https://docs.polymarket.com/market-makers/inventory#after-resolution)
- [Batch Operations](https://docs.polymarket.com/market-makers/inventory#batch-operations)
- [Next Steps](https://docs.polymarket.com/market-makers/inventory#next-steps)

Market makers need outcome tokens on both sides to quote a market. The three core inventory operations are **splitting** USDC.e into YES/NO token pairs, **merging** pairs back into USDC.e, and **redeeming** winning tokens after resolution — all executed gaslessly through the Relayer Client.

For a full breakdown of how the Conditional Token Framework works, see [CTF\\
Overview](https://docs.polymarket.com/trading/ctf/overview). This page focuses on the MM workflow using
the Relayer Client.

* * *

## [​](https://docs.polymarket.com/market-makers/inventory\#splitting-usdc-e-into-tokens)  Splitting USDC.e into Tokens

Split converts USDC.e into equal amounts of YES and NO tokens — creating the inventory you need to quote both sides of a market.

TypeScript

Python

Rust

Copy

Ask AI

```
import { ethers } from "ethers";
import { Interface } from "ethers/lib/utils";
import { RelayClient, Transaction } from "@polymarket/builder-relayer-client";

const CTF_ADDRESS = "0x4D97DCd97eC945f40cF65F87097ACe5EA0476045";
const USDCe_ADDRESS = "0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174";

const ctfInterface = new Interface([\
  "function splitPosition(address collateralToken, bytes32 parentCollectionId, bytes32 conditionId, uint[] partition, uint amount)",\
]);

// Split $1000 USDCe into YES/NO tokens
const amount = ethers.utils.parseUnits("1000", 6); // USDCe has 6 decimals

const splitTx: Transaction = {
  to: CTF_ADDRESS,
  data: ctfInterface.encodeFunctionData("splitPosition", [\
    USDCe_ADDRESS, // collateralToken\
    ethers.constants.HashZero, // parentCollectionId (always zero for Polymarket)\
    conditionId, // conditionId from market\
    [1, 2], // partition: [YES, NO]\
    amount,\
  ]),
  value: "0",
};

const response = await client.execute([splitTx], "Split USDCe into tokens");
const result = await response.wait();
console.log("Split completed:", result?.transactionHash);
```

After splitting 1000 USDC.e, you receive 1000 YES tokens and 1000 NO tokens. Your USDC.e balance decreases by 1000.

* * *

## [​](https://docs.polymarket.com/market-makers/inventory\#merging-tokens-to-usdc-e)  Merging Tokens to USDC.e

Merge converts equal amounts of YES and NO tokens back into USDC.e — useful for reducing exposure, exiting a market, or freeing up capital.

TypeScript

Python

Rust

Copy

Ask AI

```
const ctfInterface = new Interface([\
  "function mergePositions(address collateralToken, bytes32 parentCollectionId, bytes32 conditionId, uint[] partition, uint amount)",\
]);

// Merge 500 YES + 500 NO back to 500 USDCe
const amount = ethers.utils.parseUnits("500", 6);

const mergeTx: Transaction = {
  to: CTF_ADDRESS,
  data: ctfInterface.encodeFunctionData("mergePositions", [\
    USDCe_ADDRESS,\
    ethers.constants.HashZero,\
    conditionId,\
    [1, 2],\
    amount,\
  ]),
  value: "0",
};

const response = await client.execute([mergeTx], "Merge tokens to USDCe");
await response.wait();
```

After merging 500 of each, your YES and NO balances decrease by 500 and your USDC.e balance increases by 500.

* * *

## [​](https://docs.polymarket.com/market-makers/inventory\#redeeming-after-resolution)  Redeeming After Resolution

Once a market resolves, redeem winning tokens for USDC.e. Each winning token is worth 1—losingtokensredeemfor1 — losing tokens redeem for 1—losingtokensredeemfor0.

### [​](https://docs.polymarket.com/market-makers/inventory\#check-resolution-status)  Check Resolution Status

TypeScript

Python

Rust

Copy

Ask AI

```
const market = await clobClient.getMarket(conditionId);
if (market.closed) {
  const winningToken = market.tokens.find((t) => t.winner);
  console.log("Winning outcome:", winningToken?.outcome);
}
```

### [​](https://docs.polymarket.com/market-makers/inventory\#redeem-winning-tokens)  Redeem Winning Tokens

TypeScript

Python

Rust

Copy

Ask AI

```
const ctfInterface = new Interface([\
  "function redeemPositions(address collateralToken, bytes32 parentCollectionId, bytes32 conditionId, uint[] indexSets)",\
]);

const redeemTx: Transaction = {
  to: CTF_ADDRESS,
  data: ctfInterface.encodeFunctionData("redeemPositions", [\
    USDCe_ADDRESS,\
    ethers.constants.HashZero,\
    conditionId,\
    [1, 2], // Redeem both YES and NO (only winners pay out)\
  ]),
  value: "0",
};

const response = await client.execute([redeemTx], "Redeem winning tokens");
await response.wait();
```

* * *

## [​](https://docs.polymarket.com/market-makers/inventory\#negative-risk-markets)  Negative Risk Markets

Multi-outcome markets use the Neg Risk CTF Exchange. Split and merge work the same way, but use different contract addresses:

Copy

Ask AI

```
const NEG_RISK_ADAPTER = "0xd91E80cF2E7be2e162c6513ceD06f1dD0dA35296";
const NEG_RISK_CTF_EXCHANGE = "0xC5d563A36AE78145C45a50134d48A1215220f80a";
```

See [Negative Risk Markets](https://docs.polymarket.com/advanced/neg-risk) for details on how multi-outcome token mechanics differ.

* * *

## [​](https://docs.polymarket.com/market-makers/inventory\#inventory-strategies)  Inventory Strategies

### [​](https://docs.polymarket.com/market-makers/inventory\#before-quoting)  Before Quoting

1. Check market metadata via the [Gamma API](https://docs.polymarket.com/market-data/fetching-markets)
2. Split sufficient USDC.e to cover your expected quoting size
3. Set token approvals if not already done (see [Getting Started](https://docs.polymarket.com/market-makers/getting-started))

### [​](https://docs.polymarket.com/market-makers/inventory\#during-trading)  During Trading

- **Skew quotes** when inventory becomes imbalanced on one side
- **Merge excess tokens** to free up capital for other markets
- **Split more** when inventory on either side runs low

### [​](https://docs.polymarket.com/market-makers/inventory\#after-resolution)  After Resolution

1. Cancel all open orders in the market
2. Wait for resolution to complete
3. Redeem winning tokens
4. Merge any remaining YES/NO pairs

* * *

## [​](https://docs.polymarket.com/market-makers/inventory\#batch-operations)  Batch Operations

Execute multiple inventory operations in a single relayer call for efficiency:

Copy

Ask AI

```
const transactions: Transaction[] = [\
  // Split on Market A\
  {\
    to: CTF_ADDRESS,\
    data: ctfInterface.encodeFunctionData("splitPosition", [\
      USDCe_ADDRESS,\
      ethers.constants.HashZero,\
      conditionIdA,\
      [1, 2],\
      ethers.utils.parseUnits("1000", 6),\
    ]),\
    value: "0",\
  },\
  // Split on Market B\
  {\
    to: CTF_ADDRESS,\
    data: ctfInterface.encodeFunctionData("splitPosition", [\
      USDCe_ADDRESS,\
      ethers.constants.HashZero,\
      conditionIdB,\
      [1, 2],\
      ethers.utils.parseUnits("1000", 6),\
    ]),\
    value: "0",\
  },\
];

const response = await client.execute(transactions, "Batch inventory setup");
await response.wait();
```

* * *

## [​](https://docs.polymarket.com/market-makers/inventory\#next-steps)  Next Steps

[**CTF Overview** \\
\\
How the Conditional Token Framework works under the hood](https://docs.polymarket.com/trading/ctf/overview)

[**Split Tokens** \\
\\
Detailed split function parameters and prerequisites](https://docs.polymarket.com/trading/ctf/split)

[**Merge Tokens** \\
\\
Detailed merge function parameters](https://docs.polymarket.com/trading/ctf/merge)

[**Gasless Transactions** \\
\\
Relayer Client setup and configuration](https://docs.polymarket.com/trading/gasless)

Was this page helpful?

YesNo

[Trading\\
\\
Previous](https://docs.polymarket.com/market-makers/trading) [Builder Program\\
\\
Next](https://docs.polymarket.com/builders/overview)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.

Suggestions

How do I connect to WebSocket streams?What's required to place my first order?How do I find and fetch market data?