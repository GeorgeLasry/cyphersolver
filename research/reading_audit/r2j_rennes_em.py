"""r2j (rennes1563): hard-EM alignment of the 15 Dec 1562 cipher (Colbert 390 pp. 117-118, sign transcription
targets/rennes1563/c390_1562-12-15_cipher.txt) with La Ferriere I 449-450 (printed from the decipherment joined to the
letter; targets/rennes1563/c390_1562-12-15_plain.txt). Adapted from targets/matignon1586c3/f276/scripts/align_em.py:
tokens are free names; a token may also emit one of a list of strings (code words, doubled letters).

    python research/reading_audit/r2j_rennes_em.py [iters]
Prints the learned emission table and the alignment line by line.
"""
import re, sys, unicodedata, collections, pathlib
import numpy as np
T = pathlib.Path(__file__).resolve().parents[2] / 'targets' / 'rennes1563'
A = 'abcdefghilmnopqrstuxyz'; NUL = '-'
INS = 4.0; WCOST = 0.5; NULL_MIN = 2.5
# prior single-letter values: the working key (glyphs.py) plus what the hand shows on pp. 117-118 (read off by eye)
PRIOR = {'th': 'm', 'ds': 'r', 'at': 'g', 'xi': 'e', 'b': 'p', 'x1': 'e', 'd': 'e', 'zs': 's', '3': 'c', 'a1': 'n',
         'c': 's', 'io': 'i', '9': 'n', 'plus': 'f|x|s', 'G': 't', 'et': 't', 'C': 'o|h', 'mu': 'u', 'S': 'a', 'R': 'r',
         'g': 'o', 'ii': 'b', 'La': 'd', 'Y': 'd', 'z': 'a', 'sig': 'l', 'lam': 'u', 'dl': 'b', 'tz': 'z', 'mJ': 'i|m',
         'pq': 'p', 'qm': 'm', 'zz': 's', 'E': 'h', 'sh': 'y', 'qn': '<null>', 'cdo': '<null>', 'ng': '<null>',
         'dag': '<null>', 'ep': '<null>', 'ss': 'l', 'kk': 'z', 'mS': 'p'}
WORDS = {'qq': ['que'], 'Ls': ['dict'], 'yy': ['leroydesromains', 'roydesromains'], 'tu': ['faict'], 'ca': ['faire'],
         'pl': ['bien'], '8': ['luy'], 'A': ['mais'], 'Vb': ['qui'], 'Y2': ['qui'], 'lt': ['vous'], 'gt': ['nous'],
         '7': ['nous'], 'aL': ['par'], 'TT': ['pour'], 'tp': ['et'], 'sh': ['et', 'est'], 'll': ['ss'], 'N': ['ll'],
         'rr': ['rr'], 'E': ['ff'], 'ff': ['ff'], 'fq': ['qui'], 'Cm': ['a'], 'da': ['allemaigne'], 'cdo': ['com', 'con']}


def norm(t):
    t = unicodedata.normalize('NFD', t); t = ''.join(c for c in t if unicodedata.category(c) != 'Mn')
    t = t.lower().replace('v', 'u').replace('j', 'i').replace('w', 'uu').replace('k', 'c')
    return re.sub(r'[^a-z]+', '', t)


def load():
    toks = []; lines = []
    for l in open(T / 'c390_1562-12-15_cipher.txt', encoding='utf8'):
        m = re.match(r'^(L\d+):\s*(.*)$', l.strip())
        if m:
            ts = m.group(2).split(); lines.append((m.group(1), ts)); toks += ts
    P = ''.join(norm(l) for l in open(T / 'c390_1562-12-15_plain.txt', encoding='utf8') if not l.startswith('#'))
    return lines, toks, P


