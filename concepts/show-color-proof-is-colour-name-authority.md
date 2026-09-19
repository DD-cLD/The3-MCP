---
id: show-color-proof-is-colour-name-authority
title: "RESOURCES/SHOW_COLOR_PROOF/ is the colour-NAME authority for authoring — never read a colour name off the console"
role: programmer
tags: [tourshow, colour, provenance, authoring]
when_to_load: "Before naming, storing, or cross-checking a colour preset's NAME — consult RESOURCES/SHOW_COLOR_PROOF/, not a console value"
status: active
source: "findings/INBOX.md [0803-3cLD] 2026-08-04 (weighted notation, G=0.7 CONSTRAINING)"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**CONSTRAINING (G=0.7).** `RESOURCES/SHOW_COLOR_PROOF/` supplies the colour NAME for
authoring — never a console value. A console read of an existing preset's name/value is not
an authority; if the correct name is needed, it comes from this folder.

**Relation:** `show-direction-doc-and-color-sync-workflow` documents the broader colour-
authority hierarchy (frame-grabs + Color-Sync + palette lock = PRIMARY; {FESTIVAL} showfile
colours = intel-only SECONDARY) — whether `SHOW_COLOR_PROOF/` IS that PRIMARY authority's
storage location, or a separate/later artifact, is not stated by the source and is not
asserted here. `universal-presets-emitter-aware` covers the separate question of how a stored
colour preset resolves across fixture types once named.
