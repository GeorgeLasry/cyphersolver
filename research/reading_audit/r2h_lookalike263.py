"""r2h: count letters of the R9416 f.263 reading that rest on the other member of a look-alike code
(v2 codes z e/s, b d/l, K k/b, p w/b/u, f/z o/e, H u/k) rather than the code's key value.
Aligns each reading line with the hand-key decode of the same cipher line (difflib on words, then letters
of equal-length word pairs). usage: python r2h_lookalike263.py <p34_v2.txt> <f263_reading.md>"""
import sys, re, difflib
import os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from r2h_dec263 import dec
ALT = {('e','s'),('d','l'),('k','b'),('w','b'),('w','u'),('o','e'),('e','o'),('u','k'),('w','p'),('o','s')}
cipher = {}
page = None
for ln in open(sys.argv[1], encoding='utf-8'):
    if 'PAGE P3' in ln: page = 'r'
    if 'PAGE P4' in ln: page = 'v'
    m = re.match(r'^(\d+):\s?(.*)$', ln.rstrip('\n'))
    if m and page: cipher[f'{page}{int(m.group(1)):02d}'] = dec(m.group(2))
body = open(sys.argv[2], encoding='utf-8').read().split('## Reading')[1].split('## Notes')[0]
tot = alt = 0; ex = []
for ln in body.splitlines():
    m = re.match(r'^([rv]\d\d) (.*)$', ln)
    if not m: continue
    rd = [w for w in re.findall(r"[a-zäöüß]+", re.sub(r'\[[^\]]*\]', ' ', m.group(2).lower()))]
    dc = re.findall(r"[a-z]+", re.sub(r'\[[^\]]*\]', ' ', cipher.get(m.group(1), '')))
    tot += sum(len(w) for w in rd)
    sm = difflib.SequenceMatcher(a=dc, b=rd, autojunk=False)
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == 'replace' and i2 - i1 == j2 - j1:
            for a, b in zip(dc[i1:i2], rd[j1:j2]):
                if len(a) == len(b):
                    for x, y in zip(a, b):
                        if x != y and (x, y) in ALT:
                            alt += 1; ex.append(f'{m.group(1)} {a}->{b}')
print(f'letters {tot}, look-alike alternates {alt} ({alt/tot:.1%})')
print('; '.join(ex))
