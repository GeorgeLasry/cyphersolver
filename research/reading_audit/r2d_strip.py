"""r2d (23 Oct 2026): crop transcription line(s) of a page image at native resolution, the line cut into two halves
stacked (left half above right half) so the digits stay legible.

    python research/reading_audit/r2d_strip.py <image> <out.jpg> <detected-line> [n-lines]
"""
import sys, pathlib
from PIL import Image
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import r2d_lines as R

im = Image.open(sys.argv[1]); Ls = R.find(im); W, H = im.size
d = int(sys.argv[3]); n = int(sys.argv[4]) if len(sys.argv) > 4 else 1
a, b = Ls[d - 1][0] - 25, Ls[d + n - 2][1] + 25
L = im.crop((0, a, W // 2 + 80, b)); Rr = im.crop((W // 2 - 80, a, W, b))
o = Image.new('RGB', (max(L.size[0], Rr.size[0]), L.size[1] * 2 + 8), 'white')
o.paste(L, (0, 0)); o.paste(Rr, (0, L.size[1] + 8))
o.save(sys.argv[2], quality=88); print(sys.argv[2], o.size)
