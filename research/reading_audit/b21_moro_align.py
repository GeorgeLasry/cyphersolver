"""b21: align the F22b figures of morosini1589 R53 / R54 with the contemporary decipherment on f. 500r / 500v.

    python -X utf8 research/reading_audit/b21_moro_align.py R53|R54 [key_extra.json]   (b21 run: targets/morosini1589/texts/f22b_key_b21.json, 4 = c)

Figures: the DECODE transcription (decode/DOC_R53_D1717, DOC_R54_D1825), digits one by one; '?' = an illegible digit
(wildcard), '8?' = a doubtful 8 (taken as 8), '1^.' / '1_.' = a dotted 1 opening a three-figure nomenclator code.
Key: Lasry's F22b reconstruction (decode/DOC_R53_D3187), plus key_extra.json {code: value} if given.
Target: the decipherment (texts/R53_decifrato_f500r.txt, R54_decifrato_f500v.txt), bracketed expansions kept as
letters, [struck: ...] and [margin ...] notes dropped, normalised (lower case, j=i, v=u, letters only).

Dynamic programming over (figure position, letter position). An element is 1 or 2 figures, or 3 for a nomenclator
code (dotted 1 + two figures; 10x, 11x, 49x undotted). A keyed element matching the letters costs 0; a keyed element
standing for other letters costs 2 (its letters are recorded); an unkeyed element stands for 1-4 letters at cost 1;
a letter of the decipherment with no figure (double consonants the cipher spells single, words the decipherer
added) costs 0.7; a figure with no letter costs 1.2. Writes texts/<R>_align.tsv: element, figures, key value,
decipherment letters, kind; prints the unkeyed and contradicted elements grouped by code.
"""
import collections, json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
T = ROOT / 'targets' / 'morosini1589'
rec = sys.argv[1]
extra = json.loads(Path(sys.argv[2]).read_text(encoding='utf-8')) if len(sys.argv) > 2 else {}


def norm(s):
    s = s.lower().replace('j', 'i').replace('v', 'u')
    s = re.sub(r'[àá]', 'a', s); s = re.sub(r'[èé]', 'e', s); s = re.sub(r'[ìí]', 'i', s); s = re.sub(r'[òó]', 'o', s); s = re.sub(r'[ùú]', 'u', s)
    return re.sub(r'[^a-z]', '', s)


# key
KEY = collections.defaultdict(set)
for ln in (T / 'decode' / 'DOC_R53_D3187_3187.txt').read_text(encoding='utf-8').splitlines():
    m = re.match(r'^([\d|^.]+) - (.+)$', ln.strip())
    if not m: continue
    for c in m.group(1).split('|'):
        KEY[c.replace('1^.', 'D').replace('2^.', 'E')].add(norm(m.group(2)))
for c, v in extra.items():
    KEY[c] = {norm(x) for x in (v if isinstance(v, list) else [v])}
KEY['D51'] = {'nsre', 'hsre'}           # Lasry 'h.s.re' = N[ostro] S[igno]re (the decipherer's capital N looks like H)

# figures
src = {'R53': 'DOC_R53_D1717_1717.txt', 'R54': 'DOC_R54_D1825_1825.txt'}[rec]
raw = (T / 'decode' / src).read_text(encoding='utf-8')
raw = re.sub(r'<[^>]*>', ' ', raw, flags=re.S)
fig = []                                 # items: '0'-'9', '?', 'D'
for ln in raw.splitlines():
    if ln.startswith('#'): continue
    for t in ln.split():
        if t in ('1^.', '1_.'): fig.append('D'); continue
        if t == '?': fig.append('?'); continue
        for ch in t:
            if ch.isdigit(): fig.append(ch)
# target
dfile = {'R53': 'R53_decifrato_f500r.txt', 'R54': 'R54_decifrato_f500v.txt'}[rec]
lines = [l for l in (T / 'texts' / dfile).read_text(encoding='utf-8').splitlines() if not l.startswith('#')]
txt = ' '.join(lines)
txt = re.sub(r'\[(?:struck|margin|superscript)[^\]]*\]', ' ', txt)
txt = txt.replace('[', '').replace(']', '')
tgt = norm(txt)

N, L = len(fig), len(tgt)
INF = float('inf')
best = [[INF] * (L + 1) for _ in range(N + 1)]
back = [[None] * (L + 1) for _ in range(N + 1)]
best[0][0] = 0.0


