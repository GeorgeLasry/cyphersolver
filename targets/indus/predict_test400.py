"""Set 400 (goal run loop 46): impressions on clay tags (seals in use) against square-seal texts. Writes results/predict_test400.md."""
import rtools as R
from predict_test379 import mantel_haenszel

HEAD = {'817', '820', '861'}


def main():
    rd = R.Round('Four-hundredth registered predictions: goal loop 46, sealings against seals', 'predict_test400')
    A, B, rowsA, recs, F = R.load_all()
    tags, seals = set(), set()
    for r in F:
        rec = recs.get(r['sealid'])
        if not rec:
            continue
        ty = str(rec[20])
        for ln in r['seq']:
            if ln and len(ln) >= 2:
                (tags if ty.startswith('TAG') else seals if ty.startswith('SEAL:S') else set()).add(tuple(ln))
    seals -= tags
    band = lambda t: min(max(len(t), 2), 7)

    def mh(feat):
        tabs = []
        for b in sorted({band(t) for t in tags | seals}):
            a_ = [feat(t) for t in tags if band(t) == b]
            c_ = [feat(t) for t in seals if band(t) == b]
            tabs.append([[sum(a_), len(a_) - sum(a_)], [sum(c_), len(c_) - sum(c_)]])
        return mantel_haenszel(tabs)
    rd.say('- %d distinct tag lines, %d square-seal lines.' % (len(tags), len(seals)))
    o1, p1 = mh(lambda t: t[0] in HEAD)
    rd.rec('TG1', 'tag texts open with the heading more often at equal length', 'odds ratio %.2f, p = %.4f' % (o1, p1), o1 > 1 and p1 < 0.05)
    o2, p2 = mh(lambda t: any(g in R.END for g in t[-2:]))
    rd.rec('TG2', 'tag texts close with 740/520 less often at equal length', 'odds ratio %.2f, p = %.4f' % (o2, p2), o2 < 1 and p2 < 0.05)
    rd.rec('P', 'progress rule: either holds', 'TG1 %s, TG2 %s' % (o1 > 1 and p1 < 0.05, o2 < 1 and p2 < 0.05), (o1 > 1 and p1 < 0.05) or (o2 < 1 and p2 < 0.05))
    rd.finish()


if __name__ == '__main__':
    main()
