---
id: patch-export-dialog-and-mvr-lane
title: "Export Patch: the dialog route (Menu \"Patch\" → format/scope tabs) works on 2.4.2.2 — the documented direct-CLI form throws \"Illegal object\"; patch XML + MVR schemas captured"
role: programmer
tags: [ma3, cli, v2.4, patch, export, mvr]
when_to_load: "Before exporting or importing a Patch (grandMA3 XML or MVR), or before parsing/authoring either format off-console"
status: superseded
source: "findings/INBOX.md, 2026-07-14, console live 2.4.2.2; repo manual 08 + 2.4 manual (documented-vs-live conflict); wraps/2026-07-14-3drig-mirror-doctrine-grid-drills.md"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: patch-xml-export-lane-and-schema
---

**Documented CLI form does NOT work live on 2.4.2.2.** The repo manual (08 §9.2) and the 2.4 manual describe a direct CLI export: `Export Patch "name"` for grandMA3 XML, `Export Patch /MVR` for MVR. Live-tested 2026-07-14: `Export` cannot address `Patch` as an object at all — it throws **`Illegal object`**. Repo manual 08 §9.2's CLI line is confirmed wrong for 2.4.2.2.

**What actually works: the dialog route.** `Menu "Patch"` opens the patch menu from the CLI; from there the Export dialog has two independent controls:
- **Format tabs:** `grandMA3` | `MVR`
- **Scope:** `EntirePatch` | `SelectedFixtures`

**⚠️ The format tab RESETS to MVR on every dialog open** (the manual documents MVR as the default) — click the `grandMA3` tab explicitly each time XML is wanted, or the export silently lands as `.mvr` instead.

**Output paths (Mac onPC, same `gma3_library` root as the layout/plugin paths — see `project-file-locations`):**
- grandMA3 XML → `gma3_library/patch/stages/<name>.xml`
- MVR → `gma3_library/mvr/` (exact filename pattern not yet captured)

**Patch XML schema (grandMA3 format):**
- Patch folders become nested `<Fixture>` nodes (per `Mode 5.Grouping`).
- `PosX`/`PosY`/`PosZ`/`RotX`/`RotY`/`RotZ` attributes are **omitted from the XML entirely when the value is zero** — a missing attribute means zero, not an error.
- Non-zero rotation values carry a leading space in their string form — e.g. `RotX=" -90.00"` (space before the minus, verbatim from source).

**MVR schema:** an MVR file is a **zip** containing `GeneralSceneDescription.xml` plus per-fixture-type GDTFs. Each fixture's `Matrix` is `{u}{v}{w}{o}` in mm, where `o` is position and `RotX` is derivable from the v-vector via `atan2(v3,v2)`. A fixture with no `Matrix` entry sits at the origin. **The MVR is parseable — this is a second, independent verification lane** alongside a grandMA3-XML diff (export both, cross-check), and it doubles as the exemplar for future PSR-import work.

**MVR import note (documented, not live-tested this session):** per the repo manual + 2.4 manual, MVR import lives in **PSR (Show Creator)**, and importing there **clears the programmer**. This was not exercised live this session (only export was tested) — treat as a manual-sourced fact until an actual import is run and observed.

**Triple-click gotcha in the Export name field:** in the Patch Export dialog's name field specifically, triple-click does **not** select the `<Default>` token — a paste there appends after it instead of replacing it. Use cmd+A to select-all first. (General Edit Command popup field behavior — see `computer-use-input-loop`.)

**Export may be prompt-context-sensitive — see `export-context-relativity` [VERIFY]** for the one (now-uncertain) data point suggesting Export must be run from the root prompt rather than a LivePatch prompt.

History: none — schema, dialog mechanics, and the documented-vs-live CLI conflict all captured live 2026-07-14.

History addendum: superseded 2026-07-14 — duplicate minted by parallel librarian run 10 (shard brief overlap); content folded into `patch-xml-export-lane-and-schema`.
