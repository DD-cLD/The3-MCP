---
id: copy-at-occupied-slot-dialog-trap
title: "Copy At an occupied preset slot pops an overwrite dialog — unattended CLI reads it as 'User Canceled Command' and can leave a default-named husk behind"
role: programmer
tags: [ma3, cli, v2.4, dialog, preset, mcp]
when_to_load: "Before running Copy At <pool>.<slot> over MCP/unattended CLI — check the target slot is empty first, or the copy silently fails as a user-cancel and may leave a husk object in its place"
status: active
source: "findings/INBOX.md [0728cLD] 2026-07-28, live 2.4.2.2, caught mid phaser-template-set batch build; wraps/2026-07-28-song-t-full-build-and-resolver-laws.md"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**`Copy At` an EMPTY preset slot completes silently (`ok`).** **`Copy At` an OCCUPIED slot pops an Overwrite dialog** — and because the CLI channel is unattended, nothing answers the dialog, so the command returns **`"User Canceled Command"`**, exactly as if a human had actively hit Cancel.

**A husk can be left behind:** if a prior batched Copy was interrupted partway into the dialog (console healthy, PID stable, no crash), the target slot can be left holding a **default-named placeholder object** (observed: a bare `"Preset 1521"`) rather than either the old content or the new copy. A subsequent Copy At that same slot then hits the occupied-slot dialog again, because the husk itself counts as "occupied."

**Fix:** `Delete <pool>.<slot> /NoConfirmation` the husk first, **then** issue the plain `Copy At`. (Alternative: use an `/Overwrite` flag on the Copy command itself, if available for this verb, to skip the dialog entirely.)

**Same family as `assign-layout-merge-dialog-behavior`** — both are cases of a CLI verb behaving silently when the destination is empty and popping a blocking Overwrite/Merge dialog the instant it collides with existing content. Treat "does the target already exist?" as a precondition to check before any unattended batched Copy/Assign/Store-style command, not just for layouts.

**Operational takeaway for batch builds:** after any interrupted or partially-failed batched command sequence, don't assume "no crash, PID stable" means no damage — check every target slot's actual content (name + Guid) before continuing the batch, since a husk reads as legitimate content until inspected.

## Safe lane confirmed 2026-08-01 [0801cLD] — Copy .../Overwrite preserves the bound OBJECT reference through a content swap

**`Copy Preset .../Overwrite` preserves the bound OBJECT** when swapping a preset's content — proven readback: Seq 1410's recipe-line references to `21.1422` survived a baked-content overwrite fully intact. **This is the safe lane for swapping a bound preset's content**: no delete, no re-Assign needed anywhere downstream — every recipe line that already pointed at the preset keeps pointing at it correctly after the overwrite. Distinct from the occupied-slot dialog trap this concept's body documents (which is about an UNATTENDED CLI Copy hitting a blocking dialog) — this is about what happens on a normal, attended Overwrite once the dialog is answered.

## Copy grammar confirmed via MCP `Cmd()`, 2026-08-05 [0805cLD]

**`Copy Preset <src> At <dst>` and `Copy MAtricks <src> At <dst>` both land clean into an
EMPTY slot (7/7 this session)**, confirmed specifically through the MCP `Cmd()` transport (not
just attended CLI). **Occupied-slot behaviour is unchanged** — see the dialog trap documented
above. Note separately: a `Copy` also carries the source object's NAME and can trigger the
silent `#2` auto-suffix even into an empty slot if that name collides — see
`cld-sandbox-and-namespace`'s COPY-verb extension of the `#2` rule; that is a distinct hazard
from the dialog trap this concept documents.

History: none — found live, 2026-07-28, mid-build of the SONG_T phaser template set (`21.1520-1523`); resolved same session. Extended 2026-08-05 [0805cLD]: Copy grammar (Preset + MAtricks, empty-slot case) reconfirmed specifically via the MCP `Cmd()` transport. Relocated to end-of-file 2026-08-05 — `generated/build_spine.sh` truncates a concept's SPINE.md view at the first `History:` line, so the "Safe lane confirmed 2026-08-01" section above had been silently absent from SPINE.md since it was written; this relocation recovers it (gardener rule 4 — nothing deleted, only moved).


## EU tour leg refinement, 2026-08-19 — with `/o /nc` it WORKS, and it carries the SOURCE's NAME

**`Copy Preset <src> At <dst> /o /nc` into an OCCUPIED slot completes cleanly** — the `/o` (overwrite) plus `/nc` pair answers the dialog this concept warns about, and it was the workhorse of the colour crowning (12 bases crowned from live variants in one pass).

**⚠ But the copy brings the SOURCE's Name with it.** The destination silently takes on the source's label, so **every crown/mint must be followed by a re-Label and a readback**. Attested in two pools the same fortnight: crowned colour bases (names restored explicitly afterwards) and minted MAtricks twins (`matricks-property-clear-encoding`). A stale label is what a later by-name lookup will match — and a by-name lookup inside a macro is exactly what a label race breaks (`macro-lua-label-race-needs-wait`).

**Sequence to use: Copy → Label → read the label back → only then let anything reference it.**

History: extended 2026-08-28 (librarian, tour leg) — the `/o /nc` working form and the Copy-carries-the-source-name rule.
