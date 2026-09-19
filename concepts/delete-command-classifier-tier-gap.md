---
id: delete-command-classifier-tier-gap
title: "Cmd('Delete Preset ...') via send_lua classifies as Tier 1 'read-channel', not caught as a write op — unlike SaveShow-inside-Cmd, which IS caught as Tier 2"
role: programmer
tags: [mcp, classifier, verify]
when_to_load: "Before relying on the Tier classifier to gate a Delete command sent via send_lua/Cmd — the gate does NOT fire, proven at 43-slot mass-delete scale"
status: active
source: "findings/INBOX.md 2026-07-23 [0723cLD] (CLASSIFIER TIER NOTE [VERIFY deliberate-vs-gap])"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**[VERIFY deliberate-vs-gap]:** `Cmd('Delete Preset ...')` sent via `send_lua` classifies as **Tier 1 'read-channel'** — Delete-inside-`Cmd` is NOT caught as a write op, whereas `SaveShow`-inside-`Cmd` IS caught (Tier 2). Delete is Oops-recoverable, so this may fit the existing 07-17 stay-Tier-1 ruling's logic (recoverable ops don't need Tier-2 gating) — but Delete was not specifically named in that ruling, so this could equally be an un-reviewed gap in the classifier's word list rather than a deliberate choice.

**Queued for the classifier word-list review** — do not treat Tier-1 classification of Delete as a green light without that review; verify current classifier behavior before depending on it to block an unwanted Delete.

Relation: see `saveshow-discipline-and-mcp-tier` for the Tier system and the SaveShow-is-Tier-2 precedent this contrasts with.

History: none — captured 2026-07-23 [0723cLD] digest run.


## Update-in-Cmd joins the Tier-1 gap list — 2026-07-31 [0731-3cLD]

**Bare `Update` inside `Cmd()` rides Tier 1** (the gate refused it as needs-no-approval),
while **`Update /NoConfirmation` rides Tier 2** — a trailing-space prefix-match artifact.
`Update`-in-`Cmd` joins `Delete`-in-`Cmd` on this Tier-1 gap list for the classifier
word-list review — queue together, do not review independently.

⚑ [Librarian flag] This may complicate the premise of
`classifier-tier-gap-edit-and-bare-layer-keywords`'s 2026-07-17 ruling, which states "the
verbs that make programmer mutation permanent (Store/Update) are already Tier 2 — the gate
sits at the damage point." That ruling's own evidence appears to be for a different Update
invocation shape than bare-`Update`-inside-`Cmd()`. Not resolved here — flagged for the same
classifier word-list review, and for whoever next re-examines the 07-17 ruling, rather than
edited into that (closed, Dave-ratified) concept by this run.


## Update-in-Cmd status CLOSED 2026-08-01 [0801cLD] — now classifies Tier 2 (gated) on server 0.2.1

**`Update-in-Cmd` (the `Cmd([[Update /NoConfirmation]])` form) now classifies Tier 2 (gated) on MCP server 0.2.1** — live-confirmed: the gate fired and worked correctly during a live Measure fixup on SONG_E. This closes out a previously-noted classifier-gap concern that `Update-in-Cmd` might ride Tier 1 (ungated) for that specific `Cmd(...)` form — as of server 0.2.1 it does not.

**Scope note: this closes the gap for `Update` specifically, not for `Delete`.** The `Delete`-inside-`Cmd` Tier-1 classification this concept's body already documents is untouched by this finding and remains its own open `⚠ VERIFY` item, still queued for the classifier word-list review.

**[0805-2cLD] EXTENSION — the gap is wider than Delete:** a plain Lua property assignment (`r.MAtricks = ObjectList(...)[1]`) also classifies Tier 1 — the assignment carries no write keyword for the classifier to catch. Any keyword-less write rides ungated; treat handle-property writes as writes procedurally.

History: extended 2026-08-05 [0805-2cLD] — plain Lua property assignment (recipe-line MAtricks binds) also classifies Tier 1; classifier catches keywords, not mutation.


## ⛔ SETTLED 2026-08-19 (EU tour leg) — it IS a gap, and it scaled

The `[VERIFY deliberate-vs-gap]` question above is closed on the **gap** side, at cost.

**Receipt:** `Cmd('Delete Preset 4.'..slot..' /nc')`, assembled by **string concatenation**, classified **Tier 1** — the gate literally refused approval as unneeded — and **a 43-slot mass delete of preset objects ran on the read channel**. The announce-always law is what covered it; the classifier did not.

**Root cause is broader than Delete.** The classifier matches **literal keywords in the string it is handed**, so *any* command assembled by concatenation evades it, as does *any* dispatch through a plugin toolbox function (the calling line carries no keywords at all). `Cmd('Go Macro N')` classifies Tier 1 by the same mechanism. Full account, all four attested evasion instances, and the hardening candidates: **`classifier-tier-drift`**.

**Standing behaviour, unchanged and reinforced:** announce every write-effect op regardless of tier, census the target afterwards, and never dodge a gate that does fire.

History: status flipped `verify` → `active` 2026-08-19 — the deliberate-vs-gap question settled as a gap by a 43-slot mass delete that slid through the read channel; see `classifier-tier-drift`.
