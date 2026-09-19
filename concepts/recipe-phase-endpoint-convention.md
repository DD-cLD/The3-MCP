---
id: recipe-phase-endpoint-convention
title: "RESOLVED (Dave): a recipe's PhaseToX=360 is NORMALISED — one full lap, endpoints excluded, no first/last collision. 0-360 is the standard setting and the portable one; 360−360/N stays correct for locking a KNOWN rig"
role: programmer
tags: [ma3, recipes, phase-math, v2.4, portability]
when_to_load: "Before choosing a phase range for any recipe — settles that generic 0-360 is safe on any fixture count, and that the 360−360/N literal is a different lane (MAtricks pool storage on a known rig), not a competing answer"
status: active
source: "findings/INBOX.md 2026-07-16 (original question); RESOLVED by Dave operator ruling 2026-07-27 [0727-2cLD]"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**⭐ RESOLVED 2026-07-27 (Dave, operator knowledge) — the engine NORMALISES it.** A recipe's
`PhaseToX=360` is read as **one full lap with endpoints excluded**; fixture 1 and fixture N do
**NOT** land on the same output phase. **0-360 is the standard setting.** This clears the
question below, which had been promoted to ⛔ BLOCKING under the generic-phase-range doctrine
(`no-baked-n-portable-phaser-doctrine`) — **no desk test is needed and nothing gates phaser
authoring.**

**What this does NOT do:** it does not supersede `360 − 360/N`. That formula stays correct for
**MAtricks pool storage on a known rig**, where phase is a literal manual value the console
does not compute (`mtricks-phase-vs-encoder-phase`). Two surfaces, two computation paths, two
different questions — generic `0-360` for travelling content, the literal formula for locking
a fixed rig. The original tension below was real; the resolution is that both are right in
their own lane.

---

Full-spread recipes in MA's stock phaser-recipe library ship `PhaseFromX=0 PhaseToX=360` — a literal full-circle endpoint pair. This is **different** from this project's existing literal MAtricks full-spread rule, `PhaseTo = 360 − (360 / N)` (see `phase-math-formulas`), which deliberately stops short of 360° to avoid the first and last fixture landing on the same phase.

**[VERIFY]** — not yet live-tested: does a recipe's `PhaseToX=360` actually collide the first and last fixture in the selection (same phase, redundant step), or does the recipe engine auto-correct/normalize a literal 360 the way "one full lap, endpoints excluded" would read rather than a literal degree pair? The two systems (MAtricks pool object vs. phaser-recipe `PhaseFromX`/`PhaseToX`) may not share the same computation path — see `mtricks-phase-vs-encoder-phase` for a precedent of exactly that kind of surface-dependent behavior (MAtricks pool = literal/manual, Encoder Bar = auto-calculated).

Would be resolved by: building a small recipe with a known fixture count N, setting `PhaseToX=360`, and checking live whether fixture 1 and fixture N land on the same output phase.

**Corroborated 2026-07-17:** a second, independent source confirms the same convention — a **console-built** recipe (not just the stock library file) exports with `PhaseFromX="0" PhaseToX="360"` at the XML level (see `recipe-xml-schema`'s display-string phase-value format). Two independent readings now agree on the 0→360 convention itself; the collision-vs-autocorrect question remains untested live and status stays `verify`.

History: created 2026-07-16; status `verify` pending a live collision test. Updated 2026-07-17: corroborated by a second, independent console-built-recipe XML read. **RESOLVED 2026-07-27 [0727-2cLD] — Dave ruled from operator knowledge that 0-360 is the standard setting and is normalised (one lap, endpoints excluded); status verify -> active, and the ⛔ BLOCKING flag it had carried that day is cleared.** The two prior XML readings are now explained rather than merely corroborated.
