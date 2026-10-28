"""groups.py <naId> [min]: frames of a cached item (nara_reels/cache) with at least <min> (default 8) five-letter
groups, with group count, letter IC of the groups, and the text around them."""
import json, os, re, sys
sys.stdout.reconfigure(encoding='utf-8')
C = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'nara_reels', 'cache')
nid, mn = sys.argv[1], int(sys.argv[2]) if len(sys.argv) > 2 else 8
for o in json.load(open(os.path.join(C, f'{nid}.txt.json'), encoding='utf-8')):
    t = re.sub(r'\s+', ' ', o.get('extractedText') or o.get('text') or '')
    g = re.findall(r'\b[A-Za-z]{5}\b', t)
    g = [x for x in g if x.isupper() or x.islower()]
    if len(g) < mn: continue
    s = ''.join(g).upper(); n = len(s)
    ic = sum(s.count(c) * (s.count(c) - 1) for c in set(s)) / max(1, n * (n - 1))
    name = o.get('objectFilename') or o.get('filename') or o.get('objectId')
    print(f'--- {name} groups={len(g)} ic={ic:.4f}')
    print('   ', t[:900])
