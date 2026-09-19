---
id: manual-index-vocabulary-is-curated
title: "Manual search index vocabulary is hand-curated (build_index.py), not a full-text dump — misses are curation gaps, not path bugs"
role: operational-live
tags: [mcp, process]
when_to_load: "When manual_lookup(keyword) returns 0 hits for a term that should obviously be in the MA3 manual — before suspecting a path/index-build bug"
status: active
source: "findings/INBOX.md, 2026-07-05; wrap 2026-07-05-restart-gate-021-ship"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**Symptom (2026-07-05, restart-gate smoke):** `manual_lookup('SaveShow')` returned **0 hits** while Store/OSC-related lookups hit richly in the same session. Looked like an index-coverage gap or possibly a path error — the indexed set behaved like it covered curated reference docs, not the full `MA_V2.4.2_MANUAL`.

**Root cause, confirmed same session:** the manual index's vocabulary is **hand-curated by hand in `build_index.py`** — the build script's own convention is "add keywords when a release introduces them." `SaveShow` was missing because nobody had added it to the curated keyword list yet, **not** because of a path bug, a stale index, or a build failure. As of 2026-07-05 the curated set holds **156 keywords**.

**Practical consequence:** any long-tail manual lookup can silently return 0 hits for a term that genuinely exists in the manual, simply because it hasn't been added to the curated vocabulary. Two ways to close a specific gap:
1. **Fallback lookup** — server 0.2.1 shipped a `manual_lookup` grep-fallback: a bounded word-boundary live scan over source docs for curated-vocabulary misses, with meta-docs (CHANGELOG/HANDOFF etc.) explicitly excluded from being served as "manual" hits. See `crosscheck-subagent-pattern`'s 2nd data point for a gap the cross-check caught in this exact fallback (meta-docs almost leaked through before exclusion was tightened).
2. **Vocabulary add** — add the missing keyword(s) to `build_index.py`'s curated list and regenerate `INDEX.search.json` (see `project-file-locations` for the index path). This is the durable fix; the fallback is the safety net for terms nobody's added yet.

**Open candidate (not yet actioned as of this wrap):** add `SaveShow` (and any other missing CLI keywords) to the curated vocabulary and regenerate — carried as a 1-liner suggestion for Dave in the 2026-07-05 restart-gate-021-ship wrap.

History: none — first-observed and root-caused same session, 2026-07-05 (restart-gate-021-ship). Supersedes no prior concept; this is the first concept to document the manual index's curation model explicitly (the model itself — path map, regen command — already lived in `project-file-locations`, but not the "curated, not exhaustive" behavioral fact).
