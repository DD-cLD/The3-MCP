---
id: macro-handle-persistent-object-reference
title: "Handles #[Object] — persistent object reference that survives rename/renumber"
role: programmer
tags: [ma3, macro, cli, v2.4]
when_to_load: "Before hard-coding an object reference inside a macro that might get renamed or renumbered later — Handles are the survives-renumber alternative"
status: active
source: "findings/INBOX.md, 2026-07-17 (official manual + forum thread 9119)"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

`#[Object]` creates a **Handle** — a persistent reference to that object that keeps resolving correctly even after the object is renamed or renumbered (unlike a bare number/name reference, which breaks).

**Command editor "Create Handle" toggle** auto-converts the last object reference typed into a Handle.

**Multi-object handle refs** need the object keyword repeated per number — there's **no `Thru`-range shorthand** for handles (unlike a normal reference, where `Fixture 1 Thru 10` works fine).

**File-side (XML) form, added 2026-07-19:** in stored macro XML, Handles appear as raw hex references (`#000000027e001379`-style). This form is **show-specific** — imported into a different show, these hex refs dangle or resolve to the wrong object. Any port of a macro containing Handle references must replace every `#...` line with explicit `Group <n>` / object calls before it's safe to run elsewhere. This was THE key porting caveat for POSITION_WIZ (see `factory-position-wiz-anatomy-and-porting`) and applies to any handle-bearing macro.

History: none — first captured 2026-07-17, macro deep-dive session. Extended 2026-07-19: added the XML/hex-ref serialization form and its show-specific porting caveat, found reading POSITION_WIZ.xml file-side.
