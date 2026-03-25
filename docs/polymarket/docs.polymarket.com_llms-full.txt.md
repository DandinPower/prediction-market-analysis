---
url: "https://docs.polymarket.com/llms-full.txt"
title: undefined
---

\# Negative Risk Markets
Source: https://docs.polymarket.com/advanced/neg-risk

Capital-efficient trading for multi-outcome events

\*\*Negative risk\*\* is a mechanism for multi-outcome events where only one outcome can win. It enables capital-efficient trading by allowing positions across all outcomes within an event to be related through a \*\*conversion\*\* operation.

\## How It Works

In a standard multi-outcome event, each market is independent. If you want to bet against one outcome, you must buy that outcome's No tokens—but those No tokens have no relationship to the other outcomes.

Negative risk changes this. In a neg risk event:

\\* A \*\*No share\*\* in any market can be converted into \*\*1 Yes share in every other market\*\*
\\* This conversion happens through the Neg Risk Adapter contract

\### Example

Consider an event: "Who will win the 2024 Presidential Election?" with three outcomes:

\| Outcome \| Your Position \|
\| \-\-\-\-\-\-\- \| \-\-\-\-\-\-\-\-\-\-\-\-\- \|
\| Trump \| — \|
\| Harris \| — \|
\| Other \| 1 No \|

With negative risk, that 1 No on "Other" can be converted into:

\| Outcome \| After Conversion \|
\| \-\-\-\-\-\-\- \| \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- \|
\| Trump \| 1 Yes \|
\| Harris \| 1 Yes \|
\| Other \| — \|

This is capital-efficient because betting against one outcome is economically equivalent to betting \*for\* all other outcomes.

\## Identifying Neg Risk Markets

