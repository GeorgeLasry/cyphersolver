"""b30: cut a page image into horizontal strips (autocontrast, optional width) for reading, into a scratch dir.

    python research/reading_audit/b30_strips.py <img> <outprefix> x0 y0 x1 y1 nstrips [outwidth]

Used for BnF fr. 3985 f. 20 / f. 7 (mauclerc1593) and the other b30 targets, 23 Oct 2026.
"""
import sys
from PIL import Image, ImageOps
Image.MAX_IMAGE_PIXELS = None
im = Image.open(sys.argv[1]).convert('L')
x0, y0, x1, y1, n = map(int, sys.argv[3:8])
ow = int(sys.argv[8]) if len(sys.argv) > 8 else 1800
h = (y1 - y0) / n
for i in range(n):
    a = int(y0 + i * h - 30); b = int(y0 + (i + 1) * h + 30)
    c = im.crop((x0, max(a, 0), x1, min(b, im.height)))
    c = ImageOps.autocontrast(c, cutoff=1)
    c = c.resize((ow, int(c.height * ow / c.width)), Image.LANCZOS)
    c.save(f'{sys.argv[2]}_{i:02d}.png')
    print(f'{sys.argv[2]}_{i:02d}.png')
