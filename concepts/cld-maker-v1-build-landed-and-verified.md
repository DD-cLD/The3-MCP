---
id: cld-maker-v1-build-landed-and-verified
title: "cLD MAker v1 BUILD LANDED and confirmed WORKABLE live on Dave's screen — SONG_G session loads clean; plan pivots to program-a-song-first"
role: tools
tags: [tourshow, cld-maker, process]
when_to_load: "Before asking whether cLD MAker v1 has actually been built, what it currently does, or what the next working session's plan is"
status: active
source: "findings/INBOX.md, 2026-07-17 [0717-3cLD] (cLD viewed live on Dave's screen via computer-use)"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**Build landed and confirmed workable.** Sandbox at `/Users/{USER}/cld_maker_sandbox/beatgrid.html`. The SONG_G session (22 events, `09_SONG-G 06.01.26.wav`) loads clean. Codex built the spec faithfully — see `cld-maker-identity-rename-and-scope` for the spec pack this build executes.

**What's in the build:**
- Waveform/energy/section timeline (beatgrid retained)
- **Cue strip** — one cell per `qcue:true` event (AIR/INTRO/VERSE1/CHORUS1.../OUT), each with TC + label + "add recipe"
- **Cue inspector** on click — Device hint shown ("display only · never auto-fills"), Sequence/Cue/Part, Selection/Values-Preset/MAtricks/Filter/Output Filter/Generator, Phase from/to X literal°, Measure, Enabled
- **Approve step gate** (approved defaults false)
- **Export Sequence XML** button
- Choreography/Palette/Stems lanes

This IS the blocks→detail-panel pattern Dave drew in Stitch, realized in lighting. Dave viewed the build live and reacted positively — he liked how it looked, and confirmed the operating bar right now is workability, not polish.

**Plan pivot (Dave-named):** tomorrow's plan is to **program a song with cLD MAker** — the app is workable enough to start real programming; refine/polish later. The opener shifts from macros-first to **program-a-song-first** (macros become a supporting technique within it, not the lead).

History: created 2026-07-17 from the same [0717-3cLD] session that authored the v0.2 spec pack (see `cld-maker-identity-rename-and-scope`).
