"""Independent check of Michael Brackx's Cipher-1 transcriptions and keys (issues #73, #77, #78, #79, #83).

His figures and per-leaf keys are in brackx2026/ (copied from the issues). This script does not use his decoder or his
language model: each leaf is decoded line by line with this project's beam (measure.beam_aligned: period-French
6-gram lm.pkl, beam 300) over his key's letter sets, then scored three ways.

  copy   letters of the decode matched by the contemporary clear copy (difflib, matched / decoded letters, as his
         crib.py). Copies: brackx2026/copies/. f155r/f156/f157 are the readings of issue #70, made before his
         cipher-guided re-reading; the *_corr files apply his #83 corrections (which were guided by the cipher, so
         they are reported apart). f19_clear is his own reading of f. 19 (#78).
  sense  measure.py's rule: share of tokens keyed and inside a run of >= 3 corpus words / >= 10 letters.
  twin   ff. 196/201: matched letters between the two decodes / letters of the f. 196 decode.

Control: the key's letter sets permuted among its non-code figures (set sizes kept, so the decoder has the same
freedom), 3 seeds, same decoder and scores. Output brackx_validate.json.

  python brackx_validate.py            (decodes cached in measure_cache/bx_*)
"""
import json, os, sys, random, difflib, unicodedata
sys.argv = [sys.argv[0]]  # measure.py reads --key from argv at import
import measure as M

HERE = os.path.dirname(os.path.abspath(__file__))
B = os.path.join(HERE, 'brackx2026')

LEAVES = [  # name, cipher files, key, copy files (None = no copy), issue
    ('fr.15571 f.177r', ['f177r_cipher.txt'], 'key_f177.json', None, 73),
    ('fr.15571 f.177v', ['f177v_cipher.txt'], 'key_f177.json', None, 73),
    ('f.154v block A', ['f154vA_cipher.txt'], 'key_f154v.json', ['f157_f154v.txt'], 77),
    ('f.154v block B', ['f154vB_cipher.txt'], 'key_f154v.json', ['f157_f154v.txt'], 77),
    ('f.18r', ['f18r_cipher.txt'], 'key_f18.json', ['f19_clear.txt'], 78),
    ('f.18v', ['f18v_cipher.txt'], 'key_f18.json', ['f19_clear.txt'], 78),
    ('f.20r', ['f20r_cipher.txt'], 'key_f18.json', ['f19_clear.txt'], 78),
    ('f.123r', ['f123r_cipher.txt'], 'key_f123_124.json', None, 78),
    ('f.123v', ['f123v_cipher.txt'], 'key_f123_124.json', None, 78),
    ('f.124r', ['f124r_cipher.txt'], 'key_f123_124.json', None, 78),
    ('f.124v', ['f124v_cipher.txt'], 'key_f123_124.json', None, 78),
    ('f.110', ['f110_cipher.txt'], 'key_f110.json', None, 79),
    ('f.143r', ['f143r_cipher.txt'], 'key_f143.json', ['f155r_f143.txt', 'f155r_f143_corr.txt'], 83),
    ('f.143v', ['f143v_cipher.txt'], 'key_f143.json', ['f155r_f143.txt', 'f155r_f143_corr.txt'], 83),
    ('f.150r', ['f150r_cipher.txt'], 'key_f150.json', ['f155v_f150r.txt'], 83),
    ('f.150v', ['f150v_cipher.txt'], 'key_f150v.json', ['f156_f150v.txt', 'f156_f150v_corr.txt'], 83),
    ('f.154r', ['f154r_cipher.txt'], 'key_f154r.json', ['f157_f154r.txt', 'f157_f154r_corr.txt'], 83),
    ('f.173', ['f173_cipher.txt'], 'key_f173.json', None, 83),
    ('f.196', ['f196_cipher.txt'], 'key_f196_201.json', None, 83),
    ('f.201', ['f201_cipher.txt'], 'key_f196_201.json', None, 83),
]


def norm(s):
    s = unicodedata.normalize('NFD', s.lower())
    s = ''.join(c for c in s if c.isalpha())
    return s.replace('v', 'u').replace('j', 'i').replace('y', 'i').replace('w', 'u')


