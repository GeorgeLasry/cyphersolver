"""v5 (b): nunzio1718 - per figure line of lasry/364D-<n>.txt, the DECODE transcriber's PLAINTEXT row (P, their copy of
the contemporary interlinear decipherment) beside Lasry's decode row joined (L, key_extra + adopted b22 values applied,
as v5b_nunzio_rows.py). For building the reading by hand.

    python research/reading_audit/v5b_nunzio_side.py <n>
"""
import pathlib, re, sys
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from v5b_nunzio_rows import T, OV

n = sys.argv[1]
ls = (T / 'lasry' / f'364D-{n}.txt').read_text(encoding='utf8', errors='replace').splitlines()
pend, k = None, 0
for i, l in enumerate(ls):
    m = re.match(r'^<PLAINTEXT \w+ (.*)>\s*$', l)
    if m: pend = m.group(1); continue
    if l.startswith('#IMAGE') and re.search(r'\d+[rv]\.jpg', l): print('==', l.split(':', 1)[1].strip()); continue
    if l.startswith('<CLEARTEXT'): print('   {' + l[11:].rstrip('>').strip() + '}'); continue
    if not re.match(r'^[\d ?\-]+\|\s*$', l) or i + 1 >= len(ls): continue
    figs = l.split('|')[0].split(); vals = ls[i + 1].split('|')[0].split()
    s = ''
    for j, v in enumerate(vals):
        f = figs[j] if j < len(figs) else ''
        if v == '_' or f == '3': continue
        if f in OV: v = OV[f]
        if re.fullmatch(r'\d+\?|\?', v): s += f'<{f}?>'; continue
        mm = re.fullmatch(r'<(\d+)>', v)
        if mm: s += f'[{mm.group(1)}]'; continue
        v = v.replace('u/v', 'u').split('/')[0]
        s += ('·' + v + '·') if (v[:1].isupper() or '.' in v or len(v) > 3) else v
    k += 1
    print(f'{k:3d} P: {pend if pend is not None else "-"}')
    print(f'    L: {s}')
    pend = None
