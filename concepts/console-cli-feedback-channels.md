---
id: console-cli-feedback-channels
title: "Three lanes for reading CLI feedback: the docked line's inline color echo, the Display-2 Command Line History window (click-to-copy), and the History window's per-line macro-execution audit trail"
role: programmer
tags: [ma3, computer-use]
when_to_load: "When you need to verify whether a just-sent command succeeded or failed, want to reuse/copy a prior command line, or need to audit what a builder macro actually executed line-by-line after a Go+"
status: active
source: "findings/INBOX.md, 2026-07-10, console live 2.4.2.2; audit-lane extension findings/INBOX.md 2026-07-23 [0723cLD]"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**Lane 1 — docked command line inline color feedback:** the docked command line shows its **last response inline, colored** — **red = error**, **magenta = echo**. This is usable success/fail feedback for a just-sent command **without needing a Command Line History window open at all**.

**Lane 2 — Command Line History window (Display 2):** Dave swapped Display 2 to a Command Line History window mid-session (2026-07-10) — this fulfills the **cLD Program view spec's non-negotiable History-window element**, now existing live rather than just specified. **Hover hint observed on a history line:** "Click on a line to copy it back into the command line."

Use Lane 1 for a quick glance at the immediately-preceding command; use Lane 2 (when available on Display 2) to scroll back further or to copy an earlier command back into the docked line.

**Lane 3 — per-line macro-execution audit trail (2026-07-23 [0723cLD]):** running a macro (e.g. via `Go+ Macro n`) logs **every line** of that macro to the Command Line History, each prefixed `(Macro N 'name')` followed by either `OK:<cmd>` or `Illegal object:<cmd>` (or similar). This is a genuine **per-line builder-run audit trail** — not just a log of the top-level `Go+` call. **New standing verify (2026-07-23):** after every builder-macro `Go+`, read the History tail (or do a line-readback diff of the authored file against console Command strings) **alongside** the usual object census — this is the only reliable way to catch a macro that ran but silently fragmented or misfired mid-line (see `macro-xml-schema-cracked`'s quote-truncation failure mode for exactly the kind of bug this catches that a clean top-level echo would miss).

**Note:** none of the three lanes substitutes for a readback verification of a `Set` command's actual effect — see `set-command-unknown-property-fails-silently`, since a clean/non-error echo does not prove an unknown property name actually took effect.

History: none — both lanes observed/confirmed live 2026-07-10. Extended 2026-07-23 [0723cLD]: added Lane 3, the Command Line History's per-line macro-execution audit trail (`(Macro N 'name')OK:cmd` / `Illegal object:...`), discovered as the catch lane for the same-day macro quote-truncation bug — now a standing post-Go+ verify step alongside object census.
