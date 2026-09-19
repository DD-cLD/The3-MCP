---
id: group-membership-follows-refid-not-number
title: "Group membership FOLLOWS a re-FID — groups bind the OBJECT, not the FID number (export-census confirmed 2.4.2.2); contrast with GS type-bakes, which do NOT survive repatch"
role: programmer
tags: [groups, patch, console-fact]
when_to_load: "Before or after re-FIDing patched fixtures — to know whether existing group memberships need to be manually carved, and to distinguish this from GS-bake behavior"
status: active
source: "findings/INBOX.md 2026-07-23 [0723cLD] (CONSOLE FACT re-FID/group test; CARVE RULING application)"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**CONSOLE FACT (export-census confirmed, 2.4.2.2):** group membership **FOLLOWS a re-FID**. Fixtures re-FIDed 130/131/139/141/144/146 → 55-60 REMAINED members of every group that owned them before the re-FID: G101 (60 fixtures incl. 55-60), G105 (57-60 present), G601 (316 fixtures incl. all six). **Groups bind the OBJECT, not the FID number.**

**Corollary:** after ANY re-FID, the moved fixtures do NOT automatically leave groups that logically no longer own them (e.g. a general "spot contract" group that a repositioned fixture no longer belongs in) — this has to be carved out manually.

**Applied (Dave's CARVE RULING, same session):** purge FID 55-60 from the FULL spot-contract block Groups 101-110 (ALL/rows/wings/halves) — since those six now belong to the her-key/backlight doctrine, not the general spot contract. Groups 601/602 were left as-is for now (the key-precedent carve was deliberately NOT extended to them — Dave's call). Mechanism: select the six fixtures, `Store Group <n> /Remove`, export-census verify each group afterward.

**Contrast — the opposite durability:** GS (Group/Selection-scoped) type-bakes do **NOT** survive a repatch — the reverse of this fact. Don't assume patch-time durability generalizes across group-membership and GS-bake mechanisms; they behave oppositely.

Relation: `tourshow-group-contract-v01` for the resulting Group 60-64 backlight membership this carve produced; `tourshow-her-key-and-backlight-doctrine` for why FID 55-60 needed carving out in the first place.

History: none — captured 2026-07-23 [0723cLD] digest run.
