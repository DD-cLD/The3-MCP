---
id: factory-position-wiz-anatomy-and-porting
title: "POSITION_WIZ.xml (factory demo-show position builder) anatomy: 8 group blocks building Straight/Fan In/Fan Out/Cross/UP×4/Blind into Preset pool 2 via /Merge — plus its porting caveats"
role: programmer
tags: [ma3, macro, xml, v2.4]
when_to_load: "Before reading, porting, or modeling a new macro on POSITION_WIZ — its file-side anatomy, the grammar techniques it demonstrates, and the three things that break on a naive import into another show"
status: active
source: "findings/INBOX.md, 2026-07-19 [0718-19cLD]; MACRO_LIB_CATALOG_v0.1.md §5 (full anatomy)"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**Location & identity:** `gma3_library/datapools/macros/POSITION_WIZ.xml` — a **user datapool** file, already sitting in the console's macro import path (no relocation needed to use it). `DataVersion 2.4.2.2`, macro name "Position Wizard." Carries a "Red Back" Appearance via an embedded `DependencyExport` (see `macro-xml-schema-cracked` for the schema-level fact that macro XML can carry dependencies at all).

**What it produces:** universal position presets — **Straight, Fan In, Fan Out, Cross, UP Straight, UP Fan In, UP Fan Out, UP Cross, Blind** — written into stock **Preset pool 2** (Position), accumulated **per-group over Groups 1–8** using name-addressed `/Merge` stores (`Store Preset 2. "Name" /Merge` — each of the 8 group blocks merges its own values into the same named preset rather than overwriting).

**Line 1** is the self-gating Lua Confirm control-structure idiom — see `macro-control-structure-workaround-idioms` for the mechanism.

**Then 8 near-identical blocks, one per Group 1–8, each:**
1. Selects the group plus a second object via raw **Handle** references (`#000000027e001379`-style hex) — see `macro-handle-persistent-object-reference` for what Handles are and how this hex form ports.
2. `Attribute "Pan" At Absolute Physical 0` + `Tilt At Absolute Physical -45` → `Store Preset 2. "Straight" /Merge`.
3. `Pan At Absolute Physical 30 Thru -30` → "Fan In"; `-30 Thru 30` → "Fan Out". Negative-bound `Thru` spreads work fine here — this is a programmer-attribute value-spread, not the patch-`Set` CLI spread that rejects negative bounds (see `patch-set-one-prop-quoted-values` for that scope boundary).
4. Cross: one half-selection at Pan −30, the other half at +30 → "Cross".
5. UP family: `Tilt At Absolute Physical -95`, then a **single-attribute preset recall** — `Attribute "Pan" At Preset 2."Straight"` — pulls just the Pan value back out of the already-stored preset to compose "UP Straight" (new Tilt + inherited Pan), and likewise for UP Fan In / UP Fan Out / UP Cross.
6. Blind: `Grid 'Rotate' 'Right'` + `Tilt -90 Thru -45` → "Blind", then `ClearAll`. See `tourshow-position-wiz-blind-depth-grade-root-cause` for what happens when this block runs against a selection that isn't a real 2D grid.

**Porting caveats (all three matter before running an adapted copy against any other show):**
1. **Handles are show-specific** — they point at the demo show's own Groups 1–8 and selection objects; imported elsewhere they dangle or resolve to the wrong objects. Any port must replace every `#...` handle line with explicit `Group <n>` / MAtricks calls. This is THE key POSITION_WIZ porting caveat.
2. **Tilt angle semantics (−45/−95/"UP") assume the demo rig's own hang orientation** — re-derive the angles for a different rig's overhead trusses before trusting the preset names.
3. It writes into Preset pool 2 with `/Merge` and issues **no SaveShow** of its own — checkpoint first (hard rule: SaveShow before any XML import, see `saveshow-discipline-and-mcp-tier`).

cLD's own port of this macro is `cLD_POSITION_WIZ.xml` — see `cld-position-wiz-generic-v01-authored-and-deployed` for what changed in the port and its live-run status.

History: none — anatomy read whole 2026-07-19 from the factory file, `MACRO_LIB_CATALOG_v0.1.md` §5.
