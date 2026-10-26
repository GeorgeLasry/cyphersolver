"""Set 637: graffiti chronology within sites (tngraffiti.in filter by site: sign x depth counts). Writes results/predict_test637.md."""
import csv
import glob
import json
import os

import rtools as R
from scipy.stats import binomtest, mannwhitneyu


def parallels():
    out = set()
    for r in csv.DictReader((l for l in open('data/graffiti/graffiti_indus_map.tsv', encoding='utf-8') if not l.startswith('#')), delimiter='\t'):
        if '.' not in r['tnsda'] and r['m77']:
            out.add(r['tnsda'])
    return out


def sites(minn=100):
    out = {}
    for f in glob.glob('data/graffiti/raw/bysite/*.json'):
        recs = []
        for r in json.load(open(f, encoding='utf-8')).get('data', []):
            for x in r['result'].get('depth', []):
                try:
                    dep = float(x['key'])
                except ValueError:
                    continue
                recs += [(str(r['sign']).strip(), dep)] * x['value']
        if len(recs) >= minn:
            out[os.path.basename(f)[:-5]] = recs
    return out


def pct(recs):
    ds = sorted(d for s, d in recs)
    n = len(ds)
    import bisect
    return [(s, (bisect.bisect_left(ds, d) + bisect.bisect_right(ds, d)) / (2 * n)) for s, d in recs]


def main():
    rd = R.Round('Set 637 registered predictions: graffiti chronology within sites', 'predict_test637')
    P = parallels()
    S = sites()
    base = lambda s: s.replace('C', '').split('.')[0]
    a_all, b_all, c_all, d_all, dirs, dirs2 = [], [], [], [], [], []
    for site, recs in sorted(S.items()):
        pr = pct(recs)
        a = [p for s, p in pr if base(s) in P]
        b = [p for s, p in pr if base(s) not in P]
        c = [p for s, p in pr if 'C' in s]
        d = [p for s, p in pr if 'C' not in s]
        a_all += a; b_all += b; c_all += c; d_all += d
        if a and b:
            dirs.append(sum(a) / len(a) > sum(b) / len(b))
        if c and d:
            dirs2.append(sum(c) / len(c) < sum(d) / len(d))
        rd.say('- %s: %d graffiti; parallel %d (mean depth rank %.2f) vs none %d (%.2f); composites %d (%.2f).' % (
            site, len(recs), len(a), sum(a) / max(1, len(a)), len(b), sum(b) / max(1, len(b)), len(c), sum(c) / max(1, len(c))))
    rd.say()
    p1 = mannwhitneyu(a_all, b_all, alternative='greater').pvalue
    ok1 = p1 < 0.05 and sum(dirs) > len(dirs) / 2
    rd.rec('CH1', 'graffiti with an Indus parallel lie deeper within their sites', 'pooled depth rank %.3f (%d) against %.3f (%d), p = %.4g; deeper in %d of %d sites' % (
        sum(a_all) / len(a_all), len(a_all), sum(b_all) / len(b_all), len(b_all), p1, sum(dirs), len(dirs)), ok1)
    p2 = mannwhitneyu(c_all, d_all).pvalue
    ok2 = p2 < 0.05
    rd.rec('CH2', 'composite graffiti lie at a different depth from single signs (two-sided)', 'composites %.3f (%d), others %.3f (%d), p = %.4g; shallower in %d of %d sites' % (
        sum(c_all) / max(1, len(c_all)), len(c_all), sum(d_all) / len(d_all), len(d_all), p2, sum(dirs2), len(dirs2)), ok2)
    rd.rec('P', 'progress rule: CH1', 'CH1 %s' % ok1, ok1)
    rd.finish()


if __name__ == '__main__':
    main()
