"""b06: apply one logged transcription correction to a kurtz1639 R3812 tr/ file.

    python research/reading_audit/b06_r3812_fix.py <image-stem> <line-no> "<old>" "<new>" "<value>" "<note>"
<old> must occur exactly once on that line (1-based line number of the tr file). The change is appended to
read/R3812_corrections.tsv (rec, image, line, old, new, value, note).
"""
import os, sys
K = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'targets', 'kurtz1639')
stem, n, old, new, val, note = sys.argv[1], int(sys.argv[2]), sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6]
p = os.path.join(K, 'tr', stem + '.txt')
L = open(p, encoding='utf-8').read().split('\n')
line = L[n - 1]
pad = ' ' + line + ' '
o = old if old.startswith('{') else ' ' + old + ' '
nw = new if old.startswith('{') else ' ' + new + ' '
if pad.count(o) != 1: sys.exit('old %r found %d times on line %d: %s' % (old, pad.count(o), n, line))
L[n - 1] = pad.replace(o, nw)[1:-1]
open(p, 'w', encoding='utf-8').write('\n'.join(L))
t = os.path.join(K, 'read', 'R3812_corrections.tsv')
if not os.path.exists(t):
    open(t, 'w', encoding='utf-8').write('rec\timage\tline\told\tnew\tvalue\tnote\n')
open(t, 'a', encoding='utf-8').write('\t'.join(['R3812', stem, str(n), old, new, val, note]) + '\n')
print(L[n - 1])
