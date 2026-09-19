---
id: tourshow-showfile-architecture
title: "{TOUR} show-file model — monolithic file, macro-order setlist, manual TC-arming trigger per song"
role: programmer
tags: [tourshow, ma3]
when_to_load: "Before building or reasoning about the {TOUR} show file's macro/executor structure, or before exporting a multi-song QCaller sheet"
status: active
source: "MEMORY §Bird's Eye tour — team, routing, file architecture, LTC — Show-file architecture (Dave's model — treat as ground truth), 2026-07-02 evening; findings/INBOX.md 2026-07-06 + wrap 2026-07-07-beatgrid04-festival-tc"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

Dave's model — **treat as ground truth**:

- The show file is **monolithic**; it never gets cut per set. **Setlist = macro call order.**
- A song's macro is a **manual trigger** Dave fires in the groove between songs: it loads the song's page and **arms TC listening for that song's window**. TC runs continuously throughout the show.
- **No end-of-track chaining** → any song can follow any song; set-length variants are just shorter call lists (near-zero compile cost — no re-linking needed).
- **Multi-song QCaller export should mirror this:** one file = one show = calls in order, per-song TC offsets.

This model directly informs the executor model in `tourshow-tour-identity` (one busk page + one page per song; one TC-fired master executor per song).

**{FESTIVAL} predecessor evidence (2026-07-06, strings-verified on {LD}'s file):** {LD}'s per-song architecture used a **rhythm bump layer** — e.g. Kick 1 (SONG_H/SONG_B/SONG_L/SONG_J/SONG_E×2/SONG_C), Snare 1 (SONG_A/SONG_N/SONG_D/Sattelites[sic]/SONG_I/SONG_K), Clap/Jersey Clap, plus `"Intro 1/1 (Kicks In)"`, bare-title song sequences, and SPEEDMASTER×9. **Timecode strings are trace-level only ⇒ likely manually bumped, not TC-run (interpretation).**
**⛔ DISPROVEN 2026-07-27 [0727-2cLD] — superseded in place, kept for the record.** All 19 Gov
Ball song timecodes were exported and parsed: **the bumps ARE in the timecode**, as
`Temp`/`Temp(Release)` event pairs on dedicated sub-layers (SONG_E carries 422 events on a
single layer; SONG_M 872 across four). The trace-level strings were a weak signal read
too confidently. Only the AUTHORING METHOD remains open — **Dave's theory (a theory, not a
fact) is that a plugin wrote the press/unpress pairs**, which fits both the volumes and the
fact that {LD} already ships a 253-line Lua engine. If true, we can generate ours the same
way: `export-timecode-tc-event-xml-schema` is fully cracked and `tc-bump-button-architecture`
already reserves the file-side generation seam. That makes {LD}'s file evidence FOR the "recorded bumps" model that Dave's executor design explicitly moves away from (`tourshow-tour-identity`'s executor model: "hits authored on the grid, not recorded bumps") — **the {TOUR} tour TC model is a re-architecture of {LD}'s approach, not a port of it.** {LD}'s bump vocabulary maps 1:1 onto Beatgrid's stem-lane markers (kick/snare lanes → bump moments) — see `beatgrid-stem-sections-feature`; the tour-file-archaeology and beatgrid-build workstreams converge here.

**{COLORIST} confirmed (2026-07-08): {FESTIVAL} programming was "overly simple because they didn't have a lot of time"** — {LD}'s file is a time-constrained output, not a statement of design intent or a ceiling to live up to. Practical read: the bump vocabulary above stays useful reference (see `beatgrid-stem-sections-feature`), the file's colors stay intel-only (see `show-direction-doc-and-color-sync-workflow`), and there's no "ghost standard" the current rebuild owes it.

History: none — recorded 2026-07-02 evening as Dave's explicit architectural decision. 2026-07-06: {FESTIVAL} predecessor evidence added — {LD}'s system used manual/recorded bumps (trace-level TC strings only), confirming Dave's model is a re-architecture, not a port; see `festival-showfile-save-lineage` for the file's save history. 2026-07-08: {COLORIST} (de facto CD) confirmed {LD}'s {FESTIVAL} programming was time-constrained, not a design ceiling — reinforces the re-architecture read with a direct human source. 2026-07-16: `tc-bump-button-architecture` refines the executor model — dedicated bump executors ride parallel lanes alongside the main sequence's TC-fired lane, triggered by typed TC events, exiting via Release not Off. 2026-07-27 [0727-2cLD]: the 2026-07-06 "likely manually bumped, not TC-run" interpretation is DISPROVEN by a full 19-song TC export parse — the bumps are TC-run; only how they were authored is open.
