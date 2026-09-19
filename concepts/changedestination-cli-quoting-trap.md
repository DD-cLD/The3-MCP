---
id: changedestination-cli-quoting-trap
title: "ChangeDestination requires a quoted object name — a bare number fails (\"Failed:ChangeDestination 1\"); an unquoted stray like \"cd1\" gets parsed as Fixture \"cd1\" — a dictation-artifact trap"
role: programmer
tags: [ma3, cli, dictation-artifact, paid-for-lesson]
when_to_load: "Before generating or dictating a ChangeDestination command — bare numbers fail outright, and unquoted shorthand tokens silently get reinterpreted as a Fixture reference instead of erroring"
status: active
source: "findings/INBOX.md, 2026-07-17, live 2.4.2.2"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**Bare number fails outright:** `ChangeDestination 1` returns **`Failed:ChangeDestination 1`** — a bare numeric argument is not accepted.

**Quoted object name works:** `ChangeDestination "cld chase gaps"` is the correct form — the destination must be a quoted object name string.

**Dictation-artifact trap:** an unquoted stray token like `cd1` does not error — it gets silently parsed as **`Fixture "cd1"`**, a different command entirely with no relation to `ChangeDestination`. This is a live trap for voice-dictated CLI generation: a garbled/abbreviated destination name doesn't fail loudly, it fails by *executing a different, plausible-looking command*.

**Rule of thumb:** always quote the `ChangeDestination` target as a full object name string, and treat any short/abbreviated token in a dictated command as suspect until verified against the intended object — a clean-looking echo can still mean the wrong command ran (see `set-command-unknown-property-fails-silently` for the sibling "clean prompt ≠ success" doctrine).

History: none — first paid for live, 2026-07-17.
