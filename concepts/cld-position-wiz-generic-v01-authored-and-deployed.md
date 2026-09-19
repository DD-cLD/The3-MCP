---
id: cld-position-wiz-generic-v01-authored-and-deployed
title: "cLD POSITION WIZ generic v0.1 — first cLD-authored macro XML, imported and run live on console; DS-row clean, whole-rig Blind not yet depth-graded"
role: programmer
tags: [tourshow, macro, xml, v2.4]
when_to_load: "Before running, editing, or extending cLD's own position-wizard macro, or before citing it as proof the macro-XML authoring lane works end to end"
status: active
source: "findings/INBOX.md, 2026-07-19 [0718-19cLD], console live (Dave); wrap 2026-07-19-macro-lane-position-wiz-group-contract.md"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**Authored + deployed:** `cLD POSITION WIZ generic v0.1`, composed entirely from factory-verbatim grammar (see `factory-position-wiz-anatomy-and-porting` for the techniques it borrows). Design choices versus the factory original:
- **Selection-based, not handle-based** — no Handles, no Groups baked into the macro itself; it operates on whatever's selected when it fires. Sidesteps the factory version's #1 porting caveat entirely (no show-specific handles to dangle).
- **Slot-addressed stores at 2.121–2.127** — follows cLD's own century-scratch-slot convention (see `preset-copy-label-mcp-and-century-scratch-slots` for the pool-21 preset instance of the same convention; this is that convention's pool-2 application), plus a Label pass on each stored preset.
- **Self-gating Lua Confirm kept** — same control-structure idiom as the factory original (see `macro-control-structure-workaround-idioms`).
- **Cross / UP-Cross DROPPED from the generic version** — Cross needs a half-selection, which a plain selection-based macro can't derive on its own. A base-show variant queued behind air-group creation will get real Cross via mirror-half groups instead.

**Files:** repo master `generated/cLD_POSITION_WIZ_generic_v0.1.xml` (xmllint-valid); deployed via Desktop Commander to `gma3_library/datapools/macros/cLD_POSITION_WIZ.xml`.

**✅ LIVE-VERIFIED (Dave, console, 2026-07-19):** imported and ran clean — the **first cLD-authored macro XML run live on console**, putting macros alongside presets and sequences in the proven file-side XML authoring lane (see `xml-file-side-authoring-import-lane-proven`). DS-row run: fine. **Whole-rig run: stored everything correctly EXCEPT no depth-graded Blind tilt** — see `tourshow-position-wiz-blind-depth-grade-root-cause` for the diagnosed cause and the fix (2D grid groups per category, tracked in `tourshow-group-contract-v01`).

**[VERIFY] still open at desk:**
- Whether `Store .../Merge` auto-creates a preset slot that doesn't already exist, or requires the slot to pre-exist.
- `Grid Rotate` scope on cLD's own version specifically (as opposed to the factory original).
- A fuller verify checklist beyond the DS-row spot-check was raised live but not yet run in full.

History: none — authored, deployed, and given its first live run all in the 2026-07-19 session.
