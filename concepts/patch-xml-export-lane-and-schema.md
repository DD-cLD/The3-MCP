---
id: patch-xml-export-lane-and-schema
title: "Export Patch to grandMA3 XML: CLI keyword is Illegal object (repo manual 08 §9.2 is wrong for 2.4.2.2) — use the Patch Export dialog's grandMA3 tab instead; folder nesting + zero-attr-omission schema"
role: programmer
tags: [ma3, v2.4, patch, xml, export, danger]
when_to_load: "Before exporting a patch to grandMA3 XML, before trusting the repo manual's 08_PatchAndSetup CLI instructions for patch export, or before writing/parsing a patch XML file"
status: active
source: "findings/INBOX.md, 2026-07-14, console live-verified 2.4.2.2"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**The CLI route documented in the repo manual doesn't work.** `Export` can't address `Patch` as a CLI object — it fails with **"Illegal object"** on 2.4.2.2. The repo's **08_PatchAndSetup manual's §9.2 CLI line for this is wrong for 2.4.2.2** (its Patching section is otherwise a stub — positions and CLI patch-position workflow aren't covered there at all, which is why this had to be reverse-engineered live). `Menu "Patch"` does correctly open the patch menu from the CLI as a way in.

**The working route is the Patch Export dialog:** format tabs **grandMA3 | MVR** × scope tabs **EntirePatch | SelectedFixtures**. **The dialog resets to MVR format on every open** (the manual documents MVR as the default, and live behavior confirms it) — click the **grandMA3 tab explicitly, every time**, or the export silently comes out as a `.mvr` instead (see `patch-mvr-export-import-lane-and-schema`). grandMA3-format output path:
```
gma3_library/patch/stages/<name>.xml
```

**Name-field behavior:** `Cmd+A` select-all works in the dialog's name field. **Triple-click does NOT select/grab the `<Default>` placeholder token** — a paste at that point appends to it instead of replacing it. Clear the field with `Cmd+A` before pasting a name; don't rely on triple-click.

**grandMA3 patch XML schema (from a live export):** folder structure is represented as nested `<Fixture>` nodes (per `Mode 5.Grouping`). **`PosX`/`PosY`/`PosZ`/`RotX`/`RotY`/`RotZ` attributes are omitted entirely when their value is zero** — absence means zero, not an error or an unset value. The `RotX` attribute's string value carries a **leading space** in its serialized form, e.g. `" -90.00"`.

History: none — export mechanics, the CLI bug, and the XML schema were all captured live in the same session, 2026-07-14, while exporting the template rig's patch for position verification.