def run(iters=10):
    lines, toks, P = load()
    types = sorted(set(toks)); idx = {t: i for i, t in enumerate(types)}; L = len(A) + 1
    prior = np.full((len(types), L), 0.3)
    for t, i in idx.items():
        v = PRIOR.get(t)
        if v == '<null>': prior[i, L - 1] += 6
        elif v:
            for a in v.split('|'): prior[i, A.index(a)] += 6
    counts = np.zeros_like(prior)

    def costs():
        tot = counts + prior * 0.9 + 0.3; p = tot / tot.sum(1, keepdims=True); c = -np.log(p)
        nn = prior[:, L - 1] < 1; c[nn, L - 1] = np.maximum(c[nn, L - 1], NULL_MIN); return c
    Pidx = np.array([A.index(ch) for ch in P]); m = len(P); INF = 1e9
    starts = {}
    for t in types:
        for word in WORDS.get(t, []):
            starts[word] = np.array([j for j in range(m - len(word) + 1) if P.startswith(word, j)], dtype=int)
    for it in range(iters):
        C = costs(); n = len(toks)
        rows = np.full((n + 1, m + 1), INF); rows[0, :] = 0
        back = np.zeros((n + 1, m + 1), dtype=np.int8); wl = np.zeros((n + 1, m + 1), dtype=np.int16)
        for i, t in enumerate(toks):
            ti = idx[t]; prev = rows[i]
            cur = prev + C[ti, L - 1]; bk = np.full(m + 1, 2, dtype=np.int8); w = np.zeros(m + 1, dtype=np.int16)
            ce = prev[:-1] + C[ti, Pidx]; b = ce < cur[1:]; cur[1:][b] = ce[b]; bk[1:][b] = 1
            for word in WORDS.get(t, []):
                js = starts[word]; k = len(word)
                if len(js):
                    cw = prev[js] + WCOST; tgt = js + k; s = cw < cur[tgt]
                    cur[tgt[s]] = cw[s]; bk[tgt[s]] = 4; w[tgt[s]] = k
            j = np.arange(m + 1); run_ = np.minimum.accumulate(cur - j * INS) + j * INS
            b = run_ < cur - 1e-9; bk[b] = 3; cur = run_
            rows[i + 1] = cur; back[i + 1] = bk; wl[i + 1] = w
        j = int(np.argmin(rows[n])); total = rows[n, j]; i = n; path = []
        while i > 0:
            b = back[i, j]
            if b == 3: path.append(('ins', None, P[j - 1])); j -= 1
            elif b == 1: path.append(('emit', toks[i - 1], P[j - 1])); i -= 1; j -= 1
            elif b == 2: path.append(('null', toks[i - 1], '')); i -= 1
            elif b == 4: k = wl[i, j]; path.append(('word', toks[i - 1], P[j - k:j])); i -= 1; j -= k
            else: path.append(('ins', None, P[j - 1])); j -= 1
        path.reverse(); counts[:] = 0; words = collections.Counter()
        for op, t, l in path:
            if op == 'emit': counts[idx[t], A.index(l)] += 1
            elif op == 'null': counts[idx[t], L - 1] += 1
            elif op == 'word': words[(t, l)] += 1
        ne = sum(op == 'emit' for op, _, _ in path); ni = sum(op == 'ins' for op, _, _ in path)
        nn = sum(op == 'null' for op, _, _ in path)
        print(f'iter {it}: cost {total:.0f} emit {ne} ins {ni} null {nn} word {sum(words.values())}', file=sys.stderr)
    freq = collections.Counter(toks)
    print('token\tn\temissions')
    for t in sorted(types, key=lambda t: -freq[t]):
        c = counts[idx[t]]; top = sorted(((c[k], (A + NUL)[k]) for k in range(L) if c[k] > 0), reverse=True)
        ws = [f'={w}:{n}' for (tt, w), n in words.items() if tt == t]
        print(f'{t}\t{freq[t]}\t' + ' '.join(ws + [f'{l}:{int(n)}' for n, l in top]))
    print('\nALIGNMENT'); pos = 0
    for name, ts in lines:
        seg = []; k = 0
        while k < len(ts) and pos < len(path):
            op, t, l = path[pos]; pos += 1
            if op == 'ins': seg.append('+' + l); continue
            seg.append(f'{t}>{l or "-"}'); k += 1
        print(name, ' '.join(seg))


if __name__ == '__main__':
    run(int(sys.argv[1]) if len(sys.argv) > 1 else 10)
