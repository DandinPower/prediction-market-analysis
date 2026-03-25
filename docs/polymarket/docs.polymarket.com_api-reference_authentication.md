---
url: "https://docs.polymarket.com/api-reference/authentication"
title: "Authentication - Polymarket Documentation"
---

[Skip to main content](https://docs.polymarket.com/api-reference/authentication#content-area)

[Polymarket Documentation home page![light logo](https://mintcdn.com/polymarket-292d1b1b/ZibMe6Tli_amZald/logo/light.svg?fit=max&auto=format&n=ZibMe6Tli_amZald&q=85&s=9f9bd559f02181495794661ef6426c0f)![dark logo](https://mintcdn.com/polymarket-292d1b1b/ZibMe6Tli_amZald/logo/dark.svg?fit=max&auto=format&n=ZibMe6Tli_amZald&q=85&s=13abc6754579a3475368ea99d0f5a241)](https://docs.polymarket.com/)

![US](https://d3gk2c5xim1je2.cloudfront.net/flags/US.svg)

English

Search...

Ctrl KAsk AI

Search...

Navigation

Overview

Authentication

[Documentation](https://docs.polymarket.com/) [API Reference](https://docs.polymarket.com/api-reference/introduction)

##### Overview

- [Introduction](https://docs.polymarket.com/api-reference/introduction)
- [Authentication](https://docs.polymarket.com/api-reference/authentication)
- [Rate Limits](https://docs.polymarket.com/api-reference/rate-limits)
- [Clients & SDKs](https://docs.polymarket.com/api-reference/clients-sdks)
- [Geographic Restrictions](https://docs.polymarket.com/api-reference/geoblock)

##### Events

- [GET\\
\\
List events](https://docs.polymarket.com/api-reference/events/list-events)
- [GET\\
\\
Get event by id](https://docs.polymarket.com/api-reference/events/get-event-by-id)
- [GET\\
\\
Get event by slug](https://docs.polymarket.com/api-reference/events/get-event-by-slug)
- [GET\\
\\
Get event tags](https://docs.polymarket.com/api-reference/events/get-event-tags)

##### Markets

- [GET\\
\\
List markets](https://docs.polymarket.com/api-reference/markets/list-markets)
- [GET\\
\\
Get market by id](https://docs.polymarket.com/api-reference/markets/get-market-by-id)
- [GET\\
\\
Get market by slug](https://docs.polymarket.com/api-reference/markets/get-market-by-slug)
- [GET\\
\\
Get market tags by id](https://docs.polymarket.com/api-reference/markets/get-market-tags-by-id)
- [GET\\
\\
Get top holders for markets](https://docs.polymarket.com/api-reference/core/get-top-holders-for-markets)
- [GET\\
\\
Get open interest](https://docs.polymarket.com/api-reference/misc/get-open-interest)
- [GET\\
\\
Get live volume for an event](https://docs.polymarket.com/api-reference/misc/get-live-volume-for-an-event)

##### Orderbook & Pricing

- [GET\\
\\
Get order book](https://docs.polymarket.com/api-reference/market-data/get-order-book)
- [POST\\
\\
Get order books (request body)](https://docs.polymarket.com/api-reference/market-data/get-order-books-request-body)
- [GET\\
\\
Get market price](https://docs.polymarket.com/api-reference/market-data/get-market-price)
- [GET\\
\\
Get market prices (query parameters)](https://docs.polymarket.com/api-reference/market-data/get-market-prices-query-parameters)
- [POST\\
\\
Get market prices (request body)](https://docs.polymarket.com/api-reference/market-data/get-market-prices-request-body)
- [GET\\
\\
Get midpoint price](https://docs.polymarket.com/api-reference/data/get-midpoint-price)
- [GET\\
\\
Get midpoint prices (query parameters)](https://docs.polymarket.com/api-reference/market-data/get-midpoint-prices-query-parameters)
- [POST\\
\\
Get midpoint prices (request body)](https://docs.polymarket.com/api-reference/market-data/get-midpoint-prices-request-body)
- [GET\\
\\
Get spread](https://docs.polymarket.com/api-reference/market-data/get-spread)
- [POST\\
\\
Get spreads](https://docs.polymarket.com/api-reference/market-data/get-spreads)
- [GET\\
\\
Get last trade price](https://docs.polymarket.com/api-reference/market-data/get-last-trade-price)
- [GET\\
\\
Get last trade prices (query parameters)](https://docs.polymarket.com/api-reference/market-data/get-last-trade-prices-query-parameters)
- [POST\\
\\
Get last trade prices (request body)](https://docs.polymarket.com/api-reference/market-data/get-last-trade-prices-request-body)
- [GET\\
\\
Get prices history](https://docs.polymarket.com/api-reference/markets/get-prices-history)
- [GET\\
\\
Get fee rate](https://docs.polymarket.com/api-reference/market-data/get-fee-rate)
- [GET\\
\\
Get fee rate by path parameter](https://docs.polymarket.com/api-reference/market-data/get-fee-rate-by-path-parameter)
- [GET\\
\\
Get tick size](https://docs.polymarket.com/api-reference/market-data/get-tick-size)
- [GET\\
\\
Get tick size by path parameter](https://docs.polymarket.com/api-reference/market-data/get-tick-size-by-path-parameter)
- [GET\\
\\
Get server time](https://docs.polymarket.com/api-reference/data/get-server-time)

##### Orders

- [POST\\
\\
Post a new order](https://docs.polymarket.com/api-reference/trade/post-a-new-order)
- [DEL\\
\\
Cancel single order](https://docs.polymarket.com/api-reference/trade/cancel-single-order)
- [GET\\
\\
Get single order by ID](https://docs.polymarket.com/api-reference/trade/get-single-order-by-id)
- [POST\\
\\
Post multiple orders](https://docs.polymarket.com/api-reference/trade/post-multiple-orders)
- [GET\\
\\
Get user orders](https://docs.polymarket.com/api-reference/trade/get-user-orders)
- [DEL\\
\\
Cancel multiple orders](https://docs.polymarket.com/api-reference/trade/cancel-multiple-orders)
- [DEL\\
\\
Cancel all orders](https://docs.polymarket.com/api-reference/trade/cancel-all-orders)
- [DEL\\
\\
Cancel orders for a market](https://docs.polymarket.com/api-reference/trade/cancel-orders-for-a-market)
- [GET\\
\\
Get order scoring status](https://docs.polymarket.com/api-reference/trade/get-order-scoring-status)
- [POST\\
\\
Send heartbeat](https://docs.polymarket.com/api-reference/trade/send-heartbeat)

##### Trades

- [GET\\
\\
Get trades](https://docs.polymarket.com/api-reference/trade/get-trades)
- [GET\\
\\
Get builder trades](https://docs.polymarket.com/api-reference/trade/get-builder-trades)

##### CLOB Markets

- [GET\\
\\
Get simplified markets](https://docs.polymarket.com/api-reference/markets/get-simplified-markets)
- [GET\\
\\
Get sampling markets](https://docs.polymarket.com/api-reference/markets/get-sampling-markets)
- [GET\\
\\
Get sampling simplified markets](https://docs.polymarket.com/api-reference/markets/get-sampling-simplified-markets)

##### Rebates

- [GET\\
\\
Get current rebated fees for a maker](https://docs.polymarket.com/api-reference/rebates/get-current-rebated-fees-for-a-maker)

##### Rewards

- [GET\\
\\
Get current active rewards configurations](https://docs.polymarket.com/api-reference/rewards/get-current-active-rewards-configurations)
- [GET\\
\\
Get raw rewards for a specific market](https://docs.polymarket.com/api-reference/rewards/get-raw-rewards-for-a-specific-market)
- [GET\\
\\
Get multiple markets with rewards](https://docs.polymarket.com/api-reference/rewards/get-multiple-markets-with-rewards)
- [GET\\
\\
Get earnings for user by date](https://docs.polymarket.com/api-reference/rewards/get-earnings-for-user-by-date)
- [GET\\
\\
Get total earnings for user by date](https://docs.polymarket.com/api-reference/rewards/get-total-earnings-for-user-by-date)
- [GET\\
\\
Get reward percentages for user](https://docs.polymarket.com/api-reference/rewards/get-reward-percentages-for-user)
- [GET\\
\\
Get user earnings and markets configuration](https://docs.polymarket.com/api-reference/rewards/get-user-earnings-and-markets-configuration)

##### Profile

- [GET\\
\\
Get public profile by wallet address](https://docs.polymarket.com/api-reference/profiles/get-public-profile-by-wallet-address)
- [GET\\
\\
Get current positions for a user](https://docs.polymarket.com/api-reference/core/get-current-positions-for-a-user)
- [GET\\
\\
Get closed positions for a user](https://docs.polymarket.com/api-reference/core/get-closed-positions-for-a-user)
- [GET\\
\\
Get user activity](https://docs.polymarket.com/api-reference/core/get-user-activity)
- [GET\\
\\
Get total value of a user's positions](https://docs.polymarket.com/api-reference/core/get-total-value-of-a-users-positions)
- [GET\\
\\
Get trades for a user or markets](https://docs.polymarket.com/api-reference/core/get-trades-for-a-user-or-markets)
- [GET\\
\\
Get total markets a user has traded](https://docs.polymarket.com/api-reference/misc/get-total-markets-a-user-has-traded)
- [GET\\
\\
Get positions for a market](https://docs.polymarket.com/api-reference/core/get-positions-for-a-market)
- [GET\\
\\
Download an accounting snapshot (ZIP of CSVs)](https://docs.polymarket.com/api-reference/misc/download-an-accounting-snapshot-zip-of-csvs)

##### Leaderboard

- [GET\\
\\
Get trader leaderboard rankings](https://docs.polymarket.com/api-reference/core/get-trader-leaderboard-rankings)

##### Builders

- [GET\\
\\
Get aggregated builder leaderboard](https://docs.polymarket.com/api-reference/builders/get-aggregated-builder-leaderboard)
- [GET\\
\\
Get daily builder volume time-series](https://docs.polymarket.com/api-reference/builders/get-daily-builder-volume-time-series)

##### Search

- [GET\\
\\
Search markets, events, and profiles](https://docs.polymarket.com/api-reference/search/search-markets-events-and-profiles)

##### Tags

- [GET\\
\\
List tags](https://docs.polymarket.com/api-reference/tags/list-tags)
- [GET\\
\\
Get tag by id](https://docs.polymarket.com/api-reference/tags/get-tag-by-id)
- [GET\\
\\
Get tag by slug](https://docs.polymarket.com/api-reference/tags/get-tag-by-slug)
- [GET\\
\\
Get related tags (relationships) by tag id](https://docs.polymarket.com/api-reference/tags/get-related-tags-relationships-by-tag-id)
- [GET\\
\\
Get related tags (relationships) by tag slug](https://docs.polymarket.com/api-reference/tags/get-related-tags-relationships-by-tag-slug)
- [GET\\
\\
Get tags related to a tag id](https://docs.polymarket.com/api-reference/tags/get-tags-related-to-a-tag-id)
- [GET\\
\\
Get tags related to a tag slug](https://docs.polymarket.com/api-reference/tags/get-tags-related-to-a-tag-slug)

##### Series

- [GET\\
\\
List series](https://docs.polymarket.com/api-reference/series/list-series)
- [GET\\
\\
Get series by id](https://docs.polymarket.com/api-reference/series/get-series-by-id)

##### Comments

- [GET\\
\\
List comments](https://docs.polymarket.com/api-reference/comments/list-comments)
- [GET\\
\\
Get comments by comment id](https://docs.polymarket.com/api-reference/comments/get-comments-by-comment-id)
- [GET\\
\\
Get comments by user address](https://docs.polymarket.com/api-reference/comments/get-comments-by-user-address)

##### Sports

- [GET\\
\\
Get sports metadata information](https://docs.polymarket.com/api-reference/sports/get-sports-metadata-information)
- [GET\\
\\
Get valid sports market types](https://docs.polymarket.com/api-reference/sports/get-valid-sports-market-types)
- [GET\\
\\
List teams](https://docs.polymarket.com/api-reference/sports/list-teams)

##### Bridge

- [GET\\
\\
Get supported assets](https://docs.polymarket.com/api-reference/bridge/get-supported-assets)
- [POST\\
\\
Create deposit addresses](https://docs.polymarket.com/api-reference/bridge/create-deposit-addresses)
- [POST\\
\\
Get a quote](https://docs.polymarket.com/api-reference/bridge/get-a-quote)
- [GET\\
\\
Get transaction status](https://docs.polymarket.com/api-reference/bridge/get-transaction-status)
- [POST\\
\\
Create withdrawal addresses](https://docs.polymarket.com/api-reference/bridge/create-withdrawal-addresses)

##### Relayer

- [POST\\
\\
Submit a transaction](https://docs.polymarket.com/api-reference/relayer/submit-a-transaction)
- [GET\\
\\
Get a transaction by ID](https://docs.polymarket.com/api-reference/relayer/get-a-transaction-by-id)
- [GET\\
\\
Get recent transactions for a user](https://docs.polymarket.com/api-reference/relayer/get-recent-transactions-for-a-user)
- [GET\\
\\
Get current nonce for a user](https://docs.polymarket.com/api-reference/relayer/get-current-nonce-for-a-user)
- [GET\\
\\
Get relayer address and nonce](https://docs.polymarket.com/api-reference/relayer/get-relayer-address-and-nonce)
- [GET\\
\\
Check if a safe is deployed](https://docs.polymarket.com/api-reference/relayer/check-if-a-safe-is-deployed)
- [GET\\
\\
Get all relayer API keys](https://docs.polymarket.com/api-reference/relayer-api-keys/get-all-relayer-api-keys)

##### WebSocket

- [WSS\\
\\
Market Channel](https://docs.polymarket.com/api-reference/wss/market)
- [WSS\\
\\
User Channel](https://docs.polymarket.com/api-reference/wss/user)
- [WSS\\
\\
Sports Channel](https://docs.polymarket.com/api-reference/wss/sports)

On this page

- [Public vs Authenticated](https://docs.polymarket.com/api-reference/authentication#public-vs-authenticated)
- [Two-Level Authentication Model](https://docs.polymarket.com/api-reference/authentication#two-level-authentication-model)
- [L1 Authentication](https://docs.polymarket.com/api-reference/authentication#l1-authentication)
- [L2 Authentication](https://docs.polymarket.com/api-reference/authentication#l2-authentication)
- [Getting API Credentials](https://docs.polymarket.com/api-reference/authentication#getting-api-credentials)
- [Using the SDK](https://docs.polymarket.com/api-reference/authentication#using-the-sdk)
- [Using the REST API](https://docs.polymarket.com/api-reference/authentication#using-the-rest-api)
- [L2 Authentication Headers](https://docs.polymarket.com/api-reference/authentication#l2-authentication-headers)
- [CLOB Client](https://docs.polymarket.com/api-reference/authentication#clob-client)
- [Signature Types and Funder](https://docs.polymarket.com/api-reference/authentication#signature-types-and-funder)
- [Security Best Practices](https://docs.polymarket.com/api-reference/authentication#security-best-practices)
- [Troubleshooting](https://docs.polymarket.com/api-reference/authentication#troubleshooting)
- [Next Steps](https://docs.polymarket.com/api-reference/authentication#next-steps)

The CLOB API uses two levels of authentication: **L1 (Private Key)** and **L2 (API Key)**. Either can be accomplished using the CLOB client or REST API.

## [​](https://docs.polymarket.com/api-reference/authentication\#public-vs-authenticated)  Public vs Authenticated

## Public (No Auth)

The **Gamma API**, **Data API**, and CLOB read endpoints (orderbook, prices, spreads) require no authentication.

## Authenticated (CLOB)

CLOB trading endpoints (placing orders, cancellations, heartbeat) require all 5 `POLY_*` L2 HTTP headers.

* * *

## [​](https://docs.polymarket.com/api-reference/authentication\#two-level-authentication-model)  Two-Level Authentication Model

The CLOB uses two levels of authentication: L1 (Private Key) and L2 (API Key). Either can be accomplished using the CLOB client or REST API

### [​](https://docs.polymarket.com/api-reference/authentication\#l1-authentication)  L1 Authentication

L1 authentication uses the wallet’s private key to sign an EIP-712 message used in the request header. It proves ownership and control over the private key. The private key stays in control of the user and all trading activity remains non-custodial.**Used for:**

- Creating API credentials
- Deriving existing API credentials
- Signing and creating user’s orders locally

### [​](https://docs.polymarket.com/api-reference/authentication\#l2-authentication)  L2 Authentication

L2 uses API credentials (apiKey, secret, passphrase) generated from L1 authentication. These are used solely to authenticate requests made to the CLOB API. Requests are signed using HMAC-SHA256.**Used for:**

- Cancel or get user’s open orders
- Check user’s balances and allowances
- Post user’s signed orders

Even with L2 authentication headers, methods that create user orders still
require the user to sign the order payload.

* * *

## [​](https://docs.polymarket.com/api-reference/authentication\#getting-api-credentials)  Getting API Credentials

Before making authenticated requests, you need to obtain API credentials using L1 authentication.

### [​](https://docs.polymarket.com/api-reference/authentication\#using-the-sdk)  Using the SDK

- TypeScript

- Python

- Rust


Copy

Ask AI

```
import { ClobClient } from "@polymarket/clob-client";
import { Wallet } from "ethers"; // v5.8.0

const client = new ClobClient(
  "https://clob.polymarket.com",
  137, // Polygon mainnet
  new Wallet(process.env.PRIVATE_KEY)
);

// Creates new credentials or derives existing ones
const credentials = await client.createOrDeriveApiKey();

console.log(credentials);
// {
//   apiKey: "550e8400-e29b-41d4-a716-446655440000",
//   secret: "base64EncodedSecretString",
//   passphrase: "randomPassphraseString"
// }
```

Copy

Ask AI

```
from py_clob_client.client import ClobClient
import os

client = ClobClient(
    host="https://clob.polymarket.com",
    chain_id=137,  # Polygon mainnet
    key=os.getenv("PRIVATE_KEY")
)

# Creates new credentials or derives existing ones
credentials = client.create_or_derive_api_creds()

print(credentials)
# {
#     "apiKey": "550e8400-e29b-41d4-a716-446655440000",
#     "secret": "base64EncodedSecretString",
#     "passphrase": "randomPassphraseString"
# }
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

// Creates new credentials or derives existing ones,
// then initializes the authenticated client — all in one step
let client = Client::new("https://clob.polymarket.com", Config::default())?
    .authentication_builder(&signer)
    .authenticate()
    .await?;

let credentials = client.credentials();
println!("API Key: {}", credentials.key());
```

**Never commit private keys to version control.** Always use environment
variables or secure key management systems.

### [​](https://docs.polymarket.com/api-reference/authentication\#using-the-rest-api)  Using the REST API

While we highly recommend using our provided clients to handle signing and authentication, the following is for developers who choose NOT to use our [Python](https://github.com/Polymarket/py-clob-client) or [TypeScript](https://github.com/Polymarket/clob-client) clients.**Create API Credentials**

Copy

Ask AI

```
POST https://clob.polymarket.com/auth/api-key
```

**Derive API Credentials**

Copy

Ask AI

```
GET https://clob.polymarket.com/auth/derive-api-key
```

Required L1 headers:

| Header | Description |
| --- | --- |
| `POLY_ADDRESS` | Polygon signer address |
| `POLY_SIGNATURE` | CLOB EIP-712 signature |
| `POLY_TIMESTAMP` | Current UNIX timestamp |
| `POLY_NONCE` | Nonce (default: 0) |

The `POLY_SIGNATURE` is generated by signing the following EIP-712 struct:

EIP-712 Signing Example

TypeScript

Python

Copy

Ask AI

```
const domain = {
  name: "ClobAuthDomain",
  version: "1",
  chainId: chainId, // Polygon Chain ID 137
};

const types = {
  ClobAuth: [\
    { name: "address", type: "address" },\
    { name: "timestamp", type: "string" },\
    { name: "nonce", type: "uint256" },\
    { name: "message", type: "string" },\
  ],
};

const value = {
  address: signingAddress, // The Signing address
  timestamp: ts,            // The CLOB API server timestamp
  nonce: nonce,             // The nonce used
  message: "This message attests that I control the given wallet",
};

const sig = await signer._signTypedData(domain, types, value);
```

Reference implementations:

- [TypeScript](https://github.com/Polymarket/clob-client/blob/main/src/signing/eip712.ts)
- [Python](https://github.com/Polymarket/py-clob-client/blob/main/py_clob_client/signing/eip712.py)

Response:

Copy

Ask AI

```
{
  "apiKey": "550e8400-e29b-41d4-a716-446655440000",
  "secret": "base64EncodedSecretString",
  "passphrase": "randomPassphraseString"
}
```

**You’ll need all three values for L2 authentication.**

* * *

## [​](https://docs.polymarket.com/api-reference/authentication\#l2-authentication-headers)  L2 Authentication Headers

All trading endpoints require these 5 headers:

| Header | Description |
| --- | --- |
| `POLY_ADDRESS` | Polygon signer address |
| `POLY_SIGNATURE` | HMAC signature for request |
| `POLY_TIMESTAMP` | Current UNIX timestamp |
| `POLY_API_KEY` | User’s API `apiKey` value |
| `POLY_PASSPHRASE` | User’s API `passphrase` value |

The `POLY_SIGNATURE` for L2 is an HMAC-SHA256 signature created using the user’s API credentials `secret` value. Reference implementations can be found in the [TypeScript](https://github.com/Polymarket/clob-client/blob/main/src/signing/hmac.ts) and [Python](https://github.com/Polymarket/py-clob-client/blob/main/py_clob_client/signing/hmac.py) clients.

### [​](https://docs.polymarket.com/api-reference/authentication\#clob-client)  CLOB Client

- TypeScript

- Python

- Rust


Copy

Ask AI

```
import { ClobClient } from "@polymarket/clob-client";
import { Wallet } from "ethers"; // v5.8.0

const client = new ClobClient(
  "https://clob.polymarket.com",
  137,
  new Wallet(process.env.PRIVATE_KEY),
  apiCreds, // Generated from L1 auth, API credentials enable L2 methods
  1, // signatureType explained below
  funderAddress // funder explained below
);

// Now you can trade!
const order = await client.createAndPostOrder(
  { tokenID: "123456", price: 0.65, size: 100, side: "BUY" },
  { tickSize: "0.01", negRisk: false }
);
```

Copy

Ask AI

```
from py_clob_client.client import ClobClient
import os

client = ClobClient(
    host="https://clob.polymarket.com",
    chain_id=137,
    key=os.getenv("PRIVATE_KEY"),
    creds=api_creds,  # Generated from L1 auth, API credentials enable L2 methods
    signature_type=1,  # signatureType explained below
    funder=os.getenv("FUNDER_ADDRESS") # funder explained below
)

# Now you can trade!
order = client.create_and_post_order(
    {"token_id": "123456", "price": 0.65, "size": 100, "side": "BUY"},
    {"tick_size": "0.01", "neg_risk": False}
)
```

Copy

Ask AI

```
use polymarket_client_sdk::clob::types::{Side, SignatureType};
use polymarket_client_sdk::types::dec;

let client = Client::new("https://clob.polymarket.com", Config::default())?
    .authentication_builder(&signer)
    .signature_type(SignatureType::Proxy) // signatureType explained below
    // Funder auto-derived via CREATE2 for Proxy/GnosisSafe
    .authenticate()
    .await?;

// Now you can trade!
let order = client.limit_order()
    .token_id("123456".parse()?)
    .price(dec!(0.65))
    .size(dec!(100))
    .side(Side::Buy)
    .build().await?;
let signed = client.sign(&signer, order).await?;
let response = client.post_order(signed).await?;
```

Even with L2 authentication headers, methods that create user orders still
require the user to sign the order payload.

* * *

## [​](https://docs.polymarket.com/api-reference/authentication\#signature-types-and-funder)  Signature Types and Funder

When initializing the L2 client, you must specify your wallet **signatureType** and the **funder** address which holds the funds:

| Signature Type | Value | Description |
| --- | --- | --- |
| EOA | `0` | Standard Ethereum wallet (MetaMask). Funder is the EOA address and will need POL to pay gas on transactions. |
| POLY\_PROXY | `1` | A custom proxy wallet only used with users who logged in via Magic Link email/Google. Using this requires the user to have exported their PK from Polymarket.com and imported into your app. |
| GNOSIS\_SAFE | `2` | Gnosis Safe multisig proxy wallet (most common). Use this for any new or returning user who does not fit the other 2 types. |

The wallet address displayed to the user on Polymarket.com is the proxy wallet
and should be used as the funder. These can be deterministically derived or
you can deploy them on behalf of the user. These proxy wallets are
automatically deployed for the user on their first login to Polymarket.com.

* * *

## [​](https://docs.polymarket.com/api-reference/authentication\#security-best-practices)  Security Best Practices

Never expose private keys

Store private keys in environment variables or secure key management systems. Never commit them to version control.

Copy

Ask AI

```
# .env (never commit this file)
PRIVATE_KEY=0x...
```

Implement request signing on the server

Never expose your API secret in client-side code. All authenticated requests should originate from your backend.

* * *

## [​](https://docs.polymarket.com/api-reference/authentication\#troubleshooting)  Troubleshooting

Error - INVALID\_SIGNATURE

Your wallet’s private key is incorrect or improperly formatted.**Solutions:**

- Verify your private key is a valid hex string (starts with “0x”)
- Ensure you’re using the correct key for the intended address
- Check that the key has proper permissions

Error - NONCE\_ALREADY\_USED

The nonce you provided has already been used to create an API key.**Solutions:**

- Use `deriveApiKey()` with the same nonce to retrieve existing credentials
- Or use a different nonce with `createApiKey()`

Error - Invalid Funder Address

Your funder address is incorrect or doesn’t match your wallet.**Solution:** Check your Polymarket profile address at [polymarket.com/settings](https://polymarket.com/settings).If it does not exist or user has never logged into Polymarket.com, deploy it first before creating L2 authentication.

Lost both credentials and nonce

Unfortunately, there’s no way to recover lost API credentials without the nonce. You’ll need to create new credentials:

Copy

Ask AI

```
// Create fresh credentials with a new nonce
const newCreds = await client.createApiKey();
// Save the nonce this time!
```

* * *

## [​](https://docs.polymarket.com/api-reference/authentication\#next-steps)  Next Steps

[**Place Your First Order** \\
\\
Learn how to create and submit orders.](https://docs.polymarket.com/trading/quickstart)

[**Geographic Restrictions** \\
\\
Check trading availability by region.](https://docs.polymarket.com/api-reference/geoblock)

Was this page helpful?

YesNo

[Introduction\\
\\
Previous](https://docs.polymarket.com/api-reference/introduction) [Rate Limits\\
\\
Next](https://docs.polymarket.com/api-reference/rate-limits)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.

Suggestions

How do I connect to WebSocket streams?What's required to place my first order?How do I find and fetch market data?