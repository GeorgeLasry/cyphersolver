"""b18 caprile: beam21 decoder of targets/caprile1520, run per line with each token's value shown (token=value),
so every break can be looked up on the image.  Off-key letters in CAPITALS (proposals, not readings).

    python research/reading_audit/b18_caprile_beam.py <R1139|R1136> <transcription file> [extra priors json]
The optional json maps sign label -> {letter: prob} and overrides beam21's priors (to test a key value).
"""
import sys, os, json, math, pathlib
T = pathlib.Path(__file__).resolve().parent.parent.parent / 'targets' / 'caprile1520'
sys.path.insert(0, str(T))
import beam21
from lang import lm

def decode(toks, m, P):
    A = m.A; k = m.order; idx = m.index; letters = [c for c in m.alpha if c != ' ']
    beams = {(): (0.0, ())}
    for t in toks:
        if t in ('|', '#'):
            cand = {'': 0.0} if t == '|' else {c: -3.0 for c in letters}
        else:
            cand = dict(P.get(t, {}))
            for c in letters:
                if c not in cand: cand[c] = beam21.OFFKEY
        nb = {}
        for ctx, (sc, out) in beams.items():
            for v, pv in cand.items():
                s2 = sc; c2 = ctx; s2 += pv
                for ch in v:
                    i = idx[ch]
                    if len(c2) == k - 1:
                        flat = 0
                        for x in c2: flat = flat * A + x
                        s2 += float(m.lp[flat * A + i])
                    c2 = (c2 + (i,))[-(k - 1):]
                mark = v.upper() if (pv == beam21.OFFKEY or t == '#') else v
                o2 = out + ((t, mark),)
                if c2 not in nb or nb[c2][0] < s2: nb[c2] = (s2, o2)
        beams = dict(sorted(nb.items(), key=lambda kv: -kv[1][0])[:beam21.BEAM])
    return max(beams.values())

def main():
    src, f = sys.argv[1], sys.argv[2]
    m = lm.load('it-cinquecento', spaces=False)
    P = beam21.priors()
    if len(sys.argv) > 3:
        for k_, v in json.load(open(sys.argv[3], encoding='utf8')).items():
            P[k_] = {l: math.log(p) for l, p in v.items()}
    for line in open(f, encoding='utf8'):
        if not line.startswith(src + ' '): continue
        toks = beam21.tokens(line)
        sc, out = decode(toks, m, P)
        print(line.split(':')[0], ''.join(v for _, v in out))
        print('   ', ' '.join(f'{t}={v or "_"}' for t, v in out))
main()
