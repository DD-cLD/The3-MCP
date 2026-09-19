---
id: macro-xml-schema-cracked
title: "Macro XML schema cracked file-side from 13 factory samples: GMA3→Macro→MacroLine, Command/Wait/AddToCmdline/Execute, DataVersion 0.0.175.0–2.1.1.5 all import clean at 2.4.2"
role: programmer
tags: [ma3, macro, xml-schema, v2.4]
when_to_load: "Before hand-authoring or generating any macro XML file, or before trusting/rejecting an old-dialect macro file based on its DataVersion — QUOTE DIALECT IS LOAD-BEARING: read this before writing a single Command= attribute with an embedded quote"
status: active
source: "findings/INBOX.md, 2026-07-19 [0718-19cLD]; MACRO_LIB_CATALOG_v0.1.md §1 (13 factory files sampled verbatim from gma3_2.4.2/shared/resource/lib_macros); FAILURE MODE + retrieval-miss lesson added findings/INBOX.md 2026-07-23 [0723cLD]"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**The schema (cracked file-side, no console export needed):**

```xml
<?xml version="1.0" encoding="UTF-8"?>          <!-- UTF-8 BOM present -->
<GMA3 DataVersion="1.4.52.4">
    <Macro Name="World is Selection" Guid="...">   <!-- Guid OPTIONAL -->
        <MacroLine Command="Delete World 999 /NoConfirm" />
        <MacroLine Command="Store World 999" />
        <MacroLine Command="World 999" />
    </Macro>
</GMA3>
```

Root is `GMA3` + `DataVersion` — the same envelope every other export dialect uses (sequence, preset, patch) — **NOT** `<UserPlugin>` (plugins only, see `plugin-xml-schema`). `Macro` takes `Name` (required) and an OPTIONAL `Guid`. `MacroLine` attributes seen in the wild: `Command` (always present), `Wait="Go"`, `AddToCmdline="Yes"`, `Execute="No"`, plus an optional per-line `Guid`. **Absent attribute = default** (Execute=Yes, AddToCmdline=No, Wait=follow) — GUIDs are optional at both the Macro and MacroLine level (oldest factory files have none, newest have both), consistent with the proven GUID-strip→fresh-GUID import lane (see `xml-file-side-authoring-import-lane-proven`). **Inner quotes must be XML-escaped: `Command="Set Selection 1 MAtricks &quot;XShift&quot; &quot;-1&quot;"`.**

**⛔ FAILURE MODE — the `&quot;`-escaping rule above is LOAD-BEARING, not cosmetic (paid for hard, 2026-07-23 [0723cLD]):** a **raw double-quote character inside a single-quoted `Command` attribute is XML-legal and parses fine in Python** — and the import even **echoes OK** — but **MA3's own IMPORT silently truncates the Command string at the first raw quote**. Observed: `Command='Label Group 60 "cLD BACKLIGHT ALL"'` landed on console as the bare fragment `['Label]` — everything after the first raw `"` vanished. **Symptom signature:** truncated `Label`/`Store`-type fragments execute as stray standalone tokens (e.g. `[Illegal object:Fixture 'Store']`); groups get stored unlabeled or with default names, preset-store lines silently no-op. **Import always echoes OK regardless of the truncation — only a post-import LINE-READBACK DIFF (console Command strings vs. the authored file) or the Command Line History audit trail (see `console-cli-feedback-channels`) catches it; screen echo alone will not.** **Doctrine lint addition:** any authored macro XML needs an explicit quote-dialect check — double-quoted `Command` attrs, `&quot;`-escaped inner quotes, zero raw double-quote characters inside a single-quoted attribute — as a check distinct from structural/schema validation.

**Proven workaround idiom:** prefer inline `Store <Object> <n> "Name"` over a follow-up `Label` line — `Label` lines are exactly the line type this bug hits hardest. Full idiom (including its use outside the XML-quote context): `store-with-inline-name-labels-object-idiom`.

**Retrieval-miss lesson (2026-07-23):** this exact escaping fact already lived in this file's body (above) before a session hit the truncation bug — twice, in the same night. The miss was **not missing knowledge, it was missing retrieval**: this concept's INDEX line never surfaced the word "quote," so a mid-session task-type shift (desk-work → macro-authoring) never re-armed on it. See `authoring-gate-doctrine-retrieval-miss-lesson` for the standing process fix this drove. This is also the direct reason this concept's index line was rewritten to carry explicit quote/escaping trigger words — see the librarian's STAGING_REPORT for the proposed line.

**DataVersion range:** shipping factory files span **0.0.175.0 → 2.1.1.5** — a decade of dialect vintages — and all still import cleanly at 2.4.2. Old macro DataVersions are safe to import.

**Optional `DependencyExport` child:** macro XML can embed a `DependencyExport` block the same way sequence exports do (seen on POSITION_WIZ, which carries its "Red Back" Appearance this way — see `factory-position-wiz-anatomy-and-porting`).

**[VERIFY]** `Enabled` never appears in any of the 13 sampled files — presumed default-omitted like the other attributes, but this is not yet confirmed against a real console export (MACRO_LIB_CATALOG_v0.1.md §6 open item). Also **[VERIFY]**: both cLD-authored goldens referenced in the 2026-07-23 smith proof runs use a `MacroLine Name` attribute (e.g. `Name="CONFIRM GATE"`) not documented in this schema write-up — confirm whether `Name` is a real, meaningful `MacroLine` attribute or cosmetic, and fold it in.

**cLD MAker consequence:** the macro export dialect is now specifiable — same GMA3 envelope, a trivial line model — closing cLD MAker's remaining export-lane gap in principle (generation is unblocked whenever it's picked up).

Catalog + worked fixture: `MACRO_LIB_CATALOG_v0.1.md` (full write-up); `generated/factory_macro_fixture_circular_copy_x_plus.xml` (sample fixture). Closes the open item flagged in `macro-manual-gap-and-study-doc` and `macro-library-file-lane-and-bulk-authoring-workaround` — see both for what was true before the schema was cracked.

History: none — schema cracked and captured whole 2026-07-19, from 13 factory `lib_macros` files read file-side (no console export required). Extended 2026-07-23 [0723cLD]: added the ⛔ FAILURE MODE (raw-quote silent-truncation-on-import, symptom signature, catch lanes), the proven inline-Store-name idiom, the retrieval-miss lesson that drove this index-line rewrite, and a [VERIFY] flag on the undocumented `MacroLine Name` attribute.
