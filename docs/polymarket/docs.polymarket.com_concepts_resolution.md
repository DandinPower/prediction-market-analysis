---
url: "https://docs.polymarket.com/concepts/resolution"
title: "Resolution - Polymarket Documentation"
---

[Skip to main content](https://docs.polymarket.com/concepts/resolution#content-area)

[Polymarket Documentation home page![light logo](https://mintcdn.com/polymarket-292d1b1b/ZibMe6Tli_amZald/logo/light.svg?fit=max&auto=format&n=ZibMe6Tli_amZald&q=85&s=9f9bd559f02181495794661ef6426c0f)![dark logo](https://mintcdn.com/polymarket-292d1b1b/ZibMe6Tli_amZald/logo/dark.svg?fit=max&auto=format&n=ZibMe6Tli_amZald&q=85&s=13abc6754579a3475368ea99d0f5a241)](https://docs.polymarket.com/)

![US](https://d3gk2c5xim1je2.cloudfront.net/flags/US.svg)

English

Search...

Ctrl KAsk AI

Search...

Navigation

Core Concepts

Resolution

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

- [Resolution Rules](https://docs.polymarket.com/concepts/resolution#resolution-rules)
- [After Resolution](https://docs.polymarket.com/concepts/resolution#after-resolution)
- [Redeeming Tokens](https://docs.polymarket.com/concepts/resolution#redeeming-tokens)
- [Clarifications](https://docs.polymarket.com/concepts/resolution#clarifications)
- [Resolution Timeline](https://docs.polymarket.com/concepts/resolution#resolution-timeline)
- [Contract Addresses](https://docs.polymarket.com/concepts/resolution#contract-addresses)
- [Resources](https://docs.polymarket.com/concepts/resolution#resources)
- [Next Steps](https://docs.polymarket.com/concepts/resolution#next-steps)

When the outcome of an event becomes known, the market is **resolved**. Resolution determines which outcome won, allowing holders of winning tokens to redeem them for $1 each. Losing tokens become worthless.Polymarket uses the **UMA Optimistic Oracle** for decentralized, permissionless resolution. Anyone can propose an outcome, and anyone can dispute it if they believe it’s incorrect.

![](https://mintcdn.com/polymarket-292d1b1b/FOMte3ewbG-LVy3k/images/core-concepts/resolution-lifecycle.png?fit=max&auto=format&n=FOMte3ewbG-LVy3k&q=85&s=6726569af3efd6f4fda54528c8eb0d0a)![](https://mintcdn.com/polymarket-292d1b1b/FOMte3ewbG-LVy3k/images/dark/core-concepts/resolution-lifecycle.png?fit=max&auto=format&n=FOMte3ewbG-LVy3k&q=85&s=36e91c655f7f50b18dea3a23b44f8c23)

## [​](https://docs.polymarket.com/concepts/resolution\#resolution-rules)  Resolution Rules

Every market has pre-defined resolution rules that specify:

- **Resolution source** — Where the outcome will be determined from (e.g., official announcements, specific websites)
- **End date** — When the market is eligible for resolution
- **Edge cases** — How ambiguous situations should be handled

Always read the resolution rules before trading. The market title describes
the question, but the **rules** define how it resolves.

1

[Navigate to header](https://docs.polymarket.com/concepts/resolution#)

Proposal

Anyone can propose a resolution by:

1. Selecting the winning outcome
2. Posting a bond (typically $750 USDC.e)
3. Submitting the proposal to the UMA Oracle

If the proposal is correct and undisputed, the proposer receives their bond back plus a reward.

If you propose incorrectly or too early, you lose your entire bond. Only
propose if you’re confident in the outcome and understand the process.

2

[Navigate to header](https://docs.polymarket.com/concepts/resolution#)

Challenge Period

After a proposal, there’s a **2-hour challenge period** where anyone can dispute the outcome.

- **If no dispute**: The proposal is accepted and the market resolves
- **If disputed**: A new proposal round begins. If the second proposal is also disputed, the resolution escalates to UMA’s DVM (Data Verification Mechanism) for a token holder vote.

There are three possible resolution flows:

1. **No dispute** — Propose then Resolve (fastest, ~2 hours)
2. **One dispute** — Propose, Challenge, second Propose, Resolve (second proposal accepted)
3. **Two disputes** — Propose, Challenge, second Propose, second Challenge, Resolve via DVM vote

3

[Navigate to header](https://docs.polymarket.com/concepts/resolution#)

Dispute - If Challenged

To dispute a proposal:

1. Post a counter-bond (same amount as proposer, typically $750)
2. The dispute triggers a new proposal round, or if already in the second round, a debate period

During the **24-48 hour debate period**, evidence can be submitted in UMA’s Discord channels (`#evidence-rationale` and `#voting-discussion`).

4

[Navigate to header](https://docs.polymarket.com/concepts/resolution#)

UMA Vote

After the debate period, UMA token holders vote on the correct outcome. The voting process takes approximately 48 hours.

| Outcome | Result | Bond Distribution |
| --- | --- | --- |
| **Proposer wins** | Original proposal accepted | Proposer gets bond back + half of disputer’s bond |
| **Disputer wins** | Proposal rejected, new proposal needed | Disputer gets bond back + half of proposer’s bond |
| **Too Early** | Event hasn’t concluded yet | Disputer gets bond back + half of proposer’s bond |
| **Unknown/50-50** | Neither outcome applicable (rare) | Market resolves 50/50 — each token redeems for $0.50; disputer gets bond back + half of proposer’s bond |

## [​](https://docs.polymarket.com/concepts/resolution\#after-resolution)  After Resolution

Once a market resolves:

- **Trading stops** — You can no longer buy or sell tokens for this market
- **Winning tokens** become redeemable for $1.00 each
- **Losing tokens** become worthless ($0.00)

### [​](https://docs.polymarket.com/concepts/resolution\#redeeming-tokens)  Redeeming Tokens

After resolution, call the `redeemPositions` function on the CTF contract to exchange winning tokens for USDC.e. The contract burns your tokens and returns the corresponding collateral.

Copy

Ask AI

```
100 winning tokens → $100 USDC.e
```

## [​](https://docs.polymarket.com/concepts/resolution\#clarifications)  Clarifications

In rare cases, unforeseen circumstances require clarification of the rules after trading begins. Polymarket may issue an **“Additional context”** update that proposers and voters should consider during resolution.Clarifications:

- Cannot change the fundamental intent of the question
- Are published onchain via the bulletin board contract
- Should be considered by UMA voters when resolving disputes

If you believe a clarification is needed, request it in the [Polymarket\\
Discord](https://discord.com/invite/polymarket)`#market-review` channel.

## [​](https://docs.polymarket.com/concepts/resolution\#resolution-timeline)  Resolution Timeline

| Phase | Duration |
| --- | --- |
| Challenge period | 2 hours |
| Debate period (if disputed) | 24-48 hours |
| UMA voting (if disputed) | ~48 hours |

**Undisputed resolution**: ~2 hours after proposal**Disputed resolution**: 4-6 days total

## [​](https://docs.polymarket.com/concepts/resolution\#contract-addresses)  Contract Addresses

| Contract | Address | Network |
| --- | --- | --- |
| **UmaCtfAdapter v3.0** | `0x157Ce2d672854c848c9b79C49a8Cc6cc89176a49` | Polygon Mainnet |
| **UmaCtfAdapter v2.0** | `0x6A9D222616C90FcA5754cd1333cFD9b7fb6a4F74` | Polygon Mainnet |
| **UmaCtfAdapter v1.0** | `0xCB1822859cEF82Cd2Eb4E6276C7916e692995130` | Polygon Mainnet |

## [​](https://docs.polymarket.com/concepts/resolution\#resources)  Resources

- [UMA Oracle Portal](https://oracle.uma.xyz/) — View and interact with proposals
- [UMA Documentation](https://docs.uma.xyz/) — Learn more about the Optimistic Oracle
- [Polymarket Discord](https://discord.com/invite/polymarket) — Discuss resolutions and request clarifications
- [UmaCtfAdapter Source Code](https://github.com/Polymarket/uma-ctf-adapter) — Smart contract source
- [UmaCtfAdapter Audit](https://github.com/Polymarket/uma-ctf-adapter/blob/main/audit/Polymarket_UMA_Optimistic_Oracle_Adapter_Audit.pdf) — Security audit report

## [​](https://docs.polymarket.com/concepts/resolution\#next-steps)  Next Steps

[**Positions & Tokens** \\
\\
Learn how to redeem winning tokens after resolution.](https://docs.polymarket.com/concepts/positions-tokens)

[**Markets & Events** \\
\\
Understand how markets are structured.](https://docs.polymarket.com/concepts/markets-events)

Was this page helpful?

YesNo

[Order Lifecycle\\
\\
Previous](https://docs.polymarket.com/concepts/order-lifecycle) [Overview\\
\\
Next](https://docs.polymarket.com/market-data/overview)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.

Suggestions

How do I connect to WebSocket streams?What's required to place my first order?How do I find and fetch market data?

![](https://mintcdn.com/polymarket-292d1b1b/FOMte3ewbG-LVy3k/images/core-concepts/resolution-lifecycle.png?w=840&fit=max&auto=format&n=FOMte3ewbG-LVy3k&q=85&s=24bff0e4be1cc3925c8022751d08331f)

![](https://mintcdn.com/polymarket-292d1b1b/FOMte3ewbG-LVy3k/images/dark/core-concepts/resolution-lifecycle.png?w=840&fit=max&auto=format&n=FOMte3ewbG-LVy3k&q=85&s=46354d72ab1341abb004e10cfff79ae6)