"""Set 657 (lead 8): do the graffiti signs that most often enter composite marks correspond to the Indus signs that most
often serve as hosts of ligatures / marked variants? Graffiti composite share per base sign (tngraffiti.in concordance);
Indus host score = number of derived signs per base in Parpola's descriptions (devices.pairs) and the token share of
those variants; mapped through the corpus's own Indus parallels. Writes results/predict_test657.md."""
import csv
import glob
import json
import random
from collections import Counter, defaultdict

import rtools as R
from devices import pairs
from leadkit import objects
from scipy.stats import spearmanr


def graffiti_share():
    recs = {}
    for f in glob.glob('data/graffiti/raw/conc_*.json'):
        for r in json.load(open(f, encoding='utf-8')).get('unique_response', []):
            recs[r['_id']] = r
    base = {r['s1']: str(r['base']) for r in recs.values() if 's2' not in r and r['type'] in ('Base', 'Variant')}
    part, solo = Counter(), Counter()
    for r in recs.values():
        if 's2' in r:
            for k in range(1, 7):
                b = base.get(r.get('s%d' % k))
                if b:
                    part[b] += r['occurrence_count']
        elif r['type'] == 'Base':
            solo[str(r['base'])] += r['occurrence_count']
    return {b: part[b] / (part[b] + solo[b]) for b in set(part) | set(solo) if part[b] + solo[b] >= 10}


def indus_host():
    derived = defaultdict(set)
    for p in pairs():
        for gb in p['gb']:
            derived[gb] |= p['gm']
    occ = Counter(g for s, ty, mo, size, lines, rec in objects() for t in lines for g in t)
    score = {}
    for g in occ:
        d = derived.get(g, set())
        tok = sum(occ[x] for x in d)
        score[g] = (len(d), tok / (tok + occ[g]) if tok + occ[g] else 0)
    return score


def main():
    rd = R.Round('Set 657 registered predictions: graffiti composite hosts against Indus ligature hosts', 'predict_test657')
    rnd = random.Random(657)
    gs = graffiti_share()
    hs = indus_host()
    m = {}
    for r in csv.DictReader((l for l in open('data/graffiti/graffiti_indus_map.tsv', encoding='utf-8') if not l.startswith('#')), delimiter='\t'):
        if '.' not in r['tnsda'] and r['icit']:
            m[r['tnsda']] = r['icit'].split('/')
    xs, ys, yt, names = [], [], [], []
    for b, icits in m.items():
        if b in gs:
            xs.append(gs[b])
            ys.append(max(hs.get(g, (0, 0))[0] for g in icits))
            yt.append(max(hs.get(g, (0, 0))[1] for g in icits))
            names.append('%s->%s' % (b, '/'.join(icits)))
    rd.say('- %d mapped base signs with 10+ graffiti occurrences; pairs: %s.' % (len(xs), '; '.join('%s g%.2f d%d t%.2f' % (n, x, y, z) for n, x, y, z in zip(names, xs, ys, yt))))
    rd.say()
    for key, y, lab in (('GH1', ys, 'number of derived Indus signs'), ('GH2', yt, 'token share of the derived signs')):
        rho = spearmanr(xs, y).correlation if len(xs) >= 5 else 0
        ge = 0
        yy = list(y)
        for _ in range(1000):
            rnd.shuffle(yy)
            ge += spearmanr(xs, yy).correlation >= rho
        p = (ge + 1) / 1001
        rd.rec(key, 'graffiti composite share correlates with the %s of the Indus parallel' % lab, 'Spearman rho %.3f over %d signs, permutation p = %.4f' % (rho, len(xs), p), len(xs) >= 5 and p < 0.05)
    rd.rec('P', 'progress rule: none (a comparison of composition habits; the corpus\'s parallels are shape matches)', '', False)
    rd.finish()


if __name__ == '__main__':
    main()
