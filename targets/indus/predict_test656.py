"""Set 656 (lead 5): is a ligature a compressed sequence? The host + stroke ligatures whose components are certain from
Parpola's descriptions (U with 2 / 3 strokes inside = P311 / P312; jar with 1 / 2 / 3 strokes = P325-327), against the
written-out sequences numeral + host. Writes results/predict_test656.md."""
import math
import random
from collections import Counter, defaultdict

import cisi
import rtools as R
from leadkit import ab, objects

LIGS = {'P311': ('2', '700'), 'P312': ('3', '700'), 'P325': ('1', '740'), 'P326': ('2', '740'), 'P327': ('3', '740')}
LONG = {'1': '31', '2': '32', '3': '33'}


def contexts(L):
    d = defaultdict(Counter)
    for t in L:
        s = ('^',) + t + ('$',)
        for i in range(1, len(s) - 1):
            d[s[i]][(s[i - 1], s[i + 1])] += 1
    return d


def seq_ctx(L, pair):
    c = Counter()
    for t in L:
        s = ('^',) + t + ('$',)
        for i in range(1, len(s) - 2):
            if (s[i], s[i + 1]) == pair:
                c[(s[i - 1], s[i + 2])] += 1
    return c


def cos(a, b):
    num = sum(a[k] * b[k] for k in a)
    den = math.sqrt(sum(v * v for v in a.values())) * math.sqrt(sum(v * v for v in b.values()))
    return num / den if den else 0.0


def run(L, rnd, rd, name, long_strokes):
    p2i = cisi.p2icit()
    ctx = contexts(L)
    occ = Counter(g for t in L for g in t)
    res = []
    for p, (num, host) in LIGS.items():
        lig = {g for g in p2i.get(p, set()) if occ[g]}
        if not lig:
            continue
        lc = Counter()
        for g in lig:
            lc.update(ctx[g])
        pair = (LONG[num] if long_strokes else num, host)
        sc = seq_ctx(L, pair)
        if sum(sc.values()) < 3 or sum(lc.values()) < 3:
            res.append((p, sorted(lig), pair, sum(lc.values()), sum(sc.values()), None, None))
            continue
        obs = cos(lc, sc)
        n = sum(occ[g] for g in lig)
        pool = sorted((g for g in occ if g not in lig and g not in R.NUMS), key=lambda g: abs(occ[g] - n))[:20]
        null = [cos(ctx[rnd.choice(pool)], sc) for _ in range(500)]
        pv = (sum(x >= obs for x in null) + 1) / 501
        res.append((p, sorted(lig), pair, sum(lc.values()), sum(sc.values()), obs, pv))
    for r in res:
        rd.say('- %s: ligature %s (%d tokens) against sequence %s (%d): %s' % (name, '/'.join(r[1]), r[3], ' '.join(r[2]), r[4], 'cosine %.3f, p = %.3f' % (r[5], r[6]) if r[5] is not None else 'too few'))
    tested = [r for r in res if r[5] is not None]
    return tested, sum(r[6] < 0.05 for r in tested)


def main():
    rd = R.Round('Set 656 registered predictions: host + stroke ligatures against their written-out sequences', 'predict_test656')
    rnd = random.Random(656)
    F = sorted({t for s, ty, mo, size, lines, rec in objects() for t in lines})
    DA, DB = ab()
    tf, hf = run(F, rnd, rd, 'ICIT short strokes', False)
    tl, hl = run(F, rnd, rd, 'ICIT long strokes', True)
    tb, hb = run(DB, rnd, rd, 'M77 short strokes', False)
    rd.say()
    rd.rec('LG1', 'on the clean ICIT lines, a majority of the testable ligatures share the contexts of their short-stroke sequence beyond frequency-matched signs (p < 0.05)', '%d of %d' % (hf, len(tf)), bool(tf) and hf > len(tf) / 2)
    rd.rec('LG2', 'the same on Mahadevan\'s lines', '%d of %d' % (hb, len(tb)), bool(tb) and hb > len(tb) / 2)
    rd.rec('LG3', 'with long-stroke sequences instead (Wells\'s volumetric form), the same on ICIT', '%d of %d' % (hl, len(tl)), bool(tl) and hl > len(tl) / 2)
    rd.rec('P', 'progress rule: LG1 and LG2 (ligatures abbreviate sequences, so a ligature reads as its parts)', '', bool(tf) and hf > len(tf) / 2 and bool(tb) and hb > len(tb) / 2)
    rd.finish()


if __name__ == '__main__':
    main()
