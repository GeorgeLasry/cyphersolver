"""Set 363 (goal run loop 9): the SIGN task with the region and length domain models. loopkit.py."""
import loopkit as L
import rtools as R


def main():
    rd = R.Round('Three-hundred-and-sixty-third registered predictions: goal loop 9, SIGN with the domain models', 'predict_test363')
    res = []
    for name, (a, b) in zip(('fixed test', 'A -> B'), L.splits()):
        p1, p5, n = L.sign_task(a, b, [])
        d1, d5, _ = L.sign_task(a, b, L.BASE_DOMAINS)
        rd.say('- %s (%d signs): plain %.1f%% / %.1f%%, domains %.1f%% / %.1f%%.' % (name, n, 100 * p1, 100 * p5, 100 * d1, 100 * d5))
        res.append((p1, p5, d1, d5))
    rd.say()
    ok1 = all(d1 > p1 for p1, p5, d1, d5 in res)
    ok5 = all(d5 > p5 for p1, p5, d1, d5 in res)
    rd.rec('SG1', 'top-1 rises on both splits', '; '.join('%.1f%% -> %.1f%%' % (100 * r[0], 100 * r[2]) for r in res), ok1)
    rd.rec('SG2', 'top-5 rises on both splits', '; '.join('%.1f%% -> %.1f%%' % (100 * r[1], 100 * r[3]) for r in res), ok5)
    rd.rec('P', 'progress rule: SG1', 'SG1 %s' % ok1, ok1)
    rd.finish()


if __name__ == '__main__':
    main()
