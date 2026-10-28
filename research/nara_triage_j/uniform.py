"""uniform.py: from out/rg_64_corr.tsv keep items whose sample frame is mostly uniform 4- or 5-digit groups (code
telegrams) rather than tables (totals, decimals, mixed lengths)."""
import re, collections, os
OUT = os.path.join(os.path.dirname(__file__), '..', 'nara_reels', 'out')
keep = []
for l in open(os.path.join(OUT, 'rg_64_corr.tsv'), encoding='utf-8'):
    r = l.rstrip('\n').split('\t')
    if len(r) < 6: continue
    sn = r[5]; g = re.findall(r'\b\d+\b', sn)
    if len(g) < 15: continue
    top, c = collections.Counter(len(x) for x in g).most_common(1)[0]
    if top in (4, 5) and c / len(g) >= 0.7 and not re.search(r'total|\.\d|\$|per cent|%', sn, re.I):
        keep.append(r)
print(len(keep))
for r in keep: print(r[0], r[1], r[2][:28], '|', r[3][:45], '|', r[4], '|', r[5][:120])
