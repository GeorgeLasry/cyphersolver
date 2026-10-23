"""r2l (23 Oct 2026): segment decoded letter strings into Italian words with the shared lang/ model.

    python research/reading_audit/r2l_seg.py <groups.txt> [top]

groups.txt, one group per line:  ID | left context | tokens | right context
  tokens: space-separated cipher signs as their candidate values, alternatives with '/', the key value first;
  '_' is the empty value (a null). A later alternative costs ALT nats, '_' costs NUL nats, a value marked with '!'
  (look-alike reading, e.g. 'x/!ri') costs LA nats. Example:  ad | d/s | i | o/u | ... | che
Scoring: lang/ model it-cinquecento (char 5-gram with spaces, early norm) over 'left + candidate + right', plus a
word-unigram term from the same corpora (it-renaissance, it-nunziature) with a penalty per out-of-vocabulary word.
Every letter of the candidate is carried by a sign (nothing is inserted), so a candidate is a full account of the group.
"""
import collections, itertools, math, os, pathlib, pickle, re, sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from lang import lm, corpora  # noqa: E402

ALT, NUL, LA, OOV = 1.5, 2.5, 3.0, 9.0
CACHE = ROOT / 'lang' / 'cache' / 'it-cinquecento.words.pkl'


def vocab():
    if CACHE.exists():
        return pickle.load(open(CACHE, 'rb'))
    t = lm.norm(corpora.text(['it-renaissance', 'it-nunziature']), 'early')
    c = collections.Counter(t.split())
    c = collections.Counter({w: n for w, n in c.items() if n >= 2})
    pickle.dump(c, open(CACHE, 'wb'))
    return c


def letter_words():
    """the writer's own words: the read parts of this target (boosted)."""
    c = collections.Counter()
    d = ROOT / 'targets' / 'buda1489'
    for f in ['plain267.txt', 'v2831_r2e_reading.md', 'r1098_v3_reading.md']:
        p = d / f
        if p.exists():
            t = re.sub(r'\[[^\]]*\]', ' ', p.read_text(encoding='utf8'))
            c.update(lm.norm(t, 'early').split())
    return c


M = lm.load('it-cinquecento')                     # spaces, order 5
M_NS = lm.load('it-cinquecento', spaces=False)
V = vocab(); N = sum(V.values())
L = letter_words()


def wscore(w):
    n = V.get(w, 0) + 20 * L.get(w, 0)
    if n:
        return math.log(n / N)
    return M.score(' ' + w + ' ') - OOV


def segment(s, k=6):
    """k best segmentations of s by word unigram (DP with k-best lists)."""
    n = len(s)
    best = [[] for _ in range(n + 1)]
    best[0] = [(0.0, [])]
    for i in range(1, n + 1):
        cand = []
        for j in range(max(0, i - 18), i):
            w = s[j:i]
            ws = wscore(w)
            for sc, ws_ in best[j]:
                cand.append((sc + ws, ws_ + [w]))
        cand.sort(key=lambda x: -x[0])
        best[i] = cand[:k]
    return best[n]


def parse(tok):
    out = []
    for i, a in enumerate(tok.split('/')):
        cost = 0.0 if i == 0 else ALT
        if a.startswith('!'):
            a, cost = a[1:], LA
        if a == '_':
            a, cost = '', (0.0 if i == 0 else NUL)
        out.append((a, cost))
    return out


def lattice(toks, beam=4000):
    states = [('', 0.0, ())]
    for t in toks:
        nxt = []
        for s, c, ch in states:
            for a, ac in parse(t):
                nxt.append((s + a, c + ac, ch + (a,)))
        if len(nxt) > beam:
            nxt.sort(key=lambda x: -(M_NS.score(x[0]) - x[1]))
            nxt = nxt[:beam]
        states = nxt
    return states


def run(line, top=8):
    gid, left, toks, right = [x.strip() for x in line.split('|')]
    left, right = lm.norm(left, 'early'), lm.norm(right, 'early')
    res = []
    seen = set()
    for s, c, ch in lattice(toks.split()):
        if not s:
            continue
        for us, words in segment(s, 4):
            key = ' '.join(words)
            if key in seen:
                continue
            seen.add(key)
            full = ' '.join(x for x in (left, key, right) if x)
            ctx = ' '.join(x for x in (left, right) if x)
            lmsc = M.score(' ' + full + ' ') - (M.score(' ' + ctx + ' ') if ctx else 0)
            oov = sum(1 for w in words if not (V.get(w) or L.get(w)))
            res.append((lmsc - OOV * oov - c, key, oov, c, ch))
    res.sort(key=lambda x: -x[0])
    print(f'== {gid}  [{left}] {toks} [{right}]')
    for sc, key, oov, c, ch in res[:top]:
        print(f'  {sc:8.1f}  oov={oov} alt={c:.1f}  {key}')
    return res[:top]


if __name__ == '__main__':
    top = int(sys.argv[2]) if len(sys.argv) > 2 else 8
    for line in pathlib.Path(sys.argv[1]).read_text(encoding='utf8').splitlines():
        if line.strip() and not line.startswith('#'):
            run(line, top)
