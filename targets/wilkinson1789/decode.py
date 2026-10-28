"""Decode the Wilkinson dictionary/table code by alphabetical interpolation + a word trigram LM.

Both key parts are alphabetical: the numbered table [n]^ (about 1-1221, extras appended after)
and the dictionary (page, column, row). Known (code -> word) anchors from deciphered pages
bracket every unknown code; candidates are the corpus words whose alphabetical rank lies between
the bracketing anchors, weighted by distance from the linearly interpolated rank. A word trigram
LM (stupid backoff) over an English corpus then picks the sentence with beam search.

Usage:
  python decode.py eval              score on Chu et al.'s held-out LoC 3044-3045 excerpt
  python decode.py decode FILE [dict] decode a transcription file (dict: 1078 or 1096)
"""
import math, os, re, sys, collections, bisect

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, '..', '..')
CHU = os.environ.get('CHU', os.path.join(os.environ.get('TEMP', '.'), 'wilkinson'))

ROWS = {'1078': 29, '1096': 40}
TOK = re.compile(r"\[(\d+)\]\^|(\d+)\.\[(\d+)\]([-=])")


def code_of(tok):
    m = TOK.fullmatch(tok)
    if not m:
        return None
    if m.group(1):
        return ('T', int(m.group(1)))
    return ('D', int(m.group(2)), 1 if m.group(4) == '-' else 2, int(m.group(3)))


def dict_line(c, dict_id):
    _, p, col, r = c
    rows = ROWS[dict_id]
    return (p * 2 + (col - 1)) * rows + r


# ---------- anchors ----------

def load_wordbank(paths):
    out = []
    for path in paths:
        for line in open(path, encoding='utf-8', errors='replace'):
            if line.startswith('#') or '\t' not in line:
                continue
            parts = line.rstrip('\n').split('\t')
            tok, word = parts[0].strip(), parts[-1].strip()
            c = code_of(tok)
            if c and word and '?' not in word and re.fullmatch(r"[A-Za-z']+", word):
                out.append((c, word.lower()))
    return out


def lis(items, key):
    """Longest non-decreasing subsequence of items (already sorted by position) by key."""
    tails, prev, idx = [], [None] * len(items), []
    for i, it in enumerate(items):
        k = key(it)
        j = bisect.bisect_right([key(items[t]) for t in tails], k)
        if j > 0:
            prev[i] = tails[j - 1]
        if j == len(tails):
            tails.append(i)
        else:
            tails[j] = i
    seq, i = [], tails[-1] if tails else None
    while i is not None:
        seq.append(items[i]); i = prev[i]
    return seq[::-1]


def split_anchors(anchors):
    """Table anchors (n <= 1221) form one alphabetical chain; dictionary anchors split into the
    1078 book (pages to ~780, 29 rows) and the 1096 book (pages to ~430, 40 rows) by two LIS passes."""
    table = sorted({(c[1], w) for c, w in anchors if c[0] == 'T'})
    extras = {n: w for n, w in table if n > 1221}
    table = lis([(n, w) for n, w in table if n <= 1221], key=lambda x: x[1])
    d = sorted({(c, w) for c, w in anchors if c[0] == 'D'}, key=lambda x: (x[0][1], x[0][2], x[0][3]))
    big = [x for x in d if x[0][3] > 29]  # rows > 29 can only be the 1096 book
    first = lis([x for x in d if x[0][3] <= 29 or x in big], key=lambda x: x[1])
    rest = [x for x in d if x not in first]
    second = lis(rest, key=lambda x: x[1])
    # the chain that reaches the high pages is the 1078 book
    a, b = (first, second) if max(x[0][1] for x in first) > max(x[0][1] for x in second) else (second, first)
    a = [x for x in a if x[0][3] <= 29]
    return table, extras, {'1078': a, '1096': b}


# ---------- vocabulary and LM ----------

