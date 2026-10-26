"""Set 392 (goal run loop 38): local names without Harappa (mould copies are Harappan). Writes results/predict_test392.md."""
import random

import rtools as R
from predict_test390 import body
from predict_test391 import shuffle_test
from signs import load


def main():
    rnd = random.Random(392)
    rd = R.Round('Three-hundred-and-ninety-second registered predictions: goal loop 38, local names without Harappa', 'predict_test392')
    items = [(body(tuple(ln)), r['site'], r['sealid']) for r in load(only_m77=True) if r['site'] not in ('', 'unknown', 'Harappa')
             for ln in r['seq'] if ln and body(tuple(ln))]
    o, n, p = shuffle_test(items, rnd)
    rd.rec('LH1', "Mahadevan's texts without Harappa", '%d of %d pairs same city, shuffle p = %.4f' % (o, n, p), p < 0.05)
    A, B, rowsA, recs, F = R.load_all()
    items2 = [(body(tuple(ln)), r['site'], r['sealid']) for r in F if r['site'] != 'Harappa' and recs.get(r['sealid'])
              and str(recs[r['sealid']][20]).startswith('SEAL') for ln in r['seq'] if ln and body(tuple(ln))]
    o2, n2, p2 = shuffle_test(items2, rnd)
    rd.rec('LH2', 'ICIT seals without Harappa', '%d of %d pairs same city, shuffle p = %.4f' % (o2, n2, p2), p2 < 0.05)
    rd.rec('P', 'progress rule: either holds', 'LH1 %s, LH2 %s' % (p < 0.05, p2 < 0.05), p < 0.05 or p2 < 0.05)
    rd.finish()


if __name__ == '__main__':
    main()
