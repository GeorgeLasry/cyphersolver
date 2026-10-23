"""r2c (23 Oct 2026): relabel kurtz1639 tokens in tr/ and append rows to read/<rec>_corrections.tsv.
    python research/reading_audit/r2c_relabel.py <rec> <spec-file>
spec lines: page side line_in_side token_index old new value note   (tab-separated; token_index as tokens_of counts cipher tokens)"""
import sys, re, os
sys.path.insert(0, 'targets/kurtz1639')
from parse import tokens_of
rec, spec = sys.argv[1], sys.argv[2]
rows = []
for sl in open(spec, encoding='utf8'):
    if not sl.strip() or sl.startswith('#'): continue
    page, side, li, ti, old, new, val, note = sl.rstrip('\n').split('\t')
    f = f'targets/kurtz1639/tr/IMG_{rec}_{page}.txt'
    L = open(f, encoding='utf8').read().split('\n')
    sd, cnt, hit = 'F', {}, None
    for n, l in enumerate(L):
        t = l.strip()
        if t.startswith('## '):
            sd = 'L' if 'left' in t.lower() else 'R' if 'right' in t.lower() else 'F'; continue
        if not t or t == '#' or t.startswith('# ') or t.lower().startswith('legend'): continue
        cnt[sd] = cnt.get(sd, 0) + 1
        if sd == side and cnt[sd] == int(li): hit = n; break
    toks = [it[1] for it in tokens_of(L[hit].strip()) if it[0] != 'clear']
    ti = int(ti); assert toks[ti] == old, (page, side, li, toks[ti], old)
    occ = sum(1 for x in toks[:ti] if x == old)
    parts = L[hit].split(' '); k = -1
    for p_i, p in enumerate(parts):
        if p.strip('~[]').rstrip(',.:;') == old:
            k += 1
            if k == occ: parts[p_i] = p.replace(old, new, 1); break
    before = L[hit]; L[hit] = ' '.join(parts); assert before != L[hit]
    open(f, 'w', encoding='utf8', newline='').write('\n'.join(L))
    rows.append(f'{rec}\tIMG_{rec}_{page}\t{hit + 1}\t{old}\t{new}\t{val}\t{note}')
    print(page, side, li, '->', L[hit].strip())
open(f'targets/kurtz1639/read/{rec}_corrections.tsv', 'a', encoding='utf8').write('\n'.join(rows) + '\n')
