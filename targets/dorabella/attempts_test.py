"""Do the published 'solutions' define a consistent symbol -> letter key on the consensus tokens?
(Texts as printed in Bauer, Unsolved! 2017, ch. 3, pp. 131-133.)"""
import os, re, collections
HERE = os.path.dirname(os.path.abspath(__file__))
lines = [l.split() for l in open(os.path.join(HERE, 'ct.txt')).read().strip().splitlines()]
flat = [t for l in lines for t in l]
palmer = ["BLTACEIARWUNISNFNNELLHSYWYDUO", "INIEYARQATNNTEDMINUNEHOMSYRRYUO", "TOEHO'TSHGDOTNEHMOSALDOEADYA"]
palmer_rev = ["B LCAT IE AWR USIN NF NN ESHLL WY YOUD", "INTAQRAYEIN NET DMINUNEHO M SRRY YOU", "THEO O 'THS GOD THEN M SO LA OD E ADYA"]
sams = "LARKS! IT'S CHAOTIC, BUT A CLOAK OBSCURES MY NEW LETTERS, A, B BELOW: I OWN THE DARK MAKES E. E. SIGH WHEN YOU ARE TOO LONG GONE."
roberts = "P.S. Now droop beige weeds set in it—pure idiocy—one entire bed! Luigi Ccibunud luv'ngly tuned liuto studo two."
def letters(s): return re.sub(r'[^A-Za-z]', '', s).upper()
def check(name, text, order=None):
    L = letters(text)
    print(f'{name}: {len(L)} letters (cipher has {len(flat)})')
    if len(L) != len(flat): return
    toks = flat if order is None else [flat[i] for i in order]
    m = collections.defaultdict(collections.Counter)
    for t, c in zip(toks, L): m[t][c] += 1
    bad = {t: dict(c) for t, c in m.items() if len(c) > 1}
    # reverse: letters -> symbols (homophones OK) -- a symbol must map to ONE letter
    ncons = sum(1 for t in m if len(m[t]) == 1)
    print(f'   symbols {len(m)}, one-letter symbols {ncons}, inconsistent {len(bad)}; e.g. {list(bad.items())[:4]}')
    # best-case: majority letter per symbol; how many positions agree
    agree = sum(max(c.values()) for c in m.values())
    print(f'   positions explained by the best symbol->letter map: {agree}/{len(flat)}')
check('Palmer (pre-reversal)', ''.join(palmer))
check('Palmer pre-reversal, text reversed', ''.join(palmer)[::-1])
check('Sams', sams)
check('Roberts', roberts)
# shuffled baseline for 'positions explained by best map'
import random
rng = random.Random(3)
base = []
Lp = letters(''.join(palmer))
for _ in range(2000):
    t = flat[:]; rng.shuffle(t)
    m = collections.defaultdict(collections.Counter)
    for a, b in zip(t, Lp): m[a][b] += 1
    base.append(sum(max(c.values()) for c in m.values()))
print('Palmer letters vs shuffled symbols: explained mean %.1f max %d' % (sum(base) / len(base), max(base)))
