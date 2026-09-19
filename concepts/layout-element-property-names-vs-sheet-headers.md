---
id: layout-element-property-names-vs-sheet-headers
title: "Layout element sheet column headers are NOT always the real property names — the border-visibility toggle is \"VisibilityBorder\", not \"Border\""
role: programmer
tags: [ma3, cli, v2.4, layout]
when_to_load: "Before writing a Set Layout command targeting a layout element's visibility/border/ID properties — the sheet's column header is not reliable as the literal property-name string"
status: active
source: "findings/INBOX.md, 2026-07-14, console live 2.4.2.2"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**The gotcha:** the layout element sheet displays a column header of just **"Border"** (grouped under a "Visibility" heading) for the border on/off toggle — but that header is **not** the property's real name. The actual property name, confirmed live, is **`"VisibilityBorder"`** (`Visible`/`Hidden` enums). **Headers ≠ property names** — do not assume a sheet column's displayed label is what you pass to `Set`.

**Full element visibility family** (confirmed): `VisibilityElement` / `VisibilityBar` / `VisibilityObjectName` / `VisibilityID` / `VisibilityCID` / `VisibilityValue` / `VisibilityIcon` / `VisibilityIndicatorBar` / `VisibilitySelectionRelevance` / `VisibilityBorder` — reflecting the pattern `Visibility<Element>`. (Verbatim from source: "VisibilityElement/Bar/ObjectName/ID/CID/Value/Icon/IndicatorBar/SelectionRelevance/Border" — read as the `Visibility` prefix applying across that slash-separated list.)

**Separate, genuinely-named styling properties** (found directly as sheet columns, not affected by the header/property mismatch above): **`"BorderSize"`** (observed value `2`), **`"BorderColor"`** (observed value `999999FF`).

**Other sheet columns seen** (not yet individually confirmed as literal property-name strings, since the "Border" case shows headers can differ from names): Bar, ObjectName, ID, Icon, Value, IndicatorBar, SelectionRect, ObjectText, CustomText, FullResolution.

**[VERIFY] PositionX vs PosX:** a forum post (hoss, forum #3991) gives the position property as **`"PositionX"`**: `Set Layout 1.2 "PositionX" 500`. The finding as recorded states "both PositionX and PosX work on 2.4.2.2" — but this confirmation traces to the forum post, not an independent console readback in this session (unlike `"PosX"`/`"PosY"`, which this session's own `Assign Layout`/`Used`-bounds work directly exercised and verified — see `layout-cli-assign-and-posxy-syntax`). Treat "PositionX works as an alias" as **verify**, not fully console-confirmed by us, until a live `Set ... "PositionX"` + readback is run and checked directly.

**Always verify any property set by readback** — `Set` with a wrong/unknown property name fails silently. See `set-command-unknown-property-fails-silently`.

History: 2026-07-14 same-day correction — an earlier pass in this session listed "Border" (default Off) as if it were the literal toggle property name; a closer look at the same element sheet corrected this to `VisibilityBorder`, with "Border" being only the displayed column header. Folded into one file per the librarian's correction-collapse rule.
