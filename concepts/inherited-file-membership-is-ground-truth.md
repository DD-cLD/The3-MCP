---
id: inherited-file-membership-is-ground-truth
title: "⛔ On an inherited show file, MEMBERSHIP is the only ground truth — names, labels and pool positions are hypotheses; derive composition from SelectionData FIDs, never from what a group is called"
role: programmer
tags: [festival, tourshow, inherited, verification, paid-for]
when_to_load: "Before reasoning about, mapping, or building on ANY group/object in a showfile you did not author — and before treating two artifacts as contradictory. Read this before writing a crosswalk, a remap, or an inventory of someone else's file."
status: active
source: "findings/INBOX.md 2026-07-26/27 [0726-0727cLD] — paid for three times in one document during the {FESTIVAL} recon; Dave caught the first; corroborated findings/INBOX.md [0729cLD] 2026-07-29"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**⛔ THE RULE: on an inherited file, derive composition from MEMBERSHIP — never from the
name.** A showfile adapted from a previous production carries the *previous* rig's naming.
Groups get re-pointed at new fixtures; nobody renames them.

## The paid-for case ({FESTIVAL}, 2026-07-26)

The file was adapted from another artist's show. Membership census against a live
FID→FixtureType map proved the names systematically false:

- **`Strike M US / DS / SW` — 20 groups — are GLP JDC1.** Not Strike M.
- **`Veloce (Grid)`** = MAC Viper XIP x20 **+ Proteus Hybrid x14**, and all three `Spots`
  variants are the **same 34 fixtures** — so **no spot-vs-beam separation exists** anywhere
  in the group layer.
- **`Forte`** = Proteus Maximus + BMFL WashBeam; `Forte US` and `Forte SW` are the **same
  six units**. **`PL`** = COLORado PXL Bars. **`Beamwash`** = Maverick.
- **~24 of 80 groups are EMPTY** — including all 12 per-person "band" groups, which were
  vestigial from the previous artist and had no members at all.

cLD made the **same error three times in one document**: read "the file solves the BAND"
(no band existed, groups empty), read "`(Fest)`/`(Tour)` variants already exist — adopt the
pattern" (both `(Tour)` groups empty), and described the naming grammar as decomposing
cleanly (true as grammar, worthless as evidence). **Root cause each time: treating a NAME as
evidence of CONTENT.**

## The method that actually works

`Export Group <n>` → read `<SelectionData>` member FIDs → join against a live
FID→FixtureType map (`ObjectList('Fixture *')` + `:Get('FixtureType')`). Tooling written and
reusable: `showfiles/festival_recon/group_truth.py` + `fidmap.txt` → `GROUP_TRUTH.md`.
Export is the only reliable group census anyway — `handle:Children()` returns **0** for
Group objects (`group-xml-export-selectiondata-census`).

**Payoff, not just caution:** membership analysis also *collapsed* the problem. Behind 56
populated groups sat only ~12 distinct fixture sets — the rest were layout variants
(Grid/Lin/Sym) and cell-depth variants of the same members. The crosswalk was a ~12-row
job, not an 80-row one. **You cannot see that from the names either.**

## ⚠ Companion hazard — FIDs collide across shows in a shared export folder

MA3 exports every show's objects into the **same** `gma3_library/datapools/<type>/`
folders, so two shows' exports coexist and **their FID spaces overlap** (101-164 exist in
both cLD_SANDBOX and {FESTIVAL}). A first analysis run silently misread our JDC 401-412 as
{FESTIVAL}'s "Color Strike M x288." **Always scope a cross-show file-side analysis by
filename provenance; never assume a datapool folder holds one show's objects.**

## Generalisation — provenance determines authority

The same failure shape appeared in a different domain the next day: the corpus held the
SONG_T colour board and the white-void call as two peer authorities needing a ruling,
when the board was **cLD's own early sketch** predating the information that produced the
other. **Before treating two artifacts as contradictory, establish who made each, when, and
on what information.** See `song-t-board-color-contradiction-ratify-pending`.

Relation: `stripped-group-membership-recipe-uncooked-diagnosis` (the sibling failure — an
intact, correctly-labeled group with its fixtures removed makes a good recipe read dead;
**check membership before diagnosing the recipe**) · `group-xml-export-selectiondata-census`
· `source-profile-inheritance-and-reuse-doctrine`.

## ⛔ EXTENDED 2026-07-28 — IT IS NOT JUST GROUPS. PRESET NAMES LIE TOO.

Third instance in the same file, one pool over. {LD}'s **position presets** are, in Dave's
words, **"labeled as a lie"** — `Lowest` points **upstage and high**; `Highest` is **15°
upstage**. The names do not describe the stored values.

**Generalised rule: on an inherited file, an object's STORED DATA is the truth and its NAME is a
hypothesis — for GROUPS (membership), for PRESETS (values), and by extension for any pool
object.** The fix is identical in every case: read the data, never the label. Ladder detail in
`festival-position-preset-stacking-and-tilt-ladder`.

**Corollary that cost real time this session:** four of the seven ladder names were recoverable
file-side from a sequence export's `<Dependency>` blocks, but **2.6-2.8 appear in no exported
song and needed a live console read.** Do not assume a file-side census is complete just because
it returned results — it only covers what the exported material happens to reference.

## Corroboration 2026-07-29 — Strike M "Fest" variants are truthful; the liars are specifically US/DS/SW

