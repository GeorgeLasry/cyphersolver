"""Set 451 (goal run loop 97): the seal-size findings on rectangular seals. Writes results/predict_test451.md."""
from collections import Counter
from statistics import median

import rtools as R
from predict_test379 import mantel_haenszel
from predict_test388 import objects


def main():
    rd = R.Round('Four-hundred-and-fifty-first registered predictions: goal loop 97, size findings on rectangular seals', 'predict_test451')
    rc = objects('SEAL:R')
    cut = median(s for s, t in rc)
    cnt = Counter(t for s, t in rc)
    band = lambda t: min(max(len(t), 2), 7)
    tabs = []
    for b in sorted({band(t) for s, t in rc}):
        sm = [cnt[t] > 1 for s, t in rc if band(t) == b and s <= cut]
        lg = [cnt[t] > 1 for s, t in rc if band(t) == b and s > cut]
        tabs.append([[sum(sm), len(sm) - sum(sm)], [sum(lg), len(lg) - sum(lg)]])
    o1, p1 = mantel_haenszel(tabs)
    rd.rec('RZ1', 'small rectangular seals repeat texts more often at equal length', 'odds ratio small/large %.2f, p = %.4f' % (o1, p1), o1 > 1 and p1 < 0.05)
    lg = [t for s, t in rc if s > cut]
    sm = [t for s, t in rc if s <= cut]
    rate = lambda S, g: sum(g in t for t in S) / max(1, len(S))
    dirs = {g: rate(lg, g) > rate(sm, g) for g in ('706', '156', '400', '590')}
    same = sum(dirs['706']) if False else (dirs['706'] + sum(not dirs[g] for g in ('156', '400', '590')))
    rd.rec('RZ2', 'all four core size signs lean the same way on rectangular seals', '%d of 4 (%s)' % (same, ', '.join('%s %.3f/%.3f' % (g, rate(lg, g), rate(sm, g)) for g in dirs)), same == 4)
    rd.rec('P', 'progress rule: either holds', 'RZ1 %s, RZ2 %s' % (o1 > 1 and p1 < 0.05, same == 4), (o1 > 1 and p1 < 0.05) or same == 4)
    rd.finish()


if __name__ == '__main__':
    main()
