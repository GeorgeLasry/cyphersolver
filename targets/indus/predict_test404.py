"""Set 404 (goal run loop 50): heading and endings on unicorn against other-animal square seals (field 18).
Writes results/predict_test404.md."""
import rtools as R
from predict_test379 import mantel_haenszel

HEAD = {'817', '820', '861'}


def main():
    rd = R.Round('Four-hundred-and-fourth registered predictions: goal loop 50, formula by seal animal', 'predict_test404')
    A, B, rowsA, recs, F = R.load_all()
    uni, oth = set(), set()
    for r in F:
        rec = recs.get(r['sealid'])
        if not rec or not str(rec[20]).startswith('SEAL:S'):
            continue
        m = str(rec[18]).split(':')[0]
        if m in ('', '-', 'None'):
            continue
        for ln in r['seq']:
            if ln and len(ln) >= 2:
                (uni if m == 'Bull1' else oth).add(tuple(ln))
    uni -= oth
    band = lambda t: min(max(len(t), 2), 7)

    def mh(feat):
        tabs = []
        for b in sorted({band(t) for t in uni | oth}):
            a_ = [feat(t) for t in oth if band(t) == b]
            c_ = [feat(t) for t in uni if band(t) == b]
            tabs.append([[sum(a_), len(a_) - sum(a_)], [sum(c_), len(c_) - sum(c_)]])
        return mantel_haenszel(tabs)
    rd.say('- %d other-animal lines, %d unicorn lines.' % (len(oth), len(uni)))
    o1, p1 = mh(lambda t: t[0] in HEAD)
    rd.rec('AN1', 'other-animal seals open with the heading more often at equal length', 'odds ratio %.2f, p = %.4f' % (o1, p1), o1 > 1 and p1 < 0.05)
    o2, p2 = mh(lambda t: any(g in R.END for g in t[-2:]))
    rd.rec('AN2', 'other-animal and unicorn seals differ in closing with 740/520 (two-sided)', 'odds ratio %.2f, p = %.4f' % (o2, p2), p2 < 0.05)
    rd.rec('P', 'progress rule: either holds', 'AN1 %s, AN2 %s' % (o1 > 1 and p1 < 0.05, p2 < 0.05), (o1 > 1 and p1 < 0.05) or p2 < 0.05)
    rd.finish()


if __name__ == '__main__':
    main()
