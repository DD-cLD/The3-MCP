---
id: preset-range-export-open-ended-only
title: "A CLOSED preset range export silently no-ops ('Preset 4.1 Thru 4.103 /File' writes nothing) — the OPEN-ENDED form 'Preset 4.1 Thru /File' works; the echo lies either way"
role: programmer
tags: [ma3, cli, export, v2.4, gotcha, tourshow]
when_to_load: "Before exporting a preset range for census or baseline — a closed Thru bound produces no file while echoing success; census the disk, never the echo"
status: active
verified: grandMA3 onPC 2.4.2.2 (Mac), EU tour leg 2026-08
source: "findings/INBOX.md [0819-1cLD] 2026-08-19, colour-pool census on the tour file — file census caught it after the echo reported success"
supersedes: []
superseded_by: null
---

**Broken (silent no-op):**
```
Export Preset 4.1 Thru 4.103 /File "cld_colorpool.xml"
```
**Working:**
```
Export Preset 4.1 Thru /File "cld_colorpool.xml"
```

The closed upper bound kills the command. The console **echoes success in both cases** — the failure was caught only by listing the target directory and finding no file. This is the same never-trust-clean-echo family as the unquoted import filename (`import-file-argument-must-be-quoted`) and the phantom checkpoint (`saveshow-enumerate-headless-cancel-class`); the tour leg produced three independent instances of it.

**Working practice:** use the open-ended form and let the pool's own extent define the range, then verify the file exists and its byte size is plausible before treating it as a baseline. Pool-baseline exports are the insurance that made two rollbacks survivable this leg (`color-consolidation-crowning`, `venue-position-crowning-and-shell`), so a phantom one is expensive.

**Relation:** `export-sequence-writes-per-name-files` · `preset-pool-thru-range-syntax` · `import-file-argument-must-be-quoted`.

History: none — caught by file census, 2026-08-19.
