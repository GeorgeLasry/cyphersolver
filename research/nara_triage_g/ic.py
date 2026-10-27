"""Letter statistics of five-letter group runs in a cached item's OCR.
    python research/nara_triage_g/ic.py <naId> <first> <last>
Takes every 5-letter token (case-folded) on frames first..last, prints per frame count, IC and top letters,
and the pooled figures. German plaintext IC ~0.076, flat 0.038; transposition keeps plaintext IC."""
import collections, re, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from show import load
sys.stdout.reconfigure(encoding='utf-8')
naid, a, b = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
rec, frames = load(naid)
pool = collections.Counter()
def ic(c):
    n = sum(c.values()); return sum(v*(v-1) for v in c.values())/(n*(n-1)) if n > 1 else 0
for n, name, url, t in frames:
    if a <= n <= b:
        toks = [w.lower() for w in re.findall(r'(?<![A-Za-z])[A-Za-z]{5}(?![A-Za-z])', t)]
        toks = [w for w in toks if not re.fullmatch(r'(uhr|durch|monat|stunde|minuten|stelle|befordert|spruch)\w*', w)]
        if len(toks) < 8: continue
        c = collections.Counter(''.join(toks)); pool += c
        print(name, len(toks), round(ic(c), 4), ''.join(k for k, _ in c.most_common(8)), ' '.join(toks[:6]))
print('pooled', sum(pool.values()), round(ic(pool), 4), ''.join(k for k, _ in pool.most_common(26)))
