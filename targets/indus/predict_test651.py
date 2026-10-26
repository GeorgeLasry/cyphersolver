"""Set 651 (lead 10): Wells 2015's initial-cluster analysis against the scribes' line breaks. An Initial Cluster Terminal
Marker (ICTM: signs 1, 2, 60) closes the opening cluster (pp. 26-29); if so, line breaks on multi-line seals should fall
right after an ICTM and not inside the cluster. Also his claim that 60 never stands beyond the 4th position (Fig. 3.7).
Writes results/predict_test651.md."""
import icit_full
import rtools as R
from leadkit import ab
from scipy.stats import fisher_exact
from signs import load

ICTM = {'1', '2', '60'}


def multiline():
    R.load_all()
    icit = [r['seq'] for r in icit_full.objects(R.FPATH, intact_only=True) if len(r['seq']) >= 2 and r['type'].startswith('SEAL') and all(r['seq'])]
    m77 = [r['seq'] for r in load(only_m77=True) if len([ln for ln in r['seq'] if ln]) >= 2]
    return icit, [[ln for ln in s if ln] for s in m77]


def gaps(texts, reverse):
    rows = []
    for seq in texts:
        lines = list(reversed(seq)) if reverse else seq
        flat = [g for ln in lines for g in ln]
        ends = set()
        k = 0
        for ln in lines[:-1]:
            k += len(ln)
            ends.add(k - 1)
        for i in range(len(flat) - 1):
            after = flat[i] in ICTM and 1 <= i <= 3
            inside = flat[i + 1] in ICTM and 1 <= i + 1 <= 3
            rows.append((i in ends, after, inside))
    return rows


def test(rows, key, rd, label, which):
    a = [b for b, af, ins in rows if (af if which == 'after' else ins)]
    o = [b for b, af, ins in rows if not (af if which == 'after' else ins)]
    alt = 'greater' if which == 'after' else 'less'
    p = fisher_exact([[sum(a), len(a) - sum(a)], [sum(o), len(o) - sum(o)]], alternative=alt)[1]
    rd.say('- %s: %s-ICTM gaps break %d of %d, other gaps %d of %d, p = %.4g' % (label, which, sum(a), len(a), sum(o), len(o), p))
    return p < 0.05


def main():
    rd = R.Round("Set 651 registered predictions: Wells's initial clusters against the line breaks", 'predict_test651')
    icit, m77 = multiline()
    rd.say('- %d intact multi-line ICIT seals, %d multi-line M77 texts.' % (len(icit), len(m77)))
    res = {}
    for which in ('after', 'inside'):
        oks = []
        for label, texts in (('ICIT', icit), ('M77', m77)):
            for rev in (False, True):
                oks.append(test(gaps(texts, rev), None, rd, '%s %s' % (label, 'reversed' if rev else 'as listed'), which))
        res[which] = all(oks)
    rd.rec('WS1', 'a line break falls right after an ICTM (1, 2, 60 in positions 2-4) more often than at other gaps, ICIT and M77, both line orders', '', res['after'])
    rd.rec('WS2', 'a line break falls inside the initial cluster (right before the ICTM) less often than at other gaps, same four tests', '', res['inside'])
    DA, DB = ab()
    out = []
    for name, L in (('A', DA), ('B', DB)):
        toks = [i for t in L for i, g in enumerate(t) if g == '60']
        out.append((name, sum(i <= 3 for i in toks), len(toks)))
    ok3 = all(n and k / n >= 0.95 for name, k, n in out)
    rd.rec('WS3', '60 stands within the first four positions in 95%+ of its tokens, A and B', '; '.join('%s %d of %d' % o for o in out), ok3)
    rd.rec('P', 'progress rule: none (a published analysis checked; WS1 + WS2 would be consistency with the heading unit of sets 230-279)', '', False)
    rd.finish()


if __name__ == '__main__':
    main()