def copy_text(fn):
    lines = [l for l in open(os.path.join(B, 'copies', fn), encoding='utf-8') if not l.startswith('#')]
    return norm(''.join(lines))


def agree(dec, ref):
    sm = difflib.SequenceMatcher(None, dec, ref, autojunk=False)
    return sum(b.size for b in sm.get_matching_blocks()) / max(1, len(dec))


def prep_key(raw):
    k = {}
    for t, v in raw.items():
        if t == '76':
            k[t] = ['roidenauarre']
        elif v in (['+'], ['*']):
            k[t] = ['+']
        else:
            k[t] = [x.replace('v', 'u') for x in v]
    return k


def is_figure(t, v):
    return not t.isdigit() and v != ['+'] and all(len(x) <= 2 for x in v)


def scramble(key, seed):
    rng = random.Random(seed)
    figs = [t for t, v in key.items() if is_figure(t, v)]
    by = {}
    for t in figs:
        by.setdefault(len(key[t]), []).append(t)
    out = dict(key)
    for n, ts in by.items():
        vals = [key[t] for t in ts]
        rng.shuffle(vals)
        out.update(zip(ts, vals))
    return out


def decode(files, key, tag):
    os.makedirs(os.path.join(HERE, 'measure_cache'), exist_ok=True)
    cf = os.path.join(HERE, 'measure_cache', 'bx_' + tag + '.json')
    if os.path.exists(cf):
        return json.load(open(cf, encoding='utf-8'))
    res = []
    for f in files:
        for ln in open(os.path.join(B, f), encoding='utf-8'):
            toks = ln.split()
            if toks:
                txt, lens = M.beam_aligned(toks, key)
                res.append({'tokens': toks, 'text': txt, 'lens': list(lens)})
    json.dump(res, open(cf, 'w', encoding='utf-8'))
    return res


def sense(res, key):
    M.KEY = key
    n, read, ctx, unk, text, mask = M.score(res)
    return n, read / max(1, n)


def leaf_scores(name, files, key, copies, tag):
    res = decode(files, key, tag)
    n, frac = sense(res, key)
    dec = norm(''.join(r['text'] for r in res))
    out = {'tokens': n, 'sense': round(frac, 3), 'letters': len(dec)}
    for c in copies or []:
        out['copy:' + c] = round(agree(dec, copy_text(c)), 3)
    return out, dec


def main():
    report = {}
    decs = {}
    for name, files, kf, copies, issue in LEAVES:
        raw = json.load(open(os.path.join(B, kf), encoding='utf-8'))
        key = prep_key(raw)
        tag = name.replace(' ', '_').replace('.', '')
        real, dec = leaf_scores(name, files, key, copies, tag)
        decs[name] = dec
        ctl = []
        for s in range(3):
            c, cdec = leaf_scores(name, files, scramble(key, s), copies, f'{tag}_s{s}')
            ctl.append(c)
            decs[f'{name}#s{s}'] = cdec
        floor = {k: round(sum(c[k] for c in ctl) / len(ctl), 3) for k in real if k not in ('tokens', 'letters')}
        sets = [len(key.get(t, M.AL)) for f in files for ln in open(os.path.join(B, f), encoding='utf-8') for t in ln.split()]
        real['mean_set_size'] = round(sum(sets) / max(1, len(sets)), 2)
        report[name] = {'issue': issue, 'key': kf, 'real': real, 'scrambled_mean': floor}
        print(f"{name:18s} #{issue} tok {real['tokens']:5d} set {real['mean_set_size']:.2f} sense {real['sense']:.3f} "
              f"(floor {floor['sense']:.3f})" + ''.join(
                  f" | {k[5:]} {real[k]:.3f} (floor {floor[k]:.3f})" for k in real if k.startswith('copy:')), flush=True)
    for s in ['', '#s0', '#s1', '#s2']:
        a, b = decs['f.196' + s], decs['f.201' + s]
        report.setdefault('twin 196/201', {})['real' if not s else 'scrambled' + s] = round(agree(a, b), 3)
    print('twin 196/201', report['twin 196/201'])
    json.dump(report, open(os.path.join(HERE, 'brackx_validate.json'), 'w', encoding='utf-8'), indent=1)


if __name__ == '__main__':
    main()
