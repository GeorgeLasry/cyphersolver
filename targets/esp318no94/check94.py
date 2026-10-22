"""Review check of Michael Brackx's no. 94 alphabet (issue #62).

Decodes the letter-sign runs of ct94_brackx.txt with his 39-class key, scores them per character against the
shared Spanish model, and compares with two controls: the letter's own clear islands (real Spanish in this
hand) and the same transcription under keys with the class values shuffled (same value multiset).
Also counts code-group tokens and how many carry his firm or tentative readings.

    PYTHONUTF8=1 python targets/esp318no94/check94.py
"""
import math, os, re, random, sys
from collections import Counter
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from lang import lm

HERE = os.path.dirname(__file__)
KEY = dict(zip('2 3 4 5 6 7 8 9 : = A B D E F1 F2 G H I K L M O P Q S T V W X Z5 a b d e f o p q t'.split(),
               'd a e n t s h s i r o u p m c s g l r l s r a i s n d q c o s u e p o s a a a t'.split()))
FIRM = {'qa': 'que', 'rah': 'y', 'mny': 'de', 'mys': 'en', 'pif': 'no', 'nyb': 'lo', 'pat': 'por', 'nyl': 'havia',
        'qaz': 'VAl', 'qag': 'se', 'mnb': 'la', 'nae': 'los', 'lux': 'como', 'qe': 'quando', 'gik': 'su',
        'reg': 'yo', 'mnh': 'gente', 'pns': 'puerto', 'malg': 'll', 'malh': 'll'}
TENT = {'mog': 'a', 'lik': 'buena', 'pnb': 'antes', 'pad': 'bien', 're': 'esto', 'mok': 'dar', 'mas': 'el',
        'pit': 'contra', 'leg': 'ellos', 'nag': 'mas', 'neb': 'hazer', 'per': 'para', 'nob': 'dicho', 'mos': 'ellos'}


def tokens():
    for line in open(os.path.join(HERE, 'ct94_brackx.txt'), encoding='utf8'):
        if line.startswith('#'):
            continue
        line = re.sub(r'\{[^}]*\}', ' | ', line)
        for t in line.split():
            yield t


def runs(key):
    """Letter-sign runs between code groups, decoded."""
    out, cur = [], []
    for t in tokens():
        if t in key:
            cur.append(key[t])
        else:
            if len(cur) >= 4:
                out.append(''.join(cur))
            cur = []
    if len(cur) >= 4:
        out.append(''.join(cur))
    return out


def per_char(m, texts):
    tot = n = 0
    for s in texts:
        x = m.encode(s)
        if len(x) < 5:
            continue
        tot += m.score_idx(x)
        n += len(x) - m.order + 1
    return tot / n, n


def class_runs():
    """Letter-sign runs as lists of sign labels (the key's classes)."""
    out, cur = [], []
    for t in tokens():
        if t in KEY:
            cur.append(t)
        else:
            if len(cur) >= 5:
                out.append(cur)
            cur = []
    if len(cur) >= 5:
        out.append(cur)
    return out


ES_FREQ = dict(e=13.7, a=12.5, o=8.7, s=8.0, r=6.9, n=6.7, i=6.2, d=5.9, l=5.0, c=4.7, t=4.6, u=3.9, m=3.2,
               p=2.5, b=1.4, g=1.0, v=0.9, y=0.9, q=0.9, h=0.7, f=0.7, z=0.5, x=0.2)


