---
id: store-with-inline-name-labels-object-idiom
title: "Store <ObjectType> <n> \"Name\" labels the object inline at creation time — a separate Label line is unnecessary in builders"
role: programmer
tags: [cli-syntax, macros, idiom]
when_to_load: "Before writing a builder macro/CLI sequence that creates an object (Group, Preset, etc.) and needs it labeled"
status: active
source: "findings/INBOX.md 2026-07-23 [0723cLD] (PROVEN IDIOM, re-proven from GROUP_BUILDER precedent)"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**PROVEN IDIOM (re-proven, GROUP_BUILDER precedent):** `Store Group 60 "cLD BACKLIGHT ALL"` creates the object AND labels it in one command — a separate `Label` line is unnecessary in builders. This generalizes to other storable object types using the same `Store <Type> <n> "<Name>"` inline-name form.

**Corroborating evidence:** in the same session's v0.1.2 partial re-fire (a macro otherwise mangled by the quote-truncation bug — see `macro-xml-schema-cracked`), the quote-free `Store` lines using this idiom executed correctly even inside the damaged macro — `G61` export-verified with members `{55,57,58}`, Size=3, confirming the inline-name idiom itself is not what the quote bug breaks; it's specifically raw double-quotes inside XML `Command` attributes that break on import.

**Caution:** when this idiom is authored inside macro **XML** (not typed live at the CLI), the embedded quotes around the name MUST use the `&quot;`-entity escaping documented in `macro-xml-schema-cracked` — a raw double-quote in the XML `Command` attribute truncates the command silently on import. The idiom itself is sound; the transport (live CLI vs. authored XML) determines how the quotes must be written.

History: none — captured 2026-07-23 [0723cLD] digest run.
