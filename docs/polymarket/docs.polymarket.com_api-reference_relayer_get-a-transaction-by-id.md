---
url: "https://docs.polymarket.com/api-reference/relayer/get-a-transaction-by-id"
title: "Get a transaction by ID - Polymarket Documentation"
---

[Skip to main content](https://docs.polymarket.com/api-reference/relayer/get-a-transaction-by-id#content-area)

[Polymarket Documentation home page![light logo](https://mintcdn.com/polymarket-292d1b1b/ZibMe6Tli_amZald/logo/light.svg?fit=max&auto=format&n=ZibMe6Tli_amZald&q=85&s=9f9bd559f02181495794661ef6426c0f)![dark logo](https://mintcdn.com/polymarket-292d1b1b/ZibMe6Tli_amZald/logo/dark.svg?fit=max&auto=format&n=ZibMe6Tli_amZald&q=85&s=13abc6754579a3475368ea99d0f5a241)](https://docs.polymarket.com/)

![US](https://d3gk2c5xim1je2.cloudfront.net/flags/US.svg)

English

Search...

Ctrl KAsk AI

Search...

Navigation

Relayer

Get a transaction by ID

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

Get a transaction by ID

cURL

Copy

Ask AI

```
curl --request GET \
  --url https://relayer-v2.polymarket.com/transaction
```

200

400

404

500

Copy

Ask AI

```
[\
  {\
    "transactionID": "0190b317-a1d3-7bec-9b91-eeb6dcd3a620",\
    "transactionHash": "0x38cbfbeae8fffa4e2b187ee5978d3ee9cafc53af0363ed90a35b7ea9016535d8",\
    "from": "0x6e0c80c90ea6c15917308f820eac91ce2724b5b5",\
    "to": "0x2791bca1f2de4661ed88a30c99a7a9449aa84174",\
    "proxyAddress": "0x6d8c4e9adf5748af82dabe2c6225207770d6b4fa",\
    "data": "0x...",\
    "nonce": "60",\
    "value": "",\
    "signature": "0x01a060c734d7bdf4adde50c4a7e574036b1f8b12890911bdd1c1cfdcd77502381b89fa8a47c36f62a0b9f1cdfee7b260fd8108536db9f6b2089c02637e7de9fc20",\
    "state": "STATE_CONFIRMED",\
    "type": "SAFE",\
    "owner": "0x6e0c80c90ea6c15917308f820eac91ce2724b5b5",\
    "metadata": "",\
    "createdAt": "2024-07-14T21:13:08.819782Z",\
    "updatedAt": "2024-07-14T21:13:46.576639Z"\
  }\
]
```

GET

/

transaction

Try it

Get a transaction by ID

cURL

Copy

Ask AI

```
curl --request GET \
  --url https://relayer-v2.polymarket.com/transaction
```

200

400

404

500

Copy

Ask AI

```
[\
  {\
    "transactionID": "0190b317-a1d3-7bec-9b91-eeb6dcd3a620",\
    "transactionHash": "0x38cbfbeae8fffa4e2b187ee5978d3ee9cafc53af0363ed90a35b7ea9016535d8",\
    "from": "0x6e0c80c90ea6c15917308f820eac91ce2724b5b5",\
    "to": "0x2791bca1f2de4661ed88a30c99a7a9449aa84174",\
    "proxyAddress": "0x6d8c4e9adf5748af82dabe2c6225207770d6b4fa",\
    "data": "0x...",\
    "nonce": "60",\
    "value": "",\
    "signature": "0x01a060c734d7bdf4adde50c4a7e574036b1f8b12890911bdd1c1cfdcd77502381b89fa8a47c36f62a0b9f1cdfee7b260fd8108536db9f6b2089c02637e7de9fc20",\
    "state": "STATE_CONFIRMED",\
    "type": "SAFE",\
    "owner": "0x6e0c80c90ea6c15917308f820eac91ce2724b5b5",\
    "metadata": "",\
    "createdAt": "2024-07-14T21:13:08.819782Z",\
    "updatedAt": "2024-07-14T21:13:46.576639Z"\
  }\
]
```

#### Query Parameters

[​](https://docs.polymarket.com/api-reference/relayer/get-a-transaction-by-id#parameter-id)

id

string

required

Transaction ID

#### Response

200

application/json

Transaction retrieved successfully

[​](https://docs.polymarket.com/api-reference/relayer/get-a-transaction-by-id#response-items-transaction-id)

transactionID

string

Unique identifier for the transaction

Example:

`"0190b317-a1d3-7bec-9b91-eeb6dcd3a620"`

[​](https://docs.polymarket.com/api-reference/relayer/get-a-transaction-by-id#response-items-transaction-hash)

transactionHash

string

Onchain transaction hash (available once confirmed)

Example:

`"0x38cbfbeae8fffa4e2b187ee5978d3ee9cafc53af0363ed90a35b7ea9016535d8"`

[​](https://docs.polymarket.com/api-reference/relayer/get-a-transaction-by-id#response-items-from)

from

string

Signer address

Pattern: `^0x[a-fA-F0-9]{40}$`

Example:

`"0x6e0c80c90ea6c15917308f820eac91ce2724b5b5"`

[​](https://docs.polymarket.com/api-reference/relayer/get-a-transaction-by-id#response-items-to)

to

string

Target contract address

Pattern: `^0x[a-fA-F0-9]{40}$`

Example:

`"0x2791bca1f2de4661ed88a30c99a7a9449aa84174"`

[​](https://docs.polymarket.com/api-reference/relayer/get-a-transaction-by-id#response-items-proxy-address)

proxyAddress

string

User's Polymarket proxy wallet address

Pattern: `^0x[a-fA-F0-9]{40}$`

Example:

`"0x6d8c4e9adf5748af82dabe2c6225207770d6b4fa"`

[​](https://docs.polymarket.com/api-reference/relayer/get-a-transaction-by-id#response-items-data)

data

string

Encoded transaction data (0x-prefixed hex string)

Example:

`"0x..."`

[​](https://docs.polymarket.com/api-reference/relayer/get-a-transaction-by-id#response-items-nonce)

nonce

string

Transaction nonce

Example:

`"60"`

[​](https://docs.polymarket.com/api-reference/relayer/get-a-transaction-by-id#response-items-value)

value

string

Transaction value

Example:

`""`

[​](https://docs.polymarket.com/api-reference/relayer/get-a-transaction-by-id#response-items-signature)

signature

string

Transaction signature (0x-prefixed hex string)

Example:

`"0x01a060c734d7bdf4adde50c4a7e574036b1f8b12890911bdd1c1cfdcd77502381b89fa8a47c36f62a0b9f1cdfee7b260fd8108536db9f6b2089c02637e7de9fc20"`

[​](https://docs.polymarket.com/api-reference/relayer/get-a-transaction-by-id#response-items-state)

state

enum<string>

Current state of the transaction

Available options:

`STATE_NEW`,

`STATE_EXECUTED`,

`STATE_MINED`,

`STATE_CONFIRMED`,

`STATE_INVALID`,

`STATE_FAILED`

Example:

`"STATE_CONFIRMED"`

[​](https://docs.polymarket.com/api-reference/relayer/get-a-transaction-by-id#response-items-type)

type

enum<string>

Transaction type

Available options:

`SAFE`,

`PROXY`

Example:

`"SAFE"`

[​](https://docs.polymarket.com/api-reference/relayer/get-a-transaction-by-id#response-items-owner)

owner

string

Owner address

Pattern: `^0x[a-fA-F0-9]{40}$`

Example:

`"0x6e0c80c90ea6c15917308f820eac91ce2724b5b5"`

[​](https://docs.polymarket.com/api-reference/relayer/get-a-transaction-by-id#response-items-metadata)

metadata

string

Transaction metadata

Example:

`""`

[​](https://docs.polymarket.com/api-reference/relayer/get-a-transaction-by-id#response-items-created-at)

createdAt

string<date-time>

Timestamp when the transaction was created

Example:

`"2024-07-14T21:13:08.819782Z"`

[​](https://docs.polymarket.com/api-reference/relayer/get-a-transaction-by-id#response-items-updated-at)

updatedAt

string<date-time>

Timestamp when the transaction was last updated

Example:

`"2024-07-14T21:13:46.576639Z"`

Was this page helpful?

YesNo

[Submit a transaction\\
\\
Previous](https://docs.polymarket.com/api-reference/relayer/submit-a-transaction) [Get recent transactions for a user\\
\\
Next](https://docs.polymarket.com/api-reference/relayer/get-recent-transactions-for-a-user)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.

Suggestions

How do I connect to WebSocket streams?What's required to place my first order?How do I find and fetch market data?