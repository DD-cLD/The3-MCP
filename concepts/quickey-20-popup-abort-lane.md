---
id: quickey-20-popup-abort-lane
title: "`Quickey 20` — Dave's custom CLI keyword that fires an Esc dismissing any popup/stray window; the sanctioned computer-use popup-abort lane"
role: programmer
tags: [ma3, computer-use, cli, v2.4, danger]
when_to_load: "Before scripting any computer-use interaction that might need to abort a stuck popup, dialog, or stray floating window on the MA3 console — this is the tool to reach for, never a synthetic Escape keypress"
status: active
source: "findings/INBOX.md, 2026-07-16 (three convergent mentions: build/first-use, live popup-kill, edit-session clarification)"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

Dave built a custom console Quickey — **`Quickey 20`** — specifically for cLD's computer-use work. Typing `Quickey 20` on the CLI fires an Esc that dismisses **ANY** popup or stray floating window — live-verified tonight when it killed a stray floating window mid-session.

**Why it exists:** synthetic Escape keypresses are dead at the console layer, the same family of constraint as `synthetic-text-input-rejected-by-command-line` (the console rejects computer-use's synthetic input across multiple channels, not just text). `Quickey 20` is the sanctioned workaround — a real console-side keyword typed through the normal Edit Command popup loop (see `computer-use-input-loop`), which the console itself translates into a genuine Escape that DOES reach the popup layer.

**Scope — what it dismisses vs. what it doesn't:** it dismisses general popups and stray windows. It is a separate, adjacent mechanic from exiting a preset/recipe **Edit session's edit mode** — see `edit-session-mechanics-and-contamination-risk` for that: Escape/`Quickey 20` does turn edit mode off, but the values it pulled into the programmer are NOT cleared by it (that needs a separate `ClearAll`). One source mention phrased this as Quickey "not closing the Edit session banner" — read together with the other two mentions, the resolved understanding is the mode/values split just described, not a claim that Quickey fails on edit-session popups generally.

**Standing tool:** use `Quickey 20` instead of guessing at exits or attempting a synthetic Escape.

History: none — introduced and used live 2026-07-16, first session it existed.
