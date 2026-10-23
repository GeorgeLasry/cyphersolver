"""r2k: b37_wals_dec.py plus position corrections (texts/no50I_position_corrections.tsv: line, pos, label, glyph, value)
for places where one of Tomokiyo's labels stands for another glyph. Writes texts/no50I_decode.txt."""
import pathlib, csv
D = pathlib.Path(__file__).resolve().parents[2] / 'targets' / 'walsingham1581'
L = [l.strip().rstrip(';').split(';') for l in (D / 'SP53_11_50b.txt').read_text().splitlines()[1:] if l.strip()]
conc, pos = {}, {}
for r in csv.reader(open(D / 'texts' / 'no50I_concordance.tsv', encoding='utf8'), delimiter='\t'):
    if r and not r[0].startswith('#') and r[0] != 'label':
        conc[r[0]] = r[2]
for r in csv.reader(open(D / 'texts' / 'no50I_position_corrections.tsv', encoding='utf8'), delimiter='\t'):
    if r and not r[0].startswith('#') and r[0] != 'line':
        pos[(int(r[0]), int(r[1]))] = r[4]
out = []
for i, l in enumerate(L):
    s = []
    for k, t in enumerate(l):
        v = pos.get((i + 1, k), conc.get(t))
        if v is None or v == '?': s.append('#' + t)
        elif v == 'null': s.append('.')
        elif v.isupper() and len(v) > 1: s.append(' ' + v + ' ')
        else: s.append(v)
    out.append(f'{i+1:2d}: ' + ''.join(s))
(D / 'texts' / 'no50I_decode.txt').write_text('# SP 53/11 no. 50I decoded with the concordance and position corrections (r2k_wals_dec.py, after b37_wals_dec.py); . = null/space sign, #NN = label without a value\n' + '\n'.join(out) + '\n', encoding='utf8')
print('\n'.join(out))
