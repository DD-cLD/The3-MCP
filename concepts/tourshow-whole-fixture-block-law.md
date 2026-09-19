---
id: tourshow-whole-fixture-block-law
title: "tourshow whole-fixture block law — per-fixture-family MAtricks block size ({LD} Strike M=14, our JDC1=12, QX80/QX40=5), tour-variable"
role: programmer
tags: [ma3, tourshow, matricks, phase-math, tour-variable]
when_to_load: "Before setting or retuning an XBlock/XShuffle value on any MAtricks pool object meant to read fixture-as-unit — block size is per fixture MODEL, not a universal constant, and should be expected to retune house-by-house as fixture types change on tour"
status: active
source: "findings/INBOX.md [0731-2cLD] 2026-07-31 (Dave, desk session post-v.67, SONG_C 1210 pool-level MAtricks retune); wraps/2026-07-31-song-b-heard-song-c-built.md 'Rulings banked'"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**Whole-fixture block law (Dave, ruled at the desk post-v.67):** for looks meant to read **fixture-as-unit** (the whole fixture moves/steps together, not cell-by-cell), the MAtricks block size is a **per-fixture-family number**: {LD}'s Strike M reads in **groups of 14** = whole fixture together; our **JDC1 blocks in 12s**; our **QX80/QX40 line blocks in 5s**.

**Fixed at the POOL level so binds inherit it automatically:**
- `144` → **`cLD SHUFFLE 5 B5`** (`XBlock=5 XShuffle=5` — QX40/QX80 whole-fixture shuffle).
- `145` **`cLD WING 2`** += `XBlock=12` (plates/JDC1 whole-fixture wings).
- NEW `146` **`cLD SHUFFLE 5 B4 W2`** (`XWings=2 XBlock=4 XShuffle=5` — the spots-verse look).

**Rationale for the Rivale retune (144→371):** the original MAtricks `144` now carries `B5` (QX40-sized blocks) — the wrong unit for Rivale fixtures. `371` **`Diamond Lite`** (`XWings=2 XGroup=3`, a pre-existing pool object) fits Rivale instead. Confirmed exactly right by Dave on readback.

**Generalization (Dave, explicit): block numbers are per-fixture-MODEL and TOUR-VARIABLE.** Expect block retunes house by house as fixture types change — this is not a one-time setting, it is a parameter that travels WITH the fixture inventory, not with the show.

**Future authoring rule:** propose `Block=<family number>` on any phaser/MAtricks sheet entry for a figure meant to read fixture-as-unit, rather than leaving block size implicit or copying another family's number.

**Readback method:** MAtricks Lua properties (`XBlock`/`XShuffle`/`XWings`/`XGroup`) read clean via handle indexing with a `pcall` guard; a `'None'` filter is needed on the walk. The SR-line-level MAtricks property name is `'MAtricks'`, valued as the string `'MAtricks N'`.

**Relation:** `matricks-store-time-embed-travels-with-preset-export` for how to read an INHERITED figure's block/wing/shuffle literals off its export rather than inferring them. `tourshow-seq1210-song-c-build-record` for the desk session this law was ruled in.


## PLINE joins the block-size table at 16 — 2026-07-31 [0731-3cLD]

SONG_D's MAtricks workup confirms **PLINE (P-Line) blocks in 16s** for
whole-fixture-as-unit reads — `B16` on a P-Line figure catches the WHOLE pixel line as a
single unit. PLINE joins the per-fixture-family block-size table: **QX40=5, JDC1=12,
PLINE=16** ({LD}'s Strike M=14 remains the non-cLD reference point). MX `147 SHUFFLE 5
B16` is the pool object carrying this (live-read `B16 S5`).


## ⭐ BLOCK LAW EXTENDED 2026-08-01 [0801cLD] — blocks can be FRACTIONAL, not only whole-fixture

**Dave ruled (on SONG_H): a block can legitimately be a FRACTION of a fixture's whole-block number, and the fraction is a deliberate spatial choice, not a translation error.** Example: **PLINE `B8` = .5 of the whole-fixture 16-cell block** — the half-fixture read IS the intention for that figure. So the per-fixture-family table this concept documents (QX40=5, JDC1=12, PLINE=16 — see also the PLINE=16 addition already in this file's `History:`) gives the WHOLE-fixture number; authoring a deliberate fraction of it (e.g. half) is a legitimate spatial choice to recognize when spec-reading {LD}'s figures, not evidence of a copy/translation error.

**Concrete instances from the same session:** {LD}'s `B8` on his CL/PLINE population was kept as-is on our side — `B8` (`MX 156 cLD S5 B8`). His `B14`/`B7` on JDC/Strike M crosswed to our `B12` (`MX 155`) — the whole-fixture number for our JDC1, per the existing table, since that particular figure was NOT a deliberate fraction.

**Consequence for future spec-reads:** when an inherited figure's block number doesn't match a fixture family's whole-fixture number from the table, check whether it divides cleanly (a plausible deliberate fraction) before assuming it is wrong or needs correcting to the whole-fixture number.

## Family number also rules an XGroup value, not only XBlock — 2026-08-05 [0805cLD]

**RULED (Dave), SONG_L MX 183:** the object binds `cLD QX40 COLOR`, so it takes
**`XGroup=5`** — our QX40's family number from the table above — **NOT {LD}'s `14`** (his
Strike M number), even though `183`'s spatial spec was matched off a Strike M/JDC1 population
of {LD}'s `Intro 1/1 Dim#6`. **The whole-fixture family number governs whichever attribute
carries the fixture-grouping intent on the object actually being built (XGroup here, XBlock
elsewhere) — key it to what the OBJECT binds, not to which {LD} population its spatial
numbers were spec-read from.** Full detail: `tourshow-seq2210-song-l-build-record`.


## Tour-variable, proven — the EU leg, 2026-08

The "expect this to retune house-by-house" caveat above was paid out in full across four venues in one week. The block number is a property of **the venue's fixture**, not of the show:

- venue plates at **14 cells** and tubes at **28** ⇒ mint `B14` / `B28` twins;
- venue units in **1-cell** modes ⇒ **strip Block and Group entirely** (the per-unit texture is automatic), keep wings, shuffle and phase ranges;
- a venue whose fixtures match the file's native cell count ⇒ **nothing to do**.

The doctrine, the selection-scoping rule, the reverse-map discipline and the per-venue receipts are at **`mx-cell-geometry-law`**; the kit that automates it is **`venue-adapt-macro-pattern`**.

History: extended 2026-08-28 (librarian, tour leg) — pointer to the cell-geometry doctrine the tour produced.
