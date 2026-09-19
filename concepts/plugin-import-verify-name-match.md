---
id: plugin-import-verify-name-match
title: "Import verify read-back must compare slot object Name == expected — any-occupant truthiness false-positives on already-taken slots"
role: programmer
tags: [lua, mcp]
when_to_load: "Before writing or trusting a round-trip verify step after Import Plugin <slot> — any check weaker than an exact Name comparison can misreport success"
status: active
source: "findings/INBOX.md, 2026-07-05; wrap 2026-07-05-install-plugin-crosscheck"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**`Import Plugin <slot> "<name>"` does not overwrite an occupied slot.** A round-trip verify that only checks "is *something* present in the slot" (any-occupant truthiness) will **false-positive** when the slot was already taken by a different plugin before the Import call ran — the slot reads as occupied either way, so a naive presence check can't tell "my import succeeded" from "someone else's plugin was already sitting there."

**Rule:** the verify read-back must compare the slot object's **`Name` == the expected plugin name** (not just presence/truthiness). This is the check implemented in `install_plugin`'s round-trip verify (2026-07-05 build, see the wrap).

**Premise to console-verify (status: verify):** the imported **pool object's `.Name` equals the folder name** used at import time (i.e., the plugin's folder/`<UserPlugin Path="…">` name, not some other label field). This has not yet been confirmed against a live console read — it's the working assumption the Name-match check depends on. Verifies via the reviewer's attended console-verify list: attempt an occupied-slot Import and read back `.Name` against the expected folder name.

History: none — found by a second-look Fable cross-check subagent review (not by the 67-green unit test suite in place at the time) and fixed same session, 2026-07-05.
