"""r2n: for each number, cut the key rows around it in every block (1-15), labelled, in one sheet per call.
    python research/reading_audit/r2n_allblocks.py <keydir> <sheetname> 296 526 ...
Rows are approximate (b17 geometry); each crop is +-3 rows so the target row is inside."""
import os, sys, subprocess, pathlib
from PIL import Image, ImageOps, ImageDraw
ROOT = pathlib.Path(__file__).resolve().parents[2]
COL = ROOT / 'targets' / 'battier1686' / 'key' / 'colindex.txt'
out, sheetname = sys.argv[1], sys.argv[2]
blocks = [int(b) for b in os.environ.get('BLOCKS', '1,2,3,4,5,6,7,8,9,10,11,12,13,14,15').split(',')]
cols = []
for line in open(COL, encoding='utf8'):
    if line.startswith('#') or not line.strip(): continue
    s, side, c, b, start = line.split()[:5]
    cols.append((int(s), side, int(c), int(b), int(start)))
XC = {('L', 1): (0.085, 0.225), ('L', 2): (0.225, 0.365), ('L', 3): (0.365, 0.505),
      ('R', 1): (0.525, 0.665), ('R', 2): (0.66, 0.80), ('R', 3): (0.795, 0.94)}
cache = {}
tiles = []
for num in sys.argv[3:]:
    n = int(num)
    for b in blocks:
        cand = [c for c in cols if c[3] == b and c[4] <= n]
        if not cand: continue
        s, side, c, _, start = max(cand, key=lambda c: c[4])
        row = n - start
        if row > 40: continue
        f = os.path.join(out, 'NL-HaNA_1.10.29_1209_%04d.jpg' % s)
        if not os.path.exists(f):
            subprocess.run([sys.executable, str(ROOT / 'research' / 'reading_audit' / 'b17_na_fetch.py'), out, '1.10.29', '1209', str(s)], check=True)
        if f not in cache: cache[f] = Image.open(f).convert('L')
        im = cache[f]; X, Y = im.size
        y = 0.113 + row * (0.794 / 35)
        x0, x1 = XC[(side, c)]
        cc = ImageOps.autocontrast(im.crop((int((x0 - 0.005) * X), int((y - 0.075) * Y), int((x1 + 0.005) * X), int((y + 0.08) * Y))), cutoff=1)
        cc = cc.resize((int(cc.size[0] * 0.42), int(cc.size[1] * 0.42)))
        lab = Image.new('L', (cc.size[0], 18), 255); ImageDraw.Draw(lab).text((3, 3), '%d:%d s%d%s%d' % (b, n, s, side, c), fill=0)
        t = Image.new('L', (cc.size[0], cc.size[1] + 18), 255); t.paste(lab, (0, 0)); t.paste(cc, (0, 18)); tiles.append(t)
per = int(os.environ.get('PER', '8'))
rows = [tiles[i:i + per] for i in range(0, len(tiles), per)]
W = max(sum(i.size[0] for i in r) for r in rows); H = sum(max(i.size[1] for i in r) for r in rows)
sh = Image.new('L', (W, H), 255); y = 0
for r in rows:
    x = 0
    for i in r: sh.paste(i, (x, y)); x += i.size[0] + 4
    y += max(i.size[1] for i in r)
p = os.path.join(out, sheetname + '.jpg'); sh.save(p, quality=85); print(p, sh.size, len(tiles))
