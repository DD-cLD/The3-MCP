---
id: gs-multifixture-recall-unreliable
title: "GridStore (GS) multi-fixture recall is unreliable — nondeterministic per-child propagation on Down; Groups (baked at Store) are the reliable layout carrier"
role: programmer
tags: [ma3, cli, gs, bug, v2.4, doc-gap]
when_to_load: "Before trusting a GS-stored layout to propagate correctly across MULTIPLE fixtures via Down — verify the resulting shape before storing any Group built from a GS-propagated selection; safe to trust GS for single-fixture/ad-hoc use"
status: active
source: "findings/INBOX.md, 2026-07-15, Dave live observation, console 2.4.2.2"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**⚠ Dave's live observation:** a sub-layout was correct at build time, stored via `GS`, and then a later `Down`-recall of that same stored layout **broke** it — in Dave's words, "console problem, not a you problem; it does not always work."

**Failure signature (seen on a 288-sub grid):** on multi-fixture recall, per-fixture blocks propagate **inconsistently** — some fixtures keep the correctly stored layout, others compact-pack or merge instead. The failure is **nondeterministic per child fixture**. Single-fixture GS recall, by contrast, is reliable.

**Consequence / doctrine (Dave):**
- **Groups are the reliable layout carrier** — coordinates baked into a Group at `Store` time hold up on recall.
- **GS is single-fixture / ad-hoc convenience only** — do not lean on it for a multi-fixture build.
- **Reliable lanes for multi-fixture layout work:** direct CLI dot-range layout per rig (see `subfixture-thru-range-syntax`), or Layout-view + lasso (see `layout-to-grid-lasso-loop-and-preserve-gridpositions-toggle`).
- **Always verify shape** before storing any Group built from a GS-propagated multi-fixture selection — see `group-xml-export-selectiondata-census` for the export-based verification lane.

**Durable facts (agent web-research 2026-07-15, key facts preserved in the 2026-07-15 wrap):** this exact nondeterministic multi-fixture GS-recall failure is **not publicly documented anywhere**; there is **no fix in any shipped or announced version**; **2.4.2.2 is the current version** as of 2026-07-15. The full research report was written to a session-mortal outputs path (`outputs/GRIDSTORE_BUG_RESEARCH.md`) and is not part of the durable corpus — these three facts are what survive from it.

**Second failure mode confirmed (2026-07-21) — GS bakes don't survive a repatch:** beyond the nondeterministic multi-fixture recall above, a GS type-bake is also not durable across a fixture-type repatch. The 2026-07-15 ACME sandwich bake was found wiped in cLD_SANDBOX_v0.23 after the v11 repatch (a `Down` probe returned all 48 subs stacked at origin). Two independent reasons now point the same way: **Groups baked at Store are the durable carrier; GS is not.** See `gridstore-keyword-and-fixture-type-write`.

History: none — failure observed and doctrine set live in one session, 2026-07-15; web research the same day found no public documentation or fix. Extended 2026-07-21 with the repatch-wipe failure mode (GS bake gone after the v11 repatch).
