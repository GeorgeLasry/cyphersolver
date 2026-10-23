"""b24 (bergamo1585): crop R16 transcription lines (L03-L35 = 206r, L37-L60 = 206v; centres by ink projection) as zoomed
halves, several lines stacked.   python b24_bg_line.py <imgdir> <out.png> L [L ...]"""
import sys
from PIL import Image, ImageOps
P1 = [513, 585, 655, 734, 808, 878, 947, 1021, 1096, 1168, 1241, 1323, 1397, 1473, 1546, 1626, 1696, 1774, 1842, 1921, 1998,
      2064, 2137, 2213, 2286, 2367, 2448, 2506, 2602, 2683, 2751, 2818, 2891]
P2 = [508, 580, 656, 738, 813, 885, 959, 1037, 1114, 1194, 1271, 1351, 1428, 1511, 1585, 1672, 1752, 1835, 1914, 1995, 2078,
      2162, 2238, 2323]
d, out = sys.argv[1], sys.argv[2]
rows = []
for a in sys.argv[3:]:
    ln = int(a)
    page, y = ('IMG_R16_I95_P1.jpg', P1[ln - 3]) if ln <= 35 else ('IMG_R16_I96_P2.jpg', P2[ln - 37])
    im = Image.open(d + '/' + page).convert('L')
    for xa, xb in [(150, 1100), (1000, 2000)]:
        c = im.crop((xa, y - 42, xb, y + 38)); c = c.resize((int(c.width * 1.3), int(c.height * 1.3)))
        rows.append(ImageOps.autocontrast(c, cutoff=1))
o = Image.new('L', (max(r.width for r in rows), sum(r.height + 8 for r in rows)), 255); y = 0
for r in rows: o.paste(r, (0, y)); y += r.height + 8
o.save(out)
