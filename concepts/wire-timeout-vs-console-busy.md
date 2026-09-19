---
id: wire-timeout-vs-console-busy
title: "A timeout right after a write batch indicts CONSOLE BUSY-WORK before it indicts the wire — recipe reassignments trigger recook storms; prove liveness with a tiny probe before diagnosing the transport"
role: programmer
tags: [ma3, mcp, diagnosis, recipes, v2.4, tourshow]
when_to_load: "When an MCP call times out and the previous call was a batch of recipe/selection writes — check for a recook storm before touching the transport, the session or the network"
status: active
verified: grandMA3 onPC 2.4.2.2 (Mac), EU tour leg 2026-08
source: "findings/INBOX.md [0826-2cLD] and [0828-xcLD] 2026-08-26→28 — observed during the recipe-repoint sweeps"
supersedes: []
superseded_by: null
---

**Observation:** timeouts clustered immediately after batches of recipe-line reassignments. Reassigning a recipe line's `Selection`/`MAtricks`/`Preset` invalidates the cooked output, and the console **re-cooks** — across every cue that line feeds. On a show-sized file that is real work, and it can absorb the console for long enough to time a round-trip out.

**Diagnostic order for a post-write-batch timeout:**

1. **Tiny probe first.** A one-token read (`tostring(BuildDetails().BigVersion)`) proves liveness in ~66 ms. If it answers, the wire is fine and the console was busy — wait and continue.
2. Only if the probe *also* fails: **`get_console_info`** for a PID change (`segfault-manifests-as-mcp-timeout` — a timeout can be a crash).
3. Then payload **shape** (`send-lua-expression-payload-rule`) and payload **scale** (`split-and-guard-per-sequence-walk-law`).
4. Session/interface health last (`out-ok-is-send-not-reachability`).

**Corollary for build planning:** recook cost is why heavy repoint work should be **paced in batches with probes between them**, and why the recipes are expected to re-cook at the next playback anyway — the first previz run-through covers the visual settle after a repoint sweep.

**Relation:** `segfault-manifests-as-mcp-timeout` · `send-lua-expression-payload-rule` · `split-and-guard-per-sequence-walk-law` · `recipe-output-precedence-and-cooking-doctrine` (what "cooking" means) · `settle-before-export-crash`.

History: none — pattern recognised across the {FESTIVAL} → {FESTIVAL} surgery runs, 2026-08.
