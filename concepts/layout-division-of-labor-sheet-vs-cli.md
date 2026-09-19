---
id: layout-division-of-labor-sheet-vs-cli
title: "Division of labor confirmed: the property SHEET wins for bulk uniform toggles (3 clicks beats 64 CLI sets); CLI wins for generated/computed geometry"
role: programmer
tags: [ma3, v2.4, layout, process]
when_to_load: "Before deciding whether to script a bulk Layout/element property change via CLI or just do it in the sheet — a uniform change across many elements is a sheet job, not a CLI-loop job"
status: active
source: "findings/INBOX.md, 2026-07-14, console live 2.4.2.2; wrap 2026-07-14-console-cli-era-layouts-audit-grouptheory"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**Worked example — Layout 2 "SPOT PLOT" (saved as `cLD_SANDBOX_v0.2`):** 64 elements placed exactly via CLI (4 truss rows at `y=600/400/200/0`, `x=0-1100` step 100; wings at `x=-200 & 1300`, `y=0-560` step 80 — this initial wing placement was later re-specced, see `tourshow-template-rig-patch-and-layout-state`).

**Strays:** elements 63/64 got dragged out of place during Dave's manual "Setup" play; restored via CLI. (A reminder that manual UI interaction can knock CLI-placed geometry out of position — CLI is also the reliable restore path.)

**The division-of-labor lesson:** Dave then set **all 64 elements'** `VisibilityBorder=Visible` + `VisibilityID=Visible` + `ObjectName=Hidden` in **three clicks** via the property **sheet's column mass-edit** — faster and simpler than 64 individual (or even batched) CLI `Set` calls would have been.

**Rule: sheet for bulk uniform toggles, CLI for generated/computed geometry.**
- **Sheet lane:** when every element needs the *same* value for a property (uniform toggle/style change across the whole set) — use the sheet's column mass-edit.
- **CLI lane:** when each element needs a *different, computed* value (placement math, per-element geometry) — that's what CLI batching (`Assign Layout` + `Set Layout n.e "PosX"/"PosY"`, see `layout-cli-assign-and-posxy-syntax`) is for.

History: none — division of labor observed and confirmed live in one session, 2026-07-14.
