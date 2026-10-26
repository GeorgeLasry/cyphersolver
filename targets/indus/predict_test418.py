"""Set 418 (goal run loop 64): Mohenjo-daro excavation areas (ICIT field 4, two-letter code). Writes results/predict_test418.md."""
import re

import loopkit as L
import rtools as R
from predict_test371 import test


def main():
    f4 = L.field(4)
    area = {t: re.match(r'[A-Z]{2}', v).group(0) for t, v in f4.items() if re.match(r'[A-Z]{2}', v) and L.META.get(t, ('', '', ''))[0] == 'Mohenjo-daro'}
    rd = R.Round('Four-hundred-and-eighteenth registered predictions: goal loop 64 (part 1), Mohenjo-daro areas', 'predict_test418')
    _, (tr, te) = L.splits_c()
    o1 = test(tr, te, lambda t: area.get(t), 'DK', 'HR', lambda t: True, rd, 'AR1', 'DK against HR area')
    rd.finish()
    L.run_domain_set_c(4180, 'Four-hundred-and-eighteenth registered predictions: goal loop 64 (part 2), area as domain', [
        ('AR2', 'a Mohenjo-daro area domain model', lambda t, m: area.get(t, ''))])


if __name__ == '__main__':
    main()
