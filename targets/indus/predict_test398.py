"""Set 398 (goal run loop 44): the WORD task with the adopted domain models (length, type, subtype, length x subtype).
Fixed split and split C. Writes results/predict_test398.md."""
import loopkit as L
import rtools as R


def main():
    rd = R.Round('Three-hundred-and-ninety-eighth registered predictions: goal loop 44, WORD with the domain models', 'predict_test398')
    res = []
    for name, (a, b) in (('fixed', L.splits()[0]), ('C', L.splits_c()[1])):
        p1, p10, n = L.word_task(a, b, [])
        d1, d10, _ = L.word_task(a, b, L.BASE_DOMAINS)
        rd.say('- %s (%d names): plain top-1 %.1f%% / top-10 %.1f%%; domains %.1f%% / %.1f%%.' % (name, n, 100 * p1, 100 * p10, 100 * d1, 100 * d10))
        res.append((p1, p10, d1, d10))
    rd.say()
    ok1 = all(r[3] > r[1] for r in res)
    ok2 = all(r[2] > r[0] for r in res)
    rd.rec('WT1', 'WORD top-10 rises on both splits', '; '.join('%.1f%% -> %.1f%%' % (100 * r[1], 100 * r[3]) for r in res), ok1)
    rd.rec('WT2', 'WORD top-1 rises on both splits', '; '.join('%.1f%% -> %.1f%%' % (100 * r[0], 100 * r[2]) for r in res), ok2)
    rd.rec('P', 'progress rule: WT1', 'WT1 %s' % ok1, ok1)
    rd.finish()


if __name__ == '__main__':
    main()
