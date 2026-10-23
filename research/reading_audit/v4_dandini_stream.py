"""v4 (23 Oct 2026): print Lasry's R73 decryption (decode/DOC_R72_D3191_3191.txt) as a letter stream, one line per
cipher line, codes as [..], groups with no value (KaJo '?') as {?}.   python v4_dandini_stream.py <file>"""
import re, sys
L = open(sys.argv[1], encoding='utf8').read().splitlines()
skip = False
for i, l in enumerate(L):
    if skip: skip = False; continue
    if l.startswith('#IMAGE NAME'): print('==', l.split(':', 1)[1].strip())
    if l.startswith('#') or not re.search(r'\d', l) or i + 1 >= len(L): continue
    lets = L[i + 1]; skip = True
    out = []
    ms = list(re.finditer(r'\S+', l.split('|')[0]))
    for k, m in enumerate(ms):
        g = m.group(0)
        end = ms[k + 1].start() if k + 1 < len(ms) else m.end() + 8
        seg = lets[m.start():end].split('|')[0].strip() if m.start() < len(lets) else ''
        if g == '?' or not seg: out.append('{?}')
        elif len(seg) == 1: out.append(seg)
        else: out.append('[' + seg + ']')
    print(''.join(out))
