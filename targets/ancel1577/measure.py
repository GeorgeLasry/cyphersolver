"""Re-measure Harumi-Matsuba's Ancel 1577 reading (contributed/) with this project's tools.

    PYTHONUTF8=1 python targets/ancel1577/measure.py > targets/ancel1577/measure.txt

1. tokens: cipher symbols and plain-letter groups per page, from contributed/transcription/<page>.txt
2. fraction_read: symbols with a key value + plain-letter groups with a checked meaning, over all tokens
3. LM: mean log-prob per character of the key output (letters only) under lang 'fr-1530-despatches' (order 5, no spaces),
   against the same transcription decoded with 20 shuffled keys (letter values permuted)
4. coherent share: the key output of each line run, segmented by dynamic programming into words of a
   16th-century French vocabulary (fr-1520s-diplomatic + fr-henri4, words of 3+ letters seen 3+ times, plus a
   closed list of 1-2 letter words; no lone elided consonants); share of cipher tokens whose letters fall inside a word. The same is done
   for the shuffled keys, so the figure can be read against chance.
5. calibration: letter agreement of their p.258 / p.285 key output with the five-reader margin, recomputed
   from contributed/calib/*_decode.tsv where the files allow it.
The key is the TOKENS table of contributed/src/vk.py, read with ast (their code is not executed).
"""
import ast, collections, math, os, random, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, '..', '..')
sys.path.insert(0, ROOT)
from lang import lm

C = os.path.join(HERE, 'contributed')
PAGES = ['p525', 'p526', 'p539', 'p561', 'p562', 'p563', 'p565']   # the read pages; p570 and p033 reported apart

def load_key():
    src = open(os.path.join(C, 'src', 'vk.py'), encoding='utf-8').read()
    tree = ast.parse(src)
    for node in tree.body:
        if isinstance(node, ast.Assign) and getattr(node.targets[0], 'id', '') == 'TOKENS':
            return {k: v for k, (v, s) in ast.literal_eval(node.value).items()}
    raise SystemExit('no TOKENS')

KEY = load_key()
CHECKED_CODES = {'saturnus', 'juno', 'my', 'my3', 'monseigneur', 'monseig'}   # OPEN.en.md section 3: margin-checked, or clear words

def load(page):
    rows = []
    for ln in open(os.path.join(C, 'transcription', page + '.txt'), encoding='utf-8'):
        ln = ln.rstrip('\n')
        if not ln.strip() or ln.startswith('#'): continue
        lid, _, toks = ln.partition('\t')
        rows.append((lid, toks.split()))
    return rows

def base(tok):
    return tok[:-1] if tok.endswith('?') and len(tok) > 1 else tok

def tokens(rows):
    """[(kind, tok)] kind: sym (has value), unk (unreadable or not in key), code (plain-letter group)."""
    out = []
    for _, toks in rows:
        for t in toks:
            if t == '|': continue
            if t.startswith('{'):
                out.append(('code', t)); continue
            b = base(t)
            out.append(('sym', b) if b in KEY else ('unk', b))
    return out

def decode_runs(rows, key):
    """runs of (letters, token index list) broken at codes and unreadables, for segmentation and LM."""
    runs, cur, idx, i = [], [], [], 0
    for _, toks in rows:
        for t in toks:
            if t == '|': continue
            b = base(t)
            if t.startswith('{') or b not in key:
                if cur: runs.append((''.join(cur), idx)); cur, idx = [], []
                i += 1; continue
            v = lm.norm(key[b], 'early')
            for ch in v:
                cur.append(ch); idx.append(i)
            i += 1
    if cur: runs.append((''.join(cur), idx))
    return runs, i

def vocab():
    cnt = collections.Counter()
    for f in ('fr-1520s-diplomatic.txt', 'fr-henri4.txt'):
        p = os.path.join(ROOT, 'lang', 'corpora', f)
        txt = lm.norm(open(p, encoding='utf-8', errors='replace').read(), 'early')
        cnt.update(re.findall(r'[a-z]+', txt))
    v = {w for w, n in cnt.items() if len(w) >= 3 and n >= 3}
    v |= {'a', 'y', 'o', 'ie', 'il', 'le', 'la', 'de', 'du', 'en', 'et', 'ne', 'ny', 'se', 'si', 'sa', 'ce', 'ou',
          'au', 'un', 'on', 'me', 'ma', 'mo', 'ni', 'qu', 'es', 'sy', 'cy', 'ia'}
    return v

