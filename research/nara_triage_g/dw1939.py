"""Test the 25.2.1939 Luftgauschluessel (T405 roll 9 frame 350) on the 221-letter message of frame 349.
Double columnar transposition; tries both readings of the doubled '13' in key a and both key orders."""
import itertools
CT = ('xxdrx diwsm xemrn nskxl gdxze uxocn lsfks eneir tnloa dtxit udnaa tiron oafxl ketsm mneiz xrmea xetiq '
      'xstos oenrz wtqur igaaf dibth eefml peoee veled ulgbw nixxx eutbg xtnen asrru sxnaw xlkki urnli oitgg '
      'tdxfe roeae oezos ienai nxrie eeged drrzh bredw lexre rtwef a').replace(' ', '')
A0 = [17, 9, 3, 14, 21, 19, 1, 10, 20, 5, 13, 2, 16, 8, 12, 7, 4, 11, 6, 13, 18]
B = [16, 11, 1, 19, 7, 4, 15, 9, 2, 13, 6, 18, 3, 17, 5, 12, 8, 14, 10]
def undo(ct, key):  # inverse of: write rows of len(key), read columns in order of key number
    n, k = len(ct), len(key); rows = -(-n // k); full = n % k or k
    lens = [rows if i < full else rows - 1 for i in range(k)]
    cols, p = {}, 0
    for num in sorted(range(k), key=lambda i: key[i]):
        cols[num] = ct[p:p + lens[num]]; p += lens[num]
    return ''.join(cols[c][r] for r in range(rows) for c in range(k) if r < len(cols[c]))
WORDS = ['ein', 'der', 'die', 'und', 'flak', 'uhr', 'berlin', 'nicht', 'den', 'sch', 'ung', 'gruppe']
for i in (10, 19):
    A = A0[:]; A[i] = 15
    for k1, k2, lab in ((A, B, 'a then b'), (B, A, 'b then a')):
        pt = undo(undo(CT, k2), k1)
        print(i, lab, sum(pt.count(w) for w in WORDS), pt)

def inv(key):
    k = len(key); r = [0] * k
    for i, v in enumerate(key): r[v - 1] = i + 1
    return r
def score(pt):
    return sum(pt.count(w) for w in ['ein', 'der', 'die', 'und', 'en', 'er', 'ch', 'sch', 'ung', 'ei', 'ie', 'te', 'xx'])
best = []
for ct, cl in ((CT, 'full'), (CT[:30] + CT[35:], 'drop grp7')):
    for i in (10, 19):
        A = A0[:]; A[i] = 15
        for fa, fb in itertools.product((lambda x: x, inv), repeat=2):
            a2, b2 = fa(A), fb(B)
            for k1, k2, lab in ((a2, b2, 'a,b'), (b2, a2, 'b,a')):
                for mode in ('undo', 'redo'):
                    if mode == 'undo':
                        pt = undo(undo(ct, k2), k1)
                    else:
                        pt = undo(undo(ct, k1), k2)
                    best.append((score(pt), cl, i, fa.__name__, fb.__name__, lab, mode, pt))
best.sort(key=lambda x: -x[0])
for b in best[:4]: print(b)
