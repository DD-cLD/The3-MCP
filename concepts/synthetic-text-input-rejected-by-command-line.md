---
id: synthetic-text-input-rejected-by-command-line
title: "MA3's docked command line rejects ALL synthetic text input, not just voice dictation"
role: programmer
tags: [ma3, computer-use]
when_to_load: "Before attempting any automated/synthetic text entry into the MA3 command line — via voice dictation, computer-use type actions, or any non-physical-keystroke input method"
status: active
source: "MEMORY §MA3 v2.3 Technical Rules, 2026-04-01 (generalized 2026-07-04)"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

Original 2026-04-01 finding: Wispr Flow voice dictation doesn't reliably work in the MA3 command line input field.

**Generalized 2026-07-04:** the docked command line rejects **ALL synthetic text**, not just voice dictation output — this is a broader input-method constraint, not a Wispr-specific quirk. Confirmed during the v2.4 computer-use session: synthetic `type` events do not land in the docked command field at all, while **real key events DO reach the shortcut layer** (see `computer-use-input-loop` for the working workaround via the on-screen keyboard icon and Edit Command popup).

History: generalized 2026-07-04 from a Wispr-Flow-specific note (2026-04-01) to a general synthetic-text-input constraint, after the computer-use session confirmed the same rejection applies to `type` actions, not just dictation.
