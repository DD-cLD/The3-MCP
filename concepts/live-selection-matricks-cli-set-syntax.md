---
id: live-selection-matricks-cli-set-syntax
title: "Setting MAtricks properties: THREE write surfaces — live selection (Set Selection MAtricks \"XWidth\" 5), a POOL object directly (Set MAtricks <n> 'Prop' <val>, incl. PhaserTransform/XinvW), and a recipe's own MAtricks (separate dedicated editor, not reachable by either Set form)"
role: programmer
tags: [ma3, cli, matricks, doc-correction, recipes]
when_to_load: "Before generating any CLI command that sets a MAtricks property (XWidth, PhaserTransform, XinvW, etc.) on the current live selection OR on a POOL MAtricks object directly — do not follow the repo manual's ch12 §13b/§15 no-pool-number form, it fails live for the selection case. Also check this before assuming a recipe's MAtricks can be set the same way — it can't; the recipe-line MAtricks editor's full UI map (X/Y/Z tabs, no Wings row) is here too."
status: active
source: "findings/INBOX.md, 2026-07-10, console live 2.4.2.2; correct form confirmed against the official grandMA3 keyword page"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**Wrong (confirmed failing live, 2.4.2.2):** both `Set MAtricks XWidth 5` and `MAtricks XWidth 5` return **"Illegal object"** — the parser reads `XWidth` as a pool-object name, not a property.

**Repo manual doc-drift:** `MA_V2.4.2_MANUAL` ch12 §13b/§15 claims a no-pool-number `Set MAtricks <prop>` form works for the live selection. **This is wrong as written** — it drops the required `Selection` object. Correct the manual reference in your head; do not trust that section for this syntax.

**Correct (verified live against the official grandMA3 keyword page):**

```
Set Selection MAtricks "XWidth" 5
```

The object is **`Selection`**, and the property name is **quoted**. Also documented on the same keyword page:
- `Off Selection MAtricks`, `Toggle Selection MAtricks`, `Reset Selection MAtricks`
- `Set Selection 2 MAtricks "prop" val` — numbered-selection variant for a non-current/secondary selection.

**Recipe-mode caveat (2026-07-15, live):** this `Set Selection MAtricks` form does **NOT** reach a recipe's own MAtricks — a silent miss, caught only by an overlay/visual verify pass, not by command echo. A recipe's MAtricks must instead be edited in its own dedicated editor (opened via the recipe UI, not this CLI Selection-object form). That editor's internal property naming was observed via its own UI echo, e.g. **"Set DelayTo for direction X"** — different phrasing from the CLI's quoted `"XWidth"`-style names above. See `recipe-lane-end-to-end-verified` for the build this was caught in, and `store-recall-recipe-toggle-rules` for the EditRecipe bookend pattern it's part of.

