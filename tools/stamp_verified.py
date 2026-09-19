#!/usr/bin/env python3
"""stamp_verified.py — adds `verified: grandMA3 onPC 2.4.2.2 (Mac)` to every concept
whose frontmatter lacks a `verified:` line.  [0919-1cLD, decision D-F]

The corpus's credibility frame is "attested, version-stamped" — every concept was
earned against onPC 2.4.2.2 on a Mac (the build era) or on the EU tour leg, which
stamps itself. Concepts already carrying `verified:` are left byte-identical.
Idempotent. Reports the count.  Usage: python3 tools/stamp_verified.py [concepts]
"""
import os, sys
STAMP = 'verified: grandMA3 onPC 2.4.2.2 (Mac)'
cdir = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'concepts')
added = had = skipped = 0
for fn in sorted(os.listdir(cdir)):
    if not fn.endswith('.md') or fn in ('INDEX.md', 'SPINE.md'):
        continue
    p = os.path.join(cdir, fn); lines = open(p, encoding='utf-8').read().split('\n')
    if not lines or lines[0].strip() != '---':
        skipped += 1; continue
    try:
        end = next(i for i in range(1, len(lines)) if lines[i].strip() == '---')
    except StopIteration:
        skipped += 1; continue
    fm = lines[1:end]
    if any(l.startswith('verified:') for l in fm):
        had += 1; continue
    at = next((i for i, l in enumerate(fm) if l.startswith('supersedes:')), len(fm))
    fm.insert(at, STAMP)
    open(p, 'w', encoding='utf-8').write('\n'.join(lines[:1] + fm + lines[end:]))
    added += 1
print(f'stamp_verified: added {added} · already stamped {had} · no frontmatter {skipped}')
