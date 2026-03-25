---
url: "https://docs.polymarket.com/market-data/fetching-markets"
title: "Fetching Markets - Polymarket Documentation"
---

[Skip to main content](https://docs.polymarket.com/market-data/fetching-markets#content-area)

[Polymarket Documentation home page![light logo](https://mintcdn.com/polymarket-292d1b1b/ZibMe6Tli_amZald/logo/light.svg?fit=max&auto=format&n=ZibMe6Tli_amZald&q=85&s=9f9bd559f02181495794661ef6426c0f)![dark logo](https://mintcdn.com/polymarket-292d1b1b/ZibMe6Tli_amZald/logo/dark.svg?fit=max&auto=format&n=ZibMe6Tli_amZald&q=85&s=13abc6754579a3475368ea99d0f5a241)](https://docs.polymarket.com/)

![US](https://d3gk2c5xim1je2.cloudfront.net/flags/US.svg)

English

Search...

Ctrl KAsk AI

Search...

Navigation

Market Data

Fetching Markets

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

- [Fetch by Slug](https://docs.polymarket.com/market-data/fetching-markets#fetch-by-slug)
- [How to Extract the Slug](https://docs.polymarket.com/market-data/fetching-markets#how-to-extract-the-slug)
- [Examples](https://docs.polymarket.com/market-data/fetching-markets#examples)
- [Fetch by Tags](https://docs.polymarket.com/market-data/fetching-markets#fetch-by-tags)
- [Discover Available Tags](https://docs.polymarket.com/market-data/fetching-markets#discover-available-tags)
- [Filter by Tag](https://docs.polymarket.com/market-data/fetching-markets#filter-by-tag)
- [Additional Tag Filtering](https://docs.polymarket.com/market-data/fetching-markets#additional-tag-filtering)
- [Fetch All Active Markets](https://docs.polymarket.com/market-data/fetching-markets#fetch-all-active-markets)
- [Key Parameters](https://docs.polymarket.com/market-data/fetching-markets#key-parameters)
- [Pagination](https://docs.polymarket.com/market-data/fetching-markets#pagination)
- [Best Practices](https://docs.polymarket.com/market-data/fetching-markets#best-practices)
- [Next Steps](https://docs.polymarket.com/market-data/fetching-markets#next-steps)

Both the events and markets endpoints are paginated. See
[pagination](https://docs.polymarket.com/market-data/fetching-markets#pagination) for details.

There are three main strategies for retrieving market data, each optimized for different use cases:

1. **By Slug** — Best for fetching specific individual markets or events
2. **By Tags** — Ideal for filtering markets by category or sport
3. **Via Events Endpoint** — Most efficient for retrieving all active markets

* * *

## [​](https://docs.polymarket.com/market-data/fetching-markets\#fetch-by-slug)  Fetch by Slug

**Use case:** When you need to retrieve a specific market or event that you already know about.Individual markets and events are best fetched using their unique slug identifier. The slug can be found directly in the Polymarket frontend URL.

### [​](https://docs.polymarket.com/market-data/fetching-markets\#how-to-extract-the-slug)  How to Extract the Slug

From any Polymarket URL, the slug is the path segment after `/event/`:

Copy

Ask AI

```
https://polymarket.com/event/fed-decision-in-october
                                ↑
                      Slug: fed-decision-in-october
```

### [​](https://docs.polymarket.com/market-data/fetching-markets\#examples)  Examples

Copy

Ask AI

```
# Fetch an event by slug (query parameter)
curl "https://gamma-api.polymarket.com/events?slug=fed-decision-in-october"

# Or use the path endpoint
curl "https://gamma-api.polymarket.com/events/slug/fed-decision-in-october"
```

Copy

Ask AI

```
# Fetch a market by slug (query parameter)
curl "https://gamma-api.polymarket.com/markets?slug=fed-decision-in-october"

# Or use the path endpoint
curl "https://gamma-api.polymarket.com/markets/slug/fed-decision-in-october"
```

* * *

## [​](https://docs.polymarket.com/market-data/fetching-markets\#fetch-by-tags)  Fetch by Tags

**Use case:** When you want to filter markets by category, sport, or topic.Tags provide a way to categorize and filter markets. You can discover available tags and then use them to filter your requests.

### [​](https://docs.polymarket.com/market-data/fetching-markets\#discover-available-tags)  Discover Available Tags

**General tags:**`GET /tags` (Gamma API)**Sports tags and metadata:**`GET /sports` (Gamma API)The `/sports` endpoint returns metadata for sports including tag IDs, images, resolution sources, and series information.

### [​](https://docs.polymarket.com/market-data/fetching-markets\#filter-by-tag)  Filter by Tag

Once you have tag IDs, use the `tag_id` parameter in both events and markets endpoints:

Copy

Ask AI

```
# Fetch events for a specific tag
curl "https://gamma-api.polymarket.com/events?tag_id=100381&limit=10&active=true&closed=false"
```

### [​](https://docs.polymarket.com/market-data/fetching-markets\#additional-tag-filtering)  Additional Tag Filtering

You can also:

- Use `related_tags=true` to include related tag markets
- Exclude specific tags with `exclude_tag_id`

Copy

Ask AI

```
# Include related tags
curl "https://gamma-api.polymarket.com/events?tag_id=100381&related_tags=true&active=true&closed=false"
```

* * *

## [​](https://docs.polymarket.com/market-data/fetching-markets\#fetch-all-active-markets)  Fetch All Active Markets

**Use case:** When you need to retrieve all available active markets, typically for broader analysis or market discovery.The most efficient approach is to use the events endpoint with `active=true&closed=false`, as events contain their associated markets.

Copy

Ask AI

```
curl "https://gamma-api.polymarket.com/events?active=true&closed=false&limit=100"
```

### [​](https://docs.polymarket.com/market-data/fetching-markets\#key-parameters)  Key Parameters

| Parameter | Description |
| --- | --- |
| `order` | Field to order by (`volume_24hr`, `volume`, `liquidity`, `start_date`, `end_date`, `competitive`, `closed_time`) |
| `ascending` | Sort direction (`true` for ascending, `false` for descending). Default: `false` |
| `active` | Filter by active status (`true` for live tradable events) |
| `closed` | Filter by closed status |
| `limit` | Results per page |
| `offset` | Number of results to skip for pagination |

Copy

Ask AI

```
# Get the highest volume active events
curl "https://gamma-api.polymarket.com/events?active=true&closed=false&order=volume_24hr&ascending=false&limit=100"
```

* * *

## [​](https://docs.polymarket.com/market-data/fetching-markets\#pagination)  Pagination

All list endpoints return paginated responses with `limit` and `offset` parameters:

Copy

Ask AI

```
# Page 1: First 50 results
curl "https://gamma-api.polymarket.com/events?active=true&closed=false&limit=50&offset=0"

# Page 2: Next 50 results
curl "https://gamma-api.polymarket.com/events?active=true&closed=false&limit=50&offset=50"

# Page 3: Next 50 results
curl "https://gamma-api.polymarket.com/events?active=true&closed=false&limit=50&offset=100"
```

* * *

## [​](https://docs.polymarket.com/market-data/fetching-markets\#best-practices)  Best Practices

1. **For individual markets:** Use the slug method for direct lookups
2. **For category browsing:** Use tag filtering to reduce API calls
3. **For complete market discovery:** Use the events endpoint with pagination
4. **Always include `active=true&closed=false`** unless you specifically need historical data
5. **Use the events endpoint** and work backwards — events contain their associated markets, reducing the number of API calls needed

* * *

## [​](https://docs.polymarket.com/market-data/fetching-markets\#next-steps)  Next Steps

[**API Reference** \\
\\
Full endpoint documentation with parameters and response schemas.](https://docs.polymarket.com/api-reference/introduction)

[**Subgraph** \\
\\
Query onchain data directly from the Polymarket subgraph.](https://docs.polymarket.com/market-data/subgraph)

Was this page helpful?

YesNo

[Overview\\
\\
Previous](https://docs.polymarket.com/market-data/overview) [Subgraph\\
\\
Next](https://docs.polymarket.com/market-data/subgraph)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.

Suggestions

How do I connect to WebSocket streams?What's required to place my first order?How do I find and fetch market data?