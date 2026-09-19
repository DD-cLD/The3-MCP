---
id: export-diff-verification-loop
title: "Export-diff verification loop: compute an expected-positions table, then confirm it two independent ways (grandMA3 XML diff, MVR matrix parse) after every major geometry pass"
role: programmer
tags: [ma3, v2.4, patch, verification, process]
when_to_load: "After any major batch of 3D-position writes, before trusting the rig is correct — this is the milestone-level check that sits above per-paste hygiene"
status: active
source: "findings/INBOX.md, 2026-07-14; wrap 2026-07-14-3drig-mirror-doctrine-grid-drills"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**The method:** compute an expected-positions table ahead of time from the design math (not from the console's own state), then verify the console actually matches it by exporting and diffing — not by trusting the UI or a clean CLI echo. Two independent export lanes are available and were used redundantly this session:
1. **grandMA3 XML export**, diffed programmatically against the expected table (schema: `patch-xml-export-lane-and-schema`).
2. **MVR export**, parsed (position/rotation per fixture via its matrix encoding) and checked the same way (schema: `patch-mvr-export-import-lane-and-schema`).

Agreement across both lanes is the confidence signal — this is a genuine cross-check, not just running the same test twice, since the two export formats encode position/rotation differently (attribute-based vs. matrix-based).

**Applied twice this session as the template rig's geometry evolved:** the first pass confirmed **192/192 truss fixtures exact** via the grandMA3-XML diff, right after the initial alternating-hang cut. After the mirror-cut and a wing-JDC repair, a full MVR parse confirmed **all 256/256 overhead fixtures exact** — the final, fully-verified state (see `tourshow-template-rig-patch-and-layout-state`).

**This is the loop that catches phantom writes.** A 16-command wing-JDC position paste echoed clean in the CLI but had silently not landed — the census/diff step is what surfaced that, not the paste's own echo (see `paste-round-verification-protocol` for the per-paste-round discipline this loop sits above). The lesson generalizes: **census-diff after every batch is the law**, not an occasional sanity check.

**Ground-truth and export artifacts from this session:** `outputs/expected_positions.json` (the computed expected-positions table used as the diff target); exported/parsed patch files `showfiles/cld_patch_v1/v2.xml`, `cld_patch_v3/v4.mvr`, `cld_l2_final.xml`.

History: none — the two-lane loop was assembled and run twice live, 2026-07-14, verifying the template rig's 3D positions first at 192/192 and finally at 256/256.
