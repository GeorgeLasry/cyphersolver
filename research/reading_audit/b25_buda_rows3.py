"""b25: find the text rows of V2831 p. 3 (img/v2831_p3r.jpg) by a horizontal ink profile in x-blocks, and cut each
row into pieces (crops into the scratchpad).
    python b25_buda_rows3.py rows            -> prints row centres per x-block
    python b25_buda_rows3.py crop <line> [n_pieces] [scale] [half_height]
"""
import sys, json
import numpy as np
from PIL import Image, ImageOps
IMG = r'C:\Users\dbour\cypher\targets\buda1489\img\v2831_p3r.jpg'
OUT = r'C:/Users/dbour/AppData/Local/Temp/claude/C--Users-dbour-cypher/6b6912a8-0ad3-4eda-b63e-c79291f1bcc5/scratchpad/reread/b25/buda_p3/'
X0, X1, Y0, Y1 = 1010, 2720, 850, 3110
BLOCKS = 6

def load():
    return np.asarray(Image.open(IMG).convert('L'), dtype=np.float32)

def rows(a):
    w = (X1 - X0) // BLOCKS
    res = []
    for b in range(BLOCKS):
        xs = slice(X0 + b * w, X0 + (b + 1) * w)
        prof = (255 - a[Y0:Y1, xs]).mean(axis=1)
        k = np.ones(15) / 15; p = np.convolve(prof, k, 'same')
        peaks = [i for i in range(20, len(p) - 20) if p[i] == p[i - 20:i + 21].max() and p[i] > p.mean()]
        res.append([Y0 + i for i in peaks])
    return res

def centres():
    return json.load(open(OUT + 'rows.json'))

if __name__ == '__main__':
    a = load()
    if sys.argv[1] == 'rows':
        r = rows(a)
        for b, pk in enumerate(r): print(b, len(pk), pk)
        json.dump(r, open(OUT + 'rows_raw.json', 'w'))
    elif sys.argv[1] == 'crop':
        ln = int(sys.argv[2]); n = int(sys.argv[3]) if len(sys.argv) > 3 else 3
        sc = float(sys.argv[4]) if len(sys.argv) > 4 else 2.5; hh = int(sys.argv[5]) if len(sys.argv) > 5 else 48
        y3 = json.load(open(OUT + 'rows_raw.json'))[3][ln - 1]   # block-3 centre (31 rows, consistent)
        w = (X1 - X0) // BLOCKS
        xb3 = X0 + w * 3.5
        dy = int(sys.argv[6]) if len(sys.argv) > 6 else 0          # manual vertical correction
        SL = float(sys.argv[7]) if len(sys.argv) > 7 else 0.0175  # slope (page y per page x)
        im = Image.open(IMG).convert('L')
        pw = (X1 - X0 + 60) // n
        for i in range(n):
            xa = X0 - 40 + i * pw; xb = xa + pw + 40
            yc = int(y3 + ((xa + xb) / 2 - xb3) * SL) + dy
            c = im.crop((xa, yc - hh, xb, yc + hh)); c = c.resize((int(c.width * sc), int(c.height * sc)), Image.LANCZOS)
            ImageOps.autocontrast(c, cutoff=1).save(OUT + f'L{ln:02d}_{i+1}.png')
        print('ok', ln)
