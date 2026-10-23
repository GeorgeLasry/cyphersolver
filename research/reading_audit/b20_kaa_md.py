"""b20: turn a System A' line reading (targets/kaa4591/r94xx/reading.txt) into a partial reading file in the brief's
notation, without changing a word: {?} -> [...]; the writer's clear text [..] -> *..* (a '?' inside -> [?..]);
[F.G.] and [K] kept as code markers; [note: ...] dropped; x[y]z (supplied letters) kept. Lines joined in page order.

    python research/reading_audit/b20_kaa_md.py <reading.txt> <out.md> "<header comment>" "<title>"
"""
import re, sys
src, out, head, title = sys.argv[1:5]
lines = [l.rstrip('\n') for l in open(src, encoding='utf8') if re.match(r'P\d+\.\d\d', l)]
CODES = {'[F.G.]', '[K]'}
def conv(t):
    t = re.sub(r'\[note:[^\]]*\]', '', t)
    t = t.replace('{?}', '[...]')
    def clear(m):
        s = m.group(0)
        if s in CODES or s == '[...]': return s
        inner = s[1:-1]
        if re.fullmatch(r'[a-zäöüß]{1,3}', inner): return s           # supplied letters inside a word
        if '?' in inner: return '*[?' + inner.replace('?', '').strip() + ']*'
        return '*' + inner + '*'
    t = re.sub(r'\[[^\]]*\]', clear, t)
    return t
pages = {}
for l in lines:
    m = re.match(r'(P\d+)\.(\d\d)\s*(.*)', l)
    pages.setdefault(m.group(1), []).append(conv(m.group(3)))
body = []
for p, ls in pages.items():
    txt = ' '.join(ls)
    txt = re.sub(r'(\w)- (\w)', r'\1\2', txt)
    body.append(f'**{p}.** ' + re.sub(r'\s+', ' ', txt).strip())
open(out, 'w', encoding='utf8').write(f'<!-- {head} -->\n\n# {title}\n\n## Reading\n\n' + '\n\n'.join(body) + '\n')
print(out, sum(len(b.split()) for b in body))
