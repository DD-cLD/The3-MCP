---
id: patch-mvr-export-import-lane-and-schema
title: "MVR: export via the same Patch Export dialog (its default tab); import lives in PSR and CLEARS THE PROGRAMMER; zip schema with matrix-encoded position/rotation; embeds every patched type's GDTF as fixture-anatomy ground truth"
role: programmer
tags: [ma3, v2.4, patch, mvr, export, import, danger, gdtf]
when_to_load: "Before exporting or importing an MVR file, before writing/parsing an MVR's GeneralSceneDescription.xml, or before needing a fixture type's internal sub/channel anatomy without console or web access (the embedded GDTFs cover it)"
status: active
source: "findings/INBOX.md, 2026-07-14, console live-verified 2.4.2.2; repo manual 08 + 2.4 manual"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**Export:** the same Patch Export dialog used for grandMA3 XML (see `patch-xml-export-lane-and-schema`) has an **MVR format tab, and it's the dialog's default on every open** (the manual documents this default, and live behavior confirms it — the dialog does NOT remember a prior grandMA3-tab click across opens). Output path (exact filename pattern not yet captured — observed `<name>.mvr`):
```
gma3_library/mvr/
```

**Import — ⛔ danger:** MVR import lives in **PSR (Show Creator)**, and importing there **CLEARS THE PROGRAMMER** (documented in both manuals; not yet exercised live — only export has been run so far, so treat the import flow itself as manual-sourced until a live PSR run confirms it). Either way, treat any MVR-import step as destructive to whatever's live in the programmer.

**MVR file schema (from a live export/parse):** an MVR is a **zip archive** containing `GeneralSceneDescription.xml` plus per-fixture-type **GDTF** files. Each fixture's position and orientation are encoded as a **`Matrix` = {u}{v}{w}{o}** — four vectors, values in **millimeters**. `o` is the position vector; **`RotX` is derivable from the `v` basis vector via `atan2(v3, v2)`**. **Fixtures with no `Matrix` attribute are implicitly at the origin.**

**Why this matters as a verification lane:** the MVR being cleanly parseable makes it a **second, independent verification lane** alongside the grandMA3-XML diff — export both, compute the same fixture positions two different ways, and treat agreement as the confidence signal (see `export-diff-verification-loop`). It's also the ready exemplar for future PSR-import tooling work, since its schema is now captured.

**Context:** the repo's 08_PatchAndSetup manual's Patching section is a stub — it doesn't cover positions, CLI patch-position workflow, or this MVR lane at all, which is why both the export mechanics and the schema above had to be reverse-engineered live rather than looked up (see `patch-xml-export-lane-and-schema` for the parallel grandMA3-XML side and the CLI "Illegal object" bug).

**GDTF payload confirmed as fixture-anatomy ground truth (2026-07-15):** the embedded GDTF files aren't just present per-type — the MVR export carries **every patched fixture type's `.gdtf`** (a zip nested inside the MVR zip). This makes a single MVR export a **complete, file-side, console-and-web-free source of fixture anatomy**: each GDTF's geometry tree gives the sub/instance structure, and its DMX-mode section gives the channel map. Used in practice to build the JDC1 SPix channel map (see `jdc1-anatomy-ground-truth`; full tables in `WORKING/JDC1_SPIX_MAP_v0.1.md`) without touching the console or the web.

History: none — MVR export/import mechanics and schema were captured live in the same session, 2026-07-14, as the second verification lane for the template rig's final 3D positions (256/256 exact). 2026-07-15: confirmed the embedded-GDTF detail is complete (every fixture type, zip-in-zip) and used it as an offline fixture-anatomy ground-truth source for the JDC1 SPix map.
