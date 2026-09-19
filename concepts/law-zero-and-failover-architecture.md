---
id: law-zero-and-failover-architecture
title: "Law 0 — 'We don't leave {ARTIST} in the dark' — enforcement stack and the one remaining single point of failure"
role: design
tags: [tourshow]
when_to_load: "Before any design or console-architecture decision that touches {ARTIST}'s key light/position — this is the non-strikeable law that overrides other design preferences; also load before the Art-Net TC failover experiment"
status: active
source: "MEMORY §{TOUR} — direction-package intake + Law 0 — Law 0 + failover, ratified 2026-07-02"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**Law 0: "We don't leave {ARTIST} in the dark."** Ratified 2026-07-02, provenance attached. **Not strikeable** — unlike other design laws (see `tourshow-palette-and-groove-v2`, which explicitly does strike a v0.1 law).

**Why it exists:** on a prior tour, {ARTIST} went dark during console lockups because the rig was **Compact + MA nodes only — no backup, and nodes don't calculate** (they're interfaces, not calculators): console death = output death.

**Enforcement stack:**
- **Manual layer:** ~4 key washes + key spots kept **OUT of TC** — locked play-through sequence, or parked position + intensity on a manual fader; protected priority; fixed executor position on every page.
- **Followspots in every advance** — "daylight doctrine": the {FESTIVAL} "SONG_B" tape is the evidence — upstage blocking + daylight + bright wall = silhouette by default without a followspot.
- **Park** for her keys, plus backups saved in session.

**MA failover is automatic** (has been since original grandMA) — anything already active (phasers, timed sequences) survives a console takeover by the backup/PU.

**Remaining single point of failure (SPOF): TC input lands on the console, not the Processing Unit.** TC-fired GOs stop the instant the console dies; the manual macro-fire architecture (see `tourshow-showfile-architecture`) degrades gracefully because the operator can carry GOs by hand — but only for what's on the manual layer.

**Hypothesis under test:** **Art-Net TC into the PU** may carry TC through a console failure. This is an **our-rig-only ask, not festival-realistic** (house consoles on the EU leg won't have this).

**Takeover drill scheduled** at Dave's Midway/Deadmau5 show (weekend of 2026-07-04): tests output survival, takeover mechanics, state integrity (Park + manual layer + TC), recovery, and the Art-Net TC experiment. Results become the **LD.md lockup runbook**.

**Externally stated and received (2026-07-08):** Dave stated Law 0 directly to {COLORIST} (de facto Creative Director — see `tourshow-team-and-scope`): *"P0 is lighting {ARTIST} — that is the law."* It was received. The floor-storytelling two-tier model (floor = story, house rig = energy/scale — see `tourshow-tour-identity`'s Design principle row) was stated alongside it and also accepted. **Both are now externally confirmed creative direction, not internal-only doctrine.**

**SPOF stack widens (2026-07-08):** lighting now also operates Resolume on the festival leg (see `tourshow-resolume-scope-and-tc-chain`) — the same fragile TC input that feeds the console now also feeds video. A Resolume-owned fixture (if the content-driven-intensity idea ever ships) would need its own console fallback cue if video dies mid-song; open item, not yet solved.

History: none — ratified as a law 2026-07-02; the takeover drill (scheduled for the weekend of this MEMORY snapshot's date, 2026-07-04) had not yet run as of the latest corpus entry. 2026-07-08: Law 0 stated externally to the de facto CD and received (no longer internal-only); SPOF stack noted as widening now that lighting also owns the Resolume/TC-to-video path.
