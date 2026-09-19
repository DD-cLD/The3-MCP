---
id: cue-names-not-round-trip-stable-content-derived-labels
title: "Bracket cue names ('[Full/...]') are CONTENT-DERIVED auto-labels, not fixed strings — the console re-resolves and can rename them on import; census cue names off the export-back, never off what was sent"
role: programmer
tags: [xml-schema, cue-naming, import-lane, dialect]
when_to_load: "Before trusting a cue's bracket-style name as evidence of its content, or before census-ing cue names for a QC/reconciliation sheet — read names off the export-back, never off the authored/sent file"
status: active
source: "BACKLOG.md 2026-08-01 [0801cLD], 2026-08-03 [0803-1cLD]; extended findings/INBOX.md [0803-3cLD] 2026-08-04 (weighted notation: 'not a census axis' framing; note symbol/G-value mismatch in source)"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**Bracket-style cue names (`'[Full/...]'`) on {LD}'s aux sequences are CONTENT-DERIVED auto-labels, not authored fixed strings** — an authored `'[Full/Color Linear]'` re-labeled itself `'[Full/FX White]'` after import, because the phaser's stock endpoint reads through into the display name. This explains the aux naming convention file-wide; **it is not import damage.**

**The same instability hits cLD-authored cue names on import.** Desk-renamed example: authored `'[50/Neutral White]'`, export-back reads `'[Full/cLD FR NEUTRAL WHITE]'`. **Cue NAMES are not round-trip stable whenever the name references a preset the console re-resolves.**

**Practical consequence: census cue names off the export-back, never off what was authored or sent.** Any QC/reconciliation sheet, join-key logic, or census script that assumes a sent cue name will still be the name after import is checking a value the console may have already silently rewritten.

**Relation:** `inherited-file-membership-is-ground-truth` (the sibling doctrine for GROUP/preset names lying about membership — this concept is the CUE-name-specific instance of "don't trust a label," but the mechanism here is console re-resolution on import, not inherited-file staleness). `reconciliation-identity-per-song-verification-method` (a QC sheet built on this corpus needs export-back-sourced names to stay accurate).

## Not a census axis, reinforced 2026-08-04 [0803-3cLD]

**STRUCTURAL (G=0.5 — source line carries the ○ Low symbol against a G=0.5 Structural value;
the pairing is internally inconsistent with the notation's own table, flagged not resolved;
the fact itself is unambiguous).** Recipe-cue names are console-derived from bound content;
the authored `Name=` is discarded on import. Restated for emphasis: **cue name is not a census
axis** — don't count, join, or key anything on a cue's name, authored or read back; use the
cue's structural position (No=, part index) instead.
