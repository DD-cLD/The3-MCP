---
id: cold-boot
tags: [ma3, playbook, boot, agent, retrieval]
verified: grandMA3 onPC 2.4.2.2 (Mac)
---
# COLD BOOT — operating this corpus with no lighting knowledge

**Who this is for:** an agent, or a person, holding this repo with little or no
grandMA3 experience — possibly with a console attached, possibly not.

This procedure was written by an agent that had never touched a lighting console,
during the session that packaged this repo. It is the boot I actually needed, not
the one an expert would design for me.

> A story in this corpus is a stored value: the miss that drew the rule's edge,
> the receipt that earned its trust, the why that covers the case nobody wrote
> down — 🔴 READ IT LIKE PATCH, NOT LINER NOTES.

---

For a new agent or host, start with [the portable guide](../docs/AGENT_QUICKSTART.md).
It defines corpus-only use, host setup, and how to adapt missing historical files.

## 0 · The premise

**You are not expected to know MA3. You ARE expected to look it up before acting.**

Querying is not diligence theatre. It is the operating procedure, because your
priors about lighting consoles are the single most dangerous input in the room:
they are fluent, they are confident, and on this desk they are often wrong. Every
concept in `concepts/` exists because someone acted on a reasonable assumption and
the console disagreed.

⚠ **Precondition — check this before trusting any query.** `concept_lookup` reads
`concepts/INDEX.md` and parses lines of the form ``- `concept-id` — summary``. If
the index is missing, the tool returns `None`; if the format drifts, it returns
`[]` — **and an empty result is indistinguishable from "no such knowledge."**
Run the §7 self-check at boot. An unverified index is a corpus that lies by
omission.

## 1 · Truth precedence — memorise this order

| rank | source | reach it with | authority |
|---|---|---|---|
| 1 | **The live console** | operator-authorized `send_lua` (all raw Lua is gated) · `resolve_object_address` · `get_showfile_snapshot` | Beats everything, including this file. A readback is evidence; a document is a claim. |
| 2 | **`concepts/`** | `concept_lookup(keyword)` | Why a rule exists, what its edge is, what broke. Paid for in failures. |
| 3 | **The MA3 manual** | `manual_lookup(keyword)` | Official vocabulary and intended behaviour. Note: intended ≠ observed. Where they differ, §2 wins and a concept usually records the gap. |
| 4 | **Your own reasoning** | — | Last. And when you rely on it, **say so out loud** and mark the claim unverified. |

**Never invert this.** The most common agent failure here is reasoning
confidently about a console it has not read.

## 2 · The boot sequence — every session, in order

### Step 0 · Choose the mode
For corpus-only or file-side work, skip the wire check and search `concepts/INDEX.md`
directly (or use already-configured `concept_lookup`). No console is required.
For operator-requested console work only, call `get_console_info()`. The liveness
field is nested at `probe.lua_roundtrip_ok`. Generic `send_lua`, including apparent
reads, is now Tier 3 and requires the supervised gates described in the guide.

🔴 **`udp_sent` is NOT liveness.** UDP is connectionless — a fully closed onPC
still returns `udp_sent: true`. The liveness bit is **`lua_roundtrip_ok`**, which
means the console actually executed your code. If it is false, you have no
console; say so and do not proceed as if you do.

Record the returned `server_version` and console identity. A changed PID later in
the session means the console crashed and relaunched — see §6.

### Step 1 · Establish what you do not know
Name the task's territory in plain words — "timecode", "phasers", "patch",
"import" — and **query before reading anything else**:

```
concept_lookup("<territory>")
```

An exact id match returns the **full body**. Read it. If several match, read the
summaries and pull the closest body. Two minutes here routinely saves an hour and
a console crash.

### Step 2 · Load the gates
Read `playbook/console-hard-rules.md` end to end. It is short, it is fourteen
rules, and every one was written after something broke on a live desk. Rule 1
alone (`GetPresetDataFast` segfaults, and `pcall` cannot catch it) is the
difference between a session and a crash report.

### Step 3 · Orient on the actual task
If the task touches a session ritual or a firing gate, the installable skills in
`skills/` carry the procedure — `ma3-run-session` for session shape,
`ma3-desk-session` for anything that writes to a desk.

### Step 4 · Declare a contract before you act
One line back to the human: **goal · scope · what you will touch · what you will
not.** This is the last cheap moment to be corrected.

## 3 · Query triggers — look it up when you see these

| you are about to… | query first |
|---|---|
| import handwritten XML | `import-resolver-laws` — name-paths resolve by **three** different rules, and a numeric preset name parses as a **slot index** |
| write a macro | `macro-line-syntax-and-batching-rule` — one command per line; the interactive CLI batches on `;`, macros do **not** |
| touch patch | `patch-set-one-prop-quoted-values` — one property per `Set`, quote every value; chained props drop silently and bare negatives flip sign |
| save, or do anything large | `saveshow-discipline-and-mcp-tier` |
| read preset data fast | don't — `gpdf-console-killer` |
| move or delete a timecode target | `tc-track-target-cutover` — deleting a TC-targeted sequence **eats the track's events**; moves preserve them |
| build multi-part cue parts | `part-attr-order-import-absorption-gotcha` — out-of-order attrs make the importer silently absorb content into part 0 |
| anything not on this list | `concept_lookup` on the nearest noun anyway. The list is not the corpus. |

