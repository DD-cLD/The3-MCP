---
id: command-enabled-property-name-gotcha
title: "Property name is CommandEnabled, not CommandEnable — toggling a cue's CMD line with the shorter name silently fails"
role: programmer
tags: [ma3, cli, naming-precision, v2.4]
when_to_load: "Before Setting a cue's CMD-line enable property — the correct property name is CommandEnabled; the shorter guess fails silently"
status: active
source: "findings/INBOX.md, 2026-07-17 (forum thread 8253)"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

The property name for toggling a cue's CMD line on/off is **`CommandEnabled`** — NOT `CommandEnable`. The shorter, more "natural"-sounding name **fails silently**: no error, no effect, clean prompt.

Same family as the pinned `patch-set-one-prop-quoted-values` naming-precision gotcha and `set-command-unknown-property-fails-silently` (unknown/wrong property names on `Set` fail silently with no echo). Different object domain (cue CMD line vs. patch fixtures), same underlying lesson: **never trust a clean `Set` prompt on a property name you haven't verified** — always confirm by readback.

History: none — first captured 2026-07-17, macro deep-dive session, forum thread 8253.
