---
url: "https://docs.polymarket.com/trading/clients/l2"
title: "L2 Methods - Polymarket Documentation"
---

[Skip to main content](https://docs.polymarket.com/trading/clients/l2#content-area)

[Polymarket Documentation home page![light logo](https://mintcdn.com/polymarket-292d1b1b/ZibMe6Tli_amZald/logo/light.svg?fit=max&auto=format&n=ZibMe6Tli_amZald&q=85&s=9f9bd559f02181495794661ef6426c0f)![dark logo](https://mintcdn.com/polymarket-292d1b1b/ZibMe6Tli_amZald/logo/dark.svg?fit=max&auto=format&n=ZibMe6Tli_amZald&q=85&s=13abc6754579a3475368ea99d0f5a241)](https://docs.polymarket.com/)

![US](https://d3gk2c5xim1je2.cloudfront.net/flags/US.svg)

English

Search...

Ctrl KAsk AI

Search...

Navigation

Client Reference

L2 Methods

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

- [Client Initialization](https://docs.polymarket.com/trading/clients/l2#client-initialization)
- [Order Creation and Management](https://docs.polymarket.com/trading/clients/l2#order-creation-and-management)
- [createAndPostOrder](https://docs.polymarket.com/trading/clients/l2#createandpostorder)
- [createAndPostMarketOrder](https://docs.polymarket.com/trading/clients/l2#createandpostmarketorder)
- [postOrder](https://docs.polymarket.com/trading/clients/l2#postorder)
- [postOrders](https://docs.polymarket.com/trading/clients/l2#postorders)
- [cancelOrder](https://docs.polymarket.com/trading/clients/l2#cancelorder)
- [cancelOrders](https://docs.polymarket.com/trading/clients/l2#cancelorders)
- [cancelAll](https://docs.polymarket.com/trading/clients/l2#cancelall)
- [cancelMarketOrders](https://docs.polymarket.com/trading/clients/l2#cancelmarketorders)
- [Order and Trade Queries](https://docs.polymarket.com/trading/clients/l2#order-and-trade-queries)
- [getOrder](https://docs.polymarket.com/trading/clients/l2#getorder)
- [getOpenOrders](https://docs.polymarket.com/trading/clients/l2#getopenorders)
- [getTrades](https://docs.polymarket.com/trading/clients/l2#gettrades)
- [getTradesPaginated](https://docs.polymarket.com/trading/clients/l2#gettradespaginated)
- [Balance and Allowances](https://docs.polymarket.com/trading/clients/l2#balance-and-allowances)
- [getBalanceAllowance](https://docs.polymarket.com/trading/clients/l2#getbalanceallowance)
- [updateBalanceAllowance](https://docs.polymarket.com/trading/clients/l2#updatebalanceallowance)
- [API Key Management](https://docs.polymarket.com/trading/clients/l2#api-key-management)
- [getApiKeys](https://docs.polymarket.com/trading/clients/l2#getapikeys)
- [deleteApiKey](https://docs.polymarket.com/trading/clients/l2#deleteapikey)
- [Notifications](https://docs.polymarket.com/trading/clients/l2#notifications)
- [getNotifications](https://docs.polymarket.com/trading/clients/l2#getnotifications)
- [dropNotifications](https://docs.polymarket.com/trading/clients/l2#dropnotifications)
- [See Also](https://docs.polymarket.com/trading/clients/l2#see-also)

## [​](https://docs.polymarket.com/trading/clients/l2\#client-initialization)  Client Initialization

L2 methods require the client to initialize with a signer, signature type, API credentials, and funder address.

- TypeScript

- Python


Copy

Ask AI

```
import { ClobClient } from "@polymarket/clob-client";
import { Wallet } from "ethers";

const signer = new Wallet(process.env.PRIVATE_KEY);

const apiCreds = {
  apiKey: process.env.API_KEY,
  secret: process.env.SECRET,
  passphrase: process.env.PASSPHRASE,
};

const client = new ClobClient(
  "https://clob.polymarket.com",
  137,
  signer,
  apiCreds,
  2, // GNOSIS_SAFE
  process.env.FUNDER_ADDRESS
);

// Ready to send authenticated requests
const order = await client.postOrder(signedOrder);
```

Copy

Ask AI

```
from py_clob_client.client import ClobClient
from py_clob_client.clob_types import ApiCreds
import os

api_creds = ApiCreds(
    api_key=os.getenv("API_KEY"),
    api_secret=os.getenv("SECRET"),
    api_passphrase=os.getenv("PASSPHRASE")
)

client = ClobClient(
    host="https://clob.polymarket.com",
    chain_id=137,
    key=os.getenv("PRIVATE_KEY"),
    creds=api_creds,
    signature_type=2,  # GNOSIS_SAFE
    funder=os.getenv("FUNDER_ADDRESS")
)

# Ready to send authenticated requests
order = client.post_order(signed_order)
```

* * *

## [​](https://docs.polymarket.com/trading/clients/l2\#order-creation-and-management)  Order Creation and Management

* * *

### [​](https://docs.polymarket.com/trading/clients/l2\#createandpostorder)  createAndPostOrder

Convenience method that creates, signs, and posts a limit order in a single call. Use when you want to buy or sell at a specific price.

Signature

Copy

Ask AI

```
async createAndPostOrder(
  userOrder: UserOrder,
  options?: Partial<CreateOrderOptions>,
  orderType?: OrderType.GTC | OrderType.GTD, // Defaults to GTC
): Promise<OrderResponse>
```

**Params**

[​](https://docs.polymarket.com/trading/clients/l2#param-token-id)

tokenID

string

The token ID of the outcome to trade.

[​](https://docs.polymarket.com/trading/clients/l2#param-price)

price

number

The limit price for the order.

[​](https://docs.polymarket.com/trading/clients/l2#param-size)

size

number

The size of the order.

[​](https://docs.polymarket.com/trading/clients/l2#param-side)

side

Side

The side of the order (buy or sell).

[​](https://docs.polymarket.com/trading/clients/l2#param-fee-rate-bps)

feeRateBps

number

Optional fee rate in basis points.

[​](https://docs.polymarket.com/trading/clients/l2#param-nonce)

nonce

number

Optional nonce for the order.

[​](https://docs.polymarket.com/trading/clients/l2#param-expiration)

expiration

number

Optional expiration timestamp for the order.

[​](https://docs.polymarket.com/trading/clients/l2#param-taker)

taker

string

Optional taker address.

[​](https://docs.polymarket.com/trading/clients/l2#param-tick-size)

tickSize

TickSize

Tick size for the order. One of `"0.1"`, `"0.01"`, `"0.001"`, `"0.0001"`.

[​](https://docs.polymarket.com/trading/clients/l2#param-neg-risk)

negRisk

boolean

Optional. Whether the market uses negative risk.

**Response**

[​](https://docs.polymarket.com/trading/clients/l2#param-success)

success

boolean

Whether the order was successfully placed.

[​](https://docs.polymarket.com/trading/clients/l2#param-error-msg)

errorMsg

string

Error message if the order was not successful.

[​](https://docs.polymarket.com/trading/clients/l2#param-order-id)

orderID

string

The ID of the placed order.

[​](https://docs.polymarket.com/trading/clients/l2#param-transactions-hashes)

transactionsHashes

string\[\]

Array of transaction hashes associated with the order.

[​](https://docs.polymarket.com/trading/clients/l2#param-status)

status

string

The current status of the order.

[​](https://docs.polymarket.com/trading/clients/l2#param-taking-amount)

takingAmount

string

The amount being taken in the order.

[​](https://docs.polymarket.com/trading/clients/l2#param-making-amount)

makingAmount

string

The amount being made in the order.

* * *

### [​](https://docs.polymarket.com/trading/clients/l2\#createandpostmarketorder)  createAndPostMarketOrder

Convenience method that creates, signs, and posts a market order in a single call. Use when you want to buy or sell at the current market price.

Signature

Copy

Ask AI

```
async createAndPostMarketOrder(
  userMarketOrder: UserMarketOrder,
  options?: Partial<CreateOrderOptions>,
  orderType?: OrderType.FOK | OrderType.FAK, // Defaults to FOK
): Promise<OrderResponse>
```

**Params**

[​](https://docs.polymarket.com/trading/clients/l2#param-token-id-1)

tokenID

string

The token ID of the outcome to trade.

[​](https://docs.polymarket.com/trading/clients/l2#param-amount)

amount

number

The amount for the market order.

[​](https://docs.polymarket.com/trading/clients/l2#param-side-1)

side

Side

The side of the order (buy or sell).

[​](https://docs.polymarket.com/trading/clients/l2#param-price-1)

price

number

Optional price hint for the market order.

[​](https://docs.polymarket.com/trading/clients/l2#param-fee-rate-bps-1)

feeRateBps

number

Optional fee rate in basis points.

[​](https://docs.polymarket.com/trading/clients/l2#param-nonce-1)

nonce

number

Optional nonce for the order.

[​](https://docs.polymarket.com/trading/clients/l2#param-taker-1)

taker

string

Optional taker address.

[​](https://docs.polymarket.com/trading/clients/l2#param-order-type)

orderType

OrderType.FOK \| OrderType.FAK

Optional order type override. Defaults to FOK.

**Response**

[​](https://docs.polymarket.com/trading/clients/l2#param-success-1)

success

boolean

Whether the order was successfully placed.

[​](https://docs.polymarket.com/trading/clients/l2#param-error-msg-1)

errorMsg

string

Error message if the order was not successful.

[​](https://docs.polymarket.com/trading/clients/l2#param-order-id-1)

orderID

string

The ID of the placed order.

[​](https://docs.polymarket.com/trading/clients/l2#param-transactions-hashes-1)

transactionsHashes

string\[\]

Array of transaction hashes associated with the order.

[​](https://docs.polymarket.com/trading/clients/l2#param-status-1)

status

string

The current status of the order.

[​](https://docs.polymarket.com/trading/clients/l2#param-taking-amount-1)

takingAmount

string

The amount being taken in the order.

[​](https://docs.polymarket.com/trading/clients/l2#param-making-amount-1)

makingAmount

string

The amount being made in the order.

* * *

### [​](https://docs.polymarket.com/trading/clients/l2\#postorder)  postOrder

Posts a pre-signed order to the CLOB. Use with [`createOrder()`](https://docs.polymarket.com/trading/clients/l1#createorder) or [`createMarketOrder()`](https://docs.polymarket.com/trading/clients/l1#createmarketorder) from L1 methods.

Signature

Copy

Ask AI

```
async postOrder(
  order: SignedOrder,
  orderType?: OrderType, // Defaults to GTC
  postOnly?: boolean,    // Defaults to false
): Promise<OrderResponse>
```

* * *

### [​](https://docs.polymarket.com/trading/clients/l2\#postorders)  postOrders

Posts up to 15 pre-signed orders in a single batch.

Signature

Copy

Ask AI

```
async postOrders(
  args: PostOrdersArgs[],
): Promise<OrderResponse[]>
```

**Params**

[​](https://docs.polymarket.com/trading/clients/l2#param-order)

order

SignedOrder

The pre-signed order to post.

[​](https://docs.polymarket.com/trading/clients/l2#param-order-type-1)

orderType

OrderType

The order type (e.g. GTC, FOK, FAK).

[​](https://docs.polymarket.com/trading/clients/l2#param-post-only)

postOnly

boolean

Optional. Whether to post the order as post-only. Defaults to false.

* * *

### [​](https://docs.polymarket.com/trading/clients/l2\#cancelorder)  cancelOrder

Cancels a single open order.

Signature

Copy

Ask AI

```
async cancelOrder(orderID: string): Promise<CancelOrdersResponse>
```

**Response**

[​](https://docs.polymarket.com/trading/clients/l2#param-canceled)

canceled

string\[\]

Array of order IDs that were successfully canceled.

[​](https://docs.polymarket.com/trading/clients/l2#param-not-canceled)

not\_canceled

Record<string, any>

Map of order IDs to reasons why they could not be canceled.

* * *

### [​](https://docs.polymarket.com/trading/clients/l2\#cancelorders)  cancelOrders

Cancels multiple orders in a single batch.

Signature

Copy

Ask AI

```
async cancelOrders(orderIDs: string[]): Promise<CancelOrdersResponse>
```

* * *

### [​](https://docs.polymarket.com/trading/clients/l2\#cancelall)  cancelAll

Cancels all open orders.

Signature

Copy

Ask AI

```
async cancelAll(): Promise<CancelOrdersResponse>
```

* * *

### [​](https://docs.polymarket.com/trading/clients/l2\#cancelmarketorders)  cancelMarketOrders

Cancels all open orders for a specific market.

Signature

Copy

Ask AI

```
async cancelMarketOrders(
  payload: OrderMarketCancelParams
): Promise<CancelOrdersResponse>
```

**Params**

[​](https://docs.polymarket.com/trading/clients/l2#param-market)

market

string

Optional. The market condition ID to cancel orders for.

[​](https://docs.polymarket.com/trading/clients/l2#param-asset-id)

asset\_id

string

Optional. The token ID to cancel orders for.

* * *

## [​](https://docs.polymarket.com/trading/clients/l2\#order-and-trade-queries)  Order and Trade Queries

* * *

### [​](https://docs.polymarket.com/trading/clients/l2\#getorder)  getOrder

Get details for a specific order by ID.

Signature

Copy

Ask AI

```
async getOrder(orderID: string): Promise<OpenOrder>
```

**Response**

[​](https://docs.polymarket.com/trading/clients/l2#param-id)

id

string

The unique order ID.

[​](https://docs.polymarket.com/trading/clients/l2#param-status-2)

status

string

The current status of the order.

[​](https://docs.polymarket.com/trading/clients/l2#param-owner)

owner

string

The API key of the order owner.

[​](https://docs.polymarket.com/trading/clients/l2#param-maker-address)

maker\_address

string

The on-chain address of the order maker.

[​](https://docs.polymarket.com/trading/clients/l2#param-market-1)

market

string

The market condition ID the order belongs to.

[​](https://docs.polymarket.com/trading/clients/l2#param-asset-id-1)

asset\_id

string

The token ID the order is for.

[​](https://docs.polymarket.com/trading/clients/l2#param-side-2)

side

string

The side of the order (BUY or SELL).

[​](https://docs.polymarket.com/trading/clients/l2#param-original-size)

original\_size

string

The original size of the order when it was placed.

[​](https://docs.polymarket.com/trading/clients/l2#param-size-matched)

size\_matched

string

The amount of the order that has been matched so far.

[​](https://docs.polymarket.com/trading/clients/l2#param-price-2)

price

string

The limit price of the order.

[​](https://docs.polymarket.com/trading/clients/l2#param-associate-trades)

associate\_trades

string\[\]

Array of trade IDs associated with this order.

[​](https://docs.polymarket.com/trading/clients/l2#param-outcome)

outcome

string

The outcome label for the order’s token.

[​](https://docs.polymarket.com/trading/clients/l2#param-created-at)

created\_at

number

Unix timestamp of when the order was created.

[​](https://docs.polymarket.com/trading/clients/l2#param-expiration-1)

expiration

string

The expiration time of the order.

[​](https://docs.polymarket.com/trading/clients/l2#param-order-type)

order\_type

string

The order type (e.g. GTC, FOK, FAK, GTD).

* * *

### [​](https://docs.polymarket.com/trading/clients/l2\#getopenorders)  getOpenOrders

Get all your open orders.

Signature

Copy

Ask AI

```
async getOpenOrders(
  params?: OpenOrderParams,
  only_first_page?: boolean,
): Promise<OpenOrder[]>
```

**Params**

[​](https://docs.polymarket.com/trading/clients/l2#param-id-1)

id

string

Optional. Filter by order ID.

[​](https://docs.polymarket.com/trading/clients/l2#param-market-2)

market

string

Optional. Filter by market condition ID.

[​](https://docs.polymarket.com/trading/clients/l2#param-asset-id-2)

asset\_id

string

Optional. Filter by token ID.

* * *

### [​](https://docs.polymarket.com/trading/clients/l2\#gettrades)  getTrades

Get your trade history (filled orders).

Signature

Copy

Ask AI

```
async getTrades(
  params?: TradeParams,
  only_first_page?: boolean,
): Promise<Trade[]>
```

**Params**

[​](https://docs.polymarket.com/trading/clients/l2#param-id-2)

id

string

Optional. Filter by trade ID.

[​](https://docs.polymarket.com/trading/clients/l2#param-maker-address-1)

maker\_address

string

Optional. Filter by maker address.

[​](https://docs.polymarket.com/trading/clients/l2#param-market-3)

market

string

Optional. Filter by market condition ID.

[​](https://docs.polymarket.com/trading/clients/l2#param-asset-id-3)

asset\_id

string

Optional. Filter by token ID.

[​](https://docs.polymarket.com/trading/clients/l2#param-before)

before

string

Optional. Return trades before this timestamp.

[​](https://docs.polymarket.com/trading/clients/l2#param-after)

after

string

Optional. Return trades after this timestamp.

**Response**

[​](https://docs.polymarket.com/trading/clients/l2#param-id-3)

id

string

The unique trade ID.

[​](https://docs.polymarket.com/trading/clients/l2#param-taker-order-id)

taker\_order\_id

string

The order ID of the taker side.

[​](https://docs.polymarket.com/trading/clients/l2#param-market-4)

market

string

The market condition ID for the trade.

[​](https://docs.polymarket.com/trading/clients/l2#param-asset-id-4)

asset\_id

string

The token ID for the trade.

[​](https://docs.polymarket.com/trading/clients/l2#param-side-3)

side

Side

The side of the trade (BUY or SELL).

[​](https://docs.polymarket.com/trading/clients/l2#param-size-1)

size

string

The size of the trade.

[​](https://docs.polymarket.com/trading/clients/l2#param-fee-rate-bps)

fee\_rate\_bps

string

The fee rate in basis points.

[​](https://docs.polymarket.com/trading/clients/l2#param-price-3)

price

string

The price at which the trade was matched.

[​](https://docs.polymarket.com/trading/clients/l2#param-status-3)

status

string

The current status of the trade.

[​](https://docs.polymarket.com/trading/clients/l2#param-match-time)

match\_time

string

The time at which the trade was matched.

[​](https://docs.polymarket.com/trading/clients/l2#param-last-update)

last\_update

string

The time of the last update to this trade.

[​](https://docs.polymarket.com/trading/clients/l2#param-outcome-1)

outcome

string

The outcome label for the traded token.

[​](https://docs.polymarket.com/trading/clients/l2#param-bucket-index)

bucket\_index

number

The bucket index for the trade.

[​](https://docs.polymarket.com/trading/clients/l2#param-owner-1)

owner

string

The API key of the trade owner.

[​](https://docs.polymarket.com/trading/clients/l2#param-maker-address-2)

maker\_address

string

The on-chain address of the maker.

[​](https://docs.polymarket.com/trading/clients/l2#param-maker-orders)

maker\_orders

MakerOrder\[\]

Array of maker order objects that participated in this trade. Each `MakerOrder` contains the following fields:

[​](https://docs.polymarket.com/trading/clients/l2#param-maker-orders-order-id)

maker\_orders\[\].order\_id

string

The maker order ID.

[​](https://docs.polymarket.com/trading/clients/l2#param-maker-orders-owner)

maker\_orders\[\].owner

string

The API key of the maker order owner.

[​](https://docs.polymarket.com/trading/clients/l2#param-maker-orders-maker-address)

maker\_orders\[\].maker\_address

string

The on-chain address of the maker order maker.

[​](https://docs.polymarket.com/trading/clients/l2#param-maker-orders-matched-amount)

maker\_orders\[\].matched\_amount

string

The amount matched for this maker order.

[​](https://docs.polymarket.com/trading/clients/l2#param-maker-orders-price)

maker\_orders\[\].price

string

The price of the maker order.

[​](https://docs.polymarket.com/trading/clients/l2#param-maker-orders-fee-rate-bps)

maker\_orders\[\].fee\_rate\_bps

string

The fee rate in basis points for the maker order.

[​](https://docs.polymarket.com/trading/clients/l2#param-maker-orders-asset-id)

maker\_orders\[\].asset\_id

string

The token ID for the maker order.

[​](https://docs.polymarket.com/trading/clients/l2#param-maker-orders-outcome)

maker\_orders\[\].outcome

string

The outcome label for the maker order’s token.

[​](https://docs.polymarket.com/trading/clients/l2#param-maker-orders-side)

maker\_orders\[\].side

Side

The side of the maker order (BUY or SELL).

[​](https://docs.polymarket.com/trading/clients/l2#param-transaction-hash)

transaction\_hash

string

The on-chain transaction hash for the trade.

[​](https://docs.polymarket.com/trading/clients/l2#param-trader-side)

trader\_side

"TAKER" \| "MAKER"

Whether the authenticated user is the taker or a maker in this trade.

* * *

### [​](https://docs.polymarket.com/trading/clients/l2\#gettradespaginated)  getTradesPaginated

Get trade history with pagination for large result sets.

Signature

Copy

Ask AI

```
async getTradesPaginated(
  params?: TradeParams,
): Promise<TradesPaginatedResponse>
```

**Response**

[​](https://docs.polymarket.com/trading/clients/l2#param-trades)

trades

Trade\[\]

Array of trade objects for the current page.

[​](https://docs.polymarket.com/trading/clients/l2#param-limit)

limit

number

The maximum number of trades returned per page.

[​](https://docs.polymarket.com/trading/clients/l2#param-count)

count

number

The total number of trades matching the query.

* * *

## [​](https://docs.polymarket.com/trading/clients/l2\#balance-and-allowances)  Balance and Allowances

* * *

### [​](https://docs.polymarket.com/trading/clients/l2\#getbalanceallowance)  getBalanceAllowance

Get your balance and allowance for specific tokens.

Signature

Copy

Ask AI

```
async getBalanceAllowance(
  params?: BalanceAllowanceParams
): Promise<BalanceAllowanceResponse>
```

**Params**

[​](https://docs.polymarket.com/trading/clients/l2#param-asset-type)

asset\_type

AssetType

The type of asset to query. One of `"COLLATERAL"` or `"CONDITIONAL"`.

[​](https://docs.polymarket.com/trading/clients/l2#param-token-id)

token\_id

string

Optional. The token ID to query (required when `asset_type` is `CONDITIONAL`).

**Response**

[​](https://docs.polymarket.com/trading/clients/l2#param-balance)

balance

string

The current balance for the specified asset.

[​](https://docs.polymarket.com/trading/clients/l2#param-allowance)

allowance

string

The current allowance for the specified asset.

* * *

### [​](https://docs.polymarket.com/trading/clients/l2\#updatebalanceallowance)  updateBalanceAllowance

Updates the cached balance and allowance for specific tokens.

Signature

Copy

Ask AI

```
async updateBalanceAllowance(
  params?: BalanceAllowanceParams
): Promise<void>
```

* * *

## [​](https://docs.polymarket.com/trading/clients/l2\#api-key-management)  API Key Management

* * *

### [​](https://docs.polymarket.com/trading/clients/l2\#getapikeys)  getApiKeys

Get all API keys associated with your account.

Signature

Copy

Ask AI

```
async getApiKeys(): Promise<ApiKeysResponse>
```

**Response**

[​](https://docs.polymarket.com/trading/clients/l2#param-api-keys)

apiKeys

ApiKeyCreds\[\]

Array of API key credential objects associated with the account.

* * *

### [​](https://docs.polymarket.com/trading/clients/l2\#deleteapikey)  deleteApiKey

Deletes (revokes) the currently authenticated API key.

Signature

Copy

Ask AI

```
async deleteApiKey(): Promise<any>
```

* * *

## [​](https://docs.polymarket.com/trading/clients/l2\#notifications)  Notifications

* * *

### [​](https://docs.polymarket.com/trading/clients/l2\#getnotifications)  getNotifications

Retrieves all event notifications for the authenticated user. Records are automatically removed after 48 hours.

Signature

Copy

Ask AI

```
async getNotifications(): Promise<Notification[]>
```

**Response**

[​](https://docs.polymarket.com/trading/clients/l2#param-id-4)

id

number

Unique notification ID.

[​](https://docs.polymarket.com/trading/clients/l2#param-owner-2)

owner

string

The user’s API key, or an empty string for global notifications.

[​](https://docs.polymarket.com/trading/clients/l2#param-payload)

payload

any

Type-specific payload data for the notification.

[​](https://docs.polymarket.com/trading/clients/l2#param-timestamp)

timestamp

number

Optional Unix timestamp of when the notification was created.

[​](https://docs.polymarket.com/trading/clients/l2#param-type)

type

number

Notification type (see below).

| Name | Value | Description |
| --- | --- | --- |
| Order Cancellation | `1` | User’s order was canceled |
| Order Fill | `2` | User’s order was filled (maker or taker) |
| Market Resolved | `4` | Market was resolved |

* * *

### [​](https://docs.polymarket.com/trading/clients/l2\#dropnotifications)  dropNotifications

Mark notifications as read/dismissed.

Signature

Copy

Ask AI

```
async dropNotifications(params?: DropNotificationParams): Promise<void>
```

**Params**

[​](https://docs.polymarket.com/trading/clients/l2#param-ids)

ids

string\[\]

Array of notification IDs to dismiss.

* * *

## [​](https://docs.polymarket.com/trading/clients/l2\#see-also)  See Also

[**Authentication** \\
\\
Deep dive into L1 and L2 authentication.](https://docs.polymarket.com/api-reference/authentication)

[**L1 Methods** \\
\\
Sign orders and derive API credentials with your private key.](https://docs.polymarket.com/trading/clients/l1)

[**Public Methods** \\
\\
Read market data and orderbooks without auth.](https://docs.polymarket.com/trading/clients/public)

[**WebSocket** \\
\\
Real-time market data streaming.](https://docs.polymarket.com/market-data/websocket/overview)

Was this page helpful?

YesNo

[L1 Methods\\
\\
Previous](https://docs.polymarket.com/trading/clients/l1) [Builder Methods\\
\\
Next](https://docs.polymarket.com/trading/clients/builder)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.

Suggestions

How do I connect to WebSocket streams?What's required to place my first order?How do I find and fetch market data?