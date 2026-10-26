"""Audit of set 357 (not registered): domain models over random groups with the same group sizes as the region and
motif groups (lines assigned to groups by a fixed hash), to separate the side information from a plain ensemble gain."""
import hashlib
from collections import Counter

import loopkit as L
import rtools as R


def randkey(real, salt):
    (tr, te), (DA, DB) = L.splits()
    allines = sorted(set(tr) | set(te) | set(DA) | set(DB))
    sizes = Counter(real(t, L.META) for t in allines)
    order = sorted(allines, key=lambda t: hashlib.md5((salt + ' '.join(t)).encode()).hexdigest())
    lab, k = {}, 0
    for g, n in sizes.most_common():
        for t in order[k:k + n]:
            lab[t] = g
        k += n
    return lambda t, m: lab.get(t, '')


for name, real in (('motif', lambda t, m: m.get(t, ('', '', ''))[2]), ('region', lambda t, m: R.region(m.get(t, ('', '', ''))[0]))):
    for salt in ('a', 'b'):
        (a0, a1, la), (b0, b1, lb) = L.test_pair(L.domain_model(randkey(real, salt)))
        print('%s random groups %s: fixed %.4f -> %.4f (%.4f), A->B %.4f -> %.4f (%.4f)' % (name, salt, a0, a1, a0 - a1, b0, b1, b0 - b1))
