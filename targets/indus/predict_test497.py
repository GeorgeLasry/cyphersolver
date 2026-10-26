"""Set 497 (goal run loop 143): audit of set 441 (the formula on large seals) with motif strata. Writes results/predict_test497.md."""
import rtools as R
from auditkit import size_motif
from predict_test441 import has_formula


def main():
    rd = R.Round('Four-hundred-and-ninety-seventh registered predictions: goal loop 143, audit of the formula against the animal', 'predict_test497')
    o1, p1 = size_motif(has_formula)
    rd.rec('FM1', 'the formula leans to large seals with length x site x motif strata', 'odds ratio %.2f, p = %.4f' % (o1, p1), o1 > 1 and p1 < 0.05)
    o2, p2 = size_motif(has_formula, unicorn_only=True)
    rd.rec('FM2', 'the same within unicorn seals', 'odds ratio %.2f, p = %.4f' % (o2, p2), o2 > 1 and p2 < 0.05)
    rd.rec('P', 'progress rule: none (audit of set 441)', '', False)
    rd.finish()


if __name__ == '__main__':
    main()
