---
id: tourshow-tc-cutover-crosswalk-pattern
title: "TC cutover crosswalk: Dave cuts TC himself — MAIN track re-targets {LD} <century>00 → cLD <century>10; aux tracks stay on {LD}'s <century>01-0N, edited in place; census = Target + L3 event count"
role: programmer
tags: [ma3, v2.4, tourshow, timecode, cutover, sequence]
when_to_load: "Planning or executing a per-song TC cutover — deciding who cuts, which tracks re-target, and what the post-cutover census must read."
status: active
source: "findings/INBOX.md 2026-08-05 [0805-2cLD] — live console v2.4.2.2 probes + {LD} {FESTIVAL} export reads + Dave rulings"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---
Cutover pattern (Dave, attested on both songs this session): **Dave cuts TC
himself.** The MAIN track re-targets {LD} `<century>00` → cLD `<century>10`.
AUX tracks stay on {LD}'s `<century>01-0N` sequences, which Dave edits IN
PLACE — no new aux sequences are minted.

Census after cutover = per-track **Target AND per-track event count read at L3
depth** — events live two levels below the TrackGroup pointer (depth law filed at
`tc-targeted-sequence-delete-eats-events`... see also
`tc-cutover-last-and-delete-eats-events-doctrine`). CLI lane and dot-index law:
`tc-track-target-cutover`.

History: none — minted 2026-08-05 [0805-2cLD] from Dave's cutover pattern across both songs handled this session.
