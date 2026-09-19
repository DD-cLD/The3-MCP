---
id: tourshow-content-driven-rig-synthesis
title: "[INTERNAL ONLY] Content-driven fixture intensity via Resolume — NDI vs Lumiverse options, and the intensity-only/color-stays-locked synthesis"
role: design
tags: [tourshow, internal-only]
when_to_load: "INTERNAL PLANNING ONLY. Never reference or telegraph this in outbound material — no advance emails, festival-facing drafts, or external communications may mention Resolume-driven lighting output. Load only for internal design-strategy discussion, and only once the idea is ready to leave the sleeve (not yet, as of 2026-07-08)."
status: active
source: "findings/INBOX.md 2026-07-08 (Dave design riff + cLD synthesis) — SLEEVE, per Dave's explicit rule"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**SLEEVE RULE (Dave, 2026-07-08, explicit):** this entire concept is **internal only — up the sleeve, not on the table until everything's locked in.** Nothing in outbound drafts or advances may reference or telegraph it (e.g. no Resolume-lighting-output network asks in advance emails). Two-ledger discipline applies.

**The option (Dave, design riff — decision gates on Trevor's content):** since lighting now operates Resolume (see `tourshow-resolume-scope-and-tc-chain`), some cues could let CONTENT drive fixture INTENSITY for organic/smooth passages. Two paths considered:
- **(a) NDI capture** — color comes through imperfect, needs tuning/offset.
- **(b) Resolume LUMIVERSES** — Arena's lighting-output feature: pixels are placed on output maps and driven straight from the composition via Art-Net/DMX, color as-rendered, frame-locked by construction.

Dave's own framing: "we'll have to see what the content tells."

**Synthesis candidate (cLD):** drive **INTENSITY ONLY** from Resolume; **color stays console-owned** via the palette lock. This makes the NDI/compression color-fidelity worry moot (video never owns color — palette rule 5 stays upheld). **Best target: the FLOOR PACKAGE** — it's constant across every venue, so a Lumiverse pixel map would only need to be built once, never re-placed per festival; a breathing floor is already a story-tier device (see `tourshow-tour-identity`'s floor=story/house=energy principle), which fits {COLORIST}'s simplicity steer (see `tourshow-palette-and-groove-v2`) — content supplies the motion, the console supplies the color blocks.

See `tourshow-content-driven-rig-verify-items` for the technical unknowns that must be checked before leaning on this, and `law-zero-and-failover-architecture` for the failover question this raises (a Resolume-owned fixture needs a console fallback cue if video dies mid-song).

History: none — option and synthesis both recorded same session, 2026-07-08, immediately marked SLEEVE/internal-only by Dave.
