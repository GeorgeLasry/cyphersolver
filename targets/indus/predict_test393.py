"""Set 393 (goal run loop 39): which part of a name is local, the head (sign before the ending) or the first sign of the
name body? Seal pairs sharing only that part; shuffle null. Writes results/predict_test393.md."""
import random
from collections import defaultdict

import rtools as R
from predict_test390 import body


def main():
    rnd = random.Random(393)
    rd = R.Round('Three-hundred-and-ninety-third registered predictions: goal loop 39, which part of a name is local', 'predict_test393')
    A, B, rowsA, recs, F = R.load_all()
    items = [(body(tuple(ln)), r['site'], r['sealid']) for r in F if recs.get(r['sealid']) and str(recs[r['sealid']][20]).startswith('SEAL')
             for ln in r['seq'] if ln and body(tuple(ln))]

    def stat(places, part, other):
        by = defaultdict(list)
        for k, (b, s, i) in enumerate(items):
            by[part(b)].append((other(b), places[k], i))
        h = n = 0
        for lst in by.values():
            for a in range(len(lst)):
                for c in range(a + 1, len(lst)):
                    if lst[a][2] != lst[c][2] and lst[a][0] != lst[c][0]:
                        n += 1
                        h += lst[a][1] == lst[c][1]
        return h, n

    def test(key, title, part, other):
        places = [s for b, s, i in items]
        o, n = stat(places, part, other)
        ge = 0
        for _ in range(500):
            pl = list(places)
            rnd.shuffle(pl)
            ge += stat(pl, part, other)[0] >= o
        p = (ge + 1) / 501
        rd.rec(key, title, '%d of %d pairs same city, shuffle p = %.4f' % (o, n, p), p < 0.05)
        return p < 0.05
    o1 = test('NP1', 'seals sharing only the head sign come from one city', lambda b: b[-1], lambda b: b[:-1])
    o2 = test('NP2', "seals sharing only the name's first sign come from one city", lambda b: b[0], lambda b: b[1:])
    rd.rec('P', 'progress rule: either holds', 'NP1 %s, NP2 %s' % (o1, o2), o1 or o2)
    rd.finish()


if __name__ == '__main__':
    main()
