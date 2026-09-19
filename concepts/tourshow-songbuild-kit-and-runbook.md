---
id: tourshow-songbuild-kit-and-runbook
title: "The per-song build line is a PROVEN kit, not a memory — generated/songbuild/ + SONG_BUILD_RUNBOOK_v0.1 regression-reproduce a shipped song byte-exact and drive every remaining build"
role: operational-live
tags: [tourshow, songbuild, automation, runbook, process, assembly-line]
when_to_load: "Before starting ANY remaining song's build — the kit and the runbook are the order of operations; also before hand-authoring anything the kit already emits, or before trusting a kit edit"
status: active
source: "wraps/2026-07-31-song-a-built-and-heard.md; WORKING/SONG_BUILD_RUNBOOK_v0.1.md; generated/songbuild/ [0731cLD]; extended findings/INBOX.md [0803-3cLD] 2026-08-04 (weighted notation: strict= kit gotcha on phaser branch)"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

After SONG_A went end to end, the mechanical half of the line was extracted into a kit so song #2 starts from tooling rather than recall.

## What exists

- **`generated/songbuild/cld_submap.py`** — the ratified {LD}->cLD map as data. **NAME-keyed**, because G-codes are assigned per prework sheet in order of use and differ per song; {LD}'s group NAMES are the stable join key. Also carries the dimmer ladder, position retargets, beam slots, the phaser template table, and the per-song numbering arithmetic.
- **`generated/songbuild/cld_songbuild.py`** — parse the prework sheet, read {LD}'s cue skeleton (carrying **every** fade attribute verbatim), `decode_phasers()` for the spec-read, emit sequence / aux / builder-macro XML, and a doctrine `lint()`.
- **`generated/songbuild/regress_ig.py`** — the proof.
- **`SONG_BUILD_RUNBOOK_v0.1.md`** (WORKING root) — the 9-step order of operations with the gated command chain and the ranked gotcha list.

## Why it is trustworthy: it is regression-proven, not merely written

`regress_ig.py` rebuilds SONG_A from the same inputs and **sha-matches all five artifacts that actually shipped to the console** (the 122-line main sequence and four aux sequences). **Re-run it after any kit edit — a kit that stops reproducing SONG_A is broken regardless of what it does on the new song.** This is the same discipline as diffing an authored artifact against a live golden, applied to the generator instead of the output.

## The scope limit is deliberate — keep it

The kit does the mechanical join. It does **NOT** pick phaser template classes, MAtricks binds, or speed gears; `decode_phasers()` hands over the spec (steps, baked speed as BPM, Measure, phase span, and whether rows are cell-level) and the call stays human. That boundary is `idea-file-design-programmer-boundary-doctrine` in tooling form: the mechanics ride along, the taste does not.

## First evidence it generalises

Dry-run against **SONG_B** (seq 1100, 212 live lines): **210/212 auto-resolvable**, one blocker (`All FX Color`, 2 lines, needs a ruling). Preset coverage complete after the dimmer ladder closed. **Dry-running the map before authoring anything is now step 1** — it costs two minutes and tells you exactly which rulings the song needs.

Relation: `tourshow-crosswalk-prework-alias-gap` (the prework the kit consumes) · `tourshow-seq1010-build-record` (the build it was extracted from) · `import-resolver-laws` (the laws its lint enforces).


## ns_emit.py: an XML-direct emit lane for a HUMAN-dialect prework sheet, no G-code section — 2026-07-31 [0731-3cLD]

