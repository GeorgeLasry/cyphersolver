"""Set 640: the Indus-parallel share of Keeladi graffiti in the oldest dated levels (300+ cm, 5th-6th c. BCE) against
the levels above 200 cm (3rd c. BCE onward). Dates: data/graffiti/dates/dates.tsv (Rajan, Sivanantham & Yatheeskumar
2025; Keeladi 2019). Writes results/predict_test640.md."""
import json

import rtools as R
from predict_test637 import parallels
from scipy.stats import fisher_exact


def main():
    rd = R.Round('Set 640 registered predictions: Indus-parallel graffiti in the oldest dated levels at Keeladi', 'predict_test640')
    P = parallels()
    base = lambda s: s.replace('C', '').split('.')[0]
    deep = [0, 0]
    top = [0, 0]
    for r in json.load(open('data/graffiti/raw/bysite/Keeladi.json', encoding='utf-8'))['data']:
        has = base(str(r['sign']).strip()) in P
        for x in r['result'].get('depth', []):
            try:
                d = float(x['key'])
            except ValueError:
                continue
            row = deep if d >= 300 else (top if d < 200 else None)
            if row is not None:
                row[0 if has else 1] += x['value']
    p = fisher_exact([deep, top], alternative='greater')[1]
    rd.rec('KD1', 'Keeladi graffiti at 300+ cm (5th-6th c. BCE) have an Indus parallel more often than those above 200 cm',
           '300+ cm %d of %d; under 200 cm %d of %d; p = %.4f' % (deep[0], sum(deep), top[0], sum(top), p), p < 0.05)
    rd.rec('P', 'progress rule: none (a dated version of set 637 at one site)', '', False)
    rd.finish()


if __name__ == '__main__':
    main()
