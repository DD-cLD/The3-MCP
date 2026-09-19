---
id: tourshow-stb-white-release-ruling
title: "RULED: keep JDC1 US [STB] — every use needs a (W) white colour preset + an (R) release; the QX40-STB expansion has been binding the wrong colour"
role: programmer
tags: [stb, qx40, jdc1, release, crosswalk, tourshow]
when_to_load: "Before authoring, censusing, or correcting any JDC1 US [STB] site on any {TOUR} song — the ruling, the value-dependent expansion mechanic, the show-wide census, and the release-mapping rule"
status: active
source: "BACKLOG.md 2026-08-03 [0803-1cLD]"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**RULED (Dave) — KEEP `JDC1 US [STB]`. Every use needs a (W) WHITE COLOUR PRESET and an (R) RELEASE.** Reason: STB's actual intent is a **WHITE STROBE look**, and the strobe channel returns to open on default or Release. **This supersedes an earlier Dave-floated "maybe safer to drop STB" idea** (his physics for the float: strobe channels on QX40/pixel lines start at default open, and default-or-Release returns them open, so on our rig the RGBW LED intensity drives both his RGB and STB lines — programming both looked like a duplicate intensity drive). The float did not survive the census below; **file the ruling, not the float.**

**Consequence: the QX40-STB expansion has been binding the WRONG COLOUR.** It puts the SONG BASE colour where white belongs.

## The value-dependent expansion mechanic (never written down before this)

A **CONTENT value expands 1 line -> 4**: `QX40 MM ALL @ Dimmer.Full` + the content, `QX40 COLOR @ Dimmer.Full` + the base colour — the MM engine carries the figure, the COLOR engine is opened so the strobe cell reads. But **`Dimmer.0` stays 1 -> 1** (`QX40 MM ALL` only — nothing to open on an off line). SONG_J example: 9 STB sites = 4 content (×4 lines) + 5 off (×1 line) = 21 lines, +12 over source. **Anomaly, flagged not changed:** aux 2012 does NOT apply this expansion — {LD}'s `JDC1 US [STB] @ Dimmer.50` shipped as ONE line where the main sequence would have made four; `SONG-J_WORKUP v0.1` called the expansion out as needed in the aux and it did not land (tracked on the MELD AUX tab).

## Show-wide STB census (the numbers that made the drop decidable)

**64 `JDC1 US [STB]` lines show-wide.** Cues where STB and RGB BOTH carry content (the actual duplicate-drive gotcha) are only **8**: SONG_A 9 · SONG_D 6, 12, 14.1 · SONG_L 12.1 · SONG_O 7, 11, 18. Cues where **STB is the ONLY thing driving the QX40** number **21**, across 7 songs (SONG_D 9, SONG_J 4, SONG_O 4, SONG_C/SONG_E/SONG_I/SONG_Q 1 each). A blanket drop would have silenced the QX40 at 21 cues to fix 8 — hence the surgical ruling above, not a drop.

**The 8 STB/RGB collisions are not one shape:**
- **3 harmless** (SONG_O 7/11/18): RGB and STB carry the SAME phaser — one target, one line is a pure simplification.
- **3 real level conflicts**, {LD} driving the two emitters at different levels on purpose (SONG_D 6 & 12: RGB Full vs STB Dimmer.50; SONG_L 12.1: RGB Full vs STB Dimmer.20) — collapsing picks a level and loses his intent.
- **2 different FIGURES on the two emitters** (SONG_A 9; SONG_D 14.1 runs Chorus STB Sine against Verse RGB Sine, and the cLD build already preserves this correctly as `cLD QX40 MM ALL`=Chorus / `cLD QX40 COLOR`=Verse) — collapsing picks a figure.
Only the first group is mechanical; the other two need per-site judgment.

## (W)+(R) correction surface, censused show-wide

**29 STB content sites total, 18 already in built songs** (SONG_D 12, SONG_J 4, SONG_E 1, SONG_I 1) **and 11 in songs not yet built** (SONG_O 7, SONG_A / SONG_C / SONG_L / SONG_Q 1 each). Two sub-shapes:
- **(a) 8 sites where the expansion fired and bound the song base colour** — SONG_D 3.1/4.1/10.1/14.1 carry `cLD NS DEEP BLUE`; SONG_J 8.1/10.1/15.1/23.1 carry `cLD FR COBALT BLUE`. These are actively wrong and want white.
- **(b) 21 sites that are plain STB dimmer levels** (`Dimmer.50`/`30`/`20`) which crosswalked 1:1 to `cLD QX40 MM ALL` with no colour and no release at all — these need (W)+(R) added from nothing.

