"""r2j (rennes1563): word lattice over Colbert 390 p. 139 (c390_p139_v4.txt) with the p.139 value table of
targets/rennes1563/measure.py (P139) widened by the values the 15 Dec 1562 alignment measured in the same cipher
(research/reading_audit/r2j_rennes_em.py): ds = r, plus = f|s|x, C = h, zs = c, sh = est, E = ff|h, S = a, ss = l.
A proposal only: every word is then checked on the image and against the sense.

    python research/reading_audit/r2j_p139_lattice.py [first_line last_line]
"""
import sys, math, re, json, collections, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT)); sys.path.insert(0, str(ROOT / 'targets' / 'rennes1563'))
from lang import lm
import measure as M
WIDEN = dict(ds='r', plus='f|s|x', C='h', zs='c', sh='est', E='ff|h', S='a', ss='l', Sao='-', RR='-', Rx='-', at='g')
HOLE = 14.0
import os
SHOW = os.environ.get('SHOW')

def lex():
    cache = ROOT / 'lang/cache/r2j_fr16_words.json'
    if cache.exists(): return json.load(open(cache, encoding='utf8'))
    c = collections.Counter()
    for fn in ('fr-1520s-diplomatic.txt', 'fr-henri4.txt'):
        p = ROOT / 'lang/corpora' / fn
        if p.exists(): c.update(re.findall(r'[a-z]+', lm.norm(p.read_text(encoding='utf8'), 'early')))
    c = {w: n for w, n in c.items() if n >= 2 or len(w) <= 2}
    json.dump(c, open(cache, 'w', encoding='utf8')); return c

def main():
    a, b = (int(sys.argv[1]), int(sys.argv[2])) if len(sys.argv) > 2 else (1, 99)
    L = lex(); tot = sum(L.values()); wc = {w: -math.log(n / tot) for w, n in L.items()}
    trie = {}
    for w, c in wc.items():
        n = trie
        for ch in w: n = n.setdefault(ch, {})
        n['$'] = c
    lines = [l.split() for l in open(ROOT / 'targets/rennes1563/c390_p139_v4.txt', encoding='utf8')
             if l.strip() and not l.startswith('#')]
    toks = []
    for i, ln in enumerate(lines, 1):
        if a <= i <= b: toks += [(i, t) for t in ln]
    def cands(t):
        base = M.P139.get(t, M.G.get(t, ''))
        vals = set(base.split('|')) if base else set()
        if t in WIDEN: vals |= set(WIDEN[t].split('|'))
        out = []
        for v in vals:
            v = v.replace('_', '')
            out.append('' if v in ('-', '') else v)
        return out or ['']
    beams = [dict() for _ in range(len(toks) + 1)]
    beams[0][id(trie)] = (0.0, None, trie, '')
    for i, (ln, t) in enumerate(toks):
        cur = sorted(beams[i].values(), key=lambda x: x[0])[:800]
        for ent in cur:
            cost, _, node, _ = ent
            starts = [(node, cost, '')]
            if '$' in node and node is not trie: starts.append((trie, cost + node['$'], ' '))
            for nd, c0, sep in starts:
                for v in cands(t):
                    n2 = nd; ok = True; c1 = c0; lab = sep
                    for ch in v:
                        if ch in n2: n2 = n2[ch]; lab += ch
                        elif '$' in n2 and n2 is not trie and ch in trie: c1 += n2['$']; n2 = trie[ch]; lab += ' ' + ch
                        else: ok = False; break
                    if not ok: continue
                    if not v: lab += '·'
                    k = id(n2)
                    if k not in beams[i + 1] or beams[i + 1][k][0] > c1:
                        beams[i + 1][k] = (c1, ent, n2, lab + ('' if not SHOW else '<' + t + '>'))
                if nd is trie:
                    k = id(trie); c1 = c0 + HOLE
                    if k not in beams[i + 1] or beams[i + 1][k][0] > c1:
                        beams[i + 1][k] = (c1, ent, trie, sep + '{' + t + '}')
        if (i + 1 < len(toks) and toks[i + 1][0] != ln) or i + 1 == len(toks):
            pass
    fin = lambda e: e[0] + (e[2]['$'] if '$' in e[2] and e[2] is not trie else (0 if e[2] is trie else 50))
    best = min(beams[-1].values(), key=fin)
    out = []; e = best
    while e and e[1] is not None:
        out.append(e[3]); e = e[1]
    print(''.join(reversed(out)))


if __name__ == '__main__':
    main()
