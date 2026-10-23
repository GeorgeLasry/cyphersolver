"""r2p (23 Oct 2026), morosini1588: list every hole of a reading with the figures that stand in it.

    python research/reading_audit/r2p_holes.py R18 [--ctx 2]

Aligns texts/<R>_reading.md page by page with DECODE's transcription (reread_b00_align.py), then for every [...],
[NNN], [?word] and [word] prints the page, the transcription line(s), the figures between the last carried word
before it and the first carried word after it (the hole's figures), and the context words. The figures are what to
look at on the image (cancellation strokes first), then to parse with r2d_mparse.py.
"""
import argparse, inspect, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import reread_b00_align as A  # noqa: E402

src = inspect.getsource(A.align)
src = src.replace("    i, j = endi, m\n    while (i, j) in back:\n        pi, pj, info = back[(i, j)]",
                  "    i, j = endi, m\n    steps = []\n    while (i, j) in back:\n        pi, pj, info = back[(i, j)]\n        steps.append((pi, i, pj, j, info[0]))")
src = src.replace("return umatch, uslip, endv, endi", "return umatch, uslip, endv, endi, steps[::-1]")
ns = dict(A.__dict__)
exec(src, ns)
align = ns['align']


def fig_str(F, a, b):
    out, ln = [], None
    for x in F[a:b]:
        if ln is not None and x['line'] != ln:
            out.append('|')
        ln = x['line']
        out.append(x['val'] + ('^.' if x['kind'] == 'N' else ''))
    return ' '.join(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('rec'); ap.add_argument('--ctx', type=int, default=2); ap.add_argument('--reading')
    a = ap.parse_args()
    rpath = a.reading or os.path.join(A.D.TDIR, 'texts', f'{a.rec}_reading.md')
    pages = A.page_items(a.rec)
    merged, order = {}, []
    for p, s in A.segments(A.body(rpath)):
        if p is None:
            continue
        k = p.lstrip('0').lower()
        if k not in merged:
            order.append(k); merged[k] = ''
        merged[k] += ' ' + s
    n_h = 0
    for key in order:
        if key not in pages:
            print(f'== {key}: not in transcription'); continue
        words, U = A.tokenize(merged[key])
        F = pages[key]
        res = align(F, U, words) or align(F, U, words, band=600)
        if res is None:
            print(f'== {key}: no alignment'); continue
        steps = res[4]
        # figure span per unit index
        fs = {}
        for pi, i, pj, j, k in steps:
            for t in range(pj, max(pj + 1, j)):
                if pi < i and pj < j or (k == 'hole' and pj < j):
                    s0, s1 = fs.get(t, (pi, i))
                    fs[t] = (min(s0, pi), max(s1, i))
        def wspan(w):
            sp = [fs[t] for t in range(w['start'], w['end']) if t in fs and fs[t][0] < fs[t][1]]
            if not sp:
                return None
            return min(s[0] for s in sp), max(s[1] for s in sp)
        carried = [i for i, w in enumerate(words) if w['kind'] == 'word' and '[' not in w['text'] and wspan(w)]
        for wi, w in enumerate(words):
            t = w['text']
            if not (w['kind'] in ('hole', 'code', 'partly', 'supplied') or '[' in t):
                continue
            prev = [c for c in carried if c < wi]; nxt = [c for c in carried if c > wi]
            a0 = wspan(words[prev[-1]])[1] if prev else 0
            b0 = wspan(words[nxt[0]])[0] if nxt else len(F)
            lines = sorted(set(F[x]['line'] for x in range(a0, b0))) if b0 > a0 else \
                ([F[min(a0, len(F) - 1)]['line']] if F else [])
            c0 = max(0, wi - a.ctx); c1 = min(len(words), wi + a.ctx + 1)
            ctx = ' '.join(x['text'] for x in words[c0:wi]) + ' <<' + t + '>> ' + ' '.join(x['text'] for x in words[wi + 1:c1])
            n_h += 1
            print(f'{key} l.{",".join(map(str, lines))}\t{ctx}\n      figs: {fig_str(F, a0, b0) if b0 > a0 else "(none)"}')
    print(f'TOTAL holes/marked words: {n_h}')


if __name__ == '__main__':
    main()
