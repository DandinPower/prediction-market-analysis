---
url: "https://docs.polymarket.com/cn/api-reference/authentication"
title: "身份验证 - Polymarket Documentation"
---

[跳转到主要内容](https://docs.polymarket.com/cn/api-reference/authentication#content-area)

[Polymarket Documentation home page![light logo](https://mintcdn.com/polymarket-292d1b1b/ZibMe6Tli_amZald/logo/light.svg?fit=max&auto=format&n=ZibMe6Tli_amZald&q=85&s=9f9bd559f02181495794661ef6426c0f)![dark logo](https://mintcdn.com/polymarket-292d1b1b/ZibMe6Tli_amZald/logo/dark.svg?fit=max&auto=format&n=ZibMe6Tli_amZald&q=85&s=13abc6754579a3475368ea99d0f5a241)](https://docs.polymarket.com/cn)

![CN](https://d3gk2c5xim1je2.cloudfront.net/flags/CN.svg)

简体中文

搜索...

Ctrl K询问AI

搜索...

Navigation

概览

身份验证

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

- [公开 vs 需要验证](https://docs.polymarket.com/cn/api-reference/authentication#%E5%85%AC%E5%BC%80-vs-%E9%9C%80%E8%A6%81%E9%AA%8C%E8%AF%81)
- [两级身份验证模型](https://docs.polymarket.com/cn/api-reference/authentication#%E4%B8%A4%E7%BA%A7%E8%BA%AB%E4%BB%BD%E9%AA%8C%E8%AF%81%E6%A8%A1%E5%9E%8B)
- [L1 身份验证 - 私钥](https://docs.polymarket.com/cn/api-reference/authentication#l1-%E8%BA%AB%E4%BB%BD%E9%AA%8C%E8%AF%81-%E7%A7%81%E9%92%A5)
- [L2 身份验证 - API 凭证](https://docs.polymarket.com/cn/api-reference/authentication#l2-%E8%BA%AB%E4%BB%BD%E9%AA%8C%E8%AF%81-api-%E5%87%AD%E8%AF%81)
- [获取 API 凭证](https://docs.polymarket.com/cn/api-reference/authentication#%E8%8E%B7%E5%8F%96-api-%E5%87%AD%E8%AF%81)
- [使用 SDK - 推荐](https://docs.polymarket.com/cn/api-reference/authentication#%E4%BD%BF%E7%94%A8-sdk-%E6%8E%A8%E8%8D%90)
- [使用 REST API](https://docs.polymarket.com/cn/api-reference/authentication#%E4%BD%BF%E7%94%A8-rest-api)
- [L2 身份验证 Header](https://docs.polymarket.com/cn/api-reference/authentication#l2-%E8%BA%AB%E4%BB%BD%E9%AA%8C%E8%AF%81-header)
- [CLOB 客户端 - L2](https://docs.polymarket.com/cn/api-reference/authentication#clob-%E5%AE%A2%E6%88%B7%E7%AB%AF-l2)
- [签名类型和 Funder](https://docs.polymarket.com/cn/api-reference/authentication#%E7%AD%BE%E5%90%8D%E7%B1%BB%E5%9E%8B%E5%92%8C-funder)
- [安全最佳实践](https://docs.polymarket.com/cn/api-reference/authentication#%E5%AE%89%E5%85%A8%E6%9C%80%E4%BD%B3%E5%AE%9E%E8%B7%B5)
- [故障排除](https://docs.polymarket.com/cn/api-reference/authentication#%E6%95%85%E9%9A%9C%E6%8E%92%E9%99%A4)
- [下一步](https://docs.polymarket.com/cn/api-reference/authentication#%E4%B8%8B%E4%B8%80%E6%AD%A5)

CLOB API 使用两级身份验证：\*\*L1（私钥）\*\*和 **L2（API Key）**。两种方式都可以通过 CLOB 客户端或 REST API 完成。

## [​](https://docs.polymarket.com/cn/api-reference/authentication\#%E5%85%AC%E5%BC%80-vs-%E9%9C%80%E8%A6%81%E9%AA%8C%E8%AF%81)  公开 vs 需要验证

## 公开（无需验证）

**Gamma API**、 **Data API** 和 CLOB 读取端点（订单簿、价格、价差）不需要身份验证。

## 需要验证（CLOB）

CLOB 交易端点（下单、撤单、心跳）需要全部 5 个 `POLY_*` L2 HTTP header。

* * *

## [​](https://docs.polymarket.com/cn/api-reference/authentication\#%E4%B8%A4%E7%BA%A7%E8%BA%AB%E4%BB%BD%E9%AA%8C%E8%AF%81%E6%A8%A1%E5%9E%8B)  两级身份验证模型

CLOB 使用两级身份验证：L1（私钥）和 L2（API Key）。两种方式都可以通过 CLOB 客户端或 REST API 完成。

### [​](https://docs.polymarket.com/cn/api-reference/authentication\#l1-%E8%BA%AB%E4%BB%BD%E9%AA%8C%E8%AF%81-%E7%A7%81%E9%92%A5)  L1 身份验证 - 私钥

L1 身份验证使用钱包的私钥签署一个 EIP-712 消息，用于请求头。它证明了对私钥的所有权和控制权。私钥始终由用户控制，所有交易活动都是非托管的。**用于：**

- 创建 API 凭证
- 派生现有的 API 凭证
- 本地签署和创建用户订单

### [​](https://docs.polymarket.com/cn/api-reference/authentication\#l2-%E8%BA%AB%E4%BB%BD%E9%AA%8C%E8%AF%81-api-%E5%87%AD%E8%AF%81)  L2 身份验证 - API 凭证

L2 使用从 L1 身份验证生成的 API 凭证（apiKey、secret、passphrase）。这些仅用于验证发送到 CLOB API 的请求。请求使用 HMAC-SHA256 签名。**用于：**

- 取消或获取用户的活跃订单
- 检查用户的余额和授权
- 提交用户签名的订单

即使使用了 L2 身份验证 header，创建用户订单的方法仍然需要用户签署订单 payload。

* * *

## [​](https://docs.polymarket.com/cn/api-reference/authentication\#%E8%8E%B7%E5%8F%96-api-%E5%87%AD%E8%AF%81)  获取 API 凭证

在发送需要验证的请求之前，你需要使用 L1 身份验证获取 API 凭证。

### [​](https://docs.polymarket.com/cn/api-reference/authentication\#%E4%BD%BF%E7%94%A8-sdk-%E6%8E%A8%E8%8D%90)  使用 SDK - 推荐

- TypeScript

- Python


复制

询问AI

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

复制

询问AI

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

\*\*永远不要将私钥提交到版本控制系统。\*\*请始终使用环境变量或安全的密钥管理系统。

### [​](https://docs.polymarket.com/cn/api-reference/authentication\#%E4%BD%BF%E7%94%A8-rest-api)  使用 REST API

虽然我们强烈建议使用提供的客户端来处理签名和身份验证，但以下内容适用于选择不使用 [Python](https://github.com/Polymarket/py-clob-client) 或 [TypeScript](https://github.com/Polymarket/clob-client) 客户端的开发者。**创建 API 凭证**

复制

询问AI

```
POST https://clob.polymarket.com/auth/api-key
```

**派生 API 凭证**

复制

询问AI

```
GET https://clob.polymarket.com/auth/derive-api-key
```

所需的 L1 header：

| Header | 说明 |
| --- | --- |
| `POLY_ADDRESS` | Polygon 签名者地址 |
| `POLY_SIGNATURE` | CLOB EIP-712 签名 |
| `POLY_TIMESTAMP` | 当前 UNIX 时间戳 |
| `POLY_NONCE` | Nonce（默认值: 0） |

`POLY_SIGNATURE` 通过签署以下 EIP-712 结构生成：

EIP-712 签名示例

TypeScript

Python

复制

询问AI

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

参考实现：

- [TypeScript](https://github.com/Polymarket/clob-client/blob/main/src/signing/eip712.ts)
- [Python](https://github.com/Polymarket/py-clob-client/blob/main/py_clob_client/signing/eip712.py)

响应：

复制

询问AI

```
{
  "apiKey": "550e8400-e29b-41d4-a716-446655440000",
  "secret": "base64EncodedSecretString",
  "passphrase": "randomPassphraseString"
}
```

**L2 身份验证需要这三个值。**

* * *

## [​](https://docs.polymarket.com/cn/api-reference/authentication\#l2-%E8%BA%AB%E4%BB%BD%E9%AA%8C%E8%AF%81-header)  L2 身份验证 Header

所有交易端点需要以下 5 个 header：

| Header | 说明 |
| --- | --- |
| `POLY_ADDRESS` | Polygon 签名者地址 |
| `POLY_SIGNATURE` | 请求的 HMAC 签名 |
| `POLY_TIMESTAMP` | 当前 UNIX 时间戳 |
| `POLY_API_KEY` | 用户的 API `apiKey` 值 |
| `POLY_PASSPHRASE` | 用户的 API `passphrase` 值 |

L2 的 `POLY_SIGNATURE` 是使用用户 API 凭证的 `secret` 值创建的 HMAC-SHA256 签名。参考实现可在 [TypeScript](https://github.com/Polymarket/clob-client/blob/main/src/signing/hmac.ts) 和 [Python](https://github.com/Polymarket/py-clob-client/blob/main/py_clob_client/signing/hmac.py) 客户端中找到。

### [​](https://docs.polymarket.com/cn/api-reference/authentication\#clob-%E5%AE%A2%E6%88%B7%E7%AB%AF-l2)  CLOB 客户端 - L2

- TypeScript

- Python


复制

询问AI

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

复制

询问AI

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

即使使用了 L2 身份验证 header，创建用户订单的方法仍然需要用户签署订单 payload。

* * *

## [​](https://docs.polymarket.com/cn/api-reference/authentication\#%E7%AD%BE%E5%90%8D%E7%B1%BB%E5%9E%8B%E5%92%8C-funder)  签名类型和 Funder

初始化 L2 客户端时，你必须指定钱包的 **signatureType** 和持有资金的 **funder** 地址：

| 签名类型 | 值 | 说明 |
| --- | --- | --- |
| EOA | `0` | 标准 Ethereum 钱包（MetaMask）。Funder 即 EOA 地址，需要 POL 来支付链上交易的 gas 费。 |
| POLY\_PROXY | `1` | 仅用于通过 Magic Link 邮箱/Google 登录的用户的自定义代理钱包。使用此类型需要用户从 Polymarket.com 导出私钥并导入到你的应用中。 |
| GNOSIS\_SAFE | `2` | Gnosis Safe 多签代理钱包（最常见）。对于不属于其他两种类型的新用户或回归用户，请使用此类型。 |

Polymarket.com 上显示给用户的钱包地址是代理钱包地址，应作为 funder 使用。这些地址可以确定性地派生，或者你可以代表用户部署它们。这些代理钱包会在用户首次登录 Polymarket.com 时自动部署。

* * *

## [​](https://docs.polymarket.com/cn/api-reference/authentication\#%E5%AE%89%E5%85%A8%E6%9C%80%E4%BD%B3%E5%AE%9E%E8%B7%B5)  安全最佳实践

永远不要暴露私钥

将私钥存储在环境变量或安全的密钥管理系统中。永远不要将它们提交到版本控制系统。

复制

询问AI

```
# .env (never commit this file)
PRIVATE_KEY=0x...
```

在服务器端实现请求签名

永远不要在客户端代码中暴露你的 API secret。所有需要身份验证的请求都应从你的后端发起。

* * *

## [​](https://docs.polymarket.com/cn/api-reference/authentication\#%E6%95%85%E9%9A%9C%E6%8E%92%E9%99%A4)  故障排除

错误 \- INVALID\_SIGNATURE

你的钱包私钥不正确或格式不对。**解决方案：**

- 验证你的私钥是有效的十六进制字符串（以 “0x” 开头）
- 确保你使用的是目标地址对应的正确密钥
- 检查密钥是否具有正确的权限

错误 \- NONCE\_ALREADY\_USED

你提供的 nonce 已被用于创建 API key。**解决方案：**

- 使用相同的 nonce 调用 `deriveApiKey()` 来获取现有凭证
- 或使用不同的 nonce 调用 `createApiKey()`

错误 \- Invalid Funder Address

你的 funder 地址不正确或与你的钱包不匹配。\*\*解决方案：\*\*在 [polymarket.com/settings](https://polymarket.com/settings) 查看你的 Polymarket 个人资料地址。如果地址不存在或用户从未登录过 Polymarket.com，请先部署地址，然后再创建 L2 身份验证。

凭证和 nonce 都丢失了

很遗憾，没有 nonce 就无法恢复丢失的 API 凭证。你需要创建新的凭证：

复制

询问AI

```
// Create fresh credentials with a new nonce
const newCreds = await client.createApiKey();
// Save the nonce this time!
```

* * *

## [​](https://docs.polymarket.com/cn/api-reference/authentication\#%E4%B8%8B%E4%B8%80%E6%AD%A5)  下一步

[**下你的第一笔订单** \\
\\
了解如何创建和提交订单。](https://docs.polymarket.com/trading/quickstart)

[**地区限制** \\
\\
按地区检查交易可用性。](https://docs.polymarket.com/api-reference/geoblock)

此页面对您有帮助吗？

是否

[简介\\
\\
上一页](https://docs.polymarket.com/cn/api-reference/introduction) [速率限制\\
\\
下一页](https://docs.polymarket.com/cn/api-reference/rate-limits)

Ctrl+I

助手

AI生成的回答可能包含错误。