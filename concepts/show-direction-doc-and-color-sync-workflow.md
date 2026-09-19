---
id: show-direction-doc-and-color-sync-workflow
title: "ARTIST_TOURSHOW_Show_Direction.xlsx is a video-color reference, not lighting gospel — and why uploads must be copied into the repo before wrap"
role: design
tags: [tourshow, process]
when_to_load: "Before treating the Show Direction doc's colors as literal lighting cues, or when a session upload needs to survive past session end"
status: active
source: "MEMORY §Bird's Eye tour — team, routing, file architecture, LTC — Show direction doc, 2026-07-02 evening; findings/INBOX.md 2026-07-06 + wrap 2026-07-07-beatgrid04-festival-tc"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

`WORKING/ARTIST_TOURSHOW_Show_Direction.xlsx` (67 MB, copied from session uploads 2026-07-02) — **uploads are session-mortal; always copy into the repo before wrap.**

Its color directions are **for the videos** — reference material, not lighting gospel. Dave's planned color-sync workflow: frame-grab key video shots → communicate through them → land sync points in Beatgrid.

**Color authority hierarchy pinned (2026-07-06, Dave verbatim-ish — supersedes his own "colors as approved canon" framing from earlier the same night):**
- **PRIMARY** = our own frame-grabs + Color-Sync + palette lock. Dave: *"I would rather go from the frames that we grab and our color sync."*
- **SECONDARY** = {FESTIVAL} showfile colors, treated as **approved-on-site INTEL/cross-check only** (onPC color-preset export demoted to nice-to-have).
- **Song timings from the file = intel only.** The real work is **song-by-song fresh design.**
- **File-side color mining is a dead end anyway:** embedded PNGs yielded no usable swatches (4 real images, the rest truncated); color values live in binary cue data, reachable only via onPC export — which is why that export is now low priority, not unwanted.

Implemented in `beatgrid-color-sync-feature` (shipped same week).

History: none — recorded 2026-07-02 evening. The "uploads are session-mortal" lesson generalizes beyond this one file; see also `xlsx-hyperlinks-in-google-sheets-exports` for what was found when this specific file was actually parsed. 2026-07-06: Dave stated an initial "colors as approved canon" framing earlier the same night, then explicitly superseded it with the hierarchy above later that night — only the later statement banked as current.
