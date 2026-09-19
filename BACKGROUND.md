# Background

*Optional. Nothing here is needed to use the toolkit — see `RELEASE_NOTES.md`.*

Over one festival season a touring lighting director and an AI co-programmer
rebuilt a 19-song headline show on grandMA3, on a live console, under real
deadlines. The AI read the source show's exported XML, decoded its phaser
figures and effect architecture, emitted new sequences file-side, imported them
through a safety-gated MCP bridge, bound MAtricks, and verified every step
against the desk. The human ruled on taste, tempo, timecode, and every moment
the console was touched. Songs went from cold boot to heard-under-timecode in
single sessions. The show then went out on a European festival leg, where the
same pair worked out how to adapt a fixed programming set to a different rig
every few days.

This repository is what that produced other than the show itself: the bridge,
the build kit, the session workflows, the operating discipline, and several
hundred console truths — each earned by tripping over a silent failure,
catching it with a verification pass, and writing down exactly what the console
actually does.

Two things are worth stating plainly, because they are the transferable part.

**The knowledge did not exist in public.** grandMA3's deep behaviour — what the
CLI does silently, what an import resolver actually accepts, which Lua reads
lie, what deletes a timecode track's events — lived in scattered forums and
veterans' heads. Each lesson here was paid for with live-console time and
written down with its receipt.

**The method mattered more than any tool.** The discovery was an operating
rhythm that lets a human and an AI share one dangerous command surface safely:
written batch contracts, per-batch clearance callouts, checkpoints before
imports, and the standing rule that no clean echo is ever trusted — every write
is proven by reading the result back and counting it by name.

The show, the artist, and the original designer's work are not in this
repository and never will be. The names are gone; the craft is kept.
