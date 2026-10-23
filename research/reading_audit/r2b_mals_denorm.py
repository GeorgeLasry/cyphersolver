"""r2b: undo the b08 spelling normalisation (b08_norm.MAP, and the hand list of HCP496) in the malsburg1637 readings.

    python r2b_mals_denorm.py <reading.md> <f0NN.txt ...> [--alt f0NN.txt ...] [--apply]

Each word of the '## Reading' body that is a normalised form (a value of the map) is restored to the writer's form the
figures (or the transcribed clear words) give at that point: the body is walked in order against the decode stream of
the transcription files (letters only, u/v and i/j/y merged, umlauts folded), and for each normalised word the
candidate whose folded form occurs next in the stream (and is followed soonest by the next body word) is taken.
--alt files (the writer's duplicate copy) are searched when a word is not found near the pointer. Prints every change;
--apply writes the body back. Words inside [ ], { }, < > are left alone (as b08_norm did).
"""
import re, sys, pathlib, unicodedata
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from b08_dec import load, dec  # noqa
from b08_norm import MAP  # noqa

HAND = {'hirnechst': 'hiernechst', 'alhir': 'alhier', 'nunmer': 'nunmehr', 'duppelt': 'doppelt', 'Konig': 'König',
        'Virtel': 'Viertel', 'Fridenstractaten': 'Friedenstractaten'}
INV = {}
for k, v in list(MAP.items()) + list(HAND.items()):
    if k != v:
        INV.setdefault(v, []).append(k)
T = pathlib.Path(__file__).resolve().parents[2] / 'targets' / 'malsburg1637'
WIN = 80


def fold(s):
    s = unicodedata.normalize('NFKD', s.lower())
    s = ''.join(c for c in s if not unicodedata.combining(c))
    s = s.replace('v', 'u').replace('j', 'i').replace('y', 'i').replace('ß', 'ss')
    return re.sub(r'[^a-z]', '', s)


def stream(files):
    s = ''
    for f in files:
        for line in load(T / f):
            if line.startswith('#'):
                continue
            d, _ = dec(line)
            s += fold(re.sub(r'\[[^\]]*\]', '', d))
    return s


def main(a):
    apply = '--apply' in a
    a = [x for x in a if x != '--apply']
    rd = a[0]
    if '--alt' in a:
        i = a.index('--alt'); files, alt = a[1:i], a[i + 1:]
    else:
        files, alt = a[1:], []
    S, A = stream(files), stream(alt) if alt else ''
    p = pathlib.Path(rd)
    t = p.read_text(encoding='utf8')
    m = re.search(r'(^## Reading[^\n]*\n)(.*?)(?=^## |\Z)', t, re.S | re.M)
    body = m.group(2)
    # tokens: words outside [ ] { } < > marks, with their spans
    masked = re.sub(r'\[[^\]]*\]|\{[^}]*\}|<[^>]*>', lambda mm: ' ' * len(mm.group(0)), body)
    toks = [(mm.start(), mm.end(), mm.group(0)) for mm in re.finditer(r"[^\W\d_]+", masked)]
    ptr, out, changes = 0, [], []
    for n, (s0, s1, w) in enumerate(toks):
        nxt = fold(toks[n + 1][2]) if n + 1 < len(toks) else ''
        forms = ([w] + INV[w]) if w in INV else [w]
        best = None
        for f in forms:
            ff = fold(f)
            if not ff:
                continue
            pos = S.find(ff, ptr)
            if pos < 0 or pos - ptr > WIN:
                continue
            end = pos + len(ff)
            gap = S.find(nxt, end) - end if nxt and S.find(nxt, end) >= 0 else 999
            key = (pos, gap if gap >= 0 else 999, -len(ff) if f == w else 0)
            if best is None or key < best[0]:
                best = (key, f, end)
        if best is None and w in INV and A:
            hits = [f for f in INV[w] if fold(f) and fold(f) in A]
            if hits and fold(w) not in A:
                best = ((0,), hits[0], ptr)
        if best is None:
            continue
        _, f, end = best
        ptr = max(ptr, end)
        if f != w:
            f = (f[0].upper() if w[:1].isupper() else f[0].lower()) + f[1:]
            out.append((s0, s1, f)); changes.append((w, f))
    for w, f in changes:
        print(f'  {w} -> {f}')
    print(rd, len(changes), 'restored')
    if apply and out:
        b = body
        for s0, s1, f in sorted(out, reverse=True):
            b = b[:s0] + f + b[s1:]
        p.write_text(t[:m.start(2)] + b + t[m.end(2):], encoding='utf8')


if __name__ == '__main__':
    main(sys.argv[1:])