## Release mapping, RULED (Dave)

JDC1 needs a **Dim 0 cue after the STB is used** so output returns to default. **For US, the QX40 runs double duty, so (R) RELEASE IS THE PREFERRED NEXT CUE instead.** This settles the release map: at the **13 sites** where {LD}'s very next cue already carries `JDC1 US [STB] @ Dimmer.0`, that line becomes a **RELEASE on our side — a substitution, not an added line.** At the **8 sites** where the STB re-fires on the very next cue, no release belongs there at all.

**The release dialect itself needs no new authoring** — see `release-relative-universal-preset-exemplar-proven`: an (R) is an ordinary StandardRecipe bound to a preset whose content is `Specials:Release`, not a new recipe dialect.

## ⚑ Open items — not yet resolved, need a human/Dave call

1. **HOW the (R) release is expressed on the line** — release on the following cue, a part-level release inside the strobe cue so it self-clears, or a `Release` value on the recipe line itself. Standing dialect rule applies regardless: export a live golden before hand-authoring a release-carrying recipe line, since no full exemplar for the STB case specifically exists in the corpus yet.
2. **WHICH white** — one show-wide `cLD STB WHITE` minted once and referenced at all 29 sites, or each song's own white preset. **Genuinely undecided as of this backlog** — do not assume a specific slot address for this preset until Dave rules and it is read live off the console.
3. **Related, still-open pattern question (cue 23.1 of SONG_J):** Dave removed `cLD QX40 MM ALL @ Dimmer.Full` (an expansion line) and `cLD QX40 COLOR @ Dimmer.0` ({LD}'s own line, which fought the expansion's `Dimmer.Full`) — reading as "when the MM engine also carries a phaser, the expansion's `Dimmer.Full` is redundant." The same pattern still stands **unedited** at SONG_J cues 8.1, 10.1 and 15.1 (`QX40 MM ALL` carrying `Dimmer.Full` + `Swell Sine 2`). If this is a rule it belongs in the emitter and those three want the same treatment; if 23.1 was a one-off taste call, leave them. Not resolved — needs Dave's call.

**Relation:** `source-matricks-wrapper-recipe-encoding` (the `Strike M US [STB] (Lin)` wrapper alias this population is also known by). `release-relative-universal-preset-exemplar-proven` (the release-dialect mechanism). `master-default-doctrine` (a related but distinct "flow from the children" ruling — masters, not STB).


## ⭐ OPEN ITEM 2 CLOSED by cLD, 2026-08-03 — R5: ONE show-wide `cLD STB WHITE` at slot **4.83**

The librarian correctly refused to invent this: the slot number is **not in `findings/INBOX.md`**, so it
was not in that run's corpus. It is nonetheless **ruled**, and it lives in three tier-1 artifacts written
the same day:

- `CURRENT_STATE_A0803.1.md` ruling **R5** — "One show-wide `cLD STB WHITE` → **4.83**."
- `TOURSHOW_LOCK_AND_RUN_PLAN_v0.1.md` R5 — "**One show-wide `cLD STB WHITE`**, not a per-song white.
  Slot **4.83** (verified free live: **78-82 taken, 83+ clear**)."
- `TOURSHOW_CORRECTIONS_LEDGER_v0.2.md` C3 — "`cLD STB WHITE` → slot **4.83** (verified free)."

So: **one white, show-wide, at 4.83, referenced at all 29 sites** — not a per-song white. Open item 2
above is settled; items 1 and 3 stand.

**The process lesson is the durable half, and it is a filing defect, not a librarian error:** a ruling
that lands only in a state/plan/ledger file and never in `findings/INBOX.md` **is invisible to the
librarian and therefore never reaches the corpus.** State files are rehydrated and archived; the corpus
is what survives. **Any ruling written into a state, plan, or ledger file must ALSO get its one raw line
in the INBOX**, or the next spine regeneration silently drops it. Caught here because the librarian
flagged the discrepancy instead of inventing the number.


## ⛔ STANDING RULE — FILING DEFECT FOUND ON THIS CONCEPT, 2026-08-03 [0803-2cLD]

