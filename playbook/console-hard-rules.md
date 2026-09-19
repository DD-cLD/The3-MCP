---
id: console-hard-rules
tags: [ma3, playbook, hard-rules, console-truth]
verified: grandMA3 onPC 2.4.2.2 (Mac)
---
# Console hard rules — always in force

Extracted from the operating memory core. Each rule is the one-line form; the
mechanism, the failure that scoped it, and the receipts live at the concept id
named on the rule's line, in `concepts/`.

These are not style preferences. Every one of them was written after something
broke on a live desk.

> **Pointer status (2026-09-19, v0.1 release).** All 13 concept ids cited below
> resolve in `concepts/`. `tc-targeted-sequence-delete-eats-events` (rule 13)
> ships with frontmatter added at release; upstream it survives only as its
> 2026-08-05 extension block, and the file says so in its `source:` line.
> Rules stand on their own text; the id is where the receipts live, not a
> dependency.

1. **Never call `GetPresetDataFast()`** — segfaults 2.4.2.2, pcall can't catch it. → `gpdf-console-killer`
2. **SaveShow before big moves AND before every handwritten-XML Import; always `/NoConfirmation`; `LoadShow` stays denied.** → `saveshow-discipline-and-mcp-tier`
3. **An MCP timeout may be a console crash** — confirm via `get_console_info`; changed PID = crash+relaunch. → `segfault-manifests-as-mcp-timeout`
4. **MAtricks phase is LITERAL** — apply the formulas manually (full spread: `360 − 360/N`); never trust encoder-bar values for pool storage. → `phase-math-formulas`, `mtricks-phase-vs-encoder-phase`
5. **Macro lines: one command each, no `;` batching** (interactive CLI *does* batch). → `macro-line-syntax-and-batching-rule`
6. **Stock pools only** (Dimmer = `Preset 1.x`, Color = `Preset 4.x`) unless a fantastic reason. → `pool-discipline-stock-vs-custom`
7. **OSC carries nothing without an active Session.** → `osc-session-required-for-traffic`
8. **Uploads are session-mortal** — copy incoming files into the repo before wrap.
9. **Memory files are the crown jewels** — they outlive every show file; the librarian supersedes, never deletes.
10. **Patch `Set` commands: ONE property per Set, QUOTE every value.** Chained props silently drop; bare negatives silently flip sign (−0.5 applied as +0.5). → `patch-set-one-prop-quoted-values`
11. **No `Go+` / no console write-chain without an explicit "desk clear?" callout and Dave's clear-to-fire.** The console is ONE shared command surface — MCP writes land in whatever context the desk currently has open. → `desk-clear-callout-before-console-write-rule`
12. **A clean Import proves NOTHING below the structure layer — run a BINDING census** (object-level `:Get()` readback per line). Import resolves name-paths by THREE different rules: `Selection=`/`MAtricks=` want the short `Default.` form; `Preset=`/`Values=` want the long form with the pool's LIVE name and parse numeric name tokens as SLOT INDEXES (`Dimmer.0`=nil; write `Dimmer.15`); `&apos;`-quoting kills all of them. Golden exports carry stale pool names (survive on GUIDs) — dialect-test on scratch seq 1990 before any new attribute. → `import-resolver-laws` 
13. **Deleting a TC-targeted sequence eats the track's events** — target MOVES preserve events, deletes don't. Cutover is the LAST act of a build; {LD} sequences are export-for-inspection-only; TC census counts EVENTS per track, not just Targets. → `tc-targeted-sequence-delete-eats-events`
14. **Multi-part Part attrs must clone the desk-export order** (SpeedScale between MAgic and Mode, on every part) — out-of-position attrs make the importer absorb each cue's first content part into part 0, silently. Lint can't see it; ET-gate + export-back census can. → `part-attr-order-import-absorption-gotcha`
