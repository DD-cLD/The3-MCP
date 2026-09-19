---
id: tc-split-bounces-and-ltc-tools
title: "TC-split playback bounces: never MP3, always split channels, and the LTC tooling that validates it"
role: tools
tags: [tourshow, audio-dsp]
when_to_load: "Before processing any tour playback bounce that carries SMPTE LTC on a channel, or before running beatgrid analysis on tour audio; also before puzzling over weak/anomalous beatgrid results on a real tour bounce, or when a new bounce needs its TC-slot placement confirmed"
status: active
source: "MEMORY §Bird's Eye tour — team, routing, file architecture, LTC — TC-split playback bounces + LTC, 2026-07-02 evening; findings/INBOX.md 2026-07-07 + wrap 2026-07-07-beatgrid04-festival-tc"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

- Tour bounces arrive as **stereo WAVs: one channel music, one channel SMPTE LTC**. A mono mixdown of these = constant-energy LTC floor → **poisons RMS/section analysis**. **Always split the channels.**
- **NEVER convert the split bounces to MP3** — lossy encoding smears LTC biphase edges; joint stereo bleeds channels. **WAVs are masters**; WAV is also the *preferred* input format for the whole analysis stack (soundfile/librosa/browser). ffmpeg (in the VM) is fine for making music-channel-only listening copies, but not for the masters.
- **Tools live in `beatgrid/Meta/`:**
  - `ltc_tools.py` — gen/detect/decode LTC: zero-crossings → biphase bits → sync word `0011111111111101` → BCD.
  - `analyze_track_v2.py` — auto channel detect, `--music L|R` override, music-only analysis, `channels` + `tc` JSON blocks.
  - Validated round-trip: 30 fps @ `01:00:00:00` and 25 fps @ `02:03:45:10`, continuity 1.0, no false positive on plain stereo music. "SONG_Q" regression test = identical to v1.
- **`beatgrid.html` "TC split" selector** (auto/off/L/R): music-only waveform/analysis/playback (`S.playBuf`), JS LTC decoder (node-verified = Python results), status announces split + true TC, `fpsSel` snaps to decoded rate, **QCaller base-TC auto-fills from decoded LTC**, `grid.tcStart`/`grid.tcFps` persist through session save/load.
- **fmtSMPTE bug, fixed 2026-07-07 (beatgrid 0.4.1):** `fmtSMPTE` ignored the decoded LTC start entirely, so the clock+table showed **ELAPSED** time on tour bounces instead of true TC (e.g. a 00:30-slot file read as `00:00:00:00`). **Fixed via `tcBaseFrames`.** QCaller export was already computing true TC, so this bug did not double-count there.
- **v1 analyzer bug (fixed in v2):** the agglomerative segmentation boundary index can exceed the beat array on short files — clamp with `beat_times[min(b, len-1)]`.
- **SONG-Q-convention SMPTE** in deliverables computes from **0.1s-rounded times**, so SMPTE == session JSON == QCaller (otherwise half-frame drift creeps in between the three representations).

**Real tour-bounce validation (2026-07-07, first two {TOUR} bounces, `ARTIST_Timecode_WAV/`):**
- **TC-split does NOT hurt detection.** Weak-looking results on `01_INTRO.GENIUS` were diagnosed as multi-segment material analyzed with whole-file statistics, not an LTC/split artifact — see `beatgrid-dsp-reality-check` for the root-cause mechanism and `beatgrid-region-scoped-detection` for the fix. Evidence: album-envelope xcorr on the Genius body locks at 102s (r=0.74, matching the ~100s intro before the body); a same-math replica found 92 hits/sections/BPM identical to the album (119.7 both); **zero LTC bleed into the music channel** (quietest-5s spectral ratio 0.168).
- **Tour TC map — file-number-to-slot-index theory is DEAD (corrected 2026-07-07):** this bullet previously read the two known bounces (`01_INTRO.GENIUS` = `00:00:00:00`, `02_SONG-B` = `00:30:00:00`) as evidence that file number predicts slot index. It doesn't: `09_SONG-G`'s decoded LTC start is `03:29:53:22 @30ND, continuity 1.0` — a real :30 slot boundary (~6s pre-roll before `03:30:00:00`) — but file number 09 is nowhere near that slot's index. **The underlying 30-minute slot grid itself IS real and now sheet-confirmed** (see `tourshow-artist-tc-sheet`) — it's specifically the file-number-predicts-slot shortcut that's dead. **Correct method: decode each bounce's LTC individually and keep a slot ledger** — see `tourshow-tour-audio-bounce-inventory` for the ledger so far. Both original bounces remain accurate as data points: 30fps non-drop, continuity 1.0, TC on L / music on R matching filenames. See also `beatgrid-tc-carried-cuts-and-seam-gap` for how short-form/variant bounces additionally encode edits directly in their TC.
- **Tour bounce files are float32 WAV (fmt tag 3).** Python stdlib `wave` refuses them (needs a RIFF parser — lives in the session harness); browser `decodeAudioData` handles them fine. Music channels can exceed 0 dBFS (Genius peak 1.414, SONG_B exactly 1.000) — doesn't affect analysis (relative thresholds), but could clip the DAC on playback — a normalize-on-playback toggle is a someday idea. **Update 2026-07-07: the fleet now spans both formats** — the SONG_G bounces (`09_SONG-G`, `21_SONG-G SHORT`) arrived as **int32 PCM 48k** instead of float32; beatgrid's loaders handle both.

History: none — recorded 2026-07-02 evening, no later correction found. Complements `beatgrid-dsp-reality-check` (which is about analysis reliability, not audio-file handling). 2026-07-07: real tour-bounce validation added (TC-split cleared, TC slot map at verify pending more data, float32 WAV format facts). 2026-07-07 (later same day, SONG_G bounces): fmtSMPTE bug fixed via `tcBaseFrames`; file-number-to-slot-index theory corrected to dead (the slot grid itself remains real and sheet-confirmed); int32 format added alongside float32.
