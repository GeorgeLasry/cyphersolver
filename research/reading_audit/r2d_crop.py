"""r2d (23 Oct 2026): cut a DECODE page image into horizontal bands for reading at full resolution.

    python research/reading_audit/r2d_crop.py <image> <out-prefix> <n-bands> [x0 x1] [y0 y1]   (fractions)
"""
import sys
from PIL import Image
f, out, n = sys.argv[1], sys.argv[2], int(sys.argv[3])
x0, x1 = (float(sys.argv[4]), float(sys.argv[5])) if len(sys.argv) > 5 else (0.0, 1.0)
y0, y1 = (float(sys.argv[6]), float(sys.argv[7])) if len(sys.argv) > 7 else (0.0, 1.0)
im = Image.open(f).convert('RGB'); W, H = im.size
h = (y1 - y0) / n
for i in range(n):
    a, b = y0 + i * h, y0 + (i + 1) * h + 0.01
    c = im.crop((int(x0 * W), int(a * H), int(x1 * W), int(min(1, b) * H)))
    if c.size[0] > 1800: c = c.resize((1800, int(c.size[1] * 1800 / c.size[0])))
    c.save(f'{out}_{i + 1}.jpg', quality=85); print(f'{out}_{i + 1}.jpg', c.size)
