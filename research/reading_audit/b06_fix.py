"""b06: apply logged transcription corrections to kurtz1639 tr/ files (any record).

    python research/reading_audit/b06_fix.py < fixes.tsv
Each input line: <image-stem> TAB <line-no> TAB <old> TAB <new> TAB <value> TAB <note>. <old> must occur exactly once
on that line (1-based) as whole tokens (or as a {clear} span). Each change is appended to read/<rec>_corrections.tsv.
"""
import os, re, sys
K = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'targets', 'kurtz1639')
for row in sys.stdin.read().splitlines():
    if not row.strip() or row.startswith('#'): continue
    stem, n, old, new, val, note = (row.split('\t') + [''] * 6)[:6]
    n = int(n); rec = re.search(r'R\d+', stem).group()
    p = os.path.join(K, 'tr', stem + '.txt')
    L = open(p, encoding='utf-8').read().split('\n')
    pad = ' ' + L[n - 1] + ' '
    o = old if old.startswith('{') else ' ' + old + ' '
    nw = new if old.startswith('{') else ' ' + new + ' '
    if pad.count(o) != 1:
        print('SKIP %s:%d %r found %d times: %s' % (stem, n, old, pad.count(o), L[n - 1])); continue
    L[n - 1] = pad.replace(o, nw, 1)[1:-1]
    open(p, 'w', encoding='utf-8').write('\n'.join(L))
    t = os.path.join(K, 'read', rec + '_corrections.tsv')
    if not os.path.exists(t):
        open(t, 'w', encoding='utf-8').write('rec\timage\tline\told\tnew\tvalue\tnote\n')
    open(t, 'a', encoding='utf-8').write('\t'.join([rec, stem, str(n), old, new, val, note]) + '\n')
    print('%s:%d  %s' % (stem, n, L[n - 1]))
