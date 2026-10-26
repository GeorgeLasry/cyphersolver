"""Set 455 (goal run loop 101): negative control: seal condition (ICIT field 17) cannot shape the text.
Writes results/predict_test455.md and predict_test4550.md."""
import loopkit as L
import rtools as R
from predict_test371 import test


def main():
    cond = L.field(17)
    lab = lambda t: None if L.SUBTYPE.get(t) != 'SEAL:S' or t not in cond else ('complete' if cond[t] == 'complete' else 'damaged')
    rd = R.Round('Four-hundred-and-fifty-fifth registered predictions: goal loop 101 (part 1), negative control: seal condition', 'predict_test455')
    _, (tr, te) = L.splits_c()
    found = test(tr, te, lab, 'complete', 'damaged', lambda t: True, rd, 'NC1', 'complete against damaged square seals (expected: no replicated skew)')
    rd.finish()
    held = L.run_domain_set_c(4550, 'Four-hundred-and-fifty-fifth registered predictions: goal loop 101 (part 2), condition as domain', [
        ('NC2', 'a condition domain model (expected: no gain)', lambda t, m: cond.get(t, ''))])
    print('control passes' if not found and not any(held) else 'control FAILS')


if __name__ == '__main__':
    main()
