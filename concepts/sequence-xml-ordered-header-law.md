---
id: sequence-xml-ordered-header-law
title: "Sequence-XML children 1+2 MUST be OffCue then CueZero, or content cue 1 imports INTO OffCue"
role: programmer
tags: [ma3, xml, import, sequence, v2.4]
when_to_load: "Before hand-authoring or golden-deriving a sequence-XML file for import — check that the first two Cue children are OffCue and CueZero, in that order, before trusting the import"
status: active
source: "findings/INBOX.md [0728cLD] 2026-07-28; wraps/2026-07-28-song-t-full-build-and-resolver-laws.md"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**A `<Sequence>` XML's first two `<Cue>` children must be `OffCue` and `CueZero`, in that order.** Seen live on a dialect test: a file missing them mapped its **first content cue INTO `OffCue`** on import instead of creating it as a normal numbered cue — the import still completed and reported success.

Practical consequence for the golden-derived build method (author a new sequence by cloning another song's cue headers): **verify the imported sequence's `OffCue` and `CueZero` are present and distinct from cue 1** before trusting the rest of the structure — a missing or misordered header pair corrupts silently into a wrong-looking but still "successful" import.

**Relation:** sits alongside `import-resolver-laws` as a second, independent import-time gotcha on the same sequence-XML dialect; see `export-sequence-xml-schema` for the general schema (`<Cue>` header shape, `OffCue`/`CueZero`'s `No="0"`/`No="1"` convention); `tourshow-seq1510-build-record` for the build this was caught on.

History: none — found live, 2026-07-28, during the Seq 1510 SONG_T skeleton import.
