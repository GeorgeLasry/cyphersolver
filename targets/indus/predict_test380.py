"""Set 380 (goal run loop 26): seal size, the heading formula and repeated texts (square seals, clean ICIT objects).
Writes results/predict_test380.md."""
from collections import Counter
from statistics import median

import rtools as R
from predict_test379 import mantel_haenszel
from scipy.stats import fisher_exact

HEAD = {'817', '820', '861'}


def main():
    rd = R.Round('Three-hundred-and-eightieth registered predictions: goal loop 26, seal size, heading and repeated texts', 'predict_test380')
    A, B, rowsA, recs, F = R.load_all()
    objs = []
    for r in F:
        rec = recs.get(r['sealid'])
        if not rec or not str(rec[20]).startswith('SEAL:S'):
            continue
        try:
            sz = float(rec[31])
        except (TypeError, ValueError):
            continue
        if sz > 0 and r['flat']:
            objs.append((sz, tuple(r['flat'])))
    cut = median(s for s, t in objs)
    band = lambda t: min(max(len(t), 2), 7)
    tabs = []
    for b in sorted({band(t) for s, t in objs}):
        lg = [t for s, t in objs if band(t) == b and s > cut]
        sm = [t for s, t in objs if band(t) == b and s <= cut]
        a, c = sum(t[0] in HEAD for t in lg), sum(t[0] in HEAD for t in sm)
        tabs.append([[a, len(lg) - a], [c, len(sm) - c]])
    orr, p = mantel_haenszel(tabs)
    rd.say('- %d square seals with a size (median %.1f).' % (len(objs), cut))
    rd.rec('HS1', 'the heading opens large seals more often, within length bands', 'odds ratio large/small %.2f, p = %.4f' % (orr, p), orr > 1 and p < 0.05)
    cnt = Counter(t for s, t in objs)
    lg = [cnt[t] > 1 for s, t in objs if s > cut]
    sm = [cnt[t] > 1 for s, t in objs if s <= cut]
    o2, p2 = fisher_exact([[sum(sm), len(sm) - sum(sm)], [sum(lg), len(lg) - sum(lg)]], alternative='greater')
    rd.rec('HS2', 'small-seal texts recur on other seals more often', 'small %d of %d, large %d of %d, p = %.4f' % (sum(sm), len(sm), sum(lg), len(lg), p2), p2 < 0.05)
    rd.rec('P', 'progress rule: either holds (a new finding; control by length for HS1)', 'HS1 %s, HS2 %s' % (orr > 1 and p < 0.05, p2 < 0.05), (orr > 1 and p < 0.05) or p2 < 0.05)
    rd.finish()


if __name__ == '__main__':
    main()