## 4 · Write gates — the part that matters most

The server classifies every command into tiers. **Tier 0/1 read. Tier 2+ writes.**
Default mode is `dry_run`, which refuses to send Tier 2+ at all.

🔴 **No `Go+`, no store, no import, no write chain without an explicit
"desk clear?" callout and a human's clear-to-fire.** The console is ONE shared
command surface: your write lands in whatever context the desk currently has
open, which may be a live show. This is not a formality. See
`desk-clear-callout-before-console-write-rule`.

`send_lua` transport rules — the CLI is unforgiving and violations corrupt
commands rather than failing cleanly:

- single line · single quotes only (no `"`) · no `;` · no backslashes
- `want_result=True` needs a single **expression**; statements need
  `want_result=False`, which returns `udp_sent` only — **no execution proof**

## 5 · Verification laws — this corpus's, not mine

These are transferable. They are why the repo is trustworthy, and they apply to
your own work inside it.

| law | meaning |
|---|---|
| **Never trust a clean echo** | A command that returned without error proves the transport worked, not that the thing happened. Read it back. |
| **An empty census indicts the selector first** | Zero results usually means your query is wrong, not that the world is empty. Prove the selector on something you know exists. |
| **State the scope with every count** | "12 found" is not a fact. "12 of 47 files in `concepts/`" is. |
| **A clean import proves nothing below the structure layer** | Run an object-level binding census — `:Get()` readback per line. |
| **Goldens are never edited** | When output disagrees with a golden, the output is suspect. Change the golden only with a recorded reason. |
| **Self-test the instrument on planted fixtures** | Before trusting a tool, feed it a case where you know the answer. |

## 6 · Known tool traps

| trap | what actually happens |
|---|---|
| `udp_sent: true` | Proves a packet left. Proves nothing about the console. Use `lua_roundtrip_ok`. |
| An MCP timeout | May be a **console crash**, not a slow reply. Confirm with `get_console_info`; a changed PID = crash + relaunch. |
| `concept_lookup` returns `[]` | Could be "no such concept" **or** a broken/missing index. Run §7 before believing it. |
| `manual_lookup` returns nothing | The local manual index may simply not be built in this checkout. That is a config state, not an answer. |
| Enumerated OSC addresses | Shift between MA3 versions. **Never hardcode.** Resolve at runtime with `resolve_object_address`. |
| `get_showfile_snapshot` | Reads the **last** snapshot the plugin wrote. It does not take a new one. Check its timestamp before trusting it as current. |

## 7 · Index self-check — run this at boot

Before relying on a single query, prove the retrieval surface works:

1. `concept_lookup("gpdf")` — a concept known to exist in this repo. You should
   get a hit, and an exact-id query should return a **body**.
2. If that returns nothing, the index is broken or unbuilt. **Say so and stop
   relying on the corpus** — do not silently fall back to your own priors.
3. Sanity-check breadth: query two or three ordinary words for the task domain
   ("strobe", "timecode", "import"). All-zero across common terms is an index
   symptom, not a knowledge gap.

## 8 · When the corpus is silent

Silence is a result, not permission.

1. **Re-query with different words.** The index matches on substrings of id,
   summary and domain — try the console's vocabulary, not yours.
2. **Try `manual_lookup`** for official behaviour.
3. **Read the console** if one is attached — a Tier-1 readback answers more
   questions than any document.
4. **Escalate to the human.** Say plainly: what you were trying to do, what you
   queried, what came back empty, and what you would do next if told to proceed.
5. **Do not improvise into a write.** Reading on a guess costs nothing. Writing
   on a guess is how the rules in `console-hard-rules.md` got written.

## 9 · Status of this file's own pointers

Held to the same standard it asks of you. As of **2026-09-19 (v0.1 release)**: all
8 concept ids cited above resolve in `concepts/`, and the two `ma3-*` references
are installable skills in `skills/`. **`concepts/INDEX.md` is a GENERATED artifact**
— built by `tools/build_public_index.py`, which asserts that its own output parses
back through the server's `concepts.index_entries()` (361/361 at release). Never
hand-edit the index; regenerate it.

## 10 · Placeholders you will meet

Names in this corpus are deliberate placeholders: `{LD}`, `{TOUR}`, `{FESTIVAL}`,
`{USER}`, and songs as `SONG_A`…`SONG_T`. The show, the artist and the people are
not the point; the mechanisms are. Numbers — sequence `2310`, pool `21.2420` —
are **real and abstract at once**: they demonstrate the arithmetic of a numbering
scheme, and they are not addresses on your desk. Never copy a literal number from
this corpus onto a console. Derive your own, and read it back.
