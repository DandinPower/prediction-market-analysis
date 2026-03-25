---
url: "https://docs.polymarket.com/trading/orders/attribution"
title: "Order Attribution - Polymarket Documentation"
---

[Skip to main content](https://docs.polymarket.com/trading/orders/attribution#content-area)

[Polymarket Documentation home page![light logo](https://mintcdn.com/polymarket-292d1b1b/ZibMe6Tli_amZald/logo/light.svg?fit=max&auto=format&n=ZibMe6Tli_amZald&q=85&s=9f9bd559f02181495794661ef6426c0f)![dark logo](https://mintcdn.com/polymarket-292d1b1b/ZibMe6Tli_amZald/logo/dark.svg?fit=max&auto=format&n=ZibMe6Tli_amZald&q=85&s=13abc6754579a3475368ea99d0f5a241)](https://docs.polymarket.com/)

![US](https://d3gk2c5xim1je2.cloudfront.net/flags/US.svg)

English

Search...

Ctrl KAsk AI

Search...

Navigation

Orders

Order Attribution

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

  - [Overview](https://docs.polymarket.com/trading/orders/overview)
  - [Create Order](https://docs.polymarket.com/trading/orders/create)
  - [Cancel Order](https://docs.polymarket.com/trading/orders/cancel)
  - [Order Attribution](https://docs.polymarket.com/trading/orders/attribution)
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

- [Builder API Credentials](https://docs.polymarket.com/trading/orders/attribution#builder-api-credentials)
- [Remote Signing](https://docs.polymarket.com/trading/orders/attribution#remote-signing)
- [Server Implementation](https://docs.polymarket.com/trading/orders/attribution#server-implementation)
- [Client Configuration](https://docs.polymarket.com/trading/orders/attribution#client-configuration)
- [Local Signing](https://docs.polymarket.com/trading/orders/attribution#local-signing)
- [Authentication Headers](https://docs.polymarket.com/trading/orders/attribution#authentication-headers)
- [Verifying Attribution](https://docs.polymarket.com/trading/orders/attribution#verifying-attribution)
- [Get Builder Trades](https://docs.polymarket.com/trading/orders/attribution#get-builder-trades)
- [Revoke Builder API Key](https://docs.polymarket.com/trading/orders/attribution#revoke-builder-api-key)
- [Troubleshooting](https://docs.polymarket.com/trading/orders/attribution#troubleshooting)
- [Next Steps](https://docs.polymarket.com/trading/orders/attribution#next-steps)

Order attribution adds builder authentication headers when placing orders through the CLOB, enabling Polymarket to credit trades to your builder account. This allows you to:

- Track volume on the [Builder Leaderboard](https://builders.polymarket.com/)
- Earn rewards through the [Builder Program](https://docs.polymarket.com/builders/overview)
- Monitor performance via the Data API

* * *

## [​](https://docs.polymarket.com/trading/orders/attribution\#builder-api-credentials)  Builder API Credentials

Each builder receives API credentials from their [Builder Profile](https://polymarket.com/settings?tab=builder):

| Credential | Description |
| --- | --- |
| `key` | Your builder API key identifier |
| `secret` | Secret key for signing requests |
| `passphrase` | Additional authentication passphrase |

Builder API credentials are **not** the same as user API credentials. Builder
credentials are for order attribution only — you still need user credentials
for authentication. Never expose builder credentials in client-side code or
commit them to version control.

* * *

## [​](https://docs.polymarket.com/trading/orders/attribution\#remote-signing)  Remote Signing

Remote signing keeps your builder credentials secure on a server you control. The user’s client sends order details to your server, which adds the builder headers before forwarding to the CLOB.

### [​](https://docs.polymarket.com/trading/orders/attribution\#server-implementation)  Server Implementation

Your signing server receives request details and returns the authentication headers:

TypeScript

Python

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

// POST /sign - receives { method, path, body } from the client SDK
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

### [​](https://docs.polymarket.com/trading/orders/attribution\#client-configuration)  Client Configuration

Point the CLOB client to your signing server:

TypeScript

Python

Rust

Copy

Ask AI

```
import { ClobClient } from "@polymarket/clob-client";
import { BuilderConfig } from "@polymarket/builder-signing-sdk";

const builderConfig = new BuilderConfig({
  remoteBuilderConfig: {
    url: "https://your-server.com/sign",
    token: "optional-auth-token", // optional
  },
});

const client = new ClobClient(
  "https://clob.polymarket.com",
  137,
  signer,
  apiCreds,
  2, // signature type
  funderAddress,
  undefined,
  false,
  builderConfig,
);

// Orders automatically include builder headers
const response = await client.createAndPostOrder(/* ... */);
```

* * *

## [​](https://docs.polymarket.com/trading/orders/attribution\#local-signing)  Local Signing

Sign orders locally when you control the entire order placement flow (e.g., your backend places orders on behalf of users):

TypeScript

Python

Rust

Copy

Ask AI

```
import { ClobClient } from "@polymarket/clob-client";
import {
  BuilderConfig,
  BuilderApiKeyCreds,
} from "@polymarket/builder-signing-sdk";

const builderCreds: BuilderApiKeyCreds = {
  key: process.env.POLY_BUILDER_API_KEY!,
  secret: process.env.POLY_BUILDER_SECRET!,
  passphrase: process.env.POLY_BUILDER_PASSPHRASE!,
};

const builderConfig = new BuilderConfig({
  localBuilderCreds: builderCreds,
});

const client = new ClobClient(
  "https://clob.polymarket.com",
  137,
  signer,
  apiCreds,
  2,
  funderAddress,
  undefined,
  false,
  builderConfig,
);

// Orders automatically include builder headers
const response = await client.createAndPostOrder(/* ... */);
```

* * *

## [​](https://docs.polymarket.com/trading/orders/attribution\#authentication-headers)  Authentication Headers

The SDK automatically generates and attaches these headers to each request:

| Header | Description |
| --- | --- |
| `POLY_BUILDER_API_KEY` | Your builder API key |
| `POLY_BUILDER_TIMESTAMP` | Unix timestamp of signature creation |
| `POLY_BUILDER_PASSPHRASE` | Your builder passphrase |
| `POLY_BUILDER_SIGNATURE` | HMAC signature of the request |

With **local signing**, the SDK constructs and attaches these headers
automatically. With **remote signing**, your server returns these headers and
the SDK attaches them.

* * *

## [​](https://docs.polymarket.com/trading/orders/attribution\#verifying-attribution)  Verifying Attribution

### [​](https://docs.polymarket.com/trading/orders/attribution\#get-builder-trades)  Get Builder Trades

Query trades attributed to your builder account to verify attribution is working:

TypeScript

Python

Rust

Copy

Ask AI

```
const trades = await client.getBuilderTrades();

// Filtered by market
const marketTrades = await client.getBuilderTrades({
  market: "0xbd31dc8a...",
});
```

Each `BuilderTrade` includes: `id`, `market`, `assetId`, `side`, `size`, `price`, `status`, `outcome`, `owner`, `maker`, `transactionHash`, `matchTime`, `fee`, and `feeUsdc`.

### [​](https://docs.polymarket.com/trading/orders/attribution\#revoke-builder-api-key)  Revoke Builder API Key

If your credentials are compromised, revoke them immediately:

TypeScript

Python

Rust

Copy

Ask AI

```
await client.revokeBuilderApiKey();
```

After revoking, generate new credentials from your [Builder Profile](https://polymarket.com/settings?tab=builder).

* * *

## [​](https://docs.polymarket.com/trading/orders/attribution\#troubleshooting)  Troubleshooting

Invalid Signature Errors

- Verify the request body is passed correctly as JSON - Check that `path`,
`body`, and `method` match what the client sends - Ensure your server and
client use the same Builder API credentials

Missing Credentials

Ensure your environment variables are set: - `POLY_BUILDER_API_KEY` -
`POLY_BUILDER_SECRET` \- `POLY_BUILDER_PASSPHRASE`

Volume not appearing on leaderboard

- Confirm your builder credentials are valid and not revoked - Check that
orders are being placed with the builder config attached - Allow up to 24
hours for volume to appear on the leaderboard

* * *

## [​](https://docs.polymarket.com/trading/orders/attribution\#next-steps)  Next Steps

[**Builder Program** \\
\\
Learn about the Builder Program tiers and rewards](https://docs.polymarket.com/builders/overview)

[**Create Orders** \\
\\
Build, sign, and submit orders](https://docs.polymarket.com/trading/orders/create)

Was this page helpful?

YesNo

[Cancel Order\\
\\
Previous](https://docs.polymarket.com/trading/orders/cancel) [Public Methods\\
\\
Next](https://docs.polymarket.com/trading/clients/public)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.

Suggestions

How do I connect to WebSocket streams?What's required to place my first order?How do I find and fetch market data?