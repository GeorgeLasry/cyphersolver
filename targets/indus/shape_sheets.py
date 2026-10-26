"""Sheets for the shape-parallel chance test (set 639): the 42 graffiti base signs (tngraffiti.in images) and 90 signs
drawn at random (seed 639) from each of four inventories, rendered alike and labelled only P / Q / R / S."""
import csv
import io
import json
import os
import random
import urllib.request
from collections import Counter

from fontTools.ttLib import TTFont
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'data', 'shapes')
FONTS = os.path.join(OUT, 'fonts')
INDUS_FONT = r'C:/Users/dbour/indus_data/indus-website/src/assets/fonts/sk_indus_script-webfont.ttf'
N = 90


def cps(path, ranges):
    cmap = TTFont(path).getBestCmap()
    return [c for c in sorted(cmap) if any(a <= c <= b for a, b in ranges)]


def inventories():
    rnd = random.Random(639)
    inv = {}
    gl = {r['glyph']: r['codepoints'] for r in csv.DictReader(open(os.path.join(HERE, 'data', 'glyphs.tsv'), encoding='utf-8'), delimiter='\t') if r['codepoints']}
    used = Counter(g for r in csv.DictReader(open(os.path.join(HERE, 'data', 'corpus.tsv'), encoding='utf-8'), delimiter='\t') for g in r['signs_reading'].split())
    import numerals
    pool = sorted(g for g in used if g in gl and g not in numerals.NUMS and ' ' not in gl[g])
    inv['indus'] = (INDUS_FONT, [(g, int(gl[g], 16)) for g in rnd.sample(pool, N)])
    for name, f, rg in (('lineara', 'NotoSansLinearA-Regular.ttf', [(0x10600, 0x10736)]),
                        ('cyprominoan', 'NotoSansCyproMinoan-Regular.ttf', [(0x12F90, 0x12FF0)]),
                        ('linearb', 'NotoSansLinearB-Regular.ttf', [(0x10000, 0x1005D)])):
        p = os.path.join(FONTS, f)
        c = cps(p, rg)
        inv[name] = (p, [(hex(x), x) for x in rnd.sample(c, min(N, len(c)))])
    return inv


def sheet(items, title, path, font=None, imgs=None, cols=10, cell=110):
    rows = (len(items) + cols - 1) // cols
    im = Image.new('RGB', (cols * cell, rows * cell + 40), 'white')
    d = ImageDraw.Draw(im)
    lab = ImageFont.truetype('arial.ttf', 14)
    d.text((10, 10), title, fill='black', font=ImageFont.truetype('arial.ttf', 20))
    ft = ImageFont.truetype(font, 70) if font else None
    for k, it in enumerate(items):
        x, y = (k % cols) * cell, (k // cols) * cell + 40
        d.rectangle([x + 2, y + 2, x + cell - 2, y + cell - 2], outline='#bbbbbb')
        d.text((x + 5, y + 4), str(k + 1), fill='black', font=lab)
        if imgs:
            g = imgs[k].convert('L')
            g.thumbnail((cell - 30, cell - 30))
            im.paste(g.convert('RGB'), (x + (cell - g.width) // 2, y + 20))
        else:
            ch = chr(it[1])
            bb = d.textbbox((0, 0), ch, font=ft)
            w, h = bb[2] - bb[0], bb[3] - bb[1]
            d.text((x + (cell - w) // 2 - bb[0], y + 20 + (cell - 30 - h) // 2 - bb[1]), ch, fill='black', font=ft)
    im.save(path)


def main():
    os.makedirs(OUT, exist_ok=True)
    base = json.load(open(os.path.join(HERE, 'data', 'graffiti', 'raw', 'base-sign.json'), encoding='utf-8'))['data']
    base = sorted(base, key=lambda r: int(r['b_gov_sign']))
    imgs = []
    for r in base:
        url = 'https://graffiti-signs.s3.us-east-1.amazonaws.com/bv-signs/%s.png' % r['b_internal_sign']
        data = urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})).read()
        im = Image.open(io.BytesIO(data)).convert('RGBA')
        bg = Image.new('RGBA', im.size, 'white')
        imgs.append(Image.alpha_composite(bg, im))
    sheet([None] * len(base), 'Graffiti signs G1-G42', os.path.join(OUT, 'graffiti.png'), imgs=imgs)
    inv = inventories()
    labels = dict(zip(sorted(inv), 'PQRS'))
    key = {}
    for name, (font, items) in inv.items():
        L = labels[name]
        sheet(items, 'Inventory %s (%d signs)' % (L, len(items)), os.path.join(OUT, 'inventory_%s.png' % L), font=font)
        key[L] = {'inventory': name, 'signs': [i for i, c in items]}
    json.dump(key, open(os.path.join(OUT, 'KEY_do_not_show_scorers.json'), 'w'), indent=1)
    print({L: (v['inventory'], len(v['signs'])) for L, v in key.items()})


if __name__ == '__main__':
    main()
