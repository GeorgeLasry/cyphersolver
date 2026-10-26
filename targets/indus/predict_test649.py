"""Set 649 (lead 8): restoring an illegible sign from the model, scored against intact duplicates of the same text
(mould copies, sealings, repeated texts), with the model retrained without any copy of the line. Writes results/predict_test649.md."""
from collections import Counter, defaultdict

import icit_full
import rtools as R
from predict_test283 import copy_of, predict
from predict_test285 import ctx_pred
from progress import data
from scipy.stats import binomtest


def cases():
    A, B, rowsA, recs, F = R.load_all()
    clean = defaultdict(list)
    for r in F:
        for ln in r['seq']:
            if ln:
                clean[len(ln)].append(tuple(ln))
    out = []
    for rec in icit_full.records(R.FPATH):
        for ln in icit_full.lines_of(rec[34]):
            s = ln['signs']
            gaps = [i for i, g in enumerate(s) if g is None or g == '?']
            if len(gaps) != 1 or len(s) < 3:
                continue
            k = gaps[0]
            cand = Counter(t[k] for t in clean[len(s)] if all(t[i] == s[i] for i in range(len(s)) if i != k))
            if len(cand) == 1:
                out.append((rec[1] or rec[0], tuple('???' if i == k else g for i, g in enumerate(s)), k, next(iter(cand))))
    return out


def main():
    rd = R.Round('Set 649 registered predictions: restoration scored against intact duplicates', 'predict_test649')
    DL, tr, te = data()
    top = Counter(g for x in DL for g in x).most_common(1)[0][0]
    m1 = m5 = c1 = f1 = n = 0
    seen = set()
    for cid, t, k, gold in cases():
        if (t, k) in seen:
            continue
        seen.add((t, k))
        train = [u for u in DL if not copy_of(t, k, u)]
        cands = [g for g, c in Counter(g for x in train for g in x).most_common(150)]
        pred = predict(train, t, k, cands)
        n += 1
        m1 += pred[0] == gold
        m5 += gold in pred
        c1 += ctx_pred(train, t, k) == gold
        f1 += top == gold
    rd.say('- %d distinct damaged lines with a unanimous intact duplicate.' % n)
    p = binomtest(m1, n, max(c1, 1) / n, alternative='greater').pvalue if n else 1
    rd.rec('RD1', 'the copy-free model restores more signs than the neighbour-rule baseline', 'model top-1 %d, top-5 %d, context baseline %d, frequency %d, of %d; p = %.4f' % (m1, m5, c1, f1, n, p), n >= 10 and m1 > c1 and p < 0.05)
    rd.rec('RD2', 'top-1 right on 30%+', '%.0f%%' % (100 * m1 / max(1, n)), n >= 10 and m1 >= 0.3 * n)
    rd.rec('P', 'progress rule: RD1 and RD2 (restoration line gains a second, duplicate-based check)', '', n >= 10 and m1 > c1 and p < 0.05 and m1 >= 0.3 * n)
    rd.finish()


if __name__ == '__main__':
    main()
