"""Set 412 (goal run loop 58): SIGN with the current base (length, type, subtype, length x subtype). Fixed split and C.
Writes results/predict_test412.md."""
import loopkit as L
import rtools as R


def main():
    rd = R.Round('Four-hundred-and-twelfth registered predictions: goal loop 58, SIGN with the object-kind models', 'predict_test412')
    res = []
    for name, (a, b) in (('fixed', L.splits()[0]), ('C', L.splits_c()[1])):
        p1, p5, n = L.sign_task(a, b, [])
        d1, d5, _ = L.sign_task(a, b, L.BASE_DOMAINS)
        rd.say('- %s (%d signs): plain %.1f%% / %.1f%%, object-kind models %.1f%% / %.1f%%.' % (name, n, 100 * p1, 100 * p5, 100 * d1, 100 * d5))
        res.append((p1, p5, d1, d5))
    rd.say()
    ok1 = all(r[2] > r[0] for r in res)
    ok5 = all(r[3] > r[1] for r in res)
    rd.rec('SK1', 'SIGN top-1 rises on both splits', '; '.join('%.1f%% -> %.1f%%' % (100 * r[0], 100 * r[2]) for r in res), ok1)
    rd.rec('SK2', 'SIGN top-5 rises on both splits', '; '.join('%.1f%% -> %.1f%%' % (100 * r[1], 100 * r[3]) for r in res), ok5)
    rd.rec('P', 'progress rule: SK1', 'SK1 %s' % ok1, ok1)
    rd.finish()


if __name__ == '__main__':
    main()
