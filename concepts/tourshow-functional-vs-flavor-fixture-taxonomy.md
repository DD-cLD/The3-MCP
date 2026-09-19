---
id: tourshow-functional-vs-flavor-fixture-taxonomy
title: "Functional vs flavor fixture taxonomy: spots+washes carry the show, beams+strobe+linear are flavor — no musical moment may depend on beams to land"
role: design
tags: [tourshow, doctrine]
when_to_load: "Before deciding whether a cue/moment is allowed to depend on the beam category (or strobe/linear) landing, or before writing/updating TOUR_DESIGN_THEORY — this is a candidate doctrine for v0.3"
status: active
source: "findings/INBOX.md, 2026-07-19 [0718-19cLD], Dave doctrine dictation — candidate for TOUR_DESIGN_THEORY v0.3"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

Dave's doctrine, paraphrased: fixtures split into two functional classes. **Functional** = spots + washes, working all day to keep the stage lit with cohesive looks — the base layer every show needs regardless of rig. **Flavor** = beams + strobe + linear, the effect side. Beams specifically sit **between** effect and functional — grouped with strobe/linear (same zone), not with spots/washes.

**Beam availability rule:** not every festival rig carries the beam treatment — one rig might have 8, another 24, sometimes none. The show has to be able to **live with or without beams**. The practical instruction: program the full template complement (64 beams) as if they'll always be there, but **no musical moment may DEPEND on the 5xx category landing** — beam gestures layer on top of an already-complete functional base, never carry a moment alone. Scaling rationale: the investment in full beam programming pays off later at main-stage festival slots / an arena transition tour, even on legs where a given rig doesn't have the fixtures to show it.

**Architectural mechanism that makes "live without" nearly free (cLD observation, same session):** because {TOUR} is recipe-based (see `tourshow-recipe-based-show-style-ruling`), spread-fill simply leaves the 5xx role slots (Group 501+, see `tourshow-group-contract-v01`) **empty** on a beamless rig, and a fully-referenced recipe firing into an empty Selection is a **silent no-output** — cues degrade gracefully with zero re-programming per rig. This is the concrete mechanism behind "program full, tolerate absence": nothing breaks, nothing errors, the beam layer just doesn't fire on a rig that doesn't have it. An optional refinement not yet built: an understudy chain where beams' natural stand-in is spots at a tight zoom — the general understudy mechanism is already reserved in `tourshow-festival-group-theory`, just not yet wired for this specific pairing.

**Independent corroboration:** the world-practices research pass found the same functional/flavor split described industry-wide as "meat and potatoes vs. accent fixtures" — see `tourshow-world-practices-research-intake`.

History: none — doctrine dictated live 2026-07-19, flagged by Dave as a TOUR_DESIGN_THEORY v0.3 candidate (not yet folded into that doc).