A `GROUP_TRUTH` membership cross-check on the {FESTIVAL} file: **`Strike M [RGB] (Grid) (Fest)`** = Color Strike M ×336 subs (24 fixtures, `401-414`/`421-430`, a 49×8 grid); **`[STB] Fest`** = 672 subs. **Both truthful at the group layer.** The JDC1-liar scope established in the paid-for case above is specifically the **US/DS/SW** Strike M groups — not every Strike M-named group. This does not weaken the standing rule (membership is still the only proof); it narrows exactly which names in this file happen to be honest. Confirms Dave's fill-target hypothesis in `tourshow-fill-layer-rebuild-method` (the fills bind `STRIKE M FEST RGB`).

## ⛔ EXTENDED 2026-08-01 [0801-2cLD] — MAtricks pool labels lie the same way group/preset labels do; third pool class to show it

**MAtricks pool slot labels are not evidence of their stored values — extends this doctrine to a third pool class** (after groups and presets/preset names). Live read, same session: slot labeled `'YGroup 6'` actually stores **`YGroup=3`**; slot labeled `'YWing 3'` actually stores **`YWings=2`**; a slot named `'MAtrick 167'` (a DEFAULT, unedited name) turned out to be **fully populated** (`XGroup=6 XWings=4 YGroup=6 YWings=4`, X+Y `0->360`). Dave moved all three objects to pool slots 40-42 once the mismatch was found.

**The rule, restated for this pool: read MAtricks VALUES, never the slot LABEL, before reusing or trusting a pool object** — the same discipline `tourshow-stock-matricks-pool-inventory`'s companion caution already states for stock/imported MAtricks, now confirmed on a cLD-managed pool slot as well, not just inherited ones.


## ⛔ FOURTH OBJECT CLASS 2026-08-03 [0803-2cLD] — PHASER FIGURE NAMES CARRY ALMOST NO IDENTITY INFORMATION

The cross-song phaser figure content-hash (`tourshow-phaser-figure-duplication-across-songs`) confirms the same failure shape one pool over again — the **fourth** object class, after groups (membership), position presets (values), and the MAtricks pool (values), to show inherited/generated labels lying about content.

**A figure's NAME says where in *that song* it was used, not what the figure IS.** Content-hashing 166 figure name-instances across 17 songs resolves them to 57 distinct contents:

- **8** are the SAME NAME reused across songs (`Dim_Sin_Bump` in 17 songs, `Dim Sinus` in 10, `Dim_Ramp Minus` in 5, `Sin` in 4, `20x20 rel PT Circ#4` in 4) — {LD} reusing one object under one name. Not a discovery; already treated as one figure.
- **10** are **DIFFERENT NAMES carrying IDENTICAL content** — this is the actual finding. Widest span: one content hash appears across **12 songs under 8+ different names** (`Intro 1/1 Dim#2` / `Chorus 1/1 Dim#5` / `Bridge 1/1 Dim#8` / …); a second hash spans 12 songs likewise.
- **39** are unique to a single song.

**Standing consequence: hash the content, never dedup figures by name.** A phaser figure's name is exactly as untrustworthy as a group's or a preset's on this inherited file — the object class changes, the rule does not.

**Relation:** `tourshow-phaser-figure-duplication-across-songs` (the concept this fact answers; carries the full hash method plus the 47/31/16 result).

## Scope extended — the hazard now confirmed on a cLD-AUTHORED object too, 2026-08-05 [0805cLD]

**First in-house instance of the labels-lie hazard on an object cLD itself authored, rather
than an inherited one.** MX 148 `cLD XY SHUFFLE 5` reads `XShuffle=5` but **`YShuffle=None`**
— its XY phase IS 0-360 on both axes, but the shuffle is X-only despite the object's own name
saying XY. Flagged, NOT fixed (may already be bound in shipped songs); corrected sibling
minted as MX 185 `cLD S5 YS5 XY360` (Copy 148 + `Set YShuffle 5`). Full detail:
`tourshow-seq2210-song-l-build-record`. **The standing rule above — read stored VALUES,
never a label, before reusing or trusting a pool object — evidently is not limited to
inherited/source-authored content; a cLD-authored object's own name is only as trustworthy as
whatever double-check was actually run against it at authoring time.**

History: none — paid for during the {FESTIVAL} recon, 2026-07-26; generalised 2026-07-27. Extended 2026-07-28 [0727-2cLD]: the rule now covers PRESETS as well as groups — {LD}'s position-preset labels proved false the same way the group names did. Extended 2026-07-29: added a corroborating GROUP_TRUTH census result narrowing the JDC1-liar scope to specifically US/DS/SW Strike M groups, and confirming the Strike M Fest fill-target hypothesis. Extended 2026-08-01 [0801-2cLD]: MAtricks pool labels shown to lie the same way (third pool class). Extended 2026-08-03 [0803-2cLD]: phaser figure names shown to carry almost no identity information (fourth object class). Extended 2026-08-05 [0805cLD]: hazard confirmed for the first time on a cLD-authored object (MX 148), not just inherited/{LD} content; relocated to end-of-file same date — `generated/build_spine.sh` truncates a concept's SPINE.md view at the first `History:` line, so the two `##` sections above (MAtricks pool labels, phaser figure names) had been silently absent from SPINE.md since they were written; this relocation recovers them (gardener rule 4 — nothing deleted, only moved).
