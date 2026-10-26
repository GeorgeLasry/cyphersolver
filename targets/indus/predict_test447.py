"""Set 447 (goal run loop 93): the long form (fish 705/706 33 520) against the short form (fish 520): seal size, and
the same fish name in both forms. Writes results/predict_test447.md."""
import random
from collections import defaultdict

import rtools as R
from predict_test388 import objects
from scipy.stats import mannwhitneyu


def form(t):
    for i in range(1, len(t) - 2):
        if t[i] in ('705', '706') and t[i + 1] == '33' and t[i + 2] == '520' and t[i - 1].isdigit() and 220 <= int(t[i - 1]) <= 249:
            return 'long', t[max(0, i - 2):i]
    for i in range(1, len(t)):
        if t[i] == '520' and t[i - 1].isdigit() and 220 <= int(t[i - 1]) <= 249:
            return 'short', t[max(0, i - 2):i]
    return None, None


def main():
    rnd = random.Random(447)
    rd = R.Round('Four-hundred-and-forty-seventh registered predictions: goal loop 93, long and short fish names', 'predict_test447')
    sq = objects('SEAL:S')
    lg = [s for s, t in sq if form(t)[0] == 'long']
    sh = [s for s, t in sq if form(t)[0] == 'short']
    p1 = mannwhitneyu(lg, sh, alternative='greater').pvalue if lg and sh else 1
    med = lambda x: sorted(x)[len(x) // 2] if x else 0
    rd.rec('LF1', 'long-form seals are larger than short-form seals', 'median %.1f (n %d) against %.1f (n %d), p = %.4f' % (med(lg), len(lg), med(sh), len(sh), p1), p1 < 0.05)
    A, B, *_ = R.load_all()
    lines = sorted({tuple(t) for t in A})
    names = [form(t) for t in lines if form(t)[0]]
    by = defaultdict(set)
    for f, b in names:
        by[b].add(f)
    obs = sum(1 for v in by.values() if len(v) == 2)
    forms = [f for f, b in names]
    ge = 0
    for _ in range(1000):
        rnd.shuffle(forms)
        bb = defaultdict(set)
        for f, (_, b) in zip(forms, names):
            bb[b].add(f)
        ge += sum(1 for v in bb.values() if len(v) == 2) >= obs
    p2 = (ge + 1) / 1001
    rd.rec('LF2', 'fish names appear in both forms more than chance (A)', '%d names in both forms; shuffled forms as many in %d of 1000, p = %.4f' % (obs, ge, p2), p2 < 0.05)
    rd.rec('P', 'progress rule: either holds', 'LF1 %s, LF2 %s' % (p1 < 0.05, p2 < 0.05), p1 < 0.05 or p2 < 0.05)
    rd.finish()


if __name__ == '__main__':
    main()
