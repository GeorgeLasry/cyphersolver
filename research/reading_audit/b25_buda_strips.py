"""b25: per-row strips of a Buda plate. python b25_buda_strips.py <img> <outdir> <prefix> <yL16> <step> <first> <last> [dy]
Line n centre = yL16 + step*(n-16) + dy; four horizontal pieces, scale 2.5, autocontrast."""
import sys
from PIL import Image, ImageOps
img, out, pre = sys.argv[1:4]; y16, step = float(sys.argv[4]), float(sys.argv[5]); a, b = int(sys.argv[6]), int(sys.argv[7])
dy = float(sys.argv[8]) if len(sys.argv) > 8 else 0
im = Image.open(img).convert('L')
X = [(930, 1560), (1500, 2130), (2070, 2760)]
for n in range(a, b + 1):
    yc = int(y16 + step * (n - 16) + dy)
    for k, (x0, x1) in enumerate(X, 1):
        c = im.crop((x0, yc - 62, x1, yc + 50)); c = c.resize((int(c.width * 2.5), int(c.height * 2.5)), Image.LANCZOS)
        ImageOps.autocontrast(c, cutoff=1).save(f'{out}/{pre}L{n:02d}_{k}.png')
    print(n, yc)
