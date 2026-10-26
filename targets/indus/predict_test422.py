"""Set 422 (goal run loop 68): WORD with an object-subtype prior (as set 399's city prior). Fixed split and C.
Writes results/predict_test422.md."""
import loopkit as L
import rtools as R


def main():
    rd = R.Round('Four-hundred-and-twenty-second registered predictions: goal loop 68, WORD with a subtype prior', 'predict_test422')
    res = []
    for name, (a, b) in (('fixed', L.splits()[0]), ('C', L.splits_c()[1])):
        out, n = L.word_task_local(a, b, L.BASE_DOMAINS, keyfn=lambda t: L.SUBTYPE.get(t, ''))
        rd.say('- %s (%d names): without prior %d / %d; with subtype prior %d / %d (top-1 / top-10).' % (name, n, out[0][0], out[0][1], out[1][0], out[1][1]))
        res.append(out)
    rd.say()
    ok1 = all(o[1][1] > o[0][1] for o in res)
    ok2 = all(o[1][0] > o[0][0] for o in res)
    rd.rec('WK1', 'the subtype prior raises WORD top-10 on both splits', ', '.join('%d -> %d' % (o[0][1], o[1][1]) for o in res), ok1)
    rd.rec('WK2', 'the subtype prior raises WORD top-1 on both splits', ', '.join('%d -> %d' % (o[0][0], o[1][0]) for o in res), ok2)
    rd.rec('P', 'progress rule: WK1', 'WK1 %s' % ok1, ok1)
    rd.finish()


if __name__ == '__main__':
    main()
