"""Set 411 (goal run loop 57): ICIT seals restricted to Mohenjo-daro, Harappa and Lothal, body-weighted (the set 410
conflict). Writes results/predict_test411.md."""
import random

import rtools as R
from predict_test390 import body
from predict_test408 import test

SITES = {'Mohenjo-daro', 'Harappa', 'Lothal'}


def main():
    rnd = random.Random(411)
    rd = R.Round('Four-hundred-and-eleventh registered predictions: goal loop 57, ICIT seals at the three big sites', 'predict_test411')
    A, B, rowsA, recs, F = R.load_all()
    items = [(body(tuple(ln)), r['site'], r['sealid']) for r in F if r['site'] in SITES and recs.get(r['sealid'])
             and str(recs[r['sealid']][20]).startswith('SEAL') for ln in r['seq'] if ln and body(tuple(ln))]
    o, nb, p = test(items, rnd)
    rd.rec('CR1', 'ICIT seals at Mohenjo-daro, Harappa, Lothal: body-weighted locality', 'mean same-city share %.3f over %d bodies, p = %.4f' % (o, nb, p), p < 0.05)
    items2 = [x for x in items if x[1] != 'Lothal']
    o2, nb2, p2 = test(items2, rnd)
    rd.rec('CR2', 'ICIT seals at Mohenjo-daro and Harappa only', 'mean same-city share %.3f over %d bodies, p = %.4f' % (o2, nb2, p2), p2 < 0.05)
    rd.rec('P', 'progress rule: none (audit)', 'CR1 %s, CR2 %s' % (p < 0.05, p2 < 0.05), False)
    rd.finish()


if __name__ == '__main__':
    main()
