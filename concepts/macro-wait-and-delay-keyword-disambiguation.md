---
id: macro-wait-and-delay-keyword-disambiguation
title: "Three distinct 'wait' keywords in MA3 (macro-line Wait, /Wait option, CommandDelay) — don't conflate; macro-line Wait='Go' is a third pacing mode"
role: programmer
tags: [ma3, macro, cli, v2.4]
when_to_load: "Before writing or reading ANY 'wait'/'delay' keyword in MA3 — macro-line Wait column, the /Wait option keyword, and CommandDelay are three unrelated mechanisms with overlapping names"
status: active
source: "findings/INBOX.md, 2026-07-17 (macros.html; Dave corroborated live-knowledge)"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**Three distinct "wait" keywords — do not conflate:**
1. **Macro-line `Wait` column** — pacing between lines within a macro.
2. **`/Wait` option keyword** — latency in milliseconds for `Store`/`Reboot`/`Restart`/`Shutdown`.
3. **`CommandDelay`** — delay before a cue's own embedded CMD line fires on playback.

A fourth, unrelated same-named term: the plain **`Delay`** keyword is a completely different, fixture-attribute fade-delay concept — don't fold it into the "wait" family above.

**Macro-line `Wait` column has three pacing modes** (official `macros.html`; Dave corroborated from live console knowledge):
- **Numeric seconds value** — waits that many seconds before the next line.
- **`Follow`** — effectively wait 0 (falls straight through).
- **`Wait="Go"`** — halts the macro after that row until it receives a new Go+; re-firing the macro steps it forward exactly one line. [CONFIRMED official + Dave operator]

History: none — first captured 2026-07-17, macro deep-dive session.
