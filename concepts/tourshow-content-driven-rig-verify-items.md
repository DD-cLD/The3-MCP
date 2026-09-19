---
id: tourshow-content-driven-rig-verify-items
title: "[INTERNAL ONLY, VERIFY] MA3 DMX-in/sACN/Art-Net merge semantics on 2.4.2 are unknown — required checks before content-driven intensity is viable"
role: design
tags: [tourshow, internal-only]
when_to_load: "INTERNAL PLANNING ONLY. Never reference or telegraph this in outbound material. Load before doing the manual/console check of MA3's merge behavior, or before any decision that assumes Resolume and the console can both drive the same fixture safely."
status: verify
source: "findings/INBOX.md 2026-07-08 — SLEEVE, per Dave's explicit rule; technical items explicitly marked verify, don't assume"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

Technical unknowns that must be checked (manual/console check, not assumed) before leaning on the content-driven-intensity idea in `tourshow-content-driven-rig-synthesis`:

- **MA3-side DMX-in / sACN / Art-Net MERGE semantics on 2.4.2:** who owns a fixture when Resolume and the console both talk to it at once? Is it HTP on the dimmer? A per-universe merge? Does it need parking/choreography per cue to avoid a fight? **Not verified — requires a manual/console check, do not assume a specific merge behavior.**
- **Whether MA3 has ANY native NDI ingest:** believed to be **no in v2.4**, but this is unconfirmed — verify against the manual/console, don't invent an answer either way.
- **Failover angle (cross-ref `law-zero-and-failover-architecture`):** if a fixture is ever Resolume-owned, it needs its own console fallback cue for the case where video dies mid-song — the failover stack widens again and isn't solved yet.

**These are quiet homework, not blocking anything currently in flight** — they only matter if/when the content-driven-intensity option in `tourshow-content-driven-rig-synthesis` moves off the sleeve.

History: none — verify list compiled same session, 2026-07-08.