def corpus_tokens():
    paths = [os.path.join(ROOT, 'lang', 'corpora', 'en-gutenberg.txt')]
    for f in ('wikipedia-wilkinson.txt', 'wikipedia-washington.txt'):
        p = os.path.join(CHU, 'data', 'synthetic', f)
        if os.path.exists(p):
            paths.append(p)
    for p in paths:
        with open(p, encoding='utf-8', errors='replace') as fh:
            for line in fh:
                for w in re.findall(r"[a-z]+", line.lower()):
                    yield w


class LM:
    def __init__(self, toks):
        self.c1, self.c2, self.c3 = collections.Counter(), collections.Counter(), collections.Counter()
        a = b = '<s>'
        for w in toks:
            self.c1[w] += 1; self.c2[(b, w)] += 1; self.c3[(a, b, w)] += 1
            a, b = b, w
        self.n = sum(self.c1.values())

    def logp(self, a, b, w):
        if self.c3[(a, b, w)] and self.c2[(a, b)]:
            return math.log(self.c3[(a, b, w)] / self.c2[(a, b)])
        if self.c2[(b, w)] and self.c1[b]:
            return math.log(0.4 * self.c2[(b, w)] / self.c1[b])
        return math.log(0.16 * (self.c1[w] + 0.5) / self.n)


# ---------- candidates ----------

class Key:
    def __init__(self, anchors, vocab, pos, known=None):
        """anchors: list of (position, word) sorted by position; pos: function code -> position."""
        self.vocab = vocab                       # sorted list of words
        self.rank = {w: i for i, w in enumerate(vocab)}
        self.anc = [(p, self.rank[w]) for p, w in anchors if w in self.rank]
        self.exact = dict(known or {})
        self.pos = pos

    def candidates(self, code, k=40):
        p = self.pos(code)
        if p in self.exact:
            return [(w, -0.5 * i) for i, w in enumerate(self.exact[p])]
        ps = [a[0] for a in self.anc]
        i = bisect.bisect_left(ps, p)
        lo = self.anc[i - 1] if i > 0 else (0, 0)
        hi = self.anc[i] if i < len(self.anc) else (p + 1, len(self.vocab) - 1)
        if hi[0] == lo[0]:
            est = lo[1]
        else:
            est = lo[1] + (hi[1] - lo[1]) * (p - lo[0]) / (hi[0] - lo[0])
        span = max(hi[1] - lo[1], 1)
        sigma = max(span / max(hi[0] - lo[0], 1) * 1.5, 2.0)
        a, b = max(lo[1], int(est - 3 * sigma)), min(hi[1], int(est + 3 * sigma) + 1)
        out = [(self.vocab[r], -((r - est) / sigma) ** 2 / 2) for r in range(a, b + 1)]
        out.sort(key=lambda x: -x[1])
        return out[:k]


def build(dict_id, wordbank_paths, min_count=25):
    anchors = load_wordbank(wordbank_paths)
    table, extras, chains = split_anchors(anchors)
    toks = list(corpus_tokens())
    lm = LM(toks)
    words = {w for w, c in lm.c1.items() if c >= min_count and len(w) > 1 or w in ('a', 'i')}
    words |= {w for _, w in table} | {w for _, w in chains[dict_id]}
    vocab = sorted(words)
    votes = collections.defaultdict(collections.Counter)
    for c, w in anchors:
        votes[c][w] += 1
    tknown = {c[1]: [w for w, _ in v.most_common()] for c, v in votes.items() if c[0] == 'T'}
    chain_codes = {c for c, _ in chains[dict_id]}
    dknown = {dict_line(c, dict_id): [w for w, _ in v.most_common()] for c, v in votes.items()
              if c[0] == 'D' and (c in chain_codes or (dict_id == '1078') == (c[3] <= 29 and c not in {x for x, _ in chains['1096' if dict_id == '1078' else '1078']}))}
    tkey = Key([(n, w) for n, w in table], vocab, lambda c: c[1], tknown)
    dchain = sorted(((dict_line(c, dict_id), w) for c, w in chains[dict_id]))
    dkey = Key(dchain, vocab, lambda c: dict_line(c, dict_id), dknown)
    return dict(lm=lm, tkey=tkey, dkey=dkey, extras=extras, chains=chains, table=table)


