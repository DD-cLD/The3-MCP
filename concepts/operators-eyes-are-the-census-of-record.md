---
id: operators-eyes-are-the-census-of-record
title: "OPERATOR'S-EYES LAW: for desk state, Dave's eyes are the census of record — instruments confirm afterwards. Three eyes-beat-instruments events in one tour, each catching a class of truth no scan could reach."
role: operational-live
tags: [process, doctrine, verification, tourshow]
when_to_load: "When a scan reports clean and the operator says something is wrong — believe the operator and go find which class of truth the instrument was blind to; also before claiming a state is verified on instrument evidence alone"
status: active
verified: EU tour leg 2026-08
source: "findings/INBOX.md [0819-3cLD], [0819-4cLD], [0819-5cLD] 2026-08-19 — three distinct events in one day"
supersedes: []
superseded_by: null
---

## The law

**For desk state, the operator's eyes are the census of record.** Instruments — exports, greps, reference scans, command echoes — are how a finding gets *confirmed and quantified*, not how it gets *found*.

## The three events, each a different blind spot

1. **Echoes lied.** Thirteen clean `OK` responses against a `.show` file nine hours stale. Dave saw "not saved up." The instrument reporting success was the thing that was wrong (`saveshow-enumerate-headless-cancel-class`) — and the ritual that came out of it is *disk-verify every save* (`save-disk-verify-mtime-delta`).
2. **The plan was mechanically right and semantically wrong.** A consolidation sweep executed perfectly — counts exact, zero dangling refs — and snapped the show to stale base looks, because the *content* of the survivors was not what the tour wore. No count could have caught it (`color-consolidation-crowning`).
3. **The scan was pattern-blind.** A grep for colour references inside phasers matched only `Preset 4.x` text; a GUID cross-reference later showed phasers never bound the colour pool by reference at all. What Dave actually saw was the phasers' **baked step content** owing the consolidation — invisible to *any* reference scan (`reference-scan-blind-spots-guid-and-baked-content`).

**By the third event the instruments concurred on every axis** — after being pointed at the right question by an eye.

## How to hold both

- **Never argue a clean scan against an operator report.** Ask which layer the scan could not see: echo vs disk, reference vs content, count vs semantics.
- **Then build the instrument that would have caught it** and re-run it. Each of the three events produced a permanent lane: the disk-verify ritual, the crowning order, the GUID + content-semantics scan rule.
- **Honesty is part of the law.** The pattern-blind grep was corrected in the log the same session, in public, with the method lesson attached. A finding that quietly becomes right is worth less than one that shows its correction.
- **State the scope with the count** (`state-the-scope-with-the-count`) — an unqualified number invites exactly this class of over-trust.

**Relation:** `saveshow-enumerate-headless-cancel-class` · `color-consolidation-crowning` · `reference-scan-blind-spots-guid-and-baked-content` · `probe-called-unreliable-is-not-evidence` · `state-the-scope-with-the-count` · `deferred-conclusion-is-not-a-held-conclusion`.

History: none — named after three events inside one day, 2026-08-19.
