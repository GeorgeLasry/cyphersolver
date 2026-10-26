"""Audit of set 395 WD1 (not registered): dividers not preceded by a heading sign (817 / 820 / 861)."""
import random

import predict_test395 as T
import rtools as R
from signs import load

rnd = random.Random(3950)
A, B, *_ = R.load_all()
DA = sorted({tuple(t) for t in A})
DB = sorted({tuple(ln) for r in load(only_m77=True) for ln in r['seq'] if ln} - set(DA))
HEAD = {'817', '820', '861'}
orig = T.DIV
for name, L in (('A', DA), ('B', DB)):
    # strip heading + divider at line start, then rerun on the remaining positions
    L2 = [t[2:] if len(t) > 3 and t[0] in HEAD and t[1] in orig else t for t in L]
    print(name, 'without headings: cosine %.3f over %d tokens, p = %.4f' % T.divider_test(L2, rnd))
