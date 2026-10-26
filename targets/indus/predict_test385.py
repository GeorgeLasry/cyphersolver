"""Set 385 (goal run loop 31): change over the Harappa periods (ICIT field 8), stratified by length band x subtype.
Writes results/predict_test385.md."""
import loopkit as L
import rtools as R
from predict_test379 import mantel_haenszel

HEAD = {'817', '820', '861'}


def era(v):
    if v in ('Period 2', 'Period 2B', 'Period 3A', 'Period 3B', 'Period 3B-1', 'Period 3B-2', 'Period 1', 'Period 1B'):
        return 'early'
    if v.startswith('Period 3C') or v.startswith('Period 4') or v.startswith('Period 5'):
        return 'late'
    return None


def main():
    rd = R.Round('Three-hundred-and-eighty-fifth registered predictions: goal loop 31, change over the Harappa periods', 'predict_test385')
    per = L.field(8)
    (tr, te), (DA, DB) = L.splits()
    lines = [t for t in sorted(set(tr) | set(te) | set(DA)) if era(per.get(t, '')) and t in per]
    strat = lambda t: (min(max(len(t), 2), 7), L.SUBTYPE.get(t, ''))
    rd.say('- %d lines with an early (to 3B) or late (3C, 4, 5) period.' % len(lines))

    def mh(feat):
        tabs = []
        for k in sorted({strat(t) for t in lines}):
            lt = [feat(t) for t in lines if strat(t) == k and era(per[t]) == 'late']
            er = [feat(t) for t in lines if strat(t) == k and era(per[t]) == 'early']
            tabs.append([[sum(lt), len(lt) - sum(lt)], [sum(er), len(er) - sum(er)]])
        return mantel_haenszel(tabs)
    o1, p1 = mh(lambda t: any(g in R.END for g in t[-2:]))
    rd.rec('PE1', 'late texts close with 740/520 less often (length x subtype held)', 'odds ratio late/early %.2f, p = %.4f' % (o1, p1), o1 < 1 and p1 < 0.05)
    o2, p2 = mh(lambda t: t[0] in HEAD)
    rd.rec('PE2', 'the heading frequency changes between early and late (either way)', 'odds ratio late/early %.2f, p = %.4f' % (o2, p2), p2 < 0.05)
    rd.rec('P', 'progress rule: either holds', 'PE1 %s, PE2 %s' % (o1 < 1 and p1 < 0.05, p2 < 0.05), (o1 < 1 and p1 < 0.05) or p2 < 0.05)
    rd.finish()


if __name__ == '__main__':
    main()
