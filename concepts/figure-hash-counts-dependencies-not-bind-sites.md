---
id: figure-hash-counts-dependencies-not-bind-sites
title: "A song's figure-hash count is its DEPENDENCY count, not its bind-site count — census actual cue-list bind sites before sizing a build; an unbound figure is often a pool-resident LIBRARY figure, not missing or aux content"
role: programmer
tags: [ma3, tourshow, figure-hash, census, phasers, methodology]
when_to_load: "Before sizing a song's phaser/MAtricks object build off its figure-hash count, or before treating a figure that hashed for a song but shows zero main-sequence bind sites as missing content, aux content, or a gap — check the actual bind census first"
status: active
source: "findings/INBOX.md [0805cLD] 2026-08-05, SONG_L build (dg_figure_sites.py census; {LD} aux 2201-2204 export)"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**The figure hash tells you what travels WITH a song as a dependency — not what the song's
main sequence actually uses.** A figure can be hashed into a song's dependency export and
bound nowhere in that song's main cue list at all.

**Practical rule: before sizing a song's object build off the figure hash, census the actual
BIND SITES in the cue list.** The hash tells you what travels with the song; the bind census
tells you what the main sequence actually needs. Method: a direct-children-only walk over
Cue>Part>StandardRecipe, reading the `Values=`/`Preset=` leaf token per figure name — never
recurse into `DependencyExport` wrapper copies (see `export-sequence-xml-schema`'s recipe-line
census law for why recursion over-counts).

**An unbound figure is very often a pool-resident LIBRARY figure — the shape dictionary a
song's named figures are built from — not missing content, and not automatically aux content
either.** Do not guess which bucket it falls into; export and read the aux (or wherever else
it might plausibly be used) before concluding.

## Proven on SONG_L, 2026-08-05

Only 5 of SONG_L's 9 distinct content-hashed figures are bound in the main sequence
(`dg_figure_sites.py`, direct-children census): `Verse 1/2` x12 · `Intro 1/1 Dim#6` x3 ·
`Bridge 1/1 Col` x3 · `Bridge 1/1 Dim#5` x3 · `Spot Pan#2` x2 — 23 bind sites total. `Pan
Sin#3`, `Dim_Sin_Bump`, `Dim Sinus` and `Dim_Ramp Minus` show ZERO main-sequence bind sites.

cLD's first guess was that the four unbound figures were the song's AUX layers (`Dim_Sin_Bump`
reads literally as a bump — the aux bump shape). **Wrong, settled by exporting {LD}'s
actual aux (2201-2204) and reading it: the aux carries no phasers at all.** All four are
pool-resident LIBRARY figures, bound nowhere in this song, main or aux. **Generalises: a
figure hashed for a song but bound in neither its main nor its aux is a library object, not
missing content — and not automatically aux content either. Check, don't guess twice.**

## Precedent

Same shape, one step earlier in the chain, as SONG_B's aux-fired figure 658 (pool block
`21.1100-1109`), which the main-sequence export alone had missed entirely — see
`tourshow-seq1110-song-b-build-record`. SONG_B's case resolved when the AUX was checked;
SONG_L's is the harder case, where the figure lives in NEITHER main nor aux.

**Relation:** `tourshow-seq2210-song-l-build-record` (the build this was proven on),
`export-sequence-xml-schema` (the direct-children census law this rule depends on),
`empty-census-deserves-selector-suspicion` (the sibling discipline for trusting a zero once
the selector itself is confirmed correct).
