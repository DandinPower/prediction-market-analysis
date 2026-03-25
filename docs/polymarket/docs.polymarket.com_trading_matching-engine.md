---
url: "https://docs.polymarket.com/trading/matching-engine"
title: "Matching Engine Restarts - Polymarket Documentation"
---

[Skip to main content](https://docs.polymarket.com/trading/matching-engine#content-area)

[Polymarket Documentation home page![light logo](https://mintcdn.com/polymarket-292d1b1b/ZibMe6Tli_amZald/logo/light.svg?fit=max&auto=format&n=ZibMe6Tli_amZald&q=85&s=9f9bd559f02181495794661ef6426c0f)![dark logo](https://mintcdn.com/polymarket-292d1b1b/ZibMe6Tli_amZald/logo/dark.svg?fit=max&auto=format&n=ZibMe6Tli_amZald&q=85&s=13abc6754579a3475368ea99d0f5a241)](https://docs.polymarket.com/)

![US](https://d3gk2c5xim1je2.cloudfront.net/flags/US.svg)

English

Search...

Ctrl KAsk AI

Search...

Navigation

Trading

Matching Engine Restarts

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

- [Restart Schedule](https://docs.polymarket.com/trading/matching-engine#restart-schedule)
- [Announcements](https://docs.polymarket.com/trading/matching-engine#announcements)
- [Handling HTTP 425](https://docs.polymarket.com/trading/matching-engine#handling-http-425)
- [Recommended Retry Strategy](https://docs.polymarket.com/trading/matching-engine#recommended-retry-strategy)
- [Code Examples](https://docs.polymarket.com/trading/matching-engine#code-examples)
- [Best Practices](https://docs.polymarket.com/trading/matching-engine#best-practices)

The Polymarket matching engine undergoes periodic restarts for maintenance and upgrades. This page covers the restart schedule, how to detect and handle downtime, and where to get advance notice of changes.

* * *

## [​](https://docs.polymarket.com/trading/matching-engine\#restart-schedule)  Restart Schedule

The matching engine restarts **weekly on Tuesdays at 7:00 AM ET**. During a restart window, the engine is temporarily unavailable — typically for about **90 seconds**.

|  | Details |
| --- | --- |
| **Cadence** | Weekly |
| **Day & time** | Tuesday, 7:00 AM ET |
| **Typical duration** | ~90 seconds |
| **What happens** | Order matching is paused, API returns `425` |

Unscheduled restarts may occur for critical updates or hotfixes. These are announced with as much advance notice as possible.

* * *

## [​](https://docs.polymarket.com/trading/matching-engine\#announcements)  Announcements

Matching engine changes — planned restarts, updates, and maintenance windows — are announced **before they happen** in these channels:

[**Telegram** \\
\\
Join the Polymarket Trading APIs channel for real-time announcements.](https://t.me/polytradingapis)

[**Discord** \\
\\
Join the #trading-apis channel in the Polymarket Discord.](https://discord.com/channels/710897173927297116/1473553279421255803)

Announcements typically include **what’s changing**, the **scheduled time**, and the **expected downtime window**. The goal is ~2 days notice when possible.

* * *

## [​](https://docs.polymarket.com/trading/matching-engine\#handling-http-425)  Handling HTTP 425

During a restart window, the CLOB API returns **HTTP 425 (Too Early)** on all order-related endpoints. This tells your client that the matching engine is restarting and will be back shortly.

### [​](https://docs.polymarket.com/trading/matching-engine\#recommended-retry-strategy)  Recommended Retry Strategy

1

[Navigate to header](https://docs.polymarket.com/trading/matching-engine#)

Detect 425

When you receive an HTTP `425` response, the matching engine is restarting. Do not treat this as a permanent error.

2

[Navigate to header](https://docs.polymarket.com/trading/matching-engine#)

Back off and retry

Wait and retry with exponential backoff. Start at 1–2 seconds and increase the interval on each retry.

3

[Navigate to header](https://docs.polymarket.com/trading/matching-engine#)

Resume normal operation

Once you receive a successful response, the engine is back online. Resume normal order flow.

### [​](https://docs.polymarket.com/trading/matching-engine\#code-examples)  Code Examples

Check the HTTP status code on responses to the CLOB API and retry on `425`:

TypeScript

Python

Rust

Copy

Ask AI

```
const CLOB_HOST = "https://clob.polymarket.com";

async function postWithRetry(path: string, body: any, headers: Record<string, string>) {
  const MAX_RETRIES = 10;
  let delay = 1000;

  for (let attempt = 0; attempt < MAX_RETRIES; attempt++) {
    const response = await fetch(`${CLOB_HOST}${path}`, {
      method: "POST",
      headers: { "Content-Type": "application/json", ...headers },
      body: JSON.stringify(body),
    });

    if (response.status === 425) {
      console.log(`Engine restarting, retrying in ${delay / 1000}s...`);
      await new Promise((r) => setTimeout(r, delay));
      delay = Math.min(delay * 2, 30000);
      continue;
    }

    return response;
  }
  throw new Error("Engine restart exceeded maximum retry attempts");
}
```

* * *

## [​](https://docs.polymarket.com/trading/matching-engine\#best-practices)  Best Practices

- **Subscribe to announcement channels** — get notified before restarts happen so you can prepare
- **Handle 425 gracefully** — treat it as a temporary condition, not an error; your retry logic should resume automatically
- **Avoid aggressive retries** — the engine needs time to reload orderbooks; rapid-fire retries won’t speed things up and may hit rate limits once the engine is back
- **Log restart events** — track when your client encounters 425s to correlate with announced maintenance windows

Was this page helpful?

YesNo

[Negative Risk Markets\\
\\
Previous](https://docs.polymarket.com/advanced/neg-risk) [Conditional Token Framework\\
\\
Next](https://docs.polymarket.com/trading/ctf/overview)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.

Suggestions

How do I connect to WebSocket streams?What's required to place my first order?How do I find and fetch market data?