---
url: "https://docs.polymarket.com/trading/clients/public"
title: "Public Methods - Polymarket Documentation"
---

[Skip to main content](https://docs.polymarket.com/trading/clients/public#content-area)

[Polymarket Documentation home page![light logo](https://mintcdn.com/polymarket-292d1b1b/ZibMe6Tli_amZald/logo/light.svg?fit=max&auto=format&n=ZibMe6Tli_amZald&q=85&s=9f9bd559f02181495794661ef6426c0f)![dark logo](https://mintcdn.com/polymarket-292d1b1b/ZibMe6Tli_amZald/logo/dark.svg?fit=max&auto=format&n=ZibMe6Tli_amZald&q=85&s=13abc6754579a3475368ea99d0f5a241)](https://docs.polymarket.com/)

![US](https://d3gk2c5xim1je2.cloudfront.net/flags/US.svg)

English

Search...

Ctrl KAsk AI

Search...

Navigation

Client Reference

Public Methods

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

- [Client Initialization](https://docs.polymarket.com/trading/clients/public#client-initialization)
- [Health Check](https://docs.polymarket.com/trading/clients/public#health-check)
- [getOk](https://docs.polymarket.com/trading/clients/public#getok)
- [Markets](https://docs.polymarket.com/trading/clients/public#markets)
- [getMarket](https://docs.polymarket.com/trading/clients/public#getmarket)
- [getMarkets](https://docs.polymarket.com/trading/clients/public#getmarkets)
- [getSimplifiedMarkets](https://docs.polymarket.com/trading/clients/public#getsimplifiedmarkets)
- [getSamplingMarkets](https://docs.polymarket.com/trading/clients/public#getsamplingmarkets)
- [getSamplingSimplifiedMarkets](https://docs.polymarket.com/trading/clients/public#getsamplingsimplifiedmarkets)
- [Order Books and Prices](https://docs.polymarket.com/trading/clients/public#order-books-and-prices)
- [calculateMarketPrice](https://docs.polymarket.com/trading/clients/public#calculatemarketprice)
- [getOrderBook](https://docs.polymarket.com/trading/clients/public#getorderbook)
- [getOrderBooks](https://docs.polymarket.com/trading/clients/public#getorderbooks)
- [getPrice](https://docs.polymarket.com/trading/clients/public#getprice)
- [getPrices](https://docs.polymarket.com/trading/clients/public#getprices)
- [getMidpoint](https://docs.polymarket.com/trading/clients/public#getmidpoint)
- [getMidpoints](https://docs.polymarket.com/trading/clients/public#getmidpoints)
- [getSpread](https://docs.polymarket.com/trading/clients/public#getspread)
- [getSpreads](https://docs.polymarket.com/trading/clients/public#getspreads)
- [getPricesHistory](https://docs.polymarket.com/trading/clients/public#getpriceshistory)
- [Trades](https://docs.polymarket.com/trading/clients/public#trades)
- [getLastTradePrice](https://docs.polymarket.com/trading/clients/public#getlasttradeprice)
- [getLastTradesPrices](https://docs.polymarket.com/trading/clients/public#getlasttradesprices)
- [getMarketTradesEvents](https://docs.polymarket.com/trading/clients/public#getmarkettradesevents)
- [Market Parameters](https://docs.polymarket.com/trading/clients/public#market-parameters)
- [getFeeRateBps](https://docs.polymarket.com/trading/clients/public#getfeeratebps)
- [getTickSize](https://docs.polymarket.com/trading/clients/public#getticksize)
- [getNegRisk](https://docs.polymarket.com/trading/clients/public#getnegrisk)
- [Time and Server Info](https://docs.polymarket.com/trading/clients/public#time-and-server-info)
- [getServerTime](https://docs.polymarket.com/trading/clients/public#getservertime)
- [See Also](https://docs.polymarket.com/trading/clients/public#see-also)

## [​](https://docs.polymarket.com/trading/clients/public\#client-initialization)  Client Initialization

Public methods require the client to initialize with the host URL and Polygon chain ID.

- TypeScript

- Python


Copy

Ask AI

```
import { ClobClient } from "@polymarket/clob-client";

const client = new ClobClient(
  "https://clob.polymarket.com",
  137
);

// Ready to call public methods
const markets = await client.getMarkets();
```

Copy

Ask AI

```
from py_clob_client.client import ClobClient

client = ClobClient(
    host="https://clob.polymarket.com",
    chain_id=137
)

# Ready to call public methods
markets = client.get_markets()
```

* * *

## [​](https://docs.polymarket.com/trading/clients/public\#health-check)  Health Check

* * *

### [​](https://docs.polymarket.com/trading/clients/public\#getok)  getOk

Health check endpoint to verify the CLOB service is operational.

Signature

Copy

Ask AI

```
async getOk(): Promise<any>
```

* * *

## [​](https://docs.polymarket.com/trading/clients/public\#markets)  Markets

* * *

### [​](https://docs.polymarket.com/trading/clients/public\#getmarket)  getMarket

Get details for a single market by condition ID.

Signature

Copy

Ask AI

```
async getMarket(conditionId: string): Promise<Market>
```

[​](https://docs.polymarket.com/trading/clients/public#param-accepting-order-timestamp)

accepting\_order\_timestamp

string

Timestamp from which the market started accepting orders, or null if not set.

[​](https://docs.polymarket.com/trading/clients/public#param-accepting-orders)

accepting\_orders

boolean

Whether the market is currently accepting orders.

[​](https://docs.polymarket.com/trading/clients/public#param-active)

active

boolean

Whether the market is active.

[​](https://docs.polymarket.com/trading/clients/public#param-archived)

archived

boolean

Whether the market has been archived.

[​](https://docs.polymarket.com/trading/clients/public#param-closed)

closed

boolean

Whether the market is closed.

[​](https://docs.polymarket.com/trading/clients/public#param-condition-id)

condition\_id

string

The unique condition ID for the market.

[​](https://docs.polymarket.com/trading/clients/public#param-description)

description

string

Human-readable description of the market.

[​](https://docs.polymarket.com/trading/clients/public#param-enable-order-book)

enable\_order\_book

boolean

Whether the order book is enabled for this market.

[​](https://docs.polymarket.com/trading/clients/public#param-end-date-iso)

end\_date\_iso

string

ISO 8601 end date of the market.

[​](https://docs.polymarket.com/trading/clients/public#param-fpmm)

fpmm

string

Address of the Fixed Product Market Maker contract.

[​](https://docs.polymarket.com/trading/clients/public#param-game-start-time)

game\_start\_time

string

Start time of the underlying game or event.

[​](https://docs.polymarket.com/trading/clients/public#param-icon)

icon

string

URL of the market icon image.

[​](https://docs.polymarket.com/trading/clients/public#param-image)

image

string

URL of the market image.

[​](https://docs.polymarket.com/trading/clients/public#param-is-50-50-outcome)

is\_50\_50\_outcome

boolean

Whether the market has equal 50/50 outcomes.

[​](https://docs.polymarket.com/trading/clients/public#param-maker-base-fee)

maker\_base\_fee

number

Base fee charged to makers in basis points.

[​](https://docs.polymarket.com/trading/clients/public#param-market-slug)

market\_slug

string

URL-friendly slug identifier for the market.

[​](https://docs.polymarket.com/trading/clients/public#param-minimum-order-size)

minimum\_order\_size

number

Minimum order size allowed in this market.

[​](https://docs.polymarket.com/trading/clients/public#param-minimum-tick-size)

minimum\_tick\_size

number

Minimum price increment allowed in this market.

[​](https://docs.polymarket.com/trading/clients/public#param-neg-risk)

neg\_risk

boolean

Whether the market uses negative risk (binary complementary tokens).

[​](https://docs.polymarket.com/trading/clients/public#param-neg-risk-market-id)

neg\_risk\_market\_id

string

Negative risk market identifier, if applicable.

[​](https://docs.polymarket.com/trading/clients/public#param-neg-risk-request-id)

neg\_risk\_request\_id

string

Negative risk request identifier, if applicable.

[​](https://docs.polymarket.com/trading/clients/public#param-notifications-enabled)

notifications\_enabled

boolean

Whether notifications are enabled for this market.

[​](https://docs.polymarket.com/trading/clients/public#param-question)

question

string

The market question text.

[​](https://docs.polymarket.com/trading/clients/public#param-question-id)

question\_id

string

Unique identifier for the market question.

[​](https://docs.polymarket.com/trading/clients/public#param-rewards)

rewards

object

Object containing reward config: `max_spread` (number), `min_size` (number), `rates` (any)

[​](https://docs.polymarket.com/trading/clients/public#param-seconds-delay)

seconds\_delay

number

Delay in seconds before orders are processed.

[​](https://docs.polymarket.com/trading/clients/public#param-tags)

tags

string\[\]

List of tags associated with the market.

[​](https://docs.polymarket.com/trading/clients/public#param-taker-base-fee)

taker\_base\_fee

number

Base fee charged to takers in basis points.

[​](https://docs.polymarket.com/trading/clients/public#param-tokens)

tokens

MarketToken\[\]

Array of market tokens, each containing `outcome` (string), `price` (number), `token_id` (string), and `winner` (boolean).

* * *

### [​](https://docs.polymarket.com/trading/clients/public\#getmarkets)  getMarkets

Get details for multiple markets paginated.

Signature

Copy

Ask AI

```
async getMarkets(): Promise<PaginationPayload>
```

[​](https://docs.polymarket.com/trading/clients/public#param-limit)

limit

number

Maximum number of results per page.

[​](https://docs.polymarket.com/trading/clients/public#param-count)

count

number

Total number of markets returned.

[​](https://docs.polymarket.com/trading/clients/public#param-data)

data

Market\[\]

Array of Market objects. See `getMarket()` for the full Market structure.

* * *

### [​](https://docs.polymarket.com/trading/clients/public\#getsimplifiedmarkets)  getSimplifiedMarkets

Get simplified market data paginated for faster loading.

Signature

Copy

Ask AI

```
async getSimplifiedMarkets(): Promise<PaginationPayload>
```

[​](https://docs.polymarket.com/trading/clients/public#param-limit-1)

limit

number

Maximum number of results per page.

[​](https://docs.polymarket.com/trading/clients/public#param-count-1)

count

number

Total number of markets returned.

[​](https://docs.polymarket.com/trading/clients/public#param-data-1)

data

SimplifiedMarket\[\]

Array of simplified market objects, each containing `accepting_orders` (boolean), `active` (boolean), `archived` (boolean), `closed` (boolean), `condition_id` (string), `rewards` (object with `rates`, `min_size`, `max_spread`), and `tokens` (SimplifiedToken\[\]) with `outcome` (string), `price` (number), `token_id` (string).

* * *

### [​](https://docs.polymarket.com/trading/clients/public\#getsamplingmarkets)  getSamplingMarkets

Get markets eligible for sampling/liquidity rewards.

Signature

Copy

Ask AI

```
async getSamplingMarkets(): Promise<PaginationPayload>
```

* * *

### [​](https://docs.polymarket.com/trading/clients/public\#getsamplingsimplifiedmarkets)  getSamplingSimplifiedMarkets

Get simplified market data for markets eligible for sampling/liquidity rewards.

Signature

Copy

Ask AI

```
async getSamplingSimplifiedMarkets(): Promise<PaginationPayload>
```

* * *

## [​](https://docs.polymarket.com/trading/clients/public\#order-books-and-prices)  Order Books and Prices

* * *

### [​](https://docs.polymarket.com/trading/clients/public\#calculatemarketprice)  calculateMarketPrice

Calculate the estimated price for a market order of a given size.

Signature

Copy

Ask AI

```
async calculateMarketPrice(
  tokenID: string,
  side: Side,
  amount: number,
  orderType: OrderType = OrderType.FOK
): Promise<number>
```

[​](https://docs.polymarket.com/trading/clients/public#param-token-id)

tokenID

string

The token ID to calculate the market price for.

[​](https://docs.polymarket.com/trading/clients/public#param-side)

side

Side

The side of the order. One of: `BUY`, `SELL`

[​](https://docs.polymarket.com/trading/clients/public#param-amount)

amount

number

The size of the order to calculate price for.

[​](https://docs.polymarket.com/trading/clients/public#param-order-type)

orderType

OrderType

The order type. One of: `GTC` (Good Till Cancelled), `FOK` (Fill or Kill), `GTD` (Good Till Date), `FAK` (Fill and Kill). Defaults to `FOK`.

[​](https://docs.polymarket.com/trading/clients/public#param-returns)

returns

number

The calculated estimated market price for the given order size.

* * *

### [​](https://docs.polymarket.com/trading/clients/public\#getorderbook)  getOrderBook

Get the order book for a specific token ID.

Signature

Copy

Ask AI

```
async getOrderBook(tokenID: string): Promise<OrderBookSummary>
```

[​](https://docs.polymarket.com/trading/clients/public#param-market)

market

string

The market condition ID.

[​](https://docs.polymarket.com/trading/clients/public#param-asset-id)

asset\_id

string

The token/asset ID for this order book.

[​](https://docs.polymarket.com/trading/clients/public#param-timestamp)

timestamp

string

Timestamp of the order book snapshot.

[​](https://docs.polymarket.com/trading/clients/public#param-bids)

bids

OrderSummary\[\]

Array of bid entries, each with `price` (string) and `size` (string).

[​](https://docs.polymarket.com/trading/clients/public#param-asks)

asks

OrderSummary\[\]

Array of ask entries, each with `price` (string) and `size` (string).

[​](https://docs.polymarket.com/trading/clients/public#param-min-order-size)

min\_order\_size

string

Minimum order size for this market.

[​](https://docs.polymarket.com/trading/clients/public#param-tick-size)

tick\_size

string

Minimum price increment for this market.

[​](https://docs.polymarket.com/trading/clients/public#param-neg-risk-1)

neg\_risk

boolean

Whether the market uses negative risk.

[​](https://docs.polymarket.com/trading/clients/public#param-hash)

hash

string

Hash of the order book state.

* * *

### [​](https://docs.polymarket.com/trading/clients/public\#getorderbooks)  getOrderBooks

Get order books for multiple token IDs.

Signature

Copy

Ask AI

```
async getOrderBooks(params: BookParams[]): Promise<OrderBookSummary[]>
```

[​](https://docs.polymarket.com/trading/clients/public#param-token-id)

token\_id

string

The token ID to fetch the order book for.

[​](https://docs.polymarket.com/trading/clients/public#param-side-1)

side

Side

The side of the book to query. One of: `BUY`, `SELL`

[​](https://docs.polymarket.com/trading/clients/public#param-returns-1)

returns

OrderBookSummary\[\]

Array of OrderBookSummary objects. See `getOrderBook()` for the full structure.

* * *

### [​](https://docs.polymarket.com/trading/clients/public\#getprice)  getPrice

Get the current best price for buying or selling a token ID.

Signature

Copy

Ask AI

```
async getPrice(
  tokenID: string,
  side: "BUY" | "SELL"
): Promise<any>
```

[​](https://docs.polymarket.com/trading/clients/public#param-price)

price

string

The current best price for the requested side.

* * *

### [​](https://docs.polymarket.com/trading/clients/public\#getprices)  getPrices

Get the current best prices for multiple token IDs.

Signature

Copy

Ask AI

```
async getPrices(params: BookParams[]): Promise<PricesResponse>
```

[​](https://docs.polymarket.com/trading/clients/public#param-returns-2)

returns

PricesResponse

A map of token IDs to their prices. Each entry contains an optional `BUY` (string) and/or `SELL` (string) price.

* * *

### [​](https://docs.polymarket.com/trading/clients/public\#getmidpoint)  getMidpoint

Get the midpoint price (average of best bid and best ask) for a token ID.

Signature

Copy

Ask AI

```
async getMidpoint(tokenID: string): Promise<any>
```

[​](https://docs.polymarket.com/trading/clients/public#param-mid)

mid

string

The midpoint price, calculated as the average of best bid and best ask.

* * *

### [​](https://docs.polymarket.com/trading/clients/public\#getmidpoints)  getMidpoints

Get the midpoint prices for multiple token IDs.

Signature

Copy

Ask AI

```
async getMidpoints(params: BookParams[]): Promise<any>
```

[​](https://docs.polymarket.com/trading/clients/public#param-returns-3)

returns

object

A map of token IDs to their midpoint price strings. Each key is a token ID and its value is the midpoint price as a string.

* * *

### [​](https://docs.polymarket.com/trading/clients/public\#getspread)  getSpread

Get the spread (difference between best ask and best bid) for a token ID.

Signature

Copy

Ask AI

```
async getSpread(tokenID: string): Promise<SpreadResponse>
```

[​](https://docs.polymarket.com/trading/clients/public#param-spread)

spread

string

The spread value, calculated as the difference between best ask and best bid.

* * *

### [​](https://docs.polymarket.com/trading/clients/public\#getspreads)  getSpreads

Get the spreads for multiple token IDs.

Signature

Copy

Ask AI

```
async getSpreads(params: BookParams[]): Promise<SpreadsResponse>
```

[​](https://docs.polymarket.com/trading/clients/public#param-returns-4)

returns

object

A map of token IDs to their spread strings. Each key is a token ID and its value is the spread as a string.

* * *

### [​](https://docs.polymarket.com/trading/clients/public\#getpriceshistory)  getPricesHistory

Get historical price data for a token.

Signature

Copy

Ask AI

```
async getPricesHistory(params: PriceHistoryFilterParams): Promise<MarketPrice[]>
```

[​](https://docs.polymarket.com/trading/clients/public#param-market-1)

market

string

The token ID to fetch price history for.

[​](https://docs.polymarket.com/trading/clients/public#param-start-ts)

startTs

number

Optional start timestamp (Unix seconds) for the price history range.

[​](https://docs.polymarket.com/trading/clients/public#param-end-ts)

endTs

number

Optional end timestamp (Unix seconds) for the price history range.

[​](https://docs.polymarket.com/trading/clients/public#param-fidelity)

fidelity

number

Optional fidelity/resolution of the price history data.

[​](https://docs.polymarket.com/trading/clients/public#param-interval)

interval

PriceHistoryInterval

Time interval for the price history. One of: `max`, `1w`, `1d`, `6h`, `1h`

[​](https://docs.polymarket.com/trading/clients/public#paramt)

t

number

Unix timestamp of the price data point.

[​](https://docs.polymarket.com/trading/clients/public#param-p)

p

number

Price value at the corresponding timestamp.

* * *

## [​](https://docs.polymarket.com/trading/clients/public\#trades)  Trades

* * *

### [​](https://docs.polymarket.com/trading/clients/public\#getlasttradeprice)  getLastTradePrice

Get the price of the most recent trade for a token.

Signature

Copy

Ask AI

```
async getLastTradePrice(tokenID: string): Promise<LastTradePrice>
```

[​](https://docs.polymarket.com/trading/clients/public#param-price-1)

price

string

The price of the most recent trade.

[​](https://docs.polymarket.com/trading/clients/public#param-side-2)

side

string

The side of the most recent trade.

* * *

### [​](https://docs.polymarket.com/trading/clients/public\#getlasttradesprices)  getLastTradesPrices

Get the most recent trade prices for multiple tokens.

Signature

Copy

Ask AI

```
async getLastTradesPrices(params: BookParams[]): Promise<LastTradePriceWithToken[]>
```

[​](https://docs.polymarket.com/trading/clients/public#param-price-2)

price

string

The price of the most recent trade for the token.

[​](https://docs.polymarket.com/trading/clients/public#param-side-3)

side

string

The side of the most recent trade.

[​](https://docs.polymarket.com/trading/clients/public#param-token-id-1)

token\_id

string

The token ID this trade price corresponds to.

* * *

### [​](https://docs.polymarket.com/trading/clients/public\#getmarkettradesevents)  getMarketTradesEvents

Get recent trade events for a market.

Signature

Copy

Ask AI

```
async getMarketTradesEvents(conditionID: string): Promise<MarketTradeEvent[]>
```

[​](https://docs.polymarket.com/trading/clients/public#param-event-type)

event\_type

string

The type of trade event.

[​](https://docs.polymarket.com/trading/clients/public#param-market-2)

market

object

Object containing market info: `condition_id` (string), `asset_id` (string), `question` (string), `icon` (string), `slug` (string).

[​](https://docs.polymarket.com/trading/clients/public#param-user)

user

object

Object containing user info: `address` (string), `username` (string), `profile_picture` (string), `optimized_profile_picture` (string), `pseudonym` (string).

[​](https://docs.polymarket.com/trading/clients/public#param-side-4)

side

Side

The side of the trade. One of: `BUY`, `SELL`

[​](https://docs.polymarket.com/trading/clients/public#param-size)

size

string

The size of the trade.

[​](https://docs.polymarket.com/trading/clients/public#param-fee-rate-bps)

fee\_rate\_bps

string

The fee rate in basis points for the trade.

[​](https://docs.polymarket.com/trading/clients/public#param-price-3)

price

string

The price at which the trade was executed.

[​](https://docs.polymarket.com/trading/clients/public#param-outcome)

outcome

string

The outcome label for the traded token.

[​](https://docs.polymarket.com/trading/clients/public#param-outcome-index)

outcome\_index

number

The index of the outcome in the market.

[​](https://docs.polymarket.com/trading/clients/public#param-transaction-hash)

transaction\_hash

string

The on-chain transaction hash for the trade.

[​](https://docs.polymarket.com/trading/clients/public#param-timestamp-1)

timestamp

string

The timestamp of when the trade event occurred.

* * *

## [​](https://docs.polymarket.com/trading/clients/public\#market-parameters)  Market Parameters

* * *

### [​](https://docs.polymarket.com/trading/clients/public\#getfeeratebps)  getFeeRateBps

Get the fee rate in basis points for a token.

Signature

Copy

Ask AI

```
async getFeeRateBps(tokenID: string): Promise<number>
```

[​](https://docs.polymarket.com/trading/clients/public#param-returns-5)

returns

number

The fee rate in basis points for the specified token.

* * *

### [​](https://docs.polymarket.com/trading/clients/public\#getticksize)  getTickSize

Get the tick size (minimum price increment) for a market.

Signature

Copy

Ask AI

```
async getTickSize(tokenID: string): Promise<TickSize>
```

[​](https://docs.polymarket.com/trading/clients/public#param-returns-6)

returns

string

The tick size for the market. One of: `0.1`, `0.01`, `0.001`, `0.0001`

* * *

### [​](https://docs.polymarket.com/trading/clients/public\#getnegrisk)  getNegRisk

Check if a market uses negative risk (binary complementary tokens).

Signature

Copy

Ask AI

```
async getNegRisk(tokenID: string): Promise<boolean>
```

[​](https://docs.polymarket.com/trading/clients/public#param-returns-7)

returns

boolean

Whether the market uses negative risk.

* * *

## [​](https://docs.polymarket.com/trading/clients/public\#time-and-server-info)  Time and Server Info

### [​](https://docs.polymarket.com/trading/clients/public\#getservertime)  getServerTime

Get the current server timestamp.

Signature

Copy

Ask AI

```
async getServerTime(): Promise<number>
```

[​](https://docs.polymarket.com/trading/clients/public#param-returns-8)

returns

number

Unix timestamp in seconds representing the current server time.

* * *

## [​](https://docs.polymarket.com/trading/clients/public\#see-also)  See Also

[**L1 Methods** \\
\\
Private key authentication to create or derive API credentials.](https://docs.polymarket.com/trading/clients/l1)

[**L2 Methods** \\
\\
Place orders, cancel orders, and query your trades.](https://docs.polymarket.com/trading/clients/l2)

[**REST API Reference** \\
\\
Complete REST endpoint documentation.](https://docs.polymarket.com/api-reference/introduction)

[**WebSocket** \\
\\
Real-time market data streaming.](https://docs.polymarket.com/market-data/websocket/overview)

Was this page helpful?

YesNo

[Order Attribution\\
\\
Previous](https://docs.polymarket.com/trading/orders/attribution) [L1 Methods\\
\\
Next](https://docs.polymarket.com/trading/clients/l1)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.

Suggestions

How do I connect to WebSocket streams?What's required to place my first order?How do I find and fetch market data?