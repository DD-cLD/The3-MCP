---
id: pool-discipline-stock-vs-custom
title: "Use STOCK pools unless there's a fantastic reason — customization breaks cross-show mergeability"
role: programmer
tags: [ma3]
when_to_load: "Before renaming a pool, creating a new pool, or adding encoder banks — and before storing anything into a feature pool, confirm it's the correct one (e.g. Dimmer = Preset 1.x, Color = Preset 4.x)"
status: active
source: "MEMORY §Console-crash paid-for lessons — Pool discipline, 2026-07-04, onPC 2.4.2.2, MCP-driven, live"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

Pools are **fully customizable** (rename, new pools, new encoder banks) **BUT customization breaks cross-show mergeability** — **use STOCK pools unless there's a fantastic reason** not to.

**Live-confirmed pool assignments:**
- Dimmer presets = **`Preset 1.x`** (pool 1 = "Dimmer")
- Color presets = **`Preset 4.x`**

**Correction noted:** the earlier phaser stores into `Preset 21.x` (see `coachella-rig-identity`'s "Preset 21.1 Sinus phaser (dimmer)") were **into the wrong feature pool** — phasers/dimmer-type content should have gone through the stock Dimmer pool (`Preset 1.x`), not a pool numbered 21.

**Dave's closing framing, worth carrying forward as a standing principle:** "Memory files are the crown jewels — they survive every show file; protect them above any console object."

History: this concept identifies that the Coachella-era `Preset 21.1` phaser assignment (recorded plainly as fact in `coachella-rig-identity`) was, per this 2026-07-04 lesson, a wrong-pool choice — flagging the discrepancy rather than silently editing the Coachella-era record. See FLAGS in the run report. 2026-07-16: `pool-labeling-doctrine-inherited-risk` extends this — renaming stock pools is fine, the risk is inheriting a file where someone else already did it undocumented (the {FESTIVAL} file's custom pools were the trigger).
