"""Session-2 loop 24: the jar 740 after a number: a counted jar, not the ending?"""
import rtools as R
import s2kit as K
from numerals import NUMS
from scipy.stats import fisher_exact

TITLE = 'the jar after a number'
REG = '''740 directly after a numeral of value 4+ against 740 after a non-numeral (`hyp_s2_countedjar.py`). The ending 740
closes a name and is usually followed by nothing or 400 / 90; a counted jar would sit inside count records.

- **CJ1** On A, 740 after a large number is followed by further signs (other than 400 / 90) more often than 740 after a
  non-numeral (Fisher p < 0.05).
- **CJ2** The same on B.
- Progress rule: CJ1 and CJ2 (740 has a second use: a counted jar).'''
SUMMARY = ''


def tab(S):
    a = [[0, 0], [0, 0]]
    for t in S:
        for i in range(1, len(t)):
            if t[i] == '740':
                row = 0 if (t[i - 1] in NUMS and NUMS[t[i - 1]][0] >= 4) else (1 if t[i - 1] not in NUMS else None)
                if row is None:
                    continue
                more = any(g not in ('400', '90') for g in t[i + 1:])
                a[row][0 if more else 1] += 1
    return a


def run(rd):
    global SUMMARY
    DA, DB = K.ab()
    out = []
    for key, name, S in (('CJ1', 'A', DA), ('CJ2', 'B', DB)):
        a = tab(S)
        p = fisher_exact(a, alternative='greater')[1]
        rd.rec(key, 'counted 740 is followed by more, %s' % name, 'after a large number %d of %d; after a word %d of %d; p = %.4f' % (a[0][0], sum(a[0]), a[1][0], sum(a[1]), p), p < 0.05)
        out.append((p < 0.05, a))
    SUMMARY = 'A %d/%d vs %d/%d; B %d/%d vs %d/%d.' % (out[0][1][0][0], sum(out[0][1][0]), out[0][1][1][0], sum(out[0][1][1]), out[1][1][0][0], sum(out[1][1][0]), out[1][1][1][0], sum(out[1][1][1]))
    return out[0][0] and out[1][0]
