---
id: beam-not-strobe-terminology
title: "BEAM names the JDC1/ACME center element — 'strobe' names only the function run on it"
role: programmer
tags: [ma3, doctrine, terminology, tourshow, jdc1, acme]
when_to_load: "Before labeling a group, cue, or fixture element on JDC1 or ACME — or when tempted to call a center-row element 'strobe' instead of 'beam'"
status: active
source: "findings/INBOX.md, 2026-07-15, Dave dictated live"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

Dave's terminology ruling, dictated live and then explicitly widened mid-session: the center element on both JDC1 and ACME is named **BEAM**. "Strobe" is not the element's name — it's the name of the FUNCTION run on that element. A beam can be strobing or not; the hardware/grid-cell identity stays BEAM either way.

The ruling started on JDC1, where the naming was already correct in practice — Dave cited the group label "cLD JDC DS BEAM" as the existing model to follow. It was then extended explicitly to ACME: the pixel-line's center row is the same class of element and gets the same name.

Consequence: Group 126, the ACME center-row group, is currently labeled "cLD PIX DS STROBE" — under this ruling that label names the function instead of the element, the same mistake the JDC1-side naming had already avoided. It's flagged for relabeling; Dave hasn't yet given the exact replacement label or executed the change as of this run.

Practical rule going forward: any new group/cue label touching a center beam element should say BEAM, and "strobe" should only appear in a label when it's naming the strobing behavior itself (e.g., a cue that runs the strobe function), never as a stand-in for the element.

**⚠ Unresolved BEAM-vs-TUBE inconsistency (surfaced 2026-07-21, do NOT auto-resolve):** this ruling says the JDC1 center element is BEAM, but the naming is now genuinely split. Dave's own 2026-07-21 hand-built full-rig grid group is labeled "cLD(C) TUBES GRID" (group 435), and cLD's per-truss JDC center cell groups (442–445) stand as "… TUBE" to match Dave's latest — and `jdc1-anatomy-ground-truth` also calls them "tube segs." cLD first corrected those groups TUBE→BEAM per this ruling, then reverted to TUBE to match Dave's hand grids. Net split: the ACME/pixel side uses BEAM (335 "PIX BEAM GRID"), the JDC side currently uses TUBE (435 "TUBES GRID"). Left as-is pending Dave's reconciliation — he has not ruled which term wins for the JDC center. Do not auto-relabel either way.

History: none — dictated live 2026-07-15, extended from JDC1 to ACME within the same session. 2026-07-21: surfaced an unresolved BEAM-vs-TUBE naming split on the JDC center (Dave's hand grids + cLD's per-truss groups use TUBE); flagged for Dave, not auto-resolved.