def segment(s, V, maxlen=20):
    """best[i] = max letters covered in s[:i]."""
    n = len(s); best = [0] * (n + 1); back = [None] * (n + 1)
    for i in range(1, n + 1):
        best[i], back[i] = best[i - 1], None
        for L in range(1, min(maxlen, i) + 1):
            w = s[i - L:i]
            if w in V and best[i - L] + L > best[i]:
                best[i], back[i] = best[i - L] + L, L
    cov = [False] * n; i = n
    while i > 0:
        if back[i] is None: i -= 1
        else:
            for j in range(i - back[i], i): cov[j] = True
            i -= back[i]
    return cov

def coherent(rows, key, V):
    runs, ntok = decode_runs(rows, key)
    covered = set(); seen = set()
    for s, idx in runs:
        cov = segment(s, V)
        tokcov = collections.defaultdict(list)
        for c, t in zip(cov, idx): tokcov[t].append(c)
        for t, cs in tokcov.items():
            seen.add(t)
            if all(cs): covered.add(t)
    return len(covered), ntok

def shuffled(key, seed):
    letters = [k for k, v in key.items() if len(v) == 1]
    vals = [key[k] for k in letters]; random.Random(seed).shuffle(vals)
    k2 = dict(key); k2.update(zip(letters, vals)); return k2

def main():
    M = lm.load('fr-1530-despatches', order=5, spaces=False)
    V = vocab()
    print('# ancel1577 measure (measure.py), lang model fr-1530-despatches order 5 no spaces, vocabulary', len(V), 'words')
    tot = collections.Counter()
    print('page\ttokens\tsym\tunk\tcodes\tcodes_checked\tfraction_read\tLM_real\tLM_shuf_med\tcoh_real\tcoh_shuf_med')
    for page in PAGES + ['p570', 'p033']:
        rows = load(page)
        tk = tokens(rows)
        c = collections.Counter(k for k, _ in tk)
        chk = sum(1 for k, t in tk if k == 'code' and re.sub(r'[{}?]', '', t).lower() in CHECKED_CODES)
        n = len(tk); read = c['sym'] + chk
        def lmscore(key):
            runs, _ = decode_runs(rows, key)
            txt = ''.join(s for s, _ in runs)
            return M.per_char(txt)
        real = lmscore(KEY)
        sh = sorted(lmscore(shuffled(KEY, s)) for s in range(20))
        cr, ntok = coherent(rows, KEY, V)
        csh = sorted(coherent(rows, shuffled(KEY, s), V)[0] for s in range(20))
        print(f'{page}\t{n}\t{c["sym"]}\t{c["unk"]}\t{c["code"]}\t{chk}\t{read/n:.3f}\t{real:.3f}\t{sh[10]:.3f}\t'
              f'{cr/ntok:.3f}\t{csh[10]/ntok:.3f}')
        if page in PAGES:
            tot['n'] += n; tot['read'] += read; tot['sym'] += c['sym']; tot['unk'] += c['unk']; tot['code'] += c['code']
            tot['cr'] += cr; tot['ntok'] += ntok; tot['csh'] += csh[10]
    print(f'seven read pages: tokens {tot["n"]}, symbols with value {tot["sym"]}, unreadable/unkeyed {tot["unk"]}, '
          f'plain-letter groups {tot["code"]}; fraction_read {tot["read"]/tot["n"]:.3f}; '
          f'coherent share (tokens inside dictionary words) {tot["cr"]/tot["ntok"]:.3f} vs shuffled-key median '
          f'{tot["csh"]/tot["ntok"]:.3f}')
    # calibration recomputation from their per-letter decode tables, if they carry a margin column
    for p in ('p258', 'p285'):
        f = os.path.join(C, 'calib', p + '_decode.tsv')
        rows = [l.rstrip('\n').split('\t') for l in open(f, encoding='utf-8') if l.strip() and not l.startswith('#')]
        print(f'calib {p}: {len(rows)} rows in {p}_decode.tsv, header {rows[0][:6]}')

if __name__ == '__main__':
    main()
