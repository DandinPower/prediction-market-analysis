---
url: "https://docs.polymarket.com/quickstart"
title: "Quickstart - Polymarket Documentation"
---

[Skip to main content](https://docs.polymarket.com/quickstart#content-area)

[Polymarket Documentation home page![light logo](https://mintcdn.com/polymarket-292d1b1b/ZibMe6Tli_amZald/logo/light.svg?fit=max&auto=format&n=ZibMe6Tli_amZald&q=85&s=9f9bd559f02181495794661ef6426c0f)![dark logo](https://mintcdn.com/polymarket-292d1b1b/ZibMe6Tli_amZald/logo/dark.svg?fit=max&auto=format&n=ZibMe6Tli_amZald&q=85&s=13abc6754579a3475368ea99d0f5a241)](https://docs.polymarket.com/)

![US](https://d3gk2c5xim1je2.cloudfront.net/flags/US.svg)

English

Search...

Ctrl KAsk AI

Search...

Navigation

Getting Started

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

- [Next Steps](https://docs.polymarket.com/quickstart#next-steps)

Get up and running with the Polymarket API in minutes — fetch market data and place your first order.

1

[Navigate to header](https://docs.polymarket.com/quickstart#)

Fetch a Market

All data endpoints are public — no API key or authentication needed. Use the markets endpoint to find a market and get its token IDs:

- cURL

- TypeScript

- Python

- Rust


Copy

Ask AI

```
curl "https://gamma-api.polymarket.com/markets?active=true&closed=false&limit=1"
```

Copy

Ask AI

```
const response = await fetch(
  "https://gamma-api.polymarket.com/markets?active=true&closed=false&limit=1"
);
const markets = await response.json();

const market = markets[0];
console.log(market.question);
console.log(market.clobTokenIds);
// ["123456...", "789012..."]  — [Yes token ID, No token ID]
```

Copy

Ask AI

```
import requests

response = requests.get(
    "https://gamma-api.polymarket.com/markets",
    params={"active": "true", "closed": "false", "limit": 1}
)
markets = response.json()

market = markets[0]
print(market["question"])
print(market["clobTokenIds"])
# ["123456...", "789012..."]  — [Yes token ID, No token ID]
```

Copy

Ask AI

```
use polymarket_client_sdk::gamma::Client;
use polymarket_client_sdk::gamma::types::request::MarketsRequest;

let client = Client::default();

let request = MarketsRequest::builder()
    .closed(false)
    .limit(1)
    .build();
let markets = client.markets(&request).await?;

let market = &markets[0];
println!("{:?}", market.question);
println!("{:?}", market.clob_token_ids);
// Some(["123456...", "789012..."])  — [Yes token ID, No token ID]
```

Save a token ID from `clobTokenIds` — you’ll need it to place an order. The first ID is the Yes token, the second is the No token. See [Fetching Markets](https://docs.polymarket.com/market-data/fetching-markets) for more strategies like fetching by slug, tag, or event.

2

[Navigate to header](https://docs.polymarket.com/quickstart#)

Install the SDK

TypeScript

Python

Rust

Copy

Ask AI

```
npm install @polymarket/clob-client ethers@5
```

3

[Navigate to header](https://docs.polymarket.com/quickstart#)

Set Up Your Client

Derive API credentials and initialize the trading client:

- TypeScript

- Python

- Rust


Copy

Ask AI

```
import { ClobClient } from "@polymarket/clob-client";
import { Wallet } from "ethers"; // v5.8.0

const HOST = "https://clob.polymarket.com";
const CHAIN_ID = 137; // Polygon mainnet
const signer = new Wallet(process.env.PRIVATE_KEY);

// Derive API credentials (L1 → L2 auth)
const tempClient = new ClobClient(HOST, CHAIN_ID, signer);
const apiCreds = await tempClient.createOrDeriveApiKey();

// Initialize trading client
const client = new ClobClient(
  HOST,
  CHAIN_ID,
  signer,
  apiCreds,
  0, // Signature type: 0 = EOA
  signer.address, // Funder address
);
```

Copy

Ask AI

```
from py_clob_client.client import ClobClient
import os

host = "https://clob.polymarket.com"
chain_id = 137  # Polygon mainnet
private_key = os.getenv("PRIVATE_KEY")

# Derive API credentials (L1 → L2 auth)
temp_client = ClobClient(host, key=private_key, chain_id=chain_id)
api_creds = temp_client.create_or_derive_api_creds()

# Initialize trading client
client = ClobClient(
    host,
    key=private_key,
    chain_id=chain_id,
    creds=api_creds,
    signature_type=0,  # Signature type: 0 = EOA
    funder="YOUR_WALLET_ADDRESS",  # Funder address
)
```

Copy

Ask AI

```
use std::str::FromStr;
use polymarket_client_sdk::POLYGON;
use polymarket_client_sdk::auth::{LocalSigner, Signer};
use polymarket_client_sdk::clob::{Client, Config};

let private_key = std::env::var("POLYMARKET_PRIVATE_KEY")?;
let signer = LocalSigner::from_str(&private_key)?
    .with_chain_id(Some(POLYGON));

// Derive API credentials and initialize trading client (L1 → L2 auth)
// Signature type defaults to EOA (0)
let client = Client::new("https://clob.polymarket.com", Config::default())?
    .authentication_builder(&signer)
    .authenticate()
    .await?;
```

This example uses an EOA wallet (signature type `0`) — your wallet pays its
own gas. Proxy wallet users (types `1` and `2`) can use Polymarket’s gasless
relayer instead. See [Authentication](https://docs.polymarket.com/api-reference/authentication) for
details on signature types.

Before trading, your funder address needs **USDC.e** (for buying outcome
tokens) and **POL** (for gas, if using EOA type `0`).

4

[Navigate to header](https://docs.polymarket.com/quickstart#)

Place an Order

Use the `token_id` from Step 1 to place a limit order:

- TypeScript

- Python

- Rust


Copy

Ask AI

```
import { Side, OrderType } from "@polymarket/clob-client";

// Fetch market details to get tick size and neg risk
const market = await client.getMarket("YOUR_CONDITION_ID");
const tickSize = String(market.minimum_tick_size);   // e.g., "0.01"
const negRisk = market.neg_risk;             // e.g., false

const response = await client.createAndPostOrder(
  {
    tokenID: "YOUR_TOKEN_ID", // From Step 1
    price: 0.50,
    size: 10,
    side: Side.BUY,
    orderType: OrderType.GTC,
  },
  {
    tickSize,
    negRisk,
  },
);

console.log("Order ID:", response.orderID);
console.log("Status:", response.status);
```

Copy

Ask AI

```
from py_clob_client.clob_types import OrderArgs, OrderType
from py_clob_client.order_builder.constants import BUY

# Fetch market details to get tick size and neg risk
market = client.get_market("YOUR_CONDITION_ID")
tick_size = str(market["minimum_tick_size"])   # e.g., "0.01"
neg_risk = market["neg_risk"]             # e.g., False

response = client.create_and_post_order(
    OrderArgs(
        token_id="YOUR_TOKEN_ID",  # From Step 1
        price=0.50,
        size=10,
        side=BUY,
        order_type=OrderType.GTC,
    ),
    options={
        "tick_size": tick_size,
        "neg_risk": neg_risk,
    },
)

print("Order ID:", response["orderID"])
print("Status:", response["status"])
```

Copy

Ask AI

```
use polymarket_client_sdk::clob::types::Side;
use polymarket_client_sdk::types::dec;

// token_id is a U256 — parse from the string returned in Step 1
let token_id = "YOUR_TOKEN_ID".parse()?;

// The Rust SDK auto-fetches tick size, neg risk, and fee rate
// No need to manually look them up — the order builder handles it
let order = client
    .limit_order()
    .token_id(token_id)
    .price(dec!(0.50))
    .size(dec!(10))
    .side(Side::Buy)
    .build()
    .await?;
let signed_order = client.sign(&signer, order).await?;
let response = client.post_order(signed_order).await?;

println!("Order ID: {}", response.order_id);
println!("Status: {:?}", response.status);
```

* * *

## [​](https://docs.polymarket.com/quickstart\#next-steps)  Next Steps

[**Authentication** \\
\\
Understand L1/L2 auth, signature types, and API credentials.](https://docs.polymarket.com/api-reference/authentication)

[**Trading Quickstart** \\
\\
Detailed trading guide with order management and troubleshooting.](https://docs.polymarket.com/trading/quickstart)

[**Fetching Markets** \\
\\
Strategies for discovering markets by slug, tag, or category.](https://docs.polymarket.com/market-data/fetching-markets)

[**Core Concepts** \\
\\
Understand markets, events, prices, and positions.](https://docs.polymarket.com/concepts/markets-events)

Was this page helpful?

YesNo

[Polymarket 101\\
\\
Previous](https://docs.polymarket.com/polymarket-101) [Markets & Events\\
\\
Next](https://docs.polymarket.com/concepts/markets-events)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.

Suggestions

How do I connect to WebSocket streams?What's required to place my first order?How do I find and fetch market data?