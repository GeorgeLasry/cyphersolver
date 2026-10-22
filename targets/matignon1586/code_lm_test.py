"""Rank candidate words for each open code group by the 6-gram score of its contexts in the merged-key decode.

For each occurrence the decode's 30 letters either side are kept; a candidate's score is the summed log-probability
of left+candidate+right over all occurrences, minus that of the best null (code read as nothing), per occurrence.
Candidates: the 400 commonest corpus words of 2+ letters plus any extra given. Output code_lm_test.json.
"""
import json, sys
sys.argv = ['x']
import brackx_validate as V
from solve import logp, WORDS

CODES = ['16', '45', '59', '64', 'me', '101', '102', '103', '9', '44']
key = V.prep_key(json.load(open('key_merged_union.json', encoding='utf-8')))
ctx = {c: [] for c in CODES}
for name, files, *_ in V.LEAVES:
    res = V.decode(files, key, 'mku_' + name.replace(' ', '_').replace('.', ''))
    txt = ''.join(x['text'] for x in res); p = 0
    for x in res:
        for t, L in zip(x['tokens'], x['lens']):
            if t in ctx:
                ctx[t].append((name, txt[max(0, p - 30):p].replace('+', ''), txt[p + L:p + L + 30].replace('+', '')))
            p += L


def lp(s):
    return sum(logp(s[:i], s[i]) for i in range(len(s)))


cands = [w for w, c in sorted(WORDS.items(), key=lambda x: -x[1]) if len(w) >= 2][:400]
cands += ['mesme', 'argent', 'aussi', 'avec', 'ceux', 'leur', 'monsieur', 'sire', 'roy', 'eux', 'luy']
out = {}
for c, occ in ctx.items():
    sc = []
    for w in set(cands):
        s = 0
        for _, l, r in occ:
            base = lp(l + r) - lp(l)
            s += (lp(l + w + r) - lp(l)) - base
        sc.append((round(s / max(1, len(occ)), 2), w))
    sc.sort(reverse=True)
    out[c] = {'n': len(occ), 'top': sc[:8], 'contexts': occ}
    print(c, len(occ), sc[:8])
json.dump(out, open('code_lm_test.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