def anneal(m, rs, start=None, iters=60000, seed=0):
    """Simulated annealing of a homophonic key (39 classes -> letters) over the runs `rs`.
    Objective: LM log-probability minus n * KL(letter frequencies || Spanish), so that a degenerate key cannot win.
    Returns the best key's LM score per scored character."""
    import numpy as np
    signs = list(KEY)
    si = {s: i for i, s in enumerate(signs)}
    seq = np.array([si[t] for r in rs for t in r])
    cnt = np.bincount(seq, minlength=len(signs)).astype(float)
    k = m.order
    starts = np.cumsum([0] + [len(r) for r in rs])
    valid = np.concatenate([np.arange(a, b - k + 1) for a, b in zip(starts[:-1], starts[1:])])
    alph = [c for c in ES_FREQ if c in m.index]
    letters = [m.index[c] for c in alph]
    q = np.full(m.A, 1e-4)
    for c in alph:
        q[m.index[c]] = ES_FREQ[c]
    q /= q.sum()
    rnd = random.Random(seed)
    key = np.array([m.index[KEY[s]] for s in signs]) if start == 'brackx' else         np.array([rnd.choice(letters) for _ in signs])

    def lmscore(kk):
        x = kk[seq]
        ctx = np.zeros(len(valid), dtype=np.int64)
        for j in range(k):
            ctx = ctx * m.A + x[valid + j]
        return float(m.lp[ctx].sum())

    def score(kk):
        f = np.bincount(kk, weights=cnt, minlength=m.A) / cnt.sum()
        nz = f > 0
        kl = float((f[nz] * np.log(f[nz] / q[nz])).sum())
        return lmscore(kk) - len(seq) * kl
    cur = score(key)
    best, bestkey = cur, key.copy()
    T0 = 30.0
    for it in range(iters):
        T = T0 * (1 - it / iters) + 0.01
        i = rnd.randrange(len(signs))
        old = key[i]
        key[i] = rnd.choice(letters)
        s = score(key)
        if s >= cur or rnd.random() < math.exp((s - cur) / T):
            cur = s
            if s > best:
                best, bestkey = s, key.copy()
        else:
            key[i] = old
    agree = sum(1 for s, v in zip(signs, bestkey) if m.alpha[v] == KEY[s])
    return lmscore(bestkey) / len(valid), agree


def coverage(texts, minlen=4):
    """Share of decoded letters covered by Spanish words of >= minlen letters (lexicon: es-golden-age sources),
    matched greedily longest-first; a proxy for how much of the letter-sign text reads as words."""
    from lang import corpora
    raw = lm.norm(corpora.text(['es-quijote', 'es-vasto-memorias']), 'early', spaces=True)
    lex = {w for w in raw.split() if len(w) >= minlen}
    # spelling of the 1500s hand, as in the decrypt: u/v and i/j merged
    lex |= {w.replace('v', 'u').replace('j', 'i') for w in lex}
    top = max(len(w) for w in lex)
    cov = tot = 0
    for s in texts:
        s = s.replace('v', 'u').replace('j', 'i')
        tot += len(s)
        i = 0
        while i < len(s):
            for L in range(min(top, len(s) - i), minlen - 1, -1):
                if s[i:i + L] in lex:
                    cov += L
                    i += L
                    break
            else:
                i += 1
    return cov / tot


def write_tsv():
    """validation.tsv for docs/_validate.py: letter signs -> letter, firm code groups -> reading, the rest unread."""
    out = ['# model: es-golden-age', '# source: ct94_brackx.txt with Brackx\'s key (issue #62); firm code groups only',
           '# note: clear-text islands and tentative or open code groups are unread and split the text']
    for line in open(os.path.join(HERE, 'ct94_brackx.txt'), encoding='utf8'):
        if line.startswith('#'):
            continue
        line = re.sub(r'\{[^}]*\}', ' CLEAR ', line)
        for t in line.split():
            if t in KEY:
                out.append(f'{t}\t{KEY[t]}')
            elif t in FIRM:
                out.append(f'{t}\t{FIRM[t].lower()}')
            else:
                out.append(f'{t}\t?')
    open(os.path.join(HERE, 'validation.tsv'), 'w', encoding='utf8').write('\n'.join(out) + '\n')
    print(len(out) - 3, 'pairs written')


def write_reveal(start_pat='qag V a 4 5 e : a p qe', nlines=3):
    """docs/reveal/esp318no94.json: a passage of f. 120v decoded with Brackx's key (firm codes 'code', tentative
    'unc', open 'unk', clear text 'plain')."""
    import json
    lines = [l.rstrip('\n') for l in open(os.path.join(HERE, 'ct94_brackx.txt'), encoding='utf8') if not l.startswith('#')]
    i = next(k for k, l in enumerate(lines) if l.startswith(start_pat))
    toks = []
    for line in lines[i:i + nlines]:
        for part in re.split(r'(\{[^}]*\})', line):
            if part.startswith('{'):
                toks.append({'g': '', 'p': part[1:-1].upper() + ' ', 'cls': 'plain'})
                continue
            for t in part.split():
                if t in KEY:
                    toks.append({'g': t, 'p': KEY[t]})
                elif t in FIRM:
                    toks.append({'g': t, 'p': ' ' + FIRM[t].replace('VAl', 'V. Al.') + ' ', 'cls': 'code'})
                elif t in TENT:
                    toks.append({'g': t, 'p': ' ' + TENT[t] + '? ', 'cls': 'unc'})
                else:
                    toks.append({'g': t, 'p': '?', 'cls': 'unk'})
    out = {'slug': 'esp318no94', 'anchor': 'key',
           'title': 'F. 120v: Portocarrero and the 800 peones',
           'caption': 'Three lines of BnF Espagnol 318 f. 120v in Michael Brackx\'s sign transcription (ct94_brackx.txt), decoded with his key by check94.py: '
                      '"quando Puertocarrero vino, y que no ... sacar la gente; HAN ENVIADOS ASTA OCHOCIENTOS PEONES ..."',
           'unit': 'signs and code groups',
           'key_note': 'Brackx\'s 39-class alphabet and his firm code readings (issue #62); tentative readings marked ?, unread groups ?. Sign labels are his ASCII stand-ins for the glyphs.',
           'tokens': toks}
    dst = os.path.join(HERE, '..', '..', 'docs', 'reveal', 'esp318no94.json')
    open(dst, 'w', encoding='utf8').write(json.dumps(out, ensure_ascii=False, indent=1) + '\n')
    print(len(toks), 'tokens ->', dst)


