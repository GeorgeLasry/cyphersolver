"""Set 459 (goal run loop 105): tablet size and text (ICIT field 31). Writes results/predict_test459.md."""
import rtools as R
from predict_test388 import objects
from scipy.stats import mannwhitneyu, spearmanr


def main():
    rd = R.Round('Four-hundred-and-fifty-ninth registered predictions: goal loop 105, tablet size and text', 'predict_test459')
    ti = objects('TAB:I')
    r, p = spearmanr([s for s, t in ti], [len(t) for s, t in ti])
    rd.rec('TZ1', 'longer texts on larger incised tablets', 'rho %.2f over %d tablets, p = %.4f' % (r, len(ti), p), r > 0 and p < 0.05)
    tb = objects('TAB:B')
    a = [s for s, t in tb if '700' in t]
    c = [s for s, t in tb if '700' not in t]
    p2 = mannwhitneyu(a, c).pvalue if a and c else 1
    med = lambda x: sorted(x)[len(x) // 2] if x else 0
    rd.rec('TZ2', 'moulded tablets with 700 differ in size from those without (two-sided)', 'median %.1f (n %d) against %.1f (n %d), p = %.4f' % (med(a), len(a), med(c), len(c), p2), p2 < 0.05)
    rd.rec('P', 'progress rule: either holds', 'TZ1 %s, TZ2 %s' % (r > 0 and p < 0.05, p2 < 0.05), (r > 0 and p < 0.05) or p2 < 0.05)
    rd.finish()


if __name__ == '__main__':
    main()
