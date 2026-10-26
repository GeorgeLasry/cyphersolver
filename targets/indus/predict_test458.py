"""Set 458 (goal run loop 104): false-positive rate of the skew test and of the ending test under random labels.
Writes results/predict_test458.md."""
import hashlib
import io
import contextlib

import loopkit as L
import rtools as R
from predict_test371 import test
from predict_test379 import mantel_haenszel


def main():
    rd = R.Round('Four-hundred-and-fifty-eighth registered predictions: goal loop 104, false-positive rate under random labels', 'predict_test458')
    _, (tr, te) = L.splits_c()
    sq = lambda t: L.SUBTYPE.get(t) == 'SEAL:S'
    fp1 = fp2 = 0
    band = lambda t: min(max(len(t), 2), 7)
    lines = [t for t in sorted(set(tr) | set(te)) if sq(t)]
    for k in range(20):
        lab = lambda t, k=k: 'a' if int(hashlib.md5(('%d' % k + ' '.join(t)).encode()).hexdigest(), 16) % 2 else 'b'
        dummy = R.Round('x', 'x')
        with contextlib.redirect_stdout(io.StringIO()):
            fp1 += test(tr, te, lab, 'a', 'b', sq, dummy, 'x', 'x')
        tabs = []
        for b in sorted({band(t) for t in lines}):
            x = [any(g in R.END for g in t[-2:]) for t in lines if band(t) == b and lab(t) == 'a']
            y = [any(g in R.END for g in t[-2:]) for t in lines if band(t) == b and lab(t) == 'b']
            tabs.append([[sum(x), len(x) - sum(x)], [sum(y), len(y) - sum(y)]])
        fp2 += mantel_haenszel(tabs)[1] < 0.05
    rd.rec('FP1', 'the skew test reports a replicated skew in at most 1 of 20 random labellings', '%d of 20' % fp1, fp1 <= 1)
    rd.rec('FP2', 'the Mantel-Haenszel ending test is significant in at most 2 of 20 random labellings', '%d of 20' % fp2, fp2 <= 2)
    rd.rec('P', 'progress rule: none (calibration)', 'FP1 %s, FP2 %s' % (fp1 <= 1, fp2 <= 2), False)
    rd.finish()


if __name__ == '__main__':
    main()
