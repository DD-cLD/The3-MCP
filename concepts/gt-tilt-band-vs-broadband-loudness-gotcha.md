---
id: gt-tilt-band-vs-broadband-loudness-gotcha
title: "GT's 'tilt'/'band' columns track spectral balance and rhythm-section presence, NOT broadband loudness — run an independent RMS pass before lighting a 'quiet' section as a dim-out"
role: tools
tags: [beatgrid, audio-dsp]
when_to_load: "Before treating a ground-truth section's low tilt or low band number as 'this section is quiet' — corroborate with an independent broadband RMS pass first, especially for breakdowns/outros"
status: active
source: "fleet worker FINDINGS_LOCAL, 2026-07-07"
verified: grandMA3 onPC 2.4.2.2 (Mac)
supersedes: []
superseded_by: null
---

**The gotcha:** the foreman ground-truth kit's `tilt` (spectral balance) and `band` (a coarse energy-tier label) columns are frequently mistaken for broadband loudness, but they measure something else — and on multiple songs in the same batch, a section tagged "low band"/"low tilt" turned out to measure as loud as, or louder than, sections nominally above it. **Always run a tempo-agnostic independent RMS pass** (ffmpeg decode + numpy RMS, e.g. 140 points / 0.5s windows across the actual audio file) before lighting a low-band/low-tilt section as a dim-out.

**Four independent corroborating instances, same fleet batch (2026-07-07):**
- **SONG_L:** the Breakdown is `band=0` (grouped with intro/outro, the lowest bucket) but measures **0.57** RMS — essentially tied with the intro and not far under the verses (0.75–0.83). Read: bass/drums drop out, vocal/pad texture stays up. Lit as a held glow (Bloom), not a dim-out.
- **Candy:** the Breakdown reads "low energy" (band=0) but measures **0.558** RMS — closer to the verse tier (0.62–0.76) than to the true-quiet Intro (0.208) or Outro (0.246) it's nominally grouped with. Same read, same fix (Bloom, not dim-out). Candy's build also caught and corrected its own initial misreading of a *rising* tilt in the Outro as a brightening swell — the RMS pass showed a clean near-monotonic loudness *decay* instead (0.586→0.019); tilt and RMS are different axes, and the honest reconciliation was that the low end drops out first while a thinner, brighter element lingers, raising the treble ratio even as total output falls.
- **From Scratch:** GT's tilt names Verse 4 (0.08) the quietest passage in the song by a wide margin; the independent RMS pass measures it at **0.700** — statistically identical to the surrounding verses/choruses, nowhere near the song's actual quiet points. Read as a texture/mix change (darkening/rolloff), not a volume drop — lit as a color change, not a second near-silence.
- **Pilot:** "band" clusters most sections at 0.77–0.82 regardless of nominal tier, but band=0 splits into two different realities — the pre-verse Breakdown measures as loud as any verse (0.80) while the two post-chorus sections (Turn, Hold) are genuinely the quietest in the song (0.47, 0.55). The Breakdown was lit as a present, full section (Half, not a dim-out) because of this. Pilot's Outro is a second, sharper instance of the same general gotcha: it's the **loudest sustained stretch in the entire track** (0.82 avg, peaking 0.999 near 3:02) inside a section GT tags mid-tier and tilt calls the darkest — loud and dark at once, which changed how the ending was lit (color/level kept subtracting through it rather than answering the loudness).

**Practical rule:** treat `band`/`tilt` as reliable for spectral character and rough structural grouping, but never as a loudness proxy on its own — especially for any section your first instinct wants to light as "quiet" or "recede." The independent RMS pass is cheap (no librosa dependency) and has caught a real design mistake before shipping at least once (Candy's Outro).

History: none — pattern recognized independently across four builds in the same overnight fleet batch, 2026-07-07.