**Recipe-line MAtricks editor, fully mapped (2026-07-16, live)** — this is the "own dedicated editor" referenced above: **X / Y / Z tabs**; rows **X / XBlock / XGroup** + **Fade / Delay / Speed** From⇄To pairs + **XShuffle / XShift** + **InvertStyle / Transform / InvertXYZ**. **No Wings row** appears on this surface (a reduced set vs. the full MAtricks editor) — **XWings instead rides the store-time `/MAtricks` embed lane** (the `Store .../MAtricks` flag from `store-recall-recipe-toggle-rules`). So a recipe carries **two distinct MAtricks surfaces**: this recipe-line editor (X/Y/Z tabs, no Wings) and the store-time `/MAtricks` embed (has Wings) — an asymmetry worth flagging in any future LD.md documentation pass. (`menu-matricks-overlay-cli-route`'s CLI-opened `Menu "MatricksOverlay"` editor is presumed to be the general/live-selection MAtricks surface, not this recipe-line one — not independently confirmed identical, but consistent with the "two carriers" split here.)

**2026-07-17 addendum — a CLI write lane into a recipe's MAtricks does exist after all, just not this one:** `Assign MAtricks n At Sequence c Cue 1 Thru Part *.*` is a forum-sourced (Kanarek, forum 69993) CLI form that binds a MAtricks pool object onto recipe lines directly — a different verb (`Assign`, not `Set Selection MAtricks`) reaching what may be the same target this concept's recipe-mode caveat said was only reachable via the dedicated UI editor. Not yet cross-verified against the UI editor for identical results. Full grammar (plus the parallel Preset/Shape/Group Assign forms) lives in `recipe-line-pool-binding-via-assign` — load that concept for the write side; this concept remains the source of truth for the live-selection `Set` form and the recipe-line MAtricks editor's own UI surface.

## ⭐ THIRD WRITE SURFACE — `Set MAtricks <n> 'Prop' <value>` works on a POOL object directly, live-proven 2026-08-05 [0805cLD]

**`Set MAtricks <n> 'Prop' <value>` WORKS on a POOL MAtricks object**, not just on the live
Selection (the `Set Selection MAtricks` form documented above) and not just via file-side XML
authoring + Import (`xml-file-side-authoring-import-lane-proven`). Proven 3/3 with exact
readback: `Set MAtricks 183 'XGroup' 14` → reads 14; `Set MAtricks 184 'XGroup' 4` → reads 4;
`Set MAtricks 182 'PhaseFromX' 90` → reads 90.0. **Property name single-quoted, value bare.**
Far cheaper than the XML lane for a one-attribute change. Classifies Tier 2 (`Set `), gated
normally.

**Lane extended the same session, off MX 186 — three more facts:**

1. **A BARE NEGATIVE SURVIVES on this surface.** `Set MAtricks 186 'PhaseToX' -360` (unquoted)
   read back **`-360.0` exact** — no sign-eating. This CONFIRMS the scope boundary already
   asserted in `patch-set-one-prop-quoted-values`: the minus-sign trap is specific to
   patch-fixture `Set`, and does NOT extend to a MAtricks pool object. Quoting is not required
   here.
2. **`XinvW` IS SETTABLE from this lane** — `Set MAtricks 186 'XinvW' 'Yes'` reads back
   **`true`**. The invert family does not need a desk click.
3. **`PhaserTransform` IS a real property on a MAtricks pool object** — it returns `None`
   (unset) rather than erroring, so the property name is correct and the transform is settable
   in principle.

**⚑ Correct property NAMES pinned by contrast:** **`XinvW`** and **`PhaserTransform`** are
real; **`Xinv`** and **`Transform`** are NOT (both return no-such-property). Don't guess the
short forms.

## `PhaserTransform` enum token attested — `Mirror`, 2026-08-05 [0805cLD]

Dave set `PhaserTransform` at the desk on **MX 186**, and the live Lua read returns
**`PhaserTransform=Mirror`** — the token is literally `Mirror`, matching what {LD}'s own
wrapper XML writes. Property confirmed present, readable and desk-settable on a **MAtricks
pool object** (previously only ever seen as an attribute on {LD}'s `StandardRecipe`
wrappers). **Whether it is also SETTABLE from the `Set MAtricks` CLI lane above is still
untested** — Dave clicked this one at the desk; try `Set MAtricks <n> 'PhaserTransform'
'Mirror'` on a scratch object next time the question comes up. Worked example: MX 186 (`cLD W2
G2 X-360 MIR`) matches {LD}'s `Spot Pan#2` wrapper exactly on `XWings/XGroup/PhaseFromX/
PhaseToX/XinvW/PhaserTransform` — see `tourshow-seq2210-song-l-build-record`.

History: corrected same session, 2026-07-10, after the bare forms failed and the official keyword page was checked. 2026-07-15: recipe-mode caveat added — this CLI form does not reach a recipe's own MAtricks; the recipe MAtricks editor is a separate surface with its own property naming. **2026-07-16:** the recipe-line MAtricks editor's full UI surface mapped (X/Y/Z tabs, row list, no-Wings finding) — confirms and completes the 07-15 caveat. **2026-07-17:** addendum added noting a forum-sourced `Assign MAtricks` CLI form that may reach the same target via a different verb — see `recipe-line-pool-binding-via-assign`. **2026-08-05 [0805cLD]:** third write surface added — `Set MAtricks <n> 'Prop' <val>` on a POOL object directly, plus the `PhaserTransform`/`XinvW` dialect facts and the `Mirror` enum token.


## TWO INVERT LANES — do not confuse them (2026-08-20, festival clone day)

A clone-day rig needs **both**, and they are different mechanisms:

| Lane | What it is | Where | Form |
|---|---|---|---|
| **Live mirror** | MAtricks `InvertStyle` {`Pan` · `Tilt` · `Pan and Tilt` · `All`} + `InvertX` on the **current selection** | the symmetric-rig mirror tool, per selection | `Set MAtricks InvertStyle "Pan"` · `Set MAtricks InvertX 1` (0 = off) |
| **Permanent orientation** | **PATCH invert** — the fixture sheet's `InvPan` / `InvTilt` columns | the fix for fixtures hung backwards | fixture sheet / patch |

**Dave's redirect:** for cloned house fixtures the wanted tool is the **patch/setup** lane — a permanent orientation fix that presets then follow. The MAtricks lane is the *live* mirror, useful at the desk in the moment.

**⚠ The `Set MAtricks InvertStyle "<value>"` value-string form was never live-verified** — the wire was down when the toolbox around it was written, and it stayed unverified through the end of the leg. **Validate on a scratch selection before trusting it.** Manual source: local manual ch.12 §16.

History: extended 2026-08-28 (librarian, tour leg) — the two-lane distinction plus the unverified value-string flag.
