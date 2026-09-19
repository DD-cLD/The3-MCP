---
id: recipe-layer-is-fixture-agnostic-doctrine
title: "Recipe layer is FIXTURE-AGNOSTIC: author Group x Preset and nothing else — the GROUP absorbs the rig, the PRESET absorbs the fixture type, and no recipe ever names a cell count or address"
role: programmer
tags: [tourshow, festival, doctrine, portability, recipes]
when_to_load: "Before authoring ANY cue part or recipe line — this is the standing rule for what a recipe is allowed to reference. Also load before deciding whether a rig change (fewer fixtures, different type, no cell split) breaks existing content: it almost certainly does not, and this concept says why."
status: active
source: "Dave ruling 2026-07-27 [0727cLD]; re-verified 2026-07-27 [0727-2cLD] by parser against ALL 105 live SONG_T recipe-line bindings (the earlier count of 50 was wrong)"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**Dave's ruling, stated as the portability test:** the same programming must work on
**anything from a simple flood (LEDJ Q40 — which has a strobe channel) through a
LOW-channel-mode JDC1 or Strike M up to a HIGH-channel-mode JDC1 or Strike M.**

**The rule: a recipe line references a GROUP and a PRESET. Nothing else.** It never names a
cell count, a cell address, a subfixture depth, or a fixture type.

## Three layers, each absorbing a different kind of difference

| Layer | Absorbs | How |
|---|---|---|
| **RECIPE** | nothing — it is the invariant | `Selection = Group` x `Values = Preset` |
| **GROUP** | the **RIG** | the same role slot holds JDC1 cells at one venue and bare floods at the next |
| **PRESET** | the **FIXTURE TYPE** | `/Universal` store mode resolves per profile's emitter engine |

This is the mechanism that makes **author-once-fill-per-rig** real, and it is why the
festival leg is tractable at all: at each stop you re-fill the contract groups against
whatever is hanging, and the content lands unchanged.

## It is already true of the inherited content

Live-verified across **all 105 live recipe lines of SONG_T** ({FESTIVAL}, Sequence 1500):
every one is `Group x Preset` — `G70 x Preset 4.4`, `G70 x Preset 1.5`, `G71 x Preset 1.15`,
`G11 x Preset 21.1504`. **Not one recipe references a cell count or address**, even though
several of those groups contain 228+ cells.