def match(code_figs, code):
    """keys that match a figure string with '?' wildcards; an undotted 1xx also tries the dotted code (the
    transcription does not always mark the dot)"""
    if '?' not in code_figs:
        ks = [code] if code in KEY else []
        if len(code) == 3 and code[0] in '12' and 'D' + code[1:] in KEY: ks.append('D' + code[1:])
        return ks
    pat = re.compile('^' + code.replace('?', '.') + '$')
    return [k for k in KEY if pat.match(k)]


def elements(i):
    """(length in figures, code string) options starting at figure i"""
    out = []
    if fig[i] == 'D':
        if i + 2 < N: out.append((3, 'D' + fig[i + 1] + fig[i + 2]))
        return out
    for n in (1, 2, 3):
        if i + n > N: break
        s = ''.join(fig[i:i + n])
        if 'D' in s: break
        if n == 3 and not (s[:2] in ('10', '11', '49') or s.startswith('?') or s in KEY or ('D' + s[1:]) in KEY):
            continue
        out.append((n, s))
    return out


for i in range(N + 1):
    for j in range(L + 1):
        c = best[i][j]
        if c == INF: continue
        if j < L and c + 0.7 < best[i][j + 1]:
            best[i][j + 1] = c + 0.7; back[i][j + 1] = (i, j, 'extra letter', '', '')
        if i == N: continue
        if c + 1.2 < best[i + 1][j]:
            best[i + 1][j] = c + 1.2; back[i + 1][j] = (i, j, 'figure without letter', fig[i], '')
        for n, s in elements(i):
            ks = match(s, s)
            done = False
            for k in ks:
                for v in KEY[k]:
                    if tgt[j:j + len(v)] == v:
                        cc = c + (0.0 if '?' not in s else 0.3)
                        if cc < best[i + n][j + len(v)]:
                            best[i + n][j + len(v)] = cc; back[i + n][j + len(v)] = (i, j, 'keyed' if '?' not in s else 'keyed (wildcard)', k, v)
                        done = True
            for m_ in range(1, 6 if s.startswith('D') or n == 3 else 5):
                if j + m_ > L: break
                cost = c + (2.0 if ks else 1.0) + (0.15 * m_ if not s.startswith('D') else 0)
                if cost < best[i + n][j + m_]:
                    best[i + n][j + m_] = cost; back[i + n][j + m_] = (i, j, 'contradicts key' if ks else 'unkeyed', s, tgt[j:j + m_])

# trace
i, j, path = N, L, []
while (i, j) != (0, 0):
    pi, pj, kind, code, val = back[i][j]
    path.append((pi, i, pj, j, kind, code, val))
    i, j = pi, pj
path.reverse()
rows = ['n\tfigures\tcode\tkey value\tdecipherment letters\tkind']
by = collections.defaultdict(list)
cnt = collections.Counter()
for k, (i0, i1, j0, j1, kind, code, val) in enumerate(path):
    f = ''.join(fig[i0:i1])
    kv = '|'.join(sorted(KEY.get(code, []))) if code else ''
    rows.append(f'{k + 1}\t{f}\t{code}\t{kv}\t{tgt[j0:j1]}\t{kind}')
    cnt[kind] += 1
    if kind in ('unkeyed', 'contradicts key'):
        by[code].append(tgt[j0:j1] + '@' + tgt[max(0, j0 - 6):j1 + 6])
(T / 'texts' / f'{rec}_align.tsv').write_text('\n'.join(rows) + '\n', encoding='utf-8')
print(rec, 'figures', N, 'letters', L, 'cost', round(best[N][L], 1), dict(cnt))
for code, xs in sorted(by.items(), key=lambda x: -len(x[1])):
    print(' ', code, '|'.join(sorted(KEY.get(code, []))) or '-', len(xs), xs[:8])

# per word of the decipherment: the figures aligned to it and what the key gives for them (b21 word check)
words = []
pos = 0
for w in re.findall(r"[A-Za-zÀ-ÿ]+", txt):
    n = len(norm(w))
    words.append((w, pos, pos + n)); pos += n
wrows = ['word\tfigures\tkey gives\tagrees']
agree = 0
for w, a, b in words:
    fs, ks = [], []
    for (i0, i1, j0, j1, kind, code, val) in path:
        if j1 <= a or j0 >= b or i0 == i1: continue
        fs.append(''.join(fig[i0:i1]))
        kv = sorted(KEY.get(code, [])) if code else []
        ks.append(kv[0] if kv else '?')
    gives = ''.join(ks)
    ok = gives == norm(w)
    agree += ok
    wrows.append(f'{w}\t{" ".join(fs)}\t{gives}\t{"yes" if ok else "no"}')
(T / 'texts' / f'{rec}_words.tsv').write_text('\n'.join(wrows) + '\n', encoding='utf-8')
print('words', len(words), 'key gives the decipherment word exactly:', agree)
