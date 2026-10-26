"""Set 391 (goal run loop 37): locality of name bodies replicated on Mahadevan's own texts (B), and within Mohenjo-daro
by excavation area. Shuffle nulls as the set 390 audit. Writes results/predict_test391.md."""
import random
import re
from collections import defaultdict

import rtools as R
from predict_test390 import body
from signs import load


def pairs_same(items):
    by = defaultdict(list)
    for b, place, oid in items:
        by[b].append((place, oid))
    h = n = 0
    for lst in by.values():
        for a in range(len(lst)):
            for c in range(a + 1, len(lst)):
                if lst[a][1] != lst[c][1]:
                    n += 1
                    h += lst[a][0] == lst[c][0]
    return h, n


def shuffle_test(items, rnd, reps=1000):
    o, n = pairs_same(items)
    places = [p for b, p, i in items]
    ge = 0
    for _ in range(reps):
        rnd.shuffle(places)
        ge += pairs_same([(b, places[k], i) for k, (b, p, i) in enumerate(items)])[0] >= o
    return o, n, (ge + 1) / (reps + 1)


def main():
    rnd = random.Random(391)
    rd = R.Round('Three-hundred-and-ninety-first registered predictions: goal loop 37, local names on B and by area', 'predict_test391')
    items = []
    for r in load(only_m77=True):
        if r['site'] in ('', 'unknown'):
            continue
        for ln in r['seq']:
            b = body(tuple(ln)) if ln else None
            if b:
                items.append((b, r['site'], r['sealid']))
    o, n, p = shuffle_test(items, rnd)
    rd.rec('LA1', "objects sharing a name body come from one city, on Mahadevan's texts", '%d of %d pairs same city, shuffle p = %.4f' % (o, n, p), p < 0.05)
    A, B, rowsA, recs, F = R.load_all()
    items2 = []
    for r in F:
        rec = recs.get(r['sealid'])
        if r['site'] != 'Mohenjo-daro' or not rec or not str(rec[20]).startswith('SEAL'):
            continue
        m = re.match(r'[A-Z]{2}', str(rec[4]))
        if not m:
            continue
        for ln in r['seq']:
            b = body(tuple(ln)) if ln else None
            if b:
                items2.append((b, m.group(0), r['sealid']))
    o2, n2, p2 = shuffle_test(items2, rnd)
    rd.rec('LA2', 'Mohenjo-daro seals sharing a name body come from one excavation area', '%d of %d pairs same area, shuffle p = %.4f' % (o2, n2, p2), p2 < 0.05)
    rd.rec('P', 'progress rule: either holds', 'LA1 %s, LA2 %s' % (p < 0.05, p2 < 0.05), p < 0.05 or p2 < 0.05)
    rd.finish()


if __name__ == '__main__':
    main()
