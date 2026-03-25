---
url: "https://docs.polymarket.com/builders/api-keys"
title: "API Keys - Polymarket Documentation"
---

[Skip to main content](https://docs.polymarket.com/builders/api-keys#content-area)

[Polymarket Documentation home page![light logo](https://mintcdn.com/polymarket-292d1b1b/ZibMe6Tli_amZald/logo/light.svg?fit=max&auto=format&n=ZibMe6Tli_amZald&q=85&s=9f9bd559f02181495794661ef6426c0f)![dark logo](https://mintcdn.com/polymarket-292d1b1b/ZibMe6Tli_amZald/logo/dark.svg?fit=max&auto=format&n=ZibMe6Tli_amZald&q=85&s=13abc6754579a3475368ea99d0f5a241)](https://docs.polymarket.com/)

![US](https://d3gk2c5xim1je2.cloudfront.net/flags/US.svg)

English

Search...

Ctrl KAsk AI

Search...

Navigation

Builder Program

API Keys

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

- [Accessing Your Builder Profile](https://docs.polymarket.com/builders/api-keys#accessing-your-builder-profile)
- [Creating API Keys](https://docs.polymarket.com/builders/api-keys#creating-api-keys)
- [Managing Keys](https://docs.polymarket.com/builders/api-keys#managing-keys)
- [Profile Settings](https://docs.polymarket.com/builders/api-keys#profile-settings)
- [Environment Variables](https://docs.polymarket.com/builders/api-keys#environment-variables)
- [Security Best Practices](https://docs.polymarket.com/builders/api-keys#security-best-practices)
- [Troubleshooting](https://docs.polymarket.com/builders/api-keys#troubleshooting)
- [Next Steps](https://docs.polymarket.com/builders/api-keys#next-steps)

Builder API keys authenticate your application with Polymarket’s relayer and enable order attribution. You’ll need these credentials to access gasless transactions and track volume.

## [​](https://docs.polymarket.com/builders/api-keys\#accessing-your-builder-profile)  Accessing Your Builder Profile

1

[Navigate to header](https://docs.polymarket.com/builders/api-keys#)

Direct Link

Go to
[polymarket.com/settings?tab=builder](https://polymarket.com/settings?tab=builder)

2

[Navigate to header](https://docs.polymarket.com/builders/api-keys#)

From Menu

Click your profile image → Select “Builders”

## [​](https://docs.polymarket.com/builders/api-keys\#creating-api-keys)  Creating API Keys

In the **Builder Keys** section of your profile:

1. Click **”\+ Create New”** to generate a new API key
2. **Copy all three values immediately** — the secret and passphrase are only shown once
3. Store them securely in your secrets manager or environment variables

Each API key includes three components:

| Component | Description | Example |
| --- | --- | --- |
| `key` | Public identifier for your builder account | `abc123-def456-...` |
| `secret` | Secret key for signing requests | `base64-encoded-secret` |
| `passphrase` | Additional authentication value | `your-passphrase` |

The `secret` and `passphrase` are only displayed once when created. If you
lose them, you’ll need to generate a new key.

## [​](https://docs.polymarket.com/builders/api-keys\#managing-keys)  Managing Keys

Create separate keys for different environments:

| Environment | Purpose |
| --- | --- |
| Development | Testing and local development |
| Staging | Pre-production testing |
| Production | Live trading |

## [​](https://docs.polymarket.com/builders/api-keys\#profile-settings)  Profile Settings

Your builder profile includes customizable settings:

| Setting | Description |
| --- | --- |
| **Profile Picture** | Displayed on the [Builder Leaderboard](https://builders.polymarket.com/) |
| **Builder Name** | Public name shown on the leaderboard |
| **Builder Address** | Your unique builder identifier (read-only) |
| **Current Tier** | Your rate limit tier: Unverified, Verified, or Partner |

## [​](https://docs.polymarket.com/builders/api-keys\#environment-variables)  Environment Variables

Store your credentials as environment variables:

- Bash

- TypeScript

- Python

- Rust


.env

Copy

Ask AI

```
POLY_BUILDER_API_KEY=your-api-key
POLY_BUILDER_SECRET=your-secret
POLY_BUILDER_PASSPHRASE=your-passphrase
```

Copy

Ask AI

```
import { BuilderApiKeyCreds } from "@polymarket/builder-signing-sdk";

const builderCreds: BuilderApiKeyCreds = {
  key: process.env.POLY_BUILDER_API_KEY!,
  secret: process.env.POLY_BUILDER_SECRET!,
  passphrase: process.env.POLY_BUILDER_PASSPHRASE!,
};
```

Copy

Ask AI

```
import os
from py_builder_signing_sdk import BuilderApiKeyCreds

builder_creds = BuilderApiKeyCreds(
    key=os.environ["POLY_BUILDER_API_KEY"],
    secret=os.environ["POLY_BUILDER_SECRET"],
    passphrase=os.environ["POLY_BUILDER_PASSPHRASE"],
)
```

Copy

Ask AI

```
use polymarket_client_sdk::auth::Credentials;

let builder_creds = Credentials::new(
    std::env::var("POLY_BUILDER_API_KEY")?.parse()?,
    std::env::var("POLY_BUILDER_SECRET")?,
    std::env::var("POLY_BUILDER_PASSPHRASE")?,
);
```

## [​](https://docs.polymarket.com/builders/api-keys\#security-best-practices)  Security Best Practices

| Practice | Description |
| --- | --- |
| **Never commit credentials** | Use `.gitignore` to exclude `.env` files |
| **Use environment variables** | Load credentials from env vars, not hardcoded strings |
| **Use a secrets manager** | AWS Secrets Manager, HashiCorp Vault, etc. for production |
| **Separate environments** | Use different keys for dev, staging, and production |
| **Monitor usage** | Check the leaderboard for unexpected volume changes |

**Never expose Builder API credentials in client-side code.** Your secret and
passphrase must stay on your server.

## [​](https://docs.polymarket.com/builders/api-keys\#troubleshooting)  Troubleshooting

Rate limit exceeded

**Cause:** You’ve exceeded your tier’s daily transaction limit.**Solution:**

- Wait until the daily limit resets
- [Contact Polymarket](https://docs.polymarket.com/builders/tiers#contact) to upgrade your tier

Lost secret or passphrase

**Cause:** The secret and passphrase are only shown once when created.**Solution:** Create a new API key. You cannot recover the original values.

## [​](https://docs.polymarket.com/builders/api-keys\#next-steps)  Next Steps

[**Attribute Orders** \\
\\
Configure your client to credit trades to your account.](https://docs.polymarket.com/trading/orders/attribution)

[**Understand Tiers** \\
\\
Learn about rate limits and how to upgrade.](https://docs.polymarket.com/builders/tiers)

Was this page helpful?

YesNo

[Builder Program\\
\\
Previous](https://docs.polymarket.com/builders/overview) [Tiers\\
\\
Next](https://docs.polymarket.com/builders/tiers)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.

Suggestions

How do I connect to WebSocket streams?What's required to place my first order?How do I find and fetch market data?