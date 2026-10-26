"""Set 466 (goal run loop 112): do long-form texts recur less? Writes results/predict_test466.md."""
from collections import Counter

import rtools as R
from predict_test379 import mantel_haenszel
from predict_test441 import has_formula


def run(prefix):
    A, B, rowsA, recs, F = R.load_all()
    texts = [tuple(r['flat']) for r in F if recs.get(r['sealid']) and str(recs[r['sealid']][20]).startswith(prefix) and r['flat']]
    cnt = Counter(texts)
    band = lambda t: min(max(len(t), 2), 8)
    tabs = []
    for b in sorted({band(t) for t in texts}):
        x = [cnt[t] > 1 for t in texts if band(t) == b and has_formula(t)]
        y = [cnt[t] > 1 for t in texts if band(t) == b and not has_formula(t)]
        tabs.append([[sum(x), len(x) - sum(x)], [sum(y), len(y) - sum(y)]])
    return mantel_haenszel(tabs)


def main():
    rd = R.Round('Four-hundred-and-sixty-sixth registered predictions: goal loop 112, do long-form texts recur less?', 'predict_test466')
    o1, p1 = run('SEAL:S')
    rd.rec('RL1', 'square seals: formula texts recur less often at equal length', 'odds ratio %.2f, p = %.4f' % (o1, p1), o1 < 1 and p1 < 0.05)
    o2, p2 = run('SEAL')
    rd.rec('RL2', 'all seals: the same', 'odds ratio %.2f, p = %.4f' % (o2, p2), o2 < 1 and p2 < 0.05)
    rd.rec('P', 'progress rule: either holds', 'RL1 %s, RL2 %s' % (o1 < 1 and p1 < 0.05, o2 < 1 and p2 < 0.05), (o1 < 1 and p1 < 0.05) or (o2 < 1 and p2 < 0.05))
    rd.finish()


if __name__ == '__main__':
    main()
