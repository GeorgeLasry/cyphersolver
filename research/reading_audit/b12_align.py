"""b12: align a key decode (b12_dec.parse) with a contemporary clear decipherment, word by word.
Each clear word is reported as carried by letters (=), by a code group (<nnnn>), partly (~) or not at all (!).
usage: b12_align.py <DOC transcription> <decipherment.txt> [out.tsv]"""
import re, sys, unicodedata
sys.path.insert(0, __import__('os').path.dirname(__import__('os').path.abspath(__file__)))
from b12_dec import parse, parse_lasry
def norm(s):
    s = unicodedata.normalize('NFD', s.lower())
    s = ''.join(c for c in s if not unicodedata.combining(c))
    return s.replace('j', 'i').replace('v', 'u').replace('y', 'i')
def clear_words(path):
    txt = ' '.join(l.rstrip() for l in open(path, encoding='utf8') if not l.startswith('#'))
    txt = re.sub(r'-\s+', '', txt); txt = re.sub(r'\[struck[^\]]*\]', ' ', txt)
    words = []
    for w in re.findall(r"[^\s]+", txt):
        for part in re.split(r"(?<=')", w):
            n = re.sub(r'[^a-z]', '', norm(part))
            if part.strip(): words.append((part, n))
    return words
def align(toks, words):
    chars = []; owner = []
    for wi, (w, n) in enumerate(words):
        for c in n: chars.append(c); owner.append(wi)
    bound = set(); pos = 0
    for wi, (w, n) in enumerate(words):
        pos += len(n); bound.add(pos)
    bound.add(0)
    T = [(g, norm(p).replace('u/u', 'u')) for g, p in toks if p not in ('·', '|')]
    N, M = len(T), len(chars); INF = 1e9
    D = [[INF] * (M + 1) for _ in range(N + 1)]; B = [[None] * (M + 1) for _ in range(N + 1)]
    D[0][0] = 0
    for i in range(N + 1):
        for j in range(M + 1):
            d = D[i][j]
            if d >= INF: continue
            if j < M and d + 1 < D[i][j+1]: D[i][j+1] = d + 1; B[i][j+1] = (i, j, 'skipc')
            if i == N: continue
            g, s = T[i]
            if g.startswith('2') and len(g) == 4:
                for k in range(0, min(28, M - j) + 1):
                    c = d + 0.6 + (0 if (j + k) in bound else 1.5) + (0 if j in bound else 1.5) + (0.8 if k == 0 else 0)
                    if c < D[i+1][j+k]: D[i+1][j+k] = c; B[i+1][j+k] = (i, j, 'code')
            else:
                s2 = re.sub(r'[^a-z]', '', s)
                L = len(s2)
                if L == 0:
                    if d < D[i+1][j]: D[i+1][j] = d; B[i+1][j] = (i, j, 'none')
                    continue
                for L2 in {L, L - 1, L + 1} if L > 1 else {L, L + 1}:
                    if L2 < 1 or j + L2 > M: continue
                    seg = ''.join(chars[j:j+L2])
                    mm = sum(a != b for a, b in zip(s2, seg)) + abs(L - L2)
                    c = d + mm * 1.0
                    if c < D[i+1][j+L2]: D[i+1][j+L2] = c; B[i+1][j+L2] = (i, j, 'pl')
                # double consonant in clear not written in cipher
                if d + 1.2 * L < D[i+1][j]: D[i+1][j] = d + 1.2 * L; B[i+1][j] = (i, j, 'skipt')
    i, j = N, M; path = []
    while (i, j) != (0, 0):
        pi, pj, kind = B[i][j]; path.append((pi, pj, i, j, kind)); i, j = pi, pj
    path.reverse()
    cov = [dict(ok=0, n=len(n), codes=[], toks=[]) for w, n in words]
    for pi, pj, i, j, kind in path:
        if kind == 'skipc': continue
        g, s = T[pi]
        span = range(pj, j)
        for wi in sorted({owner[x] for x in span}):
            cov[wi]['toks'].append(g)
        if kind == 'code':
            for wi in sorted({owner[x] for x in span}): cov[wi]['codes'].append(g)
        elif kind == 'pl':
            s2 = re.sub(r'[^a-z]', '', s)
            for a, x in zip(s2, span):
                if a == chars[x]: cov[owner[x]]['ok'] += 1
    return cov, D[N][M]
if __name__ == '__main__':
    toks = parse_lasry(sys.argv[1][6:]) if sys.argv[1].startswith('lasry:') else parse(sys.argv[1]); words = clear_words(sys.argv[2])
    cov, cost = align(toks, words)
    rows = []
    for (w, n), c in zip(words, cov):
        if c['codes']: st = '<%s>' % ','.join(dict.fromkeys(c['codes'])); st = ('=' if c['ok'] >= max(1, len(n) - 1) else '') + st
        elif c['n'] == 0: st = '='
        elif c['ok'] >= max(1, len(n) - 1) or (len(n) >= 4 and c['ok'] >= 0.7 * len(n)): st = '='
        elif c['ok'] > 0: st = '~%d/%d' % (c['ok'], len(n))
        else: st = '!'
        rows.append((w, st, ' '.join(c['toks'])))
    out = open(sys.argv[3], 'w', encoding='utf8') if len(sys.argv) > 3 else sys.stdout
    print('# cost %.1f; words %d; letters %d, codes %d, partial %d, unmatched %d' % (cost, len(rows),
        sum(r[1] == '=' for r in rows), sum('<' in r[1] for r in rows), sum(r[1].startswith('~') for r in rows), sum(r[1] == '!' for r in rows)), file=out)
    for r in rows: print('\t'.join(r), file=out)
