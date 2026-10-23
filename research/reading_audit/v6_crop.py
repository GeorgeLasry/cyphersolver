"""v6: overview and horizontal strips of a page image, for reading in the writer's spelling.
    python v6_crop.py <image> <outprefix> [n_strips=8] [x0 x1 y0 y1 as fractions]"""
import sys
from PIL import Image
im = Image.open(sys.argv[1]).convert('L')
W, H = im.size
n = int(sys.argv[3]) if len(sys.argv) > 3 else 8
x0, x1, y0, y1 = [float(v) for v in sys.argv[4:8]] if len(sys.argv) > 7 else (0, 1, 0, 1)
box = (int(x0 * W), int(y0 * H), int(x1 * W), int(y1 * H))
reg = im.crop(box)
ov = reg.copy(); ov.thumbnail((1400, 1400)); ov.save(sys.argv[2] + '_ov.jpg', quality=85)
rh = reg.size[1] / n
for i in range(n):
    s = reg.crop((0, int(max(0, i * rh - rh * 0.12)), reg.size[0], int(min(reg.size[1], (i + 1) * rh + rh * 0.12))))
    s.thumbnail((2000, 2000)); s.save(f'{sys.argv[2]}_s{i}.jpg', quality=88)
print(W, H, box)
