---
id: layout-element-defaults-tab-is-user-profile-wide
title: "DANGER: the Layout editor's \"Layout Element Defaults\" tab edits USER-PROFILE-WIDE defaults (Edit UserProfile 1 'Default'.LayoutElementDefaultsCollect), not the current layout"
role: programmer
tags: [ma3, v2.4, layout, crash]
when_to_load: "Before clicking into the Layout editor's Layout Element Defaults tab — a stray edit there changes every future element's defaults, not just the layout you're working on"
status: active
source: "findings/INBOX.md, 2026-07-14, console live 2.4.2.2"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**Danger area:** the Layout editor's **"Layout Element Defaults"** tab actually opens **`Edit UserProfile 1 'Default'.LayoutElementDefaultsCollect`** — this is **user-profile-wide**, not scoped to the layout you're currently editing. A stray click/edit here **rewrites the defaults for every future element you ever create**, in any layout.

**Treat this tab as read-only reference.** Do not make changes there unless the intent is specifically to change the standing user-profile defaults for all future layout elements.

**Dave's rule (feedback, generalizes beyond this tab):** take a **good backup BEFORE any mass property change** — `SaveShow /Enumerate` first. See `saveshow-enumerate-versioning` for the versioned-save mechanics.

History: none — danger area identified live 2026-07-14; no incident occurred (caught before a stray edit happened), but flagged as a standing hazard.
