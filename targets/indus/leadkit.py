"""Shared helpers for sets 642-651 (the ten leads of 26 Oct 2026)."""
import math
import subprocess
from collections import Counter

import rtools as R
from signs import load


def ab():
    A, B, rowsA, recs, F = R.load_all()
    DA = sorted({tuple(t) for t in A})
    DB = sorted({tuple(ln) for r in load(only_m77=True) for ln in r['seq'] if ln} - set(DA))
    return DA, DB


def objects():
    """(site, subtype, motif, field 31 size, lines) for clean ICIT objects with a record."""
    A, B, rowsA, recs, F = R.load_all()
    out = []
    for r in F:
        rec = recs.get(r['sealid'])
        if rec:
            out.append((rec[3].strip(), ':'.join(rec[20].split(':')[:2]), rec[18].split(':')[0].strip(), rec[31], [tuple(t) for t in r['seq'] if t], rec))
    return out


def mi(pairs):
    n = len(pairs)
    if not n:
        return 0.0
    cx, cy, cxy = Counter(a for a, b in pairs), Counter(b for a, b in pairs), Counter(pairs)
    return sum(v / n * math.log2(v * n / (cx[a] * cy[b])) for (a, b), v in cxy.items())


def register(text, paths):
    p = 'PREDICTIONS.md'
    s = open(p, encoding='utf-8').read().rstrip('\n')
    open(p, 'w', encoding='utf-8').write(s + '\n\n' + text.strip() + '\n')
    git('indus: register ' + text.strip().split('\n')[0][2:60], ['targets/indus/PREDICTIONS.md'] + ['targets/indus/' + x for x in paths])


def record(text, row, paths):
    p = 'PREDICTIONS.md'
    s = open(p, encoding='utf-8').read().rstrip('\n')
    open(p, 'w', encoding='utf-8').write(s + '\n\n' + text.strip() + '\n')
    p = 'PROGRESS.md'
    s = open(p, encoding='utf-8').read().rstrip('\n')
    open(p, 'w', encoding='utf-8').write(s + '\n' + row.strip() + '\n')
    git('indus: ' + text.strip().split('\n')[0][3:70], ['targets/indus/PREDICTIONS.md', 'targets/indus/PROGRESS.md'] + ['targets/indus/' + x for x in paths])


def git(msg, paths):
    subprocess.run(['git', 'add'] + paths, cwd='../..', check=True)
    subprocess.run(['git', 'commit', '-q', '-m', msg + '\n\nCo-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>'], cwd='../..', check=True)
