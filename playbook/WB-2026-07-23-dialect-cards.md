# WORKER BRIEF — Dialect card distillation, 2026-07-23

**You are a clean-room WORKER session, not the lead.** cLD-lead is orchestrating from another session. Your entire output lands in a staging folder; you change nothing else.

## Absolute law (violations poison the run)

- NO console contact: never call any grandma3/gma3 MCP tool, no OSC, nothing that touches the desk.
- NO writes to: `MEMORY.md`, `concepts/`, any `INDEX*.md`, `findings/INBOX.md`, `wraps/`, `CURRENT_STATE*`, `NEXT_ACTIONS*`, `README.md`, show docs. Read freely; write none of them.
- ALL output goes under `WORKING/generated/staging_cards/` only.
- Never invent MA3 facts. Every card line must trace to a source. No wrap protocol.

## Mission

Distill the three one-page **dialect CARDS** — the least-possible-information kits for the minimal-kit bake-off (Dave's ruling, 2026-07-23: find the smallest amount of information that makes the programming work; excess process noise at authoring time may do more harm than good).

## Read first

1. `WORKING/AGENT_LANES_SPEC_v0.1.md` — context for what the cards are.
2. The three smith briefs in `WORKING/agents/` — each lists its arming manifest.
3. Every concept body each manifest names (under `WORKING/concepts/`).
4. `WORKING/MEMORY.md` — the ⛔ hard rules.
5. Golden fixtures: `generated/cLD_GROUP_BUILDER.xml`, `generated/factory_macro_fixture_circular_copy_x_plus.xml`, `beatgrid/Meta/cld_maker_handoff/fixtures/cld_seq102_inspect.xml`, `Tc1_Inspect.xml` (same folder).

## The distillation rule

A card holds ONLY what a strong model could NOT derive on its own: empirical console behaviors, exact syntax/dialect facts, silent-failure traps, the literal math, the output contract, one golden-fixture pointer. Cut ALL narrative, history, rationale, and process. If a line is derivable from general XML/lighting knowledge, cut it. Target ≤60 lines per card.

Every retained line carries its source concept id in a trailing comment (traceability). Anything `[VERIFY]`-tagged that survives keeps the tag.

## Output

- `staging_cards/CARD_MACRO_v0.1.md`
- `staging_cards/CARD_SEQUENCE_TC_v0.1.md`
- `staging_cards/CARD_PHASER_v0.1.md`
- `staging_cards/CARDS_REPORT.md` — for each card: line count, what was cut and WHY it's safe (derivable vs empirical tagging), and anything that resisted compression (candidate for the card's "open" footer).

## Done

Four files complete → stop. Final chat message: the three line counts + anything that resisted compression, nothing else.
