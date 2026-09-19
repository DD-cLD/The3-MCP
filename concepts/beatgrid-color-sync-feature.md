---
id: beatgrid-color-sync-feature
title: "Beatgrid 0.4 ships Color-Sync: frame-grab → median-cut swatches → redmean-anchored palette lock, timeline color strip, palette manager, QCaller pal: names"
role: tools
tags: [beatgrid]
when_to_load: "Before touching beatgrid.html's Color-Sync feature (frame-grab workflow, palette manager, color strip) or reasoning about session format 0.4's palette/colors/frame fields"
status: active
source: "findings/INBOX.md 2026-07-06 + wrap 2026-07-07-beatgrid04-festival-tc"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

Shipped unattended in beatgrid 0.4, 2026-07-06, on Dave's double green light. Pipeline: **frame-grab → median-cut swatches → redmean-anchor to the palette lock** (ARTIST_TOURSHOW palette baked in as defaults), **color strip on the timeline**, **palette manager with an MA3-preset field**, **QCaller `pal:` names-only** output. Spec: `beatgrid/Meta/COLOR_SYNC_SPEC_v0.1.md`.

Session format bumped to **0.4** (adds palette/colors/frame fields, alongside Stem-Sections' stemsets/stem fields — see `beatgrid-stem-sections-feature`); **0.3 sessions load clean** — verified against the real "SONG_Q" session. Pre-0.4 backup: `_rubbish/beatgrid_v0.3_pre-0.4_2026-07-06.html`.

Implements Dave's planned color-sync workflow first noted in `show-direction-doc-and-color-sync-workflow`, and operates under the color-authority hierarchy pinned there (frame-grabs + Color-Sync are PRIMARY; showfile colors are intel-only).

Cross-checked (see `crosscheck-subagent-pattern`'s 3rd data point) — 0 blockers/4 majors/9 minors on this diff, all majors fixed same session; the heavy-payload majors are captured in `beatgrid-undo-side-cache-pattern`.

History: none — shipped and verified same session, 2026-07-06.
