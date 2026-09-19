---
id: wrap-protocol-v2-standing-green-light
title: "Wrap Protocol v2 — the green light is STANDING (rehydration default-approved, blocks only on explicit HOLD); kickoff step-0 self-heals a pending wrap"
role: operational-meta
tags: [process, wrap, memory, method]
when_to_load: "At session wrap; at boot when checking whether state files are current; whenever a wrap was written but the state files were never rehydrated"
status: active
source: "findings/INBOX.md 2026-07-23 [0723-2cLD] (STANDING GREEN LIGHT; Wrap Protocol v2 defined)"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**THE FAILURE ANALYSIS THAT WAS WRONG, AND THE CORRECTION.** v1's two-stage wrap said: write the wrap, then **pause for Dave's green light**, then rehydrate the state files. In practice the pause became a pause-that-never-completes and state files went stale. The diagnosis assumed the missing piece was Dave's approval. Dave's response: *"I say green light every single time — I don't get it."*

**The real cause was post-light execution, not the light** — sessions died, drained, or ran out of room before Stage 2 ever ran. The lights were always there; the sessions weren't.

**THE RULING — the green light is STANDING, not per-wrap.** Rehydration is **default-approved**. The pause blocks **only** on an explicit HOLD from Dave. Combined with boot-time self-heal below, Dave never needs to re-issue a light again.

**WRAP PROTOCOL v2, the four changes:**

1. **Wrap-as-you-go.** Draft the wrap during the session rather than reconstructing it at the end, so a session that runs out of room still leaves a usable bridge.
2. **Standing green light.** Stage 2 proceeds by default; only an explicit HOLD stops it.
3. **Kickoff step 0 — SELF-HEAL.** At boot, if a wrap is newer than the state files (or a loose wrap sits in `wraps/` root), **rehydrate first, automatically**, before doing anything else. The boot fixes the previous session's unfinished business without being asked.
4. **The librarian always fires bounded at Stage 2** — not "if there's time."

**THE MARKER CONVENTION.** `wraps/processed/` **is** the rehydrated marker: a wrap sitting loose in `wraps/` root means **pending rehydration**; a wrap in `processed/` means its content has already been folded into `CURRENT_STATE` / `NEXT_ACTIONS` / concepts. This resolves the long-undecided `wraps/processed/` question (open since 2026-07-04).

**Marker established 2026-07-24:** all 34 historical wraps were swept into `processed/`, so `wraps/` root is empty and the marker now reads clean. A step-0 self-heal check is `ls WORKING/wraps/*.md` returning nothing. **Do not re-sweep** — before the sweep, a non-empty root meant nothing, and treating those 34 as pending would have triggered a false self-heal.

**Binding:** v2 binds via the README boot-chain rewrite; the `/kickoff` skill must match.

History: defined 2026-07-23 [0723-2cLD]; marker established by Dave's wrap sweep 2026-07-24.