**⚑ COUNT CORRECTED 2026-07-27 [0727-2cLD]: 105, not 50.** The original figure of 50 (repeated
in `CURRENT_STATE_A0727.1` and that session's NEXT_ACTIONS) undercounted by more than half. A
parser census of the export found **105 `StandardRecipe` elements that are DIRECT children of
a Part** — plus 10 more nested inside `DependencyExport` blocks, which are embedded dependency
COPIES, not live recipe lines, and must not be counted. **The doctrine was re-tested against
all 105 and returned ZERO violations**, so the correction makes the claim better evidenced,
not weaker. The cell-ness of a group is invisible to the
recipe; it only determines how many things receive the value.

## Corollary — the gated chain is a GROUP/DEFAULTS problem, not a content problem

`jdc1-output-gated-chain` (output = fixture master x branch master x cell) looks like it
threatens portable cell content. It does not, **provided masters are defaulted full** per
`master-default-doctrine` (`Store Default`: master full, cells zero, on every multi-cell
type). Then `Group x Full` behaves identically whether the group holds cells behind a
master or bare floods. **The gate bites a naive clone of someone else's file; it does not
bite content authored this way.**

## Corollary — a shrinking rig hits the FILL layer, not the CONTENT layer

First real test: 19 upstage JDC1 replaced by 7 LEDJ Q40 (budget-driven). Nothing in the
content breaks. Phaser resolution **degrades gracefully** — a phaser across 228 cells is a
fine chase and across 7 floods a coarse one; same recipe, still correct, reads differently.
**The correct response to a rig shrinking mid-advance is to re-fill the group, not to
re-author the song.**

**One thing this doctrine REQUIRES to hold:** no baked N anywhere in the recipe — see
`no-baked-n-portable-phaser-doctrine`. A MAtricks carrying a phase literal computed for a
specific fixture count is the one thing that genuinely does break across rigs.

Relation: `tourshow-group-contract-v01` (the role-based group scheme the GROUP layer
depends on) · `universal-presets-emitter-aware` (the `/Universal` rule the PRESET layer
depends on) · `replay-portable-strobe-doctrine` (same principle applied to strobe: build it
as a shutter chase so it carries across fixture types) · `tourshow-recipe-based-show-style-ruling`
(the show-level mode ruling this operationalises).

## ⚠ PILLAR TWO FAILS ON THE INHERITED CONTENT — verified 2026-07-28

This doctrine has two pillars: **GROUP absorbs the rig** and **PRESET absorbs the fixture type
via `/Universal`**. The 105/105 recipe-line test above verifies the RECIPE LINE layer only. It
does **not** establish that the presets those lines point at are portable — and on {LD}'s
file they are not.

**Live-read from the export:** `Intro 1/1 Spot Dim` carries `PresetMode="Global"` but its
`PresetData` holds **34 per-fixture `<Phaser ... Selective="Selective">` rows**, one per member
of the 34-fixture Spots group, each with a **baked per-fixture `Phase`** (first row
`IDType=0 ID=101 Attribute=Dimmer Phase="102.857"` — which is `10 × (360/35)`, a literal
computed against their fixture count). **The label says Global; the data is Selective and
fixture-locked.** Swapping the group on a recipe line does NOT re-point it.

**⚠ Do not read `PresetMode` as evidence of portability — read the `PresetData` rows.**

**How the build sidesteps it:** `tourshow-authoring-contract-v01` rules that we never port
their phasers at all — theirs are a checklist of where a phaser belongs, and we author fresh
template ones. The Selective/baked-N problem therefore never arrives.

**Lesson on the testing itself:** when verifying a doctrine with multiple pillars, **name which
pillar the test covered.** Reporting "zero violations" without that scope read as more
portability than had actually been established.
rig-layer difference for a content-layer break. Updated 2026-07-27 [0727-2cLD]: recipe-line
count corrected 50 -> 105 by parser census, and the fixture-agnostic test re-run across all
105 with zero violations. Its required companion `no-baked-n-portable-phaser-doctrine` — cited
by this concept before it existed — was filed the same session. Updated 2026-07-28 [0727-2cLD]: recorded that pillar two (PRESET absorbs fixture type) FAILS on the inherited content — their phasers are Selective despite a Global PresetMode — and that the 105-line test covered the recipe-line layer only.


## ⛔ PILLAR TWO, ONE LAYER DEEPER — a preset's DEPENDENCIES carry fixtures too (2026-07-31)

The section above establishes that `PresetData` rows can be fixture-locked while the header reads `Global`. {LD}'s **Synth Swell** preset (`21.1031`) adds the second half of the trap, and it is worse:

- `PresetMode="Global"` — the label, again, a lie.
- **96 `Selective` rows addressed at CELL-LEVEL dot-IDs of the OLD RIG** (`12204.1.1`, `.1.2`, …), each with baked per-cell `Phase` (6.32° steps) and baked `Speed` (238 BPM), every row stamped `Cooked=`.
- **Its `DependencyExport` embeds the actual GROUP OBJECTS** it was built against — `JDC1 SW [RGB]` and `JDC1 DS [STB]`.

**So the preset carries fixture references two independent ways**, and neither is visible from the recipe line. Swapping the Group on the cue part **re-points nothing** — the preset has to be re-authored on our own objects. (Done: re-authored as `cLD SONG_A SWELL` + Seq 1017, see `tourshow-seq1010-build-record`.)

**How it was missed, which is the actual lesson:** the sequence layer was read, its group binds looked crosswalkable, and the piece was declared compatible without opening the preset. Dave caught it. **Reading one layer is not reading the object.**

**The rule, generalised:** before calling any inherited preset compatible, read **the rows AND the dependencies**, not the header — and if either names fixtures, cells, or groups, the preset is a re-author, not a re-point. The good news is that the musical figure survives the trip: a spec-read of the steps gives the template class, and the baked speed gives the tempo gear.

History: ruled by Dave 2026-07-27 during the {FESTIVAL} recon, after cLD twice mistook a 2026-07-31 [0731cLD] — Pillar Two extended with the DependencyExport group-embedding case ({LD} Synth Swell 21.1031); rule restated as rows AND dependencies.
