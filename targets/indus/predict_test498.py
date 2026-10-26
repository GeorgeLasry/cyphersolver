"""Set 498 (goal run loop 144): audits of sets 469 (doubled signs) and 380 (repeated texts) with motif strata.
Writes results/predict_test498.md."""
from collections import Counter

import auditkit
import rtools as R


def main():
    rd = R.Round('Four-hundred-and-ninety-eighth registered predictions: goal loop 144, audits of doubles and repeats against the animal', 'predict_test498')
    o1, p1 = auditkit.size_motif(lambda t: any(t[i] == t[i + 1] and t[i] not in R.NUMS for i in range(len(t) - 1)))
    rd.rec('DA1', 'doubled signs lean to small seals with motif held', 'odds ratio large/small %.2f, p = %.4f' % (o1, p1), o1 < 1 and p1 < 0.05)
    cnt = Counter(t for t, u, x, s in auditkit.rows())
    o2, p2 = auditkit.size_motif(lambda t: cnt[t] > 1)
    rd.rec('DA2', 'repeated texts lean to small seals with motif held', 'odds ratio large/small %.2f, p = %.4f' % (o2, p2), o2 < 1 and p2 < 0.05)
    rd.rec('P', 'progress rule: none (audits of sets 469 and 380)', '', False)
    rd.finish()


if __name__ == '__main__':
    main()
