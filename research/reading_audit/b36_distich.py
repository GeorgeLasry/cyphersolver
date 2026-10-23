"""b36: urquhart distich - letter-index variants not in the earlier scripts: the k-th number as the n-th LETTER (not
word) of the k-th Proquiritation (Reticuli's tokenisation, src/reticuli_proquiritations.json), lines 1 and 2 both on
Proquiritations 1-32, with and without the signature letters, counting from 1 or 0, and line 2 on Proquiritations
32..1; scored with lang en-1640s per character against shuffled-number controls.

    python research/reading_audit/b36_distich.py
"""
import json, pathlib, random, sys
ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT)); sys.path.insert(0, str(ROOT / 'targets' / 'urquhart'))
from ct import DISTICH
from lang import lm
M = lm.load('en-1640s')
P = json.load(open(ROOT / 'targets/urquhart/src/reticuli_proquiritations.json', encoding='utf-8'))
def texts(sig):
    out = []
    for i in range(1, 33):
        w = ''.join(P[str(i)]['words'])
        if sig: w += P[str(i)]['signed']
        out.append(''.join(c for c in w if c.isalpha()).lower())
    return out
def dec(nums, T, off, rev2):
    s = []
    for k, n in enumerate(nums):
        i = k % 32
        if rev2 and k >= 32: i = 31 - i
        t = T[i]; j = n - 1 + off
        s.append(t[j] if 0 <= j < len(t) else '_')
    return ''.join(s)
def sc(s):
    s = s.replace('_', '')
    return M.score(s) / max(1, len(s))
res = []
for sig in (0, 1):
    T = texts(sig)
    for off in (0, 1):
        for rev2 in (0, 1):
            s = dec(DISTICH, T, off, rev2)
            ctrl = []
            for r in range(50):
                d = DISTICH[:]; random.Random(r).shuffle(d); ctrl.append(sc(dec(d, T, off, rev2)))
            ctrl.sort()
            res.append((sc(s), sig, off, rev2, s, ctrl[-1], sum(ctrl) / len(ctrl)))
for r in sorted(res, reverse=True):
    print('%.3f sig=%d off=%d rev2=%d ctrl max %.3f mean %.3f %s' % (r[0], r[1], r[2], r[3], r[5], r[6], r[4]))
