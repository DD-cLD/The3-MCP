---
id: off-on-overwrite-executor-default
title: "off_on_overwrite is the default executor behavior in MA3"
role: programmer
tags: [ma3]
when_to_load: "When reasoning about what happens if a running executor is re-triggered or overwritten, or when authoring executor behavior explicitly"
status: active
source: "MEMORY §MA3 v2.3 Technical Rules, 2026-04-01"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

`off_on_overwrite` is the **default executor behavior** in grandMA3 — i.e. absent an explicit override, an executor that gets overwritten while running will turn off then on with the new content, rather than crossfading or ignoring the overwrite.

History: none — stable since 2026-04-01.
