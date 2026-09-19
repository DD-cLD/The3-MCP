---
id: objectlist-thru-vs-wildcard-gotcha
title: "ObjectList Thru ranges silently return empty — use wildcard (*) for pool censuses instead"
role: programmer
tags: [ma3, lua, v2.4]
when_to_load: "Before using ObjectList() with a range expression for a pool census or bulk readback — Thru fails silently, wildcard is the correct form"
status: active
source: "findings/INBOX.md line 41, 2026-07-17 [0717-2cLD], console live 2.4.2.2"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

`ObjectList('Preset 22.1 Thru 22.46')` returned an **EMPTY list — no error, no exception** — a silent-failure trap.

`ObjectList('Preset 22.*')` **wildcard** form returned all 51 occupied slots correctly.

**Rule: use wildcard, not Thru, for pool censuses via ObjectList.**

**Relation:** companion to `recipe-lane-lua-readback-grammar`'s Get/PropertyName grammar; both fed the same live pool-22 census that cross-checked clean against the XML census (see `tourshow-stock-recipe-library-inventory`).

History: none — established live 2026-07-17.

**[0805-2cLD] EXTENSION — the Delete echo lies on Thru ranges:** `Delete Preset 21.2720 Thru 2722` echoed "Illegal object" while ACTUALLY deleting the range — the follow-up single delete's "Illegal object" was honest (already gone). Wildcard ObjectList census is the truth channel, not the echo. Same family: single-slot `ObjectList('Preset 21.2720')` returns no handle even when the object exists.

History: extended 2026-08-05 [0805-2cLD] — Thru-range Delete echoes "Illegal object" while deleting; single-slot ObjectList returns no handle on an existing object; wildcard census is the only truth channel.
