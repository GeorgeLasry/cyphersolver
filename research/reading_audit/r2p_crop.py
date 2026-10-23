"""r2p (23 Oct 2026; copy of r2d_mcrop.py), morosini1588: crop transcription line(s) of a DECODE cipher page (images fetched by batch b00 in
the session scratchpad), written to the r2d scratch folder. Same line arithmetic as reread_b00_crop.py; the crop is
cut in two halves stacked so the figures stay large.

    python research/reading_audit/r2p_crop.py R51 466r 3 [n] [shift]
"""
import os, sys
from PIL import Image
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import reread_b00_crop as C

OUT = r'C:\Users\dbour\AppData\Local\Temp\claude\C--Users-dbour-cypher\6b6912a8-0ad3-4eda-b63e-c79291f1bcc5\scratchpad\reread\r2p\crops'
rec, page, line = sys.argv[1], sys.argv[2], int(sys.argv[3])
n = int(sys.argv[4]) if len(sys.argv) > 4 else 1
sh = int(sys.argv[5]) if len(sys.argv) > 5 else 0   # shift in lines if the row grid is off
k = C.page_index(rec, page)[0]
im = Image.open(C.find_image(rec, k))
first, sp = C.grid(C.rows(im))
f0 = C.first_line(rec, page)
y0 = int(max(0, first + (line + sh - f0) * sp - sp * 0.7)); y1 = int(min(im.size[1], first + (line + sh + n - 1 - f0) * sp + sp * 0.7))
W = im.size[0]
L = im.crop((0, y0, W // 2 + 80, y1)); R = im.crop((W // 2 - 80, y0, W, y1))
o = Image.new('RGB', (L.size[0], L.size[1] * 2 + 8), 'white'); o.paste(L, (0, 0)); o.paste(R, (0, L.size[1] + 8))
os.makedirs(OUT, exist_ok=True)
p = os.path.join(OUT, f'{rec}_{page}_l{line}-{line + n - 1}.jpg'); o.save(p, quality=88); print(p, o.size)
