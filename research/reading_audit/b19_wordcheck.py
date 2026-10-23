"""b19: word-by-word carry check of a reading against its decode and clear text.
Every unbracketed word of the reading body (## Reading) must occur in the decode stream (the codebook values of the
groups, concatenated without spaces, so words the code spells in pieces are found) or in the clear text («...» in the
decode file or in extra clear files). Words found nowhere are printed: they must be bracketed or corrected.

    python b19_wordcheck.py <reading.md> <decode.txt> [<extra clear text file> ...]
"""
import re, sys, pathlib


import os
SUBS = []
if os.environ.get('SUBS'):  # tab-separated "key misreading -> word" pairs, applied to the decode values only
    SUBS = [l.rstrip(chr(10)).split(chr(9))[:2] for l in open(os.environ['SUBS'], encoding='utf8') if chr(9) in l and not l.startswith('#')]


def norm(s):
    s = s.lower().replace('ÿ', 'y').replace('ij', 'y')
    return re.sub(r'[^a-z0-9éèàç]', '', s)


rd = pathlib.Path(sys.argv[1]).read_text(encoding='utf8')
body = re.search(r'^## (?:Reading|Translation)[^\n]*\n(.*?)(?=^## |\Z)', rd, re.S | re.M).group(1)
dec = pathlib.Path(sys.argv[2]).read_text(encoding='utf8')
clear = ' '.join(re.findall(r'«(.*?)»', dec, re.S))
for f in sys.argv[3:]:
    clear += ' ' + pathlib.Path(f).read_text(encoding='utf8')
vl = [m.group(1).replace('_', ' ') for m in re.finditer(r'=(\S+)', dec)]
for a, b in SUBS:
    vl = [b if v == a else v for v in vl]
vals = norm(''.join(vl))
cl = norm(clear)
cw = set(norm(w) for w in clear.split())
body = re.sub(r'\[[^\]]*\]', ' ', body)
bad = []
for w in body.split():
    n = norm(w)
    if not n: continue
    if n in cw or n in vals or n in cl: continue
    bad.append(w)
print(sys.argv[1], 'uncarried:', bad if bad else 'none')
