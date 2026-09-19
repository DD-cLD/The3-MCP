---
id: matricks-store-time-embed-travels-with-preset-export
title: "A phaser preset's store-time /MAtricks embed travels with its export as literal XWings/XGroup/XBlock/XShuffle/YShift attrs — grep for them, don't infer phase distribution"
role: programmer
tags: [ma3, matricks, xml-schema, phasers, v2.4]
when_to_load: "Before spec-reading ANY inherited phaser preset to figure out its spatial distribution — check the export for XWings/XGroup/XBlock/XShuffle/YShift/Width literals FIRST; phase-distribution inference is the fallback, not the method"
status: active
source: "findings/INBOX.md [0731-2cLD] 2026-07-31 (SONG_B MAtricks literal decode, {LD} pool 21.1100-1109)"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**Method (card-candidate, CARD_AUTHORING):** when spec-reading any inherited phaser preset, **grep the export for `XWings`/`XGroup`/`XBlock`/`XShuffle`/`YShift`/`Width` literals FIRST.** The store-time `/MAtricks` embed travels with the preset export as literal attributes — reading them directly is the method; inferring the spatial pattern from phase distribution alone is only the fallback when no embed is present.

**Confirmed across {LD}'s SONG_B pool block 21.1100-1109** (Dave called it — "wings"), per-slot: `1100 XShuffle=5` · `1101 XWings=2` · `1102`/`1107 XWings=2+XGroup=4` · `1103 XWings=2` (5-step 72° observed → matched to our Wings2+Group5) · `1104 XWings=2` · `1105 XWings=2` (all populations) · `1106 XShuffle=5+XWings=2` · `1108 XWings=2+XGroup=16+YShift=-1` · `1109` bare (no embed).

**Cost of learning this the slow way:** two sheet revisions, before the grep-first method was adopted.

**Companion caution:** stock/imported MAtricks pool object LABELS are not evidence of their stored values (`tourshow-stock-matricks-pool-inventory`) — export-verify a candidate match before reusing it, the same discipline this method already applies to reading an inherited figure.

**Relation:** `tourshow-whole-fixture-block-law` (the block-size law this reading method feeds). `matricks-negative-value-lua-uint32-wraparound-gotcha` (why export readback, not a live Lua read, is the trustworthy lane for one of these literals — `YShift`). `tourshow-seq1110-song-b-build-record` (the build this method was proven on).


## PAID lesson 2026-08-01 [0801-2cLD] — probe with an UNFILTERED attribute dump, never a hand-written allow-list

**A phaser-embed probe using a FIXED attribute allow-list silently missed `YShuffle` on Swell Dim#3** — three distinct populations were read as only two signatures, because the allow-list didn't anticipate that attribute. **Lesson: probe with an unfiltered attribute dump — everything starting `X`/`Y`/`Z`/`Phase`/`Speed` — never a hand-written allow-list.** An allow-list can only find what you already thought of; this is the same failure shape as any fixed-vocabulary scan missing an attribute nobody wrote down in advance. Apply this to the grep-first method this concept already documents: the grep/probe pattern itself needs to be a wide prefix match, not a curated list of known attribute names.

**Companion census-methodology note:** {LD} encodes a deliberate NO-SPREAD as `PhaseFromX=0 PhaseToX=0` written explicitly ON the recipe line, rather than omitting the attributes entirely. A bare (absent) authored line and a `0->0` authored line are different artifacts with different meanings — when censusing for "bare" (unspread) figures, compare against the source's own explicit `0->0` marker, not against simple attribute absence.

## XGroup attribute order now attested, 2026-08-01 [0801-2cLD]

When a new X-family MAtricks attribute debuts, no desk-order authority previously existed in the corpus's goldens for where it belongs in the attribute sequence. **`XGroup`'s first use (SONG_I `157`/`161`/`162`) is now proven on import**: it lands correctly at the emitted position **`ShuffleMode -> XGroup -> XBlock -> XShuffle`**, live Lua read-back exact. Export-verify is still owed on any FUTURE first-use of a different new attribute in this family — this only settles `XGroup`'s position specifically.

**[0805-2cLD] EXTENSION:** fuller form of this law, with {LD}'s recipe anatomy and the residue-miscall evidence: `source-figures-are-recipe-presets-spread-read-law` — iterate `pre.iter('StandardRecipe')`, do not just grep the literals.

History: extended 2026-08-05 [0805-2cLD] — cross-ref to source-figures-are-recipe-presets-spread-read-law (the embed is full StandardRecipe lines; iterate them first).
