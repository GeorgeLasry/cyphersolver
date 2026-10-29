"""b5_score.py -- score the frozen b5 candidates on the full 37-item battery (b5_PREREG.md).

Reads b5_params.json (commit it first).  Seeds 1-5 per candidate; b3's battery, tolerance and match rule
unchanged; real values and tolerances from this run's corrected-parse ZL and autocopist seeds 19 / 7.
Primary outcome: held-out matches (groups d e g h i j k, 20 items), full battery, mean and range over seeds,
against the voynich_A / voynich_B calibration rows.
"""
import sys, os, json, time, collections, statistics
_HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, _HERE)
import a4_selfcitation as a4, b3_bakeoff as b3, b5_generators as g5

HELD = [k for k, _ in b3.ITEMS if k[0] in 'degkhij']
FIT = [k for k, _ in b3.ITEMS if k[0] in 'abcf']
SEEDS = [1, 2, 3, 4, 5]


def main():
    t0 = time.time()
    P = json.load(open(os.path.join(_HERE, 'b5_params.json')))
    zl = b3.load_zl_lang(); skel = a4.skeleton(zl); N = len(b3.words_of(zl)); NS = 10053
    corpora = collections.OrderedDict()
    corpora['voynich_ZL'] = zl
    corpora['voynich_A'] = [p for p in zl if p['lang'] == 'A']
    corpora['voynich_B'] = [p for p in zl if p['lang'] == 'B']
    corpora['autocopist_s19'] = a4.Autocopist(19).generate(skel)
    corpora['autocopist_s7'] = a4.Autocopist(7).generate(skel)
    for c, make in (('G', g5.make_G), ('C', g5.make_C)):
        if c in P:
            for s in SEEDS:
                corpora[f'{c}_s{s}'] = make(s, **P[c]['params'])
    full = collections.OrderedDict(); short = collections.OrderedDict(); xf = {}; xs = {}
    for n, p in corpora.items():
        full[n] = b3.battery(p, n, xf); short[n] = b3.battery(b3.truncate_pages(p, NS), n, xs)
        print(f'[{time.time()-t0:5.0f}s] {n} done', flush=True)
    tol_f, mf = b3.score(full); tol_s, ms = b3.score(short)

    def cnt(m, keys): return sum(m[k] for k in keys)
    summ = collections.OrderedDict()
    for n in corpora:
        summ[n] = {'held_full': cnt(mf[n], HELD), 'held_short': cnt(ms[n], HELD), 'fit_full': cnt(mf[n], FIT), 'fit_short': cnt(ms[n], FIT)}
    agg = {}
    for c in ('G', 'C'):
        names = [f'{c}_s{s}' for s in SEEDS if f'{c}_s{s}' in summ]
        if not names: continue
        agg[c] = {k: {'mean': statistics.mean(summ[n][k] for n in names), 'min': min(summ[n][k] for n in names), 'max': max(summ[n][k] for n in names)}
                  for k in ('held_full', 'held_short', 'fit_full', 'fit_short')}
        agg[c]['held_items_matched_by_all_seeds'] = [k for k in HELD if all(mf[n][k] for n in names)]
        agg[c]['held_items_failed_by_all_seeds'] = [k for k in HELD if not any(mf[n][k] for n in names)]
    calib = min(summ['voynich_A']['held_full'], summ['voynich_B']['held_full'])
    for c in agg:
        agg[c]['reproduces'] = agg[c]['held_full']['mean'] >= calib
    out = {'params': P, 'held_items': HELD, 'fit_items': FIT, 'calibration_held_full': calib,
           'summary': summ, 'aggregate': agg, 'full': full, 'short': short, 'tol_full': tol_f, 'tol_short': tol_s,
           'marks_full': mf, 'marks_short': ms, 'extra_full': xf, 'runtime_s': round(time.time() - t0, 1)}
    json.dump(out, open(os.path.join(_HERE, 'results', 'b5.json'), 'w'), indent=1, default=str)
    lab = dict(b3.ITEMS)
    L = ['# b5: generators built to pass the battery (scored once, after b5_params.json was committed)', '',
         f'Pre-registration: b5_PREREG.md.  Held-out items ({len(HELD)}): ' + ', '.join(lab[k] for k in HELD) + '.', '',
         f'Calibration (lower of voynich_A, voynich_B held-out matches, full): **{calib}/{len(HELD)}**', '',
         '| corpus | held-out full | held-out short | fit full | fit short |', '|---|---|---|---|---|']
    for n, v in summ.items():
        L.append(f"| {n} | {v['held_full']} | {v['held_short']} | {v['fit_full']} | {v['fit_short']} |")
    L += ['', '| candidate | held-out full mean (range) | held-out short mean | reproduces? | held-out items no seed matches |', '|---|---|---|---|---|']
    for c, a in agg.items():
        L.append(f"| {c} | {a['held_full']['mean']:.1f} ({a['held_full']['min']}-{a['held_full']['max']}) | {a['held_short']['mean']:.1f} | {'yes' if a['reproduces'] else 'no'} | "
                 + ', '.join(lab[k] for k in a['held_items_failed_by_all_seeds']) + ' |')
    L += ['', '## Values, full battery (real, tolerance, G seed 1, C seed 1)', '', '| item | set | real | tol | G_s1 | C_s1 |', '|---|---|---|---|---|---|']
    for k, _ in b3.ITEMS:
        f = lambda n: (f"{full[n][k]:.4g}" + (' ✓' if mf[n][k] else '')) if n in full and full[n][k] is not None else '-'
        L.append(f"| {lab[k]} | {'held' if k in HELD else 'fit'} | {full['voynich_ZL'][k]:.4g} | {tol_f[k]:.3g} | {f('G_s1')} | {f('C_s1')} |")
    open(os.path.join(_HERE, 'results', 'b5.md'), 'w', encoding='utf-8').write('\n'.join(L) + '\n')
    print('\n'.join(L[:30]))


if __name__ == '__main__':
    main()