The Gamma API includes a \`negRisk\` boolean on events and markets:

\`\`\`json theme={null}
{
 "id": "123",
 "title": "Who will win the 2024 Presidential Election?",
 "negRisk": true,
 "markets": \[...\]
}
\`\`\`

When placing orders on neg risk markets, you must specify this in your order options:

\`\`\`typescript theme={null}
const response = await client.createAndPostOrder(
 {
 tokenID: "TOKEN\_ID",
 price: 0.5,
 size: 100,
 side: Side.BUY,
 },
 {
 tickSize: "0.01",
 negRisk: true, // Required for neg risk markets
 },
);
\`\`\`

\## Contract Addresses

Neg risk markets use different contracts than standard markets:

See \[Contract Addresses\](/resources/contract-addresses) for the Neg Risk Adapter and Neg Risk CTF Exchange addresses.

\## Augmented Negative Risk

Standard negative risk requires the complete set of outcomes to be known at market creation. But sometimes new outcomes emerge after trading begins (e.g., a new candidate enters a race).

\*\*Augmented negative risk\*\* solves this with:

\| Outcome Type \| Description \|
\| \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- \| \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- \|
\| \*\*Named outcomes\*\* \| Known outcomes (e.g., "Trump", "Harris") \|
\| \*\*Placeholder outcomes\*\* \| Reserved slots that can be clarified later (e.g., "Person A") \|
\| \*\*Explicit Other\*\* \| Catches any outcome not explicitly named \|

\### How Placeholders Work

1\. Event launches with named outcomes + placeholders + "Other"
2\. When a new outcome emerges, a placeholder is clarified via the bulletin board
3\. The "Other" definition narrows as placeholders are assigned

\### Trading Rules for Augmented Neg Risk

 Only trade on \*\*named outcomes\*\*. Placeholder outcomes should be ignored until
 they are named or until resolution occurs. The Polymarket UI does not display
 unnamed outcomes.

\\* If the correct outcome at resolution is not named, the market resolves to "Other"
\\* The "Other" outcome's definition changes as placeholders are clarified—avoid trading it directly

\### Identifying Augmented Neg Risk

An event is augmented neg risk when both flags are true:

\`\`\`json theme={null}
{
 "enableNegRisk": true,
 "negRiskAugmented": true
}
\`\`\`

 The Gamma API includes a boolean field \`negRisk\` on events and markets, which indicates whether the event uses negative risk. For augmented neg risk events, an additional \`enableNegRisk\` field is also \`true\`. When placing orders, the SDK option is always \`negRisk: true\` / \`neg\_risk: True\` regardless of whether the market is standard or augmented neg risk.

\## Technical Details

\### Conversion Mechanics

The conversion operation is atomic and happens through the Neg Risk Adapter:

1\. You hold 1 No token for Outcome A
2\. Call the convert function on the adapter
3\. You receive 1 Yes token for every other outcome in the event

\## Resources

\\* \[Neg Risk Adapter Source Code\](https://github.com/Polymarket/neg-risk-ctf-adapter)
\\* \[Gamma API Documentation\](/market-data/overview)

\## Next Steps

 Understand how multi-market events are structured.

 Learn about token operations like split, merge, and redeem.


\# Authentication
Source: https://docs.polymarket.com/api-reference/authentication

How to authenticate requests to the CLOB API

The CLOB API uses two levels of authentication: \*\*L1 (Private Key)\*\* and \*\*L2 (API Key)\*\*. Either can be accomplished using the CLOB client or REST API.

\## Public vs Authenticated

 The \*\*Gamma API\*\*, \*\*Data API\*\*, and CLOB read endpoints (orderbook, prices, spreads) require no authentication.

 CLOB trading endpoints (placing orders, cancellations, heartbeat) require all 5 \`POLY\_\*\` L2 HTTP headers.


\\*\\*\\*

\## Two-Level Authentication Model

The CLOB uses two levels of authentication: L1 (Private Key) and L2 (API Key). Either can be accomplished using the CLOB client or REST API

\### L1 Authentication

L1 authentication uses the wallet's private key to sign an EIP-712 message used in the request header. It proves ownership and control over the private key. The private key stays in control of the user and all trading activity remains non-custodial.

\*\*Used for:\*\*

\\* Creating API credentials
\\* Deriving existing API credentials
\\* Signing and creating user's orders locally

\### L2 Authentication

L2 uses API credentials (apiKey, secret, passphrase) generated from L1 authentication. These are used solely to authenticate requests made to the CLOB API. Requests are signed using HMAC-SHA256.

\*\*Used for:\*\*

\\* Cancel or get user's open orders
\\* Check user's balances and allowances
\\* Post user's signed orders

 Even with L2 authentication headers, methods that create user orders still
 require the user to sign the order payload.

\\*\\*\\*

\## Getting API Credentials

Before making authenticated requests, you need to obtain API credentials using L1 authentication.

\### Using the SDK

 \`\`\`typescript theme={null}
 import { ClobClient } from "@polymarket/clob-client";
 import { Wallet } from "ethers"; // v5.8.0

 const client = new ClobClient(
 "https://clob.polymarket.com",
 137, // Polygon mainnet
 new Wallet(process.env.PRIVATE\_KEY)
 );

 // Creates new credentials or derives existing ones
 const credentials = await client.createOrDeriveApiKey();

 console.log(credentials);
 // {
 // apiKey: "550e8400-e29b-41d4-a716-446655440000",
 // secret: "base64EncodedSecretString",
 // passphrase: "randomPassphraseString"
 // }
 \`\`\`

 \`\`\`python theme={null}
 from py\_clob\_client.client import ClobClient
 import os

 client = ClobClient(
 host="https://clob.polymarket.com",
 chain\_id=137, # Polygon mainnet
 key=os.getenv("PRIVATE\_KEY")
 )

 # Creates new credentials or derives existing ones
 credentials = client.create\_or\_derive\_api\_creds()

 print(credentials)
 # {
 # "apiKey": "550e8400-e29b-41d4-a716-446655440000",
 # "secret": "base64EncodedSecretString",
 # "passphrase": "randomPassphraseString"
 # }
 \`\`\`

 \`\`\`rust theme={null}
 use std::str::FromStr;
 use polymarket\_client\_sdk::POLYGON;
 use polymarket\_client\_sdk::auth::{LocalSigner, Signer};
 use polymarket\_client\_sdk::clob::{Client, Config};

 let private\_key = std::env::var("POLYMARKET\_PRIVATE\_KEY")?;
 let signer = LocalSigner::from\_str(&private\_key)?
 .with\_chain\_id(Some(POLYGON));

 // Creates new credentials or derives existing ones,
 // then initializes the authenticated client — all in one step
 let client = Client::new("https://clob.polymarket.com", Config::default())?
 .authentication\_builder(&signer)
 .authenticate()
 .await?;

 let credentials = client.credentials();
 println!("API Key: {}", credentials.key());
 \`\`\`

 \*\*Never commit private keys to version control.\*\* Always use environment
 variables or secure key management systems.

\### Using the REST API

While we highly recommend using our provided clients to handle signing and authentication, the following is for developers who choose NOT to use our \[Python\](https://github.com/Polymarket/py-clob-client) or \[TypeScript\](https://github.com/Polymarket/clob-client) clients.

\*\*Create API Credentials\*\*

\`\`\`bash theme={null}
POST https://clob.polymarket.com/auth/api-key
\`\`\`

\*\*Derive API Credentials\*\*

\`\`\`bash theme={null}
GET https://clob.polymarket.com/auth/derive-api-key
\`\`\`

Required L1 headers:

\| Header \| Description \|
\| \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- \| \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- \|
\| \`POLY\_ADDRESS\` \| Polygon signer address \|
\| \`POLY\_SIGNATURE\` \| CLOB EIP-712 signature \|
\| \`POLY\_TIMESTAMP\` \| Current UNIX timestamp \|
\| \`POLY\_NONCE\` \| Nonce (default: 0) \|

The \`POLY\_SIGNATURE\` is generated by signing the following EIP-712 struct:

 \`\`\`typescript TypeScript theme={null}
 const domain = {
 name: "ClobAuthDomain",
 version: "1",
 chainId: chainId, // Polygon Chain ID 137
 };

 const types = {
 ClobAuth: \[\
 { name: "address", type: "address" },\
 { name: "timestamp", type: "string" },\
 { name: "nonce", type: "uint256" },\
 { name: "message", type: "string" },\
 \],
 };

 const value = {
 address: signingAddress, // The Signing address
 timestamp: ts, // The CLOB API server timestamp
 nonce: nonce, // The nonce used
 message: "This message attests that I control the given wallet",
 };

 const sig = await signer.\_signTypedData(domain, types, value);
 \`\`\`

 \`\`\`python Python theme={null}
 domain = {
 "name": "ClobAuthDomain",
 "version": "1",
 "chainId": chainId, # Polygon Chain ID 137
 }

 types = {
 "ClobAuth": \[\
 {"name": "address", "type": "address"},\
 {"name": "timestamp", "type": "string"},\
 {"name": "nonce", "type": "uint256"},\
 {"name": "message", "type": "string"},\
 \]
 }

 value = {
 "address": signingAddress, # The signing address
 "timestamp": ts, # The CLOB API server timestamp
 "nonce": nonce, # The nonce used
 "message": "This message attests that I control the given wallet",
 }

 sig = signer.sign\_typed\_data(domain, types, value)
 \`\`\`


Reference implementations:

\\* \[TypeScript\](https://github.com/Polymarket/clob-client/blob/main/src/signing/eip712.ts)
\\* \[Python\](https://github.com/Polymarket/py-clob-client/blob/main/py\_clob\_client/signing/eip712.py)

Response:

\`\`\`json theme={null}
{
 "apiKey": "550e8400-e29b-41d4-a716-446655440000",
 "secret": "base64EncodedSecretString",
 "passphrase": "randomPassphraseString"
}
\`\`\`

\*\*You'll need all three values for L2 authentication.\*\*

\\*\\*\\*

\## L2 Authentication Headers

All trading endpoints require these 5 headers:

\| Header \| Description \|
\| \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- \| \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- \|
\| \`POLY\_ADDRESS\` \| Polygon signer address \|
\| \`POLY\_SIGNATURE\` \| HMAC signature for request \|
\| \`POLY\_TIMESTAMP\` \| Current UNIX timestamp \|
\| \`POLY\_API\_KEY\` \| User's API \`apiKey\` value \|
\| \`POLY\_PASSPHRASE\` \| User's API \`passphrase\` value \|

The \`POLY\_SIGNATURE\` for L2 is an HMAC-SHA256 signature created using the user's API credentials \`secret\` value. Reference implementations can be found in the \[TypeScript\](https://github.com/Polymarket/clob-client/blob/main/src/signing/hmac.ts) and \[Python\](https://github.com/Polymarket/py-clob-client/blob/main/py\_clob\_client/signing/hmac.py) clients.

\### CLOB Client

 \`\`\`typescript theme={null}
 import { ClobClient } from "@polymarket/clob-client";
 import { Wallet } from "ethers"; // v5.8.0

 const client = new ClobClient(
 "https://clob.polymarket.com",
 137,
 new Wallet(process.env.PRIVATE\_KEY),
 apiCreds, // Generated from L1 auth, API credentials enable L2 methods
 1, // signatureType explained below
 funderAddress // funder explained below
 );

 // Now you can trade!
 const order = await client.createAndPostOrder(
 { tokenID: "123456", price: 0.65, size: 100, side: "BUY" },
 { tickSize: "0.01", negRisk: false }
 );
 \`\`\`

 \`\`\`python theme={null}
 from py\_clob\_client.client import ClobClient
 import os

 client = ClobClient(
 host="https://clob.polymarket.com",
 chain\_id=137,
 key=os.getenv("PRIVATE\_KEY"),
 creds=api\_creds, # Generated from L1 auth, API credentials enable L2 methods
 signature\_type=1, # signatureType explained below
 funder=os.getenv("FUNDER\_ADDRESS") # funder explained below
 )

 # Now you can trade!
 order = client.create\_and\_post\_order(
 {"token\_id": "123456", "price": 0.65, "size": 100, "side": "BUY"},
 {"tick\_size": "0.01", "neg\_risk": False}
 )
 \`\`\`

 \`\`\`rust theme={null}
 use polymarket\_client\_sdk::clob::types::{Side, SignatureType};
 use polymarket\_client\_sdk::types::dec;

 let client = Client::new("https://clob.polymarket.com", Config::default())?
 .authentication\_builder(&signer)
 .signature\_type(SignatureType::Proxy) // signatureType explained below
 // Funder auto-derived via CREATE2 for Proxy/GnosisSafe
 .authenticate()
 .await?;

 // Now you can trade!
 let order = client.limit\_order()
 .token\_id("123456".parse()?)
 .price(dec!(0.65))
 .size(dec!(100))
 .side(Side::Buy)
 .build().await?;
 let signed = client.sign(&signer, order).await?;
 let response = client.post\_order(signed).await?;
 \`\`\`

 Even with L2 authentication headers, methods that create user orders still
 require the user to sign the order payload.

\\*\\*\\*

\## Signature Types and Funder

When initializing the L2 client, you must specify your wallet \*\*signatureType\*\* and the \*\*funder\*\* address which holds the funds:

\| Signature Type \| Value \| Description \|
\| \-\-\-\-\-\-\-\-\-\-\-\-\-\- \| \-\-\-\-\- \| \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- \|
\| EOA \| \`0\` \| Standard Ethereum wallet (MetaMask). Funder is the EOA address and will need POL to pay gas on transactions. \|
\| POLY\\\_PROXY \| \`1\` \| A custom proxy wallet only used with users who logged in via Magic Link email/Google. Using this requires the user to have exported their PK from Polymarket.com and imported into your app. \|
\| GNOSIS\\\_SAFE \| \`2\` \| Gnosis Safe multisig proxy wallet (most common). Use this for any new or returning user who does not fit the other 2 types. \|

 The wallet address displayed to the user on Polymarket.com is the proxy wallet
 and should be used as the funder. These can be deterministically derived or
 you can deploy them on behalf of the user. These proxy wallets are
 automatically deployed for the user on their first login to Polymarket.com.

\\*\\*\\*

\## Security Best Practices

 Store private keys in environment variables or secure key management systems. Never commit them to version control.

 \`\`\`bash theme={null}
 # .env (never commit this file)
 PRIVATE\_KEY=0x...
 \`\`\`

 Never expose your API secret in client-side code. All authenticated requests should originate from your backend.


\\*\\*\\*

\## Troubleshooting

 Your wallet's private key is incorrect or improperly formatted.

 \*\*Solutions:\*\*

 \\* Verify your private key is a valid hex string (starts with "0x")
 \\* Ensure you're using the correct key for the intended address
 \\* Check that the key has proper permissions

 The nonce you provided has already been used to create an API key.

 \*\*Solutions:\*\*

 \\* Use \`deriveApiKey()\` with the same nonce to retrieve existing credentials
 \\* Or use a different nonce with \`createApiKey()\`

 Your funder address is incorrect or doesn't match your wallet.

 \*\*Solution:\*\* Check your Polymarket profile address at \[polymarket.com/settings\](https://polymarket.com/settings).

 If it does not exist or user has never logged into Polymarket.com, deploy it first before creating L2 authentication.

 Unfortunately, there's no way to recover lost API credentials without the nonce. You'll need to create new credentials:

 \`\`\`typescript theme={null}
 // Create fresh credentials with a new nonce
 const newCreds = await client.createApiKey();
 // Save the nonce this time!
 \`\`\`


\\*\\*\\*

\## Next Steps

 Learn how to create and submit orders.

 Check trading availability by region.


\# Clients & SDKs
Source: https://docs.polymarket.com/api-reference/clients-sdks

Official open-source libraries for interacting with Polymarket

Polymarket provides official open-source clients in TypeScript, Python, and Rust. All three support the full CLOB API including market data, order management, and authentication.

\## Installation

 \`\`\`bash TypeScript theme={null}
 npm install @polymarket/clob-client ethers@5
 \`\`\`

 \`\`\`bash Python theme={null}
 pip install py-clob-client
 \`\`\`

 \`\`\`bash Rust theme={null}
 cargo add polymarket-client-sdk
 \`\`\`

\## Quick Example

 \`\`\`typescript TypeScript theme={null}
 import { ClobClient } from "@polymarket/clob-client";

 const client = new ClobClient(
 "https://clob.polymarket.com",
 137,
 signer,
 apiCreds,
 );

 const markets = await client.getMarkets();
 \`\`\`

 \`\`\`python Python theme={null}
 from py\_clob\_client.client import ClobClient

 client = ClobClient(
 "https://clob.polymarket.com",
 key=private\_key,
 chain\_id=137,
 creds=api\_creds,
 )

 markets = client.get\_markets()
 \`\`\`

 \`\`\`rust Rust theme={null}
 use polymarket\_client\_sdk::clob::{Client, Config};

 let client = Client::new("https://clob.polymarket.com", Config::default())?
 .authentication\_builder(&signer)
 .authenticate()
 .await?;

 let markets = client.markets(None).await?;
 \`\`\`

\## Source Code

\| Language \| Package \| Repository \|
\| \-\-\-\-\-\-\-\-\-\- \| \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- \| \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- \|
\| TypeScript \| \`@polymarket/clob-client\` \| \[github.com/Polymarket/clob-client\](https://github.com/Polymarket/clob-client) \|
\| Python \| \`py-clob-client\` \| \[github.com/Polymarket/py-clob-client\](https://github.com/Polymarket/py-clob-client) \|
\| Rust \| \`polymarket-client-sdk\` \| \[github.com/Polymarket/rs-clob-client\](https://github.com/Polymarket/rs-clob-client) \|

Each repository includes working examples in the \`/examples\` directory.

\## Builder SDKs

If you're building an app through the \[Builder Program\](/builders/overview), additional signing SDKs are available:

\| Language \| Package \| Repository \|
\| \-\-\-\-\-\-\-\-\-\- \| \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- \| \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- \|
\| TypeScript \| \`@polymarket/builder-signing-sdk\` \| \[github.com/Polymarket/builder-signing-sdk\](https://github.com/Polymarket/builder-signing-sdk) \|
\| Python \| \`py\_builder\_signing\_sdk\` \| \[github.com/Polymarket/py-builder-signing-sdk\](https://github.com/Polymarket/py-builder-signing-sdk) \|

See \[Order Attribution\](/trading/orders/attribution) for usage details.

\## Relayer SDK

For \[gasless transactions\](/trading/gasless) using proxy wallets, the relayer client handles submitting transactions through Polymarket's relayer:

\| Language \| Package \| Repository \|
\| \-\-\-\-\-\-\-\-\-\- \| \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- \| \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- \|
\| TypeScript \| \`@polymarket/builder-relayer-client\` \| \[github.com/Polymarket/builder-relayer-client\](https://github.com/Polymarket/builder-relayer-client) \|
\| Python \| \`py-builder-relayer-client\` \| \[github.com/Polymarket/py-builder-relayer-client\](https://github.com/Polymarket/py-builder-relayer-client) \|

\## Next Steps

 Set up your client and place your first order.

 Understand L1/L2 auth and API credentials.


\# Get top holders for markets
Source: https://docs.polymarket.com/api-reference/core/get-top-holders-for-markets

/api-spec/data-openapi.yaml get /holders

\# Get midpoint price
Source: https://docs.polymarket.com/api-reference/data/get-midpoint-price

/api-spec/clob-openapi.yaml get /midpoint
Retrieves the midpoint price for a specific token ID.
The midpoint is calculated as the average of the best bid and best ask prices.

\# Get server time
Source: https://docs.polymarket.com/api-reference/data/get-server-time

/api-spec/clob-openapi.yaml get /time
Returns the current Unix timestamp of the server.
This can be used to synchronize client time with server time.

\# Get event by id
Source: https://docs.polymarket.com/api-reference/events/get-event-by-id

/api-spec/gamma-openapi.yaml get /events/{id}

\# Get event by slug
Source: https://docs.polymarket.com/api-reference/events/get-event-by-slug

/api-spec/gamma-openapi.yaml get /events/slug/{slug}

\# Get event tags
Source: https://docs.polymarket.com/api-reference/events/get-event-tags

/api-spec/gamma-openapi.yaml get /events/{id}/tags

\# List events
Source: https://docs.polymarket.com/api-reference/events/list-events

/api-spec/gamma-openapi.yaml get /events

\# Geographic Restrictions
Source: https://docs.polymarket.com/api-reference/geoblock

Check geographic restrictions before placing orders on the Polymarket API

Polymarket restricts order placement from certain geographic locations due to regulatory requirements and compliance with international sanctions. Before placing orders, builders should verify the location.

 Orders submitted from blocked regions will be rejected. Implement geoblock
 checks in your application to provide users with appropriate feedback before
 they attempt to trade.

\\*\\*\\*

\## Geoblock Endpoint

Check the geographic eligibility of the requesting IP address:

\`\`\`bash theme={null}
GET https://polymarket.com/api/geoblock
\`\`\`

This endpoint is on \`polymarket.com\`, not the API servers.

\### Response

\`\`\`json theme={null}
{
 "blocked": true,
 "ip": "203.0.113.42",
 "country": "US",
 "region": "NY"
}
\`\`\`

\| Field \| Type \| Description \|
\| \-\-\-\-\-\-\-\-\- \| \-\-\-\-\-\-\- \| \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- \|
\| \`blocked\` \| boolean \| Whether the user is blocked from placing orders \|
\| \`ip\` \| string \| Detected IP address \|
\| \`country\` \| string \| ISO 3166-1 alpha-2 country code \|
\| \`region\` \| string \| Region/state code \|

\\*\\*\\*

\## Blocked Countries

The following countries are restricted from placing orders on Polymarket. Countries marked as \*\*close-only\*\* can close existing positions but cannot open new ones:

\| Country Code \| Country Name \| Status \|
\| \-\-\-\-\-\-\-\-\-\-\-\- \| \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- \| \-\-\-\-\-\-\-\-\-\- \|
\| AU \| Australia \| Blocked \|
\| BE \| Belgium \| Blocked \|
\| BY \| Belarus \| Blocked \|
\| BI \| Burundi \| Blocked \|
\| CF \| Central African Republic \| Blocked \|
\| CD \| Congo (Kinshasa) \| Blocked \|
\| CU \| Cuba \| Blocked \|
\| DE \| Germany \| Blocked \|
\| ET \| Ethiopia \| Blocked \|
\| FR \| France \| Blocked \|
\| GB \| United Kingdom \| Blocked \|
\| IR \| Iran \| Blocked \|
\| IQ \| Iraq \| Blocked \|
\| IT \| Italy \| Blocked \|
\| KP \| North Korea \| Blocked \|
\| LB \| Lebanon \| Blocked \|
\| LY \| Libya \| Blocked \|
\| MM \| Myanmar \| Blocked \|
\| NI \| Nicaragua \| Blocked \|
\| NL \| Netherlands \| Blocked \|
\| PL \| Poland \| Close-only \|
\| RU \| Russia \| Blocked \|
\| SG \| Singapore \| Close-only \|
\| SO \| Somalia \| Blocked \|
\| SS \| South Sudan \| Blocked \|
\| SD \| Sudan \| Blocked \|
\| SY \| Syria \| Blocked \|
\| TH \| Thailand \| Close-only \|
\| TW \| Taiwan \| Close-only \|
\| UM \| United States Minor Outlying Islands \| Blocked \|
\| US \| United States \| Blocked \|
\| VE \| Venezuela \| Blocked \|
\| YE \| Yemen \| Blocked \|
\| ZW \| Zimbabwe \| Blocked \|

\\*\\*\\*

\## Blocked Regions

In addition to fully blocked countries, the following specific regions within otherwise accessible countries are also restricted:

\| Country \| Region \| Region Code \|
\| \-\-\-\-\-\-\-\-\-\-\-\- \| \-\-\-\-\-\-\- \| \-\-\-\-\-\-\-\-\-\-\- \|
\| Canada (CA) \| Ontario \| ON \|
\| Ukraine (UA) \| Crimea \| 43 \|
\| Ukraine (UA) \| Donetsk \| 14 \|
\| Ukraine (UA) \| Luhansk \| 09 \|

\\*\\*\\*

\## Blocking Logic

The geoblocking system includes:

1\. \*\*OFAC-Sanctioned Countries\*\*: Countries sanctioned by the U.S. Office of Foreign Assets Control (OFAC)
2\. \*\*Additional Regulatory Restrictions\*\*: Countries added for specific regulatory compliance reasons

\\*\\*\\*

\## Server Infrastructure

\\* \*\*Primary Servers\*\*: eu-west-2
\\* \*\*Closest Non-Georestricted Region\*\*: eu-west-1

\\*\\*\\*

\## Usage Examples

 \`\`\`typescript theme={null}
 interface GeoblockResponse {
 blocked: boolean;
 ip: string;
 country: string;
 region: string;
 }

 async function checkGeoblock(): Promise {
 const response = await fetch("https://polymarket.com/api/geoblock");
 return response.json();
 }

 // Usage
 const geo = await checkGeoblock();

 if (geo.blocked) {
 console.log(\`Trading not available in ${geo.country}\`);
 } else {
 console.log("Trading available");
 }
 \`\`\`

 \`\`\`python theme={null}
 import requests

 def check\_geoblock() -> dict:
 response = requests.get("https://polymarket.com/api/geoblock")
 return response.json()

 # Usage
 geo = check\_geoblock()

 if geo\["blocked"\]:
 print(f"Trading not available in {geo\['country'\]}")
 else:
 print("Trading available")
 \`\`\`

 \`\`\`rust theme={null}
 use polymarket\_client\_sdk::clob::Client;

 let client = Client::default();
 let geo = client.check\_geoblock().await?;

 if geo.blocked {
 println!("Trading not available in {}", geo.country);
 } else {
 println!("Trading available");
 }
 \`\`\`


\\*\\*\\*

\## Why These Restrictions

Geographic restrictions are implemented to ensure compliance with:

\\* International sanctions and embargoes
\\* Local financial regulations
\\* Gambling and prediction market laws
\\* Anti-money laundering (AML) requirements
\\* Know Your Customer (KYC) regulations

If you believe you are incorrectly restricted or have questions about geographic availability, please contact \[Polymarket Support\](https://polymarket.com/support).

\\*\\*\\*

\## Next Steps

 Learn how to authenticate trading requests.

 Start placing orders (from eligible regions).


\# Introduction
Source: https://docs.polymarket.com/api-reference/introduction

Overview of the Polymarket APIs

The Polymarket API provides programmatic access to the world's largest prediction market. The platform is served by three separate APIs, each handling a different domain.

\\*\\*\\*

\## APIs

 \*\*\`https://gamma-api.polymarket.com\`\*\*

 Markets, events, tags, series, comments, sports, search, and public profiles. This is the primary API for discovering and browsing market data.

 \*\*\`https://data-api.polymarket.com\`\*\*

 User positions, trades, activity, holder data, open interest, leaderboards, and builder analytics.

 \*\*\`https://clob.polymarket.com\`\*\*

 Orderbook data, pricing, midpoints, spreads, and price history. Also handles order placement, cancellation, and other trading operations. Trading endpoints require \[authentication\](/api-reference/authentication).

 A separate \*\*Bridge API\*\* (\`https://bridge.polymarket.com\`) handles deposits and withdrawals. Bridges are not handled by Polymarket, it is a proxy of fun.xyz service.

\\*\\*\\*

\## Authentication

The Gamma API and Data API are fully public — no authentication required.

The CLOB API has both public endpoints (orderbook, prices) and authenticated endpoints (order management). See \[Authentication\](/api-reference/authentication) for details.

\\*\\*\\*

\## Next Steps

 Learn how to authenticate requests for trading endpoints.

 Official TypeScript, Python, and Rust libraries.


\# Get fee rate
Source: https://docs.polymarket.com/api-reference/market-data/get-fee-rate

/api-spec/clob-openapi.yaml get /fee-rate
Retrieves the base fee rate for a specific token ID.
The fee rate can be provided either as a query parameter or as a path parameter.

\# Get fee rate by path parameter
Source: https://docs.polymarket.com/api-reference/market-data/get-fee-rate-by-path-parameter

/api-spec/clob-openapi.yaml get /fee-rate/{token\_id}
Retrieves the base fee rate for a specific token ID using the token ID as a path parameter.

\# Get last trade price
Source: https://docs.polymarket.com/api-reference/market-data/get-last-trade-price

/api-spec/clob-openapi.yaml get /last-trade-price
Retrieves the last trade price and side for a specific token ID.
Returns default values of "0.5" for price and empty string for side if no trades found.

\# Get last trade prices (query parameters)
Source: https://docs.polymarket.com/api-reference/market-data/get-last-trade-prices-query-parameters

/api-spec/clob-openapi.yaml get /last-trades-prices
Retrieves last trade prices for multiple token IDs using query parameters.
Maximum 500 token IDs can be requested per call.

\# Get last trade prices (request body)
Source: https://docs.polymarket.com/api-reference/market-data/get-last-trade-prices-request-body

/api-spec/clob-openapi.yaml post /last-trades-prices
Retrieves last trade prices for multiple token IDs using a request body.
Maximum 500 token IDs can be requested per call.

\# Get market price
Source: https://docs.polymarket.com/api-reference/market-data/get-market-price

/api-spec/clob-openapi.yaml get /price
Retrieves the best market price for a specific token ID and side (bid or ask).
Returns the best bid price for BUY side or best ask price for SELL side.

\# Get market prices (query parameters)
Source: https://docs.polymarket.com/api-reference/market-data/get-market-prices-query-parameters

/api-spec/clob-openapi.yaml get /prices
Retrieves market prices for multiple token IDs and sides using query parameters.

\# Get market prices (request body)
Source: https://docs.polymarket.com/api-reference/market-data/get-market-prices-request-body

/api-spec/clob-openapi.yaml post /prices
Retrieves market prices for multiple token IDs and sides using a request body.
Each request must include both token\_id and side.

\# Get midpoint prices (query parameters)
Source: https://docs.polymarket.com/api-reference/market-data/get-midpoint-prices-query-parameters

/api-spec/clob-openapi.yaml get /midpoints
Retrieves midpoint prices for multiple token IDs using query parameters.
The midpoint is calculated as the average of the best bid and best ask prices.

\# Get midpoint prices (request body)
Source: https://docs.polymarket.com/api-reference/market-data/get-midpoint-prices-request-body

/api-spec/clob-openapi.yaml post /midpoints
Retrieves midpoint prices for multiple token IDs using a request body.
The midpoint is calculated as the average of the best bid and best ask prices.

\# Get order book
Source: https://docs.polymarket.com/api-reference/market-data/get-order-book

/api-spec/clob-openapi.yaml get /book
Retrieves the order book summary for a specific token ID.
Includes bids, asks, market details, and last trade price.

\# Get order books (request body)
Source: https://docs.polymarket.com/api-reference/market-data/get-order-books-request-body

/api-spec/clob-openapi.yaml post /books
Retrieves order book summaries for multiple token IDs using a request body.

\# Get spread
Source: https://docs.polymarket.com/api-reference/market-data/get-spread

/api-spec/clob-openapi.yaml get /spread
Retrieves the spread for a specific token ID.
The spread is the difference between the best ask and best bid prices.

\# Get spreads
Source: https://docs.polymarket.com/api-reference/market-data/get-spreads

/api-spec/clob-openapi.yaml post /spreads
Retrieves spreads for multiple token IDs.
The spread is the difference between the best ask and best bid prices.

\# Get tick size
Source: https://docs.polymarket.com/api-reference/market-data/get-tick-size

/api-spec/clob-openapi.yaml get /tick-size
Retrieves the minimum tick size (price increment) for a specific token ID.
The tick size can be provided either as a query parameter or as a path parameter.

\# Get tick size by path parameter
Source: https://docs.polymarket.com/api-reference/market-data/get-tick-size-by-path-parameter

/api-spec/clob-openapi.yaml get /tick-size/{token\_id}
Retrieves the minimum tick size (price increment) for a specific token ID using the token ID as a path parameter.

\# Get market by id
Source: https://docs.polymarket.com/api-reference/markets/get-market-by-id

/api-spec/gamma-openapi.yaml get /markets/{id}

\# Get market by slug
Source: https://docs.polymarket.com/api-reference/markets/get-market-by-slug

/api-spec/gamma-openapi.yaml get /markets/slug/{slug}

\# Get market tags by id
Source: https://docs.polymarket.com/api-reference/markets/get-market-tags-by-id

/api-spec/gamma-openapi.yaml get /markets/{id}/tags

\# Get prices history
Source: https://docs.polymarket.com/api-reference/markets/get-prices-history

/api-spec/clob-openapi.yaml get /prices-history
Retrieve historical price data for a market.

\# Get simplified markets
Source: https://docs.polymarket.com/api-reference/markets/get-simplified-markets

/api-spec/clob-openapi.yaml get /simplified-markets

\# List markets
Source: https://docs.polymarket.com/api-reference/markets/list-markets

/api-spec/gamma-openapi.yaml get /markets

\# Get live volume for an event
Source: https://docs.polymarket.com/api-reference/misc/get-live-volume-for-an-event

/api-spec/data-openapi.yaml get /live-volume

\# Get open interest
Source: https://docs.polymarket.com/api-reference/misc/get-open-interest

/api-spec/data-openapi.yaml get /oi

\# Rate Limits
Source: https://docs.polymarket.com/api-reference/rate-limits

API rate limits for all Polymarket endpoints

All API rate limits are enforced using Cloudflare's throttling system. When you exceed the limit for any endpoint, requests are throttled (delayed/queued) rather than immediately rejected. Limits reset on sliding time windows.

\\*\\*\\*

\## General

\| Endpoint \| Limit \|
\| \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- \| \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- \|
\| General rate limiting \| 15,000 req / 10s \|
\| Health check (\`/ok\`) \| 100 req / 10s \|

\\*\\*\\*

\## Gamma API

Base URL: \`https://gamma-api.polymarket.com\`

\| Endpoint \| Limit \|
\| \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- \| \-\-\-\-\-\-\-\-\-\-\-\-\-\-\- \|
\| General \| 4,000 req / 10s \|
\| \`/events\` \| 500 req / 10s \|
\| \`/markets\` \| 300 req / 10s \|
\| \`/markets\` + \`/events\` listing \| 900 req / 10s \|
\| \`/comments\` \| 200 req / 10s \|
\| \`/tags\` \| 200 req / 10s \|
\| \`/public-search\` \| 350 req / 10s \|

\\*\\*\\*

\## Data API

Base URL: \`https://data-api.polymarket.com\`

\| Endpoint \| Limit \|
\| \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- \| \-\-\-\-\-\-\-\-\-\-\-\-\-\-\- \|
\| General \| 1,000 req / 10s \|
\| \`/trades\` \| 200 req / 10s \|
\| \`/positions\` \| 150 req / 10s \|
\| \`/closed-positions\` \| 150 req / 10s \|
\| Health check (\`/ok\`) \| 100 req / 10s \|

\\*\\*\\*

\## CLOB API

Base URL: \`https://clob.polymarket.com\`

\### General

\| Endpoint \| Limit \|
\| \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- \| \-\-\-\-\-\-\-\-\-\-\-\-\-\-\- \|
\| General \| 9,000 req / 10s \|
\| \`GET\` balance allowance \| 200 req / 10s \|
\| \`UPDATE\` balance allowance \| 50 req / 10s \|

\### Market Data

\| Endpoint \| Limit \|
\| \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- \| \-\-\-\-\-\-\-\-\-\-\-\-\-\-\- \|
\| \`/book\` \| 1,500 req / 10s \|
\| \`/books\` \| 500 req / 10s \|
\| \`/price\` \| 1,500 req / 10s \|
\| \`/prices\` \| 500 req / 10s \|
\| \`/midpoint\` \| 1,500 req / 10s \|
\| \`/midpoints\` \| 500 req / 10s \|
\| \`/prices-history\` \| 1,000 req / 10s \|
\| Market tick size \| 200 req / 10s \|

\### Ledger

\| Endpoint \| Limit \|
\| \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- \| \-\-\-\-\-\-\-\-\-\-\-\-\- \|
\| \`/trades\`, \`/orders\`, \`/notifications\`, \`/order\` \| 900 req / 10s \|
\| \`/data/orders\` \| 500 req / 10s \|
\| \`/data/trades\` \| 500 req / 10s \|
\| \`/notifications\` \| 125 req / 10s \|

\### Authentication

\| Endpoint \| Limit \|
\| \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- \| \-\-\-\-\-\-\-\-\-\-\-\-\- \|
\| API key endpoints \| 100 req / 10s \|

\### Trading

Trading endpoints have both \*\*burst\*\* limits (short spikes allowed) and \*\*sustained\*\* limits (longer-term average).

\| Endpoint \| Burst Limit \| Sustained Limit \|
\| \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- \| \-\-\-\-\-\-\-\-\-\-\-\-\-\-\- \| \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- \|
\| \`POST /order\` \| 3,500 req / 10s \| 36,000 req / 10 min \|
\| \`DELETE /order\` \| 3,000 req / 10s \| 30,000 req / 10 min \|
\| \`POST /orders\` \| 1,000 req / 10s \| 15,000 req / 10 min \|
\| \`DELETE /orders\` \| 1,000 req / 10s \| 15,000 req / 10 min \|
\| \`DELETE /cancel-all\` \| 250 req / 10s \| 6,000 req / 10 min \|
\| \`DELETE /cancel-market-orders\` \| 1,000 req / 10s \| 1,500 req / 10 min \|

\\*\\*\\*

\## Other

\| Endpoint \| Limit \|
\| \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- \| \-\-\-\-\-\-\-\-\-\-\-\-\-\- \|
\| Relayer \`/submit\` \| 25 req / 1 min \|
\| User PNL API \| 200 req / 10s \|

\\*\\*\\*

\## Next Steps

 Learn how to authenticate trading requests.

 Official TypeScript, Python, and Rust libraries.


\# Cancel all orders
Source: https://docs.polymarket.com/api-reference/trade/cancel-all-orders

/api-spec/clob-openapi.yaml delete /cancel-all
Cancels all open orders for the authenticated user. Works even in cancel-only mode.

\# Cancel multiple orders
Source: https://docs.polymarket.com/api-reference/trade/cancel-multiple-orders

/api-spec/clob-openapi.yaml delete /orders
Cancels multiple orders by their IDs. Maximum 3000 orders per request.
Duplicate order IDs in the request are automatically ignored.
Works even in cancel-only mode.

\# Cancel orders for a market
Source: https://docs.polymarket.com/api-reference/trade/cancel-orders-for-a-market

/api-spec/clob-openapi.yaml delete /cancel-market-orders
Cancels all open orders for the authenticated user in a specific market (condition) and asset.
Works even in cancel-only mode.

\# Cancel single order
Source: https://docs.polymarket.com/api-reference/trade/cancel-single-order

/api-spec/clob-openapi.yaml delete /order
Cancels a single order by its ID. Works even in cancel-only mode.

\# Get builder trades
Source: https://docs.polymarket.com/api-reference/trade/get-builder-trades

/api-spec/clob-openapi.yaml get /builder/trades
Retrieves originated trades for a given builder.
Builders can only see their own originated trades.

\# Get order scoring status
Source: https://docs.polymarket.com/api-reference/trade/get-order-scoring-status

/api-spec/clob-openapi.yaml get /order-scoring
Checks if a specific order is currently scoring for rewards.

An order is considered "scoring" if it meets all the criteria for earning maker rewards:
\- The order is live on a rewards-eligible market
\- The order meets the minimum size requirements
\- The order is within the valid spread range
\- The order has been live for the required duration

\# Get single order by ID
Source: https://docs.polymarket.com/api-reference/trade/get-single-order-by-id

/api-spec/clob-openapi.yaml get /order/{orderID}
Retrieves a specific order by its ID (order hash) for the authenticated user.
Builder-authenticated clients can also use this endpoint to retrieve orders attributed to their builder account.

\# Get trades
Source: https://docs.polymarket.com/api-reference/trade/get-trades

/api-spec/clob-openapi.yaml get /trades
Retrieves trades for the authenticated user. Returns paginated results.
Requires readonly or level 2 API key authentication.

\# Get user orders
Source: https://docs.polymarket.com/api-reference/trade/get-user-orders

/api-spec/clob-openapi.yaml get /orders
Retrieves open orders for the authenticated user. Returns paginated results.
Builder-authenticated clients can also use this endpoint to retrieve orders attributed to their builder account.

\# Post a new order
Source: https://docs.polymarket.com/api-reference/trade/post-a-new-order

/api-spec/clob-openapi.yaml post /order
Creates a new order in the order book

\# Post multiple orders
Source: https://docs.polymarket.com/api-reference/trade/post-multiple-orders

/api-spec/clob-openapi.yaml post /orders
Creates multiple new orders in the order book. Orders are processed in parallel.
Maximum 15 orders per request.

\# Send heartbeat
Source: https://docs.polymarket.com/api-reference/trade/send-heartbeat

/api-spec/clob-openapi.yaml post /heartbeats
Sends a heartbeat signal to maintain active session status.
If heartbeats are not sent regularly, all open orders for the user will be automatically canceled.
This is useful for automated trading systems that need to ensure orders are canceled
if the system becomes unresponsive.

\# API Keys
Source: https://docs.polymarket.com/builders/api-keys

Create and manage your Builder API credentials

Builder API keys authenticate your application with Polymarket's relayer and enable order attribution. You'll need these credentials to access gasless transactions and track volume.

\## Accessing Your Builder Profile

 Go to
 \[polymarket.com/settings?tab=builder\](https://polymarket.com/settings?tab=builder)
 Click your profile image → Select "Builders"

\## Creating API Keys

In the \*\*Builder Keys\*\* section of your profile:

1\. Click \*\*"+ Create New"\*\* to generate a new API key
2\. \*\*Copy all three values immediately\*\* — the secret and passphrase are only shown once
3\. Store them securely in your secrets manager or environment variables

Each API key includes three components:

\| Component \| Description \| Example \|
\| \-\-\-\-\-\-\-\-\-\-\-\- \| \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- \| \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- \|
\| \`key\` \| Public identifier for your builder account \| \`abc123-def456-...\` \|
\| \`secret\` \| Secret key for signing requests \| \`base64-encoded-secret\` \|
\| \`passphrase\` \| Additional authentication value \| \`your-passphrase\` \|

 The \`secret\` and \`passphrase\` are only displayed once when created. If you
 lose them, you'll need to generate a new key.

\## Managing Keys

Create separate keys for different environments:

\| Environment \| Purpose \|
\| \-\-\-\-\-\-\-\-\-\-\- \| \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- \|
\| Development \| Testing and local development \|
\| Staging \| Pre-production testing \|
\| Production \| Live trading \|

\## Profile Settings

Your builder profile includes customizable settings:

\| Setting \| Description \|
\| \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- \| \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- \|
\| \*\*Profile Picture\*\* \| Displayed on the \[Builder Leaderboard\](https://builders.polymarket.com) \|
\| \*\*Builder Name\*\* \| Public name shown on the leaderboard \|
\| \*\*Builder Address\*\* \| Your unique builder identifier (read-only) \|
\| \*\*Current Tier\*\* \| Your rate limit tier: Unverified, Verified, or Partner \|

\## Environment Variables

Store your credentials as environment variables:

 \`\`\`bash .env theme={null}
 POLY\_BUILDER\_API\_KEY=your-api-key
 POLY\_BUILDER\_SECRET=your-secret
 POLY\_BUILDER\_PASSPHRASE=your-passphrase
 \`\`\`

 \`\`\`typescript theme={null}
 import { BuilderApiKeyCreds } from "@polymarket/builder-signing-sdk";

 const builderCreds: BuilderApiKeyCreds = {
 key: process.env.POLY\_BUILDER\_API\_KEY!,
 secret: process.env.POLY\_BUILDER\_SECRET!,
 passphrase: process.env.POLY\_BUILDER\_PASSPHRASE!,
 };
 \`\`\`

 \`\`\`python theme={null}
 import os
 from py\_builder\_signing\_sdk import BuilderApiKeyCreds

 builder\_creds = BuilderApiKeyCreds(
 key=os.environ\["POLY\_BUILDER\_API\_KEY"\],
 secret=os.environ\["POLY\_BUILDER\_SECRET"\],
 passphrase=os.environ\["POLY\_BUILDER\_PASSPHRASE"\],
 )
 \`\`\`

 \`\`\`rust theme={null}
 use polymarket\_client\_sdk::auth::Credentials;

 let builder\_creds = Credentials::new(
 std::env::var("POLY\_BUILDER\_API\_KEY")?.parse()?,
 std::env::var("POLY\_BUILDER\_SECRET")?,
 std::env::var("POLY\_BUILDER\_PASSPHRASE")?,
 );
 \`\`\`


\## Security Best Practices

\| Practice \| Description \|
\| \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- \| \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- \|
\| \*\*Never commit credentials\*\* \| Use \`.gitignore\` to exclude \`.env\` files \|
\| \*\*Use environment variables\*\* \| Load credentials from env vars, not hardcoded strings \|
\| \*\*Use a secrets manager\*\* \| AWS Secrets Manager, HashiCorp Vault, etc. for production \|
\| \*\*Separate environments\*\* \| Use different keys for dev, staging, and production \|
\| \*\*Monitor usage\*\* \| Check the leaderboard for unexpected volume changes \|

 \*\*Never expose Builder API credentials in client-side code.\*\* Your secret and
 passphrase must stay on your server.

\## Troubleshooting

 \*\*Cause:\*\* You've exceeded your tier's daily transaction limit.

 \*\*Solution:\*\*

 \\* Wait until the daily limit resets
 \\* \[Contact Polymarket\](/builders/tiers#contact) to upgrade your tier

 \*\*Cause:\*\* The secret and passphrase are only shown once when created.

 \*\*Solution:\*\* Create a new API key. You cannot recover the original values.


\## Next Steps

 Configure your client to credit trades to your account.

 Learn about rate limits and how to upgrade.


\# Builder Program
Source: https://docs.polymarket.com/builders/overview

Build applications that route orders through Polymarket

A \*\*builder\*\* is a person, group, or organization that routes orders from users to Polymarket. If you've created a platform that allows users to trade on Polymarket through your system, this program is for you.

\## Program Benefits

 All onchain operations are gas-free through our relayer

 Get credit for orders and compete for grants on the Builder Leaderboard


\### What You Get

\| Benefit \| Description \|
\| \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- \| \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- \|
\| \*\*Relayer Access\*\* \| Gas-free wallet deployment, approvals, order execution and CTF operations \|
\| \*\*Volume Tracking\*\* \| All orders attributed to your builder profile \|
\| \*\*Weekly Rewards\*\* \| USDC rewards program based on volume (Verified+) \|
\| \*\*Leaderboard\*\* \| Public visibility on \[builders.polymarket.com\](https://builders.polymarket.com) \|
\| \*\*Support\*\* \| Telegram channel and engineering support (Verified+) \|

 EOA wallets do not have relayer access. Users trading directly from an EOA pay
 their own gas fees.

\## How It Works

 User places an order through your application.

 Your app signs the request with Builder API credentials.

 Order is submitted to Polymarket's CLOB with attribution headers.

 Polymarket matches the order and covers gas fees for onchain operations.

 Volume is credited to your builder account.


\## Getting Started

 Go to
 \[polymarket.com/settings?tab=builder\](https://polymarket.com/settings?tab=builder)
 and generate your API keys.

 Set up your CLOB client to include builder authentication headers with every
 order.

 Use the Relayer Client for gas-free wallet deployment and onchain
 operations.

 Monitor your volume on the \[Builder\
 Leaderboard\](https://builders.polymarket.com).


\## SDKs and Libraries

 Place orders with builder attribution

 Place orders with builder attribution

 Gasless onchain transactions

 Gasless onchain transactions

 Place orders with builder attribution

 Sign builder authentication headers

 Sign builder authentication headers


\## Examples

These open-source demo applications show how to integrate Polymarket's CLOB Client and Builder Relayer Client for gasless trading with builder order attribution.

 Multiple wallet providers

 Safe & Proxy wallet support

 Orders, positions, CTF ops


\### Safe Wallet Examples

Deploy Gnosis Safe wallets for your users:

 MetaMask, Phantom, Rabby, and other browser wallets

 Privy embedded wallets

 Magic Link email/social authentication

 Turnkey embedded wallets


\### Proxy Wallet Examples

For existing Magic Link users from Polymarket.com:

 Auto-deploying proxy wallets for Polymarket.com Magic users


\### What Each Demo Covers

 \\* User sign-in via wallet provider
 \\* User API credential derivation (L2 auth)
 \\* Builder config with remote signing
 \\* Signature types for Safe vs Proxy wallets

 \\* Safe wallet deployment via Relayer
 \\* Batch token approvals (USDC.e + outcome tokens)
 \\* CTF operations (split, merge, redeem)
 \\* Transaction monitoring

 \\* CLOB client initialization
 \\* Order placement with builder attribution
 \\* Position and order management
 \\* Market discovery via Gamma API


\\*\\*\\*

\## Next Steps

 Create and manage your Builder API credentials.

 Learn about rate limits and how to upgrade.

 Configure your client to credit trades to your account.

 Set up gasless transactions for your users.


\# Tiers
Source: https://docs.polymarket.com/builders/tiers

Rate limits, rewards, and how to upgrade

The Builder Program uses a tiered system to manage rate limits while rewarding high-performing integrations. Higher tiers unlock increased limits, weekly rewards, and priority support.

\## Feature Definitions

\| Feature \| Description \|
\| \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- \| \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- \|
\| \*\*Daily Relayer Txn Limit\*\* \| Maximum Relayer transactions per day for Safe/Proxy wallet operations \|
\| \*\*API Rate Limits\*\* \| Rate limits for non-relayer endpoints (CLOB, Gamma, etc.) \|
\| \*\*Gasless Trading\*\* \| Gas fees subsidized for trading via Safe/Proxy wallets \|
\| \*\*Order Attribution\*\* \| Orders tracked and attributed to your Builder profile \|
\| \*\*Builder Fees\*\* \| Builders who route orders can charge fees and monetize on flow \|
\| \*\*Leaderboard Visibility\*\* \| Visibility on the \[Builder Leaderboard\](https://builders.polymarket.com/) \|
\| \*\*Weekly Rewards\*\* \| Weekly USDC rewards program for visible builders based on volume \|
\| \*\*Grants\*\* \| Builder grants subject to approval, awarded based on innovation and impact \|
\| \*\*Telegram Channel\*\* \| Private Builders channel for announcements and support \|
\| \*\*Engineering Support\*\* \| Direct access to engineering team \|
\| \*\*Marketing Support\*\* \| Promotion via official Polymarket social accounts \|
\| \*\*Priority Access\*\* \| Early access to new features and products \|

\\*\\*\\*

\## Tier Comparison

\| Feature \| Unverified \| Verified \| Partner \|
\| \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- \| :--------: \| :-----------------: \| :-----------------: \|
\| \*\*Daily Relayer Txn Limit\*\* \| 100/day \| 3,000/day \| Unlimited \|
\| \*\*API Rate Limits\*\* \| Standard \| Standard \| Highest \|
\| \*\*Gasless Trading\*\*\\\* \| Yes \| Yes \| Yes \|
\| \*\*Order Attribution\*\* \| Yes \| Yes \| Yes \|
\| \*\*Builder Fees\*\* \| — \| Yes \| Yes \|
\| \*\*Leaderboard Visibility\*\* \| — \| Yes \| Yes \|
\| \*\*Weekly Rewards\*\* \| — \| Subject to approval \| Subject to approval \|
\| \*\*Grants\*\* \| — \| Subject to approval \| Subject to approval \|
\| \*\*Telegram Channel\*\* \| — \| Yes \| Yes \|
\| \*\*Engineering Support\*\* \| — \| Standard \| Elevated \|
\| \*\*Marketing Support\*\* \| — \| Standard \| Elevated \|
\| \*\*Priority Access\*\* \| — \| — \| Yes \|

\\*\\*\\*

\## Unverified

 The default tier for all new builders. Start immediately with no approval
 required.

\*\*How to get started:\*\*

1\. Go to \[polymarket.com/settings?tab=builder\](https://polymarket.com/settings?tab=builder)
2\. Create a builder profile
3\. Click \*\*"+ Create New"\*\* to generate API keys
4\. Implement \[builder signing\](/trading/orders/attribution) — required for Relayer access and CLOB order attribution

\*\*What's included:\*\*

\\* Gasless trading on all CLOB orders through Safe/Proxy wallets
\\* Gas subsidized on all Relayer transactions up to daily limit (through Safe/Proxy wallets)
\\* Access to all client libraries and documentation

\\*\\*\\*

\## Verified

 For builders who need higher throughput. Requires manual approval.

\*\*How to upgrade:\*\*

Contact us at \[builder@polymarket.com\](mailto:builder@polymarket.com) with:

\\* Your Builder API Key
\\* Use case description
\\* Expected volume
\\* Other relevant information (links, docs, decks, etc.)

\*\*Unlocks over Unverified:\*\*

\\* 30x daily Relayer transaction limit
\\* Monetize with Builder fees
\\* Leaderboard visibility at \[builders.polymarket.com\](https://builders.polymarket.com)
\\* Private Telegram channel for announcements and support
\\* Weekly USDC rewards based on volume (subject to approval)
\\* Grants (subject to approval)

\\*\\*\\*

\## Partner

 Enterprise tier for high-volume integrations and strategic partners.

\*\*Unlocks over Verified:\*\*

\\* Unlimited Relayer transactions
\\* Highest API rate limits
\\* Elevated engineering support
\\* Elevated and coordinated marketing support
\\* Priority access to new features and products
\\* Multiplier on the Weekly Rewards Program

\\*\\*\\*

\## How to Upgrade

 Start with the Unverified tier and build your integration.

 Route orders through Polymarket and demonstrate consistent usage.

 Email \[builder@polymarket.com\](mailto:builder@polymarket.com) with your
 builder key and use case.

 The Polymarket team reviews applications and responds within a few business
 days.


\## Contact

Ready to upgrade or have questions?

 Email us with your Builder API Key and use case details.

\## FAQ

 Verification is displayed in your \[Builder Profile\](https://polymarket.com/settings?tab=builder) settings.

 Relayer requests beyond your daily limit will be rate-limited and return an
 error. Consider upgrading to Verified or Partner tier if you're hitting
 limits.

 If you're not routing orders for other users (wallets), you can get unlimited
 daily Relay transactions by obtaining a \[Relayer API key\](https://polymarket.com/settings?tab=api-keys).


\\*\\*\\*

\## Next Steps

 Create your Builder API credentials.

 Configure your client to credit trades to your account.


\# Markets & Events
Source: https://docs.polymarket.com/concepts/markets-events

Understanding the fundamental building blocks of Polymarket

Every prediction on Polymarket is structured around two core concepts: \*\*markets\*\* and \*\*events\*\*. Understanding how they relate is essential for building on the platform.



\## Markets

A \*\*market\*\* is the fundamental tradable unit on Polymarket. Each market represents a single binary question with Yes/No outcomes.



Every market has:

\| Identifier \| Description \|
\| \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- \| \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- \|
\| \*\*Condition ID\*\* \| Unique identifier for the market's condition in the CTF contracts \|
\| \*\*Question ID\*\* \| Hash of the market question used for resolution \|
\| \*\*Token IDs\*\* \| ERC1155 token IDs used for trading on the CLOB — one for Yes, one for No \|

 Markets can only be traded via the CLOB if \`enableOrderBook\` is \`true\`. Some
 markets may exist onchain but not be available for order book trading.

\### Market Example

A simple market might be:

\> \*\*"Will Bitcoin reach \\$150,000 by December 2026?"\*\*

This creates two outcome tokens:

\\* \*\*Yes token\*\* - Redeemable for \`$1\` if Bitcoin reaches \`$150k\`
\\* \*\*No token\*\* - Redeemable for \`$1\` if Bitcoin doesn't reach \`$100k\`

\## Events

An \*\*event\*\* is a container that groups one or more related markets together. Events provide organizational structure and enable multi-outcome predictions.

\### Single-Market Events

When an event contains just one market, it creates a simple market pair. The event and market are essentially equivalent.

\`\`\`
Event: Will Bitcoin reach $100,000 by December 2024?
└── Market: Will Bitcoin reach $100,000 by December 2024? (Yes/No)
\`\`\`

\### Multi-Market Events

When an event contains two or more markets, it creates a grouped market pair. This enables mutually exclusive multi-outcome predictions.

\`\`\`
Event: Who will win the 2024 Presidential Election?
├── Market: Donald Trump? (Yes/No)
├── Market: Joe Biden? (Yes/No)
├── Market: Kamala Harris? (Yes/No)
└── Market: Other? (Yes/No)
\`\`\`

\## Identifying Markets

Every market and event has a unique \*\*slug\*\* that appears in the Polymarket URL:

\`\`\`
https://polymarket.com/event/fed-decision-in-october
 └── slug: fed-decision-in-october
\`\`\`

You can use slugs to fetch specific markets or events from the API:

\`\`\`bash theme={null}
\# Fetch event by slug
curl "https://gamma-api.polymarket.com/events?slug=fed-decision-in-october"
\`\`\`

\## Sports Markets

Specifically for sports markets, outstanding limit orders are \*\*automatically cancelled\*\* once the game begins, clearing the order book at the official start time. However, game start times can shift — if a game starts earlier than scheduled, orders may not be cleared in time. Always monitor your orders closely around game start times.

\\*\\*\\*

\## Next Steps

 Learn how prices are determined and how the order book works.

 Start querying markets and events from the API.


\# Order Lifecycle
Source: https://docs.polymarket.com/concepts/order-lifecycle

Understanding how orders flow from creation to settlement

Every trade on Polymarket follows a specific lifecycle. Orders are created offchain, matched by an operator, and settled onchain through smart contracts. This hybrid approach combines the speed of centralized matching with the security of blockchain settlement.



\## How Orders Work

All orders on Polymarket are \*\*limit orders\*\*. A limit order specifies the price you're willing to pay (or accept) and the quantity you want to trade.

 "Market orders" are simply limit orders with a price set to execute
 immediately against the best available resting orders.

Orders are \*\*EIP712-signed messages\*\*. When you place an order, you sign a structured message with your private key. This signature authorizes the Exchange contract to execute the trade on your behalf—without ever taking custody of your funds.

\## Order Types

\| Type \| Behavior \| Use Case \|
\| \-\-\-\-\-\-\- \| \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- \| \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- \|
\| \*\*GTC\*\* \| Good Till Cancelled — rests on book until filled or cancelled \| Standard limit orders \|
\| \*\*GTD\*\* \| Good Till Date — auto-expires at specified time \| Time-limited orders \|
\| \*\*FOK\*\* \| Fill Or Kill — fill entirely or cancel immediately \| All-or-nothing execution \|
\| \*\*FAK\*\* \| Fill And Kill — fill what's available, cancel the rest \| Partial fills acceptable \|

\### Post-Only Orders

Post-only orders will only rest on the book. If a post-only order would match immediately (cross the spread), it's rejected instead of executed. This guarantees you're always the maker, never the taker.

 Your client creates an order object containing:

 \\* Token ID (which outcome you're trading)
 \\* Side (buy or sell)
 \\* Price and size
 \\* Expiration time
 \\* Nonce (for replay protection)

 You sign this order with your private key, creating an EIP712 signature.

 The signed order is submitted to the Central Limit Order Book (CLOB) operator. The operator validates:

 \\* Signature is valid
 \\* You have sufficient balance
 \\* You have set the required allowances
 \\* Price meets minimum tick size requirements

 \*\*If the order is marketable\*\* (your buy price ≥ lowest ask, or your sell price ≤ highest bid), it matches immediately against resting orders.

 \*\*If the order is not marketable\*\*, it rests on the book waiting for a counterparty. It remains open until:

 \\* Another order matches against it
 \\* You cancel it
 \\* It expires (GTD orders only)

 When orders match, the operator submits the trade to the blockchain. The Exchange contract:

 \\* Verifies both signatures
 \\* Transfers tokens from seller to buyer
 \\* Transfers USDC.e from buyer to seller

 Settlement is \*\*atomic\*\*—either the entire trade succeeds or nothing happens.

 The trade achieves finality on Polygon. Your token balances update and the trade appears in your history.


\## Order Statuses

When you place an order, it receives one of these statuses:

\| Status \| Description \|
\| \-\-\-\-\-\-\-\-\-\-\- \| \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- \|
\| \`live\` \| Order is resting on the book \|
\| \`matched\` \| Order matched immediately \|
\| \`delayed\` \| Marketable order subject to a 3-second matching delay (sports markets) \|
\| \`unmatched\` \| Marketable order placed on the book after the delay expired without a match \|

\## Trade Statuses

After matching, trades progress through these statuses:

\| Status \| Terminal \| Description \|
\| \-\-\-\-\-\-\-\-\-\-\- \| \-\-\-\-\-\-\-\- \| \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- \|
\| \`MATCHED\` \| No \| Trade matched, sent to executor for onchain submission \|
\| \`MINED\` \| No \| Transaction mined into the blockchain \|
\| \`CONFIRMED\` \| Yes \| Trade achieved finality, successful \|
\| \`RETRYING\` \| No \| Transaction failed, being retried \|
\| \`FAILED\` \| Yes \| Trade failed permanently \|

\## Maker vs Taker

\| Role \| Description \| When \|
\| \-\-\-\-\-\-\-\-\- \| \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- \| \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- \|
\| \*\*Maker\*\* \| Adds liquidity to the book \| Your order rests and is later matched \|
\| \*\*Taker\*\* \| Removes liquidity from the book \| Your order matches immediately against resting orders \|

Price improvement always benefits the taker. If you place a buy order at \`$0.55\` and it matches against a resting sell at \`$0.52\`, you pay \`$0.52\`.

\## Cancellation

You can cancel orders at any time before they're matched:

\\* \*\*Via API\*\* — Cancel through the CLOB API (instant)
\\* \*\*Onchain\*\* — Cancel directly on the Exchange contract (fallback if API is unavailable)

Partial fills cannot be cancelled—only the unfilled portion of an order can be cancelled.

\## Requirements

Before placing orders, ensure:

\| Requirement \| Description \|
\| \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- \| \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- \|
\| \*\*Balance\*\* \| Sufficient USDC.e (for buys) or tokens (for sells) \|
\| \*\*Allowance\*\* \| Approve the Exchange contract to spend your assets \|
\| \*\*API Credentials\*\* \| Valid API key for authenticated endpoints \|

 Order size is limited by your available balance minus any amounts reserved by existing open orders.

 $$
 \\text{maxOrderSize} = \\text{balance} - \\sum(\\text{openOrderSize} - \\text{filledAmount})
 $$

\## Next Steps

 Learn how markets are resolved and winning tokens redeemed.

 Start placing orders with our step-by-step guide.


\# Positions & Tokens
Source: https://docs.polymarket.com/concepts/positions-tokens

Understanding outcome tokens and how positions work on Polymarket

Every prediction on Polymarket is represented by \*\*outcome tokens\*\*. When you trade, you're buying and selling these tokens. Your \*\*position\*\* is simply your balance of tokens for a given market.



\## Outcome Tokens

Each market has exactly two outcome tokens:

\| Token \| Redeems for \| If... \|
\| \-\-\-\-\-\-\- \| \-\-\-\-\-\-\-\-\-\-\- \| \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- \|
\| \*\*Yes\*\* \| \\$1.00 \| The event occurs \|
\| \*\*No\*\* \| \\$1.00 \| The event does not occur \|

Tokens are \*\*ERC1155\*\* assets on Polygon, using the \[Gnosis Conditional Token Framework\](https://github.com/gnosis/conditional-tokens-contracts/) (CTF). This means they're fully onchain and function as standard ERC1155 tokens.

 Outcome tokens are always fully backed. Every Yes/No pair in existence is
 backed by exactly \`$1\` of USDC.e collateral locked in the CTF contract.

\### Split

Convert USDC.e into outcome tokens. Splitting \\$1 creates 1 Yes token and 1 No token.

\`\`\`
$100 USDC.e → 100 Yes tokens + 100 No tokens
\`\`\`

Use this when you want to:

\\* Create inventory for market making
\\* Obtain both sides of a market

\### Trade

Buy or sell tokens on the order book. This is how most users acquire positions.

\\* \*\*Buy Yes\*\* at \`$0.60\` → Pay \`$0.60\`, receive 1 Yes token
\\* \*\*Sell Yes\*\* at \`$0.60\` → Give up 1 Yes token, receive \`$0.60\`

You can sell your position at any time before resolution.

\### Merge

Convert a complete set of tokens back into USDC.e. Merging requires equal amounts of Yes and No tokens.

\`\`\`
100 Yes tokens + 100 No tokens → $100 USDC.e
\`\`\`

Use this when you want to:

\\* Exit a position without trading
\\* Convert accumulated tokens back to collateral

\### Redeem

After a market resolves, exchange winning tokens for USDC.e.

\| Outcome \| Yes tokens \| No tokens \|
\| \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- \| \-\-\-\-\-\-\-\-\-\-\-\-\-\- \| \-\-\-\-\-\-\-\-\-\-\-\-\-\- \|
\| Event occurs \| Worth \\$1 each \| Worth \\$0 \|
\| Event doesn't occur \| Worth \\$0 \| Worth \\$1 each \|

\`\`\`
100 winning tokens → $100 USDC.e
\`\`\`

\### Position Value

The value of your position depends on the current market price:

\`\`\`
Position value = Token balance × Current price
\`\`\`

If you hold 100 Yes tokens and Yes is trading at \\$0.75:

\`\`\`
Position value = 100 × $0.75 = $75
\`\`\`

\## Profit and Loss

Your profit depends on how the market resolves compared to your entry price.

\### Example - Buying Yes at 0.40

\| Scenario \| Outcome \| Return \| Profit \|
\| \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- \| \-\-\-\-\-\-\-\- \| \-\-\-\-\-\- \| \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- \|
\| Event occurs \| Yes wins \| \\$1.00 \| +\\$0.60 per token (150%) \|
\| Event doesn't occur \| No wins \| \\$0.00 \| -\\$0.40 per token (-100%) \|

\### Holding Rewards

Polymarket pays a \*\*4.00% annualized\*\* Holding Reward based on your total position value in eligible markets. Your total position value is randomly sampled once each hour, and the reward is distributed daily. The rate is variable and subject to change at Polymarket's discretion.

\### Example - Selling Before Resolution

You can lock in profits or cut losses by selling before the market resolves:

\\* Bought Yes at \`$0.40\`
\\* Price rises to \`$0.70\`
\\* Sell at \`$0.70\` → Profit of \`$0.30\` per token (75%)

\# Prices & Orderbook
Source: https://docs.polymarket.com/concepts/prices-orderbook

How prices work and how the order book enables peer-to-peer trading

Polymarket uses a \*\*Central Limit Order Book (CLOB)\*\* for trading. Prices aren't set by Polymarket—they emerge from supply and demand as users trade with each other.



\## Prices Are Probabilities

Every share on Polymarket is priced between \`$0.00\` and \`$1.00\`. The price directly represents the market's belief in the probability of that outcome.

\| Price \| Implied Probability \|
\| \-\-\-\-\-\- \| \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- \|
\| \\$0.25 \| 25% chance \|
\| \\$0.50 \| 50% chance \|
\| \\$0.75 \| 75% chance \|

 The displayed price is the \*\*midpoint\*\* of the bid-ask spread. If the spread
 is wider than \\$0.10, the last traded price is shown instead.

\### Example

If the best bid for "Yes" is \`$0.34\` and the best ask is \`$0.40\`:

\`\`\`
Displayed price = ($0.34 + $0.40) / 2 = $0.37 (37% probability)
\`\`\`

You won't necessarily trade at \`$0.37\`—you'll pay the ask (\`$0.40\`) when buying or receive the bid (\`$0.34\`) when selling.

\## The Order Book

The order book is a list of all open buy and sell orders for a market. It has two sides:

\| Side \| Description \|
\| \-\-\-\- \| \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- \|
\| Bids \| Buy orders—the highest prices traders are willing to pay \|
\| Asks \| Sell orders—the lowest prices traders are willing to accept \|

The \*\*spread\*\* is the gap between the highest bid and lowest ask. Tighter spreads mean more liquid markets.

\## Order Types

\### Market Orders

Execute immediately at the best available price. Use when you want instant execution and are willing to pay the spread.

\\* \*\*Buying\*\*: You pay the lowest ask price
\\* \*\*Selling\*\*: You receive the highest bid price

\### Limit Orders

Execute only at your specified price or better. Use when you want price control and are willing to wait.

\\* Your order sits in the book until someone trades against it
\\* Orders can \*\*partially fill\*\* as different traders match portions of your order
\\* You can cancel unfilled orders at any time

 All orders on Polymarket are technically limit orders. A "market order" is
 simply a limit order priced to execute immediately against resting orders.

\## How Trades Work

Polymarket's CLOB is \*\*hybrid-decentralized\*\*:

1\. \*\*Offchain matching\*\* — An operator matches compatible orders
2\. \*\*Onchain settlement\*\* — Matched trades settle via smart contracts



This design gives you the speed of centralized matching with the security of onchain settlement. You always maintain custody of your funds.

\## Price Discovery

When a new market launches, there's no initial price. The first price emerges when:

1\. Someone places a limit order to buy Yes at a price (e.g., \`$0.60\`)
2\. Someone places a limit order to buy No at the complementary price (e.g., \`$0.40\`)
3\. Since \`$0.60\` + \`$0.40\` = \`$1.00\`, the orders match

When matched, \`$1.00\` is converted into 1 Yes token and 1 No token, each going to their respective buyers.

\## Next Steps

 Polymarket's orderbook has \*\*no trading size limits\*\* — it matches willing
 buyers and sellers of any amount. However, large orders may move the price
 significantly. Always check orderbook depth before trading in size.

 Learn about outcome tokens and how positions work.

 Understand what happens from order placement to settlement.


\# Resolution
Source: https://docs.polymarket.com/concepts/resolution

How markets are resolved and winning positions redeemed

When the outcome of an event becomes known, the market is \*\*resolved\*\*. Resolution determines which outcome won, allowing holders of winning tokens to redeem them for \\$1 each. Losing tokens become worthless.

Polymarket uses the \*\*UMA Optimistic Oracle\*\* for decentralized, permissionless resolution. Anyone can propose an outcome, and anyone can dispute it if they believe it's incorrect.



\## Resolution Rules

Every market has pre-defined resolution rules that specify:

\\* \*\*Resolution source\*\* — Where the outcome will be determined from (e.g., official announcements, specific websites)
\\* \*\*End date\*\* — When the market is eligible for resolution
\\* \*\*Edge cases\*\* — How ambiguous situations should be handled

 Always read the resolution rules before trading. The market title describes
 the question, but the \*\*rules\*\* define how it resolves.

 Anyone can propose a resolution by:

 1\. Selecting the winning outcome
 2\. Posting a bond (typically \\$750 USDC.e)
 3\. Submitting the proposal to the UMA Oracle

 If the proposal is correct and undisputed, the proposer receives their bond back plus a reward.


 If you propose incorrectly or too early, you lose your entire bond. Only
 propose if you're confident in the outcome and understand the process.

 After a proposal, there's a \*\*2-hour challenge period\*\* where anyone can dispute the outcome.

 \\* \*\*If no dispute\*\*: The proposal is accepted and the market resolves
 \\* \*\*If disputed\*\*: A new proposal round begins. If the second proposal is also disputed, the resolution escalates to UMA's DVM (Data Verification Mechanism) for a token holder vote.

 There are three possible resolution flows:

 1\. \*\*No dispute\*\* — Propose then Resolve (fastest, \\~2 hours)
 2\. \*\*One dispute\*\* — Propose, Challenge, second Propose, Resolve (second proposal accepted)
 3\. \*\*Two disputes\*\* — Propose, Challenge, second Propose, second Challenge, Resolve via DVM vote

 To dispute a proposal:

 1\. Post a counter-bond (same amount as proposer, typically \\$750)
 2\. The dispute triggers a new proposal round, or if already in the second round, a debate period

 During the \*\*24-48 hour debate period\*\*, evidence can be submitted in UMA's Discord channels (\`#evidence-rationale\` and \`#voting-discussion\`).

 After the debate period, UMA token holders vote on the correct outcome. The voting process takes approximately 48 hours.

 \| Outcome \| Result \| Bond Distribution \|
 \| \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- \| \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- \| \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- \|
 \| \*\*Proposer wins\*\* \| Original proposal accepted \| Proposer gets bond back + half of disputer's bond \|
 \| \*\*Disputer wins\*\* \| Proposal rejected, new proposal needed \| Disputer gets bond back + half of proposer's bond \|
 \| \*\*Too Early\*\* \| Event hasn't concluded yet \| Disputer gets bond back + half of proposer's bond \|
 \| \*\*Unknown/50-50\*\* \| Neither outcome applicable (rare) \| Market resolves 50/50 — each token redeems for \\$0.50; disputer gets bond back + half of proposer's bond \|


\## After Resolution

Once a market resolves:

\\* \*\*Trading stops\*\* — You can no longer buy or sell tokens for this market
\\* \*\*Winning tokens\*\* become redeemable for \\$1.00 each
\\* \*\*Losing tokens\*\* become worthless (\\$0.00)

\### Redeeming Tokens

After resolution, call the \`redeemPositions\` function on the CTF contract to exchange winning tokens for USDC.e. The contract burns your tokens and returns the corresponding collateral.

\`\`\`
100 winning tokens → $100 USDC.e
\`\`\`

\## Clarifications

In rare cases, unforeseen circumstances require clarification of the rules after trading begins. Polymarket may issue an \*\*"Additional context"\*\* update that proposers and voters should consider during resolution.

Clarifications:

\\* Cannot change the fundamental intent of the question
\\* Are published onchain via the bulletin board contract
\\* Should be considered by UMA voters when resolving disputes

 If you believe a clarification is needed, request it in the \[Polymarket\
 Discord\](https://discord.com/invite/polymarket) \`#market-review\` channel.

\## Resolution Timeline

\| Phase \| Duration \|
\| \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- \| \-\-\-\-\-\-\-\-\-\-\- \|
\| Challenge period \| 2 hours \|
\| Debate period (if disputed) \| 24-48 hours \|
\| UMA voting (if disputed) \| \\~48 hours \|

\*\*Undisputed resolution\*\*: \\~2 hours after proposal

\*\*Disputed resolution\*\*: 4-6 days total

\## Contract Addresses

\| Contract \| Address \| Network \|
\| \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- \| \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- \| \-\-\-\-\-\-\-\-\-\-\-\-\-\-\- \|
\| \*\*UmaCtfAdapter v3.0\*\* \| \`0x157Ce2d672854c848c9b79C49a8Cc6cc89176a49\` \| Polygon Mainnet \|
\| \*\*UmaCtfAdapter v2.0\*\* \| \`0x6A9D222616C90FcA5754cd1333cFD9b7fb6a4F74\` \| Polygon Mainnet \|
\| \*\*UmaCtfAdapter v1.0\*\* \| \`0xCB1822859cEF82Cd2Eb4E6276C7916e692995130\` \| Polygon Mainnet \|

\## Resources

\\* \[UMA Oracle Portal\](https://oracle.uma.xyz/) — View and interact with proposals
\\* \[UMA Documentation\](https://docs.uma.xyz/) — Learn more about the Optimistic Oracle
\\* \[Polymarket Discord\](https://discord.com/invite/polymarket) — Discuss resolutions and request clarifications
\\* \[UmaCtfAdapter Source Code\](https://github.com/Polymarket/uma-ctf-adapter) — Smart contract source
\\* \[UmaCtfAdapter Audit\](https://github.com/Polymarket/uma-ctf-adapter/blob/main/audit/Polymarket\_UMA\_Optimistic\_Oracle\_Adapter\_Audit.pdf) — Security audit report

\## Next Steps

 Learn how to redeem winning tokens after resolution.

 Understand how markets are structured.


\# Overview
Source: https://docs.polymarket.com/index

Build on the world's largest prediction market. Trade, integrate, and access real-time market data with the Polymarket API.

[🇺🇸Looking for Polymarket US documentation?Visit US Docs →](https://docs.polymarket.us/)

# Polymarket Documentation

Build on the world's largest prediction market. APIs, SDKs, and tools for prediction market developers.


## Developer Quickstart

Make your first API request in minutes. Learn the basics of the Polymarket platform, fetch market data, place orders, and redeem winning positions.


[Get Started →](https://docs.polymarket.com/quickstart)

\`\`\`typescript TypeScript theme={null}
import { ClobClient, Side } from "@polymarket/clob-client";

const client = new ClobClient(host, chainId, signer, creds);

const order = await client.createAndPostOrder(
{ tokenID, price: 0.50, size: 10, side: Side.BUY },
{ tickSize: "0.01", negRisk: false }
);
\`\`\`

\`\`\`python Python theme={null}
from py\_clob\_client.client import ClobClient
from py\_clob\_client.order\_builder.constants import BUY

client = ClobClient(host, key=key, chain\_id=chain\_id, creds=creds)
order = client.create\_and\_post\_order(
OrderArgs(token\_id=token\_id, price=0.50, size=10, side=BUY),
options={"tick\_size": "0.01", "neg\_risk": False}
)
\`\`\`

\`\`\`rust Rust theme={null}
use polymarket\_client\_sdk::clob::{Client, Config};
use polymarket\_client\_sdk::clob::types::Side;
use polymarket\_client\_sdk::types::dec;

let client = Client::new(host, Config::default())?.authentication\_builder(&signer).authenticate().await?;
let order = client.limit\_order().token\_id(token\_id).price(dec!(0.50)).size(dec!(10)).side(Side::Buy).build().await?;
let signed = client.sign(&signer, order).await?;
let response = client.post\_order(signed).await?;
\`\`\`


## Get Familiar with Polymarket

Learn the fundamentals, explore our APIs, and start building on the world's largest prediction market.


Set up your environment and make your first API call in minutes.

Understand markets, events, tokens, and how trading works.

Explore REST endpoints, WebSocket streams, and authentication.

Official Python, TypeScript, and Rust libraries for faster development.


\# Fetching Markets
Source: https://docs.polymarket.com/market-data/fetching-markets

Three strategies for discovering and querying markets

 Both the events and markets endpoints are paginated. See
 \[pagination\](#pagination) for details.

There are three main strategies for retrieving market data, each optimized for different use cases:

1\. \*\*By Slug\*\* — Best for fetching specific individual markets or events
2\. \*\*By Tags\*\* — Ideal for filtering markets by category or sport
3\. \*\*Via Events Endpoint\*\* — Most efficient for retrieving all active markets

\\*\\*\\*

\## Fetch by Slug

\*\*Use case:\*\* When you need to retrieve a specific market or event that you already know about.

Individual markets and events are best fetched using their unique slug identifier. The slug can be found directly in the Polymarket frontend URL.

\### How to Extract the Slug

From any Polymarket URL, the slug is the path segment after \`/event/\`:

\`\`\`
https://polymarket.com/event/fed-decision-in-october
 ↑
 Slug: fed-decision-in-october
\`\`\`

\### Examples

\`\`\`bash theme={null}
\# Fetch an event by slug (query parameter)
curl "https://gamma-api.polymarket.com/events?slug=fed-decision-in-october"

\# Or use the path endpoint
curl "https://gamma-api.polymarket.com/events/slug/fed-decision-in-october"
\`\`\`

\`\`\`bash theme={null}
\# Fetch a market by slug (query parameter)
curl "https://gamma-api.polymarket.com/markets?slug=fed-decision-in-october"

\# Or use the path endpoint
curl "https://gamma-api.polymarket.com/markets/slug/fed-decision-in-october"
\`\`\`

\\*\\*\\*

\## Fetch by Tags

\*\*Use case:\*\* When you want to filter markets by category, sport, or topic.

Tags provide a way to categorize and filter markets. You can discover available tags and then use them to filter your requests.

\### Discover Available Tags

\*\*General tags:\*\* \`GET /tags\` (Gamma API)

\*\*Sports tags and metadata:\*\* \`GET /sports\` (Gamma API)

The \`/sports\` endpoint returns metadata for sports including tag IDs, images, resolution sources, and series information.

\### Filter by Tag

Once you have tag IDs, use the \`tag\_id\` parameter in both events and markets endpoints:

\`\`\`bash theme={null}
\# Fetch events for a specific tag
curl "https://gamma-api.polymarket.com/events?tag\_id=100381&limit=10&active=true&closed=false"
\`\`\`

\### Additional Tag Filtering

You can also:

\\* Use \`related\_tags=true\` to include related tag markets
\\* Exclude specific tags with \`exclude\_tag\_id\`

\`\`\`bash theme={null}
\# Include related tags
curl "https://gamma-api.polymarket.com/events?tag\_id=100381&related\_tags=true&active=true&closed=false"
\`\`\`

\\*\\*\\*

\## Fetch All Active Markets

\*\*Use case:\*\* When you need to retrieve all available active markets, typically for broader analysis or market discovery.

The most efficient approach is to use the events endpoint with \`active=true&closed=false\`, as events contain their associated markets.

\`\`\`bash theme={null}
curl "https://gamma-api.polymarket.com/events?active=true&closed=false&limit=100"
\`\`\`

\### Key Parameters

\| Parameter \| Description \|
\| \-\-\-\-\-\-\-\-\-\-\- \| \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- \|
\| \`order\` \| Field to order by (\`volume\_24hr\`, \`volume\`, \`liquidity\`, \`start\_date\`, \`end\_date\`, \`competitive\`, \`closed\_time\`) \|
\| \`ascending\` \| Sort direction (\`true\` for ascending, \`false\` for descending). Default: \`false\` \|
\| \`active\` \| Filter by active status (\`true\` for live tradable events) \|
\| \`closed\` \| Filter by closed status \|
\| \`limit\` \| Results per page \|
\| \`offset\` \| Number of results to skip for pagination \|

\`\`\`bash theme={null}
\# Get the highest volume active events
curl "https://gamma-api.polymarket.com/events?active=true&closed=false&order=volume\_24hr&ascending=false&limit=100"
\`\`\`

\\*\\*\\*

\## Pagination

All list endpoints return paginated responses with \`limit\` and \`offset\` parameters:

\`\`\`bash theme={null}
\# Page 1: First 50 results
curl "https://gamma-api.polymarket.com/events?active=true&closed=false&limit=50&offset=0"

\# Page 2: Next 50 results
curl "https://gamma-api.polymarket.com/events?active=true&closed=false&limit=50&offset=50"

\# Page 3: Next 50 results
curl "https://gamma-api.polymarket.com/events?active=true&closed=false&limit=50&offset=100"
\`\`\`

\\*\\*\\*

\## Best Practices

1\. \*\*For individual markets:\*\* Use the slug method for direct lookups
2\. \*\*For category browsing:\*\* Use tag filtering to reduce API calls
3\. \*\*For complete market discovery:\*\* Use the events endpoint with pagination
4\. \*\*Always include \`active=true&closed=false\`\*\* unless you specifically need historical data
5\. \*\*Use the events endpoint\*\* and work backwards — events contain their associated markets, reducing the number of API calls needed

\\*\\*\\*

\## Next Steps

 Full endpoint documentation with parameters and response schemas.

 Query onchain data directly from the Polymarket subgraph.


\# Overview
Source: https://docs.polymarket.com/market-data/overview

Fetch market data with no authentication required

All market data is available through public REST endpoints. No API key, no authentication, no wallet required.

\`\`\`bash theme={null}
curl "https://gamma-api.polymarket.com/events?limit=5"
\`\`\`

\\*\\*\\*

\## Data Model

Polymarket structures data using two organizational models. The most fundamental element is always markets—events simply provide additional organization.

 A top-level object representing a question (e.g., "Who will win the 2024
 Presidential Election?"). Contains one or more markets.

 A specific tradable binary outcome within an event. Maps to a pair of CLOB
 token IDs, a market address, a question ID, and a condition ID.


\### Single-Market Events vs Multi-Market Events

\| Type \| Example \|
\| \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- \| \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- \|
\| Single-market event \| "Will Bitcoin reach \\$100k?" → 1 market (Yes/No) \|
\| Multi-market event \| "Where will Barron Trump attend College?" → Markets for Georgetown, NYU, UPenn, Harvard, Other \|

\### Outcomes and Prices

Each market has \`outcomes\` and \`outcomePrices\` arrays that map 1:1. Prices represent implied probabilities:

\`\`\`json theme={null}
{
 "outcomes": "\[\\"Yes\\", \\"No\\"\]",
 "outcomePrices": "\[\\"0.20\\", \\"0.80\\"\]"
}
// Index 0: "Yes" → 0.20 (20% probability)
// Index 1: "No" → 0.80 (80% probability)
\`\`\`

Markets can be traded via the CLOB if \`enableOrderBook\` is \`true\`.

\\*\\*\\*

\## Available Data

Endpoints are split across three APIs. See the \[API Reference\](/api-reference/introduction) for full endpoint documentation with parameters and response schemas.

\### Gamma API - Events Markets and Discovery

\| Endpoint \| Description \|
\| \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- \| \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- \|
\| \`GET /events\` \| List events with filtering and pagination \|
\| \`GET /events/{id}\` \| Get a single event by ID \|
\| \`GET /markets\` \| List markets with filtering and pagination \|
\| \`GET /markets/{id}\` \| Get a single market by ID \|
\| \`GET /public-search\` \| Search across events, markets, and profiles \|
\| \`GET /tags\` \| Ranked tags/categories \|
\| \`GET /series\` \| Series (grouped events) \|
\| \`GET /sports\` \| Sports metadata \|
\| \`GET /teams\` \| Teams \|

\### CLOB API - Prices and Orderbooks

\| Endpoint \| Description \|
\| \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- \| \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- \|
\| \`GET /price\` \| Price for a single token \|
\| \`GET /prices\` \| Prices for multiple tokens \|
\| \`GET /book\` \| Order book for a token \|
\| \`POST /books\` \| Order books for multiple tokens \|
\| \`GET /prices-history\` \| Historical price data for a token \|
\| \`GET /midpoint\` \| Midpoint price for a token \|
\| \`GET /spread\` \| Spread for a token \|

\### Data API - Positions Trades and Analytics

\| Endpoint \| Description \|
\| \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- \| \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- \|
\| \`GET /positions?user={address}\` \| Current positions for a user \|
\| \`GET /closed-positions?user={address}\` \| Closed positions for a user \|
\| \`GET /activity?user={address}\` \| Onchain activity for a user \|
\| \`GET /value?user={address}\` \| Total position value \|
\| \`GET /oi\` \| Open interest for a market \|
\| \`GET /holders\` \| Top holders of a market \|
\| \`GET /trades\` \| Trade history \|

\\*\\*\\*

\## Next Steps

 Three strategies for discovering and querying markets.

 Full endpoint documentation with parameters and response schemas.


\# Subgraph
Source: https://docs.polymarket.com/market-data/subgraph

Query onchain Polymarket data using GraphQL

Polymarket's subgraphs provide indexed onchain data via GraphQL. Use them to query positions, volume, liquidity data, orders, activity, and market data.

\## Available Subgraphs

\| Subgraph \| Description \| Endpoint \|
\| \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- \| \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- \| \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- \|
\| \*\*Positions\*\* \| User token balances \| \[GraphQL Playground\](https://api.goldsky.com/api/public/project\_cl6mb8i9h0003e201j6li0diw/subgraphs/positions-subgraph/0.0.7/gn) \|
\| \*\*Orders\*\* \| Order book and trade events \| \[GraphQL Playground\](https://api.goldsky.com/api/public/project\_cl6mb8i9h0003e201j6li0diw/subgraphs/orderbook-subgraph/0.0.1/gn) \|
\| \*\*Activity\*\* \| Splits, merges, redemptions \| \[GraphQL Playground\](https://api.goldsky.com/api/public/project\_cl6mb8i9h0003e201j6li0diw/subgraphs/activity-subgraph/0.0.4/gn) \|
\| \*\*Open Interest\*\* \| Market and global OI \| \[GraphQL Playground\](https://api.goldsky.com/api/public/project\_cl6mb8i9h0003e201j6li0diw/subgraphs/oi-subgraph/0.0.6/gn) \|
\| \*\*PNL\*\* \| User position P\\&L \| \[GraphQL Playground\](https://api.goldsky.com/api/public/project\_cl6mb8i9h0003e201j6li0diw/subgraphs/pnl-subgraph/0.0.14/gn) \|

 Subgraphs are hosted by \[Goldsky\](https://goldsky.com). Each endpoint includes
 an interactive GraphQL playground for exploring the schema.

\## Querying

Send GraphQL queries via POST request to any subgraph endpoint.

\`\`\`bash theme={null}
curl -X POST \
 https://api.goldsky.com/api/public/project\_cl6mb8i9h0003e201j6li0diw/subgraphs/orderbook-subgraph/0.0.1/gn \
 -H "Content-Type: application/json" \
 -d '{
 "query": "query MyQuery { orderbooks { id tradesQuantity } }"
 }'
\`\`\`

\## Schema Reference

\### Positions

\| Query \| Description \|
\| \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- \| \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- \|
\| \`userBalance\` / \`userBalances\` \| User token balances \|
\| \`netUserBalance\` / \`netUserBalances\` \| Aggregated net balances \|
\| \`tokenIdCondition\` / \`tokenIdConditions\` \| Token ID to condition mappings \|
\| \`condition\` / \`conditions\` \| Market conditions \|

\### Orders

\| Query \| Description \|
\| \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- \| \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- \|
\| \`marketData\` / \`marketDatas\` \| Market-level data \|
\| \`orderFilledEvent\` / \`orderFilledEvents\` \| Order fill events \|
\| \`ordersMatchedEvent\` / \`ordersMatchedEvents\` \| Order match events \|
\| \`orderbook\` / \`orderbooks\` \| Orderbook state \|
\| \`ordersMatchedGlobal\` / \`ordersMatchedGlobals\` \| Global match statistics \|

\### Activity

\| Query \| Description \|
\| \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- \| \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- \|
\| \`split\` / \`splits\` \| USDC to token splits \|
\| \`merge\` / \`merges\` \| Token to USDC merges \|
\| \`redemption\` / \`redemptions\` \| Position redemptions \|
\| \`negRiskConversion\` / \`negRiskConversions\` \| Neg risk conversions \|
\| \`negRiskEvent\` / \`negRiskEvents\` \| Neg risk event data \|
\| \`fixedProductMarketMaker\` / \`fixedProductMarketMakers\` \| FPMM data \|
\| \`position\` / \`positions\` \| Position records \|
\| \`condition\` / \`conditions\` \| Market conditions \|

\### Open Interest

\| Query \| Description \|
\| \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- \| \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- \|
\| \`condition\` / \`conditions\` \| Market conditions \|
\| \`negRiskEvent\` / \`negRiskEvents\` \| Neg risk event data \|
\| \`marketOpenInterest\` / \`marketOpenInterests\` \| Per-market open interest \|
\| \`globalOpenInterest\` / \`globalOpenInterests\` \| Global open interest \|

\### PNL

\| Query \| Description \|
\| \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- \| \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- \|
\| \`userPosition\` / \`userPositions\` \| User position P\\&L data \|
\| \`negRiskEvent\` / \`negRiskEvents\` \| Neg risk event data \|
\| \`condition\` / \`conditions\` \| Market conditions \|
\| \`fpmm\` / \`fpmms\` \| Fixed product market maker data \|

\## Source Code

The subgraph is open source. Review the schema and mappings on GitHub:

 View source code, schema definitions, and deployment configuration.

\# Market Channel
Source: https://docs.polymarket.com/market-data/websocket/market-channel

Real-time orderbook, price, and trade data

Public channel for market data updates (level 2 price data). Subscribe with asset IDs to receive orderbook snapshots, price changes, trade executions, and market events.

\## Endpoint

\`\`\`
wss://ws-subscriptions-clob.polymarket.com/ws/market
\`\`\`

\## Subscription

\`\`\`json theme={null}
{
 "assets\_ids": \["", ""\],
 "type": "market",
 "custom\_feature\_enabled": true
}
\`\`\`

Set \`custom\_feature\_enabled: true\` to receive \`best\_bid\_ask\`, \`new\_market\`, and \`market\_resolved\` events.

\## Message Types

Each message includes an \`event\_type\` field identifying the type.

\### book

Emitted when first subscribed to a market and when there is a trade that affects the book.

\`\`\`json theme={null}
{
 "event\_type": "book",
 "asset\_id": "65818619657568813474341868652308942079804919287380422192892211131408793125422",
 "market": "0xbd31dc8a20211944f6b70f31557f1001557b59905b7738480ca09bd4532f84af",
 "bids": \[\
 { "price": ".48", "size": "30" },\
 { "price": ".49", "size": "20" },\
 { "price": ".50", "size": "15" }\
 \],
 "asks": \[\
 { "price": ".52", "size": "25" },\
 { "price": ".53", "size": "60" },\
 { "price": ".54", "size": "10" }\
 \],
 "timestamp": "123456789000",
 "hash": "0x0...."
}
\`\`\`

\### price\\\_change

Emitted when a new order is placed or an order is cancelled.

\`\`\`json theme={null}
{
 "market": "0x5f65177b394277fd294cd75650044e32ba009a95022d88a0c1d565897d72f8f1",
 "price\_changes": \[\
 {\
 "asset\_id": "71321045679252212594626385532706912750332728571942532289631379312455583992563",\
 "price": "0.5",\
 "size": "200",\
 "side": "BUY",\
 "hash": "56621a121a47ed9333273e21c83b660cff37ae50",\
 "best\_bid": "0.5",\
 "best\_ask": "1"\
 },\
 {\
 "asset\_id": "52114319501245915516055106046884209969926127482827954674443846427813813222426",\
 "price": "0.5",\
 "size": "200",\
 "side": "SELL",\
 "hash": "1895759e4df7a796bf4f1c5a5950b748306923e2",\
 "best\_bid": "0",\
 "best\_ask": "0.5"\
 }\
 \],
 "timestamp": "1757908892351",
 "event\_type": "price\_change"
}
\`\`\`

A \`size\` of \`"0"\` means the price level has been removed from the book.

\### tick\\\_size\\\_change

Emitted when the minimum tick size of a market changes. This happens when the book's price reaches the limits: price > 0.96 or price \\< 0.04.

\`\`\`json theme={null}
{
 "event\_type": "tick\_size\_change",
 "asset\_id": "65818619657568813474341868652308942079804919287380422192892211131408793125422",
 "market": "0xbd31dc8a20211944f6b70f31557f1001557b59905b7738480ca09bd4532f84af",
 "old\_tick\_size": "0.01",
 "new\_tick\_size": "0.001",
 "timestamp": "100000000"
}
\`\`\`

\### last\\\_trade\\\_price

Emitted when a maker and taker order is matched, creating a trade event.

\`\`\`json theme={null}
{
 "asset\_id": "114122071509644379678018727908709560226618148003371446110114509806601493071694",
 "event\_type": "last\_trade\_price",
 "fee\_rate\_bps": "0",
 "market": "0x6a67b9d828d53862160e470329ffea5246f338ecfffdf2cab45211ec578b0347",
 "price": "0.456",
 "side": "BUY",
 "size": "219.217767",
 "timestamp": "1750428146322"
}
\`\`\`

\### best\\\_bid\\\_ask

Requires \`custom\_feature\_enabled: true\`.

Emitted when the best bid or ask prices for a market change.

\`\`\`json theme={null}
{
 "event\_type": "best\_bid\_ask",
 "market": "0x0005c0d312de0be897668695bae9f32b624b4a1ae8b140c49f08447fcc74f442",
 "asset\_id": "85354956062430465315924116860125388538595433819574542752031640332592237464430",
 "best\_bid": "0.73",
 "best\_ask": "0.77",
 "spread": "0.04",
 "timestamp": "1766789469958"
}
\`\`\`

\### new\\\_market

Requires \`custom\_feature\_enabled: true\`.

Emitted when a new market is created.

\`\`\`json theme={null}
{
 "id": "1031769",
 "question": "Will NVIDIA (NVDA) close above $240 end of January?",
 "market": "0x311d0c4b6671ab54af4970c06fcf58662516f5168997bdda209ec3db5aa6b0c1",
 "slug": "nvda-above-240-on-january-30-2026",
 "description": "This market will resolve to \\"Yes\\" if the official closing price...",
 "assets\_ids": \[\
 "76043073756653678226373981964075571318267289248134717369284518995922789326425",\
 "31690934263385727664202099278545688007799199447969475608906331829650099442770"\
 \],
 "outcomes": \["Yes", "No"\],
 "event\_message": {
 "id": "125819",
 "ticker": "nvda-above-in-january-2026",
 "slug": "nvda-above-in-january-2026",
 "title": "Will NVIDIA (NVDA) close above \_\_\_ end of January?",
 "description": "This market will resolve to \\"Yes\\" if the official closing price..."
 },
 "timestamp": "1766790415550",
 "event\_type": "new\_market"
}
\`\`\`

\### market\\\_resolved

Requires \`custom\_feature\_enabled: true\`.

Emitted when a market is resolved.

\`\`\`json theme={null}
{
 "id": "1031769",
 "question": "Will NVIDIA (NVDA) close above $240 end of January?",
 "market": "0x311d0c4b6671ab54af4970c06fcf58662516f5168997bdda209ec3db5aa6b0c1",
 "slug": "nvda-above-240-on-january-30-2026",
 "description": "This market will resolve to \\"Yes\\" if the official closing price...",
 "assets\_ids": \[\
 "76043073756653678226373981964075571318267289248134717369284518995922789326425",\
 "31690934263385727664202099278545688007799199447969475608906331829650099442770"\
 \],
 "outcomes": \["Yes", "No"\],
 "winning\_asset\_id": "76043073756653678226373981964075571318267289248134717369284518995922789326425",
 "winning\_outcome": "Yes",
 "event\_message": {
 "id": "125819",
 "ticker": "nvda-above-in-january-2026",
 "slug": "nvda-above-in-january-2026",
 "title": "Will NVIDIA (NVDA) close above \_\_\_ end of January?",
 "description": "This market will resolve to \\"Yes\\" if the official closing price..."
 },
 "timestamp": "1766790415550",
 "event\_type": "market\_resolved"
}
\`\`\`

\# Overview
Source: https://docs.polymarket.com/market-data/websocket/overview

Real-time market data and trading updates via WebSocket

Polymarket provides WebSocket channels for near real-time streaming of orderbook data, trades, and personal order activity. There are four available channels: \`market\`, \`user\`, \`sports\`, and \`RTDS\` (Real-Time Data Socket).

\## Channels

\| Channel \| Endpoint \| Auth \|
\| \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- \| \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- \| \-\-\-\-\-\-\-\- \|
\| Market \| \`wss://ws-subscriptions-clob.polymarket.com/ws/market\` \| No \|
\| User \| \`wss://ws-subscriptions-clob.polymarket.com/ws/user\` \| Yes \|
\| Sports \| \`wss://sports-api.polymarket.com/ws\` \| No \|
\| \[RTDS\](/market-data/websocket/rtds) \| \`wss://ws-live-data.polymarket.com\` \| Optional \|

\### Market Channel

\| Type \| Description \| Custom Feature \|
\| \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- \| \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- \| \-\-\-\-\-\-\-\-\-\-\-\-\-\- \|
\| \`book\` \| Full orderbook snapshot \| No \|
\| \`price\_change\` \| Price level updates \| No \|
\| \`tick\_size\_change\` \| Tick size changes \| No \|
\| \`last\_trade\_price\` \| Trade executions \| No \|
\| \`best\_bid\_ask\` \| Best prices update \| Yes \|
\| \`new\_market\` \| New market created \| Yes \|
\| \`market\_resolved\` \| Market resolution \| Yes \|

Types marked "Custom Feature" require \`custom\_feature\_enabled: true\` in your subscription.

\### User Channel

\| Type \| Description \|
\| \-\-\-\-\-\-\- \| \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- \|
\| \`trade\` \| Trade lifecycle updates (MATCHED → CONFIRMED) \|
\| \`order\` \| Order placements, updates, and cancellations \|

\### Sports

\| Type \| Description \|
\| \-\-\-\-\-\-\-\-\-\-\-\-\-\- \| \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- \|
\| \`sport\_result\` \| Live game scores, periods, and status \|

\## Subscribing

Send a subscription message after connecting to specify which data you want to receive.

\### Market Channel

\`\`\`json theme={null}
{
 "assets\_ids": \[\
 "21742633143463906290569050155826241533067272736897614950488156847949938836455",\
 "48331043336612883890938759509493159234755048973500640148014422747788308965732"\
 \],
 "type": "market",
 "custom\_feature\_enabled": true
}
\`\`\`

\| Field \| Type \| Description \|
\| \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- \| \-\-\-\-\-\-\-\-\- \| \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- \|
\| \`assets\_ids\` \| string\\\[\] \| Token IDs to subscribe to \|
\| \`type\` \| string \| Channel identifier \|
\| \`custom\_feature\_enabled\` \| boolean \| Enable \`best\_bid\_ask\`, \`new\_market\`, and \`market\_resolved\` events \|

\### User Channel

\`\`\`json theme={null}
{
 "auth": {
 "apiKey": "your-api-key",
 "secret": "your-api-secret",
 "passphrase": "your-passphrase"
 },
 "markets": \["0x1234...condition\_id"\],
 "type": "user"
}
\`\`\`

 The \`auth\` fields (\`apiKey\`, \`secret\`, \`passphrase\`) are \*\*only required for
 the user channel\*\*. For the market channel, these fields are optional and can
 be omitted.

\| Field \| Type \| Description \|
\| \-\-\-\-\-\-\-\-\- \| \-\-\-\-\-\-\-\-\- \| \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- \|
\| \`auth\` \| object \| API credentials (\`apiKey\`, \`secret\`, \`passphrase\`) \|
\| \`markets\` \| string\\\[\] \| Condition IDs to receive events for \|
\| \`type\` \| string \| Channel identifier \|

 The user channel subscribes by \*\*condition IDs\*\* (market identifiers), not
 asset IDs. Each market has one condition ID but two asset IDs (Yes and No
 tokens).

\### Sports Channel

No subscription message required. Connect and start receiving data for all active sports events.

\## Dynamic Subscription

Modify subscriptions without reconnecting.

\### Subscribe to more assets

\`\`\`json theme={null}
{
 "assets\_ids": \["new\_asset\_id\_1", "new\_asset\_id\_2"\],
 "operation": "subscribe",
 "custom\_feature\_enabled": true
}
\`\`\`

\### Unsubscribe from assets

\`\`\`json theme={null}
{
 "assets\_ids": \["asset\_id\_to\_remove"\],
 "operation": "unsubscribe"
}
\`\`\`

For the user channel, use \`markets\` instead of \`assets\_ids\`:

\`\`\`json theme={null}
{
 "markets": \["0x1234...condition\_id"\],
 "operation": "subscribe"
}
\`\`\`

\## Heartbeats

\### Market and User Channels

Send \`PING\` every 10 seconds. The server responds with \`PONG\`.

\`\`\`
PING
\`\`\`

\### Sports Channel

The server sends \`ping\` every 5 seconds. Respond with \`pong\` within 10 seconds.

\`\`\`
pong
\`\`\`

 If you don't respond to the server's ping within 10 seconds, the connection
 will be closed.

\## Troubleshooting

 Send a valid subscription message immediately after connecting. The server may
 close connections that don't subscribe within a timeout period.

 You're not sending heartbeats. Send \`PING\` every 10 seconds for market/user
 channels, or respond to server \`ping\` with \`pong\` for the sports channel.

 1\. Verify your asset IDs or condition IDs are correct 2. Check that the
 markets are active (not resolved) 3. Set \`custom\_feature\_enabled: true\` if
 expecting \`best\_bid\_ask\`, \`new\_market\`, or \`market\_resolved\` events

 Verify your API credentials are correct and haven't expired.

\# Real-Time Data Socket
Source: https://docs.polymarket.com/market-data/websocket/rtds

Stream comments and crypto prices via WebSocket

The Polymarket Real-Time Data Socket (RTDS) is a WebSocket-based streaming service that provides real-time updates for \*\*comments\*\* and \*\*crypto prices\*\*.

 Official RTDS TypeScript client (\`real-time-data-client\`).

\## Endpoint

\`\`\`
wss://ws-live-data.polymarket.com
\`\`\`

Some user-specific streams may require \`gamma\_auth\` with your wallet address.

\## Subscribing

Send a JSON message to subscribe to data streams:

\`\`\`json theme={null}
{
 "action": "subscribe",
 "subscriptions": \[\
 {\
 "topic": "topic\_name",\
 "type": "message\_type",\
 "filters": "optional\_filter\_string",\
 "gamma\_auth": {\
 "address": "wallet\_address"\
 }\
 }\
 \]
}
\`\`\`

To unsubscribe, send the same structure with \`"action": "unsubscribe"\`.

Subscriptions can be added, removed, and modified without disconnecting. Send \`PING\` messages every 5 seconds to maintain the connection.

Only the subscription types documented below are supported.

\## Message Structure

All messages follow this structure:

\`\`\`json theme={null}
{
 "topic": "string",
 "type": "string",
 "timestamp": "number",
 "payload": "object"
}
\`\`\`

\| Field \| Type \| Description \|
\| \-\-\-\-\-\-\-\-\-\-\- \| \-\-\-\-\-\- \| \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- \|
\| \`topic\` \| string \| The subscription topic (e.g., \`crypto\_prices\`, \`comments\`) \|
\| \`type\` \| string \| The message type/event (e.g., \`update\`, \`reaction\_created\`) \|
\| \`timestamp\` \| number \| Unix timestamp in milliseconds when the message was sent \|
\| \`payload\` \| object \| Event-specific data object \|

\## Crypto Prices

Real-time cryptocurrency price data from two sources: \*\*Binance\*\* and \*\*Chainlink\*\*. No authentication required.

\### Binance Source

Subscribe to all symbols:

\`\`\`json theme={null}
{
 "action": "subscribe",
 "subscriptions": \[\
 {\
 "topic": "crypto\_prices",\
 "type": "update"\
 }\
 \]
}
\`\`\`

Subscribe to specific symbols with a comma-separated filter:

\`\`\`json theme={null}
{
 "action": "subscribe",
 "subscriptions": \[\
 {\
 "topic": "crypto\_prices",\
 "type": "update",\
 "filters": "solusdt,btcusdt,ethusdt"\
 }\
 \]
}
\`\`\`

Symbols use lowercase concatenated format (e.g., \`solusdt\`, \`btcusdt\`).

\*\*Solana price update:\*\*

\`\`\`json theme={null}
{
 "topic": "crypto\_prices",
 "type": "update",
 "timestamp": 1753314064237,
 "payload": {
 "symbol": "solusdt",
 "timestamp": 1753314064213,
 "value": 189.55
 }
}
\`\`\`

\*\*Bitcoin price update:\*\*

\`\`\`json theme={null}
{
 "topic": "crypto\_prices",
 "type": "update",
 "timestamp": 1753314088421,
 "payload": {
 "symbol": "btcusdt",
 "timestamp": 1753314088395,
 "value": 67234.50
 }
}
\`\`\`

\### Chainlink Source

 \*\*Trading 15m Crypto Markets?\*\* Get a sponsored Chainlink API key with onboarding support from Chainlink. Fill out \[this form\](https://pm-ds-request.streams.chain.link/).

Subscribe to all symbols:

\`\`\`json theme={null}
{
 "action": "subscribe",
 "subscriptions": \[\
 {\
 "topic": "crypto\_prices\_chainlink",\
 "type": "\*",\
 "filters": ""\
 }\
 \]
}
\`\`\`

Subscribe to a specific symbol with a JSON filter:

\`\`\`json theme={null}
{
 "action": "subscribe",
 "subscriptions": \[\
 {\
 "topic": "crypto\_prices\_chainlink",\
 "type": "\*",\
 "filters": "{\\"symbol\\":\\"eth/usd\\"}"\
 }\
 \]
}
\`\`\`

Symbols use slash-separated format (e.g., \`eth/usd\`, \`btc/usd\`).

\*\*Ethereum price update:\*\*

\`\`\`json theme={null}
{
 "topic": "crypto\_prices\_chainlink",
 "type": "update",
 "timestamp": 1753314064237,
 "payload": {
 "symbol": "eth/usd",
 "timestamp": 1753314064213,
 "value": 3456.78
 }
}
\`\`\`

\*\*Bitcoin price update:\*\*

\`\`\`json theme={null}
{
 "topic": "crypto\_prices\_chainlink",
 "type": "update",
 "timestamp": 1753314088421,
 "payload": {
 "symbol": "btc/usd",
 "timestamp": 1753314088395,
 "value": 67234.50
 }
}
\`\`\`

\### Price Payload Fields

\| Field \| Type \| Description \|
\| \-\-\-\-\-\-\-\-\-\-\- \| \-\-\-\-\-\- \| \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- \|
\| \`symbol\` \| string \| Trading pair symbol. \*\*Binance\*\*: lowercase concatenated (e.g., \`solusdt\`, \`btcusdt\`). \*\*Chainlink\*\*: slash-separated (e.g., \`eth/usd\`, \`btc/usd\`) \|
\| \`timestamp\` \| number \| When the price was recorded, in Unix milliseconds \|
\| \`value\` \| number \| Current price value in the quote currency \|

\### Supported Symbols

\*\*Binance Source\*\* — lowercase concatenated format:

\\* \`btcusdt\` — Bitcoin to USDT
\\* \`ethusdt\` — Ethereum to USDT
\\* \`solusdt\` — Solana to USDT
\\* \`xrpusdt\` — XRP to USDT

\*\*Chainlink Source\*\* — slash-separated format:

\\* \`btc/usd\` — Bitcoin to USD
\\* \`eth/usd\` — Ethereum to USD
\\* \`sol/usd\` — Solana to USD
\\* \`xrp/usd\` — XRP to USD

\## Comments

Real-time comment events on the Polymarket platform, including new comments, replies, reactions, and removals. May require Gamma authentication for user-specific data.

\### Subscribe

\`\`\`json theme={null}
{
 "action": "subscribe",
 "subscriptions": \[\
 {\
 "topic": "comments",\
 "type": "comment\_created"\
 }\
 \]
}
\`\`\`

\### Message Types

\| Type \| Description \|
\| \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- \| \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- \|
\| \`comment\_created\` \| A user creates a new comment or reply \|
\| \`comment\_removed\` \| A comment is removed or deleted \|
\| \`reaction\_created\` \| A user adds a reaction to a comment \|
\| \`reaction\_removed\` \| A reaction is removed from a comment \|

\### comment\\\_created

Emitted when a user posts a new comment or replies to an existing one.

\`\`\`json theme={null}
{
 "topic": "comments",
 "type": "comment\_created",
 "timestamp": 1753454975808,
 "payload": {
 "body": "That's a good point about the definition.",
 "createdAt": "2025-07-25T14:49:35.801298Z",
 "id": "1763355",
 "parentCommentID": "1763325",
 "parentEntityID": 18396,
 "parentEntityType": "Event",
 "profile": {
 "baseAddress": "0xce533188d53a16ed580fd5121dedf166d3482677",
 "displayUsernamePublic": true,
 "name": "salted.caramel",
 "proxyWallet": "0x4ca749dcfa93c87e5ee23e2d21ff4422c7a4c1ee",
 "pseudonym": "Adored-Disparity"
 },
 "reactionCount": 0,
 "replyAddress": "0x0bda5d16f76cd1d3485bcc7a44bc6fa7db004cdd",
 "reportCount": 0,
 "userAddress": "0xce533188d53a16ed580fd5121dedf166d3482677"
 }
}
\`\`\`

A reply to the above comment — note \`parentCommentID\` references the parent:

\`\`\`json theme={null}
{
 "topic": "comments",
 "type": "comment\_created",
 "timestamp": 1753454985123,
 "payload": {
 "body": "I agree, the resolution criteria should be clearer.",
 "createdAt": "2025-07-25T14:49:45.120000Z",
 "id": "1763356",
 "parentCommentID": "1763355",
 "parentEntityID": 18396,
 "parentEntityType": "Event",
 "profile": {
 "baseAddress": "0x1234567890abcdef1234567890abcdef12345678",
 "displayUsernamePublic": true,
 "name": "trader",
 "proxyWallet": "0x9876543210fedcba9876543210fedcba98765432",
 "pseudonym": "Bright-Analysis"
 },
 "reactionCount": 0,
 "replyAddress": "0x0bda5d16f76cd1d3485bcc7a44bc6fa7db004cdd",
 "reportCount": 0,
 "userAddress": "0x1234567890abcdef1234567890abcdef12345678"
 }
}
\`\`\`

\### Comment Payload Fields

\| Field \| Type \| Description \|
\| \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- \| \-\-\-\-\-\- \| \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- \|
\| \`body\` \| string \| The text content of the comment \|
\| \`createdAt\` \| string \| ISO 8601 timestamp when the comment was created \|
\| \`id\` \| string \| Unique identifier for this comment \|
\| \`parentCommentID\` \| string \| ID of the parent comment if this is a reply (null for top-level comments) \|
\| \`parentEntityID\` \| number \| ID of the parent entity (event, market, etc.) \|
\| \`parentEntityType\` \| string \| Type of parent entity (\`Event\`, \`Market\`) \|
\| \`profile\` \| object \| Profile information of the comment author \|
\| \`reactionCount\` \| number \| Current number of reactions on this comment \|
\| \`replyAddress\` \| string \| Polygon address for replies (may differ from userAddress) \|
\| \`reportCount\` \| number \| Current number of reports on this comment \|
\| \`userAddress\` \| string \| Polygon address of the comment author \|

\### Profile Object Fields

\| Field \| Type \| Description \|
\| \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- \| \-\-\-\-\-\-\- \| \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- \|
\| \`baseAddress\` \| string \| User profile address \|
\| \`displayUsernamePublic\` \| boolean \| Whether the username is displayed publicly \|
\| \`name\` \| string \| User's display name \|
\| \`proxyWallet\` \| string \| Proxy wallet address used for transactions \|
\| \`pseudonym\` \| string \| Generated pseudonym for the user \|

\### Comment Hierarchy

Comments support nested threading:

\\* \*\*Top-level comments\*\*: \`parentCommentID\` is null or empty
\\* \*\*Reply comments\*\*: \`parentCommentID\` contains the ID of the parent comment
\\* All comments are associated with a \`parentEntityID\` and \`parentEntityType\` (\`Event\` or \`Market\`)

\## Troubleshooting

 Send \`PING\` messages every 5 seconds to keep the connection alive. Connection errors will trigger automatic reconnection attempts.

 Verify your subscription message is valid JSON with the correct \`action\`, \`topic\`, and \`type\` fields. Invalid subscription messages may result in connection closure.

 If subscribing to user-specific streams, ensure your \`gamma\_auth\` object includes a valid wallet \`address\`. Authentication failures will prevent subscription to protected topics.

\# Sports WebSocket
Source: https://docs.polymarket.com/market-data/websocket/sports

Live sports scores and game state

The Sports WebSocket provides real-time sports results updates, including scores, periods, and game status. No authentication required.

\## Endpoint

\`\`\`
wss://sports-api.polymarket.com/ws
\`\`\`

No subscription message required — connect and start receiving data for all active sports events.

\## Heartbeat

The server sends \`ping\` every 5 seconds. Respond with \`pong\` within 10 seconds or the connection will close.

\`\`\`javascript theme={null}
ws.onmessage = (event) => {
 if (event.data === "ping") {
 ws.send("pong");
 return;
 }

 // Handle JSON messages...
};
\`\`\`

\## Message Type

Each message is a JSON object with game state fields.

\### sport\\\_result

Emitted when:

\\* A match goes live
\\* The score changes
\\* The period changes (e.g., halftime, overtime)
\\* A match ends
\\* Possession changes (NFL and CFB only)

\*\*NFL (in progress):\*\*

\`\`\`json theme={null}
{
 "gameId": 19439,
 "leagueAbbreviation": "nfl",
 "slug": "nfl-lac-buf-2025-01-26",
 "homeTeam": "LAC",
 "awayTeam": "BUF",
 "status": "InProgress",
 "score": "3-16",
 "period": "Q4",
 "elapsed": "5:18",
 "live": true,
 "ended": false,
 "turn": "lac"
}
\`\`\`

\*\*Esports — CS2 (finished):\*\*

\`\`\`json theme={null}
{
 "gameId": 1317359,
 "leagueAbbreviation": "cs2",
 "slug": "cs2-arcred-the-glecs-2025-07-20",
 "homeTeam": "ARCRED",
 "awayTeam": "The glecs",
 "status": "finished",
 "score": "000-000\|2-0\|Bo3",
 "period": "2/3",
 "live": false,
 "ended": true,
 "finished\_timestamp": "2025-07-20T18:30:00.000Z"
}
\`\`\`

The \`finished\_timestamp\` field is an ISO 8601 timestamp only present when \`ended: true\`.

The \`slug\` field follows the format \`{league}-{team1}-{team2}-{date}\` (e.g., \`nfl-buf-kc-2025-01-26\`).

\## Period Values

\| Period \| Description \|
\| \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- \| \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- \|
\| \`1H\` \| First half \|
\| \`2H\` \| Second half \|
\| \`1Q\`, \`2Q\`, \`3Q\`, \`4Q\` \| Quarters (NFL, NBA) \|
\| \`HT\` \| Halftime \|
\| \`FT\` \| Full time (match ended in regulation) \|
\| \`FT OT\` \| Full time with overtime \|
\| \`FT NR\` \| Full time, no result (draw or canceled) \|
\| \`End 1\`, \`End 2\`, ... \| End of inning (MLB) \|
\| \`1/3\`, \`2/3\`, \`3/3\` \| Map number in Bo3 series (Esports) \|
\| \`1/5\`, \`2/5\`, ... \| Map number in Bo5 series (Esports) \|

\## Game Status Values

Game status values vary by sport:

\### NFL

\| Status \| Description \|
\| \-\-\-\-\-\-\-\-\-\-\-\-\-\- \| \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- \|
\| \`Scheduled\` \| Game not yet started \|
\| \`InProgress\` \| Game currently playing \|
\| \`Final\` \| Game completed in regulation \|
\| \`F/OT\` \| Final after overtime \|
\| \`Suspended\` \| Game suspended \|
\| \`Postponed\` \| Game postponed \|
\| \`Delayed\` \| Game delayed \|
\| \`Canceled\` \| Game canceled \|
\| \`Forfeit\` \| Game forfeited \|
\| \`NotNecessary\` \| Scheduled, but not needed \|

\### NHL

\| Status \| Description \|
\| \-\-\-\-\-\-\-\-\-\-\-\-\-\- \| \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- \|
\| \`Scheduled\` \| Game not yet started \|
\| \`InProgress\` \| Game currently playing \|
\| \`Final\` \| Game completed in regulation \|
\| \`F/OT\` \| Final after overtime \|
\| \`F/SO\` \| Final after shootout \|
\| \`Suspended\` \| Game suspended \|
\| \`Postponed\` \| Game postponed \|
\| \`Delayed\` \| Game delayed \|
\| \`Canceled\` \| Game canceled \|
\| \`Forfeit\` \| Game forfeited \|
\| \`NotNecessary\` \| Scheduled, but not needed \|

\### MLB

\| Status \| Description \|
\| \-\-\-\-\-\-\-\-\-\-\-\-\-\- \| \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- \|
\| \`Scheduled\` \| Game not yet started \|
\| \`InProgress\` \| Game currently playing \|
\| \`Final\` \| Game completed \|
\| \`Suspended\` \| Game suspended \|
\| \`Delayed\` \| Game delayed \|
\| \`Postponed\` \| Game postponed \|
\| \`Canceled\` \| Game canceled \|
\| \`Forfeit\` \| Game forfeited \|
\| \`NotNecessary\` \| Scheduled, but not needed \|

\### NBA and CBB

\| Status \| Description \|
\| \-\-\-\-\-\-\-\-\-\-\-\-\-\- \| \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- \|
\| \`Scheduled\` \| Game not yet started \|
\| \`InProgress\` \| Game currently playing \|
\| \`Final\` \| Game completed \|
\| \`F/OT\` \| Final after overtime \|
\| \`Suspended\` \| Game suspended \|
\| \`Postponed\` \| Game postponed \|
\| \`Delayed\` \| Game delayed \|
\| \`Canceled\` \| Game canceled \|
\| \`Forfeit\` \| Game forfeited \|
\| \`NotNecessary\` \| Scheduled, but not needed \|

\### CFB

\| Status \| Description \|
\| \-\-\-\-\-\-\-\-\-\-\-\- \| \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- \|
\| \`Scheduled\` \| Game not yet started \|
\| \`InProgress\` \| Game currently playing \|
\| \`Final\` \| Game completed \|
\| \`F/OT\` \| Final after overtime \|
\| \`Suspended\` \| Game suspended \|
\| \`Postponed\` \| Game postponed \|
\| \`Delayed\` \| Game delayed \|
\| \`Canceled\` \| Game canceled \|
\| \`Forfeit\` \| Game forfeited \|

\### Soccer

\| Status \| Description \|
\| \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- \| \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- \|
\| \`Scheduled\` \| Game not yet started \|
\| \`InProgress\` \| Game currently playing \|
\| \`Break\` \| Halftime or other break \|
\| \`Suspended\` \| Game suspended \|
\| \`PenaltyShootout\` \| Penalty shootout in progress \|
\| \`Final\` \| Game completed \|
\| \`Awarded\` \| Result awarded due to ruling/forfeit \|
\| \`Postponed\` \| Game postponed \|
\| \`Canceled\` \| Game canceled \|

\### Esports

\| Status \| Description \|
\| \-\-\-\-\-\-\-\-\-\-\-\-\- \| \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- \|
\| \`not\_started\` \| Match not yet started \|
\| \`running\` \| Match currently playing \|
\| \`finished\` \| Match completed \|
\| \`postponed\` \| Match postponed \|
\| \`canceled\` \| Match canceled \|

\### Tennis

\| Status \| Description \|
\| \-\-\-\-\-\-\-\-\-\-\-\- \| \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- \|
\| \`scheduled\` \| Match not yet started \|
\| \`inprogress\` \| Match currently playing \|
\| \`suspended\` \| Match suspended \|
\| \`finished\` \| Match completed \|
\| \`postponed\` \| Match postponed \|
\| \`cancelled\` \| Match canceled \|

\# User Channel
Source: https://docs.polymarket.com/market-data/websocket/user-channel

Authenticated order and trade updates

Authenticated channel for updates related to your orders and trades, filtered by API key.

\## Endpoint

\`\`\`
wss://ws-subscriptions-clob.polymarket.com/ws/user
\`\`\`

\## Authentication

Include API credentials in your subscription message:

\`\`\`json theme={null}
{
 "auth": {
 "apiKey": "your-api-key",
 "secret": "your-api-secret",
 "passphrase": "your-passphrase"
 },
 "markets": \["0x1234...condition\_id"\],
 "type": "user"
}
\`\`\`

 Never expose your API credentials in client-side code. Use the user channel
 only from server environments.

\## Message Types

Each message includes a \`type\` field identifying the event.

\### trade

Emitted when:

\\* A market order is matched (\`MATCHED\`)
\\* A limit order for the user is included in a trade (\`MATCHED\`)
\\* Subsequent status changes for the trade (\`MINED\`, \`CONFIRMED\`, \`RETRYING\`, \`FAILED\`)

\`\`\`json theme={null}
{
 "asset\_id": "52114319501245915516055106046884209969926127482827954674443846427813813222426",
 "event\_type": "trade",
 "id": "28c4d2eb-bbea-40e7-a9f0-b2fdb56b2c2e",
 "last\_update": "1672290701",
 "maker\_orders": \[\
 {\
 "asset\_id": "52114319501245915516055106046884209969926127482827954674443846427813813222426",\
 "matched\_amount": "10",\
 "order\_id": "0xff354cd7ca7539dfa9c28d90943ab5779a4eac34b9b37a757d7b32bdfb11790b",\
 "outcome": "YES",\
 "owner": "9180014b-33c8-9240-a14b-bdca11c0a465",\
 "price": "0.57"\
 }\
 \],
 "market": "0xbd31dc8a20211944f6b70f31557f1001557b59905b7738480ca09bd4532f84af",
 "matchtime": "1672290701",
 "outcome": "YES",
 "owner": "9180014b-33c8-9240-a14b-bdca11c0a465",
 "price": "0.57",
 "side": "BUY",
 "size": "10",
 "status": "MATCHED",
 "taker\_order\_id": "0x06bc63e346ed4ceddce9efd6b3af37c8f8f440c92fe7da6b2d0f9e4ccbc50c42",
 "timestamp": "1672290701",
 "trade\_owner": "9180014b-33c8-9240-a14b-bdca11c0a465",
 "type": "TRADE"
}
\`\`\`

\#### Trade Statuses

\`\`\`
MATCHED → MINED → CONFIRMED
 ↓ ↑
RETRYING ───┘
 ↓
 FAILED
\`\`\`

\| Status \| Terminal \| Description \|
\| \-\-\-\-\-\-\-\-\-\-\- \| \-\-\-\-\-\-\-\- \| \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- \|
\| \`MATCHED\` \| No \| Trade has been matched and sent to the executor service by the operator \|
\| \`MINED\` \| No \| Trade observed to be mined into the chain, no finality threshold established \|
\| \`CONFIRMED\` \| Yes \| Trade has achieved strong probabilistic finality and was successful \|
\| \`RETRYING\` \| No \| Trade transaction has failed (revert or reorg) and is being retried/resubmitted by the operator \|
\| \`FAILED\` \| Yes \| Trade has failed and is not being retried \|

\### order

Emitted when:

\\* An order is placed (\`PLACEMENT\`)
\\* An order is updated — some of it is matched (\`UPDATE\`)
\\* An order is cancelled (\`CANCELLATION\`)

\`\`\`json theme={null}
{
 "asset\_id": "52114319501245915516055106046884209969926127482827954674443846427813813222426",
 "associate\_trades": null,
 "event\_type": "order",
 "id": "0xff354cd7ca7539dfa9c28d90943ab5779a4eac34b9b37a757d7b32bdfb11790b",
 "market": "0xbd31dc8a20211944f6b70f31557f1001557b59905b7738480ca09bd4532f84af",
 "order\_owner": "9180014b-33c8-9240-a14b-bdca11c0a465",
 "original\_size": "10",
 "outcome": "YES",
 "owner": "9180014b-33c8-9240-a14b-bdca11c0a465",
 "price": "0.57",
 "side": "SELL",
 "size\_matched": "0",
 "timestamp": "1672290687",
 "type": "PLACEMENT"
}
\`\`\`

\# Getting Started
Source: https://docs.polymarket.com/market-makers/getting-started

One-time setup for market making on Polymarket

Before you can start market making, you need to complete these one-time setup steps — deposit USDC.e to Polygon, deploy a wallet, approve tokens for trading, and generate API credentials.

 Market makers need USDC.e on Polygon to fund their trading operations.

 \| Method \| Best For \| Documentation \|
 \| \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- \| \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- \| \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- \|
 \| Bridge API \| Automated deposits from other chains \| \[Bridge Deposit\](/trading/bridge/deposit) \|
 \| Direct Polygon transfer \| Already have USDC.e on Polygon \| N/A \|
 \| Cross-chain bridge \| Large deposits from Ethereum \| \[Supported Assets\](/trading/bridge/supported-assets) \|

 ### Using the Bridge API

 \`\`\`typescript theme={null}
 // Get deposit addresses for your Polymarket wallet
 const deposit = await fetch("https://bridge.polymarket.com/deposit", {
 method: "POST",
 headers: { "Content-Type": "application/json" },
 body: JSON.stringify({
 address: "YOUR\_POLYMARKET\_WALLET\_ADDRESS",
 }),
 });

 // Returns deposit addresses for EVM, SVM, and BTC networks
 const addresses = await deposit.json();
 // Send USDC to the appropriate address for your source chain
 \`\`\`

 ### EOA

 Standard Ethereum wallet. You pay for all onchain transactions (approvals, splits, merges, trade execution).

 ### Safe Wallet

 Gnosis Safe-based wallet deployed via Polymarket's relayer. Benefits:

 \\* \*\*Gasless transactions\*\* — Polymarket pays gas fees for onchain operations
 \\* \*\*Contract wallet\*\* — Enables advanced features like batched transactions

 Deploy a Safe wallet using the Relayer Client:


 \`\`\`typescript TypeScript theme={null}
 import { RelayClient, RelayerTxType } from "@polymarket/builder-relayer-client";

 const client = new RelayClient(
 "https://relayer-v2.polymarket.com/",
 137, // Polygon mainnet
 signer,
 builderConfig,
 RelayerTxType.SAFE,
 );

 // Deploy the Safe wallet
 const response = await client.deploy();
 const result = await response.wait();
 console.log("Safe Address:", result?.proxyAddress);
 \`\`\`

 \`\`\`python Python theme={null}
 from py\_builder\_relayer\_client.client import RelayClient

 # client initialized with builder\_config

 # Deploy the Safe wallet
 response = client.deploy()
 result = response.wait()
 print("Safe Address:", result.get("proxyAddress"))
 \`\`\`

 See \[Gasless Transactions\](/trading/gasless) for full Relayer Client setup
 including local and remote signing configurations.

 Before trading, you must approve the exchange contracts to spend your tokens.

 ### Required Approvals

 \| Token \| Spender \| Purpose \|
 \| \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- \| \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- \| \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- \|
 \| USDC.e \| CTF Contract \| Split USDC.e into outcome tokens \|
 \| CTF (outcome tokens) \| CTF Exchange \| Trade outcome tokens \|
 \| CTF (outcome tokens) \| Neg Risk CTF Exchange \| Trade neg-risk market tokens \|

 ### Contract Addresses

 \`\`\`typescript theme={null}
 const ADDRESSES = {
 USDCe: "0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174",
 CTF: "0x4D97DCd97eC945f40cF65F87097ACe5EA0476045",
 CTF\_EXCHANGE: "0x4bFb41d5B3570DeFd03C39a9A4D8dE6Bd8B8982E",
 NEG\_RISK\_CTF\_EXCHANGE: "0xC5d563A36AE78145C45a50134d48A1215220f80a",
 NEG\_RISK\_ADAPTER: "0xd91E80cF2E7be2e162c6513ceD06f1dD0dA35296",
 };
 \`\`\`

 ### Approve via Relayer Client


 \`\`\`typescript TypeScript theme={null}
 import { ethers } from "ethers";
 import { Interface } from "ethers/lib/utils";

 const erc20Interface = new Interface(\[\
 "function approve(address spender, uint256 amount) returns (bool)",\
 \]);

 // Approve USDCe for CTF contract
 const approveTx = {
 to: ADDRESSES.USDCe,
 data: erc20Interface.encodeFunctionData("approve", \[\
 ADDRESSES.CTF,\
 ethers.constants.MaxUint256,\
 \]),
 value: "0",
 };

 const response = await client.execute(\[approveTx\], "Approve USDCe for CTF");
 await response.wait();
 \`\`\`

 \`\`\`python Python theme={null}
 from web3 import Web3

 USDC = "0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174"
 CTF = "0x4D97DCd97eC945f40cF65F87097ACe5EA0476045"
 MAX\_UINT256 = 2\*\*256 - 1

 approve\_tx = {
 "to": USDC,
 "data": Web3().eth.contract(
 address=USDC,
 abi=\[{\
 "name": "approve",\
 "type": "function",\
 "inputs": \[\
 {"name": "spender", "type": "address"},\
 {"name": "amount", "type": "uint256"}\
 \],\
 "outputs": \[{"type": "bool"}\]\
 }\]
 ).encode\_abi(abi\_element\_identifier="approve", args=\[CTF, MAX\_UINT256\]),
 "value": "0"
 }

 response = client.execute(\[approve\_tx\], "Approve USDC for CTF")
 response.wait()
 \`\`\`

 To place orders and access authenticated endpoints, you need L2 API credentials derived from your wallet.


 \`\`\`typescript TypeScript theme={null}
 import { ClobClient } from "@polymarket/clob-client";

 const client = new ClobClient("https://clob.polymarket.com", 137, signer);

 // Derive API credentials from your wallet
 const credentials = await client.createOrDeriveApiKey();
 console.log("API Key:", credentials.key);
 console.log("Secret:", credentials.secret);
 console.log("Passphrase:", credentials.passphrase);
 \`\`\`

 \`\`\`python Python theme={null}
 from py\_clob\_client.client import ClobClient
 import os

 private\_key = os.getenv("PRIVATE\_KEY")

 temp\_client = ClobClient("https://clob.polymarket.com", key=private\_key, chain\_id=137)
 credentials = temp\_client.create\_or\_derive\_api\_creds()
 \`\`\`

 \`\`\`rust Rust theme={null}
 use std::str::FromStr;
 use polymarket\_client\_sdk::POLYGON;
 use polymarket\_client\_sdk::auth::{LocalSigner, Signer};
 use polymarket\_client\_sdk::clob::{Client, Config};

 let private\_key = std::env::var("POLYMARKET\_PRIVATE\_KEY")?;
 let signer = LocalSigner::from\_str(&private\_key)?
 .with\_chain\_id(Some(POLYGON));

 // The Rust SDK derives credentials and initializes in one step
 let client = Client::new("https://clob.polymarket.com", Config::default())?
 .authentication\_builder(&signer)
 .authenticate()
 .await?;
 \`\`\`


 See \[Authentication\](/trading/overview#authentication) for full details on signature types and REST API headers.


\\*\\*\\*

\## Next Steps

 Post limit orders and manage quotes

 Connect to real-time market data


\# Inventory Management
Source: https://docs.polymarket.com/market-makers/inventory

Managing outcome token inventory for market making

Market makers need outcome tokens on both sides to quote a market. The three core inventory operations are \*\*splitting\*\* USDC.e into YES/NO token pairs, \*\*merging\*\* pairs back into USDC.e, and \*\*redeeming\*\* winning tokens after resolution — all executed gaslessly through the Relayer Client.

 For a full breakdown of how the Conditional Token Framework works, see \[CTF\
 Overview\](/trading/ctf/overview). This page focuses on the MM workflow using
 the Relayer Client.

\\*\\*\\*

\## Splitting USDC.e into Tokens

Split converts USDC.e into equal amounts of YES and NO tokens — creating the inventory you need to quote both sides of a market.

 \`\`\`typescript TypeScript theme={null}
 import { ethers } from "ethers";
 import { Interface } from "ethers/lib/utils";
 import { RelayClient, Transaction } from "@polymarket/builder-relayer-client";

 const CTF\_ADDRESS = "0x4D97DCd97eC945f40cF65F87097ACe5EA0476045";
 const USDCe\_ADDRESS = "0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174";

 const ctfInterface = new Interface(\[\
 "function splitPosition(address collateralToken, bytes32 parentCollectionId, bytes32 conditionId, uint\[\] partition, uint amount)",\
 \]);

 // Split $1000 USDCe into YES/NO tokens
 const amount = ethers.utils.parseUnits("1000", 6); // USDCe has 6 decimals

 const splitTx: Transaction = {
 to: CTF\_ADDRESS,
 data: ctfInterface.encodeFunctionData("splitPosition", \[\
 USDCe\_ADDRESS, // collateralToken\
 ethers.constants.HashZero, // parentCollectionId (always zero for Polymarket)\
 conditionId, // conditionId from market\
 \[1, 2\], // partition: \[YES, NO\]\
 amount,\
 \]),
 value: "0",
 };

 const response = await client.execute(\[splitTx\], "Split USDCe into tokens");
 const result = await response.wait();
 console.log("Split completed:", result?.transactionHash);
 \`\`\`

 \`\`\`python Python theme={null}
 from web3 import Web3

 CTF\_ADDRESS = "0x4D97DCd97eC945f40cF65F87097ACe5EA0476045"
 USDCe\_ADDRESS = "0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174"

 ctf\_abi = \[{\
 "name": "splitPosition",\
 "type": "function",\
 "inputs": \[\
 {"name": "collateralToken", "type": "address"},\
 {"name": "parentCollectionId", "type": "bytes32"},\
 {"name": "conditionId", "type": "bytes32"},\
 {"name": "partition", "type": "uint256\[\]"},\
 {"name": "amount", "type": "uint256"}\
 \],\
 "outputs": \[\]\
 }\]

 # Split $1000 USDCe into YES/NO tokens
 amount = 1000 \* 10\*\*6 # USDCe has 6 decimals

 split\_tx = {
 "to": CTF\_ADDRESS,
 "data": Web3().eth.contract(
 address=CTF\_ADDRESS, abi=ctf\_abi
 ).encode\_abi(
 abi\_element\_identifier="splitPosition",
 args=\[\
 USDCe\_ADDRESS,\
 bytes(32), # parentCollectionId (always zero)\
 condition\_id, # conditionId from market\
 \[1, 2\], # partition: \[YES, NO\]\
 amount,\
 \]
 ),
 "value": "0"
 }

 response = client.execute(\[split\_tx\], "Split USDCe into tokens")
 response.wait()
 \`\`\`

 \`\`\`rust Rust theme={null}
 use polymarket\_client\_sdk::ctf::Client as CtfClient;
 use polymarket\_client\_sdk::ctf::types::SplitPositionRequest;
 use polymarket\_client\_sdk::types::{U256, address};

 let ctf\_client = CtfClient::new(provider, 137)?;

 // Split $1000 USDCe into YES/NO tokens
 let request = SplitPositionRequest::builder()
 .collateral\_token(address!("0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174"))
 .condition\_id(condition\_id)
 .partition(vec!\[U256::from(1), U256::from(2)\])
 .amount(U256::from(1000\_000\_000u64)) // 1000 USDCe (6 decimals)
 .build();
 let result = ctf\_client.split\_position(&request).await?;
 println!("Split tx: {:?}", result.transaction\_hash);
 \`\`\`

After splitting 1000 USDC.e, you receive 1000 YES tokens and 1000 NO tokens. Your USDC.e balance decreases by 1000.

\\*\\*\\*

\## Merging Tokens to USDC.e

Merge converts equal amounts of YES and NO tokens back into USDC.e — useful for reducing exposure, exiting a market, or freeing up capital.

 \`\`\`typescript TypeScript theme={null}
 const ctfInterface = new Interface(\[\
 "function mergePositions(address collateralToken, bytes32 parentCollectionId, bytes32 conditionId, uint\[\] partition, uint amount)",\
 \]);

 // Merge 500 YES + 500 NO back to 500 USDCe
 const amount = ethers.utils.parseUnits("500", 6);

 const mergeTx: Transaction = {
 to: CTF\_ADDRESS,
 data: ctfInterface.encodeFunctionData("mergePositions", \[\
 USDCe\_ADDRESS,\
 ethers.constants.HashZero,\
 conditionId,\
 \[1, 2\],\
 amount,\
 \]),
 value: "0",
 };

 const response = await client.execute(\[mergeTx\], "Merge tokens to USDCe");
 await response.wait();
 \`\`\`

 \`\`\`python Python theme={null}
 merge\_abi = \[{\
 "name": "mergePositions",\
 "type": "function",\
 "inputs": \[\
 {"name": "collateralToken", "type": "address"},\
 {"name": "parentCollectionId", "type": "bytes32"},\
 {"name": "conditionId", "type": "bytes32"},\
 {"name": "partition", "type": "uint256\[\]"},\
 {"name": "amount", "type": "uint256"}\
 \],\
 "outputs": \[\]\
 }\]

 # Merge 500 YES + 500 NO back to 500 USDCe
 amount = 500 \* 10\*\*6

 merge\_tx = {
 "to": CTF\_ADDRESS,
 "data": Web3().eth.contract(
 address=CTF\_ADDRESS, abi=merge\_abi
 ).encode\_abi(
 abi\_element\_identifier="mergePositions",
 args=\[USDCe\_ADDRESS, bytes(32), condition\_id, \[1, 2\], amount\]
 ),
 "value": "0"
 }

 response = client.execute(\[merge\_tx\], "Merge tokens to USDCe")
 response.wait()
 \`\`\`

 \`\`\`rust Rust theme={null}
 use polymarket\_client\_sdk::ctf::types::MergePositionsRequest;

 // Merge 500 YES + 500 NO back to 500 USDCe
 let request = MergePositionsRequest::builder()
 .collateral\_token(address!("0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174"))
 .condition\_id(condition\_id)
 .partition(vec!\[U256::from(1), U256::from(2)\])
 .amount(U256::from(500\_000\_000u64)) // 500 USDCe (6 decimals)
 .build();
 let result = ctf\_client.merge\_positions(&request).await?;
 \`\`\`

After merging 500 of each, your YES and NO balances decrease by 500 and your USDC.e balance increases by 500.

\\*\\*\\*

\## Redeeming After Resolution

Once a market resolves, redeem winning tokens for USDC.e. Each winning token is worth $1 — losing tokens redeem for $0.

\### Check Resolution Status

 \`\`\`typescript TypeScript theme={null}
 const market = await clobClient.getMarket(conditionId);
 if (market.closed) {
 const winningToken = market.tokens.find((t) => t.winner);
 console.log("Winning outcome:", winningToken?.outcome);
 }
 \`\`\`

 \`\`\`python Python theme={null}
 market = clob\_client.get\_market(condition\_id)
 if market.get("closed"):
 winning = next(t for t in market\["tokens"\] if t.get("winner"))
 print("Winning outcome:", winning\["outcome"\])
 \`\`\`

 \`\`\`rust Rust theme={null}
 let market = clob\_client.market(condition\_id).await?;
 if market.closed {
 if let Some(winner) = market.tokens.iter().find(\|t\| t.winner) {
 println!("Winning outcome: {}", winner.outcome);
 }
 }
 \`\`\`

\### Redeem Winning Tokens

 \`\`\`typescript TypeScript theme={null}
 const ctfInterface = new Interface(\[\
 "function redeemPositions(address collateralToken, bytes32 parentCollectionId, bytes32 conditionId, uint\[\] indexSets)",\
 \]);

 const redeemTx: Transaction = {
 to: CTF\_ADDRESS,
 data: ctfInterface.encodeFunctionData("redeemPositions", \[\
 USDCe\_ADDRESS,\
 ethers.constants.HashZero,\
 conditionId,\
 \[1, 2\], // Redeem both YES and NO (only winners pay out)\
 \]),
 value: "0",
 };

 const response = await client.execute(\[redeemTx\], "Redeem winning tokens");
 await response.wait();
 \`\`\`

 \`\`\`python Python theme={null}
 redeem\_abi = \[{\
 "name": "redeemPositions",\
 "type": "function",\
 "inputs": \[\
 {"name": "collateralToken", "type": "address"},\
 {"name": "parentCollectionId", "type": "bytes32"},\
 {"name": "conditionId", "type": "bytes32"},\
 {"name": "indexSets", "type": "uint256\[\]"}\
 \],\
 "outputs": \[\]\
 }\]

 redeem\_tx = {
 "to": CTF\_ADDRESS,
 "data": Web3().eth.contract(
 address=CTF\_ADDRESS, abi=redeem\_abi
 ).encode\_abi(
 abi\_element\_identifier="redeemPositions",
 args=\[USDCe\_ADDRESS, bytes(32), condition\_id, \[1, 2\]\]
 ),
 "value": "0"
 }

 response = client.execute(\[redeem\_tx\], "Redeem winning tokens")
 response.wait()
 \`\`\`

 \`\`\`rust Rust theme={null}
 use polymarket\_client\_sdk::ctf::types::RedeemPositionsRequest;

 let request = RedeemPositionsRequest::builder()
 .collateral\_token(address!("0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174"))
 .condition\_id(condition\_id)
 .index\_sets(vec!\[U256::from(1), U256::from(2)\]) // Redeem both (only winners pay)
 .build();
 let result = ctf\_client.redeem\_positions(&request).await?;
 \`\`\`

\\*\\*\\*

\## Negative Risk Markets

Multi-outcome markets use the Neg Risk CTF Exchange. Split and merge work the same way, but use different contract addresses:

\`\`\`typescript theme={null}
const NEG\_RISK\_ADAPTER = "0xd91E80cF2E7be2e162c6513ceD06f1dD0dA35296";
const NEG\_RISK\_CTF\_EXCHANGE = "0xC5d563A36AE78145C45a50134d48A1215220f80a";
\`\`\`

See \[Negative Risk Markets\](/advanced/neg-risk) for details on how multi-outcome token mechanics differ.

\\*\\*\\*

\## Inventory Strategies

\### Before Quoting

1\. Check market metadata via the \[Gamma API\](/market-data/fetching-markets)
2\. Split sufficient USDC.e to cover your expected quoting size
3\. Set token approvals if not already done (see \[Getting Started\](/market-makers/getting-started))

\### During Trading

\\* \*\*Skew quotes\*\* when inventory becomes imbalanced on one side
\\* \*\*Merge excess tokens\*\* to free up capital for other markets
\\* \*\*Split more\*\* when inventory on either side runs low

\### After Resolution

1\. Cancel all open orders in the market
2\. Wait for resolution to complete
3\. Redeem winning tokens
4\. Merge any remaining YES/NO pairs

\\*\\*\\*

\## Batch Operations

Execute multiple inventory operations in a single relayer call for efficiency:

\`\`\`typescript theme={null}
const transactions: Transaction\[\] = \[\
 // Split on Market A\
 {\
 to: CTF\_ADDRESS,\
 data: ctfInterface.encodeFunctionData("splitPosition", \[\
 USDCe\_ADDRESS,\
 ethers.constants.HashZero,\
 conditionIdA,\
 \[1, 2\],\
 ethers.utils.parseUnits("1000", 6),\
 \]),\
 value: "0",\
 },\
 // Split on Market B\
 {\
 to: CTF\_ADDRESS,\
 data: ctfInterface.encodeFunctionData("splitPosition", \[\
 USDCe\_ADDRESS,\
 ethers.constants.HashZero,\
 conditionIdB,\
 \[1, 2\],\
 ethers.utils.parseUnits("1000", 6),\
 \]),\
 value: "0",\
 },\
\];

const response = await client.execute(transactions, "Batch inventory setup");
await response.wait();
\`\`\`

\\*\\*\\*

\## Next Steps

 How the Conditional Token Framework works under the hood

 Detailed split function parameters and prerequisites

 Detailed merge function parameters

 Relayer Client setup and configuration


\# Liquidity Rewards
Source: https://docs.polymarket.com/market-makers/liquidity-rewards

Earn rewards for providing liquidity on Polymarket

By posting resting limit orders, liquidity providers (makers) are automatically eligible for Polymarket's incentive program. Rewards are distributed directly to maker addresses daily at midnight UTC.

The program is designed to:

\\* Catalyze liquidity across all markets
\\* Encourage liquidity throughout a market's entire lifecycle
\\* Motivate passive, balanced quoting tight to a market's midpoint
\\* Encourage trading activity
\\* Discourage blatantly exploitative behaviors

 This program is heavily inspired by \[dYdX's liquidity provider\
 rewards\](https://www.dydx.foundation/blog/liquidity-provider-rewards). The
 methodology is essentially a copy of dYdX's approach with adjustments for
 binary contract markets — distinct books, no staking mechanic, a modified
 order utility-relative depth function, and reward amounts isolated per market.

\\*\\*\\*

\## Methodology

Liquidity providers are rewarded based on a formula that rewards participation in markets, boosts two-sided depth (single-sided orders still score), and tighter spread vs the size-cutoff-adjusted midpoint. Each market configures a max spread and min size cutoff within which orders are considered. The average of rewards earned is determined by the relative share of each participant's Qn in market m.

\### Variables

\| Variable \| Description \|
\| \-\-\-\-\-\-\-\-\-\-\-\-\-\- \| \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- \|
\| S \| Order position scoring function \|
\| v \| Max spread from midpoint (in cents) \|
\| s \| Spread from size-cutoff-adjusted midpoint \|
\| b \| In-game multiplier \|
\| m \| Market \|
\| m' \| Market complement (i.e. NO if m = YES) \|
\| n \| Trader index \|
\| u \| Sample index \|
\| c \| Scaling factor (currently 3.0 on all markets) \|
\| Qne \| Point total for book one for a sample \|
\| Qno \| Point total for book two for a sample \|
\| Spread% \| Distance from midpoint (bps or relative) for order n in market m \|
\| BidSize \| Share-denominated quantity of bid \|
\| AskSize \| Share-denominated quantity of ask \|

\\*\\*\\*

\## Equations

\### 1\. Order Scoring Function

Quadratic scoring rule for an order based on position between the adjusted midpoint and the minimum qualifying spread:

$S(v,s)= (\\frac{v-s}{v})^2 \\cdot b$

\### 2\. First Market Side Score

$Q\_{one}= S(v,Spread\_{m\_1}) \\cdot BidSize\_{m\_1} + S(v,Spread\_{m\_2}) \\cdot BidSize\_{m\_2} + \\dots $
$ \+ S(v, Spread\_{m^\\prime\_1}) \\cdot AskSize\_{m^\\prime\_1} + S(v, Spread\_{m^\\prime\_2}) \\cdot AskSize\_{m^\\prime\_2}$

\### 3\. Second Market Side Score

$Q\_{two}= S(v,Spread\_{m\_1}) \\cdot AskSize\_{m\_1} + S(v,Spread\_{m\_2}) \\cdot AskSize\_{m\_2} + \\dots $
$ \+ S(v, Spread\_{m^\\prime\_1}) \\cdot BidSize\_{m^\\prime\_1} + S(v, Spread\_{m^\\prime\_2}) \\cdot BidSize\_{m^\\prime\_2}$

\### 4\. Minimum Score

Boosts two-sided liquidity by taking the minimum of Qne and Qno, while still rewarding single-sided liquidity at a reduced rate (divided by c).

\*\*If midpoint is in range \\\[0.10, 0.90\]\*\* — single-sided liquidity can score:

$Q\_{\\min} = \\max(\\min({Q\_{one}, Q\_{two}}), \\max(Q\_{one}/c, Q\_{two}/c))$

\*\*If midpoint is in range \\\[0, 0.10) or (0.90, 1.0\]\*\* — liquidity must be double-sided to score:

$Q\_{\\min} = \\min({Q\_{one}, Q\_{two}})$

\### 5\. Normalized Score

Qmin of a market maker divided by the sum of all Qmin across market makers in a given sample:

$Q\_{normal} = \\frac{Q\_{min}}{\\sum\_{n=1}^{N}{(Q\_{min})\_n}}$

\### 6\. Epoch Score

Sum of all Qnormal for a trader across all samples in an epoch:

$Q\_{epoch} = \\sum\_{u=1}^{10,080}{(Q\_{normal})\_u}$

\### 7\. Final Score

Normalizes Qepoch by dividing by the sum of all market makers' Qepoch in a given epoch. This value is multiplied by the rewards available for the market to get a trader's reward:

$Q\_{final}=\\frac{Q\_{epoch}}{\\sum\_{n=1}^{N}{(Q\_{epoch})\_n}}$

\\*\\*\\*

\## Worked Example

Assume an adjusted market midpoint of 0.50 and a max spread config of 3 cents for both m and m'.

\### Step 2 - First Side Score

A trader has the following open orders:

\\* 100Q bid on m @ 0.49 (spread = 1 cent)
\\* 200Q bid on m @ 0.48 (spread = 2 cents)
\\* 100Q ask on m' @ 0.51 (spread = 1 cent)

$$
Q\_{ne} = \\left( \\frac{(3-1)}{3} \\right)^2 \\cdot 100 + \\left( \\frac{(3-2)}{3} \\right)^2 \\cdot 200 + \\left( \\frac{(3-1)}{3} \\right)^2 \\cdot 100
$$

Qne is calculated every minute using random sampling.

\### Step 3 - Second Side Score

The same trader also has:

\\* 100Q bid on m @ 0.485 (spread = 1.5 cents)
\\* 100Q bid on m' @ 0.48 (spread = 2 cents)
\\* 200Q ask on m' @ 0.505 (spread = 0.5 cents)

$$
Q\_{no} = \\left( \\frac{(3-1.5)}{3} \\right)^2 \\cdot 100 + \\left( \\frac{(3-2)}{3} \\right)^2 \\cdot 100 + \\left( \\frac{(3-.5)}{3} \\right)^2 \\cdot 200
$$

Qno is calculated every minute using random sampling.

\### Steps 4-7

4\. Take the minimum of Qne and Qno (with single-sided adjustment if midpoint is in \\\[0.10, 0.90\])
5\. Normalize against all other market makers in the sample
6\. Sum across all 10,080 samples in the epoch
7\. Normalize again to get final reward share

\\*\\*\\*

 The minimum reward payout is \*\*\\$1\*\*; amounts below this will not be paid.

 Both \`min\_incentive\_size\` and \`max\_incentive\_spread\` can be fetched alongside
 full market objects via the CLOB API and \[Markets\
 API\](/market-data/fetching-markets). Reward allocations for an epoch can also
 be fetched via the Markets API.

\## Next Steps

 Order entry and quoting best practices

 Earn USDC rebates on eligible crypto and sports markets


\# Maker Rebates Program
Source: https://docs.polymarket.com/market-makers/maker-rebates

Earn daily USDC rebates by providing liquidity on Polymarket

Polymarket has enabled taker fees on \*\*all crypto markets\*\*, \*\*NCAAB (college basketball)\*\*, and \*\*Serie A\*\* markets. These fees fund a \*\*Maker Rebates\*\* program that pays daily USDC rebates to liquidity providers.

\\*\\*\\*

\## Why Maker Rebates

Sports markets benefit from the same dynamics as crypto markets. When liquidity is deeper:

\\* Spreads tend to be tighter
\\* Price impact is lower
\\* Fills are more reliable
\\* Markets are more resilient during volatility

Maker Rebates incentivize \*\*consistent, competitive quoting\*\* so everyone gets a better trading experience.

\\*\\*\\*

\## How Maker Rebates Work

\\* \*\*Paid daily in USDC:\*\* Rebates are calculated and distributed every day.
\\* \*\*Performance-based:\*\* You earn based on the share of liquidity you provided that actually got taken.

\### Eligibility

Place orders that add liquidity to the book and get filled (i.e., your liquidity is taken by another trader).

\### Payment

Rebates are paid daily in USDC, directly to your wallet.

\\*\\*\\*

\## Funding

Maker Rebates are funded by taker fees collected in eligible markets. A percentage of these fees are redistributed to makers who keep the markets liquid. The rebate percentage differs by market type.

\| Market Type \| Period \| Maker Rebate \| Distribution Method \|
\| \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- \| \-\-\-\-\-\-\-\-\-\-\-\-\- \| \-\-\-\-\-\-\-\-\-\-\-\- \| \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- \|
\| 15-Min Crypto \| Jan 19, 2026+ \| 20% \| Fee-curve weighted \|
\| 5-Min Crypto \| Feb 12, 2026+ \| 20% \| Fee-curve weighted \|
\| Sports (NCAAB, Serie A) \| Feb 18, 2026+ \| 25% \| Fee-curve weighted \|
\| 1H, 4H, Daily, Weekly Crypto \| Mar 6, 2026+ \| 20% \| Fee-curve weighted \|

 Polymarket collects taker fees in eligible markets (all crypto markets, NCAAB,
 and Serie A). The rebate percentage is at the sole discretion of Polymarket
 and may change over time.

\\*\\*\\*

\## Fee-Curve Weighted Rebates

Rebates are distributed using the \*\*same formula as taker fees\*\*. This ensures makers are rewarded proportionally to the fee value their liquidity generates.

For each filled maker order:

\`\`\`text theme={null}
fee\_equivalent = C × p × feeRate × (p × (1 - p))^exponent
\`\`\`

Where \*\*C\*\* = number of shares traded and \*\*p\*\* = price of the shares. The fee parameters differ by market type:

\| Parameter \| Sports (NCAAB, Serie A) \| Crypto \|
\| \-\-\-\-\-\-\-\-\- \| \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- \| \-\-\-\-\-\- \|
\| Fee Rate \| 0.0175 \| 0.25 \|
\| Exponent \| 1 \| 2 \|

Your daily rebate:

\`\`\`text theme={null}
rebate = (your\_fee\_equivalent / total\_fee\_equivalent) \* rebate\_pool
\`\`\`

Totals are calculated per market, so you only compete with other makers in the same market.

\\*\\*\\*

\## Taker Fee Structure

Taker fees are calculated in USDC and vary based on the share price. However, fees are collected in shares on buy orders and USDC on sell orders. Fees are highest at 50% probability and lowest at the extremes (near 0% or 100%).