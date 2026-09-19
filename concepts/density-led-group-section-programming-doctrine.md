---
id: density-led-group-section-programming-doctrine
title: "Design-language intake: Codex idea-files speak in 'Group A / Group B' — bringing on SECTIONS of the rig and letting DENSITY (alternation/accumulation of rig subsets) carry the rhythm, not just per-fixture effects; lands directly on the group spine's bind table"
role: design
tags: [tourshow, doctrine]
when_to_load: "Before translating a Codex/design idea-file that references 'Group A/Group B' density language into console groups and recipes"
status: active
source: "findings/INBOX.md 2026-07-23 [0722-2cLD] (Dave, relaying Codex design-file vocabulary)"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**The vocabulary (Dave, relaying how Codex's design idea-files actually talk):** design-side deliverables speak in terms of **"Group A / Group B"** — bringing on SECTIONS of the rig (subsets, not individual fixtures) and letting **DENSITY talk**: alternation and accumulation of rig subsets as the rhythm carrier. This is explicitly named as **the classy lane** — as opposed to per-fixture chase/flash effects. Effects are still used, but classically, sometimes randomly, rather than as the primary rhythm mechanism.

**Why this is easy to build (no new infrastructure):** this design language lands **directly on the existing group spine** — scopes, composites, and subsets already defined in `tourshow-group-contract-v01` — via the recipe bind table (a recipe's Selection slot just points at "Group A" = whichever contract group/composite the idea-file names). Handoff JSONs from the design side already carry **per-cue density** as a value, so this isn't a new authoring concept, just a naming convention to honor when translating an idea-file into recipes.

**Relation:** `idea-file-design-programmer-boundary-doctrine` for the idea-file handoff this vocabulary rides in. `tourshow-group-contract-v01` for the group spine this vocabulary targets. `cross-type-groups-vision` for a related existing doctrine (whole-rig cross-type rhythm groups) this density language sits alongside — not a duplicate, a complementary technique (cross-type = mixing fixture TYPES in one group; density-led sections = alternating rig SUBSETS/zones).

History: none — vocabulary relayed and doctrine named in one session, 2026-07-23 (digesting the [0722-2cLD] session block).
