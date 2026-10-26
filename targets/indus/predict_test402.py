"""Set 402 (goal run loop 48): Harappa square seals over the periods. Writes results/predict_test402.md."""
import rtools as R
from scipy.stats import spearmanr

ORDER = {'Period 1': 1, 'Period 1B': 1.5, 'Period 2': 2, 'Period 2B': 2.5, 'Period 3A': 3, 'Period 3B': 4, 'Period 3B-1': 4,
         'Period 3B-2': 4.5, 'Period 3C-1': 5, 'Period 3C-2': 6, 'Period 3C-3': 7, 'Period 3C-4': 8, 'Period 4': 9, 'Period 5A': 10}


def main():
    rd = R.Round('Four-hundred-and-second registered predictions: goal loop 48, Harappa seals over time', 'predict_test402')
    A, B, rowsA, recs, F = R.load_all()
    rows = []
    for r in F:
        rec = recs.get(r['sealid'])
        if not rec or r['site'] != 'Harappa' or not str(rec[20]).startswith('SEAL:S'):
            continue
        per = ORDER.get(str(rec[8]).strip())
        try:
            sz = float(rec[31])
        except (TypeError, ValueError):
            sz = 0
        if per is not None and r['flat']:
            rows.append((per, sz, len(r['flat'])))
    s = [(p, z) for p, z, n in rows if z > 0]
    r1, p1 = spearmanr([p for p, z in s], [z for p, z in s])
    r2, p2 = spearmanr([p for p, z, n in rows], [n for p, z, n in rows])
    rd.say('- %d Harappa square seals with a period (%d with a size).' % (len(rows), len(s)))
    rd.rec('SP1', 'seal size falls over the periods', 'rho %.2f, p = %.4f' % (r1, p1), r1 < 0 and p1 < 0.05)
    rd.rec('SP2', 'text length rises over the periods', 'rho %.2f, p = %.4f' % (r2, p2), r2 > 0 and p2 < 0.05)
    rd.rec('P', 'progress rule: either holds', 'SP1 %s, SP2 %s' % (r1 < 0 and p1 < 0.05, r2 > 0 and p2 < 0.05), (r1 < 0 and p1 < 0.05) or (r2 > 0 and p2 < 0.05))
    rd.finish()


if __name__ == '__main__':
    main()
