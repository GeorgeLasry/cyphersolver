"""b23 (sanchez1522 R9635): align the reading body word by word with the contemporary decipherment (f. 22r) and list
every unbracketed reading word that the decipherment does not carry (expansions of its abbreviations allowed).
    python b23_sanchez_align.py <reading.md> <decifrado.txt>"""
import re, sys, difflib, pathlib
EXP = {'vuestra': ['v.', 'vra.'], 'magestad': ['mad.', 'ma.']}
r = pathlib.Path(sys.argv[1]).read_text(encoding='utf8')
body = re.search(r'^## Reading\n(.*?)(?=^## )', r, re.S | re.M).group(1)
d = '\n'.join(l[3:] for l in pathlib.Path(sys.argv[2]).read_text(encoding='utf8').splitlines() if not l.startswith('#'))
norm = lambda s: re.sub(r'[^\wñ\[\]?….]', ' ', s.lower())
rw = [w for w in norm(body).split() if w]
dw = [w.strip('.') if w not in ('v.', 'vra.', 'mad.', 'ma.') else w for w in norm(d).replace('/', ' ').split()]
# join decipherment words split by line breaks / clitics so 'dixeles', 'pagarlos', 'respondieronme' match
dj = ' '.join(dw)
plain = [w.strip('.') for w in rw if not w.startswith('[')]
unc = []
for w in plain:
    if w in dw or any(a in dw for a in EXP.get(w, [])):
        continue
    if w.replace(' ', '') in dj.replace(' ', ''):  # carried across a split (pagar los -> pagarlos)
        continue
    unc.append(w)
print('reading words (unbracketed):', len(plain), 'not carried:', len(unc), unc)
