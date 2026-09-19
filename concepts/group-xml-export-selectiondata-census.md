---
id: group-xml-export-selectiondata-census
title: "`Export Group <n>` writes full SelectionData (per-item ID + X/Y/Z grid coords) to XML — a numeric census + shape-verification lane for Groups"
role: programmer
tags: [ma3, cli, export, group, verification, v2.4]
when_to_load: "Before trusting a Group build (especially a multi-paste or GS-propagated one) without export-verifying it — this is the group-level counterpart to the grandMA3-XML/MVR diff loops used for patch and layout"
status: active
source: "findings/INBOX.md, 2026-07-15, console live 2.4.2.2"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**`Export Group <n>`** writes to `gma3_library/datapools/groups/<name>.xml`, with a full `<SelectionData Size...>` block containing a per-`<Item>` `ID` plus `X`/`Y`/`Z` grid coordinates for every member.

**Proven live:** used to census a built Group — caught missing fixtures (407/408 silently absent from a multi-paste build) AND numerically verified every present block's coordinates against the intended layout. Extends the existing `export-diff-verification-loop` pattern (patch/layout) to **Groups** as a third verification lane.

**Bridge:** Desktop-Commander reads the exported XML Mac-side for inspection.

**Filename gotcha:** MA3 lowercases and underscores the Group name for the export filename — e.g. a group named `cLD` exports as `c_ld`.

**Why Export is the ONLY reliable member census (paid for 2026-07-21):** `handle:Children()` returns **0** for GROUP objects — a group's members live in its SelectionData, not as pool child handles, so `:Children()` (which only gives a line-count on Macros) cannot count them. A related Lua-handle trap hit the same readback: `.Count` is a **METHOD, not a property** — `handle.Count` returns a function (live concat error); use `handle:Count()` or `#handle:Children()`. Net: for group member census the ONLY reliable readback is `Export Group` → read the `SelectionData Size` attr from the XML (proven on G51/101/109/601). Never try to census a group via `:Children()`.

History: none — export lane proven live in one session, 2026-07-15, catching a real silently-dropped-fixture bug (see `paste-round-verification-protocol` for the paste-hygiene half of this same finding). Extended 2026-07-21: pinned WHY this is the only lane — `:Children()` returns 0 for groups and `.Count` is a method, so Lua-handle census fails; Export is the reliable path.
