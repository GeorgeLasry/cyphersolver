"""Set 408 (goal run loop 54): local names with every name body weighted equally (the set 407 note). Writes results/predict_test408.md."""
import random
from collections import defaultdict

import rtools as R
from predict_test390 import body
from signs import load


def body_share(items):
    by = defaultdict(list)
    for b, place, oid in items:
        by[b].append((place, oid))
    shares = []
    for lst in by.values():
        h = n = 0
        for a in range(len(lst)):
            for c in range(a + 1, len(lst)):
                if lst[a][1] != lst[c][1]:
                    n += 1
                    h += lst[a][0] == lst[c][0]
        if n:
            shares.append(h / n)
    return sum(shares) / max(1, len(shares)), len(shares)


def test(items, rnd, reps=1000):
    o, nb = body_share(items)
    places = [p for b, p, i in items]
    ge = 0
    for _ in range(reps):
        rnd.shuffle(places)
        ge += body_share([(b, places[k], i) for k, (b, p, i) in enumerate(items)])[0] >= o
    return o, nb, (ge + 1) / (reps + 1)


def main():
    rnd = random.Random(408)
    rd = R.Round('Four-hundred-and-eighth registered predictions: goal loop 54, local names with bodies weighted equally', 'predict_test408')
    A, B, rowsA, recs, F = R.load_all()
    items = [(body(tuple(ln)), r['site'], r['sealid']) for r in F if recs.get(r['sealid']) and str(recs[r['sealid']][20]).startswith('SEAL')
             for ln in r['seq'] if ln and body(tuple(ln))]
    o, nb, p = test(items, rnd)
    rd.rec('LW1', 'ICIT seals, bodies weighted equally', 'mean same-city share %.3f over %d bodies, p = %.4f' % (o, nb, p), p < 0.05)
    items2 = [(body(tuple(ln)), r['site'], r['sealid']) for r in load(only_m77=True) if r['site'] not in ('', 'unknown')
              for ln in r['seq'] if ln and body(tuple(ln))]
    o2, nb2, p2 = test(items2, rnd)
    rd.rec('LW2', "Mahadevan's texts, bodies weighted equally", 'mean same-city share %.3f over %d bodies, p = %.4f' % (o2, nb2, p2), p2 < 0.05)
    rd.rec('P', 'progress rule: none (audit of sets 390-391)', 'LW1 %s, LW2 %s' % (p < 0.05, p2 < 0.05), False)
    rd.finish()


if __name__ == '__main__':
    main()
