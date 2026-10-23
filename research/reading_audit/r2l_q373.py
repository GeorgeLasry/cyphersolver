"""r2l: one image per line of f. 373 (deskewed view), the line cut in four overlapping quarters, enlarged, stacked.
    python r2l_q373.py <view_r> <x0> <x1> <tag> <y> [<tag> <y> ...]"""
import sys
from PIL import Image, ImageOps
M = 'C:/Users/dbour/AppData/Local/Temp/claude/C--Users-dbour-cypher/6b6912a8-0ad3-4eda-b63e-c79291f1bcc5/scratchpad/reread/r2l/maisse/'
view, x0, x1 = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
im = Image.open(M + f'v{view}.jpg').convert('L')
args = sys.argv[4:]
q = (x1 - x0) // 4
for tag, y in zip(args[::2], map(int, args[1::2])):
    parts = []
    for i in range(4):
        c = im.crop((x0 + i * q - 40, y - 52, x0 + (i + 1) * q + 40, y + 52))
        c = c.resize((int(c.width * 1.35), int(c.height * 1.35)), Image.LANCZOS)
        parts.append(ImageOps.autocontrast(c, cutoff=1))
    out = Image.new('L', (parts[0].width, sum(p.height + 8 for p in parts)), 255)
    yy = 0
    for p in parts:
        out.paste(p, (0, yy)); yy += p.height + 8
    out.save(M + f'Q{tag}.png')
