#!/usr/bin/env python3
"""L3 — CROSS-SONG PHASER FIGURE CONTENT-HASH (v2, safe parse + scoped counts)

v1 had two defects, both caught by validating instead of reporting:
  1. iterparse + root.clear() inside the loop could drop nested Dependency
     subtrees. v2 uses a full parse per file (_figlib).
  2. v1 reported ONE number for cross-song sharing. That number silently mixed
     two very different things:
        (a) the SAME NAMED preset appearing in many songs  -> {LD} reused one
            object; we already know it is one figure. Not a discovery.
        (b) DIFFERENT names with IDENTICAL content         -> the actual question.
            This is where we have been minting duplicate pool-21 copies.
     v2 reports them separately. State the scope with the count.

GROUND TRUTH: reproduces the proven SONG_J twin (Verse 1/1 Dim#8 ==
Chorus 1/1 Dim#11 -> 9a10a77feb5b). See validate2.py.
"""
import sys, collections, csv, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _figlib import figures

# Point these at your own export. SEQ is a directory of sequence XML exported
# from the desk; OUT is where the CSVs land. Env vars keep the script portable
# between a workstation and a console share.
SEQ = os.environ.get('FIGHASH_SEQ_DIR', './export/sequences/')
OUT = os.environ.get('FIGHASH_OUT_DIR', './out/')
SONGS = [('1000','SONG_A'),('1100','SONG_B'),('1200','SONG_C'),('1300','SONG_D'),
         ('1400','SONG_E'),('1600','SONG_F[CUT]'),('1700','SONG_G'),('1800','SONG_H'),
         ('1900','SONG_I'),('2000','SONG_J'),('2100','SONG_K'),('2200','SONG_L'),
         ('2300','SONG_M'),('2400','SONG_N'),('2500','SONG_O'),
         ('2600','SONG_P'),('2700','SONG_Q'),('2800','SONG_R')]
BUILT = {'1000','1100','1200','1300','1400','1700','1800','1900','2000',
         '2100','2200','2400','2600'}   # +run songs heard by 08-05 (A0805.1)
REMAIN = {'2300','2500','2700'}         # 2800 SONG_R = empty stub, PROVISIONAL

allf, per_song = collections.defaultdict(list), {}
for sid, sname in SONGS:
    p = os.path.join(SEQ, f'gb_s{sid}.xml')
    if not os.path.exists(p):
        continue
    f = figures(p)
    per_song[sid] = len(f)
    for nm, d in f.items():
        allf[d['h']].append((sid, sname, nm, d))

same_name, multi_name, single = [], [], 0
for h, uses in allf.items():
    songs, names = {u[0] for u in uses}, {u[2] for u in uses}
    if len(songs) > 1 and len(names) > 1:  multi_name.append((h, uses))
    elif len(songs) > 1:                   same_name.append((h, uses))
    else:                                  single += 1
multi_name.sort(key=lambda x: -len({u[0] for u in x[1]}))
same_name.sort(key=lambda x: -len({u[0] for u in x[1]}))

tot_names = sum(len(v) for v in allf.values())
print('=' * 76)
print('CROSS-SONG PHASER FIGURE CONTENT-HASH — 17 songs (SONG_R 2800 is an empty stub)')
print('=' * 76)
print(f'figure NAME-instances read across the show : {tot_names}')
print(f'distinct CONTENT hashes                    : {len(allf)}')
print()
print('SCOPE SPLIT — the two things v1 conflated:')
print(f'  (a) same NAME reused across songs        : {len(same_name)} figures'
      f'  ({LD} reusing one object — already one figure to us)')
print(f'  (b) DIFFERENT names, IDENTICAL content   : {len(multi_name)} figures  <-- THE ANSWER')
print(f'  (c) content unique to a single song      : {single}')
print()
rem_saving = 0
for h, uses in multi_name:
    s = {u[0] for u in uses}
    if s & BUILT and s & REMAIN:
        rem_saving += len({u[0] for u in uses if u[0] in REMAIN})
print(f'⭐ FIGURES IN THE REMAINING {len(REMAIN)} SONGS WITH A KNOWN COPY SOURCE: {rem_saving}')
print('   (already minted for a BUILT song — the new song COPIES it into its own slot: zero decode;')
print('    never a cross-song bind — tourshow-authoring-contract, Dave 08-03)')
print()
print('--- (b) different-name/identical-content groups, widest first ---')
for h, uses in multi_name[:8]:
    songs = sorted({(u[0], u[1]) for u in uses})
    b = [s[1] for s in songs if s[0] in BUILT]
    r = [s[1] for s in songs if s[0] in REMAIN]
    d = uses[0][3]
    print(f'  {h}  {len(songs)} songs  attr={",".join(a.split(".")[-1] for a in d["attrs"])[:20]}'
          f'  steps={sorted({len(s) for s in d["shapes"]})}')
    print(f'      built  : {", ".join(b) if b else "-"}')
    print(f'      TO BUILD: {", ".join(r) if r else "-"}')
    print(f'      names  : {"; ".join(sorted({u[2] for u in uses}))[:130]}')
if len(multi_name) > 8:
    print(f'  ... +{len(multi_name)-8} more in the CSV')
print()
print('--- (a) same-name reuse, for reference (not a discovery) ---')
for h, uses in same_name[:5]:
    nm = uses[0][2]
    print(f'  {len({u[0] for u in uses}):2d} songs  "{nm}"')
print()
print('--- per-song distinct figure names ---')
print('  ' + '  '.join(f'{s}:{per_song.get(s,0)}' for s,_ in SONGS if s in per_song))

with open(OUT + 'FIGURE_HASH_SHOWWIDE_v2.csv', 'w', newline='') as fh:
    w = csv.writer(fh)
    w.writerow(['content_hash','class','n_songs','n_distinct_names','song_id','song',
                'figure_name','attributes','measures','speeds','step_counts','phaser_rows','song_status'])
    for h, uses in sorted(allf.items(), key=lambda x: -len({u[0] for u in x[1]})):
        songs, names = {u[0] for u in uses}, {u[2] for u in uses}
        cls = ('DIFF-NAME-SAME-CONTENT' if len(songs) > 1 and len(names) > 1
               else 'SAME-NAME-RECURS' if len(songs) > 1 else 'single-song')
        for sid, sname, nm, d in sorted(uses):
            w.writerow([h, cls, len(songs), len(names), sid, sname, nm,
                        '|'.join(d['attrs']), '|'.join(d['meas']), '|'.join(d['spds']),
                        '|'.join(str(len(s)) for s in sorted(d['shapes'], key=len)),
                        d['nrows'],
                        'BUILT' if sid in BUILT else ('TO BUILD' if sid in REMAIN else 'cut/empty')])
print(f'\ndetail -> generated/figure_hash/FIGURE_HASH_SHOWWIDE_v2.csv')
