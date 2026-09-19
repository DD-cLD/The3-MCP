#!/usr/bin/env python3
"""make_manifest.py — release manifest: per-file SHA-256, and the verifier.

Generate (at release time):   python3 tools/make_manifest.py
Verify a copy:                python3 tools/make_manifest.py --verify
Self-test:                    python3 tools/make_manifest.py --selftest

What this does and does not protect:
- A PASS means the tree matches the MANIFEST that shipped WITH it.
- It does NOT prove the manifest itself is authentic: whoever modifies a copy
  can regenerate the manifest. Authenticity comes from comparing your
  MANIFEST.sha256 (a single small file) against the canonical repository's,
  or from a signed release tag. The manifest turns "diff a whole tree" into
  "diff one file" — that is its whole job.
Canonical source: https://github.com/DD-cLD/The3-MCP
"""
import argparse, hashlib, os, sys, tempfile

MANIFEST = 'MANIFEST.sha256'
SKIP_DIRS = {'.git', '.venv', '__pycache__', '.pytest_cache', 'node_modules',
             '_internal', '_to_delete'}  # _to_delete: parked strays, never ship [0919-1]
SKIP_FILES = {MANIFEST, '.DS_Store', 'Icon\r'}  # Icon\r: macOS/Drive stray [0919-1, D-K]
# The redaction instruments build this tree and NEVER ship: their selftests carry
# planted fixtures of the very tokens they remove, and their token law lives in
# _internal/. Release v0.1 ships the tree they produced, not the tools that
# produced it. (Synthetic-fixture selftests are the path to shipping them later.)
NEVER_SHIP = {'tools/scrubber.py', 'tools/scrub_lint.py', 'tools/_scrublib.py'}


def walk_files(root):
    out = []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = sorted(d for d in dirnames if d not in SKIP_DIRS)
        for fn in sorted(filenames):
            if fn in SKIP_FILES:
                continue
            p = os.path.join(dirpath, fn)
            rel = os.path.relpath(p, root)
            if rel.replace(os.sep, '/') in NEVER_SHIP:
                continue
            out.append(rel.replace(os.sep, "/"))
    return sorted(out)


def sha256_of(path):
    h = hashlib.sha256()
    with open(path, 'rb') as fh:
        for chunk in iter(lambda: fh.read(65536), b''):
            h.update(chunk)
    return h.hexdigest()


def generate(root):
    lines = [f'{sha256_of(os.path.join(root, rel))}  {rel}'
             for rel in walk_files(root)]
    with open(os.path.join(root, MANIFEST), 'w', encoding='utf-8') as fh:
        fh.write('# MANIFEST.sha256 — regenerate at every release; verify with'
                 ' tools/make_manifest.py --verify\n')
        fh.write('# canonical: https://github.com/DD-cLD/The3-MCP\n')
        fh.write('\n'.join(lines) + '\n')
    print(f'manifest written: {len(lines)} files')
    return 0


def verify(root):
    mpath = os.path.join(root, MANIFEST)
    if not os.path.exists(mpath):
        print('VERDICT: FAIL — no MANIFEST.sha256 in this copy (or you are '
              'pre-release). Fetch the canonical source.')
        return 1
    want = {}
    with open(mpath, encoding='utf-8') as fh:
        for line in fh:
            line = line.rstrip('\n')
            if not line or line.startswith('#'):
                continue
            digest, rel = line.split('  ', 1)
            want[rel] = digest
    have = {rel: sha256_of(os.path.join(root, rel)) for rel in walk_files(root)}
    missing = sorted(set(want) - set(have))
    extra = sorted(set(have) - set(want))
    changed = sorted(r for r in set(want) & set(have) if want[r] != have[r])
    for r in missing:
        print(f'MISSING  {r}')
    for r in extra:
        print(f'EXTRA    {r}')
    for r in changed:
        print(f'CHANGED  {r}')
    print(f'\ncensus: {len(have)} files · {len(changed)} changed · '
          f'{len(missing)} missing · {len(extra)} extra')
    if missing or extra or changed:
        print('VERDICT: FAIL — this copy does not match its own manifest.')
        return 1
    print('VERDICT: PASS — tree matches its manifest. Now compare '
          'MANIFEST.sha256 itself against the canonical repository.')
    return 0


def selftest():
    """Prove the verifier catches tampering before trusting it."""
    with tempfile.TemporaryDirectory() as td:
        os.mkdir(os.path.join(td, 'docs'))
        with open(os.path.join(td, 'docs', 'a.md'), 'w') as f:
            f.write('alpha\n')
        with open(os.path.join(td, 'b.py'), 'w') as f:
            f.write('print(1)\n')
        generate(td)
        ok_clean = verify(td) == 0
        with open(os.path.join(td, 'docs', 'a.md'), 'a') as f:
            f.write('tampered\n')
        ok_caught = verify(td) == 1
        os.remove(os.path.join(td, 'docs', 'a.md'))
        ok_missing = verify(td) == 1
        good = ok_clean and ok_caught and ok_missing
        print(f'\nclean PASS: {ok_clean} · tamper caught: {ok_caught} · '
              f'missing caught: {ok_missing}')
        print('SELFTEST:', 'PASS' if good else 'FAIL')
        return 0 if good else 1


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('root', nargs='?',
                    default=os.path.join(os.path.dirname(
                        os.path.abspath(__file__)), '..'))
    ap.add_argument('--verify', action='store_true')
    ap.add_argument('--selftest', action='store_true')
    a = ap.parse_args()
    root = os.path.abspath(a.root)
    if a.selftest:
        sys.exit(selftest())
    sys.exit(verify(root) if a.verify else generate(root))


if __name__ == '__main__':
    main()
