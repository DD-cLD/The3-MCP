---
id: beatgrid-stem-sections-feature
title: "Beatgrid 0.4 ships Stem-Sections: section → child stem lanes, band-proxy or real-stem detection, hits/presence, low-confidence suggestions"
role: tools
tags: [beatgrid]
when_to_load: "Before touching beatgrid.html's Stem-Sections feature (child stem lanes, stem detection, suggestion thresholds) or reasoning about session format 0.4's stemsets/stem fields"
status: active
source: "findings/INBOX.md 2026-07-06 + wrap 2026-07-07-beatgrid04-festival-tc"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

Shipped unattended in beatgrid 0.4, 2026-07-06, alongside Color-Sync (see `beatgrid-color-sync-feature`). Each section can carry **child stem lanes**; detection works via **band-proxy OR real-stem-file** input; lanes carry **hits/presence** data; **suggestions below 0.6 confidence** are flagged as such rather than asserted. Spec: `beatgrid/Meta/STEM_SECTIONS_SPEC_v0.1.md`.

Session format 0.4 adds stemsets/stem fields (see `beatgrid-color-sync-feature` for the palette/colors/frame half of the same version bump); **0.3 sessions load clean**. Pre-0.4 backup: `_rubbish/beatgrid_v0.3_pre-0.4_2026-07-06.html`.

**Convergence note:** {LD}'s {FESTIVAL} per-song bump vocabulary (kick/snare/clap — see `tourshow-showfile-architecture`) maps 1:1 onto these stem lanes (kick/snare lanes → bump moments) — the tour-file-archaeology workstream and the beatgrid-build workstream met here.

Cross-checked (see `crosscheck-subagent-pattern`'s 3rd data point) — 0 blockers/4 majors/9 minors on this diff (shared with Color-Sync, same diff/review pass).

History: none — shipped and verified same session, 2026-07-06.
