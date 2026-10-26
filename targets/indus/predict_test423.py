"""Set 423 (goal run loop 69): do small-seal names and texts recur on tablets? Writes results/predict_test423.md."""
from statistics import median

import rtools as R
from predict_test379 import mantel_haenszel
from predict_test388 import objects
from predict_test390 import body


def main():
    rd = R.Round('Four-hundred-and-twenty-third registered predictions: goal loop 69, small-seal names on tablets', 'predict_test423')
    A, B, rowsA, recs, F = R.load_all()
    tab_bodies, tab_texts = set(), set()
    for r in F:
        rec = recs.get(r['sealid'])
        if rec and str(rec[20]).startswith('TAB'):
            for ln in r['seq']:
                if ln:
                    tab_texts.add(tuple(ln))
                    b = body(tuple(ln))
                    if b:
                        tab_bodies.add(b)
    sq = objects('SEAL:S')
    cut = median(s for s, t in sq)
    band = lambda t: min(max(len(t), 2), 7)

    def mh(feat):
        tabs = []
        for b in sorted({band(t) for s, t in sq}):
            sm = [feat(t) for s, t in sq if band(t) == b and s <= cut]
            lg = [feat(t) for s, t in sq if band(t) == b and s > cut]
            tabs.append([[sum(sm), len(sm) - sum(sm)], [sum(lg), len(lg) - sum(lg)]])
        return mantel_haenszel(tabs)
    o1, p1 = mh(lambda t: body(t) is not None and body(t) in tab_bodies)
    rd.rec('ST1', 'small-seal name bodies recur on tablets more often at equal length', 'odds ratio small/large %.2f, p = %.4f' % (o1, p1), o1 > 1 and p1 < 0.05)
    o2, p2 = mh(lambda t: any(tuple(t[i:i + len(x)]) == x for x in () ) or t in tab_texts)
    rd.rec('ST2', 'small-seal whole texts recur on tablets more often at equal length', 'odds ratio small/large %.2f, p = %.4f' % (o2, p2), o2 > 1 and p2 < 0.05)
    rd.rec('P', 'progress rule: either holds', 'ST1 %s, ST2 %s' % (o1 > 1 and p1 < 0.05, o2 > 1 and p2 < 0.05), (o1 > 1 and p1 < 0.05) or (o2 > 1 and p2 < 0.05))
    rd.finish()


if __name__ == '__main__':
    main()
