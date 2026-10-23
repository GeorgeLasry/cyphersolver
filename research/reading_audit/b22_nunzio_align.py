"""b22: align Lasry's decode rows of nunzio1718 (lasry/364D-<n>.txt: DECODE's figure groups with Lasry's values) with the
contemporary interlinear decipherment transcribed from the images (lasry/<R>_decifrato.txt), letter by letter.

    python -X utf8 research/reading_audit/b22_nunzio_align.py R154|R173

Groups: as segmented in Lasry's rows (two figures; four for nomenclator codes 4xxx; 3 = null). Values: Lasry's row value;
codes he left open (<4xxx>) take key_extra.txt where it has them; 'NN?' groups are unread. 'a/b' = either.
Costs: a group whose value is the decipherment's letters 0 (nomenclator: 0 when equal, 0.3 when the decipherment's
abbreviation shares its first two letters); a two-figure group that gives the letters only if one figure is read as
its look-alike (1/7, 3/8, 5/6, 0/6, 4/9, 2/7, 0/9, 1/4, 2/3; for a four-figure code, a code whose value begins with the same three letters) 0.6 ('look-alike'); an unread group standing for 1-4 letters (codes 1-20) 1;
a keyed group standing for other letters 2 ('contradicts'); a decipherment letter with no group (the cipher spells
one consonant where the decipherer writes two; words he adds) 0.7; a group with no letter 1.2; a null 0.
Writes lasry/<R>_align.tsv (group by group) and lasry/<R>_words.tsv (word by word, with what carries each word).
"""
import collections, json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
T = ROOT / 'targets' / 'nunzio1718'
R = sys.argv[1]
N = {'R154': '1', 'R173': '20'}[R]


def norm(s):
    s = s.lower().replace('j', 'i').replace('v', 'u')
    for a, b in (('àá', 'a'), ('èé', 'e'), ('ìí', 'i'), ('òó', 'o'), ('ùú', 'u')):
        s = re.sub('[' + a + ']', b, s)
    return re.sub(r'[^a-z]', '', s)


# key: Lasry's sheet (code -> values), for the look-alike test
KEY = collections.defaultdict(set)
for ln in open(T / 'decode' / 'keep' / 'lasry_key_S364.txt', encoding='utf-8', errors='replace'):
    m = re.match(r'^([\d|]+)\s*-\s*(.+)$', ln.strip())
    if m:
        for c in m.group(1).split('|'):
            for v in m.group(2).split('|'): KEY[c].add(norm(v))
extra = {}
for ln in open(T / 'key_extra.txt', encoding='utf-8'):
    m = re.match(r'^(\d{4})\s*=\s*(.+)$', ln.strip())
    if m: extra[m.group(1)] = m.group(2).strip()

# b22 key changes (key_b22.tsv, status adopted) override Lasry's row values
B22 = {}
for ln in open(T / 'key_b22.tsv', encoding='utf-8'):
    f = ln.rstrip('\n').split('\t')
    if len(f) >= 4 and f[3] == 'adopted': B22[f[0]] = norm(f[2])
for c, v in B22.items(): KEY[c] = {v}

# groups from Lasry's rows
L = (T / 'lasry' / f'364D-{N}.txt').read_text(encoding='utf-8', errors='replace').splitlines()


def cols(a):
    starts = []; prev_end = -2
    for m in re.finditer(r'\S+', a):
        if m.start() > prev_end + 1: starts.append(m.start())
        prev_end = m.end() - 1
    starts.append(len(a)); return starts


G = []   # (figures, set of values or None for unread, is_code)
for i in range(len(L) - 1):
    a, b = L[i], L[i + 1]
    if not (a.rstrip().endswith('|') and b.rstrip().endswith('|')) or not re.match(r'^\s*\d', a): continue
    s = cols(a)
    for j in range(len(s) - 1):
        ct = a[s[j]:s[j + 1]].strip(); p = b[s[j]:s[j + 1]].strip() if s[j] < len(b) else ''
        if ct in ('|', ''): continue
        code = bool(re.fullmatch(r'4\d{3}', ct))
        if ct in B22: G.append((ct, {B22[ct]}, code)); continue
        if p == '_': G.append((ct, {''}, False)); continue
        if re.fullmatch(r'<\d{4}>', p):
            G.append((ct, {norm(extra[ct])} if ct in extra else None, True)); continue
        if re.fullmatch(r'\d+\?|\S*\?', p): G.append((ct, None, code)); continue
        G.append((ct, {norm(x) for x in p.split('/') if norm(x)} or {''}, code))

# decipherment
txt = []
for ln in (T / 'lasry' / f'{R}_decifrato.txt').read_text(encoding='utf-8').splitlines():
    if ln.startswith('#') or not ln.strip(): continue
    ln = re.sub(r'^\d+\s*', '', ln)
    if '[clear]' in ln: continue
    ln = re.sub(r'\[(?:struck|figure|blot)[^\]]*\]', ' ', ln)
    ln = ln.replace('[?', '').replace('[', '').replace(']', '')
    txt.append(ln)
