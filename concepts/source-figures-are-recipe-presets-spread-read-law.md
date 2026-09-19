---
id: source-figures-are-recipe-presets-spread-read-law
title: "{LD}'s figures are RECIPE PRESETS — read the embedded StandardRecipe lines first; cooked per-fixture rows are residue and miscall spreads"
role: programmer
tags: [ma3, v2.4, tourshow, source, phaser, recipe, matricks, preset]
when_to_load: "Before reading any {LD} figure's spread/MAtricks intent from a {FESTIVAL} export, and any time a spread call is about to be made from cooked per-fixture Phaser@Phase rows."
status: active
source: "findings/INBOX.md 2026-08-05 [0805-2cLD] — live console v2.4.2.2 probes + {LD} {FESTIVAL} export reads + Dave rulings"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---
{LD}'s figures are RECIPE PRESETS: each figure carries its own internal
StandardRecipe lines (Selection + XWings/XShuffle/XBlock/XGroup/YShuffle +
PhaseFrom/To per population) inside the preset export. That is {LD} doing at
the PRESET layer what cLD's build does at the CUE layer. The cooked per-fixture
Phaser@Phase rows are the RESIDUE those recipes leave.

**METHOD LAW: read `pre.iter('StandardRecipe')` FIRST; cooked rows are fallback
only.** Reading residue instead of recipe lines produced three wrong spread calls
on SONG_Q: wash "unison" was actually W2 G4 X-360 · RIVALE "unison" actually
W2 X-90 · PLATES half-rev bound shuffled S5-X-180 where the recipe says winged
W2 X-180.

The embeds are trustworthy: Dave's from-memory corrections matched the embedded
recipes EXACTLY (W2 S5 X-360 for Swell/Bridge · W2/W6 Breakdown · S5 fills ·
W2 X-90 pline).

{LD}'s MX vocabulary across gb_s2500 + gb_s2700: XWings 2 (once 6) · XShuffle
always 5 · XBlock 7 (linear JDC runs) · XGroup 4 (once) · Y only ever YShuffle=5
paired with XShuffle=5 (XY sparkle) · phase literals ride with the knobs
(0→±360, 90→0, 90→−180). Never YWings/YBlock/YGroup.

Full form of the read-order law previewed in
`matricks-store-time-embed-travels-with-preset-export` (grep-the-literals was the
partial method; iterating the StandardRecipe lines is the whole one). Flat-literal
phase scoping: `phase-math-formulas`.

History: none — minted 2026-08-05 [0805-2cLD]; recipe-first read law + MX vocabulary from {FESTIVAL} export probes, three SONG_Q residue miscalls corrected against Dave's memory.
