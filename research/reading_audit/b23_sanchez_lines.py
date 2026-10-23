"""b23 (sanchez1522 R9635): cut one cipher line into two overlapping halves at 2x for reading by eye.
    python b23_sanchez_lines.py <img> <x0> <x1> <outprefix> <y_center> [<y_center> ...]"""
import sys
from PIL import Image, ImageOps
f, x0, x1, out = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
im = Image.open(f).convert('L')
for n, y in enumerate(int(v) for v in sys.argv[5:]):
    m = (x0 + x1) // 2
    for h, (a, b) in enumerate([(x0, m + 60), (m - 60, x1)]):
        c = ImageOps.autocontrast(im.crop((a, y - 42, b, y + 38)), cutoff=1)
        c = c.resize((c.size[0] * 2, c.size[1] * 2), Image.LANCZOS)
        c.save('%s_%02d%s.png' % (out, n + 1, 'ab'[h]))
