"""b17: look up battier1686 codebook groups on the key scans (NA 1.10.29 inv. 1209): for each block:number, find the
scan/side/column in key/colindex.txt, fetch the scan (cached in the scratchpad) and cut the rows around it.

    python research/reading_audit/b17_keylook.py <outdir> 12:909 4:696 ...
Writes <outdir>/k_<block>_<num>.jpg (five rows, the target in the middle) and prints the location.
Row geometry is approximate (36 rows a column, first row at 11.3% of the height, last at 90.7%).
"""
import os, sys, subprocess, pathlib
from PIL import Image, ImageOps
ROOT = pathlib.Path(__file__).resolve().parents[2]
COL = ROOT / 'targets' / 'battier1686' / 'key' / 'colindex.txt'
out = sys.argv[1]
os.makedirs(out, exist_ok=True)
cols = []
for line in open(COL, encoding='utf8'):
    if line.startswith('#') or not line.strip(): continue
    s, side, c, b, start = line.split()[:5]
    cols.append((int(s), side, int(c), int(b), int(start)))
XC = {('L', 1): (0.085, 0.225), ('L', 2): (0.225, 0.365), ('L', 3): (0.365, 0.505),
      ('R', 1): (0.525, 0.665), ('R', 2): (0.66, 0.80), ('R', 3): (0.795, 0.94)}
for tok in sys.argv[2:]:
    b, n = (int(x) for x in tok.split(':'))
    cand = [c for c in cols if c[3] == b and c[4] <= n]
    if not cand:
        print(tok, 'no column'); continue
    s, side, c, _, start = max(cand, key=lambda c: c[4])
    row = n - start
    f = os.path.join(out, 'NL-HaNA_1.10.29_1209_%04d.jpg' % s)
    if not os.path.exists(f):
        subprocess.run([sys.executable, str(ROOT / 'research' / 'reading_audit' / 'b17_na_fetch.py'), out, '1.10.29', '1209', str(s)], check=True)
    im = Image.open(f).convert('L'); X, Y = im.size
    y = 0.113 + row * (0.794 / 35)
    x0, x1 = XC[(side, c)]
    cc = ImageOps.autocontrast(im.crop((int((x0 - 0.03) * X), int((y - 0.05) * Y), int(x1 * X), int((y + 0.06) * Y))), cutoff=1)
    p = os.path.join(out, 'k_%d_%d.jpg' % (b, n)); cc.save(p)
    print(tok, 'scan', s, side, 'col', c, 'row', row + 1, p)

# contact sheet of this call's crops, side by side
_ims = [Image.open(os.path.join(out, 'k_%s.jpg' % t.replace(':', '_'))) for t in sys.argv[2:] if os.path.exists(os.path.join(out, 'k_%s.jpg' % t.replace(':', '_')))]
if _ims:
    _sheet = Image.new('L', (sum(i.size[0] for i in _ims), max(i.size[1] for i in _ims)), 255)
    _x = 0
    for _i in _ims:
        _sheet.paste(_i, (_x, 0)); _x += _i.size[0]
    _sheet.save(os.path.join(out, 'sheet.jpg')); print('sheet', _sheet.size)
