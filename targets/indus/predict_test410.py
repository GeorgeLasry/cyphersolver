"""Set 410 (goal run loop 56): is the M77 locality (set 408 LW2) in seal-like or tablet-like texts? Lines with 400 (the
Harappa tablet formula 740 400) against lines without it; body-weighted, shuffle null. Writes results/predict_test410.md."""
import random

import rtools as R
from predict_test390 import body
from predict_test408 import test
from signs import load


def main():
    rnd = random.Random(410)
    rd = R.Round('Four-hundred-and-tenth registered predictions: goal loop 56, M77 locality in seal-like and tablet-like texts', 'predict_test410')
    rows = [(r, tuple(ln)) for r in load(only_m77=True) if r['site'] not in ('', 'unknown') for ln in r['seq'] if ln and body(tuple(ln))]
    seal_like = [(body(t), r['site'], r['sealid']) for r, t in rows if '400' not in t]
    tab_like = [(body(t), r['site'], r['sealid']) for r, t in rows if '400' in t]
    o, nb, p = test(seal_like, rnd)
    rd.rec('MB1', 'M77 lines without 400 (seal-like): body-weighted locality', 'mean same-city share %.3f over %d bodies, p = %.4f' % (o, nb, p), p < 0.05)
    o2, nb2, p2 = test(tab_like, rnd)
    rd.rec('MB2', 'M77 lines with 400 (tablet-like): body-weighted locality', 'mean same-city share %.3f over %d bodies, p = %.4f' % (o2, nb2, p2), p2 < 0.05)
    rd.rec('P', 'progress rule: MB1 (seal names local after all, on an independent sample)', 'MB1 %s' % (p < 0.05), p < 0.05)
    rd.finish()


if __name__ == '__main__':
    main()
