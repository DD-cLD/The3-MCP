---
id: group-edit-remove-pattern
title: "To remove members from an existing Group: select the fixtures to remove, hit Store, choose the group, hit Remove"
role: programmer
tags: [ma3, cli, group, v2.4]
when_to_load: "Before editing an existing Group's membership down (removing specific fixtures) rather than rebuilding it from scratch"
status: active
source: "findings/INBOX.md, 2026-07-15, Dave, console 2.4.2.2"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**Dave's pattern:** to remove members from an already-stored Group — select the fixtures that should come OUT, hit **Store**, choose the target group, then choose **Remove** (rather than Overwrite or Merge) in the resulting dialog.

**Companion patterns:** this sits alongside `Store` → **Overwrite** (replace the group's contents entirely) and the subtraction-at-selection-time method documented in `group-subtraction-preserves-grid-coords` (build the reduced set via `Group A - Group B` before storing, rather than storing a Remove against an existing group). Same family of choices also appears in the `Store Default` popup (Overwrite/Merge/Remove/Cancel — see `store-default-values-keyword`), suggesting Remove-as-a-store-mode is a consistent idiom across MA3's Store dialogs.

History: none — pattern dictated live by Dave, 2026-07-15.