# ---------- decoding ----------

def slots(text):
    """Cipher text -> list of slots: (kind, payload, suffix). '+x' attaches to the previous slot."""
    out = []
    for tok in text.split():
        if tok.startswith('+') and out:
            out[-1] = (out[-1][0], out[-1][1], out[-1][2] + tok[1:])
            continue
        c = code_of(tok)
        if c:
            out.append(('C', c, ''))
        elif re.fullmatch(r"[A-Za-z]+\.?", tok):
            out.append(('W', tok.lower().strip('.'), ''))
        else:
            out.append(('U', tok, ''))
    return out


def options(slot, M):
    kind, c, suf = slot
    if kind == 'W':
        return [(c, 0.0)]
    if kind == 'U':
        return [('?', 0.0)]
    if c[0] == 'T':
        if c[1] in M['extras']:
            return [(M['extras'][c[1]], 0.0)]
        if c[1] > 1221:
            return [('?', 0.0)]
        cand = M['tkey'].candidates(c)
    else:
        cand = M['dkey'].candidates(c)
    if suf:
        cand = [(inflect(w, suf), s) for w, s in cand]
    return cand


def inflect(w, suf):
    if suf in ('y',) and w == 'me':
        return 'my'
    if suf == 'n' and w == 'be':
        return 'been'
    if suf == 'ing':
        return (w[:-1] if w.endswith('e') else w) + 'ing'
    return w + suf


def beam(sl, M, width=64, prior_w=1.0):
    lm = M['lm']
    beams = [(0.0, '<s>', '<s>', [])]
    for s in sl:
        opts = options(s, M)
        nb = []
        for sc, a, b, hist in beams:
            for w, pr in opts:
                lp = lm.logp(a, b, w) if w != '?' else -8.0
                nb.append((sc + lp + prior_w * pr, b, w, hist + [w]))
        nb.sort(key=lambda x: -x[0])
        beams, seen = [], set()
        for x in nb:
            k = (x[1], x[2])
            if k in seen:
                continue
            seen.add(k); beams.append(x)
            if len(beams) >= width:
                break
    return beams[0][3]


def edit_distance(a, b):
    d = list(range(len(b) + 1))
    for i in range(1, len(a) + 1):
        prev, d[0] = d[0], i
        for j in range(1, len(b) + 1):
            cur = d[j]
            d[j] = min(d[j] + 1, d[j - 1] + 1, prev + (a[i - 1] != b[j - 1]))
            prev = cur
    return d[-1]


def main():
    wb = [os.path.join(CHU, 'wordbanks', f) for f in ('wordbank', 'wordbank.clean2', 'wordbank.miro')]
    if sys.argv[1] == 'eval':
        M = build('1078', wb)
        ct = open(os.path.join(CHU, 'data', 'eval', 'ciphertext.txt'), encoding='utf-8').read()
        gold = open(os.path.join(CHU, 'data', 'eval', 'plaintext.txt'), encoding='utf-8').read()
        out = []
        for line in ct.splitlines():
            out += beam(slots(line), M)
        g = [w for w in re.findall(r"[A-Za-z?]+", gold.lower())]
        acc = 1 - edit_distance(out, g) / len(g)
        print('tokens', len(g), 'accuracy %.3f' % acc)
        print(' '.join(out[:200]))
        print('chains: table', len(M['table']), {k: len(v) for k, v in M['chains'].items()})
    else:
        dict_id = sys.argv[3] if len(sys.argv) > 3 else '1078'
        M = build(dict_id, wb)
        for line in open(sys.argv[2], encoding='utf-8'):
            if TOK.search(line):
                print(' '.join(beam(slots(line), M)))
            else:
                print(line.rstrip())


if __name__ == '__main__':
    main()
