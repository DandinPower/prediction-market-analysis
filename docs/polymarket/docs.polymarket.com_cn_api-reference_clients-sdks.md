---
url: "https://docs.polymarket.com/cn/api-reference/clients-sdks"
title: "客户端与 SDK - Polymarket Documentation"
---

[跳转到主要内容](https://docs.polymarket.com/cn/api-reference/clients-sdks#content-area)

[Polymarket Documentation home page![light logo](https://mintcdn.com/polymarket-292d1b1b/ZibMe6Tli_amZald/logo/light.svg?fit=max&auto=format&n=ZibMe6Tli_amZald&q=85&s=9f9bd559f02181495794661ef6426c0f)![dark logo](https://mintcdn.com/polymarket-292d1b1b/ZibMe6Tli_amZald/logo/dark.svg?fit=max&auto=format&n=ZibMe6Tli_amZald&q=85&s=13abc6754579a3475368ea99d0f5a241)](https://docs.polymarket.com/cn)

![CN](https://d3gk2c5xim1je2.cloudfront.net/flags/CN.svg)

简体中文

搜索...

Ctrl K询问AI

搜索...

Navigation

概览

客户端与 SDK

[文档](https://docs.polymarket.com/cn) [API 参考](https://docs.polymarket.com/cn/api-reference/introduction)

##### 概览

- [简介](https://docs.polymarket.com/cn/api-reference/introduction)
- [身份验证](https://docs.polymarket.com/cn/api-reference/authentication)
- [速率限制](https://docs.polymarket.com/cn/api-reference/rate-limits)
- [客户端与 SDK](https://docs.polymarket.com/cn/api-reference/clients-sdks)
- [地区限制](https://docs.polymarket.com/cn/api-reference/geoblock)

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

在此页面

- [安装](https://docs.polymarket.com/cn/api-reference/clients-sdks#%E5%AE%89%E8%A3%85)
- [快速示例](https://docs.polymarket.com/cn/api-reference/clients-sdks#%E5%BF%AB%E9%80%9F%E7%A4%BA%E4%BE%8B)
- [源代码](https://docs.polymarket.com/cn/api-reference/clients-sdks#%E6%BA%90%E4%BB%A3%E7%A0%81)
- [Builder SDK](https://docs.polymarket.com/cn/api-reference/clients-sdks#builder-sdk)
- [Relayer SDK](https://docs.polymarket.com/cn/api-reference/clients-sdks#relayer-sdk)
- [下一步](https://docs.polymarket.com/cn/api-reference/clients-sdks#%E4%B8%8B%E4%B8%80%E6%AD%A5)

Polymarket 提供 TypeScript、Python 和 Rust 的官方开源客户端。三者都支持完整的 CLOB API，包括市场数据、订单管理和身份验证。

## [​](https://docs.polymarket.com/cn/api-reference/clients-sdks\#%E5%AE%89%E8%A3%85)  安装

TypeScript

Python

Rust

复制

询问AI

```
npm install @polymarket/clob-client ethers@5
```

## [​](https://docs.polymarket.com/cn/api-reference/clients-sdks\#%E5%BF%AB%E9%80%9F%E7%A4%BA%E4%BE%8B)  快速示例

TypeScript

Python

复制

询问AI

```
import { ClobClient } from "@polymarket/clob-client";

const client = new ClobClient(
  "https://clob.polymarket.com",
  137,
  signer,
  apiCreds,
);

const markets = await client.getMarkets();
```

## [​](https://docs.polymarket.com/cn/api-reference/clients-sdks\#%E6%BA%90%E4%BB%A3%E7%A0%81)  源代码

| 语言 | 包 | 仓库 |
| --- | --- | --- |
| TypeScript | `@polymarket/clob-client` | [github.com/Polymarket/clob-client](https://github.com/Polymarket/clob-client) |
| Python | `py-clob-client` | [github.com/Polymarket/py-clob-client](https://github.com/Polymarket/py-clob-client) |
| Rust | `polymarket-client-sdk` | [github.com/Polymarket/rs-clob-client](https://github.com/Polymarket/rs-clob-client) |

每个仓库的 `/examples` 目录中包含可运行的示例。

## [​](https://docs.polymarket.com/cn/api-reference/clients-sdks\#builder-sdk)  Builder SDK

如果你通过 [Builder Program](https://docs.polymarket.com/builders/overview) 构建应用，还可以使用额外的签名 SDK：

| 语言 | 包 | 仓库 |
| --- | --- | --- |
| TypeScript | `@polymarket/builder-signing-sdk` | [github.com/Polymarket/builder-signing-sdk](https://github.com/Polymarket/builder-signing-sdk) |
| Python | `py_builder_signing_sdk` | [github.com/Polymarket/py-builder-signing-sdk](https://github.com/Polymarket/py-builder-signing-sdk) |

使用详情请参阅 [订单归因](https://docs.polymarket.com/trading/orders/attribution)。

## [​](https://docs.polymarket.com/cn/api-reference/clients-sdks\#relayer-sdk)  Relayer SDK

对于使用代理钱包的 [免 Gas 交易](https://docs.polymarket.com/trading/gasless)，Relayer 客户端负责通过 Polymarket 的 relayer 提交交易：

| 语言 | 包 | 仓库 |
| --- | --- | --- |
| TypeScript | `@polymarket/builder-relayer-client` | [github.com/Polymarket/builder-relayer-client](https://github.com/Polymarket/builder-relayer-client) |
| Python | `py-builder-relayer-client` | [github.com/Polymarket/py-builder-relayer-client](https://github.com/Polymarket/py-builder-relayer-client) |

## [​](https://docs.polymarket.com/cn/api-reference/clients-sdks\#%E4%B8%8B%E4%B8%80%E6%AD%A5)  下一步

[**快速开始** \\
\\
设置客户端并下你的第一笔订单。](https://docs.polymarket.com/quickstart)

[**身份验证** \\
\\
了解 L1/L2 身份验证和 API 凭证。](https://docs.polymarket.com/api-reference/authentication)

此页面对您有帮助吗？

是否

[速率限制\\
\\
上一页](https://docs.polymarket.com/cn/api-reference/rate-limits) [地区限制\\
\\
下一页](https://docs.polymarket.com/cn/api-reference/geoblock)

Ctrl+I

助手

AI生成的回答可能包含错误。