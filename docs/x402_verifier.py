# x402_verifier.py — facilitator-free on-chain verifier for x402 (USDC on Base)
# MIT License — copy freely. Part of the Grand Line fleet:
# https://seyitwb-svg.github.io/grand-line-fleet/
#
# Verifies that a transaction hash transferred USDC on Base mainnet to your
# payTo address, using only public RPC endpoints. No facilitator, no API key.
#
# Design notes (what bit us in production):
#   * Exact-amount matching: issue every 402 with a unique jittered amount
#     (base price + randbelow(10_000)) bound to an order id, then require
#     `units == expected` — prevents cross-order tx reuse.
#   * Atomic claim: INSERT the tx hash into a PK'd table before serving;
#     IntegrityError = already redeemed. A check-then-insert pair races.
#   * eth_getLogs on the USDC contract is rate-limited to ~5 queries/day on
#     mainnet.base.org — parse the receipt's logs instead (free, unlimited).
#   * Receipts arrive while pending: `status` may be missing or "0x0" — only
#     accept "0x1". Optionally require confirmations via blockNumber vs
#     eth_blockNumber if your goods are worth more than a reorg costs.
#   * Set a User-Agent: several public RPCs 403 bare `Python-urllib`
#     (and occasionally other default library UAs) under load — a neutral
#     UA like `x402-verifier/1.0` stays unblocked. httpx/curl are fine.

import json
import urllib.request

USDC_BASE = "0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913"
NETWORK = "eip155:8453"
TRANSFER_TOPIC = ("0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628"
                  "f55a4df523b3ef")

RPCS = ["https://mainnet.base.org",
        "https://base-rpc.publicnode.com",
        "https://base.drpc.org",
        "https://1rpc.io/base",
        "https://base-mainnet.public.blastapi.io"]


def _rpc(method, params):
    body = json.dumps({"jsonrpc": "2.0", "id": 1,
                       "method": method, "params": params}).encode()
    last = None
    for rpc in RPCS:
        try:
            r = urllib.request.urlopen(urllib.request.Request(
                rpc, body, {"content-type": "application/json",
                            "user-agent": "x402-verifier/1.0"}), timeout=12)
            res = json.loads(r.read())
            if "result" in res:
                return res["result"]
            last = res.get("error")
        except Exception as e:
            last = e
    return None


def usdc_transfers(tx_hash):
    """Parse a receipt -> ({recipient_lc: total_units}, block, status_ok)."""
    tx_hash = tx_hash.lower()
    if not (tx_hash.startswith("0x") and len(tx_hash) == 66):
        return {}, 0, False
    rec = _rpc("eth_getTransactionReceipt", [tx_hash])
    if not isinstance(rec, dict):
        return {}, 0, False
    ok = rec.get("status") == "0x1"
    block = int(rec.get("blockNumber") or "0x0", 16)
    out = {}
    for lg in rec.get("logs") or []:
        if (lg.get("address") or "").lower() != USDC_BASE.lower():
            continue
        t = lg.get("topics") or []
        if len(t) < 3 or t[0].lower() != TRANSFER_TOPIC:
            continue
        to = "0x" + t[2][-40:].lower()
        try:
            out[to] = out.get(to, 0) + int(lg.get("data") or "0x0", 16)
        except (TypeError, ValueError):
            pass
    return out, block, ok


def paid_at_least(tx_hash, pay_to, min_units):
    """True if tx_hash paid >= min_units USDC atomic units to pay_to."""
    transfers, _block, ok = usdc_transfers(tx_hash)
    return bool(ok and transfers.get(pay_to.lower(), 0) >= min_units)


if __name__ == "__main__":
    import sys
    txh = sys.argv[1] if len(sys.argv) > 1 else ""
    print(json.dumps(usdc_transfers(txh), indent=2))
