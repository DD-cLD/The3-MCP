---
id: cue-display-number-vs-no-addressing-gotcha
title: "MA3 stores a cue's display number ×1000 as its internal .no — single-cue CLI/Lua addressing needs the DISPLAY number (Cue 5), not .no (Cue 5000 returns nil); wildcard Cue * enumerates BY .no"
role: programmer
tags: [ma3, cli, cues, v2.4]
when_to_load: "Before addressing a single cue by number via CLI or Lua, or before interpreting a wildcard Cue * enumeration's numbering"
status: active
source: "findings/{FESTIVAL}/FESTIVAL_FINDINGS_v0.1.md [0722cLD] 2026-07-22, console notes, live 2.4.2.2"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**The gotcha:** MA3 stores cue **5.000** internally as `.no` **5000** (the display number × 1000, leaving room for decimal sub-cues like 5.1, 5.2). **Single-cue addressing needs the DISPLAY number** — `Cue 5` — not the internal `.no` value: `Cue 5000` resolves to **nil**.

**Wildcard behavior differs:** `Cue *` (wildcard enumeration) returns cues addressed **BY `.no`** — i.e. the wildcard census surfaces the internal ×1000 numbering, not the display numbers. Don't assume the two addressing conventions match just because they're both "cue numbers" — single-object addressing and wildcard-enumeration addressing use different number spaces here.

**Relation:** parallels other MA3 dot-scaled internal-vs-display numbering traps in the corpus (e.g. `phaser-preset-xml-measure-speed-fixed-point-encoding`'s 2^24 fixed-point encoding) — internal storage often scales a display value, and code/CLI that assumes 1:1 will silently fail (nil) rather than error loudly.

History: none — observed live in one session, 2026-07-22, working {FESTIVAL}'s cue structure via Lua/CLI.
