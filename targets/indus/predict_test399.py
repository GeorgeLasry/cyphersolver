"""Set 399 (goal run loop 45): WORD with a city prior from the local-names finding (sets 390-391). Writes results/predict_test399.md."""
import loopkit as L
import rtools as R


def main():
    rd = R.Round('Three-hundred-and-ninety-ninth registered predictions: goal loop 45, WORD with a city prior', 'predict_test399')
    res = []
    for name, (a, b) in zip(('fixed', 'A -> B'), L.splits()):
        out, n = L.word_task_local(a, b, L.BASE_DOMAINS)
        rd.say('- %s (%d names): without prior top-1 %.1f%% / top-10 %.1f%%; with city prior %.1f%% / %.1f%%.' % (
            name, n, 100 * out[0][0] / n, 100 * out[0][1] / n, 100 * out[1][0] / n, 100 * out[1][1] / n))
        res.append(out)
    rd.say()
    ok1 = all(o[1][1] > o[0][1] for o in res)
    ok2 = all(o[1][0] > o[0][0] for o in res)
    rd.rec('WL1', 'the city prior raises WORD top-10 on both splits', ', '.join('%d -> %d' % (o[0][1], o[1][1]) for o in res), ok1)
    rd.rec('WL2', 'the city prior raises WORD top-1 on both splits', ', '.join('%d -> %d' % (o[0][0], o[1][0]) for o in res), ok2)
    rd.rec('P', 'progress rule: WL1', 'WL1 %s' % ok1, ok1)
    rd.finish()


if __name__ == '__main__':
    main()
