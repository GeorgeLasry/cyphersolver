"""b37: decode SP 53/11 no. 50I from Tomokiyo's numeric labels (targets/walsingham1581/SP53_11_50b.txt) through a
label -> glyph -> value concordance built on the f. 138 image (DECODE R3839 P3) with Tomokiyo's glyph key
(cryptiana mary_sp53_11_50b.png). The concordance is targets/walsingham1581/texts/no50I_concordance.tsv
(label, glyph as seen, value, evidence). Output: texts/no50I_decode.txt (per manuscript line; nulls as '.', unknown
labels as #NN, word signs in capitals)."""
import pathlib, csv, sys
D = pathlib.Path(__file__).resolve().parents[2] / 'targets' / 'walsingham1581'
L = [l.strip().rstrip(';').split(';') for l in (D / 'SP53_11_50b.txt').read_text().splitlines()[1:] if l.strip()]
conc = {}
for r in csv.reader(open(D / 'texts' / 'no50I_concordance.tsv', encoding='utf8'), delimiter='\t'):
    if r and not r[0].startswith('#') and r[0] != 'label':
        conc[r[0]] = r[2]
out = []
for i, l in enumerate(L):
    s = []
    for t in l:
        v = conc.get(t)
        if v is None or v == '?': s.append('#' + t)
        elif v == 'null': s.append('.')
        elif v.isupper() and len(v) > 1: s.append(' ' + v + ' ')
        else: s.append(v)
    out.append(f'{i+1:2d}: ' + ''.join(s))
(D / 'texts' / 'no50I_decode.txt').write_text('# SP 53/11 no. 50I decoded with the concordance (b37_wals_dec.py); . = null/space sign, #NN = label without a value\n' + '\n'.join(out) + '\n', encoding='utf8')
print('\n'.join(out))
