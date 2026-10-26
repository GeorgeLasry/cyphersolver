"""Set 488 (goal run loop 134): rare and common signs by seal size (sizekit). Writes results/predict_test488.md."""
from collections import Counter

import rtools as R
import sizekit


def main():
    rd = R.Round('Four-hundred-and-eighty-eighth registered predictions: goal loop 134, rare and common signs by seal size', 'predict_test488')
    A, B, rowsA, recs, F = R.load_all()
    cnt = Counter(g for r in F for g in r['flat'])
    top = {g for g, n in cnt.most_common(50)}
    sizekit._SQ = None
    o1, p1 = sizekit.size_test(lambda t: any(cnt[g] <= 2 for g in t))
    rd.rec('RC1', 'large and small seals differ in carrying a sign seen at most twice in the corpus (two-sided)', 'odds ratio %.2f, p = %.4f' % (o1, p1), p1 < 0.05)
    o2, p2 = sizekit.size_test(lambda t: all(g in top for g in t))
    rd.rec('RC2', 'they differ in texts made only of the 50 commonest signs (two-sided)', 'odds ratio %.2f, p = %.4f' % (o2, p2), p2 < 0.05)
    rd.rec('P', 'progress rule: either holds', 'RC1 %s, RC2 %s' % (p1 < 0.05, p2 < 0.05), p1 < 0.05 or p2 < 0.05)
    rd.finish()


if __name__ == '__main__':
    main()
