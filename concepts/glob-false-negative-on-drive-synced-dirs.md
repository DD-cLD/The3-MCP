---
id: glob-false-negative-on-drive-synced-dirs
title: "Glob/list false-negatives, Read-tool stale-cache reads, AND device_stage_files stale-container-copy reads on Drive-synced directories — verify with ls/live grep/byte-size before trusting any of them"
role: operational-live
tags: [process]
when_to_load: "Before concluding a directory is empty (or that files were lost) from a Glob/list-tool result, before trusting a Read-tool result that looks stale/wrong, OR before editing based on a device_stage_files-staged copy of a file inside a Google-Drive-synced folder (e.g. WORKING/wraps, WORKING/concepts, WORKING/findings) — cross-check with ls/live grep/byte-size comparison first"
status: active
source: "findings/INBOX.md, 2026-07-05 and 2026-07-08; wrap 2026-07-05-restart-gate-021-ship; third symptom (stage-lane) added findings/INBOX.md 2026-07-20 (07-20 bridge)"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**Symptom (2026-07-05, session-start rehydration):** a `Glob` on `wraps/*.md` returned **"No files found"** while the directory actually held **14 wraps** — confirmed by running `ls` at rehydration, which listed them all correctly.

**Root cause:** the directory lives inside a **Google-Drive-synced** folder tree (`MA_PROGRAMMING/WORKING/`). Drive-sync directories can cause glob/list-style tools to false-negative — the mechanism isn't confirmed (sync-placeholder files, FS-event timing, virtual filesystem quirks are all plausible), but the observed behavior is reproducible: the tool reports empty when the directory is not.

**Rule: verify with a second method before trusting a Glob/list "empty" result inside a Drive-synced directory.** `ls` (or an equivalent direct filesystem read) is the confirmed-working second method — it correctly saw all 14 wraps when Glob saw none. Don't conclude "directory is empty" or "files were lost" from a single Glob/list call in these directories; cross-check.

**Cost this session:** the false-negative briefly produced a wrong "wraps missing" note written into session state, caught only at the verification step before it propagated further. The near-miss is the reason this is worth banking as a standing check, not a one-off curiosity.

**Scope:** observed specifically for `WORKING/wraps/`; likely applies to any Drive-synced directory in this project (`WORKING/concepts/`, `WORKING/findings/`, etc.) since the sync mechanism is directory-tree-wide, not specific to one folder. Treat the caution as project-wide until/unless a narrower boundary is confirmed.

**Second symptom, same hazard class (2026-07-08, self-observed during a librarian run):** the **Read tool's file-state cache can briefly lag live disk** in this same Drive-synced folder — a file's `History:` date read as stale via Read, while a live `grep` on the same file showed the current content. Different tool (Read vs Glob) and different failure shape (stale content vs false-empty), but the same underlying hazard class: a tool's view of a Drive-synced directory can disagree with the actual filesystem state. **Rule extended:** cross-check with a live `grep`/`ls` (not just a re-Read) whenever a just-edited file reads oddly, not only when a directory looks suspiciously empty.

**Third symptom, same hazard class, the STAGE lane (2026-07-20) — `device_stage_files` can serve a stale container copy of an already-staged path**, even past the tool's own settle delay: a re-stage of `findings/INBOX.md` was read back at **836 bytes** in the container while the stage call's own result reported **2473 bytes** for the same path. **Rule extended again:** before deriving an edit from a staged copy, compare the actual on-disk byte size at the staged path (`ls -la`) against the stage result's own `bytes` field — if they disagree, the staged copy is stale; re-stage (or rebuild from a known-good read) rather than trusting it.

History: none — first-observed, live, 2026-07-05 (restart-gate-021-ship, session-start rehydration). Broadened 2026-07-08 (librarian run 8, self-observed) to cover a second symptom (Read-tool cache lag) in the same hazard class. Extended 2026-07-20 (07-20 bridge): third symptom added — `device_stage_files` can itself serve a stale container copy of an already-staged path; verify by comparing `ls -la` byte size against the stage result's reported `bytes` field.


## Fourth symptom — a stale STAGED SPINE.md fed to a SUBAGENT, first hit on a subagent rather than cLD — 2026-08-03 [0803-2cLD]

**The exit-gate librarian (a dispatched subagent) grepped its staged copy of `concepts/SPINE.md`, found ZERO of the 5 ids the dispatch brief said were already filed, and read the header as `GENERATED 2026-08-01`** — so it flagged the discrepancy and refused to assume, rather than silently trusting the absence. It was reading a snapshot taken at session start, **before** the same-day regen; the live device copy read `GENERATED 2026-08-03 / 255 concepts` with all 5 ids present.

**Standing rule for dispatch: `device_stage_files` serves a POINT-IN-TIME copy, so any subagent packet assembled early and used late is stale by construction.** RE-STAGE the duplicate-check surface immediately before dispatch, or hand the agent a freshly generated extract — do not reuse a packet staged earlier in the session.

Fourth documented instance of this concept's hazard family (first three: Glob/list false-negative, Read-tool stale-cache, `device_stage_files` stale-container-copy on the STAGE lane) — and the first to bite a **subagent** rather than cLD directly.


## Companion rule from the EU tour leg, 2026-08-08 — hunt with ONE full sweep

Dave's teach the same month: when hunting a file on the device, run **one comprehensive sweep from the top of the allowed roots**, never a string of single-path probes off remembered paths — mounts and repo roots drift between sessions, and a serial probe will happily find a **stale snapshot** of the file you wanted and let you write to it. Full rule, with the ground-truth vs stale-copy receipt: **`device-file-hunt-full-sweep-law`**.

The two rules pair: the full sweep finds the candidates, the live `ls`/`grep` cross-check tells you which one is real.

History: extended 2026-08-28 (librarian, tour leg) — pointer to the device hunt law.
