---
id: smith-packet-must-stage-multi-part-golden
title: "Smith packets must stage a MULTI-PART golden, not a single-part one — single-part exemplars can't attest SpeedMaster/SpeedScale/parts serialization"
role: programmer
tags: [ma3, smith-lane, xml-schema, goldens, dispatch]
when_to_load: "Before assembling a smith dispatch packet for any sequence-authoring task — which golden exemplar file to stage so the smith can actually certify parts-per-century facts, instead of burning its manifest re-proving something already closed"
status: active
source: "findings/INBOX.md [0731-2cLD] 2026-07-31 (SONG_C smith-certification pass); wraps/2026-07-31-song-b-heard-song-c-built.md 'Open' §4 (Runbook v0.2 owed)"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**Lesson (SONG_C smith certification):** stage **`cld_song-b_seq_v2.xml`** as the MULTI-PART golden in every future sequence-smith packet. **⚑ Qualified 2026-08-05 — see the bottom of this file: this file is NOT a raw desk export**, so it cannot independently attest everything below; it retains authority for part-attribute ORDER only. A single-part golden **cannot attest** `SpeedMaster`-on-Sequence, `SpeedScale`-on-Part, or multi-part serialization at all — it has no second part to prove any of that against. Without a multi-part golden staged, the smith burns its own manifest re-proving a hole the corpus had ALREADY closed elsewhere (in this case, the proof existed in a desk export that simply hadn't been staged into the packet).

**Also stage the song's `gb_sNN00.xml` export** so the sheet-transcription link closes as part of the same certification pass.

**Consequence observed:** all 4 of the smith's WARNs on SONG_C's certification were closed by evidence found OUTSIDE the smith manifest — evidence that a properly staged multi-part golden would have made available INSIDE the manifest from the start.

**Relation:** `parts-per-century-emit-pattern-and-et-gate` (the architecture whose facts a multi-part golden must attest). `part-attr-order-import-absorption-gotcha` (a fact only a multi-part golden's attribute order can verify). `tourshow-seq1210-song-c-build-record` (the certification run this lesson was paid for on).

## ⛔ `cld_song-b_seq_v2.xml` IS NOT A RAW DESK EXPORT — qualifies the golden above, 2026-08-05 [0805cLD]

**Byte-shape proof (sequence smith F1):** `cld_song-b_seq_v2.xml` carries **0 `Guid=`, 0
`Active=`, 0 `DependencyExport`, 0 `PresetData`, and 6-7 attrs per StandardRecipe** — against a
known console export's 11 Guids / 36 attrs and {LD}'s 33-34. It has the AUTHORED dialect's
byte shape, i.e. it is a scrubbed export-back, not a raw export.

**This partly circularises the lesson above**, which names this file the authority for exactly
the facts an emitter-shaped file cannot independently attest (`SpeedMaster`-on-Sequence,
`SpeedScale`-on-Part, multi-part serialization). **It DOES retain authority for part-attribute
ORDER** — it carries the desk form at both sealed-divergence spots, which our own emitter does
not produce.

**A "golden" is only golden if its byte shape matches a real export** — generalised: before
trusting any file labelled desk-export, check for `Guid=` / `Active=` / `DependencyExport`
presence. Their absence means authored or scrubbed, not a genuine console export.

**Owed:** stage one true multi-part RAW console export for the smith lane, or state SONG_B's
actual provenance explicitly in the packet. Not resolved this session.
