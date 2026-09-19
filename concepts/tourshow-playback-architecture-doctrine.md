---
id: tourshow-playback-architecture-doctrine
title: "{TOUR} playback architecture: executors 1-15 + 101-115 are the portable envelope (console-portability doctrine); each song = ONE theatrical cue stack headed by a SET cue, all layers tracked inside it, every cue a TC-fired Go"
role: programmer
tags: [tourshow, doctrine, v2.4, timecode]
when_to_load: "Before architecting any song's sequence/executor structure — the executor budget, the SET-cue-first pattern, and the TC-fired-Go default this show is built on"
status: active
source: "findings/INBOX.md 2026-07-21 (07-21 song-g-infra, Dave, dictated); wraps/2026-07-20-days-programming-bridge.md RESUME HERE section"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**Executor envelope — portability doctrine (Dave, dictated):** the whole show (SONG_G, and by extension every song) lives on executors **1-15 + 101-115** ("that whole section") — nothing outside it. This is deliberate: it keeps the show portable to a **SMALLER or OTHER MA console** that might be encountered at a festival stop (Dave: likely a couple of stops on the tour will have this constraint). This extends the inheritable-file doctrine (`tourshow-mission-and-handoff`) from pools/recipes down to the **playback layout** itself — executor budget is now part of what "inheritable" means. Note: as of 2026-07-21, executors 1-15 are **not actually instantiated** on the Mac onPC build machine (see `executor-1-15-not-instantiated-mac-onpc`) — that's a separate BUG from this ARCHITECTURE RULE; builds currently land on the 101+ scratch bank and must be re-mapped to 1-15 before the tour desk.

**Theatrical cue-stack pattern, per song (Dave, dictated, "SONG_G ARCHITECTURE RULED"):** **ONE sequence per song** (e.g. "cLD SONG_G" on a single executor) — everything tracks **INSIDE** that one sequence. There is no separate KEY/BAND/BREATHE/FIELD layer-master; those layers live as tracked content **within the cues themselves**. **Every cue is a TC-fired GO** by default (a song like SONG_G is "all Goes, no follows") — the TC list is a plain sequence of CmdEvents, one Go per cue, matching the Export Timecode schema (`export-timecode-tc-event-xml-schema`).

**SET CUE heads every stack (Dave — "basic lighting 101," a foundational miss the first time through):** Cue 0 "SET" is a preset/blocking cue that **positions the whole rig** — movers pre-pointed for cue 1 AND for anything later cues will need, so nothing swings visibly on-look — **loads the gut color**, and has the **base intensity ridden up, written into it**. Every subsequent cue **tracks from SET**. Worked example (SONG_G): SET → AIR → INTRO → VERSE1 → CHORUS2 → MID8 → CHORUS3 → DESCENT → OUT (+ a slide-pop bump, see below).

**Button-bump exception (Dave, general playback doctrine, dictated):** rhythm/repetitive flash effects that read better **timed on a button** get built as a bump on a dedicated button executor instead of a run of TC-fired cues — but the button push is **still entered into the TC list as an event**, so one reusable bump can be fired many times by TC without writing a thousand near-identical cues for a repetitive flash. Some cues on more complex songs may be **Follows** instead of TC time-events, while still being driven by the overall TC window. SONG_G itself is all Goes plus the one slide-pop bump.

**Relation:** `tc-bump-button-architecture` for the bump-executor mechanics (Release-not-Off exit, Output Filters). `export-timecode-tc-event-xml-schema` for the CmdEvent/Go schema this pattern authors against. `tourshow-showfile-architecture` for the higher-level show-file model (monolithic file, macro-order setlist) this playback pattern nests inside.

## ⭐ CUE-DECIMAL PHRASE ENVELOPE (Dave, 2026-07-28) — four parts per section

Measured against the SONG_T export, {LD}'s existing convention is **whole number = the
LANDING · `.1` = the TRAVEL between landings** (20 of 27 whole-number cues are empty and merely
track; the 7 that carry content are exactly the impact moments — Mark, Prechorus, Chorus, Stab,
Chorus, Stab, Break. Line split: 39 in whole numbers, 66 in `.1` decimals).

**Dave extends it with further decimals of the SAME whole cue for the recovery:**

| Part | Job |
|---|---|
| whole `N` | **LAND** — the hit / state change |
| `N.1` | **TRAVEL** — movement, the mask layer, voice-leading into the next landing |
| `N.2` | **CLEAR** — bring intensity back to zero |
| `N.3` | **RESET** — a Release so movers return home UNSEEN, pre-positioned for what follows |

Recipes the whole way through. **This is the SET cue's job done locally, per section, rather
than only once at the top** — and musically it is the rest at the end of a phrase, the clear-out
that lets the next phrase start from silence instead of leftovers. See
`cue-structure-is-tonal-harmony` for the frame this sits inside, including the anacrusis rule
(start the movement BEFORE the cue it lands on).
History: none — architecture ruled in one session, 2026-07-21, digesting the 07-21 song-g-infra INBOX block plus the matching RESUME-HERE build runbook in `wraps/2026-07-20-days-programming-bridge.md`. Consolidated by the librarian (2026-07-23 digest) from two closely-related INBOX rulings (executor-budget portability + theatrical-stack/SET-cue architecture) into one playback-architecture concept. Extended 2026-07-28 [0727-2cLD] with Dave's four-part cue-decimal phrase envelope (LAND/TRAVEL/CLEAR/RESET), measured against the SONG_T cue census.
