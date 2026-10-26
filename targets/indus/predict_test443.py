"""Set 443 (goal run loop 89): the closing formula by city and by seal animal (square seals). Writes results/predict_test443.md."""
import rtools as R
from predict_test379 import mantel_haenszel
from predict_test441 import has_formula


def main():
    rd = R.Round('Four-hundred-and-forty-third registered predictions: goal loop 89, the closing formula by city and animal', 'predict_test443')
    A, B, rowsA, recs, F = R.load_all()
    rows = []
    for r in F:
        rec = recs.get(r['sealid'])
        if rec and str(rec[20]).startswith('SEAL:S') and r['flat']:
            rows.append((tuple(r['flat']), r['site'], str(rec[18]).split(':')[0]))
    band = lambda t: min(max(len(t), 2), 7)

    def mh(lab, a, b):
        tabs = []
        for k in sorted({band(t) for t, s, m in rows}):
            x = [has_formula(t) for t, s, m in rows if band(t) == k and lab(s, m) == a]
            y = [has_formula(t) for t, s, m in rows if band(t) == k and lab(s, m) == b]
            tabs.append([[sum(x), len(x) - sum(x)], [sum(y), len(y) - sum(y)]])
        return mantel_haenszel(tabs)
    o1, p1 = mh(lambda s, m: s, 'Mohenjo-daro', 'Harappa')
    rd.rec('FC1', 'the closing formula differs between Mohenjo-daro and Harappa seals (two-sided)', 'odds ratio MD/H %.2f, p = %.4f' % (o1, p1), p1 < 0.05)
    o2, p2 = mh(lambda s, m: None if m in ('', '-', 'None') else ('u' if m == 'Bull1' else 'o'), 'o', 'u')
    rd.rec('FC2', 'the closing formula differs between other-animal and unicorn seals (two-sided)', 'odds ratio other/unicorn %.2f, p = %.4f' % (o2, p2), p2 < 0.05)
    rd.rec('P', 'progress rule: either holds', 'FC1 %s, FC2 %s' % (p1 < 0.05, p2 < 0.05), p1 < 0.05 or p2 < 0.05)
    rd.finish()


if __name__ == '__main__':
    main()
