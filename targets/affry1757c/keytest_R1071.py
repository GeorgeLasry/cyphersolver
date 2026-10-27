# keytest_R1071.py : apply every machine-readable key of the period to R1071 (code C) and score the result.
# For each key: coverage (share of R1071 groups with a value) and the French LM per-char score of the 9-group
# windows, against the same key with its values shuffled over its codes (20 shuffles: mean and max).
# Keys covering under 30% of the groups give too few full windows to judge. A key that fits scores far above its shuffles; the d'Affry A/B key on R1054 (../affry1757) is the positive control.
import os, sys, json, glob, random, statistics
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
from lang import lm
os.chdir(os.path.dirname(os.path.abspath(__file__)))
M = lm.load('fr-modern', spaces=False)
T = os.path.join('..')
A = os.path.join('..', 'affry1757')

def own():
    k = dict(json.load(open(f'{A}/key_M.json', encoding='utf8')))
    k.update(json.load(open(f'{A}/key_X.json', encoding='utf8')))
    return {g: v for g, v in k.items() if v and '?' not in v}
def tsv(path, ci, vi, skip='#'):
    k = {}
    for f in glob.glob(path):
        for line in open(f, encoding='utf8'):
            if line.startswith(skip): continue
            p = line.rstrip('\n').split('\t')
            if len(p) > max(ci, vi) and p[ci].strip().isdigit() and p[vi].strip() and not p[vi].startswith('<'):
                k.setdefault(str(int(p[ci])), p[vi].split(',')[0].split('/')[0].strip())
    return k
KEYS = {
    "d'Affry A/B 1757 (key_M + key_X, Lyonet alignments)": own(),
    'Van Swieten-Cobenzl table (swieten1759/key.json)':
        {g: v for g, v in json.load(open(f'{T}/swieten1759/key.json', encoding='utf8')).items() if v},
    'Hanoverian army code 1743, 1-863 (ilten1743)': tsv(f'{T}/ilten1743/key1743/decode_*.tsv', 0, 1),
    'Prussian Michell code 1751 (michell1751 R1957 key v2)': tsv(f'{T}/michell1751/key1751/R1957_decipherment.tsv', 1, 2),
    'Croiset 1765 codebook, plain numbers (R1038, deswart1782)': tsv(f'{T}/deswart1782/R1038_key_parsed.tsv', 0, 1),
}

def groups(r):
    if r == 'R1071': return open('cipher_C.txt').read().split()[2:]
    return [t.split('|')[0] for line in open(f'{A}/transcr/{r}.txt', encoding='utf8') if not line.startswith('#')
            for t in line.split() if t.split('|')[0].isdigit()]
def score(g, key, W=4):
    vals = [key.get(x) for x in g]
    cov = sum(v is not None for v in vals) / len(vals)
    s = []
    for i in range(0, len(g) - 2 * W, 3):
        win = [v for v in vals[i:i + 2 * W + 1] if v]
        t = lm.norm(''.join(win), 'modern', spaces=False)
        if len(t) >= 8: s.append(M.per_char(t))
    return cov, (statistics.mean(s) if s else float('nan'))
def shuffled(key, rng):
    ks, vs = list(key), list(key.values()); rng.shuffle(vs); return dict(zip(ks, vs))

rng = random.Random(1757)
for r in ['R1054', 'R1071']:
    g = groups(r)
    print(f'== {r} ({len(g)} groups)')
    for name, key in KEYS.items():
        cov, sc = score(g, key)
        sh = [x for x in (score(g, shuffled(key, rng))[1] for _ in range(20)) if x == x] or [float('nan')]
        print(f'  {name[:62]:62s} codes {len(key):5d}  cover {cov:.2f}  LM {sc:6.2f}  '
              f'shuffled {statistics.mean(sh):6.2f} (max {max(sh):6.2f})  '
              f'{"too sparse to judge" if cov < 0.3 else "FITS" if sc > max(sh) + 0.15 else "no"}')
