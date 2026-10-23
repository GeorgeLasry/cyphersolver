"""b35: letter-level alignment of a reading body with its decode; prints every place where they differ, so each
reading word not carried by the figures can be bracketed or justified.

    python b35_align.py <reading.md> <decode.txt> [context]
"""
import re, sys, difflib, pathlib, unicodedata
r = pathlib.Path(sys.argv[1]).read_text(encoding='utf-8')
body = re.search(r'^## Reading[^\n]*\n(.*?)(?=^## |\Z)', r, re.S | re.M).group(1)
d = pathlib.Path(sys.argv[2]).read_text(encoding='utf-8')
d = '\n'.join(l for l in d.splitlines() if not l.startswith('#'))
def letters(s, drop_codes):
    s = unicodedata.normalize('NFD', s)
    s = ''.join(c for c in s if unicodedata.category(c) != 'Mn')
    s = re.sub(r'<[^>]*>|\{[^}]*\}', '', s) if drop_codes else s
    s = re.sub(r'\[\d+\]', '', s)
    s = s.lower().replace('j', 'i').replace('v', 'u').replace('y', 'i')
    return re.sub(r'[^a-z]', '', s)
a, b = letters(d, True), letters(body, False)
sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
C = int(sys.argv[3]) if len(sys.argv) > 3 else 8
n = 0
for op, a0, a1, b0, b1 in sm.get_opcodes():
    if op == 'equal': continue
    n += 1
    print('%-7s decode %-14r reading %-14r | ...%s[%s]%s...' % (op, a[a0:a1], b[b0:b1], b[max(0, b0 - C):b0], b[b0:b1], b[b1:b1 + C]))
print('differences', n, 'decode letters', len(a), 'reading letters', len(b))
