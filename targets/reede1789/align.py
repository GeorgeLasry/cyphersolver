"""Align glossed runs of unglossed_*.txt (CT + PT, no AL) to their groups by dynamic programming, anchored on table values.

Each group takes a piece of the gloss's letters (1-14 letters); a piece equal to the group's current table value
scores +2 (sure value) or +1, any other piece costs 0.3. The best split is kept when at least half the groups with
a table value land on it. Output: aligned_unglossed.txt in the pairs format (AL lines), which table.py then reads
with the hand alignments.  Usage: python align.py [fold k of 2: 0, 1 or all]
"""
import glob, os, re, sys, unicodedata
from decode import load
from table import norm_group

HERE = os.path.dirname(os.path.abspath(__file__))


def nz(s):
    return re.sub('[^a-z]', '', unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode().lower())


def runs():
    for f in sorted(glob.glob(os.path.join(HERE, 'unglossed_*.txt'))):
        tag = ct = None
        for r in open(f, encoding='utf8'):
            if r.startswith('# id'):
                tag = r[2:].strip()
            elif r.startswith('CT:'):
                ct = [g for g in r[3:].split() if g != '?' and norm_group(g)[0]]
            elif r.startswith('PT:') and ct:
                pt = nz(r[3:])
                if pt and pt != 'none':
                    yield tag, ct, pt
                ct = None


def align(ct, pt, M, B):
    n, L = len(ct), len(pt)
    NEG = -1e9
    best = [[NEG] * (L + 1) for _ in range(n + 1)]
    back = [[None] * (L + 1) for _ in range(n + 1)]
    best[0][0] = 0
    vals = []
    for g in ct:
        k, key = norm_group(g)
        v = M.get(key) or B.get(k)
        vals.append((nz(v[0]), v[1]) if v else (None, False))
    for i in range(n):
        val, sure = vals[i]
        for j in range(L + 1):
            if best[i][j] == NEG:
                continue
            for ln in range(1, min(14, L - j) + 1):
                piece = pt[j:j + ln]
                s = (2 if sure else 1) if val and piece == val else -0.3
                if best[i][j] + s > best[i + 1][j + ln]:
                    best[i + 1][j + ln] = best[i][j] + s
                    back[i + 1][j + ln] = (j, piece)
    if best[n][L] == NEG:
        return None
    pieces, j = [], L
    for i in range(n, 0, -1):
        pj, piece = back[i][j]
        pieces.append(piece); j = pj
    pieces.reverse()
    known = [i for i in range(n) if vals[i][0]]
    hit = sum(1 for i in known if pieces[i] == vals[i][0])
    return pieces if known and hit * 2 >= len(known) else None


if __name__ == '__main__':
    fold = sys.argv[1] if len(sys.argv) > 1 else 'all'
    M, B = load()
    out, kept, tot = [], 0, 0
    for idx, (tag, ct, pt) in enumerate(runs()):
        if fold != 'all' and idx % 2 != int(fold):
            continue
        tot += 1
        p = align(ct, pt, M, B)
        if p:
            kept += 1
            out.append(f'# scan {tag}\nCT: {" ".join(ct)}\nAL: ' + ' '.join(f'{g}={x}' for g, x in zip(ct, p)) + '\n')
    open(os.path.join(HERE, 'pairs_auto.txt'), 'w', encoding='utf8').write(''.join(out))
    print(f'fold {fold}: {kept} of {tot} glossed runs aligned -> pairs_auto.txt')
