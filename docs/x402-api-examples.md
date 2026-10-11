# x402 API — curl examples (working, live)

Store origin (stable): `https://grandline-fleet.shares.zrok.io`
Discovery: `GET /.well-known/x402` · `GET /openapi.json` · x402scan listing (registered).

Payment model: facilitator-free `exact` scheme, USDC on Base (`eip155:8453`).
Each `402` response carries a **unique per-order amount** (base + jitter)
in `accepts[0].amount` and a unique `oid` in `resource.url`. Pay exactly
`amount` to `payTo`, then retry the oid'd URL with `X-PAYMENT` =
`{"x402Version":2,"scheme":"exact","network":"eip155:8453","payload":{"txHash":"0x…"}}`
(a bare `0x…` hash works too).

## Free demo (no payment)

```bash
# fetch+parse any public URL — 10 free calls/day
curl 'https://grandline-fleet.shares.zrok.io/x402/free/pagescan?url=https://example.com'
```

## Pay-per-call endpoints (≤ $0.02)

```bash
# 1) challenge: returns 402 + Payment-Required header + JSON body
curl -i 'https://grandline-fleet.shares.zrok.io/x402/pagescan?url=https://example.com'

# 2) send exactly `accepts[0].amount` USDC (6 decimals) on Base to `payTo`

# 3) retry the `resource.url` from the 402 body with your tx hash
curl '<resource.url-from-402-body>' -H 'X-PAYMENT: 0x<txhash>'
```

| Endpoint | What | Price |
|---|---|---|
| `GET /x402/verify?tx=&to=&min=&chain=base\|bitcoin\|tron` | multi-chain settlement attestation | $0.002 |
| `GET /x402/pagescan?url=` | fetch+parse URL → title/meta/links/text | $0.005 |
| `GET /x402/tokeninfo?address=` | ERC-20 info on Base | $0.005 |
| `GET /x402/hn?q=` | Hacker News search JSON | $0.005 |
| `GET /x402/enrich?kind=rdap\|dns\|geoip&target=` | domain/IP enrichment | $0.005 |
| `GET /x402/proxy/ogpng` | OG/social image render | $0.005 |
| `GET /x402/proxy/qrpng` | QR code PNG | $0.005 |
| `GET /x402/proxy/mdrender` | Markdown → HTML | $0.002 |
| `GET /x402/proxy/burnlink` | burn-after-read secret link | $0.01 |
| `GET /x402/proxy/webhookinbox` | disposable webhook inbox | $0.01 |
| `GET /x402/proxy/livepoll` | live poll + vote link | $0.02 |
| `GET /x402/proxy/keylicense` | signed license key + payment receipt (agent commerce) | $0.01 |

## Buy source packages

```bash
# end-to-end test purchase for ~1 cent
curl -i 'https://grandline-fleet.shares.zrok.io/x402/hello'
# → 402 with unique amount + oid; pay; retry:
curl 'https://grandline-fleet.shares.zrok.io/x402/order/<oid>' -H 'X-PAYMENT: 0x<txhash>'
# → {status:"paid", download:"https://…/d/<token>"}
```

| Item | Contents | Price |
|---|---|---|
| `hello` | MIT x402 verifier + worked example — proves the rail | $0.01 |
| `x402stack` | SecretDock + OGDock + QRDock sources (3 agent-payable apps) | $9 |
| `app:<slug>` | single app source (e.g. `app:heard`, `app:cronwatch`) | $29 |
| `app:goldshop` | this checkout itself (BTC+USDT+x402 paywall, auto-delivery) | $49 |
| `bundle` | all 21 apps | $99 |
| `fleet` | everything incl. deploy pipeline | $299 |

Notes: amounts are in USDC atomic units (1e6 per USD). Orders bind via
exact-amount match — wrong amount/address cannot auto-credit. Paid URLs
are idempotent; re-serving with the same tx returns the result again.
