"""b19 (dedem1788): look codes up on the scans of Kroll's codebook, NA 1.02.20 (legatie Turkije) inv. 785
("Kroll. Un Chiffre", 6 scans). Each 500-group block is a page of five columns of 100: column c (0-4) holds codes
B + 100c + row, row 1-88 written as "word  number", rows 89-100 in a small table at the foot of the column.
For each code a window of rows r-2..r+2 of its column is cut and the windows are stacked into montage images,
labelled with the code, so the word can be read next to its printed number.

    python b19_keylook.py <scan_dir> <out_prefix> <code> [<code> ...]

Calibration (full-resolution pixels, measured on the header and foot strips, 23 Oct 2026): for each block the
scan, the x of the printed number of each column, and y of rows 2 and 88.
"""
import os, sys
from PIL import Image, ImageDraw
Image.MAX_IMAGE_PIXELS = None

CAL = {  # block start: (scan, [x of number col 0..4], y row2, y row88)
    1:    (2, [300, 600, 905, 1190, 1500], 86, 2895),
    501:  (2, [1795, 2107, 2420, 2700, 2990], 88, 2890),
    1001: (2, [3283, 3607, 3907, 4200, 4493], 92, 2892),
    1501: (3, [2600, 2871, 3143, 3414, 3686], 67, 2677),
    2001: (4, [871, 1150, 1429, 1707, 1993], 67, 2677),
    2501: (4, [2250, 2536, 2821, 3086, 3357], 67, 2677),
    3001: (4, [3700, 3971, 4243, 4507, 4786], 67, 2677),
    3501: (5, [3729, 4014, 4300, 4586, 4871], 67, 2868),
}
CELLW = 300


def window(code):
    b = ((code - 1) // 500) * 500 + 1
    scan, xs, y2, y88 = CAL[b]
    off = code - b
    col, row = off // 100, off % 100 + 1
    xr = xs[col] + 45
    xl = xs[col] - CELLW
    pitch = (y88 - y2) / 86.0
    if row <= 88:
        yc = y2 + (row - 2) * pitch
        box = (xl - 10, int(yc - 2.4 * pitch), xr, int(yc + 2.4 * pitch))
    else:  # foot table
        box = (xl - 10, int(y88 + 0.4 * pitch), xr, int(y88 + 7.6 * pitch))
    return scan, box, row


def main(d, out, codes):
    tiles = []
    for c in codes:
        scan, box, row = window(c)
        im = Image.open(os.path.join(d, 'NL-HaNA_1.02.20_785_%04d.jpg' % scan)).convert('L')
        t = im.crop(box)
        lab = Image.new('L', (t.size[0], 26), 255)
        ImageDraw.Draw(lab).text((4, 4), '%d  (row %d%s)' % (c, row, ', foot table' if row > 88 else ''), fill=0)
        tile = Image.new('L', (t.size[0], t.size[1] + 26), 255)
        tile.paste(lab, (0, 0)); tile.paste(t, (0, 26))
        tiles.append(tile)
    per = 12
    for k in range(0, len(tiles), per):
        grp = tiles[k:k + per]
        half = (len(grp) + 1) // 2
        cols = [grp[:half], grp[half:]]
        w = sum(max(t.size[0] for t in c) for c in cols if c) + 20
        h = max(sum(t.size[1] + 6 for t in c) for c in cols if c)
        m = Image.new('L', (w, h), 255)
        x = 0
        for c in cols:
            y = 0
            for t in c:
                m.paste(t, (x, y)); y += t.size[1] + 6
            if c: x += max(t.size[0] for t in c) + 20
        p = '%s_%02d.jpg' % (out, k // per)
        m.save(p, quality=88); print(p, m.size, codes[k:k + per])


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], [int(a) for a in sys.argv[3:]])
