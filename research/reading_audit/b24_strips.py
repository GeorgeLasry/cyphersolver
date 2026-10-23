"""b24: find text lines by row ink profile and save zoomed strips (two halves per line), several lines per png.
    python b24_strips.py <img> <outprefix> y0 y1 [scale] [lines_per_png] [x0 x1]"""
import sys
from PIL import Image, ImageOps
im = Image.open(sys.argv[1]).convert('L')
y0, y1 = int(sys.argv[3]), int(sys.argv[4]); sc = float(sys.argv[5]) if len(sys.argv) > 5 else 2
per = int(sys.argv[6]) if len(sys.argv) > 6 else 5
X0, X1 = (int(sys.argv[7]), int(sys.argv[8])) if len(sys.argv) > 8 else (0, im.width)
px = im.load()
prof = [sum(1 for x in range(X0, X1, 2) if px[x, y] < 120) for y in range(y0, y1)]
lines, inl, s = [], False, 0
for i, v in enumerate(prof):
    if v > 4 and not inl: inl, s = True, i
    elif v <= 4 and inl:
        inl = False
        if i - s > 8: lines.append((y0 + s, y0 + i))
print(lines)
mid = (X0 + X1) // 2
rows = []
for a, b in lines:
    a, b = a - 12, b + 12
    for xa, xb in [(X0, mid + 40), (mid - 40, X1)]:
        c = im.crop((xa, a, xb, b)); c = c.resize((int(c.width * sc), int(c.height * sc)), Image.LANCZOS)
        rows.append(ImageOps.autocontrast(c, cutoff=1))
k = 0
for i in range(0, len(rows), per * 2):
    sub = rows[i:i + per * 2]
    out = Image.new('L', (max(r.width for r in sub), sum(r.height + 6 for r in sub)), 255); y = 0
    for r in sub: out.paste(r, (0, y)); y += r.height + 6
    out.save('%s_%d.png' % (sys.argv[2], k)); k += 1
