"""Session-2 audit of set 593 (61 / 575 share slots): with numeral contexts removed."""
import random
from collections import Counter

import rtools as R
import s2kit as K
from hyp_s2_subst import ctx, cos

TITLE = 'audit: 61 / 575 without numeral contexts'
REG = '''Set 593 found 61 and 575 share (previous, next) contexts. Both are counted signs (set 552), so the shared part may be
'after a numeral'. Contexts whose previous sign is a numeral are dropped and the test re-run (`hyp_s2_subaudit.py`).

- **SA1** On A, 61 and 575 still share contexts beyond random partners (p < 0.05).
- **SA2** On B the same.
- Progress rule: none (audit); a failure withdraws set 593 and the logged streak is not reset by it.'''
SUMMARY = ''


def run(rd):
    global SUMMARY
    rnd = random.Random(598)
    DA, DB = K.ab()
    out = []
    for key, S in (('SA1', DA), ('SA2', DB)):
        d = ctx(S)
        for g in d:
            d[g] = Counter({k: v for k, v in d[g].items() if k[0] not in R.NUMS})
        occ = sorted(d, key=lambda g: -sum(d[g].values()))
        obs = cos(d['61'], d['575'])
        k = occ.index('575')
        pool = [g for g in occ[max(0, k - 5):k + 6] if g not in ('61', '575')]
        ge = sum(cos(d['61'], d[rnd.choice(pool)]) >= obs for _ in range(500))
        p = (ge + 1) / 501
        rd.rec(key, '61 / 575 share non-numeral contexts', 'cosine %.3f, p = %.4f' % (obs, p), p < 0.05)
        out.append(p < 0.05)
    SUMMARY = 'SA1 %s, SA2 %s (audit of set 593).' % tuple(out)
    return False
