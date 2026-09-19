---
id: macro-call-and-nesting-lifetime-semantics
title: "Macro X.Y addressing calls ONE line, not 'start at line Y'; bare-called sub-macros share the parent's lifetime; nested calls do NOT block"
role: programmer
tags: [ma3, macro, v2.4]
when_to_load: "Before calling one macro from another, or before assuming a called sub-macro's timing/lifetime works like a function call — three gotchas apply"
status: active
source: "findings/INBOX.md, 2026-07-17 (forum threads 7844, 8456, 5998)"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

Three related gotchas about macros calling other macros:

**1. `Macro X.Y` addressing calls that ONE line as a standalone unit** — it does NOT mean "start macro X at line Y" (i.e. it doesn't begin executing macro X from line Y onward). MA dev Andreas corrected this live on the forum, 2023 (thread 7844).

**2. Lifetime differs by call style:**
- **Bare-called** sub-macros (referenced directly, not via `Call Macro`) share the PARENT macro's lifetime — they die if the parent stops or finishes first.
- **`Call Macro X`** gives the sub-macro an INDEPENDENT lifetime instead, decoupled from the parent.

**3. Nested/called macros do NOT block.** The parent's next line fires immediately — it does not wait for the sub-macro to finish. Two independent forum threads agree on this (8456 + 5998). **Fix:** pad the parent's `Wait` column to a duration sized to the sub-macro's real runtime, or move to Lua for real sequencing.

History: none — all three facts first captured 2026-07-17, macro deep-dive session.
