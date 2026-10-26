"""Set 456 (goal run loop 102): negative control: odd against even ICIT record numbers. Writes results/predict_test456.md
and predict_test4560.md."""
import loopkit as L
import rtools as R
from predict_test371 import test


def main():
    A, B, rowsA, recs, F = R.load_all()
    par = {}
    for r in F:
        n = str(r['sealid']).split('.')[0]
        if n.isdigit():
            for ln in r['seq']:
                if ln:
                    par.setdefault(tuple(ln), 'odd' if int(n) % 2 else 'even')
    rd = R.Round('Four-hundred-and-fifty-sixth registered predictions: goal loop 102 (part 1), negative control: record parity', 'predict_test456')
    _, (tr, te) = L.splits_c()
    found = test(tr, te, lambda t: par.get(t), 'odd', 'even', lambda t: True, rd, 'NP1', 'odd against even record numbers (expected: no replicated skew)')
    rd.finish()
    held = L.run_domain_set_c(4560, 'Four-hundred-and-fifty-sixth registered predictions: goal loop 102 (part 2), parity as domain', [
        ('NP2', 'a parity domain model (expected: no gain)', lambda t, m: par.get(t, ''))])
    print('control passes' if not found and not any(held) else 'control FAILS')


if __name__ == '__main__':
    main()
