---
id: settle-before-export-crash
title: "Export Preset on a freshly Copy+mutated preset segfaulted onPC (Program Error Memory) — same crash family as gpdf-console-killer; settle with a SaveShow before exporting anything just written"
role: programmer
tags: [crash, mcp, v2.4, onpc, preset, lua]
when_to_load: "Before running Export Preset (or any Export) on an object that was Copied/Assigned/Set in the last few seconds — settle state with a SaveShow first, and verify fresh objects via Lua :Get() readback rather than Export, until this is fully trigger-isolated"
status: active
source: "findings/INBOX.md [0728cLD] 2026-07-28, crashlog 2026-07-28T14.02, onPC 2.4.2.2, live during the phaser template-set build; wraps/2026-07-28-song-t-full-build-and-resolver-laws.md"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**`Export Preset` on a freshly Copy+mutated preset segfaulted onPC** — `Program Error Memory`, a `_sigtramp` fault in the LUA thread with a recursive native stack — **the same crash family as `gpdf-console-killer`** (a C-side crash, not a catchable Lua error: `pcall` cannot help, and the round-trip just times out rather than returning an error).

**Sequence that crashed:** `Copy 21.51 → 21.53`, then `Assign Shape`, then `Set PlaybackDirection`, then `Export` **~30 seconds later**.

**Contrast:** the identical `Export` survived minutes earlier on a different object (21.52) that was freshly-Assigned but NOT copied. This isolates the trigger toward the **fresh-COPY step, or the `Set PlaybackDirection` write** specifically — **but this is one data point; do not over-conclude which exact step is the cause.**

**Mitigation adopted (both data points support it):**
- **Never `Export` an object in the same breath as writing it.** Verify freshly-written objects with **safe Lua `:Get()` reads only.**
- **`Export` only after a `SaveShow` has settled the state.** A second data point the same session (the phaser template-set import, see `tourshow-seq1510-build-record`) confirms: Export of freshly-imported presets is clean when it runs after a SaveShow.

**Recovery:** the crash reverted cleanly to a checkpoint (`v.25`) taken minutes before — the standing pre-write `SaveShow` checkpoint discipline (`saveshow-discipline-and-mcp-tier`) paid for itself in full; zero rework lost beyond the crashed step itself.

**Relation:** `gpdf-console-killer` for the sibling crash family (same signature, different triggering call — `GetPresetDataFast()` there vs `Export Preset` here); both are C-side crashes that an MCP round-trip only sees as a timeout (`segfault-manifests-as-mcp-timeout`). The CLI grammar that led into this crash (`Assign Shape <n> At Preset <pool>.<slot>.1` — the `.1` addresses the preset's `PhaserRecipe` child; the bare preset address without `.1` is a loud `Illegal object`) is recorded in `tourshow-seq1510-build-record`.

History: none — first (and so far only) occurrence, 2026-07-28; trigger not yet fully isolated, flagged for verification.
