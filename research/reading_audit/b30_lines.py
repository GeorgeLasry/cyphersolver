"""b30: one text line per row, each line cut in two halves stacked (left half above right half), k lines per image.

    python research/reading_audit/b30_lines.py <img> <outprefix> x0 x1 halfheight k y1 y2 y3 ...

The y values are line centres (from an ink-density profile). Images go to a scratch dir. 23 Oct 2026.
"""
import sys
from PIL import Image, ImageOps
Image.MAX_IMAGE_PIXELS = None
im = Image.open(sys.argv[1]).convert('L')
x0, x1, hh, k = map(int, sys.argv[3:7]); ys = list(map(int, sys.argv[7:]))
mid = (x0 + x1) // 2; ov = 120
for g in range(0, len(ys), k):
    rows = []
    for y in ys[g:g + k]:
        for a, b in ((x0, mid + ov), (mid - ov, x1)):
            rows.append(ImageOps.autocontrast(im.crop((a, y - hh, b, y + hh)), cutoff=1))
    W = max(r.width for r in rows); H = sum(r.height + 6 for r in rows)
    c = Image.new('L', (W, H), 0); yy = 0
    for r in rows:
        c.paste(r, (0, yy)); yy += r.height + 6
    sc = 1500 / W
    c.resize((1500, int(H * sc)), Image.LANCZOS).save(f'{sys.argv[2]}_{g // k:02d}.png')
print('done')
