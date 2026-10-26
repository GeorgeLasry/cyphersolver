"""Set 416 (goal run loop 62): change over the Mohenjo-daro phases (ICIT field 9: Early + Intermediate against Late),
stratified by length band x subtype. Writes results/predict_test416.md."""
import loopkit as L
import rtools as R
from predict_test379 import mantel_haenszel

HEAD = {'817', '820', '861'}


def main():
    rd = R.Round('Four-hundred-and-sixteenth registered predictions: goal loop 62, change over the Mohenjo-daro phases', 'predict_test416')
    ph = L.field(9)
    era = lambda t: {'Early': 'early', 'Intermediate': 'early', 'Late': 'late'}.get(ph.get(t)) if L.META.get(t, ('', '', ''))[0] == 'Mohenjo-daro' else None
    (tr, te), (DA, DB) = L.splits()
    lines = [t for t in sorted(set(tr) | set(te) | set(DA)) if era(t)]
    strat = lambda t: (min(max(len(t), 2), 7), L.SUBTYPE.get(t, ''))
    rd.say('- %d Mohenjo-daro lines with a phase.' % len(lines))

    def mh(feat):
        tabs = []
        for k in sorted({strat(t) for t in lines}):
            lt = [feat(t) for t in lines if strat(t) == k and era(t) == 'late']
            er = [feat(t) for t in lines if strat(t) == k and era(t) == 'early']
            tabs.append([[sum(lt), len(lt) - sum(lt)], [sum(er), len(er) - sum(er)]])
        return mantel_haenszel(tabs)
    o1, p1 = mh(lambda t: any(g in R.END for g in t[-2:]))
    rd.rec('MP1', 'late Mohenjo-daro texts differ in closing with 740/520 (two-sided)', 'odds ratio late/early %.2f, p = %.4f' % (o1, p1), p1 < 0.05)
    o2, p2 = mh(lambda t: t[0] in HEAD)
    rd.rec('MP2', 'the heading frequency changes between the phases (two-sided)', 'odds ratio late/early %.2f, p = %.4f' % (o2, p2), p2 < 0.05)
    rd.rec('P', 'progress rule: either holds', 'MP1 %s, MP2 %s' % (p1 < 0.05, p2 < 0.05), p1 < 0.05 or p2 < 0.05)
    rd.finish()


if __name__ == '__main__':
    main()
