"""Set 409 (goal run loop 55): the cross-section shape (ICIT field 16) of moulded tablets. Split C. Writes results/predict_test409.md."""
import loopkit as L
import rtools as R
from predict_test371 import test


def main():
    sec = L.field(16)
    rd = R.Round('Four-hundred-and-ninth registered predictions: goal loop 55 (part 1), moulded-tablet section shapes', 'predict_test409')
    _, (tr, te) = L.splits_c()
    lab = lambda t: None if L.SUBTYPE.get(t) != 'TAB:B' or t not in sec else ('rect' if sec[t] == 'rectangular' else 'other')
    o1 = test(tr, te, lab, 'rect', 'other', lambda t: True, rd, 'TS1', 'rectangular against other-section moulded tablets')
    rd.finish()
    L.run_domain_set_c(4090, 'Four-hundred-and-ninth registered predictions: goal loop 55 (part 2), section shape as domain', [
        ('TS2', 'a section-shape domain model (field 16)', lambda t, m: sec.get(t, ''))])


if __name__ == '__main__':
    main()
