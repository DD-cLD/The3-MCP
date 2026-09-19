---
id: out-ok-is-send-not-reachability
title: "out_ok is a send-succeeded flag, not a reachability/liveness check — UDP send never raises"
role: programmer
tags: [mcp, osc]
when_to_load: "Before trusting gma3-mcp probe's out_ok as evidence that onPC is up and listening — it proves nothing about the far end; also before trusting get_console_info's lua_roundtrip_ok as proof that a DIFFERENT send_lua call will actually work"
status: active
source: "MEMORY §Paid-for lessons 2026-06-29 — out_ok semantics; refined findings/INBOX.md [0729cLD] 2026-07-29 — lua_roundtrip_ok false-positive layer"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

`gma3-mcp probe`'s `ping()` sets `out_ok = True` the instant `send_cmd()` returns without raising. `send_cmd` is a **UDP** datagram (`SimpleUDPClient.send_message`) to `127.0.0.1:8000`; UDP is connectionless, so the send never raises whether or not onPC is listening.

**Verified 2026-06-29:** onPC was fully closed (no process, nothing bound on UDP 8000) and `out_ok` still came back `true`.

Therefore **`out_ok` cannot distinguish** "onPC up but silent" from "onPC closed" — both yield `out_ok:true, echo_received:false`. This corrects any claim that "onPC closed → out_ok:false."

**For real reachability**, the queued probe rework must use the **Lua-file round-trip** (send `Lua "..."` that writes a sentinel JSON to a known path; poll-read it) — that genuinely requires onPC to execute, which a bare UDP send cannot fake. (Same underlying pattern as `osc-outbound-is-event-driven`'s Lua-file recommendation.)

## Refined 2026-07-29 — a Lua-roundtrip probe only proves ITS OWN payload round-tripped, not that a different send_lua call will

**Observed live:** `get_console_info.lua_roundtrip_ok` read **TRUE** (33-68ms RTT) across the same minutes that **FIVE separate `send_lua` calls all failed** with no-roundtrip-file — including a zero-quote, probe-identical-looking payload. `gma3_library` held no `alchemease_rt.txt` and no token files; the desk was clear and the console was alive. In the moment, this read as a new, higher-layer false-positive class ("probe-true does not mean send_lua-works"), the same lesson-shape as this concept's core lesson, one layer up — a healthy probe proves the probe's own action succeeded, not that a differently-shaped action will.

**RESOLVED, same session:** the actual cause of all six of that session's `send_lua` failures — including these — was a payload-SHAPE bug, not a probe/session/transport problem: `send_lua` requires a bare Lua EXPRESSION, and the failing calls were statement-shaped. See `send-lua-expression-payload-rule` for the full mechanism. **The standing caution above still generalizes** (a probe's own successful round-trip doesn't certify that a differently-shaped payload will succeed) even though this session's specific instances turned out to have a simpler explanation.

**Standing fallback if a future case is NOT explained by payload shape:** try a full Cmd+Q relaunch of Claude Desktop (the stale-mcp-process rule), then require one clean read before trusting the channel again; desk-typed CLI or computer-use are the fallback lanes in the meantime.

History: none as a correction-in-place — but this finding functionally corrects an unstated prior assumption that `out_ok` implied liveness; recorded as the definitive statement 2026-06-29. **Refined 2026-07-29:** added, then resolved in the same session, a second-layer observation (Lua-roundtrip probe reading healthy while real `send_lua` calls failed) — the standing caution generalizes, but this instance's actual cause was a payload-shape bug; see `send-lua-expression-payload-rule` and `reread-tool-description-on-misbehavior` for the process lesson it produced.