**This concept is itself the paid-for case.** R5 (`cLD STB WHITE` → slot 4.83, verified free, sites 78-82 taken / 83+ clear) was ruled and recorded in `CURRENT_STATE_A0803.1`, `TOURSHOW_LOCK_AND_RUN_PLAN_v0.1`, and `TOURSHOW_CORRECTIONS_LEDGER_v0.2` (ledger item C3) — but it never got a `findings/INBOX.md` line, so it was invisible to the librarian, which correctly refused to invent it rather than file a ruling it had never been shown.

**STANDING RULE: any ruling written into a state file, a plan, or a ledger must ALSO get its own raw line in `findings/INBOX.md`, or the corpus never sees it.** State files get archived; the corpus is what survives. Writing a ruling only into a working document is not filing it — filing means putting it on the librarian's actual input surface. cLD patched this concept by hand this session as the immediate fix; this note generalises it into the standing rule for every future ruling.

## STB EXPANSION IS VALUE-DEPENDENT, 2026-08-03 [0803-2cLD]

The prework-sheet STB expansion note is **value-dependent**, not blanket: a **CONTENT value** (a real colour, not black/off) expands **1→4** lines and needs both **(W)** white and **(R)** release per R3; **`Dimmer.0`** (already off) stays **1→1** and needs **neither**. First pass labelled every STB line as needing (W)+(R) regardless of value, which would have overstated the correction surface by **2x**.

**STB CONTENT sites in the remaining (unbuilt) songs = 9** — SONG_O 7, SONG_L 1, SONG_Q 1. This reconciles exactly with corrections-ledger item C3's 11-site figure for all unbuilt songs, minus the 2 songs it also covered that are already built (SONG_A, SONG_C).

**Relation:** ledger C3 (`TOURSHOW_CORRECTIONS_LEDGER_v0.2.md`) carries the full 29-site release/white map and the 13/8/8 release-disposition split (R4).

---
**⚑ Librarian note (not part of the concept body — for cLD, remove before or on apply):** this run could not confirm `tourshow-stb-white-release-ruling` exists in the accessible `concepts/SPINE.md` snapshot (grepped, zero hits — see RUN_REPORT.md). Writing this amendment on the dispatch brief's explicit word that cLD hand-patched it live this session. If the file does not in fact exist at apply time, promote this content into a new concept instead of appending it.


## STB correction sheet generated, per-site — 2026-08-03 [0803-2cLD]

**`generated/desk_pack/STB_CORRECTION_SHEET.csv` generated: 29 content sites — matches ledger C3 exactly — 20 in built songs, 9 in songs to build.** Release disposition per R4: **12 SUBSTITUTE / 9 ADD / 8 NO-RELEASE.**

**⚑ One-site discrepancy vs. ledger C3's 13/8/8 split** — totals agree at 29, but one site classes differently between the two sheets. This sheet takes the **STRICT reading**: the next cue must carry `JDC1 US [STB] @ Dimmer.0` specifically for a site to count as a SUBSTITUTE. Not reconciled against ledger C3 as of this filing; both numbers stand until a human resolves which site classes correctly.

The per-site sheet names every site individually, so the discrepancy — and the whole correction surface — resolves at previz on one look.

