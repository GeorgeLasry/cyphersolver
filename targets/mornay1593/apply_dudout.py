"""Apply Brice Dudout's key (key_dudout.tsv) to ciphertext.txt; print each passage and the share of groups read."""
import sys
from pathlib import Path
here = Path(__file__).parent
key = {}
for l in (here / 'key_dudout.tsv').read_text(encoding='utf-8').splitlines():
    if l and not l.startswith('#'):
        n, c = l.split('\t'); key[n] = c
def group(g):
    """All readings of a group: one sign, or two signs split anywhere. Ambiguous splits come back as {x/y}."""
    alts = [key[g]] if g in key else []
    alts += [key[g[:k]] + key[g[k:]] for k in range(1, len(g)) if g[:k] in key and g[k:] in key]
    if not alts: return None
    return alts[0] if len(alts) == 1 else '{' + '/'.join(alts) + '}'

tot = ok = 0
for l in (here / 'ciphertext.txt').read_text(encoding='utf-8').splitlines():
    if not l or l.startswith('#'): continue
    f = [x.strip() for x in l.split('|')]
    out = []
    for g in f[4].split():
        r = group(g); tot += 1; ok += r is not None
        out.append(r if r else f'[{g}]')
    print(f[0], ''.join(out))
print(f'groups read: {ok}/{tot} = {100*ok/tot:.1f}%')
