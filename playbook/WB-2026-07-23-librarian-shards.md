# WORKER BRIEF — Librarian shard digest (backlog), 2026-07-23

**You are a clean-room WORKER session, not the lead.** cLD-lead is orchestrating from another session. Your entire output lands in a staging folder; you change nothing else. Cheap/Sonnet-class session is fine for this work.

## Absolute law (violations poison the run)

- NO console contact: never call any grandma3/gma3 MCP tool, no OSC, nothing that touches the desk.
- NO writes to: `MEMORY.md`, `concepts/` (the live folder), any `INDEX*.md`, `findings/INBOX.md`, `wraps/`, `CURRENT_STATE*`, `NEXT_ACTIONS*`, `README.md`, show docs. Read them freely; write NONE of them.
- ALL output goes under `WORKING/generated/staging_librarian/` only.
- Never invent MA3 facts. Verbatim values are the payload. Provenance on everything. `[VERIFY]` stays `[VERIFY]`.
- No wrap protocol, no rehydration, no INBOX clearing — those are lead-only acts.

## Mission

Digest the **pre-[0723-2cLD] backlog** of `WORKING/findings/INBOX.md` into DRAFT concept files under the v0.2 filing law, staged for the lead's merge.

## Read first, in order

1. `WORKING/LIBRARIAN.md` (v0.2) — schema, role partition table, gardener rules, trigger-worded-line law. Follow it exactly.
2. `WORKING/concepts/INDEX.md` — for duplicate/supersede detection (read bodies only where a finding might collide).
3. The corpus for this run: `WORKING/findings/INBOX.md` — ONLY the blocks tagged 07-20 bridge, 07-21 song-g-infra, [0721-2cLD], [0721-3cLD], [0722-2cLD], [0723cLD]. The [0723-2cLD] block is EXCLUDED (the lead handles it). Plus `WORKING/findings/{FESTIVAL}/FESTIVAL_FINDINGS_v0.1.md`. Source wraps in `wraps/processed/` 07-20 → 07-23 as provenance where a line references one.

## Do

1. Draft atomic concept files per the v0.2 schema — full frontmatter including `role:` — into `staging_librarian/concepts_draft/`.
2. For updates to EXISTING concepts, do not edit the live file: write `staging_librarian/updates_draft/<id>.md` containing the full proposed new body.
3. Write `staging_librarian/STAGING_REPORT.md`: counts (new / update / merge-proposal / supersede-proposal per role) · every dupe/supersede PROPOSAL with one-line rationale (proposals only — the lead executes) · every ⚑ line you couldn't confidently digest · every `→packet` show-operative flag · a proposed trigger-worded index line for every file, grouped by target index (INDEX.md / INDEX_DESIGN.md / INDEX_TOOLS.md per the partition table).

## Done

STAGING_REPORT.md complete and self-consistent → stop. Your final chat message: the report's summary counts and flags, nothing else.
