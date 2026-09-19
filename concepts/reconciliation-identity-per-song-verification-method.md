---
id: reconciliation-identity-per-song-verification-method
title: "Reconciliation identity: a per-song crosswalk QC shape stronger than a count census — every per-cue line-count difference must land on a NAMED cause"
role: operational-live
tags: [qc, verification, crosswalk, crosscheck, tourshow]
when_to_load: "Before trusting a crosswalked song's total line count as 'close enough,' or before building/reading a per-song QC/RECONCILE sheet — a count match alone is a weaker proof than accounting for every per-cue difference by name"
status: active
source: "BACKLOG.md 2026-08-03 [0803-1cLD]"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**The reconciliation identity, exact and residual-free on SONG_J's 37 content cues:**

```
{LD} 245 − 1 HELD − 1 Position-on-QX40 law drop + 12 QX40-STB expansion + 2 JDC gate-openers = 257 cLD
```

**Every per-cue difference lands on one of those named causes.** This is a stronger check than a count census: it proves not just that the TOTALS agree, but that each INDIVIDUAL difference is explained. Reusable per song — a `RECONCILE` sheet tab is the shape to build for any crosswalked song.

**⚠ Forward-looking note:** the `+2 JDC gate-openers` term is scheduled to disappear from this identity on future songs — `master-default-doctrine` now retires the `JDC_OPENERS` emitter behavior (masters are never programmed; see that concept). Expect the identity's cause-list to shrink by one term on any song built after that change lands.

## Predecessor method (08-01): constraint-propagation bind census

Before the reconciliation identity was named, the same verification goal was reached a different way: a **constraint-propagation bind census** (global group -> selection function, plus per-cue multiset equality) proved 27/32 SONG_I cues **bind-for-bind** file-side, zero conflicts. Also **stronger than a count census**, and **reusable pre-import** on any crosswalk emit — a companion technique to the reconciliation identity, useful when a full named-cause accounting isn't yet built.

## Sheet-freshness rule: the cLD side of a QC sheet must be a FRESH desk pull, not the as-built export-back

**Paid-for lesson:** the 08-01 export-back for SONG_J went stale the moment Dave started cleaning at the desk. `Export Sequence 2010` taken live on 08-03 read **225 SRs against the shipped 257** — 34 line-instances removed, 2 changed by hand. **A sheet built off the as-built file describes a console that no longer exists.** Standing rule: pull the sequence fresh at sheet-build time, and keep the as-built export as its own separate tab so the chain **{LD} -> as-built -> now** stays readable and each stage stays honest about its own age.

## Process rule: corrections found during a reconciliation pass are DEFERRED, not fixed in place

**RULED (Dave):** corrections surfaced by a reconciliation/QC pass are **deferred to an end-of-build circle-back**, not fixed during the run. Breadcrumbs + method get logged as they are found. Landed as `TOURSHOW_CORRECTIONS_LEDGER_v0.1.md` (WORKING root) — as of this backlog, 11 entries, each with exact sites and the method, so the circle-back is **execution, not rediscovery**. Anything found during a build run gets **APPENDED** to that ledger rather than fixed in place — the whole point of the rule is that a run session makes no correction decisions of its own.

## Reconciliation vocabulary pinned — `Enabled`, not `Active`, 2026-08-05 [0805cLD]

**{LD}'s recipe lines carry TWO enable-ish attributes — pin which one a "live SR" count
means.** `Enabled` reads Yes on all 109 of SONG_L's lines; `Active` reads Yes on only 21,
No on 88. **"109 live SRs" = the `Enabled=Yes` / direct-child count, NOT `Active=Yes`.** The
one HELD line (Follow Spots, cue 1) is itself `Active="No"` — the same state as 87 lines that
WERE carried into the build — so `Active` is not a hold criterion at all. **Pin the vocabulary
to `Enabled=Yes` / direct-child count**, so a future reconciliation pass doesn't re-derive this
from scratch. See `tourshow-seq2210-song-l-build-record` for the identity this vocabulary
was pinned on (`{LD} 109 − 1 HELD = 108 cLD`).

**Relation:** `tourshow-recipe-line-redundancy-taxonomy` (the duplicate/redundancy classes a reconciliation pass will surface). `tourshow-cue-century-review-sheet-doctrine` (the sibling per-song review artifact — that one is for TASTE verification, this one is for crosswalk-completeness verification; they are different sheets serving different checks). `tourshow-seq2010-song-j-build-record` (the song this identity and its evidence were first proven on).
