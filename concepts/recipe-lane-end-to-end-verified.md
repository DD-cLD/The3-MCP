---
id: recipe-lane-end-to-end-verified
title: "Recipe lane verified end-to-end (2.4.2.2) — two builds: CLI EditRecipe bookend (07-15, standard recipes) and UI Recipe-Editor template-cook (07-16, imported phaser-recipe templates); both cook Group+preset references to correct DMX"
role: programmer
tags: [ma3, recipes, cli, ui, v2.4]
when_to_load: "Before building a recipe-based cue (Group × preset references stored as recipe cue-parts), or before using the Recipe Editor UI to cook an imported phaser-recipe template (Selection/Values pickers, Add Standard Recipe) — this is the full worked, live-verified path for both the CLI and UI lanes"
status: active
source: "findings/INBOX.md, 2026-07-15, console live 2.4.2.2, first recipe build"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**Full verified path, live 2.4.2.2:**

1. **Show Creator Menu ("ShowCreator")** → create **Universal Dimmer (11)** and **Universal Mixcolor (61)** presets.
2. **`EditRecipe Programmer`** ON (the bookend pattern — see `store-recall-recipe-toggle-rules`) → **`Store Sequence 101 Cue 1 Part 1` / `Part 2`** with **Group + universal-preset references** → `EditRecipe Programmer` OFF. Parts built this way show **recipe markers** in the Sequence Sheet (see `select-sequence-retargets-sheet` for getting the sheet to follow Sequence 101).
3. **`Go+`** → DMX outputs the cooked recipe correctly — verified at universe 202: plates at R255/G0/B0, dimmers at 255 (checked via the DMX viewer's address calculator, see `dmx-viewer-address-edit-calculator`).

**Robustness confirmed:** firing `ClearAll` **inside** recipe-edit mode did **not** break the bookend — toggling `EditRecipe Programmer` off afterward stayed clean and the stored recipe was intact (folded into `store-recall-recipe-toggle-rules` as the canonical statement of this rule).

**Caveat found the same build:** a recipe's own MAtricks is **not** reachable via `Set Selection MAtricks` — see `live-selection-matricks-cli-set-syntax` for the silent-miss detail and the recipe MAtricks editor's own internal property naming.

**Preset behavior this build depends on:** universal presets resolve through each fixture's color-engine/emitter data — see `universal-presets-emitter-aware`.

---

**Second build, live-verified 2026-07-16 (UI-driven Recipe Editor — a different, pixel-driven lane from the CLI EditRecipe bookend above; this one cooks imported phaser-recipe templates, not just standard recipes).** Prerequisite context: MA's stock phaser-recipe presets are empty as bare presets — see `stock-recipe-presets-empty-as-templates` for the diagnostic that forced this lane.

**Template-cook mechanics (the fix):** Recipe Editor → **Add Standard Recipe** on programmer Part Zero → **Selection** cell offers None / From Value / **TAKE SELECTION** (captured selection shows as `<Recipe>` in brackets) → **Values** cell opens a preset picker (tabs confirm **pool numbers**: Phaser=21, All 2=22, All 3=23…) → pick e.g. Chase → cooks to output **immediately** (webinar realtime claim confirmed live). Observed on a single cell traveling across a Group-121 selection: **AdaptiveWidth** moved one cell at a time while **AdaptiveMeasure** paced it to the grid — screenshot-verified motion between frames.

**Recipe Editor UI quirks:**
- **"Add Standard Recipe" no-ops unless the "New Recipe" row is focused FIRST** (click the row, then click the button).
- **Selection-cell picker** = None / From Value / Take Selection + a row of Groups pool tiles — clicking a **tile = REFERENCE**, **Take Selection = captured** (shows `<Recipe>`).
- **Values-cell picker tabs prove pool numbers**: …9 Video, 21 Phaser, 22 All 2, 23-25 All 3-5, Bitmaps, Generators.
- Re-entering the Selection cell takes **two clicks** (first selects the cell, second opens the picker); the picker **remembers pool scroll position** between opens.

**Fully-referenced workflow, end-to-end live:** a StandardRecipe (Selection = **Group 124**, REFERENCE via picker group-tile click; Values = **Chase** template) cooked realtime → `Store Sequence 102 Cue 1` `/Overwrite` → executor playback cooks the chase straight from the cue. Observed: on Store, the recipe row **left Part Zero** (moved to the cue?) — **[VERIFY]** whether the stored cue holds a live recipe *reference* vs. *baked values* (check the Show Recipes column in the sequence sheet). Sequence 102 was assigned to **Executor 401** via the assign-dialog lane (Object → Sequence tab → row click); cue labeled **"cLD CHASE GAPS"**; show saved **v0.14**. This is the live proof of the webinar's fully-referenced doctrine banked in `v24-phaser-model`.

**Three-temporal-characters demo (attended, live):** one StandardRecipe line (Values = Chase template), **Selection reference swapped live 121→123→124** — the same phaser produced three distinct rhythmic characters purely from grid choice (flat march / paired double-hits / bounce-with-rests). Each Selection-cell swap **recooks instantly**. The reference-doctrine demo in miniature: **Groups = WHO, recipe = WHAT, grid = WHEN**.

History: full lane built and verified 2026-07-15 (first recipe build, CLI EditRecipe bookend + universal presets). **2026-07-16:** second build added — UI Recipe-Editor template-cook lane, picker mechanics, the fully-referenced workflow's live proof, and the three-temporal-characters demo.
