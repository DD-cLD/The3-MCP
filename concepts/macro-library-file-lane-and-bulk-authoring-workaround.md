---
id: macro-library-file-lane-and-bulk-authoring-workaround
title: "Macro library file location + import CLI; bulk-authoring workaround (build one, export, edit XML, reimport) since the macro XML schema itself is still uncracked"
role: programmer
tags: [ma3, macro, xml, v2.4]
when_to_load: "Before importing a macro library, locating macro XML files on disk, or trying to bulk-author many macros at once"
status: active
source: "findings/INBOX.md, 2026-07-17 (MA staff-confirmed workaround, forum thread 5283)"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**File location — CORRECTED 2026-07-19, version-scoped:** `gma3_2.4.2/shared/resource/lib_macros/` (207 XML files) — one macro per XML file. This is also where MA's factory/predefined macros live (e.g. `help context sensitive.xml`). The path is versioned per install; an earlier note recorded it as `grandma3/shared/resource/lib_macros`, which was imprecise.

**Import CLI:** `ChangeDestination Macro` (or `CD Macro`) → `Import Library "*.xml"` → `ChangeDestination Root`. The wildcard imports every XML file in the targeted library folder. **Correction to older forum assumption:** the DataPool path segment is the pool's ACTUAL name (e.g. `"Default"` in a fresh show) — it is not always literally `"Global"` as older forum posts assumed.

**Bulk-authoring workaround (MA staff-confirmed):** build one macro by hand, export it, edit the XML directly (search/replace), reimport. Same lane already proven for preset/sequence XML authoring (see `xml-file-side-authoring-import-lane-proven`). **Update 2026-07-19: the macro XML schema is no longer uncracked** — it fell out file-side from 13 of these 207 factory files, no console export needed. See `macro-xml-schema-cracked` for the schema itself; this closes the open item forum thread 5283 flagged.

History: first captured 2026-07-17, macro deep-dive session. Extended 2026-07-19: version-scoped path correction (207 files, from `grandma3/...` to `gma3_2.4.2/...`) and the schema-cracked resolution folded in (see `macro-xml-schema-cracked`).
