---
id: tc-targeted-sequence-delete-eats-events
title: "Deleting a sequence that a timecode track targets EATS that track's events — census event counts at L3 (Timecode → TrackGroup → Track → SubTrack → events), never at the TrackGroup pointer"
role: programmer
tags: [ma3, timecode, tc, delete, census, v2.4]
when_to_load: "Before deleting or retargeting any sequence that a Timecode track points at, and before trusting any TC event census — a shallow counter reads a healthy cutover as emptied"
status: verify
source: "Filing note: upstream this concept survives only as its 2026-08-05 EXTENSION block plus History; the original mechanism paragraph was lost show-side. The headline claim is carried by the id and by hard rule 13 in playbook/console-hard-rules.md. Body below is the extension as filed."
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---
**[0805-2cLD] EXTENSION — census depth law:** the tree is Timecode → TrackGroup → Track → SubTrack → events. `tc:Ptr(j)` is a TRACKGROUP; `Track.Target` lives one level down; real event counts live TWO levels down (L3). A shallow counter reads a healthy cutover as event-emptied — cost two false-empty censuses on 2026-08-05. Any event census in this family counts at L3.

History: extended 2026-08-05 [0805-2cLD] — traversal depth: tc:Ptr is a TrackGroup, event counts live at L3; shallow counters false-report empty (two censuses paid).
