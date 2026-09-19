---
id: classifier-tier-gap-edit-and-bare-layer-keywords
title: "RULED 2026-07-17: Edit Preset x, bare layer keywords, and ClearAll STAY Tier 1 — Store/Update already gate the damage point; Oops is the only real promotion candidate"
role: programmer
tags: [mcp, safety, classifier]
when_to_load: "When auditing the MCP command classifier's Tier 1/Tier 2 word list, or citing why Edit / bare-layer / ClearAll lines are intentionally NOT Tier-2 gated (settled ruling, 2026-07-17)"
status: active
source: "findings/INBOX.md, 2026-07-17 [0717-2cLD]"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**Gap observed:** `Edit Preset x` (pulls a preset's values into the programmer, see `edit-session-mechanics-and-contamination-risk`) and bare layer keywords like `Measure 2` (sets the Measure layer at the CLI, see `phasers-via-measures-curriculum` context) both classified as **Tier 1** (read-channel) — but both **mutate programmer state**. Neither `Edit` nor bare layer-value keywords are in the classifier's Tier-2 operation word list.

**Distinction from `lua-body-write-api-classifier-gate`:** that concept covers a different mechanism — write-API calls embedded inside generated Lua bodies slipping past prefix rules (fixed 2026-07-05, scans Lua body text for `SetVar(`/`Delete(`/etc.). This gap is at the **CLI/bare-command classification level** — `Edit` and layer keywords are CLI-native, not Lua write-API calls, so the existing body-scan fix does not cover them.

**RULED 2026-07-17** (Dave, dictated, paraphrased) — **no promotion.** Edit / bare layer keywords / ClearAll STAY Tier 1: ClearAll is Oops-recoverable, and the verbs that make programmer mutation permanent (Store/Update) are already Tier 2 — the gate sits at the damage point, not at every mutating read-adjacent command that precedes it. The genuinely irreversible verb is **Oops** itself (un-oops/redo does not exist in MA3 as of 2.4.2.2 — operator knowledge); chat-fired Oops is the promotion candidate if one is ever needed.

History: found and logged 2026-07-17, not yet actioned. RESOLVED same day (2026-07-17) — Dave ruling as stated above; no promotion, Oops flagged as the only future promotion candidate. Status kept `active` (not `verify`) — this is now a settled policy decision, not an open question.
