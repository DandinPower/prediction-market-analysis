---
url: "https://docs.polymarket.com/api-reference/rewards/get-total-earnings-for-user-by-date.md"
title: undefined
---

\> ## Documentation Index
\> Fetch the complete documentation index at: https://docs.polymarket.com/llms.txt
\> Use this file to discover all available pages before exploring further.

\# Get total earnings for user by date

\> Returns the summed total rewards earnings for a user on a provided day,
grouped by asset address.

Requires CLOB L2 Auth headers.

\## OpenAPI

\`\`\`\`yaml /api-spec/clob-openapi.yaml get /rewards/user/total
openapi: 3.1.0
info:
 title: Polymarket CLOB API
 description: Polymarket CLOB API Reference
 license:
 name: MIT
 identifier: MIT
 version: 1.0.0
servers:
 \- url: https://clob.polymarket.com
 description: Production CLOB API
 \- url: https://clob-staging.polymarket.com
 description: Staging CLOB API
security: \[\]
tags:
 \- name: Trade
 description: Trade endpoints
 \- name: Markets
 description: Market data endpoints
 \- name: Account
 description: Account and authentication endpoints
 \- name: Notifications
 description: User notification endpoints
 \- name: Rewards
 description: Rewards and earnings endpoints
 \- name: Rebates
 description: Maker rebate endpoints
paths:
 /rewards/user/total:
 get:
 tags:
 \- Rewards
 summary: Get total earnings for user by date
 description: \|
 Returns the summed total rewards earnings for a user on a provided day,
 grouped by asset address.

 Requires CLOB L2 Auth headers.
 operationId: getTotalEarningsForUserForDay
 parameters:
 \- name: date
 in: query
 description: Date in YYYY-MM-DD format
 required: true
 schema:
 type: string
 format: date
 example: '2024-03-26'
 \- name: signature\_type
 in: query
 description: \|
 Signature type for address derivation (required for API KEY auth):
 \- 0: EOA
 \- 1: POLY\_PROXY
 \- 2: POLY\_GNOSIS\_SAFE
 required: false
 schema:
 type: integer
 enum:
 \- 0
 \- 1
 \- 2
 \- name: maker\_address
 in: query
 description: Maker address to query earnings for
 required: false
 schema:
 type: string
 example: '0xFeA4cB3dD4ca7CefD3368653B7D6FF9BcDFca604'
 \- name: sponsored
 in: query
 description: If true, aggregates both native and sponsored earnings
 required: false
 schema:
 type: boolean
 default: false
 responses:
 '200':
 description: Successfully retrieved total user earnings
 content:
 application/json:
 schema:
 type: array
 items:
 $ref: '#/components/schemas/TotalUserEarning'
 example:
 \- date: '2024-04-09T00:00:00Z'
 asset\_address: '0x9c4E1703476E875070EE25b56A58B008CFb8FA78'
 maker\_address: '0xD527CCdBEB6478488c848465F9947bDA3C2e6994'
 earnings: 1.59984
 asset\_rate: 0.999357
 \- date: '2024-04-09T00:00:00Z'
 asset\_address: '0x69308FB512518e39F9b16112fA8d994F4e2Bf8bB'
 maker\_address: '0xD527CCdBEB6478488c848465F9947bDA3C2e6994'
 earnings: 8.187219
 asset\_rate: 3.51
 '400':
 description: Bad request - Invalid parameters
 content:
 application/json:
 schema:
 $ref: '#/components/schemas/ErrorResponse'
 examples:
 invalid\_date:
 summary: Invalid date format
 value:
 error: 'Invalid date (format: YYYY-MM-DD)'
 invalid\_signature\_type:
 summary: Invalid signature type
 value:
 error: Invalid signature\_type
 invalid\_maker\_address:
 summary: Invalid maker address
 value:
 error: Invalid maker\_address
 '401':
 description: Unauthorized - Invalid API key or authentication failed
 content:
 application/json:
 schema:
 $ref: '#/components/schemas/ErrorResponse'
 example:
 error: Invalid API key
 '500':
 description: Internal server error
 content:
 application/json:
 schema:
 $ref: '#/components/schemas/ErrorResponse'
 example:
 error: Internal server error
 security:
 \- polyApiKey: \[\]
 polyAddress: \[\]
 polySignature: \[\]
 polyPassphrase: \[\]
 polyTimestamp: \[\]
components:
 schemas:
 TotalUserEarning:
 type: object
 description: Total user earnings for a given day grouped by asset
 properties:
 date:
 type: string
 format: date-time
 description: Date of the earnings
 asset\_address:
 type: string
 description: Address of the reward asset
 maker\_address:
 type: string
 description: Address of the maker
 earnings:
 type: number
 format: double
 description: Total amount of earnings in the asset
 asset\_rate:
 type: number
 format: double
 description: Exchange rate of the asset
 required:
 \- date
 \- asset\_address
 \- maker\_address
 \- earnings
 \- asset\_rate
 ErrorResponse:
 type: object
 required:
 \- error
 properties:
 error:
 type: string
 description: Error message
 securitySchemes:
 polyApiKey:
 type: apiKey
 in: header
 name: POLY\_API\_KEY
 description: Your API key
 polyAddress:
 type: apiKey
 in: header
 name: POLY\_ADDRESS
 description: Ethereum address associated with the API key
 polySignature:
 type: apiKey
 in: header
 name: POLY\_SIGNATURE
 description: HMAC signature of the request
 polyPassphrase:
 type: apiKey
 in: header
 name: POLY\_PASSPHRASE
 description: API key passphrase
 polyTimestamp:
 type: apiKey
 in: header
 name: POLY\_TIMESTAMP
 description: Unix timestamp of the request

\`\`\`\`

Built with \[Mintlify\](https://mintlify.com).