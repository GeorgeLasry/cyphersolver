"""b5_tune.py -- tune a b5 candidate on the FIT items only (groups a, b, c, f; b5_PREREG.md).

Computes nothing from groups d, e, g, h, i, j, k.  Random search, then writes the best parameters to
b5_params.json, which b5_score.py reads; commit b5_params.json before running b5_score.py.
usage: python b5_tune.py G [n_trials]
"""
import sys, os, json, math, random, collections, time
_HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, _HERE)
import a4_selfcitation as a4, b3_bakeoff as b3, b5_generators as g5

FIT = [k for k, _ in b3.ITEMS if k[0] in 'abcf']
RANGES = {'G': {'p_reuse': (0, 0.6), 'w_page': (0.3, 1), 'w_sect': (0, 1), 'habit': (0, 0.8), 'p_n1': (0.1, 0.9)},
          'C': {'nomen': (0, 2000), 'p_single': (0, 1), 'homo': (1, 40), 'overlap': (0, 1), 'p_null': (0, 0.3)}}
MAKE = {'G': g5.make_G, 'C': g5.make_C}
DEFAULTS = {'G': g5.G_DEFAULTS, 'C': g5.C_DEFAULTS}


def fit_items(pages):
    words = b3.words_of(pages); N = len(words); R = {}
    h0, h1, h2, h3 = b3.char_entropies(b3.page_strings(pages))
    _, _, m2, m3 = b3.char_entropies(b3.page_strings(pages, merged=True))
    R.update(a_h0_raw=h0, a_h1_raw=h1, a_h2_raw=h2, a_h3_raw=h3, a_h2_mrg=m2, a_h3_mrg=m3)
    L = [len(w) for w in words]; mean = sum(L) / N
    R['b_len_mean'] = mean; R['b_len_sd'] = math.sqrt(sum((x - mean) ** 2 for x in L) / N)
    R['b_len1'] = sum(x == 1 for x in L) / N; R['b_len9'] = sum(x >= 9 for x in L) / N
    cnt = collections.Counter(words); hap = sum(v == 1 for v in cnt.values())
    R['c_zipf'] = a4.zipf_slope(words); R['c_ttr'] = len(cnt) / N
    R['c_hapax_types'] = hap / len(cnt); R['c_hapax_tokens'] = hap / N; R['c_heaps'] = b3.heaps_exponent(words)
    mw = [a4.merge_glyphs(w) for w in words]; bg = collections.Counter()
    for w in mw: bg.update(zip(w, w[1:]))
    top = [b for b, _ in bg.most_common(200)]
    R['f_irrev'] = sum(bg.get((y, x), 0) == 0 for (x, y) in top) / len(top)
    ini = collections.Counter(w[0] for w in mw); fin = collections.Counter(w[-1] for w in mw)
    ti = {g for g, _ in ini.most_common(5)}; tf = {g for g, _ in fin.most_common(5)}
    R['f_lock'] = sum(w[0] in ti and w[-1] in tf for w in mw) / N
    return R


def loss(R, real, tol):
    """matches first, then summed distance in tolerance units"""
    d = {k: abs(R[k] - real[k]) / tol[k] for k in FIT}
    return -sum(v <= 1 for v in d.values()), sum(min(v, 5) for v in d.values())


def main():
    cand = sys.argv[1]; n = int(sys.argv[2]) if len(sys.argv) > 2 else 60
    real = fit_items(g5.real_pages())
    ac = [fit_items(a4.Autocopist(s).generate(a4.skeleton(g5.real_pages()))) for s in (19, 7)]
    tol = {k: max(0.10 * abs(real[k]), abs(ac[0][k] - ac[1][k])) for k in FIT}
    rng = random.Random(2026); best = None; t0 = time.time()
    trials = [dict(DEFAULTS[cand])] + [{k: rng.uniform(*r) for k, r in RANGES[cand].items()} for _ in range(n)]
    for i, par in enumerate(trials):
        R = fit_items(MAKE[cand](101, **par)); L = loss(R, real, tol)   # tuning seed 101, scoring seeds 1-5
        if best is None or L < best[0]:
            best = (L, par, R); print(f'[{time.time()-t0:5.0f}s] trial {i}: fit {-L[0]}/{len(FIT)} dist {L[1]:.2f} {par}', flush=True)
    # local refinement around the best point
    for i in range(n // 2):
        par = {k: min(max(best[1][k] + rng.gauss(0, 0.08 * (r[1] - r[0])), r[0]), r[1]) for k, r in RANGES[cand].items()}
        R = fit_items(MAKE[cand](101, **par)); L = loss(R, real, tol)
        if L < best[0]:
            best = (L, par, R); print(f'[{time.time()-t0:5.0f}s] refine {i}: fit {-L[0]}/{len(FIT)} dist {L[1]:.2f} {par}', flush=True)
    path = os.path.join(_HERE, 'b5_params.json')
    allp = json.load(open(path)) if os.path.exists(path) else {}   # G and C tuned in separate runs: re-read
    allp[cand] = {'params': best[1], 'fit_matches': -best[0][0], 'fit_items': FIT, 'tuning_seed': 101,
                  'trials': len(trials) + n // 2, 'fit_values': best[2], 'real_fit_values': real, 'tol': tol}
    json.dump(allp, open(path, 'w'), indent=1)
    print('wrote', path, best[1])


if __name__ == '__main__':
    main()
