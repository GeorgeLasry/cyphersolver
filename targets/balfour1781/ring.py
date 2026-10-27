"""Rebuild the ring (Saberton's 'Common cipher' order) and the per-group settings from the interlinear.

Model (Saberton, JAR 2019): an inner ring of numbers turned against the alphabet. A letter at
alphabet position p, under setting k, is sent as RING[(p + k) mod 25]. Numbers >= FILLER_FROM are fillers.
The setting can change inside a letter, so it is estimated for every dash-separated group.

Usage: python ring.py            -> ring.txt, ring_decipherment.txt, agreement per page
"""
import collections
import glob
import os
import re
import string

from key_from_interlinear import load, tokens, align

HERE = os.path.dirname(os.path.abspath(__file__))
FILLER_FROM = 30
A = 'abcdefghiklmnopqrstuvwxyz'   # 25 letters, i/j one sign
M = len(A)


def groups(L):
    """Split a line into dash groups of (number, uncertain) tokens, fillers removed."""
    out, cur = [], []
    for t in tokens(L):
        if t == '-':
            if cur:
                out.append(cur)
            cur = []
        elif t[0] is not None and t[0] < FILLER_FROM:
            cur.append(t[0])
    if cur:
        out.append(cur)
    return out


def paired_groups(lines):
    """For each line, align the kept numbers with the interlinear letters; return per-group pair lists."""
    res = []
    for ln in lines:
        gs = groups(ln['L'])
        flat = [n for g in gs for n in g]
        letters = [('i' if c == 'j' else c) for c in ln['I'].lower() if c in A or c == 'j']
        if not flat or abs(len(flat) - len(letters)) > max(3, len(flat) // 5):
            res.append((ln, gs, [[] for _ in gs]))
            continue
        pairs = align(list(range(len(flat))), letters)
        bypos = {i: c for i, c in pairs}
        out, i = [], 0
        for g in gs:
            out.append([(n, bypos.get(i + j)) for j, n in enumerate(g) if bypos.get(i + j)])
            i += len(g)
        res.append((ln, gs, out))
    return res


def solve(lines, rounds=6):
    pg = paired_groups(lines)
    ring = {}       # number -> ring position (setting 0 = first group's frame)
    # seed: first group with pairs fixes the frame at k = 0
    for _, _, gp in pg:
        for pairs in gp:
            if len(pairs) >= 3:
                for n, c in pairs:
                    ring.setdefault(n, A.index(c))
                break
        if ring:
            break
    settings = {}
    for _ in range(rounds):
        votes = collections.defaultdict(collections.Counter)
        for li, (ln, gs, gp) in enumerate(pg):
            for gi, pairs in enumerate(gp):
                kv = collections.Counter((ring[n] - A.index(c)) % M for n, c in pairs if n in ring)
                if not kv:
                    continue
                k, cnt = kv.most_common(1)[0]
                if cnt < 2 and len(pairs) > 2:
                    continue
                settings[li, gi] = k
                for n, c in pairs:
                    votes[n][(A.index(c) + k) % M] += 1
        ring = {n: v.most_common(1)[0][0] for n, v in votes.items()}
    return pg, ring, settings


def main():
    lines = load(sorted(glob.glob(os.path.join(HERE, 'transcription', 'p*.txt'))))
    pg, ring, settings = solve(lines)
    pos2num = collections.defaultdict(list)
    for n, p in ring.items():
        pos2num[p].append(n)
    with open(os.path.join(HERE, 'ring.txt'), 'w', encoding='utf8') as f:
        f.write('ring position (letter under setting 0) -> numbers\n')
        for p in range(M):
            f.write(f'{p:2d} {A[p]}  {sorted(pos2num.get(p, []))}\n')
    stat = collections.Counter()
    with open(os.path.join(HERE, 'ring_decipherment.txt'), 'w', encoding='utf8') as f:
        for li, (ln, gs, gp) in enumerate(pg):
            words = []
            last_k = None
            for gi, g in enumerate(gs):
                k = settings.get((li, gi), last_k)
                last_k = k
                if k is None:
                    words.append('?' * len(g))
                    continue
                words.append(''.join(A[(ring[n] - k) % M] if n in ring else '?' for n in g))
            dec = ' '.join(words)
            il = [('i' if c == 'j' else c) for c in ln['I'].lower() if c in A or c == 'j']
            dl = [c for c in dec if c in A]
            pairs = align(dl, il)
            stat[ln['page'], 'a'] += sum(a == b for a, b in pairs)
            stat[ln['page'], 't'] += max(len(dl), len(il))
            ks = [settings.get((li, gi)) for gi in range(len(gs))]
            f.write(f"p{ln['page']} L{ln['line']:02d} k={ks}\n  L | {ln['L']}\n  I | {ln['I']}\n  D | {dec}\n\n")
    for p in sorted({ln['page'] for ln in lines}):
        print(f"p{p}: {stat[p, 'a']}/{stat[p, 't']} = {stat[p, 'a'] / max(stat[p, 't'], 1):.1%}")
    print('ring numbers placed:', len(ring), ' positions filled:', len(pos2num))


if __name__ == '__main__':
    main()