**Relation:** ledger C3 (`TOURSHOW_CORRECTIONS_LEDGER_v0.2.md`, the 13/8/8 figure this sheet's 12/9/8 disagrees with by one site).


## ⭐⭐ (W)+(R) OBJECTS NAMED AND SPECCED — both remaining ⚑ answered, 2026-08-03 [0803-2cLD]

**RULED (Dave).** Final names: **(W) `cLD LED WHITE`** · **(R) colour `cLD LED (R)`** · **(R) beam `cLD RATE (R)`** (`cLD ` prefix confirmed against the standing namespace law — see `cld-sandbox-and-namespace`). **Collision-checked against {LD}'s pools show-wide: zero exact matches** — the silent `#2` auto-suffix trap (`cld-sandbox-and-namespace`) will not fire on any of the three.

**⚑ Naming note, flagged not asserted:** this appears to be the same object OPEN ITEM 2 (below) closed as `cLD STB WHITE` at slot 4.83 (R5) — same slot, a different name now on file. Treat **`cLD LED WHITE`** as the name of record going forward; `cLD STB WHITE` was the working label carried in the state/plan/ledger files R5 was sourced from. This correspondence is a librarian inference from the slot match (4.83), not an explicit renaming statement in the source line — worth a console-side confirm.

**Slots:** **4.83** = (W) `cLD LED WHITE` · **4.84** = (R) colour `cLD LED (R)` (pairing inferred from listing order and consistency with R5's 4.83; both verified clear — 78-82 taken / 83+ clear). ~~**Beam slot UNKNOWN** — {LD} occupies **Beam.1 Open / .2 RateFast / .3 RateMed / .4 RateSlow**, so `cLD RATE (R)` has no home yet. Needs **one console read**, alongside the still-open QX40 strobe attribute name (see `release-relative-universal-preset-exemplar-proven`) — **two reads, one visit.**~~ **Corrected 2026-08-05 — CLOSED at Beam 5.8, see bottom of file.**

## ⭐ OPEN ITEM 1 CLOSED (Dave) — the (R) is a PAIR, not one preset, 2026-08-03 [0803-2cLD]

**Answers "HOW is the (R) expressed."** The QX40-STB expansion drives BOTH the MM/colour engine and the beam rate, so a release takes **one release preset in EACH pool the expansion touches**: a colour release (`cLD LED (R)`) and a beam release (`cLD RATE (R)`). The `Position.Release Relative` dialect (`release-relative-universal-preset-exemplar-proven` — a Universal preset carrying `Relative="Specials:Release"`, bound by an ordinary StandardRecipe) still applies to each — the same mechanism, used twice, not a new dialect. This is more than the corpus held before this ruling.

## ⛔ SCOPED EXCEPTION TO A HARD RULE, RULED AND RECORDED IN THE FOREGROUND, 2026-08-03 [0803-2cLD]

**All three objects above store GLOBAL, not `/Universal`.** Dave: *"global so only our QX40 look at it."* A scoped, deliberate exception to the standing `/Universal`-on-every-store law — see `universal-presets-emitter-aware` for the exception recorded against the rule itself and why the rule's purpose is served, not broken, here. Already written into `cld_submap.py` and `CARD_AUTHORING.md` so a future session does not "correct" it back to Universal. Carried caveat, not a blocker: the Global-anchor portability verify item still applies in principle, but the QX40 is cLD's own floor fixture and travels with the show.

## ⭐ OPEN ITEM 3 NARROWED — cue 23.1 pattern settled as ROUTING, not a rule, 2026-08-03 [0803-2cLD]

**RULED (Dave) — SONG_J is on the clean-up pass.** This settles open item 3 (below) as a **routing call**: the `Dimmer.Full`-beside-a-phaser question at SONG_J cues 8.1/10.1/15.1 is handled **per-site by eye** in the clean-up pass, does **NOT** enter the emitter, and **no other song inherits it**. Ledger C4 + C5 both re-routed. **The general question — is `Dimmer.Full` beside a phaser always redundant? — stays open**, simply not generalised off SONG_J. SONG_J's own build record: `tourshow-seq2010-song-j-build-record`.

## Open items, re-stated 2026-08-03 [0803-2cLD]

Of the original three ⚑ below: item 2 (white naming/slot) closed same day, earlier session; item 1 (HOW the (R) is expressed) closed above; item 3 (cue 23.1 generalization) narrowed to routing above. **Genuinely still open:**
1. ~~**Beam slot for `cLD RATE (R)`** — needs one console read ({LD} holds Beam.1-4, see above).~~ **CLOSED 2026-08-05 — Beam 5.8, see bottom of file.**
2. **QX40's own strobe attribute name** — needs one console read, same desk visit as the beam slot. **Still open as of 2026-08-05** — this was the one console read NOT answered by the beam-slot visit.
3. **Not song-j-scoped:** is `Dimmer.Full` beside a phaser always redundant, in general? Stays open.


## cLD resolves the two inferences the librarian flagged — 2026-08-03 [0803-2cLD]

The pass-4 librarian correctly refused to assert two things the backlog did not state.
Both are cLD's to settle, and both are settled here:

1. **`cLD LED WHITE` IS the object R5 called `cLD STB WHITE` — it is a RENAME, not a
   second object.** R5 ruled "one show-wide white for all 29 STB sites" and verified
   4.83 free; Dave later named the actual objects `LED White` / `LED (R)` / `Rate (R)`.
   Same object, same one-show-wide intent, Dave's name. **`cLD STB WHITE` is a dead
   placeholder — do not mint it.**
2. **The 4.83 → (W) / 4.84 → (R)-colour pairing is cLD's ASSIGNMENT, not Dave's
   ruling.** What Dave ruled is the names and the store mode; what R5 verified live is
   that 78-82 are taken and **83+ is clear**. Which of the two clear slots takes which
   preset is arbitrary and may be re-picked at the desk without breaking anything —
   nothing binds them by slot, every bind is by name.

~~**Still genuinely unknown and needing a console read: the Beam pool slot for
`cLD RATE (R)`.** {LD} occupies Beam.1 Open / .2 RateFast / .3 RateMed / .4
RateSlow. Read it on the same desk visit as the QX40 strobe attribute name.~~
**CORRECTED 2026-08-05 — see the closing section below.**


## ⭐⭐ BOTH REMAINING CONSOLE READS ANSWERED — BEAM SLOT CLOSED, 2026-08-05 [0805cLD]

**`cLD RATE (R)` is programmed at Beam `5.8`** (pool "Beam", slot 8) — closes the "Beam slot
UNKNOWN" open item above ({LD} held Beam.1-4). This was one of the two console reads that
had been owed; **the QX40's own strobe attribute name is the remaining open read.**

**All three (W)+(R) objects the R7 correction pass needs now exist:** `cLD LED WHITE` 4.83 ·
`cLD LED (R)` 4.84 (colour, both already on file above) · `cLD RATE (R)` Beam 5.8 (beam, new).
Storage mode Global for all three, consistent with the scoped exception already ruled on this
concept.

## R7 (W)+(R) correction pass — UNBLOCKED, and SONG_L adds 2 sites, 2026-08-05 [0805cLD]

With the STB trio closed (above), **the R7 (W)+(R) correction pass is unblocked.** SONG_L
contributes **2 sites** to the surface: main sequence cue 12.1 (`Dimmer.20`) and aux 2213
(`JDC1 US [STB] @ Dimmer.30`) — both plain STB dimmer-level lines shipped 1:1 with no colour
and no release, matching shape (b) above ("21 sites that are plain STB dimmer levels... need
(W)+(R) added from nothing"). The aux site matches the SONG_J aux 2012 precedent: the
expansion does not fire in an aux there either. Both logged, not fixed, in
`tourshow-seq2210-song-l-build-record`.

**⚑ Librarian note on the running total:** the last count on file in this concept's own body
("Show-wide STB census" section above) is **29 STB content sites**. State tracking outside
this concept (`CURRENT_STATE_A0805.1.md`) carries the surface at **34** after SONG_L's +2
— i.e. it was already at **32** before this session, per that same state file. That 29→32 step
happened in some earlier session but, per this concept's own STANDING RULE above ("any ruling
written into a state file... must ALSO get its own raw line in `findings/INBOX.md`, or the
corpus never sees it"), it never reached `findings/INBOX.md` and so was never available to any
librarian run to file into this concept's own body. **This concept's own 29-site figure is
therefore stale and the corpus does not currently hold the intermediate 29→32 evidence** — a
repeat instance of the exact filing-defect this concept already documents about itself, not a
new kind of miss. Flagged for a human/cLD decision: backfill the missing 29→32 step (find its
source and file it), or accept the state file as the count of record going forward.

**[0805-2cLD] EXTENSION — emitter scoping law:** the (W) white is a BLANKET law (all correction-sheet rows want it); the (R) release is a PER-SITE disposition — ADD 9 / SUBSTITUTE 12 / NO RELEASE 8 — so any blanket release rule is wrong at 8 sites by construction. First patch cut emitted (R) at every Dimmer.0 STB site; the SONG_A byte-exact regression refused it (122→124 SRs); content-sites-only scoping restored 5/5. The direct-value STB branch gap WAS the correction sheet: all 21 "no colour bound at all" rows were direct-value sites the old emitter shipped bare. **Console-vs-corpus naming (live read):** 4.83 = "QX40 Only W" · 4.84 = "QX40 Only W (R)" · Beam 5.8 = "QX40 STB (R)". None carry the cLD prefix. Slot-form binds unaffected; a census-by-NAME searching corpus names reads ZERO. Fix the corpus, not the console.

History: extended 2026-08-05 [0805-2cLD] — (W) blanket / (R) per-site scoping; content-sites-only emitter restored SONG_A 5/5; direct-value branch gap explained the 21-row correction sheet.
History: corrected 2026-08-05 [0805-2cLD] — live console names for the trio (QX40 Only W 4.83 · QX40 Only W (R) 4.84 · QX40 STB (R) Beam 5.8) replace corpus names; census by NAME must use the live names.
