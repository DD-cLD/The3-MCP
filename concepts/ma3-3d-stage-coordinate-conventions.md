---
id: ma3-3d-stage-coordinate-conventions
title: "MA3 3D stage axes: +X = stage left, +Y = upstage, +Z = up; RotX+ tips a fixture's top downstage; four lanes exist for editing patch positions"
role: programmer
tags: [ma3, v2.4, 3d, patch, coordinates]
when_to_load: "Before computing, writing, or interpreting any fixture Pos X/Y/Z or Rot X/Y/Z value — or before deciding which UI/CLI lane to use to place a fixture in 3D"
status: active
source: "findings/INBOX.md, 2026-07-14 (help.malighting patch_position_fixtures, 2.4 manual); console live 2.4.2.2"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**Axis convention (per the 2.4 manual):** **+X = stage left**, **+Y = upstage** (so downstage is negative Y), **+Z = up**. Units are meters for position, degrees for rotation. The patch sheet's position columns are **Pos X/Y/Z** and **Rot X/Y/Z**, matching the XML attribute names (`PosX`/`PosY`/`PosZ`/`RotX`/`RotY`/`RotZ`).

**Rotation convention:** positive **RotX** tips a fixture's top toward **downstage**. Practically, **RotX = −90** faces a hung, non-moving-head fixture (a strobe or batten-style unit) out toward the crowd — this is exactly the value used on the template rig's JDC1 and ACME pix, both patched at RotX −90 (see `tourshow-template-rig-patch-and-layout-state`). Moving-head fixture types (spots, washes) aim via pan/tilt in the programmer rather than RotX, and this corpus doesn't record a RotX value for them.

**Four lanes exist for editing patch fixture positions**, each suited to a different job:
1. **Patch sheet, Full-columns mode** — direct cell entry, best for reading/spot-checking or small manual edits.
2. **3D Setup-mode Arrangement tool** (Line / Grid / Circle, with spacing encoders) — an encoder/UI lane for auto-arranging a selection in 3D space. No CLI equivalent is documented for it, and this session didn't end up using it (positions were written by CLI `Set` instead).
3. **CLI `Set`** — e.g. `Set Fixture 101 "PosX" "0.6"`. Works from LivePatch context; property names match the XML attrs; `Thru` ranges are supported for bulk addressing. See `patch-cli-set-command-gotchas` for the failure modes this lane has (one property per command, mandatory quoting, no negative-bound spreads).
4. **Patch sheet cell-editor spreads** — the sheet's cells embed a `Thru`-capable calculator (e.g. typing `-7 Thru *` spreads a value across the selected rows). This is Dave's mass-edit idiom, and it's the only lane confirmed to handle **negative-bounded** spreads (CLI `Set` can't — see `patch-cli-set-command-gotchas`). **[VERIFY]** whether the editor's ✗-close button commits or cancels a pending spread is untested — treat it as commit until verified.

History: none — coordinate convention and lane inventory both captured live 2026-07-14, cross-referenced against the same session's 3D rig build.
