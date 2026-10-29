"""Test the 1761 Windward Islands key (mercier1761/key1761.tsv) and the 1765 d'Ennery form
(mercier1761/key1765_ennery.tsv) on the 1778 letter (transcription.txt); report coverage and any sense."""
import os, sys, collections
H = os.path.dirname(os.path.abspath(__file__)); M = os.path.join(H, '..', 'mercier1761')
toks = [t for l in open(os.path.join(H, 'transcription.txt'), encoding='utf8') if not l.startswith('#') for t in l.split()]
def load(fn, vcol=1):
    d = {}
    for l in open(os.path.join(M, fn), encoding='utf8'):
        if l[:1].isdigit():
            p = l.rstrip('\n').split('\t')
            if len(p) > vcol and p[vcol] not in ('', '?'): d[p[0]] = p[vcol]
    return d
for fn in ('key1761.tsv', 'key1765_ennery.tsv'):
    k = load(fn)
    hit = [k[t] for t in toks if t in k]
    print(fn, 'entries', len(k), 'range', min(map(int, k)), max(map(int, k)), 'tokens valued', len(hit), '/', len(toks))
    print('  ', ' '.join(k.get(t, '[%s]' % t) for t in toks[:60]))
c = collections.Counter(toks)
print('range', min(map(int, toks)), max(map(int, toks)), 'over 696:', sum(1 for t in toks if int(t) > 696), 'over 800:', sum(1 for t in toks if int(t) > 800))
