---
id: stripped-group-membership-recipe-uncooked-diagnosis
title: "A recipe that reads broken/uncooked may have an intact recipe and a STRIPPED group instead — check group membership (fixtures removed, objects/labels kept) before assuming the recipe itself is corrupt"
role: programmer
tags: [ma3, recipes, diagnosis, v2.4]
when_to_load: "When a recipe-based look reads broken, uncooked, or 'not doing anything' on an inherited/handed-off showfile — check the Selection group's actual membership before assuming the recipe, preset, or phaser is at fault"
status: active
source: "findings/{FESTIVAL}/FESTIVAL_FINDINGS_v0.1.md [0722cLD] 2026-07-22, live diagnosis on {LD}'s {FESTIVAL} AR showfile, onPC 2.4.2.2, Dave live"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**Root cause diagnosed live ({FESTIVAL} AR file, 2026-07-22):** recipes that looked broken/uncooked on inheritance turned out to have their **GROUP MEMBERSHIPS stripped** — the Group *objects* and *labels* were intact, but the fixtures inside them had been removed. A recipe whose Selection bind slot points at such a group has **no WHO to cook onto**, so it reads as uncooked/non-functional even though the recipe itself (preset + phaser + grid) is fine.

**Fix, proven live:** re-add the fixtures to the stripped group → the recipe cooks normally. Confirmed on the prior showfile version too, which points to a **deliberate hand-off strip** (likely IP-protection practice when passing a file to another programmer/production) rather than transit/import damage.

**Scope refinement (same session):** the stripped groups specifically hit the **look/phaser library** (recipe-based, group-bound content) — NOT the song cue stacks, which use a different construction method entirely (see `festival-main-cue-baked-vs-recipe-status`).

**Diagnostic takeaway, generalized:** when inheriting or reviewing someone else's recipe-based showfile and a look reads dead, **check group membership first** (`Export Group <n>` → XML census, see `group-xml-export-selectiondata-census`) before concluding the recipe/preset/phaser chain is broken — an empty-but-labeled group is a distinct failure mode from a genuinely corrupt recipe, and the fix (re-populate the group) is trivial once diagnosed. Distinct from the deliberate design pattern in `tourshow-functional-vs-flavor-fixture-taxonomy` (an intentionally-empty flavor group as graceful degrade) — this is an *inherited* file showing *accidental-looking* (but likely deliberate, hand-off-side) empty groups, not a design choice made by the current programmer.

History: none — diagnosed and fixed live in one session, 2026-07-22, on {LD}'s {FESTIVAL} AR showfile.
