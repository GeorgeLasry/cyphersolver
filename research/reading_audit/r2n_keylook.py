"""r2n: battier1686 key lookup with taller crops (b17_keylook geometry, +-6 rows) stacked vertically in one sheet.
    python research/reading_audit/r2n_keylook.py <outdir> <sheetname> 12:909 4:696 ...
Key scans must be cached in <outdir> (NL-HaNA_1.10.29_1209_NNNN.jpg); missing ones are fetched with b17_na_fetch.py."""
import os, sys, subprocess, pathlib
from PIL import Image, ImageOps, ImageDraw
ROOT = pathlib.Path(__file__).resolve().parents[2]
COL = ROOT / 'targets' / 'battier1686' / 'key' / 'colindex.txt'
out, sheetname = sys.argv[1], sys.argv[2]
cols = []
for line in open(COL, encoding='utf8'):
    if line.startswith('#') or not line.strip(): continue
    s, side, c, b, start = line.split()[:5]
    cols.append((int(s), side, int(c), int(b), int(start)))
XC = {('L', 1): (0.085, 0.225), ('L', 2): (0.225, 0.365), ('L', 3): (0.365, 0.505),
      ('R', 1): (0.525, 0.665), ('R', 2): (0.66, 0.80), ('R', 3): (0.795, 0.94)}
ims = []
for tok in sys.argv[3:]:
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
    cc = ImageOps.autocontrast(im.crop((int((x0 - 0.01) * X), int((y - 0.12) * Y), int((x1 + 0.005) * X), int((y + 0.13) * Y))), cutoff=1)
    cc = cc.resize((cc.size[0] * 2 // 3, cc.size[1] * 2 // 3))
    lab = Image.new('L', (cc.size[0], 26), 255); ImageDraw.Draw(lab).text((5, 5), '%s  (scan %d%s col %d)' % (tok, s, side, c), fill=0)
    t = Image.new('L', (cc.size[0], cc.size[1] + 26), 255); t.paste(lab, (0, 0)); t.paste(cc, (0, 26)); ims.append(t)
    print(tok, 'scan', s, side, 'col', c, 'row', row + 1)
# grid: 4 per row
per = 4
rows = [ims[i:i + per] for i in range(0, len(ims), per)]
W = max(sum(i.size[0] for i in r) for r in rows); H = sum(max(i.size[1] for i in r) for r in rows)
sh = Image.new('L', (W, H), 255); y = 0
for r in rows:
    x = 0
    for i in r: sh.paste(i, (x, y)); x += i.size[0]
    y += max(i.size[1] for i in r)
p = os.path.join(out, sheetname + '.jpg'); sh.save(p, quality=88); print(p, sh.size)
