---
id: device-file-hunt-full-sweep-law
title: "DEVICE HUNT LAW (Dave): hunt files with ONE comprehensive sweep from the top of the allowed roots — never serial single-path probes off remembered paths, because mounts and repo roots drift between sessions"
role: operational-live
tags: [process, tooling, tourshow]
when_to_load: "Before looking for any repo/project file on the device from a fresh session — especially INBOX, wraps, staging folders — and immediately if a remembered path 'doesn't exist'"
status: active
verified: EU tour leg 2026-08
source: "findings/INBOX.md [0808-1cLD] 2026-08-08, Dave teach ('full seal sweep')"
supersedes: []
superseded_by: null
---

**Dave's teach, paraphrased:** when hunting for a file on the device, run **one comprehensive sweep from the top of the space** — search the allowed roots — rather than a string of single-path probes off paths remembered from a previous session. **Mounts and repo roots drift between sessions**; a remembered path that fails tells you nothing about whether the file exists.

**The failure this prevents:** filing into a stale copy. Ground truth established the same day —

- **live INBOX = `My Drive/Documents/MA_PROGRAMMING/WORKING/findings/INBOX.md`**
- `cld_maker_sandbox/REVIEW/corpus/findings/INBOX.md` is a **2026-07-21 snapshot, STALE — never file there.**

A serial probe would have found the stale copy first and written to it silently.

**Compounding hazard:** the same directories are Drive-synced, where list tools already false-negative and staged copies can read stale — see `glob-false-negative-on-drive-synced-dirs`. A full sweep plus a live `ls`/`grep` cross-check is the pair that gets to truth.

**Relation:** `glob-false-negative-on-drive-synced-dirs` · `project-file-locations` · `empty-census-deserves-selector-suspicion`.

History: none — taught and applied 2026-08-08.
