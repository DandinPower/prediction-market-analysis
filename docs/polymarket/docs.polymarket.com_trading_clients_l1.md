---
url: "https://docs.polymarket.com/trading/clients/l1"
title: "L1 Methods - Polymarket Documentation"
---

[Skip to main content](https://docs.polymarket.com/trading/clients/l1#content-area)

[Polymarket Documentation home page![light logo](https://mintcdn.com/polymarket-292d1b1b/ZibMe6Tli_amZald/logo/light.svg?fit=max&auto=format&n=ZibMe6Tli_amZald&q=85&s=9f9bd559f02181495794661ef6426c0f)![dark logo](https://mintcdn.com/polymarket-292d1b1b/ZibMe6Tli_amZald/logo/dark.svg?fit=max&auto=format&n=ZibMe6Tli_amZald&q=85&s=13abc6754579a3475368ea99d0f5a241)](https://docs.polymarket.com/)

![US](https://d3gk2c5xim1je2.cloudfront.net/flags/US.svg)

English

Search...

Ctrl KAsk AI

Search...

Navigation

Client Reference

L1 Methods

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

  - [Public Methods](https://docs.polymarket.com/trading/clients/public)
  - [L1 Methods](https://docs.polymarket.com/trading/clients/l1)
  - [L2 Methods](https://docs.polymarket.com/trading/clients/l2)
  - [Builder Methods](https://docs.polymarket.com/trading/clients/builder)
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

- [Client Initialization](https://docs.polymarket.com/trading/clients/l1#client-initialization)
- [API Key Management](https://docs.polymarket.com/trading/clients/l1#api-key-management)
- [createApiKey](https://docs.polymarket.com/trading/clients/l1#createapikey)
- [deriveApiKey](https://docs.polymarket.com/trading/clients/l1#deriveapikey)
- [createOrDeriveApiKey](https://docs.polymarket.com/trading/clients/l1#createorderiveapikey)
- [Order Signing](https://docs.polymarket.com/trading/clients/l1#order-signing)
- [createOrder](https://docs.polymarket.com/trading/clients/l1#createorder)
- [createMarketOrder](https://docs.polymarket.com/trading/clients/l1#createmarketorder)
- [Troubleshooting](https://docs.polymarket.com/trading/clients/l1#troubleshooting)
- [See Also](https://docs.polymarket.com/trading/clients/l1#see-also)

## [​](https://docs.polymarket.com/trading/clients/l1\#client-initialization)  Client Initialization

L1 methods require the client to initialize with a signer.

- TypeScript

- Python


Copy

Ask AI

```
import { ClobClient } from "@polymarket/clob-client";
import { Wallet } from "ethers";

const signer = new Wallet(process.env.PRIVATE_KEY);

const client = new ClobClient(
  "https://clob.polymarket.com",
  137,
  signer // Signer required for L1 methods
);

// Ready to create user API credentials
const apiKey = await client.createApiKey();
```

Copy

Ask AI

```
from py_clob_client.client import ClobClient
import os

private_key = os.getenv("PRIVATE_KEY")

client = ClobClient(
    host="https://clob.polymarket.com",
    chain_id=137,
    key=private_key  # Signer required for L1 methods
)

# Ready to create user API credentials
api_key = client.create_api_key()
```

Never commit private keys to version control. Always use environment variables or a secure key management system.

* * *

## [​](https://docs.polymarket.com/trading/clients/l1\#api-key-management)  API Key Management

* * *

### [​](https://docs.polymarket.com/trading/clients/l1\#createapikey)  createApiKey

Creates a new API key (L2 credentials) for the wallet signer. Each wallet can only have one active API key at a time — creating a new key invalidates the previous one.

Signature

Copy

Ask AI

```
async createApiKey(nonce?: number): Promise<ApiKeyCreds>
```

[​](https://docs.polymarket.com/trading/clients/l1#param-nonce)

nonce

number

Optional custom nonce for deterministic key generation. Optional.

[​](https://docs.polymarket.com/trading/clients/l1#param-api-key)

apiKey

string

The generated API key string.

[​](https://docs.polymarket.com/trading/clients/l1#param-secret)

secret

string

The secret associated with the API key.

[​](https://docs.polymarket.com/trading/clients/l1#param-passphrase)

passphrase

string

The passphrase associated with the API key.

* * *

### [​](https://docs.polymarket.com/trading/clients/l1\#deriveapikey)  deriveApiKey

Derives an existing API key using a specific nonce. If you’ve already created credentials with a particular nonce, this returns the same credentials.

Signature

Copy

Ask AI

```
async deriveApiKey(nonce?: number): Promise<ApiKeyCreds>
```

[​](https://docs.polymarket.com/trading/clients/l1#param-nonce-1)

nonce

number

The nonce used when originally creating the key. Optional.

[​](https://docs.polymarket.com/trading/clients/l1#param-api-key-1)

apiKey

string

The derived API key string.

[​](https://docs.polymarket.com/trading/clients/l1#param-secret-1)

secret

string

The secret associated with the API key.

[​](https://docs.polymarket.com/trading/clients/l1#param-passphrase-1)

passphrase

string

The passphrase associated with the API key.

* * *

### [​](https://docs.polymarket.com/trading/clients/l1\#createorderiveapikey)  createOrDeriveApiKey

Convenience method that attempts to derive an API key with the default nonce, or creates a new one if it doesn’t exist. **Recommended for initial setup.**

Signature

Copy

Ask AI

```
async createOrDeriveApiKey(nonce?: number): Promise<ApiKeyCreds>
```

[​](https://docs.polymarket.com/trading/clients/l1#param-api-key-2)

apiKey

string

The API key string, either derived or newly created.

[​](https://docs.polymarket.com/trading/clients/l1#param-secret-2)

secret

string

The secret associated with the API key.

[​](https://docs.polymarket.com/trading/clients/l1#param-passphrase-2)

passphrase

string

The passphrase associated with the API key.

* * *

## [​](https://docs.polymarket.com/trading/clients/l1\#order-signing)  Order Signing

### [​](https://docs.polymarket.com/trading/clients/l1\#createorder)  createOrder

Create and sign a limit order locally without posting it to the CLOB. Use this when you want to sign orders in advance or implement custom submission logic. Submit via [`postOrder()`](https://docs.polymarket.com/trading/clients/l2#postorder) or [`postOrders()`](https://docs.polymarket.com/trading/clients/l2#postorders).

Signature

Copy

Ask AI

```
async createOrder(
  userOrder: UserOrder,
  options?: Partial<CreateOrderOptions>
): Promise<SignedOrder>
```

[​](https://docs.polymarket.com/trading/clients/l1#param-token-id)

tokenID

string

The token ID of the market outcome to trade.

[​](https://docs.polymarket.com/trading/clients/l1#param-price)

price

number

The limit price for the order.

[​](https://docs.polymarket.com/trading/clients/l1#param-size)

size

number

The size (number of shares) for the order.

[​](https://docs.polymarket.com/trading/clients/l1#param-side)

side

Side

The side of the order (buy or sell).

[​](https://docs.polymarket.com/trading/clients/l1#param-fee-rate-bps)

feeRateBps

number

Optional fee rate in basis points. Optional.

[​](https://docs.polymarket.com/trading/clients/l1#param-nonce-2)

nonce

number

Optional nonce for the order. Optional.

[​](https://docs.polymarket.com/trading/clients/l1#param-expiration)

expiration

number

Optional expiration timestamp for the order. Optional.

[​](https://docs.polymarket.com/trading/clients/l1#param-taker)

taker

string

Optional taker address for the order. Optional.

[​](https://docs.polymarket.com/trading/clients/l1#param-tick-size)

tickSize

TickSize

The tick size used for order validation (CreateOrderOptions).

[​](https://docs.polymarket.com/trading/clients/l1#param-neg-risk)

negRisk

boolean

Optional flag for negative risk markets (CreateOrderOptions). Optional.

[​](https://docs.polymarket.com/trading/clients/l1#param-salt)

salt

string

A random salt value for the signed order.

[​](https://docs.polymarket.com/trading/clients/l1#param-maker)

maker

string

The maker’s address.

[​](https://docs.polymarket.com/trading/clients/l1#param-signer)

signer

string

The signer’s address.

[​](https://docs.polymarket.com/trading/clients/l1#param-taker-1)

taker

string

The taker’s address in the signed order.

[​](https://docs.polymarket.com/trading/clients/l1#param-token-id)

tokenId

string

The token ID in the signed order.

[​](https://docs.polymarket.com/trading/clients/l1#param-maker-amount)

makerAmount

string

The maker amount as a string.

[​](https://docs.polymarket.com/trading/clients/l1#param-taker-amount)

takerAmount

string

The taker amount as a string.

[​](https://docs.polymarket.com/trading/clients/l1#param-side-1)

side

number

The side of the order as a number (0 = BUY, 1 = SELL).

[​](https://docs.polymarket.com/trading/clients/l1#param-expiration-1)

expiration

string

The expiration timestamp as a string.

[​](https://docs.polymarket.com/trading/clients/l1#param-nonce-3)

nonce

string

The nonce as a string.

[​](https://docs.polymarket.com/trading/clients/l1#param-fee-rate-bps-1)

feeRateBps

string

The fee rate in basis points as a string.

[​](https://docs.polymarket.com/trading/clients/l1#param-signature-type)

signatureType

number

The type identifier for the signature scheme used.

[​](https://docs.polymarket.com/trading/clients/l1#param-signature)

signature

string

The cryptographic signature of the order.

* * *

### [​](https://docs.polymarket.com/trading/clients/l1\#createmarketorder)  createMarketOrder

Create and sign a market order locally without posting it to the CLOB. Submit via [`postOrder()`](https://docs.polymarket.com/trading/clients/l2#postorder) or [`postOrders()`](https://docs.polymarket.com/trading/clients/l2#postorders).

Signature

Copy

Ask AI

```
async createMarketOrder(
  userMarketOrder: UserMarketOrder,
  options?: Partial<CreateOrderOptions>
): Promise<SignedOrder>
```

[​](https://docs.polymarket.com/trading/clients/l1#param-token-id-1)

tokenID

string

The token ID of the market outcome to trade.

[​](https://docs.polymarket.com/trading/clients/l1#param-amount)

amount

number

The order amount. For BUY orders this is a dollar amount; for SELL orders this is the number of shares.

[​](https://docs.polymarket.com/trading/clients/l1#param-side-2)

side

Side

The side of the order (buy or sell).

[​](https://docs.polymarket.com/trading/clients/l1#param-price-1)

price

number

Optional price limit for the market order. Optional.

[​](https://docs.polymarket.com/trading/clients/l1#param-fee-rate-bps-2)

feeRateBps

number

Optional fee rate in basis points. Optional.

[​](https://docs.polymarket.com/trading/clients/l1#param-nonce-4)

nonce

number

Optional nonce for the order. Optional.

[​](https://docs.polymarket.com/trading/clients/l1#param-taker-2)

taker

string

Optional taker address for the order. Optional.

[​](https://docs.polymarket.com/trading/clients/l1#param-order-type)

orderType

OrderType.FOK \| OrderType.FAK

Optional order type, either FOK (Fill-Or-Kill) or FAK (Fill-And-Kill). Optional.

[​](https://docs.polymarket.com/trading/clients/l1#param-salt-1)

salt

string

A random salt value for the signed order.

[​](https://docs.polymarket.com/trading/clients/l1#param-maker-1)

maker

string

The maker’s address.

[​](https://docs.polymarket.com/trading/clients/l1#param-signer-1)

signer

string

The signer’s address.

[​](https://docs.polymarket.com/trading/clients/l1#param-taker-3)

taker

string

The taker’s address in the signed order.

[​](https://docs.polymarket.com/trading/clients/l1#param-token-id-1)

tokenId

string

The token ID in the signed order.

[​](https://docs.polymarket.com/trading/clients/l1#param-maker-amount-1)

makerAmount

string

The maker amount as a string.

[​](https://docs.polymarket.com/trading/clients/l1#param-taker-amount-1)

takerAmount

string

The taker amount as a string.

[​](https://docs.polymarket.com/trading/clients/l1#param-side-3)

side

number

The side of the order as a number (0 = BUY, 1 = SELL).

[​](https://docs.polymarket.com/trading/clients/l1#param-expiration-2)

expiration

string

The expiration timestamp as a string.

[​](https://docs.polymarket.com/trading/clients/l1#param-nonce-5)

nonce

string

The nonce as a string.

[​](https://docs.polymarket.com/trading/clients/l1#param-fee-rate-bps-3)

feeRateBps

string

The fee rate in basis points as a string.

[​](https://docs.polymarket.com/trading/clients/l1#param-signature-type-1)

signatureType

number

The type identifier for the signature scheme used.

[​](https://docs.polymarket.com/trading/clients/l1#param-signature-1)

signature

string

The cryptographic signature of the order.

* * *

## [​](https://docs.polymarket.com/trading/clients/l1\#troubleshooting)  Troubleshooting

Error - INVALID\_SIGNATURE

Your wallet’s private key is incorrect or improperly formatted.**Solution:**

- Verify your private key is a valid hex string (starts with `0x`)
- Ensure you’re using the correct key for the intended address
- Check that the key has proper permissions

Error - NONCE\_ALREADY\_USED

The nonce you provided has already been used to create an API key.**Solution:**

- Use `deriveApiKey()` with the same nonce to retrieve existing credentials
- Or use a different nonce with `createApiKey()`

Error - Invalid Funder Address

Your funder address is incorrect or doesn’t match your wallet.**Solution:** Check your proxy wallet address at [polymarket.com/settings](https://polymarket.com/settings). If it doesn’t exist, the user has never logged in to Polymarket.com — deploy the proxy wallet first before creating L2 credentials.

Lost API credentials but have nonce

Copy

Ask AI

```
// Use deriveApiKey with the original nonce
const recovered = await client.deriveApiKey(originalNonce);
```

Lost both credentials and nonce

There’s no way to recover lost credentials without the nonce. Create new ones:

Copy

Ask AI

```
// Create fresh credentials with a new nonce
const newCreds = await client.createApiKey();
// Save the nonce this time!
```

* * *

## [​](https://docs.polymarket.com/trading/clients/l1\#see-also)  See Also

[**Authentication** \\
\\
Deep dive into L1 and L2 authentication.](https://docs.polymarket.com/api-reference/authentication)

[**Trading Quickstart** \\
\\
Initialize the client and place your first order.](https://docs.polymarket.com/trading/quickstart)

[**Public Methods** \\
\\
Access market data, orderbooks, and prices without auth.](https://docs.polymarket.com/trading/clients/public)

[**L2 Methods** \\
\\
Place and manage orders with API credentials.](https://docs.polymarket.com/trading/clients/l2)

Was this page helpful?

YesNo

[Public Methods\\
\\
Previous](https://docs.polymarket.com/trading/clients/public) [L2 Methods\\
\\
Next](https://docs.polymarket.com/trading/clients/l2)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.

Suggestions

How do I connect to WebSocket streams?What's required to place my first order?How do I find and fetch market data?