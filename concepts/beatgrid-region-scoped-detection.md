---
id: beatgrid-region-scoped-detection
title: "Region-scoped detection shipped in beatgrid.html — analysisScope() runs EST/hits/suck-outs on local stats inside a selected region"
role: tools
tags: [beatgrid, audio-dsp]
when_to_load: "Before running beatgrid detection on a multi-segment or tour-bounce file (intro + song, or any file with heterogeneous sections) — select a region first so stats are local, not whole-file"
status: active
source: "findings/INBOX.md 2026-07-07 + wrap 2026-07-07-beatgrid04-festival-tc"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

Shipped 2026-07-07 as the fix for the multi-segment/whole-file-statistics problem diagnosed the same day (see `beatgrid-dsp-reality-check`). **`analysisScope()`**: select a region → **EST + Detect hits + Detect suck-outs** all run **inside that region with LOCAL stats** (local 95th-pct reference, local mean/σ) and **scoped idempotent clearing**, so per-song passes accumulate without clobbering each other. **No selection = whole file** — the original album-analysis behavior is unchanged.

**10 new harness assertions green**, including the proof-case: a suck-out that's **invisible to global eMax** is **found when scoped**.

**Tour-bounce workflow going forward: punch song regions, then detect per song** — not one whole-file pass.

History: none — designed and shipped same day as the diagnosis, 2026-07-07.
