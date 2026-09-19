---
id: assign-layout-merge-dialog-behavior
title: "Assign Layout onto an existing layout pops an Overwrite/Merge/Remove/Cancel dialog; Merge appends in selection order but one run silently dropped the range-head FID (47/48)"
role: programmer
tags: [ma3, cli, v2.4, layout, dialog]
when_to_load: "Before running Assign Layout against a layout number that already exists — expect a dialog, and verify Merge results by export diff"
status: active
source: "findings/INBOX.md, 2026-07-14, console live 2.4.2.2; wraps/2026-07-14-3drig-mirror-doctrine-grid-drills.md"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**Assigning to a layout number that already exists pops a dialog** with four options: **Overwrite / Merge / Remove / Cancel**. This is distinct from the first-time-creation case (`Assign Layout <n>` with no existing Layout `<n>` — see `layout-cli-assign-and-posxy-syntax`), which creates the layout directly with no dialog.

**The dialog only fires when the incoming selection overlaps existing layout content.** Confirmed by contrast: re-`Assign`-ing a single fixture (FID 201) that was already merged in produced **no dialog at all**, because there was no overlap left to resolve.

**Merge appends the new elements in selection order** onto the existing layout.

**⚑ Anomaly, cause unconfirmed:** one Merge of `Fixture 201 Thru 248` (48 fixtures) into an existing layout appended only **47 of 48** — FID 201, the **range head**, was silently skipped, with no error or warning. A follow-up re-`Assign` of FID 201 alone appended it cleanly (and triggered no dialog, since by then it didn't overlap). The mechanism is not understood — **export-verify (XML or MVR diff) after every Merge** until this is root-caused; don't trust the on-screen element count alone.

**Contrast: `Store <object> /Overwrite` does NOT pop a dialog.** Unlike `Assign Layout`'s Merge/Overwrite prompt, storing over an existing object with the explicit `/Overwrite` flag (e.g. `Store Group ... /Overwrite`) ran with no dialog at all — the flag-based CLI form suppresses the interactive prompt that the plain `Assign` form triggers on overlap.

**New elements added by Merge get auto-placed, not left at a fixed default** — they inherit the layout's current arrange-tool state (e.g. a Line arrangement) until explicitly positioned by `Set` — see `layout-xml-export-schema-and-import-lane`.

**Batching note:** this dialog is a blocking dialog — see `dialog-suspend-resume-batched-lines` for what happens to the rest of a `;`-batched line when it pops (suspend, then resume on resolution, even on Cancel).

History: none — first (and so far only) live exercise of the existing-layout Assign path, 2026-07-14; the 47/48 anomaly is flagged, not yet root-caused.
