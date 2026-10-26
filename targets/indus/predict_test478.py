"""Set 478 (goal run loop 124): the closing formula and doubled signs by seal thickness (ICIT field 33; sizekit with
kind=33). Writes results/predict_test478.md."""
import rtools as R
import sizekit
from predict_test441 import has_formula


def main():
    rd = R.Round('Four-hundred-and-seventy-eighth registered predictions: goal loop 124, formula and doubles by thickness', 'predict_test478')
    sizekit._SQ = None
    o1, p1 = sizekit.size_test(has_formula, kind=33)
    rd.rec('TH1', 'thick seals carry the closing formula more often', 'odds ratio thick/thin %.2f, p = %.4f' % (o1, p1), o1 > 1 and p1 < 0.05)
    o2, p2 = sizekit.size_test(lambda t: any(t[i] == t[i + 1] and t[i] not in R.NUMS for i in range(len(t) - 1)), kind=33)
    rd.rec('TH2', 'thin seals carry doubled signs more often', 'odds ratio thick/thin %.2f, p = %.4f' % (o2, p2), o2 < 1 and p2 < 0.05)
    rd.rec('P', 'progress rule: none (a second dimension for findings already made; consistency)', 'TH1 %s, TH2 %s' % (o1 > 1 and p1 < 0.05, o2 < 1 and p2 < 0.05), False)
    rd.finish()


if __name__ == '__main__':
    main()
