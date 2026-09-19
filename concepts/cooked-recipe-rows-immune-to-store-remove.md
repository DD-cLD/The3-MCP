---
id: cooked-recipe-rows-immune-to-store-remove
title: "⛔ Recipe-COOKED rows in a cue cannot be killed by Store /Remove or At Remove — recipe data dies by SELECTION/MATRICKS REPOINT, raw data dies by At Remove + /Merge. Repointing also MIGRATES the look intact."
role: programmer
tags: [ma3, recipes, cues, v2.4, gotcha, tourshow]
when_to_load: "Before trying to remove values from a cue — first establish whether the rows are RAW stores or recipe COOKED output, because the two die by completely different mechanisms and the wrong one is a silent no-op"
status: active
verified: grandMA3 onPC 2.4.2.2 (Mac), EU tour leg 2026-08
source: "findings/INBOX.md [0826-3cLD] 2026-08-26, {FESTIVAL} — scratch tests plus live counts on the masters surgery; confirmed again on the prep file [0826-4cLD] with an identical fingerprint"
supersedes: []
superseded_by: null
---

## The revelation

Rows that look like ordinary stored values in a cue may be **cooked output of a StandardRecipe** on a part. In an export they carry the `Cooked=` attribute. **Four removal lanes were tried against cooked rows and all four were silent no-ops:**

- `Store /Remove`
- `At Remove` (default store)
- `At Remove` with `/Merge`
- the `/Remove` option form

**Nothing addressed at the value layer can touch them, because the value layer is not where they live** — they are re-derived from the recipe line every time the cue cooks (`recipe-output-precedence-and-cooking-doctrine`).

## The two kill lanes

| Row kind | Dies by |
|---|---|
| **Recipe-cooked** | **repointing the recipe line's `Selection` or `MAtricks`** |
| **Raw store** | `At Remove` + `/Merge` default-store (scratch-proven), or `Store /Remove` (`store-remove-attribute-scoped`) |

## Migrate-by-repoint: the kill that preserves the look

The tour's masters surgery is the worked example. QX40 "master rows" were **not raw stores** — 147 recipe lines rode a `cLD QX40 MM ALL` selection across 22 sequences, mixing Dimmer values with strobe, tilt and colour. Masters legitimately own strobe/tilt/colour, so **only the Dimmer-pool lines were migrated**: every recipe line whose `Values` parent pool was Dimmer had its **`Selection` repointed from the master group to the cell group** — **65 lines** (`0` ×36, `50` ×14, `Full` ×13, `30` ×2).

**Same presets, same parts, same timing ⇒ the look is preserved exactly**, and the masters leave the dimmer lane. Verse-compliant migrate-then-die in one move (`master-default-doctrine`).

**Proof:** fresh export rescan — master-kind rows **294 → 240**, QX40 dotless **69 → 15**; the 15 survivors are all figure-cooked `abs:100` (phaser-pool values, deliberate swell dynamics), a separate aesthetic question for Dave. The identical 65-line fingerprint reproduced on a second file, which is what let the whole treatment become a one-tap macro (`venue-adapt-macro-pattern`).

**Benign residue to expect:** raw cell rows written by an earlier batch can survive an `At Remove` sweep by landing in a different part via auto-routing (`merge-store-part-auto-routing`). If they hold the same presets the recipes now cook, there is no visual conflict — pure duplication, a calm-day cleanup.

**Relation:** `store-remove-attribute-scoped` · `merge-store-part-auto-routing` · `recipe-output-precedence-and-cooking-doctrine` · `master-default-doctrine` · `assign-cli-recipe-line-grammar`.

History: none — established by scratch test plus live counts, 2026-08-26; reproduced 2026-08-26 on the prep file.
