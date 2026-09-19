---
id: many-lines-ride-macros-not-lua
title: "Dave's method law: 'easier to execute by macro or script than lua lua lua' — many-line desk batches ship as re-runnable MACRO artifacts, and recipe fields ARE assignable by macro line (the Assign lane)"
role: programmer
tags: [ma3, macro, doctrine, method, v2.4, tourshow]
when_to_load: "When a batch of desk writes is about to be issued as a chain of individual Lua calls — if the batch will ever repeat, it should be born as a macro artifact instead"
status: active
verified: grandMA3 onPC 2.4.2.2 (Mac), EU tour leg 2026-08
source: "findings/INBOX.md [0826-4cLD] 2026-08-27 — Dave's ruling, verbatim fragment quoted below"
supersedes: []
superseded_by: null
---

**Dave, verbatim:** *"easier to execute by macro or script than lua lua lua."*

**The law:** a many-line desk batch is delivered as a **desk-native, re-runnable artifact** — a macro (or a script that writes one) — not as a chain of individual bridge calls. Two reasons, both proven on tour:

1. **Dave can re-fire it himself**, on any file, without cLD or a wire. `cLD MASTERS TX` re-ran the entire masters treatment on a fresh file lineage from one press.
2. **A chain of calls leaves nothing behind.** The batch that ran as Lua exists only in a session log; the batch that ran as a macro exists in the pool and in `gma3_library/datapools/macros/` as an XML.

**Corollary — the Assign lane (Dave's note, same ruling):** **recipe fields (`Preset`, and the rest) ARE assignable by macro line.** This matters because recipe *line creation* is not wire-reachable at all (`recipe-line-creation-not-wire-reachable`) — the macro lane reaches further into the recipe layer than raw Lua does, which is a second reason to prefer it.

**Where the boundary sits.** Bulk *analysis* still goes export + Mac-side python (`export-plus-python-bulk-lane`) — the macro lane is for **writes that repeat**, not for questions. A useful split: **questions → export+python · repeated writes → macro · one-off targeted writes → per-sequence Lua calls.**

**Macro artifacts must report counts, not success** (`macro-lua-label-race-needs-wait`), and must be import-verified after landing (`import-file-argument-must-be-quoted`, `plugin-import-verify-name-match`).

**Relation:** `macro-ization-doctrine` · `venue-adapt-macro-pattern` (the kit this law produced) · `recipe-line-creation-not-wire-reachable` · `export-plus-python-bulk-lane` · `macro-library-file-lane-and-bulk-authoring-workaround`.

History: none — ruled 2026-08-27 and applied for the remainder of the leg.