**Prework sheets come in (at least) two dialects.** SONG_D's prework sheet is the
**HUMAN-dialect batch** (no G-code section) — unlike whatever prior sheet(s) carried a
G-code section for `parse_prework` to consume. For this dialect, **`ns_emit.py` builds
binds directly from `gb_s1300.xml`** ({LD}'s own export) under the **same live-SR parse
law** as the rest of the kit, rather than via the prework sheet's G-code section. Census
cross-checked **143 vs. sheet**, exact.

**Runbook note:** check which dialect a song's prework sheet is in **before** assuming
`parse_prework` consumes it — a G-code-section assumption will not hold for a HUMAN-dialect
sheet.

**Regression re-confirmed the same session:** after a 3-row submap patch, the SONG_A regression
(`regress_ig.py`) was re-run — **BYTE-EXACT 5/5** (main + 4 aux). The kit edit is proven
inert against the shipped golden, per this concept's standing "re-run after any kit edit"
discipline.


## Kit gotcha found 2026-08-01 [0801cLD] — asterisk-prefixed fixed-point values crash decode_phasers(), local guard in place ~~, permanent fix still owed~~ **FIXED, see 2026-08-05 note below**

**`gb_s1400.xml` (SONG_E) phaser embeds carry `*`-prefixed fixed-point values** (e.g. `Measure="*67108864"`) — the first file seen doing this. The kit's `decode_phasers()` crashes on a bare `int()` conversion when it hits one. **A local `lstrip('*')` guard was used to get through the session**, but this has not yet been promoted into the kit itself. ~~**Still owed: a permanent kit patch plus an SONG_A regression re-run** to confirm the fix doesn't disturb the byte-exact regression this concept's body describes.~~ **CORRECTED 2026-08-05 — the permanent fix is already in the kit; see below.**


## ⭐ SUBMAP DEBT PAID — L1 / LEDGER C7, 2026-08-03 [0803-2cLD]

**Root cause was subtler than a missing row.** All three Position presets flagged as ledger item C7 (`Position.I I`, `Position.Side Wash [Forte SW]`, `Position.Stage Wash [VL3600 + Strike M SW]`) were in `cld_submap.PRESETS_FIXED` **all along** — but keyed by the **prework-sheet ABBREVIATION** (`I_I`, `SideWashFSW`, `StageWashVL`), never by **{LD}'s FULL preset name**. The lookup missed silently every time a build resolved by full name, so every build patched the full names in **locally**, in a separate per-build dict, instead of hitting the shared fixed map. **A local patch applied N times is a missing row** — the map looked complete because each build quietly worked around the gap rather than failing loudly.

**Fix:** promoted all three full-name keys into `PRESETS_FIXED`; deleted `recipe_extract.LOCAL_PRESETS` (the per-build local patch dict) entirely. `PRESETS_FIXED` is now **29 rows**. SONG_A regression re-run after the patch: **BYTE-EXACT 5/5**, unchanged.

**Verified paid, not just patched:** a show-wide coverage re-run after the promotion found preset gaps drop **4 → 1**, and the one survivor (`Position.Release Relative`, SONG_H, 1 line) is not a gap needing a fix — it is the RELEASE EXEMPLAR (a Universal preset carrying `Relative="Specials:Release"`, bound by an ordinary StandardRecipe) that unblocks the STB (R) release work. Confirmed by the same script that originally found the debt.

**Relation:** `never-edit-the-golden-gate-behind-a-flag` (the sibling kit-integrity rule paid for the same session, same regression discipline) · `tourshow-stb-white-release-ruling` (the STB release work this submap fix unblocks).


## RUNBOOK v0.2 — per-song RUN LIST, ordered cheapest-first off the figure hash — 2026-08-03 [0803-2cLD]

**RUNBOOK v0.2 written, superseding v0.1** (`SONG_BUILD_RUNBOOK_v0.1.md`, referenced above under "What exists," is now superseded by v0.2). `NEXT_ACTIONS` was rewritten as the per-song RUN LIST (A0803.3), ordered **CHEAPEST-FIRST off the figure hash**:

SONG_N (0 new figures) → SONG_P (1) → SONG_K (1) → SONG_Q (2) → SONG_O (2, but 7 of the 9 remaining STB sites) → SONG_L (5) → SONG_M (5) → SONG_R/SONG_S last.

This front-loads the songs the figure hash made nearly free, so the first run session proves the line at low risk before spending effort on the expensive songs.

**LOCK EXIT CONTRACT met for everything not needing a console: 6 of 7 items closed, only L5 (mint the STB pair) needs the desk.**

**Relation:** `tourshow-stb-white-release-ruling` (L5, the STB pair this run list still owes the desk).

## Mark grid independently re-proves the submap promotion — 2026-08-03 [0803-2cLD]

The L7 Mark-cue position grid (`tourshow-mark-position-grid-flow-pass-signal`) re-proves the submap promotion (above, "SUBMAP DEBT PAID — L1 / LEDGER C7") works show-wide, independent of the SONG_A regression test: three preset names that would have printed blank now resolve to a cLD ref — `Side Wash [Forte SW]` (16 lines), `Stage Wash [VL3600 + Strike M SW]` (16), and `I I` (15) — **47 lines total** that previously printed `(no row)`.

**Relation:** `tourshow-mark-position-grid-flow-pass-signal` (the census this re-proof was read off).

## Kit gotcha found 2026-08-04 [0803-3cLD] — cld_songbuild.py:226 omits strict= on the phaser branch

**CONSTRAINING (G=0.7), scoped to a phaser targeting a wash: `cld_songbuild.py:226` omits
`strict=` on the phaser branch.** Same shape as the shared-path lesson already on file
(`parts-per-century-emit-pattern-and-et-gate`'s "protective transforms must live in the SHARED
emit path, not per-lane") — **patch the site locally until the shared path carries the fix.**
Still owed: promote the fix into the shared path and re-run the SONG_A regression, per this
concept's own "re-run after any kit edit" discipline.

## ⚑ STALE CORPUS NOTE CORRECTED 2026-08-05 [0805cLD] — the asterisk-prefix fix is already in the kit

The "still owed" note above (2026-08-01 gotcha) is **NO LONGER TRUE**. `cld_songbuild.py:106`
already carries `_fp = lambda v: int(re.sub(r'^[\\*\\?]', '', str(v)))`, handling `?` as well as
`*`. Confirmed against `gb_s2200.xml`, which carries **89,349** asterisk-prefixed attribute
values. No further action owed on this gotcha.

## Kit gotcha found 2026-08-05 [0805cLD] — `mx_of()` substring matching is a latent trap, patched

**Emitter fragility (smith F6): `mx_of()` dispatched on `'US' in sel`**, which also matches
`Forte US (Grid)` and `Strike M US [STB] (Lin)` — correct only by accident of the SONG_L
`Intro` figure having exactly three populations. **Replaced with exact population-name tests
that raise on anything unexpected.** Substring tests on {LD} group names are a latent trap;
use exact names and fail loud — same shape as the shared-path lesson already on file for the
`strict=` gotcha above.
