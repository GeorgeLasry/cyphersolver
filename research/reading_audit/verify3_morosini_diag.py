"""VERIFY_BRIEF pass 3, morosini1588: for each word reread_b00_align.py flags (a letter with no figure), show the
figures the alignment put under it and the figures left over ('extra', including dotted groups) right around it.

    PYTHONUTF8=1 python research/reading_audit/verify3_morosini_diag.py R44 [R..]

Line format: page  word  |prev word figs| [word figs] |next word figs|  extras-before / extras-after  (dotted = .NNN)
A letter with no figure next to a left-over dotted group whose digits spell it (e.g. .525 = c+e) is carried by a
figure group with a spurious dot; a letter with nothing left over beside it is not carried.
"""
import os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
src = open(os.path.join(HERE, 'reread_b00_align.py'), encoding='utf-8').read()
src = src.replace("                umatch[t] = k\n", "                umatch[t] = k\n                PATH.append((pi, i, pj, j, k))\n")
src = src.replace("    umatch = ['?'] * m\n", "    umatch = ['?'] * m\n    PATH.clear()\n")
src = src.replace("if __name__ == '__main__':\n    main()", '')
G = {'__name__': 'a3', '__file__': os.path.join(HERE, 'reread_b00_align.py'), 'PATH': []}
exec(compile(src, 'reread_b00_align_traced', 'exec'), G)
PATH = G['PATH']


def fig(x):
    return ('.' if x['kind'] == 'N' else '') + x['val']


def run(rec):
    rpath = os.path.join(G['D'].TDIR, 'texts', f'{rec}_reading.md')
    pages = G['page_items'](rec)
    merged, order = {}, []
    btxt = re.sub(r'\[f\.\s*(\d+[rv]),[^\]]*\]', lambda m: '[f. ' + m.group(1) + ']', G['body'](rpath))
    for p, s in G['segments'](btxt):
        if p is None:
            continue
        k = p.lstrip('0').lower()
        if k not in merged:
            order.append(k); merged[k] = ''
        merged[k] += ' ' + s
    if MERGE:
        # one alignment over the whole letter, pages in reading order (words split across a page break stay whole)
        txt, F = '', []
        for key in order:
            if key in pages:
                txt += ' ' + merged[key]
                F += [dict(x, line=f"{key}:{x['line']}") for x in pages[key]]
        pages, merged, order = {'all': F}, {'all': txt}, ['all']
    for key in order:
        if key not in pages:
            continue
        words, U = G['tokenize'](merged[key])
        F = pages[key]
        res = G['align'](F, U, words, band=400 if MERGE else 260) or G['align'](F, U, words, band=900)
        if not res:
            print(key, 'no alignment'); continue
        path = list(reversed(PATH))
        # every figure index -> (unit index or None)
        fowner = {}
        extras = []
        for (i0, i1, j0, j1, k) in path:
            if j1 > j0:
                for f in range(i0, i1):
                    fowner[f] = j0
        # rebuild extras (figures consumed with no unit): walk full back chain is not stored; infer: figures not owned
        owned = set(fowner)
        fl = G['report'](rec, words, U, res, key)
        flagged = {f[1].split(' ')[0] for f in fl if f[2]}
        umatch = res[0]
        # unit -> figure span
        uspan = {}
        for (i0, i1, j0, j1, k) in path:
            for t in range(j0, j1):
                uspan[t] = (i0, i1)
        for wi, w in enumerate(words):
            if w['kind'] != 'word':
                continue
            us = [t for t in range(w['start'], w['end']) if U[t][3] == 'n']
            if not us or not any(umatch[t] == 'nofig' for t in us):
                continue
            spans = [uspan[t] for t in range(w['start'], w['end']) if t in uspan and uspan[t][1] > uspan[t][0]]
            lo = min((s[0] for s in spans), default=None)
            hi = max((s[1] for s in spans), default=None)
            if lo is None:
                # find neighbours
                prev = [uspan[t] for t in range(0, w['start']) if t in uspan and uspan[t][1] > uspan[t][0]]
                lo = hi = prev[-1][1] if prev else 0
            a, b = max(0, lo - 8), min(len(F), hi + 8)
            show = []
            for f in range(a, b):
                s = fig(F[f])
                if f not in owned:
                    s = '{' + s + '}'
                if f == lo:
                    show.append('[')
                show.append(s)
                if f == hi - 1:
                    show.append(']')
            if lo == hi:
                show.insert(min(len(show), lo - a), '[]')
            ctx = ' '.join(x['text'] for x in words[max(0, wi - 3):wi + 4])
            shown = ''.join(U[t][1].upper() if umatch[t] == 'nofig' and U[t][3] == 'n' else U[t][1]
                            for t in range(w['start'], w['end']))
            # classify: each letter without a figure, is its code in a left-over figure group beside the word?
            left = [F[f] for f in range(max(0, lo - 3), min(len(F), hi + 3)) if f not in owned]
            ld = ''.join(x['val'] for x in left)
            verdict = 'CARRIED' if left else 'NOT'
            for t in range(w['start'], w['end']):
                if umatch[t] == 'nofig' and U[t][3] == 'n':
                    codes = G['D'].LET.get(U[t][1], '').split()
                    if not any(c in ld for c in codes):
                        verdict = 'NOT'
            print(f'{verdict:7s} {rec} {key} l.{F[min(lo, len(F)-1)]["line"]}  {w["text"]:14s} {shown:14s} :: {" ".join(show)}   «{ctx}»')


MERGE = '--merge' in sys.argv
for r in [a for a in sys.argv[1:] if not a.startswith('--')]:
    run(r)
