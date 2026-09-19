---
id: choreography-lane-generalizes-stemsets
title: "cLD MAker's choreography/locale lane generalizes the Stem-Sections pattern: section→child lanes→markers-as-Events, reusing delete/undo/save for free"
role: tools
tags: [tourshow, cld-maker, beatgrid]
when_to_load: "Before designing cLD MAker's choreography/locale timeline lane (the cue-caller heads-up feature) or reasoning about whether it should share implementation with beatgrid's Stem-Sections"
status: active
source: "findings/INBOX.md, 2026-07-17 [0717-3cLD]"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**Architecture insight:** `STEM_SECTIONS_SPEC_v0.1`'s stemsets lane pattern — section → child lanes → markers-as-Events — generalizes cleanly to a choreography/locale lane for Dave's "cue-caller heads-up" ask (e.g. "{ARTIST} about to go DSC"). Reusing the pattern means reusing existing delete/undo/save semantics for free, rather than inventing a new subsystem for choreography tracking.

**Open judgment call, not pre-decided:** the spec flags whether stemsets and choreography should share a base implementation as a Codex judgment call at build time.

**Relation:** `beatgrid-stem-sections-feature` is the pattern being generalized. `cld-maker-identity-rename-and-scope` for where this lane lands in the dashboard scope (dashboard indexes CHOREOGRAPHY as a timeline lane; locale events feed QCaller prompts + specials/position-preset planning).

History: none — architecture insight recorded 2026-07-17, same session as the cLD MAker scope ratification.
