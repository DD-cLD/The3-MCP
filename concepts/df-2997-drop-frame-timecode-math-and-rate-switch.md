---
id: df-2997-drop-frame-timecode-math-and-rate-switch
title: "29.97 drop-frame timecode: console rate-switch recalculates automatically (no re-entry/re-export); math pinned + Python-verified (30000/1001, 17982 frames/10min, integer frame-space arithmetic only)"
role: programmer
tags: [ma3, timecode, xml-schema, v2.4]
when_to_load: "Before authoring, converting, or displaying 29.97 drop-frame timecode anywhere in the pipeline — console rate-switch behavior and the pinned DF math formulas"
status: active
source: "findings/INBOX.md, 2026-07-18 (Dave operator-confirmed console behavior; beatgrid/Meta/harness/df_verify.py)"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**Console rate-switch behavior [Dave operator-confirmed]:** author timecode at 30fps; switching the show's TC frame rate to 29.97 drop makes the console recalculate everything itself — **no TC re-entry, no re-export needed.** Consistent with the cracked TC-event schema (`export-timecode-tc-event-xml-schema`): `CmdEvent` `Time` is a decimal-seconds string, which is rate-agnostic by construction.

**Repo manual gap:** ZERO hits for drop-frame/29.97 in the repo manual — another entry in the running manual-gap list (alongside `measure-layer-math` and `at-filters-worlds-manual-gap-and-study-doc`).

**DF math, pinned + Python-verified** (`beatgrid/Meta/harness/df_verify.py`):
- Rate = **exact `30000/1001`**, never float.
- DF drops **2 frame NUMBERS per minute**, except each 10th minute (no drop).
- **17982 frames per 10 minutes.**
- `01:00:00;00` = **107892 frames** = **3599.9964 seconds**.
- Invalid DF labels: `FF ∈ {0,1}` when `SS=0` and `MM % 10 ≠ 0`.
- **Drift comparison:** a 29.97 NDF (non-drop) label drifts −0.3s @ 5min, unbounded over time; DF stays bounded to ±2 frames.
- **All TC arithmetic must happen in integer frame space** — worked example: `03:29:53;22 + 42.8s = 03:30:36;15` (DF) vs `03:30:36:16` (30 NDF) — the one-frame delta is correct; they're different clocks, not an error.

History: created 2026-07-18 from the DF verification session; console rate-switch behavior and math formulas captured together since both are needed for any DF timecode work.
