---
id: send-lua-expression-payload-rule
title: "⛔ send_lua payloads must be a bare Lua EXPRESSION, not a statement — the server wraps every payload as pcall(function() return (<code>) end), so local/return payloads syntax-error before the round-trip file is ever written"
role: programmer
tags: [mcp, lua, send_lua, v2.4]
when_to_load: "Before writing ANY send_lua payload, and immediately if a send_lua call times out with 'no-roundtrip-file' while get_console_info reads the channel as healthy — check payload SHAPE (expression vs statement) before suspecting the wire"
status: active
source: "findings/INBOX.md [0729cLD] 2026-07-29, live 2.4.2.2, console-echo debug session (Dave read the console echo); wraps/2026-07-29-song-t-complete-fills-cutover-prework.md"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**⛔ ROOT CAUSE (the wire was NEVER down — Dave read the console echo, which is what cracked it):** the `send_lua` server wraps every incoming payload as `pcall(function() return (<code>) end)`. Any payload that starts with `local` or `return` assembles into `return (return ...)` — a Lua **syntax error** (`[1: unexpected symbol near 'return']`). The whole Lua line dies **before** the round-trip file is ever written, so the server only ever reports a **no-roundtrip timeout** — which looks exactly like a dead channel, a suspended session, or a crashed console, and is none of those.

## The rule

**Send bare EXPRESSIONS**, e.g.:
```
ObjectList(...)[1]:Get(...)
tostring(...)
Cmd([[...]])
```

**Wrap multi-statement code as an IIFE** (immediately-invoked function expression) instead of a `local`/`return` block:
```
(function() <statements> return <val> end)()
```

## Wrapper mechanics (banked)

The wrapper writes `Library/alchemease_rt.txt` via a `.tmp` file + `os.rename`, nonced per call. This is why the failure is silent from the caller's side — nothing ever gets far enough to write the file, so there's no partial/corrupt artifact to inspect, just an absence.

## What this explains

**All 6 of this session's send_lua failures**, and — just as importantly — **why 2026-07-17 and 2026-07-28 reads and writes worked fine**: those payloads happened to already be expression-shaped. Nothing about the transport, the MA-Net session, or the OSC interface changed between then and now; the difference was always payload shape.

**Verified fixed live:** `tostring(BuildDetails().BigVersion)` → `2.4.2.2` @ 66ms.

**End-to-end re-verification, same session, once the rule was applied:**
- Tier-1 read: `2.4.2.2` @ 66ms.
- Tier-2 `confirm_gate` flow clean: `SaveShow /Enumerate` v.37→v.38 **verified on disk** (113,287,266 B, 18:22).
- `Export Sequence` 1501 `'gb_fill1'` + 1502 `'gb_fill2'` OK @ 65-67ms, both landed in `datapools/sequences` and copied to the repo (`showfiles/festival_recon/sequences/`, 617,262 / 487,527 B).
- `/Enumerate` trailing-version increment now **9-for-9**.

## What this was mistaken for, and why that mattered

Before the root cause was found, the same symptom (probe reads healthy, send_lua times out with no round-trip file) was chased down two other paths in the same session: (1) a suspicion that the reachability **probe itself** was giving a false positive — that strand is real and stands independently, see the refinement in `out-ok-is-send-not-reachability`; and (2) after Dave's IP/network reset, a live suspicion that the **MA-Net Session** had dropped or the **OSC line Interface** had gone orphaned by the network change — investigated and **not** the cause this time. **Refined diagnostic order:** probe-true + send_lua-timeout ⇒ check payload **SHAPE** first (this concept), then session/interface health (`out-ok-is-send-not-reachability`), then crash-as-timeout (`segfault-manifests-as-mcp-timeout`).

**Companion process lesson:** the expression-only rule was already stated in the `send_lua` tool's own description the whole time — see `reread-tool-description-on-misbehavior`.

**Relation:** `out-ok-is-send-not-reachability` (the probe-trustworthiness question, one layer removed from this payload-shape question) · `saveshow-discipline-and-mcp-tier` (the companion quoting rule for dotted show names inside `send_lua`) · `reread-tool-description-on-misbehavior` (the process lesson this saga produced).

History: none — root cause found, fixed, and verified end-to-end in one session, 2026-07-29.
