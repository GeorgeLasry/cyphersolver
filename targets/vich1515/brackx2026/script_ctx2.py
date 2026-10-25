# ctx2.py LABEL [LABEL...]: every occurrence of the split labels, with 9 tokens of decoded context on each side.
# Values in lower case; tentative values in {braces}; unread groups as [label]; unvalued signs as <label>; the label
# itself as >>label<<. Run from the vich1515 folder after renotate.py (reads tokens.tsv).
import csv, sys
T = list(csv.DictReader(open('tokens.tsv'), delimiter='\t'))
def show(r):
    v, s, l = r['value'], r['status'], r['split_label']
    if s == 'unread group': return f'[{l}]'
    if s == 'unvalued sign': return f'<{l}>'
    if s == 'tentative': return '{' + v + '}'
    return v if l != l.lower() else v.upper()
for lab in sys.argv[1:]:
    for i, r in enumerate(T):
        if r['split_label'] == lab:
            a = ''.join(show(x) for x in T[max(0, i - 9):i]); b = ''.join(show(x) for x in T[i + 1:i + 10])
            print(f"{lab:6} {r['line']:>3}.{r['position']:<3} {a[-45:]:>45} >>{lab}<< {b[:45]}")