txt = ' '.join(txt)
tgt = norm(txt)
LOOK = {'1': '74', '7': '12', '3': '82', '8': '3', '5': '6', '6': '50', '0': '69', '4': '91', '9': '40', '2': '73'}


def look(ct, letters):
    if len(ct) not in (2, 4): return None
    for k in range(len(ct)):
        for alt in LOOK.get(ct[k], ''):
            c2 = ct[:k] + alt + ct[k + 1:]
            vals = KEY.get(c2, ())
            if letters in vals: return c2
            if len(ct) == 4 and len(letters) >= 3 and any(v[:3] == letters[:3] for v in vals): return c2
    return None


n, Lt = len(G), len(tgt)
INF = float('inf')
best = [[INF] * (Lt + 1) for _ in range(n + 1)]
back = [[None] * (Lt + 1) for _ in range(n + 1)]
best[0][0] = 0.0
for i in range(n + 1):
    for j in range(Lt + 1):
        c = best[i][j]
        if c == INF: continue
        if j < Lt and c + 0.7 < best[i][j + 1]:
            best[i][j + 1] = c + 0.7; back[i][j + 1] = (i, j, 'extra letter', '')
        if i == n: continue
        ct, vals, code = G[i]
        if vals == {''}:
            if c < best[i + 1][j]: best[i + 1][j] = c; back[i + 1][j] = (i, j, 'null', '')
            continue
        if c + 1.2 < best[i + 1][j]:
            best[i + 1][j] = c + 1.2; back[i + 1][j] = (i, j, 'group without letter', '')
        maxm = 20 if code else 4
        for m_ in range(1, maxm + 1):
            if j + m_ > Lt: break
            seg = tgt[j:j + m_]
            if vals is None:
                cost, kind = 1.0, 'unread'
            elif seg in vals:
                cost, kind = 0.0, 'keyed'
            elif code and any(v[:2] == seg[:2] and (v.startswith(seg) or seg.startswith(v[:3])) for v in vals):
                cost, kind = 0.3, 'code abbreviated'
            elif look(ct, seg):
                cost, kind = 0.6, 'look-alike ' + look(ct, seg)
            else:
                if m_ > (6 if code else 3): continue
                cost, kind = 2.0, 'contradicts'
            if c + cost < best[i + 1][j + m_]:
                best[i + 1][j + m_] = c + cost; back[i + 1][j + m_] = (i, j, kind, seg)

i, j, path = n, Lt, []
while (i, j) != (0, 0):
    pi, pj, kind, seg = back[i][j]
    path.append((pi, i, pj, j, kind)); i, j = pi, pj
path.reverse()
rows = ['n\tfigures\tvalue\tdecipherment letters\tkind']
cnt = collections.Counter(); letters = collections.Counter()
for k, (i0, i1, j0, j1, kind) in enumerate(path):
    f = G[i0][0] if i1 > i0 else ''
    v = '|'.join(sorted(G[i0][1])) if i1 > i0 and G[i0][1] is not None else ('?' if i1 > i0 else '')
    rows.append(f'{k + 1}\t{f}\t{v}\t{tgt[j0:j1]}\t{kind}')
    cnt[kind.split(' ')[0] if kind.startswith('look') else kind] += 1
    letters[kind.split(' ')[0] if kind.startswith('look') else kind] += j1 - j0
(T / 'lasry' / f'{R}_align.tsv').write_text('\n'.join(rows) + '\n', encoding='utf-8')
print(R, 'groups', n, 'letters', Lt, 'cost', round(best[n][Lt], 1))
print(' groups by kind', dict(cnt))
print(' letters by kind', dict(letters), 'share keyed+code', round((letters['keyed'] + letters['code abbreviated']) / Lt, 3))

# word by word
words = []; pos = 0
for w in re.findall(r"[A-Za-zÀ-ÿ']+", txt):
    for part in w.split("'"):
        k = len(norm(part))
        if k: words.append((part, pos, pos + k)); pos += k
wrows = ['word\tfigures\tkinds\tcarried']
carried = collections.Counter()
for w, a, b in words:
    fs, kinds = [], []
    for (i0, i1, j0, j1, kind) in path:
        if j1 <= a or j0 >= b: continue
        if i1 > i0: fs.append(G[i0][0])
        kinds.append(kind.split(' ')[0])
    good = sum(1 for (i0, i1, j0, j1, kind) in path for q in range(max(a, j0), min(b, j1))
               if kind in ('keyed', 'code abbreviated') or kind.startswith('look'))
    st = 'figures' if good == b - a else ('partly' if good >= (b - a) / 2 else 'decipherment')
    carried[st] += 1
    wrows.append(f'{w}\t{" ".join(fs)}\t{",".join(sorted(set(kinds)))}\t{st}')
(T / 'lasry' / f'{R}_words.tsv').write_text('\n'.join(wrows) + '\n', encoding='utf-8')
print(' words', len(words), dict(carried))
