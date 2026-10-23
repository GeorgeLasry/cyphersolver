"""v3 verify (b): turn a line-numbered reading ('12  text-' per manuscript line, '#' comments, '== f.250r' markers)
into running text for scoring: line numbers, comments and folio markers cut, words broken at a line end joined.

    python research/reading_audit/v3b_lines.py <reading> <out.md> [--conj]     --conj: <...> conjectures become [?...]
"""
import re, sys
src, out = sys.argv[1], sys.argv[2]
t = ''
for l in open(src, encoding='utf8'):
    l = l.rstrip('\n')
    if l.startswith('#') or l.startswith('==') or not l.strip():
        continue
    l = re.sub(r'^\s*\d+[a-z]?\s+', '', l).strip()
    if t.endswith('-'):
        t = t[:-1] + l.lstrip('-')
    else:
        t = (t + ' ' + l) if t else l
if '--conj' in sys.argv:
    t = re.sub(r'<([^>]*)>', lambda m: ' '.join('[?' + w + ']' for w in m.group(1).split()), t)
open(out, 'w', encoding='utf8').write('## Reading\n' + t + '\n')
print(out, len(t.split()))
