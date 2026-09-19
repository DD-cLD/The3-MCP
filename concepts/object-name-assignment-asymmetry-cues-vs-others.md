---
id: object-name-assignment-asymmetry-cues-vs-others
title: "⛔ Renaming by Lua is asymmetric: on a CUE, direct .Name= SILENTLY FAILS and :Set('Name',…) works — groups, sequences, appearances, images and macros all accept .Name= fine"
role: programmer
tags: [ma3, lua, cues, v2.4, gotcha, tourshow]
when_to_load: "Before renaming any object from Lua — cues are the exception and fail silently, so a rename batch that mixes object classes needs the Set form for its cue members"
status: active
verified: grandMA3 onPC 2.4.2.2 (Mac), EU tour leg 2026-08
source: "findings/INBOX.md [0812-2cLD] 2026-08-12 — cue 19 spelling fix on the automator sequence; corroborated [0812-3cLD] (macro .Name= works)"
supersedes: []
superseded_by: null
---

| Object class | `obj.Name = "x"` | `obj:Set('Name', "x")` |
|---|---|---|
| **Cue** | ❌ **silent failure** | ✅ works |
| Group | ✅ | ✅ |
| Sequence | ✅ | ✅ |
| Appearance | ✅ | ✅ |
| Image | ✅ | ✅ |
| Macro | ✅ | ✅ |

**The silent half is the problem.** A cue rename by direct assignment reports nothing and changes nothing, so a mixed rename batch appears to succeed while leaving its cue members untouched — and cue names are load-bearing, because timecode events address cues **by name** (`automator-tc-architecture`, `tc-track-target-cutover`).

**Attested fix:** the hand-added automator cue read `In _N_OUT` with `CMD Go+ Macro "SONG_S"`. Corrected via `:Set('Name', 'SONG_S')` plus the CMD respelling, and verified by readback. **Exact-spelling law** applies throughout that chain — the whole song-fire path resolves by exact token, no case-insensitivity bets (`speedmaster-name-token-exact-match-gotcha`, `name-token-single-holder-cutover-law`).

**Standing lane:** any future cue relabel — the `[Release]` relabels parked on the trick sequences, for instance — uses `:Set('Name', …)` and reads back.

**A related silent no-op in the same family:** a **macro-LINE handle's `:Delete()` also silently no-ops** (an empty line left by a PSR import survived every attempt). Macro *objects* rename fine; macro *lines* do not delete from the wire — leave them for the desk when the macro is critical.

**Relation:** `cue-names-not-round-trip-stable-content-derived-labels` (the other cue-naming trap: auto-labels derived from content) · `set-command-unknown-property-fails-silently` · `macro-cli-creation-and-edit-lane` · `name-token-single-holder-cutover-law`.

History: none — found and fixed 2026-08-12; macro-line `:Delete()` no-op corroborated 2026-08-12 the same arc.
