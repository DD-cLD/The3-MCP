---
id: beatgrid-tc-carried-cuts-and-seam-gap
title: "Short-form tour bounces carry their edit IN the TC itself (Christopher's claim, verified frame-exact) — and beatgrid's 20s-only LTC decode breaks SMPTE across the seam"
role: tools
tags: [tourshow, beatgrid, audio-dsp]
when_to_load: "Before trusting a beatgrid SMPTE/TC readout on a short-form or variant tour bounce (anything numbered 21/22/23-style), or before reaching for audio-alignment on a cutdown when the TC itself might already encode the cut"
status: active
source: "findings/INBOX.md 2026-07-07 + wrap 2026-07-07-beatgrid041-daysshow-tourintake [0707cLD]"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

- **Christopher's claim, verified frame-exact (2026-07-07):** short-form/cutdown bounces carry their edit encoded directly in the LTC track. On `21_SONG-G SHORT`: same LTC base as `09_SONG-G`, with a **TC jump at file time ~39.7s that skips forward +66.8s** — and the post-seam TC **lands exactly on `09_SONG-G`'s own end timecode**.
- **Consequence: cues addressed to the original (long-form) TC stay valid across the seam** — because the short-form file's LTC track literally re-encodes the same timeline, minus the cut section. **The LTC itself IS the edit map** for the 21/22/23-style variant bounces — frame-exact, with none of the chorus-aliasing risk that audio-correlation alignment carries (see `chorus-aliasing-lesson`).
- **Gap this exposes in beatgrid.html:** `decodeLTCjs` only reads the **first 20 seconds** of a file to establish TC. On a seamed variant bounce, everything read after the seam is offset — **SMPTE readouts are WRONG past the jump.**
- **P1 fix queue:** **full-file LTC scan → TC-segment map → per-segment SMPTE + automatic seam markers.** This would kill the need for audio-based alignment on variant bounces entirely — the TC would just tell you where the cut is.
- **Confirming counterpart (2026-07-07/08, 2 data points): primary-slot bounces do NOT carry cuts.** `09_SONG-G` and `16_SONG-N` both bounce their show EDIT flat, with continuous, unbroken TC — no seam anywhere in the file. Only the `21`/`22`/`23`-style SHORT/variant bounces carry cuts encoded in the TC (the mechanism above). **Working rule: don't expect a TC edit map from a primary-slot bounce** — its TC is just the slot clock; the edit only shows up in variant files. See `tourshow-slot-ledger` for the per-file results.

History: none — Christopher's claim landed and was verified, and the beatgrid gap it exposes was diagnosed, same session, 2026-07-07. 2026-07-08: confirming counterpart added — primary-slot bounces (SONG_G 09, SONG_N 16) bounce their edit flat with continuous TC; the cut-in-TC mechanism above is specifically a variant-bounce behavior, now 2-for-2 confirmed on the primary side too.


## Frame-level confirmation on the EU tour leg, 2026-08-08 — and the design consequence

A frame-by-frame biphase decode of the corpus WAVs (`ltc_confirm.py`, run on the codex runtime — the system python has no numpy) **confirmed the mechanism exactly**, on two songs:

- **Full versions:** continuity 1.0000, **zero jumps**, stripe base matching the automator's block for that song to the frame.
- **Cut-down versions:** same base, same final frame, with a single **forward jump at the edit point** — **+66.43 s** on one, **+58.90 s** on the other, each followed within ~50 ms by a small splice artifact (a few frames back, or a ~3.3 s hop) that is seam garbage or a second small trim. **The TC is carried through the edit — cut and paste, not re-stripe.**
- One full version's decoded stripe also **measured the correct offset for its timecode show**, proving a suspect inherited offset field wrong (`automator-tc-architecture`).

**Dave's read was right on every count:** a web tool reported "continuous/re-striped" (it does not refresh across a jump — an artifact), he watched the jump happen in the video machine, and called the web read wrong.

**⇒ Design consequence, which flipped the working plan for the better:** because TC values keep their musical meaning across the cut, **the full version's timecode show remains valid for the short version**. Events inside the cut span never fire (their times never arrive), and because all events address cues **by name**, the first post-cut event re-aims the sequence correctly. **Probably zero new timecode shows and zero retiming** — at most one "landing" event per cut. The seam behaviour is then tuned by `AssertPrevEvents` (`timecode-assertprevevents-and-goto-seam-controls`), which was set TRUE on every song show for exactly this.

**Lane banked:** `ltc_confirm.py` is repeatable for every future short version and outputs the exact **edit map** (cut points + skip sizes) — the ingredient list for landing events if they are ever needed.

History: extended 2026-08-08 — mechanism confirmed frame-exact on the EU leg, with the zero-new-TC-shows consequence and the repeatable decoder lane.
