---
id: release-mechanism-fundamentals
title: "Release = special function on any channel — falls back to the next claim (running cue, else fixture default) instead of forcing zero"
role: programmer
tags: [ma3, doctrine, release, v2.4]
when_to_load: "Before building any Release preset, bump executor, or TC-bump architecture — defines what Release actually does at the channel level"
status: active
source: "findings/INBOX.md, 2026-07-16 (Dave, dictated live, [0716-1cLD] session)"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

Dave's definition, the base mechanism everything else in this domain builds on: **Release is a special function assignable to ANY channel.** Instead of writing a zero value, it RELEASES the channel — the channel falls back to whatever else is claiming it: the running cue underneath if one exists, otherwise the fixture's default value.

This is the console mechanism that `release-preset-design-doctrine` (our preset-building pattern) and `tc-bump-button-architecture` (bumps exit via Release, not Off) both depend on. See `release-family-ships-stock` for confirmation that stock presets built on this mechanism already ship in pool 21.

History: none — mechanism defined 2026-07-16, first capture in the corpus.
