---
id: beatgrid-keydown-guard-scoped-to-text-entry
title: "beatgrid.html keydown guard now scoped to text-entry fields only — a focused checkbox no longer eats H/all keyboard shortcuts"
role: tools
tags: [beatgrid]
when_to_load: "Before adding a new global keyboard shortcut to beatgrid.html, or when a shortcut mysteriously stops firing after a checkbox/select gains focus"
status: active
source: "findings/INBOX.md 2026-07-07 + wrap 2026-07-07-beatgrid041-daysshow-tourintake [0707cLD]"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

- **Bug (Dave live-diagnosed it):** a focused checkbox ate H and all other keyboard shortcuts until focus moved elsewhere. **Root cause:** the keydown guard blocked key events from **ALL** `<input>` elements, not just text-entry ones.
- **Fix:** only **text-entry fields** swallow keydown events now; **checkboxes and selects blur on change**, so focus doesn't linger and block shortcuts afterward.
- **Test coverage:** the DOM-stub harness now covers this guard matrix explicitly (see `beatgrid-dom-stub-test-harness` — this fix brought the suite to 37 green assertions, on the way to the session's final count of 45).

History: none — diagnosed and fixed same session, 2026-07-07.
