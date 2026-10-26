"""Set 407 (goal run loop 53): are 740 names more local than 520 names? Seals (ICIT, clean) and Mahadevan's texts.
Writes results/predict_test407.md."""
import random
from collections import defaultdict

import rtools as R
from signs import load


def body_end(t):
    for i in range(len(t) - 1, 0, -1):
        if t[i] in R.END:
            return (tuple(t[max(0, i - 3):i]), t[i]) if i >= 2 else None
    return None


def same_share(items):
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


def test(items, rnd, reps=1000):
    e740 = [(b, p, i) for (b, e), p, i in items if e == '740']
    e520 = [(b, p, i) for (b, e), p, i in items if e == '520']
    h1, n1 = same_share(e740)
    h2, n2 = same_share(e520)
    obs = h1 / max(1, n1) - h2 / max(1, n2)
    labels = [e for (b, e), p, i in items]
    ge = 0
    for _ in range(reps):
        rnd.shuffle(labels)
        x = [((b, labels[k]), p, i) for k, ((b, e), p, i) in enumerate(items)]
        a = same_share([(b, p, i) for (b, e), p, i in x if e == '740'])
        c = same_share([(b, p, i) for (b, e), p, i in x if e == '520'])
        ge += a[0] / max(1, a[1]) - c[0] / max(1, c[1]) >= obs
    return h1, n1, h2, n2, (ge + 1) / (reps + 1)


def main():
    rnd = random.Random(407)
    rd = R.Round('Four-hundred-and-seventh registered predictions: goal loop 53, are 740 names more local than 520 names?', 'predict_test407')
    A, B, rowsA, recs, F = R.load_all()
    items = [(body_end(tuple(ln)), r['site'], r['sealid']) for r in F if recs.get(r['sealid']) and str(recs[r['sealid']][20]).startswith('SEAL')
             for ln in r['seq'] if ln and body_end(tuple(ln))]
    h1, n1, h2, n2, p = test(items, rnd)
    rd.rec('LE1', 'ICIT seals: 740 bodies share a city more often than 520 bodies', '740 %d of %d, 520 %d of %d, p = %.4f' % (h1, n1, h2, n2, p), p < 0.05)
    items2 = [(body_end(tuple(ln)), r['site'], r['sealid']) for r in load(only_m77=True) if r['site'] not in ('', 'unknown')
              for ln in r['seq'] if ln and body_end(tuple(ln))]
    h1, n1, h2, n2, p2 = test(items2, rnd)
    rd.rec('LE2', "Mahadevan's texts: the same", '740 %d of %d, 520 %d of %d, p = %.4f' % (h1, n1, h2, n2, p2), p2 < 0.05)
    rd.rec('P', 'progress rule: both hold (replicated)', 'LE1 %s, LE2 %s' % (p < 0.05, p2 < 0.05), p < 0.05 and p2 < 0.05)
    rd.finish()


if __name__ == '__main__':
    main()
