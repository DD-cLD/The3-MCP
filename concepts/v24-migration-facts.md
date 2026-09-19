---
id: v24-migration-facts
title: "v2.4 facts from the manual (PSR/MVR flow, v2.3->v2.4 migration behavior) — unverified live at time of writing"
role: programmer
tags: [ma3, v2.4, verify]
when_to_load: "Before opening an old (pre-2.4) showfile on v2.4, or before using the new PSR/MVR import/export flow"
status: verify
source: "MEMORY §v2.4 facts already banked (from MA_V2.4.2_MANUAL, unverified live), 2026-07-02"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

These facts come from reading `MA_V2.4.2_MANUAL` and were **not yet live-verified on-console** at the time they were recorded (2026-07-02). Treat as banked-but-unconfirmed until checked against actual v2.4.2.2 behavior:

- MVR **import** moved into **Partial Show Read** (Menu → Show Creator); MVR **export** into the patch Export dialog; the old patch-menu buttons were removed.
- PSR matchmaking order: **FID → CID → GUID → Name**; partial property import (Patch / Position / Rotation individually); fixture types are exchangeable in Prepare.
- **PSR MVR import clears the programmer.** MA+ESC (or Shift+ESC) held 5 s cancels a running GDTF/MVR import.
- `Export Patch /MVR` works from the command line (outbound half is scriptable).
- v2.3→v2.4 migration: old-show load **wipes the programmer**; `IDType` Universal → Generic; "Auto" preset mode removed; Lua core **5.4.8**.

Related: `store-recall-recipe-toggle-rules` and `v24-phaser-model` cover the recipe/phaser side of v2.4 changes, live-verified 2026-07-04 (those are `status: active`, this file remains `status: verify` since the migration/PSR-specific claims here were not the ones tested that session).

History: none — status remains `verify`; would be confirmed by walking the PSR/MVR runbook (`WORKING/HOWTO_PSR_MVR_v0.1.md`) on-console and by loading an actual pre-2.4 showfile under 2.4.2.2.
