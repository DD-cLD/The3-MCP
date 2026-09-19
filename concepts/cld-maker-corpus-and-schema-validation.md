---
id: cld-maker-corpus-and-schema-validation
title: "cLD MAker session corpus corrected to 11 real sessions (10 Bird's Eye album + SONG_G SHOW); all validate clean against draft-2020-12; palette ma3 field still empty everywhere"
role: tools
tags: [tourshow, cld-maker, beatgrid]
when_to_load: "Before trusting a claim about how many real beatgrid sessions exist, which folders hold full sessions vs. edit-map-only, or the current state of the palette-to-console-pool binding gap"
status: active
source: "findings/INBOX.md, 2026-07-17"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**Fixture-landscape correction:** of the four `*SHOW - lighting/` folders, only **SONG_G SHOW - lighting/** has a full beatgrid session. The Genius / SONG_N / SONG_T SHOW-lighting siblings hold only an edit-map JSON + intake notes — NOT a full session.

**The real backward-compat corpus** is `beatgrid/{ARTIST} {ARTIST}/Bird's Eye/<Song> - lighting/<Song>_beatgrid_session.json` — **10 full album sessions**: SONG_G, SONG_T, SONG_L, Genius, Pilot, SONG_H, SONG_Q, 1 of 1, From Scratch, Candy.

**All 11 real sessions** (10 Bird's Eye + SONG_G SHOW) validated clean, zero errors, against the new **draft-2020-12** JSON schema (`jsonschema 4.26.0`, meta-check + instance-check both pass).

**Concrete v1 gap:** every palette entry in every real session (checked on SONG_G) has an **empty `ma3` field** — hex colors are not yet bound to console pool addresses. This was originally named an explicit closeable v1 target in the spec (S2.4); note that the end-of-session v1/v1.1 scope lock later moved "palette-ma3 lock" to **v1.1** instead (see `cld-maker-identity-rename-and-scope`) — the gap itself hasn't changed, only which release closes it.

**Relation:** `beatgrid-session-json-schema-conventions` for the JSON field conventions this corpus validates against. `cld-maker-identity-rename-and-scope` for the spec pack and scope lock this corpus check fed into.

History: none — corpus corrected and fully revalidated same session, 2026-07-17.
