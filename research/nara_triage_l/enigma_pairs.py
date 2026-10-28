"""enigma_pairs.py <naId>: on a cached reel, list frames holding Enigma groups (5-letter groups, flat IC) with their
part headers ('n TL - len') and reference numbers (Nr. x/38), and the clear frames carrying the same reference."""
import json, os, re, sys
sys.stdout.reconfigure(encoding='utf-8')
C = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'nara_reels', 'cache')
T = json.load(open(os.path.join(C, f'{sys.argv[1]}.txt.json'), encoding='utf-8'))
REF = re.compile(r'N[Rr]\.? ?(\d{3,5}) ?/ ?(3[6-9])')
def groups(t):
    return [x for x in re.findall(r'\b[A-Za-z]{5}\b', t) if x.isupper()]
def ic(gs):
    s = ''.join(gs); n = len(s)
    return sum(s.count(c) * (s.count(c) - 1) for c in set(s)) / max(1, n * (n - 1))
cipher, clear = [], {}
for i, o in enumerate(T):
    t = re.sub(r'\s+', ' ', o.get('extractedText') or '')
    g = groups(t); refs = {'/'.join(m) for m in REF.findall(t)}
    if len(g) >= 20 and ic(g) < 0.045:
        parts = re.findall(r'(\d{1,2})\s*\.?\s*T(?:L|EIL)\s*\.?\s*-\s*\.?\s*(\d{2,3})', t)
        dt = re.findall(r'\b\d{1,2}\.\d{1,2}\.(?:19)?38\b|\b\d{1,2}/\d{1,2}\b', t)[:2]
        cipher.append((i, o['objectId'], len(g), parts, sorted(refs), dt))
    else:
        for r in refs: clear.setdefault(r, []).append(o['objectId'])
for i, oid, n, parts, refs, dt in cipher:
    print(f'{oid} groups={n} parts={parts} refs={refs} dates={dt}')
    for r in refs: print('      clear frames with', r, ':', clear.get(r, [])[:8])