def main():
    if '--reveal' in sys.argv:
        return write_reveal()
    if '--tsv' in sys.argv:
        return write_tsv()
    if '--coverage' in sys.argv:
        rnd = random.Random(94)
        signs, vals = list(KEY), list(KEY.values())
        print('word coverage, Brackx key:', round(coverage(runs(KEY)), 3))
        for i in range(3):
            rnd.shuffle(vals)
            print('word coverage, shuffled-value key:', round(coverage(runs(dict(zip(signs, vals)))), 3))
        clear = []
        for line in open(os.path.join(HERE, 'ct94_brackx.txt'), encoding='utf8'):
            clear += [c.replace(' ', '') for c in re.findall(r'\{([^}]*)\}', line)]
        print('word coverage, the letter\'s clear islands:', round(coverage(clear), 3))
        return
    if '--anneal' in sys.argv:
        m = lm.load('es-golden-age', order=5, spaces=False)
        rs = class_runs()
        flat = [t for r in rs for t in r]
        rnd = random.Random(1)
        rnd.shuffle(flat)
        sh, i = [], 0
        for r in rs:
            sh.append(flat[i:i + len(r)])
            i += len(r)
        print('anneal from Brackx key, real text (score, classes agreeing with his key):', anneal(m, rs, 'brackx'))
        for sd in range(4):
            print(f'random start {sd}: real text', anneal(m, rs, seed=sd), '| shuffled-order text', anneal(m, sh, seed=sd))
        return

    m = lm.load('es-golden-age', order=5, spaces=False)
    real = runs(KEY)
    s_real, n = per_char(m, real)
    clear = []
    for line in open(os.path.join(HERE, 'ct94_brackx.txt'), encoding='utf8'):
        clear += re.findall(r'\{([^}]*)\}', line)
    s_clear, nc = per_char(m, [c.replace(' ', '') for c in clear])
    rnd = random.Random(94)
    ctrl = []
    signs, vals = list(KEY), list(KEY.values())
    for _ in range(200):
        rnd.shuffle(vals)
        ctrl.append(per_char(m, runs(dict(zip(signs, vals))))[0])
    ctrl.sort()
    groups = Counter(t for t in tokens() if re.fullmatch(r'[a-z]{2,4}', t) and t not in KEY)
    tot = sum(groups.values())
    firm = sum(c for g, c in groups.items() if g in FIRM)
    tent = sum(c for g, c in groups.items() if g in TENT)
    print(f'letter-sign runs decoded: {n} chars, {s_real:.3f} per char')
    print(f'clear islands of the same letter: {nc} chars, {s_clear:.3f} per char')
    print(f'200 shuffled-value keys: best {ctrl[-1]:.3f}, median {ctrl[100]:.3f}')
    print(f'code-group tokens {tot}, distinct {len(groups)}; firm {firm}, tentative {tent}, open {tot - firm - tent}')
    print('initials of code-group tokens:', Counter(g[0] for g in groups.elements()).most_common(8))
    words = ['puertocarero', 'cardona', 'semenaoa', 'pesquisa', 'iuramento', 'presoneros', 'castillo', 'castill',
             'saque', 'aprouech', 'inuentar', 'acuchi', 'hocuentos', 'punsaladas', 'principal', 'seruador', 'conseeruador']
    joined = '|'.join(real)
    print('words in the decoded runs:', {w: joined.count(w) for w in words if w in joined})


if __name__ == '__main__':
    main()
