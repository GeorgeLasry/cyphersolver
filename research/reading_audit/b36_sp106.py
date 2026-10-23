"""b36: sp106r929 (R929, SP 106/10 f. 247) - take Pettersson's cipher rows from Lasry's interlinear file (DECODE D3084,
scratchpad copy), apply the corrections read on the full-size image (targets/sp106r929/R929_corrections.tsv), write the
corrected sign transcription (targets/sp106r929/R929_signs.txt) and decode it with Lasry's SP106-5 key (D3085) plus the
one value added here (o2 = WE), printing Lasry's plaintext row under each decoded row.

    python research/reading_audit/b36_sp106.py <dir with DOC_R929_* files>
"""
import csv, re, sys, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[2]
T = ROOT / 'targets' / 'sp106r929'
sys.path.insert(0, str(T))
from apply_key import load_key

D = pathlib.Path(sys.argv[1])
key = load_key(D / 'DOC_R929_D3085_3085.txt')
key['o2'] = 'WE'          # b36: holds at both occurrences (weke, wekly); o0 is WE in Lasry's key
cur, rows = None, []
for l in (D / 'DOC_R929_D3084_3084.txt').read_text(encoding='utf-8', errors='replace').splitlines():
    m = re.match(r'#{6,}\s*tna[ _]sp106.(\S+?)(\.txt)?\s*$', l)
    if m: cur = m.group(1); continue
    if l.startswith('#KEY'): cur = None
    if cur == '0247' and l.strip() and not l.lstrip().startswith('#'): rows.append(l.rstrip().rstrip('|').split())
cipher, plain = rows[0::2], rows[1::2]
fix = list(csv.DictReader(open(T / 'R929_corrections.tsv', encoding='utf-8'), delimiter='\t'))
for f in fix:
    r, i = int(f['row']), int(f['index'])
    assert cipher[r][i] == f['old'], (f, cipher[r])
    cipher[r][i] = f['value']
out = ['# R929 sign transcription: Pettersson (DECODE D1821, cipher rows of Lasry\'s D3084) with R929_corrections.tsv '
       'applied (checked on the full-size image); one manuscript line per row, the last three rows are the margin; '
       '=n is a numeral written in clear']
out += [' '.join(c) for c in cipher]
(T / 'R929_signs.txt').write_text('\n'.join(out) + '\n', encoding='utf-8')
for n, (c, p) in enumerate(zip(cipher, plain)):
    dec = []
    for g in c:
        if g.startswith('='): dec.append(g[1:])
        elif g in key: dec.append(key[g].lower() if len(key[g]) == 1 else key[g])
        else: dec.append('<%s>' % g)
    print('%2d' % n, ' '.join(dec))
    print('  L', ' '.join(p))
