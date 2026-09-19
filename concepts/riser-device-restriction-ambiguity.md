---
id: riser-device-restriction-ambiguity
title: "UNRESOLVED: does Law 6 restrict Riser/Chase like Strobe burst, or only Strobe? Resolved permissively this round — TOUR_DESIGN_THEORY still needs a ruling line"
role: design
tags: [tourshow]
when_to_load: "Before placing a Riser or Chase device on a Bird's Eye/{TOUR} build — the doc is genuinely ambiguous about whether these are tour-restricted like strobe; check whether Dave has ruled on this yet before assuming the permissive reading still holds"
status: active
source: "findings/INBOX.md 2026-07-08, raised by the Pilot fleet worker"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**The ambiguity:** `TOUR_DESIGN_THEORY_v0.2.md` §3's device table lists **"Riser / Chase / Strobe burst" together**, with home-tier "—" and a note pointing to **Law 6** — but Law 6's own prose only explicitly names **strobe** as restricted to three sanctioned tour moments (see `tourshow-palette-and-groove-v2`). Read strictly, Riser (and Chase) could be equally restricted, which would matter: several fleet-batch builds used Riser on non-sanctioned songs.

**Resolved permissively this round (not a formal ruling):** the Pilot worker used Riser on its Build section, reasoning that (a) `beatgrid.html`'s own `DEVICE_FOR` default maps `build → "Riser"` directly (read from source, not assumed), and (b) SONG_L's build, same batch, had already used Riser on its own Build without incident. Flagged explicitly in `pilot_analysis.json.device_note_riser_ambiguity` rather than silently resolved.

**Still needed: a ruling line in `TOUR_DESIGN_THEORY_v0.2.md` itself.** Until Dave rules on it, treat the permissive reading (Riser/Chase unrestricted, only Strobe burst is the 3-moment-sanctioned device) as this project's working assumption, not a settled fact — a stricter reading remains live and would change any build that used Riser outside SONG_H/Sat Night/SONG_Q.

History: none — ambiguity raised, worked around permissively, and flagged for a doc ruling, 2026-07-08 (fleet worker finding, digested from batch date 2026-07-07).
