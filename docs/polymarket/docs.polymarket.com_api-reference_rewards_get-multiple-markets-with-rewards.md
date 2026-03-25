---
url: "https://docs.polymarket.com/api-reference/rewards/get-multiple-markets-with-rewards"
title: "Get multiple markets with rewards - Polymarket Documentation"
---

[Skip to main content](https://docs.polymarket.com/api-reference/rewards/get-multiple-markets-with-rewards#content-area)

[Polymarket Documentation home page![light logo](https://mintcdn.com/polymarket-292d1b1b/ZibMe6Tli_amZald/logo/light.svg?fit=max&auto=format&n=ZibMe6Tli_amZald&q=85&s=9f9bd559f02181495794661ef6426c0f)![dark logo](https://mintcdn.com/polymarket-292d1b1b/ZibMe6Tli_amZald/logo/dark.svg?fit=max&auto=format&n=ZibMe6Tli_amZald&q=85&s=13abc6754579a3475368ea99d0f5a241)](https://docs.polymarket.com/)

![US](https://d3gk2c5xim1je2.cloudfront.net/flags/US.svg)

English

Search...

Ctrl KAsk AI

Search...

Navigation

Rewards

Get multiple markets with rewards

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

Get multiple markets with rewards

cURL

Copy

Ask AI

```
curl --request GET \
  --url 'https://clob.polymarket.com/rewards/markets/multi?page_size=100'
```

200

Example

Copy

Ask AI

```
{
  "limit": 50,
  "count": 1,
  "next_cursor": "NQ==",
  "data": [\
    {\
      "condition_id": "0xbd31dc8a20211944f6b70f31557f1001557b59905b7738480ca09bd4532f84af",\
      "event_id": "12345",\
      "event_slug": "2024-us-election",\
      "created_at": "2024-05-01T12:00:00Z",\
      "group_item_title": "",\
      "image": "https://example.com/image.png",\
      "market_competitiveness": 0.42,\
      "market_id": "248849",\
      "market_slug": "will-trump-win-the-2024-iowa-caucus",\
      "one_day_price_change": 0.03,\
      "question": "Will Trump win the 2024 Iowa Caucus?",\
      "rewards_max_spread": 99,\
      "rewards_min_size": 10,\
      "spread": 0.12,\
      "end_date": "2024-08-10 00:00:00",\
      "tokens": [\
        {\
          "token_id": "1343197538147866997676250008839231694243646439454152539053893078719042421992",\
          "outcome": "YES",\
          "price": 0.8\
        },\
        {\
          "token_id": "16678291189211314787145083999015737376658799626183230671758641503291735614088",\
          "outcome": "NO",\
          "price": 0.2\
        }\
      ],\
      "volume_24hr": 12345.67,\
      "rewards_config": [\
        {\
          "id": 7,\
          "asset_address": "0x9c4E1703476E875070EE25b56A58B008CFb8FA78",\
          "start_date": "2024-03-01",\
          "end_date": "2500-12-31",\
          "rate_per_day": 2,\
          "total_rewards": 92\
        }\
      ]\
    }\
  ]
}
```

GET

https://clob.polymarket.comhttps://clob-staging.polymarket.com

/

rewards

/

markets

/

multi

Try it

Get multiple markets with rewards

cURL

Copy

Ask AI

```
curl --request GET \
  --url 'https://clob.polymarket.com/rewards/markets/multi?page_size=100'
```

200

Example

Copy

Ask AI

```
{
  "limit": 50,
  "count": 1,
  "next_cursor": "NQ==",
  "data": [\
    {\
      "condition_id": "0xbd31dc8a20211944f6b70f31557f1001557b59905b7738480ca09bd4532f84af",\
      "event_id": "12345",\
      "event_slug": "2024-us-election",\
      "created_at": "2024-05-01T12:00:00Z",\
      "group_item_title": "",\
      "image": "https://example.com/image.png",\
      "market_competitiveness": 0.42,\
      "market_id": "248849",\
      "market_slug": "will-trump-win-the-2024-iowa-caucus",\
      "one_day_price_change": 0.03,\
      "question": "Will Trump win the 2024 Iowa Caucus?",\
      "rewards_max_spread": 99,\
      "rewards_min_size": 10,\
      "spread": 0.12,\
      "end_date": "2024-08-10 00:00:00",\
      "tokens": [\
        {\
          "token_id": "1343197538147866997676250008839231694243646439454152539053893078719042421992",\
          "outcome": "YES",\
          "price": 0.8\
        },\
        {\
          "token_id": "16678291189211314787145083999015737376658799626183230671758641503291735614088",\
          "outcome": "NO",\
          "price": 0.2\
        }\
      ],\
      "volume_24hr": 12345.67,\
      "rewards_config": [\
        {\
          "id": 7,\
          "asset_address": "0x9c4E1703476E875070EE25b56A58B008CFb8FA78",\
          "start_date": "2024-03-01",\
          "end_date": "2500-12-31",\
          "rate_per_day": 2,\
          "total_rewards": 92\
        }\
      ]\
    }\
  ]
}
```

#### Query Parameters

[​](https://docs.polymarket.com/api-reference/rewards/get-multiple-markets-with-rewards#parameter-q)

q

string

Text search on market question/description

[​](https://docs.polymarket.com/api-reference/rewards/get-multiple-markets-with-rewards#parameter-tag-slug)

tag\_slug

string

Filter by tag slug. Can be repeated for OR logic (e.g., ?tag\_slug=sports&tag\_slug=politics)

[​](https://docs.polymarket.com/api-reference/rewards/get-multiple-markets-with-rewards#parameter-event-id)

event\_id

string

Filter by event ID. Can be repeated for multiple events (e.g., ?event\_id=100&event\_id=200)

[​](https://docs.polymarket.com/api-reference/rewards/get-multiple-markets-with-rewards#parameter-event-title)

event\_title

string

Search event titles using case-insensitive pattern matching

[​](https://docs.polymarket.com/api-reference/rewards/get-multiple-markets-with-rewards#parameter-order-by)

order\_by

enum<string>

Field to sort results by

Available options:

`market_id`,

`created_at`,

`volume_24hr`,

`spread`,

`competitiveness`,

`max_spread`,

`min_size`,

`question`,

`one_day_price_change`,

`rate_per_day`,

`price`,

`end_date`,

`start_date`,

`reward_end_date`

[​](https://docs.polymarket.com/api-reference/rewards/get-multiple-markets-with-rewards#parameter-position)

position

enum<string>

Sort direction

Available options:

`ASC`,

`DESC`

[​](https://docs.polymarket.com/api-reference/rewards/get-multiple-markets-with-rewards#parameter-min-volume-24hr)

min\_volume\_24hr

number<double>

Minimum 24-hour volume filter

[​](https://docs.polymarket.com/api-reference/rewards/get-multiple-markets-with-rewards#parameter-max-volume-24hr)

max\_volume\_24hr

number<double>

Maximum 24-hour volume filter

[​](https://docs.polymarket.com/api-reference/rewards/get-multiple-markets-with-rewards#parameter-min-spread)

min\_spread

number<double>

Minimum spread filter

[​](https://docs.polymarket.com/api-reference/rewards/get-multiple-markets-with-rewards#parameter-max-spread)

max\_spread

number<double>

Maximum spread filter

[​](https://docs.polymarket.com/api-reference/rewards/get-multiple-markets-with-rewards#parameter-min-price)

min\_price

number<double>

Minimum first token price filter

[​](https://docs.polymarket.com/api-reference/rewards/get-multiple-markets-with-rewards#parameter-max-price)

max\_price

number<double>

Maximum first token price filter

[​](https://docs.polymarket.com/api-reference/rewards/get-multiple-markets-with-rewards#parameter-next-cursor)

next\_cursor

string

Pagination cursor from previous response

[​](https://docs.polymarket.com/api-reference/rewards/get-multiple-markets-with-rewards#parameter-page-size)

page\_size

integer

default:100

Number of items per page (max 500, values above are capped)

Required range: `x <= 500`

#### Response

200

application/json

Successfully retrieved markets with rewards

Paginated list of markets with rewards and trading metrics

[​](https://docs.polymarket.com/api-reference/rewards/get-multiple-markets-with-rewards#response-limit)

limit

integer

required

Maximum number of items per page

[​](https://docs.polymarket.com/api-reference/rewards/get-multiple-markets-with-rewards#response-count)

count

integer

required

Number of items in the current response

[​](https://docs.polymarket.com/api-reference/rewards/get-multiple-markets-with-rewards#response-next-cursor)

next\_cursor

string

required

Cursor for the next page. "LTE=" indicates the last page.

[​](https://docs.polymarket.com/api-reference/rewards/get-multiple-markets-with-rewards#response-data)

data

object\[\]

required

Showchild attributes

Was this page helpful?

YesNo

[Get raw rewards for a specific market\\
\\
Previous](https://docs.polymarket.com/api-reference/rewards/get-raw-rewards-for-a-specific-market) [Get earnings for user by date\\
\\
Next](https://docs.polymarket.com/api-reference/rewards/get-earnings-for-user-by-date)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.

Suggestions

How do I connect to WebSocket streams?What's required to place my first order?How do I find and fetch market data?