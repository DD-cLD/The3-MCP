---
id: selection-count-probe
title: "Cheap group-membership census: Cmd a Group select, read Lua SelectionCount(), announce, ClearAll after — no export, no walk"
role: programmer
tags: [ma3, lua, cli, census, v2.4, tourshow]
when_to_load: "When you need to know how many fixtures a group actually holds on THIS file/rig before trusting a repoint, a recipe selection or a wings/block calculation — and a full export would be overkill"
status: active
verified: grandMA3 onPC 2.4.2.2 (Mac), EU tour leg 2026-08
source: "findings/INBOX.md [0826-2/3cLD] 2026-08-26, {FESTIVAL} — used to verify groups 401/415/422 = 52 each, 1401 QX40 MM = 7, 1402 QX40 COLOR = 35 before the masters surgery"
supersedes: []
superseded_by: null
---

**The probe:** issue the group selection over the command line, then read the count from Lua:

```
Cmd('Group <n>')      -- select
SelectionCount()      -- read
Cmd('ClearAll')       -- tidy (ending-law)
```

It is a **write-effect operation riding the read channel** — the selection is real console state — so the **announce-always law applies** (see `classifier-tier-drift`), and **`ClearAll` afterwards is not optional**: leaving a live selection behind is exactly the shared-command-surface hazard `desk-clear-callout-before-console-write-rule` exists for.

**Why it matters more on tour than in the shop.** Group membership is the one number every venue adaptation depends on — wings divide it, blocks partition it, phase spreads across it. It is also the number that changes silently when a rig is cloned. Receipts from the leg: `cLD JDC PLATE MASTER` / `BEAM MASTER` / `ALL` = **52** each at {FESTIVAL}; **G416 plates = 18, G417 tubes = 0 (dormant)** at {FESTIVAL}; **24 and 24** at {FESTIVAL}; **11 and 11** at {FESTIVAL}. Each of those numbers changed the doctrine call that followed (`mx-cell-geometry-law`).

**Relation:** `inherited-file-membership-is-ground-truth` (never trust a group's *label*) · `mx-cell-geometry-law` · `group-xml-export-selectiondata-census` (the export-side alternative when you need membership, not just a count).

History: none — used repeatedly across the EU leg, 2026-08-26 onward.
