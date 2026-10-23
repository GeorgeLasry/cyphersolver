"""b18 fork C: cut given line centres (fractions of height) of an R9957 page into two half-line crops.
    python research/reading_audit/b18_r9957C_rows.py <page> <tag> <half-height frac> <scale> c1 c2 ...
"""
import sys, pathlib
from PIL import Image, ImageOps
OUT = pathlib.Path(r'C:\Users\dbour\AppData\Local\Temp\claude\C--Users-dbour-cypher\6b6912a8-0ad3-4eda-b63e-c79291f1bcc5\scratchpad\reread\b18\C')
pg, tag, hh, sc = sys.argv[1], sys.argv[2], float(sys.argv[3]), float(sys.argv[4])
im = Image.open(rf'C:\Users\dbour\cypher\targets\charles1536\img\r9957_p{pg}.jpg').convert('L'); W, H = im.size
for n, c in enumerate(sys.argv[5:]):
    c = float(c)
    for half, (xa, xb) in (('a', (0.06, 0.54)), ('b', (0.48, 0.99))):
        cr = ImageOps.autocontrast(im.crop((int(xa*W), int((c-hh)*H), int(xb*W), int((c+hh)*H))), cutoff=1)
        cr = cr.resize((int(cr.width*sc), int(cr.height*sc)), Image.LANCZOS)
        cr.save(OUT / f'{tag}{n:02d}{half}.jpg', quality=92)
print('ok')
