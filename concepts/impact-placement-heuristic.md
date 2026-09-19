---
id: impact-placement-heuristic
title: "Impact placement heuristic: spend the one rationed Impact on measured evidence over the thematically 'obvious' spot, and never on top of another rationed effect"
role: design
tags: [tourshow, design]
when_to_load: "When deciding where a song's single rationed Impact (the closed-at-7 device set — see tourshow-palette-and-groove-v2) should land"
status: active
source: "fleet worker FINDINGS_LOCAL, 2026-07-07"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

Cross-song pattern from the six-song fleet batch (all six held the ration: exactly one Impact per song, zero exceptions):

- **Prefer measured evidence over the thematically "obvious" spot.** SONG_L spent its Impact 70s after the "obvious" chorus payoff, on the objectively hottest transient in a plain returning verse (164.2s), because two independent measurements (GT transients + the song's own RMS pass) pointed there, not because it was dramatically convenient. From Scratch went further — no transient at all sits near its chosen spot (Verse 5); the absence of a sharp hit was itself the finding, corroborated only by two independent loudness measurements agreeing the section is the song's real peak.
- **Don't spend the Impact inside another rationed effect's window.** SONG_H's strobe (sanctioned exactly once, at the jersey-club breakdown 1:31–1:44) and its Impact were deliberately kept apart — both builds independently reasoned that piling the Impact on top of the strobe party wastes it; the Impact instead lands at the exit/slam-out of the strobe window, the decision the party sets up rather than the party itself.
- **Don't spend it too early.** From Scratch's hardest-measured hit (18.8s) was passed over for the Impact specifically because spending the show's one gesture that early, before either chorus, "undersells rationed." Pilot's hottest onset (0:38.4, in the Breakdown) was passed over for the same reason — 38 seconds in, before her voice or any verse is established, front-loads the show's one gesture ahead of the material it should pay off.
- **Respect device character, not just loudness.** Pilot's Outro contains the single loudest sustained instant in the song (0.999 normalized RMS) but was *not* given the Impact: Impact's own definition is a struck, radial, one-shot gesture, and a sustained swell is the opposite in character — plus the section is governed by "dissolves only subtract," which spending the one payoff inside would directly contradict. The finding instead produced a deliberate choice to let the light keep subtracting through the loud stretch rather than answering it.
- **When two measures (structural + measured) agree, that's worth naming as a stronger case than when they conflict.** Candy's Impact (t=95.9, inside its longest/biggest chorus) is explicitly noted as a case where structural prominence and measured prominence agree — flagged as not true of every song in this project, with the real alternate (t=140.6) named rather than hidden.
- **Always flag ◆ for ratify, never smuggle the call.** Every non-obvious Impact placement in the batch is flagged ◆ in the analysis JSON, moodboard, and CSV, with the rejected alternate(s) named and reasoned, not just the winner.

See also `gt-tilt-band-vs-broadband-loudness-gotcha` (the measurement technique that often drives these calls) and `bar-math-corroboration-method` (used in 1 of 1 to split a block specifically so the Impact could land on a real transient).

History: none — heuristic distilled from six independent builds converging on the same reasoning shape, fleet batch 2026-07-07.
