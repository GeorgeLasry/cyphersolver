"""Session-2 loop 28: set 552 within long-stroke numerals (the second series)."""
from collections import Counter

import s2kit as K
from hyp_s2_s2common import LARGE, SMALL
from numerals import NUMS

TITLE = 'number size within long strokes'
REG = '''Set 553 confirmed set 552 within short strokes. Here long-stroke numerals (31-36) alone (`hyp_s2_seriesaudit.py`).

- **SA1** On A, of set 552's signs with 4+ long-stroke-counted tokens, 70%+ keep their small / large direction.
- **SA2** On B the same (3+ tokens).
- Progress rule: none (audit).'''
SUMMARY = ''


def run(rd):
    global SUMMARY
    DA, DB = K.ab()
    out = []
    for key, name, S, mn in (('SA1', 'A', DA, 4), ('SA2', 'B', DB, 3)):
        c = {'s': Counter(), 'l': Counter()}
        for t in S:
            for i in range(1, len(t)):
                if t[i - 1] in NUMS and NUMS[t[i - 1]][1] == 'long' and t[i] not in NUMS:
                    c['s' if NUMS[t[i - 1]][0] <= 3 else 'l'][t[i]] += 1
        ns, nl = max(1, sum(c['s'].values())), max(1, sum(c['l'].values()))
        test = [g for g in SMALL | LARGE if c['s'][g] + c['l'][g] >= mn]
        keep = sum((c['s'][g] / ns > c['l'][g] / nl) == (g in SMALL) for g in test)
        ok = bool(test) and keep / len(test) >= 0.7
        rd.rec(key, 'directions kept within long strokes, %s' % name, '%d of %d (%s)' % (keep, len(test), ' '.join(sorted(test))), ok)
        out.append((keep, len(test)))
    SUMMARY = 'long strokes: A %d/%d, B %d/%d keep direction (audit).' % (out[0] + out[1])
    return False
