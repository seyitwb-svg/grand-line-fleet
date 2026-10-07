# Grand Line — 20 self-hosted micro-SaaS tools

![apps](https://img.shields.io/badge/apps-21-orange)
![runtime](https://img.shields.io/badge/runtime-python%2Bsqlite-green)
![deploy](https://img.shields.io/badge/deploy-docker-blue)
![payment](https://img.shields.io/badge/payment-BTC%2BUSDT-f7931a)

Own the code. Skip the rent. One flat price — paid in BTC or USDT,
delivered automatically on-chain. No Stripe, no account, no KYC.

Every tool below is **live right now** — click through and inspect the
real product before buying anything. The whole fleet runs on ~1 GB RAM
on a 4 €/month VPS.

**Read:** [the fleet story](https://telegra.ph/21-self-hosted-micro-SaaS-tools-on-one-4-EUR-VPS-and-how-the-crypto-checkout-works-10-07) · [how the KYC-free checkout works](https://telegra.ph/Accept-bitcoin-for-downloads-without-KYC--the-200-line-checkout-10-07) · [why it beats a boilerplate](https://telegra.ph/The-99-boilerplate-that-is-not-Nextjs--21-shipping-PythonSQLite-apps-10-07) · nostr: npub1qjewu586lvgsswge2jmycj4ncjm4k7hfkfyc3hmh6eka4eyvjdwsehgw5l

## The 20 apps

| App | Replaces | Hosted price | 
|---|---|---|
| Heard | Canny ($79/mo) | feedback board + changelog |
| FormDock | Formspree | form backend + webhooks |
| StatusPage | Statuspage.io | hosted status + auto-incidents |
| QueueMe | waiting-room lists | waitlist + referral tracking |
| DockRoom | client portals | project portal + file exchange |
| JobDesk | Jobber-lite | job tracking + invoices |
| QuoteDeck | quote tools | proposals + client-opened tracking |
| HourJar | Harvest | time tracking → invoice → paid |
| BookMe | Calendly | booking + blocked days |
| CronWatch | Healthchecks.io | cron monitoring + alerts |
| Metrik | Plausible | privacy-first analytics + goals |
| NewsDock | changelog feeds | posts + RSS + API publishing |
| MarkDock | docs hosting | Markdown → hosted docs + search |
| ProofDock | Senja | testimonials + wall of love |
| TalkDock | Disqus/Hyvor | moderated comment embeds |
| SecretDock | OneTimeSecret | burn-after-reading secrets |
| OGDock | DynaPictures | OG images as a URL API |
| QRDock | QR-code services | dynamic QR + scan stats |
| BioDock | Linktree | link-in-bio + click stats |
| SurveyDock | Typeform | surveys + shared results |

Python + FastAPI + SQLite + Docker, ~50 MB RAM each. Shared `grkit`
auth/db layer vendored per app — every app deploys standalone in minutes.

## Free sample

**QRDock is MIT-licensed** — inspect the exact code quality you're buying:
[github.com/seyitwb-svg/qrdock](https://github.com/seyitwb-svg/qrdock)

## Buy the source

**$99 one-time — all 21 apps, complete source, deploy docs.**

Payment is a plain on-chain transfer (BTC or USDT-TRC20). Your download
unlocks automatically after 1 network confirmation. You own the code —
modify it, self-host it, never think about subscriptions again.

🛒 **Shop:** https://seyitwb-svg.github.io/grand-line-fleet/go/?app=goldshop&p=/shop (permanent redirect — always resolves to the current live shop)
📊 **Live status:** https://seyitwb-svg.github.io/grand-line-fleet/go/?app=statuspage&p=/s/st-907738732f
🤖 **x402 for agents:** https://seyitwb-svg.github.io/grand-line-fleet/go/?app=goldshop&p=/.well-known/x402

## Why crypto-only

Self-hosters shouldn't need to hand identity documents to a payment
processor to buy code. A wallet transfer is the whole checkout: exact
amount identifies your order, confirmation unlocks the file, done.

## License

Run, modify, self-host forever. Don't resell the source itself.
