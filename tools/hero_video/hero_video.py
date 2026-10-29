"""Render the site's two pixel-art videos: the front page's 41-second cut and the full cut on the contribute page.

    python tools/hero_video/hero_video.py                      # the front-page cut: docs/hero.mp4 + poster
    python tools/hero_video/hero_video.py --cut full           # the contribute page's: docs/hero_full.mp4 + poster
    python tools/hero_video/hero_video.py --sheet sheet.png    # contact sheet, one frame every 2 s
    python tools/hero_video/hero_video.py --still 6.5 f.png    # one frame, 2x
    python tools/hero_video/hero_video.py --audio mix.wav      # with the soundtrack from audio.py (same --cut)
    python tools/hero_video/hero_video.py --featured marmont1812  # this cipher instead of the week's

Drawn at 320x180 and scaled 4x without smoothing, so every art pixel is a 4x4 block. The counts and the timeline
dots are read from docs/index.html, so a re-render after a site build shows the current ledger. The cipher the
video deciphers is a real passage from docs/reveal/, one of featured.json's, a different one each ISO week. The
narration is burned in as captions, because the page plays the video muted until someone asks for sound. A render
of a cut also writes its chapters, its links and a fresh ?v= into its page (CUTS[...]['page']). Needs Pillow, numpy,
and ffmpeg on PATH.

Storyboard of the front-page cut (seconds; CUTS below is the source of truth, and audio.py follows it):
  0-11.25     the week's cipher: the manuscript, then its figures deciphered against the key; the English
  11.25-18.75 the ledger: the timeline fills while the years of silence count up; the oldest entry and a
              failure, close up
  18.75-32.5  how to contribute: pick from the catalogue or Read Further, paste the page into Claude Code, which
              works through it and reports back; credited by name
  32.5-37.5   to the archive: the archives with the most open requests (archive_requests.json); one is taken
  37.5-41.25  pick a cipher, break it, write it up (the page puts its buttons over the end)
The full cut adds "how it works" after the cipher, the headline counts and the paper.
"""
import argparse
import datetime
import html
import json
import math
import random
import re
import subprocess
import sys
import unicodedata
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw

sys.path.insert(0, str(Path(__file__).resolve().parent))
from assets import FLAMES, FONT, SIGNS, SPRITES, parse  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
DOCS = ROOT / 'docs'
W, H, FPS = 320, 180, 30
DUR = 30.0             # of the cut being rendered; main() sets it from CUTS
SCALE = 4


def hx(s):
    s = s.lstrip('#')
    return tuple(int(s[i:i + 2], 16) for i in (0, 2, 4))


def mix(a, b, t):
    return tuple(round(a[i] + (b[i] - a[i]) * t) for i in range(3))


# the site's palette (docs/style.css, dark theme) plus the browns, parchments and night blues the scenes need
C = dict(
    void=hx('05070b'), night=hx('0c0f15'), night2=hx('121724'), night3=hx('1b2335'), night4=hx('283350'),
    night5=hx('3a4a6e'), ink=hx('e9e4d8'), ink2=hx('c9c3b4'), muted=hx('8f8a7d'), dim=hx('4d4a44'),
    gold=hx('d9ac52'), gold2=hx('f0cf86'), goldhi=hx('fff6dc'), golddk=hx('8a6716'), golddk2=hx('3d2d0e'),
    parch=hx('e8d9b0'), parch2=hx('d4c294'), parch3=hx('b39d6c'), parchdk=hx('7d6a45'),
    wood=hx('22180f'), wood2=hx('3a281a'), wood3=hx('5a3e27'), wood4=hx('7d5937'),
    red=hx('b3402f'), red2=hx('ff8d7e'), reddk=hx('6e2219'), green=hx('6fd39a'), greendk=hx('2f7d4f'),
    blue=hx('7fb3ff'), bluedk=hx('2b5fa8'), violet=hx('b9a8ff'), amber=hx('ecc25a'), orange=hx('e08a3a'),
    clerk=hx('8c3b22'), sepia=hx('3a2a1a'), white=hx('ffffff'),
)
SPAL = dict(k=hx('120e0a'), G=C['gold'], g=C['golddk'], H=C['gold2'], P=C['parch'], p=C['parch3'], d=C['parchdk'],
            R=C['red'], r=C['reddk'], W=C['goldhi'], w=C['ink2'], n=hx('6b5a40'), E=C['green'], e=C['greendk'],
            B=C['blue'], b=C['bluedk'], V=C['violet'], s=hx('6d7690'), S=hx('aab4cc'), o=C['orange'], y=C['gold2'])
# outcome colours of the timeline, as the scoreboard on the index page mixes them
CAT = dict(ct=C['green'], extpt=mix(C['green'], C['blue'], .35), adjpt=mix(C['green'], C['blue'], .6),
           extkey=C['violet'], known=mix(C['violet'], C['blue'], .5), deciph=C['amber'], notsolved=C['red2'],
           na=C['muted'], active=C['gold'])


# ---------------------------------------------------------------- dithering

def _bayer(n):
    if n == 1:
        return np.zeros((1, 1))
    b = _bayer(n // 2)
    return np.block([[4 * b, 4 * b + 2], [4 * b + 3, 4 * b + 1]])


B8 = (_bayer(8) + .5) / 64


def tile_th(h, w):
    return np.tile(B8, (h // 8 + 1, w // 8 + 1))[:h, :w]


TH = tile_th(H, W)
_yy, _xx = np.mgrid[:H, :W]
VIG = np.clip((np.hypot((_xx - W / 2) / (W / 2), (_yy - H / 2) / (H / 2)) - .82) * 1.4, 0, .75)


def clamp(x, a=0., b=1.):
    return a if x < a else b if x > b else x


def ease(x):
    x = clamp(x)
    return x * x * (3 - 2 * x)


def ease_out(x):
    x = clamp(x)
    return 1 - (1 - x) ** 3


def dither(a, level, col, th=TH):
    """Paint col wherever the Bayer threshold is under level (a number or an array)."""
    a[th < level] = col


def dissolve(a, b, p):
    """b replaces a pixel by pixel as p goes 0 -> 1."""
    m = TH < p
    a[m] = b[m]
    return a


def light(a, cx, cy, r, col, amt, th=TH):
    """Warm or cold light in dithered bands, added to what is there."""
    h, w = a.shape[:2]
    yy, xx = np.ogrid[:h, :w]
    lv = np.clip(1 - np.hypot(xx - cx, (yy - cy) * 1.15) / r, 0, 1) ** 1.5 * amt
    q = np.clip(np.floor(lv * 4 + th) / 4, 0, 1)[..., None]
    out = a.astype(np.float32) * (1 + .55 * q) + np.array(col, np.float32) * .32 * q
    a[:] = np.clip(out, 0, 255).astype(np.uint8)


# ---------------------------------------------------------------- canvas, text and sprites

class Cv:
    def __init__(self, a):
        self.im = Image.fromarray(a)
        self.d = ImageDraw.Draw(self.im)

    @classmethod
    def blank(cls, col=None):
        return cls(np.full((H, W, 3), col or C['night'], np.uint8))

    def a(self):
        return np.asarray(self.im).copy()

    def set(self, a):
        self.im = Image.fromarray(a)
        self.d = ImageDraw.Draw(self.im)

    def rect(self, x, y, w, h, c):
        if w > 0 and h > 0:
            self.d.rectangle([x, y, x + w - 1, y + h - 1], fill=c)

    def box(self, x, y, w, h, c):
        self.d.rectangle([x, y, x + w - 1, y + h - 1], outline=c)

    def line(self, x0, y0, x1, y1, c):
        self.d.line([x0, y0, x1, y1], fill=c)

    def px(self, x, y, c):
        if 0 <= x < self.im.width and 0 <= y < self.im.height:
            self.im.putpixel((int(x), int(y)), c)


_gm = {}


def gmask(ch, scale, sign=False):
    key = (ch, scale, sign)
    if key not in _gm:
        rows, w = SIGNS[ch] if sign else FONT[ch]
        m = Image.new('L', (max(w, 1) * scale, 7 * scale), 0)
        for y, row in enumerate(rows):
            for x, v in enumerate(row):
                if v == '#':
                    m.paste(255, (x * scale, y * scale, (x + 1) * scale, (y + 1) * scale))
        _gm[key] = (m, w)
    return _gm[key]


def tw(s, scale=1, sp=1):
    if not s:
        return 0
    return (sum((3 if ch == ' ' else FONT[ch][1]) + sp for ch in s) - sp) * scale


def text(cv, s, x, y, col, scale=1, align='l', shadow=None, upto=None, sp=1):
    if align == 'c':
        x -= tw(s, scale, sp) // 2
    elif align == 'r':
        x -= tw(s, scale, sp)
    if shadow is not None:
        o = max(1, scale - 1)
        text(cv, s, x + o, y + o, shadow, scale, 'l', None, upto, sp)
    n = len(s) if upto is None else max(0, min(len(s), upto))
    cx = x
    for ch in s[:n]:
        if ch == ' ':
            cx += (3 + sp) * scale
            continue
        m, w = gmask(ch, scale)
        cv.im.paste(col, (cx, y), m)
        cx += (w + sp) * scale
    return cx


def typed(t, t0, cps=32):
    return int((t - t0) * cps) if t >= t0 else -1


def text_lines(cv, lines, x, y, t, t0, col, scale=1, lh=None, align='c', shadow=C['void'], cps=32, cursor=True):
    """Type lines out one after another, with a block cursor while typing."""
    lh = lh or 9 * scale + (scale > 1) * 2
    n = typed(t, t0, cps)
    if n < 0:
        return
    for i, s in enumerate(lines):
        k = min(n, len(s))
        if k > 0:
            if align == 'c':
                x0 = x - tw(s, scale) // 2
            else:
                x0 = x
            end = text(cv, s, x0, y + i * lh, col, scale, 'l', shadow, k)
            if cursor and n < len(s) and int(t * 6) % 2 == 0:
                cv.rect(end + scale, y + i * lh, 4 * scale, 7 * scale, col)
        elif n == 0 and i == 0 and cursor and int(t * 6) % 2 == 0:
            x0 = x - tw(s, scale) // 2 if align == 'c' else x
            cv.rect(x0, y, 4 * scale, 7 * scale, col)
        n -= len(s)
        if n <= 0:
            break


_sp = {}


def sprite(src, scale=1, flip=False, pal=None):
    key = (src, scale, flip, tuple(sorted(pal.items())) if pal else None)
    if key not in _sp:
        rows = parse(src)
        p = dict(SPAL, **(pal or {}))
        h, w = len(rows), len(rows[0])
        im = Image.new('RGBA', (w * scale, h * scale), (0, 0, 0, 0))
        dr = ImageDraw.Draw(im)
        for y, row in enumerate(rows):
            for x, v in enumerate(row[::-1] if flip else row):
                if v != '.':
                    dr.rectangle([x * scale, y * scale, x * scale + scale - 1, y * scale + scale - 1], fill=p[v] + (255,))
        _sp[key] = im
    return _sp[key]


def blit(cv, name, x, y, scale=1, flip=False, pal=None, src=None):
    im = sprite(src or SPRITES[name], scale, flip, pal)
    cv.im.paste(im, (int(x), int(y)), im)
    return im.size


def flame(cv, x, y, t, k=0):
    f = FLAMES[(int(t * 10) + k * 3 + (int(t * 23) % 3 == 0)) % len(FLAMES)]
    blit(cv, None, x, y, src=f)


def flicker(t, k=0):
    return .82 + .1 * math.sin(t * 17 + k) + .08 * math.sin(t * 41 + 2 * k)


# ---------------------------------------------------------------- data from the site

def ledger():
    s = (DOCS / 'index.html').read_text(encoding='utf8')

    def num(pat):
        m = re.search(pat, s, re.S)
        if not m:
            sys.exit(f'docs/index.html: pattern not found: {pat}')
        return m.group(1)

    # the counts are floored and given with a "+", so the video stays true as the ledger grows
    L = {k: floor(num(pat)) for k, pat in dict(
        entries=r'<b>([\d,]+)</b> entries',
        keys=r'<b>([\d,]+)</b> keys recovered',
        silence=r'<b>([\d,]+)</b> years of silence',
    ).items()}
    dots = []
    for c, href, lab, y in re.findall(r'<a class="pt (\w+)" href="([^"]+)" aria-label="([^"]*)"[^>]*?data-year="(\d+)"', s):
        dots.append((int(y), c, caps(html.unescape(lab).split(',')[0]), href))
    L['dots'] = sorted(dots, key=lambda d: d[0])
    years = [d[0] for d in L['dots']]
    L['first'], L['last'] = min(years), max(years)
    # the two entries the ledger scene picks out: the oldest text recovered, and the oldest entry if it failed
    L['oldest_read'] = next(d for d in L['dots'] if d[1] not in ('notsolved', 'na', 'active'))
    L['oldest'] = L['dots'][0]
    return L


def shown(L):
    """What a render puts on screen from the site's data; update.py compares it with the site to see if it is stale."""
    return {k: L[k] for k in ('entries', 'keys', 'silence', 'open', 'partial', 'first', 'last', 'requests')} | {
        'archives': [r[1] for r in L['arch_rows']],
        'picked': L['cat_rows'][0][0], 'oldest': L['oldest'][3], 'oldest_read': L['oldest_read'][3],
        'featured': FT['slug'] if FT else None}


def lists():
    """The top rows and the sizes of the two lists a contributor picks from: the Unsolved Catalogue and Read Further."""
    out = {}
    for key, page, pat, cell in (('cat', 'catalogue.html', r'<title>The Unsolved Catalogue — ([\d,]+) ciphers', 2),
                                 ('fur', 'further.html', r'<title>Read Further — ([\d,]+) readings', 2)):
        s = (DOCS / page).read_text(encoding='utf8')
        m = re.search(pat, s)
        if not m:
            sys.exit(f'docs/{page}: pattern not found: {pat}')
        out['open' if key == 'cat' else 'partial'] = floor(m.group(1))
        rows = []
        for attrs, body in re.findall(r'<tr class="e"([^>]*)>(.*?)</tr>', s, re.S)[:4]:
            cells = [re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', c))).strip()
                     for c in re.findall(r'<td[^>]*>(.*?)</td>', body, re.S)]
            rows.append((re.search(r'data-href="([^"]+)"', attrs).group(1), cells[0], caps(cells[cell].lstrip('●◇○◆ '))))
        if len(rows) < 4:
            sys.exit(f'docs/{page}: fewer than four rows')
        out[key + '_rows'] = rows
    out.update(archives())
    return out


ARCH_SHORT = {'Bibliothèque nationale de France': 'BNF', 'Arxiu Capitular de Barcelona': 'CATHEDRAL ARCHIVE',
              'Real Academia de la Historia': 'REAL ACADEMIA', 'Archivio Apostolico Vaticano': 'VATICAN ARCHIVES',
              'The National Archives': 'NATIONAL ARCHIVES', 'British Library': 'BRITISH LIBRARY',
              'U.S. National Archives (NARA)': 'NARA', 'Hungarian National Archives (MNL OL)': 'MNL OL',
              'Nationaal Archief': 'NATIONAAL ARCHIEF', 'Riksarkivet': 'RIKSARKIVET'}


def archives():
    """The open archive requests (archive_requests.json, the page docs/archives.html): their count, and the four
    archives with the most, as (city, short name, count)."""
    reqs = json.loads((DOCS.parent / 'archive_requests.json').read_text(encoding='utf8'))['requests']
    live = [r for r in reqs if r['status'] in ('open', 'claimed', 'requested')]
    n = {}
    for r in live:
        if r.get('city'):
            n[(r['city'], r['archive'])] = n.get((r['city'], r['archive']), 0) + 1
    top = sorted(n.items(), key=lambda kv: (-kv[1], kv[0]))[:4]
    return dict(requests=floor(str(len(live))), archives=len({a for _, a in n}),
                arch_rows=[(caps(c.split(',')[0]), caps(ARCH_SHORT.get(a, a)), k) for (c, a), k in top])


def caps(s):
    """A title in the pixel font's capitals: accents dropped, unknown characters made spaces."""
    s = unicodedata.normalize('NFKD', s.replace('’', "'").replace('‘', "'").replace('—', '-'))
    s = ''.join(ch for ch in s if not unicodedata.combining(ch)).upper()
    return re.sub(r'\s+', ' ', ''.join(ch if ch == ' ' or ch in FONT else ' ' for ch in s)).strip()


def fit(s, width):
    """s cut to fit width pixels, with '..' where it was cut."""
    if tw(s) <= width:
        return s
    while s and tw(s + '..') > width:
        s = s[:-1]
    return s.rstrip(' ,;:-') + '..'


LG = None


def floor(s):
    v = int(s.replace(',', ''))
    return v // 1000 * 1000 if v >= 1000 else v // 10 * 10


def plus(v):
    return f'{v:,}+'

# ---------------------------------------------------------------- the week's cipher

FT = None      # the featured cipher being drawn: featured.json's entry, its tokens and its key, set by main()


def featured(slug=None, day=None):
    """featured.json's entry for slug, or the one for day's ISO week, with its tokens from docs/reveal/."""
    entries = json.loads((HERE / 'featured.json').read_text(encoding='utf8'))['entries']
    if slug:
        e = next((e for e in entries if e['slug'] == slug), None)
        if not e:
            sys.exit(f'featured.json has no entry {slug}')
    else:
        e = entries[(day or datetime.date.today()).isocalendar()[1] % len(entries)]
    rev = json.loads((DOCS / 'reveal' / f"{e['slug']}.json").read_text(encoding='utf8'))
    toks = []
    for r, (a, b) in enumerate(e['runs']):
        for i in range(a, b + 1):
            tk = rev['tokens'][i]
            if not tk['g'] or tk.get('cls') == 'plain':
                continue
            p = caps(tk['p'])
            if not p or '?' in tk['p']:
                sys.exit(f"{e['slug']}: token {i} has no reading; pick runs that read in full")
            toks.append(dict(g=tk['g'], p=p, w=bool(tk.get('w')) or not toks or toks[-1]['run'] != r, run=r))
    key = {}
    for tk in toks:
        key.setdefault(tk['g'], tk['p'])
    href = f"{e['slug']}.html" + (f"#{rev['anchor']}" if rev.get('anchor') else '')
    return dict(e, tokens=toks, key=key, href=href)


# ---------------------------------------------------------------- the archive (scenes 1 and 7)

WA = 560
TH_A = tile_th(H, WA)
CANDLE = (518, 114)          # candle sprite, archive coordinates
BEAM = [(30, 92), (78, 92), (206, 178), (124, 178)]
_arch = None


def window(d, x, y, w, h, rng, moon=True):
    stone, stone2 = C['night5'], C['night4']
    r = w // 2
    d.ellipse([x - 3, y - 3, x + w + 2, y + w + 2], fill=stone2)
    d.rectangle([x - 3, y + r, x + w + 2, y + h + 2], fill=stone2)
    d.ellipse([x - 2, y - 2, x + w + 1, y + w + 1], fill=stone)
    d.rectangle([x - 2, y + r, x + w + 1, y + h + 1], fill=stone)
    d.ellipse([x, y, x + w - 1, y + w - 1], fill=C['night4'])
    d.rectangle([x, y + r, x + w - 1, y + h - 1], fill=C['night4'])
    for _ in range(w * h // 60):
        sx, sy = rng.randrange(x + 2, x + w - 2), rng.randrange(y + 3, y + h - 2)
        d.point((sx, sy), fill=C['ink2'] if rng.random() < .4 else C['night5'])
    if moon:
        mx, my, mr = x + w * 3 // 4 - 2, y + 9, max(3, w // 8)
        d.ellipse([mx - mr, my - mr, mx + mr, my + mr], fill=hx('efe6cc'))
        d.ellipse([mx - mr + 2, my - mr, mx + mr + 2, my + mr], fill=C['night4'])
    d.rectangle([x + r - 1, y, x + r, y + h - 1], fill=C['wood'])
    d.rectangle([x, y + h // 2, x + w - 1, y + h // 2 + 1], fill=C['wood'])
    d.rectangle([x - 6, y + h, x + w + 5, y + h + 3], fill=stone)
    d.line([x - 6, y + h + 3, x + w + 5, y + h + 3], fill=stone2)


def bundle(d, x, base, rng):
    w, n = rng.randint(17, 27), rng.randint(4, 8)
    for i in range(n):
        xo = rng.randint(-1, 1)
        c = (C['parch'], C['parch2'], C['parch3'])[rng.randrange(3)]
        d.rectangle([x + xo, base - 2 * i - 2, x + xo + w - 1, base - 2 * i - 1], fill=c)
        d.point((x + xo, base - 2 * i - 1), fill=C['parchdk'])
        d.line([x + xo + 1, base - 2 * i - 1, x + xo + w - 1, base - 2 * i - 1], fill=mix(c, C['parchdk'], .45))
    rc = C['red'] if rng.random() < .55 else C['wood4']
    d.line([x + w // 2, base - 2 * n - 1, x + w // 2, base - 1], fill=rc)
    d.rectangle([x + w // 2 - 1, base - 2 * n - 2, x + w // 2 + 1, base - 2 * n - 1], fill=rc)
    return w + 2


def archbox(d, x, base, rng):
    w, h = rng.randint(14, 20), rng.randint(18, 25)
    c = (hx('4b4a2e'), C['wood3'], hx('5a2a22'), hx('2f3a52'), hx('4a3a2a'))[rng.randrange(5)]
    d.rectangle([x, base - h, x + w - 1, base - 1], fill=c, outline=C['wood'])
    d.line([x + 1, base - h + 1, x + 1, base - 2], fill=mix(c, C['ink'], .15))
    d.rectangle([x + 3, base - h + 4, x + w - 4, base - h + 9], fill=C['parch2'])
    d.line([x + 4, base - h + 6, x + w - 6, base - h + 6], fill=C['parchdk'])
    return w + 1


def books(d, x, base, rng):
    cx = x
    for _ in range(rng.randint(3, 6)):
        w, h = rng.randint(3, 4), rng.randint(16, 25)
        c = (C['reddk'], hx('2f4a3a'), hx('3a3f6b'), C['wood3'], hx('5c3b52'), hx('4a3d1a'))[rng.randrange(6)]
        d.rectangle([cx, base - h, cx + w - 1, base - 1], fill=c)
        d.line([cx, base - h, cx, base - 1], fill=mix(c, C['ink'], .2))
        for by in (base - h + 3, base - 5):
            d.line([cx, by, cx + w - 1, by], fill=C['golddk'])
        cx += w
    return cx - x + 2


def scrolls(d, x, base, rng):
    rows = rng.randint(2, 3)
    for r in range(rows):
        for i in range(rows - r):
            cx, cy = x + 3 + i * 7 + r * 3, base - 4 - r * 6
            d.ellipse([cx - 3, cy - 3, cx + 3, cy + 3], fill=C['parch2'], outline=C['parchdk'])
            d.point((cx, cy), fill=C['parchdk'])
    return rows * 7 + 2


def archive_bg():
    global _arch
    if _arch is not None:
        return _arch
    rng = random.Random(1533)
    a = np.full((H, WA, 3), C['night'], np.uint8)
    yy = np.broadcast_to(np.arange(H)[:, None] / H, (H, WA))
    a[TH_A < yy * .9] = C['night2']
    im = Image.fromarray(a)
    d = ImageDraw.Draw(im)
    mortar = hx('0a0d13')
    for row, y in enumerate(range(3, 160, 9)):
        d.line([0, y, WA, y], fill=mortar)
        for x in range(9 * (row % 2), WA, 18):
            d.line([x, y + 1, x, y + 8], fill=mortar)
    window(d, 30, 14, 48, 78, rng)
    # shelves
    posts = [104, 250, 396, 542]
    d.rectangle([posts[0], 4, posts[-1] + 5, 160], fill=hx('140e09'))
    for x in range(posts[0], posts[-1], 2):
        if (x // 2) % 5 == 0:
            d.line([x, 4, x, 160], fill=hx('1a120c'))
    planks = [36, 70, 104, 138]
    for i in range(3):
        for base in planks:
            x, end = posts[i] + 8, posts[i + 1] - 2
            while x < end - 14:
                kind = rng.random()
                if kind < .36:
                    w = bundle(d, x, base, rng)
                elif kind < .56:
                    w = archbox(d, x, base, rng)
                elif kind < .78:
                    w = books(d, x, base, rng)
                elif kind < .9:
                    w = scrolls(d, x, base, rng)
                else:
                    w = rng.randint(5, 12)
                x += w
            d.rectangle([posts[i], base, posts[i + 1], base + 3], fill=C['wood3'])
            d.line([posts[i], base, posts[i + 1], base], fill=C['wood4'])
            d.line([posts[i], base + 4, posts[i + 1], base + 4], fill=C['wood'])
    for x in posts:
        d.rectangle([x, 2, x + 5, 160], fill=C['wood2'])
        d.line([x, 2, x, 160], fill=C['wood4'])
        d.line([x + 5, 2, x + 5, 160], fill=C['wood'])
    d.rectangle([posts[0] - 2, 0, posts[-1] + 7, 4], fill=C['wood3'])
    d.line([posts[0] - 2, 4, posts[-1] + 7, 4], fill=C['wood'])
    # floor
    d.rectangle([0, 160, WA, H], fill=C['wood'])
    for y in range(162, H, 5):
        d.line([0, y, WA, y], fill=hx('170f09'))
        for x in range(rng.randrange(30), WA, rng.randint(40, 70)):
            d.line([x, y + 1, x, y + 4], fill=hx('170f09'))
    d.line([0, 160, WA, 160], fill=C['wood2'])
    # ladder against the second bay
    for k in range(2):
        d.line([318 + 12 * k, 176, 342 + 12 * k, 10], fill=C['wood4'])
        d.line([319 + 12 * k, 176, 343 + 12 * k, 10], fill=C['wood2'])
    for y in range(20, 172, 11):
        f = (176 - y) / 166
        x0 = 318 + 24 * f
        d.line([x0 + 1, y, x0 + 12, y], fill=C['wood3'])
    # the desk
    d.rectangle([426, 126, 556, 129], fill=C['wood4'])
    d.rectangle([426, 130, 556, 158], fill=C['wood2'])
    d.line([426, 130, 556, 130], fill=C['wood'])
    for dx in (432, 492):
        d.rectangle([dx, 135, dx + 54, 152], outline=C['wood'])
        d.rectangle([dx + 25, 142, dx + 28, 144], fill=C['golddk'])
    d.rectangle([428, 158, 433, 172], fill=C['wood2'])
    d.rectangle([549, 158, 554, 172], fill=C['wood2'])
    bundle(d, 432, 126, rng)
    bundle(d, 436, 116, rng)
    # an upright letter on a reading slope, in cipher
    d.polygon([(462, 126), (502, 126), (498, 94), (466, 94)], fill=C['parch'], outline=C['parchdk'])
    for i, y in enumerate(range(99, 121, 4)):
        x = 469 - (y - 94) // 8
        while x < 494 + (y - 94) // 8 - 3:
            w = rng.randint(2, 5)
            d.line([x, y, x + w - 1, y], fill=C['sepia'])
            if rng.random() < .3:
                d.point((x + 1, y - 1), fill=C['sepia'])
            x += w + rng.randint(1, 2)
    d.ellipse([491, 116, 497, 122], fill=C['red'], outline=C['reddk'])
    d.rectangle([462, 126, 502, 127], fill=C['wood3'])
    # inkwell and quill
    d.rectangle([505, 119, 511, 125], fill=hx('1b1a24'), outline=C['void'])
    d.line([506, 120, 506, 123], fill=C['night5'])
    _arch = np.asarray(im).copy()
    q = Image.fromarray(_arch)
    qi = sprite(SPRITES['quill'])
    q.paste(qi, (503, 104), qi)
    ci = sprite(SPRITES['candle'])
    q.paste(ci, CANDLE, ci)
    _arch = np.asarray(q).copy()
    # moonlight
    m = Image.new('L', (WA, H), 0)
    ImageDraw.Draw(m).polygon(BEAM, fill=255)
    beam = np.asarray(m) > 0
    lit = beam & (TH_A < .3)
    _arch[lit] = np.clip(_arch[lit].astype(int) + np.array([22, 30, 48]), 0, 255)
    return _arch


_motes = [(random.Random(i).random(), random.Random(i * 7 + 1).random(), random.Random(i * 13 + 5).random())
          for i in range(34)]


def archive_frame(t, cam):
    a = archive_bg()[:, cam:cam + W].copy()
    cv = Cv(a)
    # dust in the moonbeam
    for u, v, ph in _motes:
        y = 92 + ((v * 86 - t * 4) % 86)
        f = (y - 92) / 86
        x0, x1 = 30 + 94 * f, 78 + 128 * f
        x = x0 + (x1 - x0) * ((u + .04 * math.sin(t * .9 + ph * 6)) % 1)
        c = C['ink2'] if ph < .3 else hx('8fa0c8')
        cv.px(round(x) - cam, round(y), c)
    # stars twinkle
    if 30 - cam > -60:
        for i in range(6):
            r = random.Random(i + 99)
            if math.sin(t * (2 + r.random() * 3) + i) > .6:
                cv.px(33 + r.randrange(40) - cam, 18 + r.randrange(28), C['white'])
    cx, cy = CANDLE
    flame(cv, cx + 1 - cam, cy - 6, t)
    a = cv.a()
    light(a, cx + 3 - cam, cy - 3, 120, C['orange'], .62 * flicker(t))
    dither(a, VIG, C['void'])
    return a


def caption_band(a, y0, level=.62):
    m = np.zeros_like(TH, bool)
    m[y0:] = TH[y0:] < level
    a[m] = C['void']


def night_bg():
    a = np.full((H, W, 3), C['void'], np.uint8)
    dither(a, (_yy / H) * .9, C['night'])
    dither(a, np.clip((_yy / H) - .55, 0, 1) * 1.6, C['night2'])
    return a


# ---------------------------------------------------------------- method

def silhouette(x, y):
    m = Image.new('L', (W, H), 0)
    d = ImageDraw.Draw(m)
    d.ellipse([x + 9, y + 3, x + 27, y + 23], fill=255)
    for cx, cy, r in ((x + 12, y + 5, 4), (x + 17, y + 2, 5), (x + 23, y + 4, 4), (x + 26, y + 8, 3), (x + 9, y + 9, 3)):
        d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=255)
    d.ellipse([x + 7, y + 11, x + 11, y + 17], fill=255)
    d.ellipse([x + 25, y + 11, x + 29, y + 17], fill=255)
    d.rectangle([x + 13, y + 21, x + 23, y + 29], fill=255)
    d.polygon([(x + 2, y + 31), (x + 34, y + 31), (x + 40, y + 41), (x + 41, H), (x - 5, H), (x - 4, y + 41)], fill=255)
    d.ellipse([x - 5, y + 28, x + 12, y + 47], fill=255)
    d.ellipse([x + 24, y + 28, x + 41, y + 47], fill=255)
    return np.asarray(m) > 0


SIL = silhouette(96, 92)
_rim = SIL & ~np.roll(SIL, -1, axis=1) | SIL & ~np.roll(SIL, 1, axis=0)
RIM = _rim & (_xx > 112)
RIM2 = SIL & ~np.roll(SIL, 1, axis=0) & (_xx <= 112)


def desk_scene(t):
    a = night_bg()
    cv = Cv(a)
    rng = random.Random(3)
    window(cv.d, 18, 14, 30, 48, rng)
    for y in (40, 70, 100):
        cv.rect(236, y, 84, 2, hx('16120d'))
    for x in range(240, 320, 5):
        r = random.Random(x)
        for y in (40, 70, 100):
            h = r.randint(12, 24)
            cv.rect(x, y - h, 4, h, mix(C['night2'], hx('2a1f16'), r.random()))
    # desk
    cv.rect(0, 134, W, 3, C['wood4'])
    cv.rect(0, 137, W, H - 137, C['wood2'])
    cv.line(0, 137, W, 137, C['wood'])
    # laptop
    cv.d.polygon([(116, 134), (216, 134), (209, 127), (123, 127)], fill=hx('8a93ab'), outline=hx('3c4256'))
    for ky in (129, 131):
        for kx in range(126, 206, 4):
            cv.rect(kx + (ky - 129) // 2, ky, 3, 1, hx('4b5266'))
    cv.rect(126, 74, 80, 54, hx('2a2d36'))
    cv.rect(127, 75, 78, 52, hx('3c4256'))
    sx0, sy0, sx1, sy1 = 130, 78, 202, 124
    cv.rect(sx0, sy0, sx1 - sx0, sy1 - sy0, hx('0b1714'))
    off = t * 9
    first = int(off // 5)
    for li in range(first, first + 11):
        y = sy0 + 2 + li * 5 - int(off)
        if y < sy0 + 1 or y > sy1 - 4:
            continue
        r = random.Random(li)
        x = sx0 + 3
        cv.rect(x, y, 2, 2, C['gold'])
        x += 4
        while x < sx1 - 6 and r.random() > .12:
            w = r.randint(2, 12)
            w = min(w, sx1 - 3 - x)
            c = (C['green'], C['green'], C['ink2'], C['gold'], C['blue'])[r.randrange(5)]
            cv.rect(x, y, w, 2, mix(c, hx('0b1714'), .25))
            x += w + 2
    if int(t * 3) % 2 == 0:
        cv.rect(sx0 + 3, sy1 - 7, 4, 4, C['green'])
    # papers and the candle
    cv.d.polygon([(212, 134), (238, 134), (234, 104), (214, 106)], fill=C['parch'], outline=C['parchdk'])
    r = random.Random(11)
    for y in range(110, 130, 4):
        x = 217
        while x < 231:
            w = r.randint(2, 4)
            cv.line(x, y, min(x + w - 1, 231), y, C['sepia'])
            x += w + 2
    bundle(cv.d, 262, 134, random.Random(5))
    bundle(cv.d, 266, 124, random.Random(8))
    blit(cv, 'candle', 246, 122)
    flame(cv, 247, 116, t, 1)
    a = cv.a()
    light(a, 166, 101, 110, hx('2f9070'), .55)
    light(a, 249, 119, 90, C['orange'], .5 * flicker(t, 1))
    a[SIL] = hx('06080b')
    a[RIM] = hx('4fae8c')
    a[RIM2] = hx('1d3a33')
    cv = Cv(a)
    cv.rect(89, 146, 52, 5, C['wood3'])
    cv.line(89, 146, 140, 146, C['wood4'])
    cv.line(89, 151, 140, 151, C['wood'])
    for px_ in (92, 134):
        cv.rect(px_, 151, 4, H - 151, C['wood2'])
        cv.line(px_ + 3, 151, px_ + 3, H, C['wood'])
    for px_ in (105, 114, 123):
        cv.rect(px_, 151, 2, H - 151, C['wood2'])
    return cv.a()


STEPS = [('1 FIND', ['ARCHIVES,', 'DECODE']),
         ('2 TRANSCRIBE', ['EVERY SIGN', 'ON THE PAGE']),
         ('3 THE KEY', ['REBUILT', 'OR FOUND']),
         ('4 WRITE UP', ['EVERY STEP', 'RECORDED'])]


def steps_scene(t):
    a = night_bg()
    cv = Cv(a)
    for y in range(40, 150, 12):
        for x in range(0, W, 4):
            cv.px(x, y, C['night2'])
    text(cv, 'FROM ARCHIVE TO TEXT', W // 2, 12, C['gold2'], 2, 'c', shadow=C['void'])
    pw, gap, y0, ph = 72, 6, 42, 100
    x0 = (W - (4 * pw + 3 * gap)) // 2
    for i, (title, sub) in enumerate(STEPS):
        ti = .2 + i * .95
        if t < ti:
            continue
        p = ease_out((t - ti) / .35)
        x, y = x0 + i * (pw + gap), y0 + round((1 - p) * 10)
        lay = Cv(cv.a())
        lay.rect(x, y, pw, ph, C['night2'])
        lay.box(x, y, pw, ph, C['night4'])
        lay.rect(x, y, pw, 2, C['gold'] if i == min(3, int((t - .2) / .95)) else C['golddk'])
        cx, iy = x + pw // 2, y + 12
        lt = t - ti
        if i == 0:
            lay.rect(cx - 14, iy + 18, 28, 14, C['wood3'])
            lay.box(cx - 14, iy + 18, 28, 14, C['wood'])
            lay.rect(cx - 6, iy + 22, 12, 4, C['parch2'])
            for k in range(3):
                lay.rect(cx - 12 + k * 9, iy + 14 - k % 2, 7, 4, C['parch'])
            blit(lay, 'glass', cx - 14 + round(5 * math.sin(lt * 3)), iy - 2 + round(3 * math.cos(lt * 3)), 2)
        elif i == 1:
            # the week's cipher, group by group: the figures on the page, and the letter each stands for
            singles = [tk for tk in FT['tokens'] if len(tk['p']) == 1] or FT['tokens']
            tk = singles[int(lt * 4) % len(singles)]
            lay.rect(cx - 32, iy, 26, 26, C['parch'])
            text(lay, tk['g'], cx - 19, iy + 10, C['sepia'], 1, 'c')
            text(lay, '→', cx, iy + 10, C['gold'], 1, 'c')
            text(lay, tk['p'][:1], cx + 18, iy + 6, C['green'], 2, 'c')
        elif i == 2:
            blit(lay, 'key', cx - 16, iy, 2)
            q = clamp(lt / 1.6)
            q = q if q >= 1 else q * (.85 + .15 * math.sin(lt * 20))
            lay.box(cx - 26, iy + 26, 52, 5, C['night4'])
            lay.rect(cx - 25, iy + 27, int(50 * q), 3, C['green'] if q >= 1 else C['gold'])
        else:
            blit(lay, 'scroll', cx - 16, iy - 2, 2)
            if lt > 1.0:
                blit(lay, 'check', cx + 8, iy + 14)
        text(lay, title, cx, y + 52, C['gold2'], 1, 'c')
        for k, s in enumerate(sub):
            text(lay, s, cx, y + 66 + 10 * k, C['ink2'], 1, 'c')
        if i:
            text(lay, '→', x - gap // 2, y + 46, C['gold'], 1, 'c')
        cv.set(dissolve(cv.a(), lay.a(), p * 1.05))
    a = cv.a()
    dither(a, VIG, C['void'])
    return a


METHOD_STEPS = 5.4     # seconds into the method scene when the four steps replace the desk


def scene_method(t):
    T1 = METHOD_STEPS
    if t < T1:
        a = desk_scene(t)
    else:
        a = steps_scene(t - T1)
        if t < T1 + .35:
            a = dissolve(desk_scene(t), a, (t - T1) / .35)
        return a
    cv = Cv(a)
    caption_band_top(cv, 52)
    text_lines(cv, ['AN AI, A HUMAN, A LAPTOP'], W // 2, 8, t, .25, C['gold2'], 2)
    text_lines(cv, ['HOW FAR CAN CLAUDE GET ON CIPHERS', 'THAT HAVE RESISTED PEOPLE FOR CENTURIES?'],
               W // 2, 30, t, .9, C['ink'], 1, lh=10, cps=60)
    a = cv.a()
    dither(a, VIG, C['void'])
    return a


def caption_band_top(cv, y1, level=.55):
    a = cv.a()
    m = np.zeros_like(TH, bool)
    m[:y1] = TH[:y1] < level
    a[m] = C['void']
    cv.set(a)


# ---------------------------------------------------------------- one line deciphered

_parch = None


def parchment():
    global _parch
    if _parch is None:
        rng = np.random.default_rng(5)
        a = np.full((H, W, 3), C['parch'], np.uint8)
        blot = np.zeros((H, W))
        for _ in range(40):
            cx, cy, r = rng.uniform(0, W), rng.uniform(0, H), rng.uniform(8, 40)
            blot += np.exp(-((_xx - cx) ** 2 + (_yy - cy) ** 2) / (2 * r * r)) * rng.uniform(.2, .6)
        dither(a, np.clip(blot * .35, 0, .6), C['parch2'])
        edge = np.clip(np.hypot((_xx - W / 2) / (W / 2), (_yy - H / 2) / (H / 2)) - .55, 0, 1)
        dither(a, edge * 1.6, C['parch3'])
        dither(a, (edge - .35) * 2.2, C['parchdk'])
        a[:, 158][TH[:, 158] < .5] = C['parch3']
        _parch = a
    return _parch.copy()


# when things happen in the decipher scene (seconds into it); audio.py times its sounds from these
DEC = dict(snip=3.0, key=3.4, scan=3.9, scan_end=7.7, band=8.0)
SNIP = (8, 26, 304, 128)          # where the manuscript is shown: x, y, w, h
_snip = {}


def snip_strip():
    """The write-up's photograph of the passage, cropped and scaled to cover SNIP, in the parchment's colours:
    its tones mapped onto five browns and Bayer-dithered, so the real page sits in the pixel world."""
    if FT['slug'] not in _snip:
        im = Image.open(DOCS / FT['image']).convert('L')
        if FT.get('crop'):
            im = im.crop(tuple(FT['crop']))
        _, _, w, h = SNIP
        k = max(w / im.width, h / im.height)
        im = im.resize((max(w, round(im.width * k)), max(h, round(im.height * k))), Image.LANCZOS)
        g = np.asarray(im, np.float32)
        lo, hi = np.percentile(g, 3), np.percentile(g, 97)
        g = np.clip((g - lo) / max(1, hi - lo), 0, 1) ** 1.25
        ramp = np.array([C['sepia'], C['parchdk'], C['parch3'], C['parch2'], C['parch']], np.uint8)
        th = tile_th(*g.shape)
        idx = np.clip(np.floor(g * (len(ramp) - 1) + th), 0, len(ramp) - 1).astype(int)
        _snip[FT['slug']] = ramp[idx]
    return _snip[FT['slug']]


def snip_frame(t):
    x0, y0, w, h = SNIP
    a = night_bg()
    s = snip_strip()
    p = ease(t / DEC['snip']) * FT.get('pan', 1)
    ox, oy = round((s.shape[1] - w) * p), round((s.shape[0] - h) * p)
    a[y0:y0 + h, x0:x0 + w] = s[oy:oy + h, ox:ox + w]
    cv = Cv(a)
    cv.box(x0 - 1, y0 - 1, w + 2, h + 2, C['parchdk'])
    text(cv, FT['shelf'], x0, 6, C['gold2'], shadow=C['void'])
    text(cv, FT['date'], x0 + w, 6, C['gold2'], 1, 'r', shadow=C['void'])
    text(cv, FT['credit'], x0, 15, C['muted'])
    return cv.a()


def token_layout(s=1):
    """Where each group of the passage goes at scale s: rows across the parchment, the reading above the figures."""
    out, x, row, maxw = [], 0, 0, 292
    for k, tk in enumerate(FT['tokens']):
        w = max(tw(tk['g'], s), tw(tk['p'], s))
        gap = (9 if tk['run'] != FT['tokens'][k - 1]['run'] else 6 if tk['w'] else 3) * s if k else 0
        if x + gap + w > maxw:
            row, x, gap = row + 1, 0, 0
        out.append((row, x + gap, w))
        x += gap + w
    rows = row + 1
    widths = [max(x + w for r, x, w in out if r == i) for i in range(rows)]
    return [((W - widths[r]) // 2 + x, r, w) for r, x, w in out], rows


def key_cells():
    """The key, as far as the passage uses it: one cell per figure group, in order of first use, in one ribbon."""
    cells, x = {}, 0
    for g, p in FT['key'].items():
        w = tw(g) + 3 + tw(p) + 6
        cells[g] = (x, w)
        x += w + 2
    return cells, x - 2


def scene_decipher(t):
    if t < DEC['snip']:
        return snip_frame(t)
    a = parchment()
    cv = Cv(a)
    toks = FT['tokens']
    n = len(toks)
    # the key, a ribbon across the top: it slides to keep the cell of the group being read in the middle, lit
    cells, kw = key_cells()
    ky = 16
    dt = (DEC['scan_end'] - DEC['scan']) / n
    cur = int((t - DEC['scan']) / dt) if t >= DEC['scan'] else -1
    if t >= DEC['key']:
        q = ease_out((t - DEC['key']) / .4)
        lay_ = Cv(cv.a())

        def centre(k):
            x, w = cells[toks[min(max(k, 0), n - 1)]['g']]
            return x + w / 2
        if kw <= 268:
            off = (W - kw) / 2
        else:                                   # glide from cell to cell as the scan moves
            f = clamp((t - DEC['scan']) / dt - .5, 0, n - 1)
            k0 = int(f)
            c = centre(k0) + (centre(k0 + 1) - centre(k0)) * ease(f - k0)
            off = clamp(W / 2 - c, W - 26 - kw, 26)
        lay_.rect(0, ky - 4, W, 15, C['parch3'])
        lay_.rect(0, ky - 3, W, 13, C['parch2'])
        for g, (x, w) in cells.items():
            bx = round(off + x)
            if bx > W or bx + w < 0:
                continue
            lit = 0 <= cur < n and toks[cur]['g'] == g
            used = any(tk['g'] == g for tk in toks[:max(0, cur)])
            lay_.rect(bx, ky - 1, w, 9, C['gold2'] if lit else C['parch'])
            ex = text(lay_, g, bx + 2, ky, C['sepia'])
            text(lay_, FT['key'][g], ex + 3, ky, C['clerk'] if used or lit else C['parch3'])
        lay_.rect(0, ky - 3, 24, 13, C['parch3'])
        text(lay_, 'KEY', 3, ky, C['sepia'])
        ribbon = lay_.a(), q
    # the passage: figures in the scribe's ink, the reading written above as the scan passes; twice the size
    # when it fits in two rows
    top, bottom = ky + 18, 122
    lay, rows = token_layout(2)
    s = 2 if rows <= 2 else 1
    if s == 1:
        lay, rows = token_layout(1)
    rh = 20 * s
    y0 = top + max(0, (bottom - top - rows * rh) // 2)
    for k, ((x, r, w), tk) in enumerate(zip(lay, toks)):
        gy = y0 + r * rh + 9 * s
        if k == cur:
            cv.rect(x - 2, gy - 10 * s - 2, w + 4, 17 * s + 4, C['gold2'])
        text(cv, tk['g'], x + w // 2, gy, C['sepia'], s, 'c')
        if 0 <= k < cur or (k == cur and t - DEC['scan'] - k * dt > dt * .4):
            text(cv, tk['p'], x + w // 2, gy - 9 * s, C['clerk'], s, 'c')
        if k and toks[k - 1]['run'] != tk['run'] and lay[k - 1][1] == r:
            text(cv, '..', x - 5 * s, gy, C['parch3'], s, 'c')
    a = cv.a()
    dither(a, VIG * .6, C['void'])
    if t >= DEC['key']:
        rib, q = ribbon
        band = slice(ky - 4, ky + 11)
        m = np.zeros_like(TH, bool)
        m[band] = TH[band] < q * 1.1
        a[m] = rib[m]
    if t < DEC['snip'] + .5:
        a = dissolve(snip_frame(t), a, (t - DEC['snip']) / .5)
    q = ease_out((t - DEC['band']) / .45)
    if q > 0:
        top = H - round(56 * q)
        a[top:] = C['night']
        a[top:top + 1, :] = C['gold']
        a[top + 1:top + 2, :] = C['golddk']
        cv = Cv(a)
        text_lines(cv, FT['en'], W // 2, top + 7, t, DEC['band'] + .3, C['gold2'], 1, lh=10, cps=52)
        if t > DEC['band'] + 1.9:
            text(cv, FT['who'], W // 2, top + 31, C['ink2'], 1, 'c')
            text(cv, FT['how'], W // 2, top + 42, C['green'], 1, 'c')
        a = cv.a()
    return a


# ---------------------------------------------------------------- the ledger

X0, X1, BASE = 20, 300, 134


def yx(year):
    return X0 + (year - 1390) * (X1 - X0) / 610


_stack = None


def stacks():
    global _stack
    if _stack is None:
        cols, out = {}, []
        for year, cat, lab, href in LG['dots']:
            col = int((yx(year) - X0) // 3)
            k = cols.get(col, 0)
            cols[col] = k + 1
            out.append((year, cat, X0 + col * 3, BASE - k * 3 - 1, href))
        _stack = out
    return _stack


LEGEND = [('KEY RECOVERED HERE', C['green']), ('EXISTING KEY', CAT['known']), ('OLD DECIPHERMENT', C['amber']),
          ('NOT SOLVED', C['red2'])]
SWEEP = .3, 3.6          # when the timeline's sweep starts, and how long it takes


def landed(x, t):
    td = SWEEP[0] + (x - X0) / (X1 - X0) * SWEEP[1]
    return td, t >= td


def silence_so_far(t):
    """The years-of-silence count as the sweep passes: the site's total, shared out over the texts obtained
    (each weighted by its years to 2026), so it ends on the number the page gives."""
    w = [(x, 2026 - year) for year, cat, x, _, _ in stacks() if cat not in ('notsolved', 'na', 'active')]
    tot = sum(v for _, v in w) or 1
    return LG['silence'] * sum(v for x, v in w if landed(x, t)[1]) / tot


def timeline_scene(t):
    cv = Cv(night_bg())
    for y in range(46, BASE, 12):
        for x in range(X0, X1, 3):
            cv.px(x, y, C['night2'])
    cv.line(X0 - 4, BASE + 3, X1 + 4, BASE + 3, C['muted'])
    for yr in range(1400, 2000, 100):
        x = round(yx(yr))
        cv.line(x, BASE + 3, x, BASE + 5, C['muted'])
        text(cv, str(yr), x, BASE + 8, C['muted'], 1, 'c')
    for year, cat, x, y, _ in stacks():
        td, on = landed(x, t)
        if not on:
            continue
        q = ease_out((t - td) / .2)
        yy = y - round((1 - q) * 10)
        cv.rect(x, yy, 2, 2, C['white'] if t - td < .05 else CAT[cat])
    p = (t - SWEEP[0]) / SWEEP[1]
    if 0 <= p <= 1.04:
        x = X0 + round(min(p, 1) * (X1 - X0))
        for y in range(40, BASE + 2, 2):
            cv.px(x, y, C['gold'])
        yr = round(1390 + min(p, 1) * 610)
        yr = max(LG['first'], min(LG['last'], yr))
        text(cv, str(yr), max(14, min(W - 14, x)), 26, C['gold2'], 1, 'c', shadow=C['void'])
    elif p > 1.04:
        s = f"{LG['first']}–{LG['last']}"
        text(cv, s, W // 2, 26, C['gold2'], 1, 'c', shadow=C['void'])
    for k, (s, c) in enumerate(LEGEND):
        if t > .8 + k * .15:
            cv.rect(22, 37 + k * 10, 5, 5, c)
            text(cv, s, 31, 36 + k * 10, C['ink2'], shadow=C['void'])
    # the years of silence, counting up as the texts land
    if t > SWEEP[0]:
        n = silence_so_far(t)
        text(cv, f'{round(n):,}' if p < 1.04 else plus(LG['silence']), 300, 38, C['gold'], 2, 'r', shadow=C['golddk2'])
        text(cv, 'YEARS OF SILENCE ENDED', 300, 56, C['muted'], 1, 'r', shadow=C['void'])
    return cv.a()


def zoom(a, z, fx, fy):
    """a magnified z times about (fx, fy), nearest-neighbour, kept inside the frame; returns it and the mapping."""
    w, h = W / z, H / z
    x0, y0 = clamp(fx - w / 2, 0, W - w), clamp(fy - h / 2, 0, H - h)
    xs = np.clip((x0 + np.arange(W) / z).astype(int), 0, W - 1)
    ys = np.clip((y0 + np.arange(H) / z).astype(int), 0, H - 1)
    return a[ys][:, xs], (lambda x, y: (round((x - x0) * z), round((y - y0) * z)))


def callout(cv, px, py, lx, ly, lines, col):
    """A label at (lx, ly) with a stepped leader down or up to the dot at (px, py)."""
    wd = max(tw(s) for s in lines) + 8
    hgt = 10 * len(lines) + 4
    cv.rect(lx - 1, ly - 1, wd + 2, hgt + 2, col)
    cv.rect(lx, ly, wd, hgt, C['void'])
    for k, s in enumerate(lines):
        text(cv, s, lx + 4, ly + 3 + 10 * k, col if k == 0 else C['ink2'])
    ey = ly + hgt + 1 if py > ly else ly - 2
    cv.line(lx + 6, ey, lx + 6, (ey + py) // 2, col)
    cv.line(lx + 6, (ey + py) // 2, px, (ey + py) // 2, col)
    cv.line(px, (ey + py) // 2, px, py + (-3 if py > ly else 3), col)
    cv.box(px - 2, py - 2, 6, 6, col)


def closeup_scene(t, t_tl):
    """The left end of the timeline, magnified: the oldest entry and the oldest text recovered, each named."""
    a = timeline_scene(t_tl)
    z = 1 + 2 * ease(t / .6)
    old, rd = LG['oldest'], LG['oldest_read']
    pos = {href: (x, y) for _, _, x, y, href in stacks()}
    fx, fy = pos[old[3]]
    a, m = zoom(a, z, fx + 30, fy - 20)
    # everything else dims, so the two entries named stand out
    d = clamp((t - .5) / .4)
    if d > 0:
        keep = np.zeros(a.shape[:2], bool)
        for e in (old, rd):
            x, y = m(*pos[e[3]])
            keep[max(0, y):y + round(2 * z), max(0, x):x + round(2 * z)] = True
        dim = (a * (1 - .62 * d)).astype(np.uint8)
        a = np.where(keep[..., None], a, dim)
    cv = Cv(a)
    items = [(rd, CAT[rd[1]], 'THE OLDEST TEXT RECOVERED')]
    if old is not rd:
        failed = old[1] == 'notsolved'
        items.append((old, C['red2'] if failed else CAT[old[1]],
                      'NOT SOLVED: THE WRITE-UP SAYS WHY' if failed else 'THE OLDEST ENTRY'))
    for i, (d, col, tag) in enumerate(items):
        if t < .7 + i * .9:
            continue
        px, py = m(*pos[d[3]])
        lx, head = 104, f'{d[0]} · '
        callout(cv, px + 3, py + 1, lx, 30 + 40 * i, [head + fit(d[2], W - 12 - lx - 8 - tw(head)), tag], col)
    return cv.a()


def stats_scene(t, paper=True):
    cv = Cv(night_bg())
    cols = [(LG['entries'], ['ENTRIES', f"{LG['first']}–{LG['last']}"]),
            (LG['keys'], ['KEYS RECOVERED', 'BY CRYPTANALYSIS']),
            (LG['silence'], ['YEARS OF SILENCE', 'ENDED'])]
    for i, (n, lab) in enumerate(cols):
        cx = (50, 140, 248)[i]
        ti = .15 + i * .25
        if t < ti:
            continue
        q = ease_out((t - ti) / 1.1)
        text(cv, plus(n) if q >= 1 else f'{round(n * q):,}', cx, 46, C['gold'], 3, 'c', shadow=C['golddk2'])
        text(cv, lab[0], cx, 76, C['ink'], 1, 'c')
        text(cv, lab[1], cx, 86, C['muted'], 1, 'c')
    if t > 1.6:
        p = ease((t - 1.6) / .4)
        for x in range(160 - int(120 * p), 160 + int(120 * p), 2):
            cv.px(x, 106, C['golddk'])
    if paper:
        text_lines(cv, ['EVERY ATTEMPT IS RECORDED, FAILURES TOO:', 'THE DATA FOR A PAPER WITH GEORGE LASRY'],
                   W // 2, 116, t, 1.9, C['ink'], 1, lh=11, cps=46)
        text_lines(cv, ['ON HOW AI PERFORMS AGAINST HISTORICAL CIPHERS'], W // 2, 138, t, 3.65, C['gold2'], 1, cps=46)
    else:
        text_lines(cv, ['EVERY ATTEMPT IS RECORDED, FAILURES TOO'], W // 2, 118, t, .9, C['ink'], 1, cps=50)
    return cv.a()


def ledger_scene(t_close, t_stats, paper):
    """The ledger in three parts: the timeline fills, the close-up from t_close, the counts from t_stats."""
    def scene(t):
        if t < t_close:
            a = timeline_scene(t)
        elif t < t_stats:
            a = closeup_scene(t - t_close, t_close)
        else:
            a = stats_scene(t - t_stats, paper)
            if t < t_stats + .35:
                a = dissolve(closeup_scene(t - t_close, t_close), a, (t - t_stats) / .35)
        cv = Cv(a)
        text(cv, 'THE LEDGER SO FAR', W // 2, 8, C['gold2'], 2, 'c', shadow=C['void'])
        a = cv.a()
        dither(a, VIG, C['void'])
        return a
    scene.t_close, scene.t_stats = t_close, t_stats      # audio.py times its sounds from these
    return scene


# ---------------------------------------------------------------- contributing

# when things happen in the contribute scene (seconds into each part); audio.py times its clicks from these
PICK = dict(click=2.2, page=2.6, copy=4.3)
AGENT = dict(paste=.25, first=1.0, step=.55)
AGENT_LINES = ['READING THE TASK PAGE', 'OPENING THE IMAGES', 'TRANSCRIBING THE CIPHER', 'TESTING KEYS',
               'WRITING THE REPORT']
URL = 'DBOURDEAU.GITHUB.IO/CYPHERSOLVER/'


def browser(cv, x, y, w, h, bar='', dark=False):
    """A pixel browser or terminal window: shadow, frame, three dots and an address bar (or a title)."""
    cv.rect(x + 3, y + 3, w, h, C['void'])
    cv.rect(x, y, w, h, hx('080b10') if dark else C['night2'])
    cv.box(x, y, w, h, C['night4'])
    cv.rect(x + 1, y + 1, w - 2, 11, C['night3'])
    for k, c in enumerate((C['red2'], C['amber'], C['green'])):
        cv.rect(x + 5 + k * 5, y + 5, 3, 3, c)
    if dark:
        text(cv, bar, x + w // 2, y + 3, C['muted'], 1, 'c')
    elif bar:
        cv.rect(x + 22, y + 2, w - 26, 9, C['night'])
        room = w - 32
        while tw(bar) > room:                     # keep the end of an address: the page is what matters
            bar = '..' + bar.lstrip('.')[1:]
        text(cv, bar, x + 26, y + 3, C['ink2'])


def pointer(cv, x, y, pressed=False):
    blit(cv, 'pointer', x + pressed, y + pressed)


def glide(t, t0, t1, a, b):
    p = ease((t - t0) / (t1 - t0))
    return round(a[0] + (b[0] - a[0]) * p), round(a[1] + (b[1] - a[1]) * p)


def pick_scene(t):
    """The catalogue and the Read Further list side by side; a row is picked, its page opens, its prompt is copied."""
    cv = Cv(night_bg())
    text(cv, 'HELPING IS SIMPLE', W // 2, 8, C['gold2'], 2, 'c', shadow=C['void'])
    href, _, name = LG['cat_rows'][0]
    num = re.search(r'(\d+)', href).group(1)
    row0 = (100, 28 + 27 + 4)
    if t < PICK['page'] + .3:
        lay = Cv(cv.a())
        # one above the other, full width, two rows each, so the titles fit
        panels = [(28, 'THE CATALOGUE', f"{plus(LG['open'])} NOBODY HAS READ", 'CATALOGUE.HTML', LG['cat_rows'], C['gold']),
                  (92, 'READ FURTHER', f"{plus(LG['partial'])} LEFT PARTIAL", 'FURTHER.HTML', LG['fur_rows'], C['green'])]
        x, pw = 10, 300
        for i, (y0, title, sub, url, rows, sc) in enumerate(panels):
            ti = .2 + i * .35
            if t < ti:
                continue
            q = ease_out((t - ti) / .35)
            y = y0 + round((1 - q) * 8)
            browser(lay, x, y, pw, 58, url)
            sx = text(lay, title, x + 6, y + 15, C['gold2'])
            text(lay, sub, sx + 8, y + 15, C['muted'])
            for k, (_, score, label) in enumerate(rows[:2]):
                if t < ti + .3 + k * .12:
                    break
                ry = y + 27 + k * 15
                picked = i == 0 and k == 0 and t >= PICK['click']
                lay.rect(x + 3, ry - 3, pw - 6, 13, (C['goldhi'] if t < PICK['click'] + .08 else C['night4']) if picked else C['night'])
                sx = text(lay, score, x + 7, ry, sc) + 5
                text(lay, fit(label, x + pw - 8 - sx), sx, ry, C['ink'] if picked else C['ink2'])
        cv.set(lay.a())
    if t >= PICK['page']:
        lay = Cv(night_bg())
        text(lay, 'HELPING IS SIMPLE', W // 2, 8, C['gold2'], 2, 'c', shadow=C['void'])
        x, y, w, h = 20, 30, 280, 118
        browser(lay, x, y, w, h, URL + f'SOLVE/{num}.HTML')
        text(lay, fit(f'NO. {num}: {name}', w - 16), x + 8, y + 17, C['gold2'])
        text(lay, 'HAND THIS PAGE TO YOUR AI AGENT', x + 8, y + 30, C['ink'])
        lay.rect(x + 8, y + 42, w - 16, 68, C['night'])
        lay.box(x + 8, y + 42, w - 16, 68, C['golddk'])
        text(lay, fit(f'TASK: HELP READ UNSOLVED CATALOGUE NO. {num}', w - 70), x + 13, y + 47, C['ink2'])
        r = random.Random(int(num))
        for k in range(6):
            xx, yy = x + 13, y + 60 + k * 8
            end = x + w - 14 - (r.randint(20, 120) if k == 5 else r.randint(0, 30))
            while xx < end:
                ww = r.randint(4, 18)
                lay.rect(xx, yy, min(ww, end - xx), 2, C['night4'])
                xx += ww + 3
        copied = t >= PICK['copy']
        bx, by = x + w - 50, y + 45
        lay.rect(bx, by, 38, 11, C['green'] if copied else C['gold'])
        text(lay, 'COPIED' if copied else 'COPY', bx + 19, by + 2, C['void'], 1, 'c')
        cv.set(dissolve(cv.a(), lay.a(), (t - PICK['page']) / .3))
        bxy = (bx + 22, by + 6)
    # the cursor: up to the first row of the catalogue, click; then to the copy button, click
    if t >= 1.2:
        if t < PICK['page'] + .3:
            px, py = glide(t, 1.2, 2.0, (160, 176), row0)
        else:
            px, py = glide(t, 3.3, 4.1, row0, bxy)
        pressed = abs(t - PICK['click']) < .1 or abs(t - PICK['copy']) < .1
        pointer(cv, px, py, pressed)
    return cv.a()


def agent_scene(t):
    """The page's address pasted into Claude Code, which works through the task and reports back."""
    cv = Cv(night_bg())
    text(cv, 'PASTE INTO CLAUDE CODE', W // 2, 8, C['gold2'], 2, 'c', shadow=C['void'])
    num = re.search(r'(\d+)', LG['cat_rows'][0][0]).group(1)
    x, y, w, h = 24, 30, 272, 118
    browser(cv, x, y, w, h, 'CLAUDE CODE', dark=True)
    if t >= AGENT['paste']:
        lines = [URL, f'SOLVE/{num}.HTML']
        if t < AGENT['paste'] + .35:
            cv.rect(x + 15, y + 16, tw(lines[0]) + 4, 20, C['bluedk'])
        text(cv, '>', x + 8, y + 18, C['gold'])
        for k, s in enumerate(lines):
            text(cv, s, x + 17, y + 18 + 10 * k, C['ink'])
    for i, s in enumerate(AGENT_LINES):
        ti = AGENT['first'] + i * AGENT['step']
        if t < ti:
            break
        ly = y + 44 + i * 11
        done = t >= ti + AGENT['step']
        if done:
            cv.rect(x + 9, ly + 2, 3, 3, C['green'])
        else:
            for k in range(3):
                cv.px(x + 8 + 2 * k, ly + 3, C['gold'] if int(t * 12) % 3 == k else C['night4'])
        text(cv, s, x + 17, ly, C['ink2'] if done else C['ink'])
        if s == 'TESTING KEYS':
            q = clamp((t - ti) / AGENT['step'])
            bx = x + 17 + tw(s) + 8
            cv.box(bx, ly + 1, 70, 5, C['night4'])
            cv.rect(bx + 1, ly + 2, int(68 * q), 3, C['green'] if q >= 1 else C['gold'])
    tf = AGENT['first'] + len(AGENT_LINES) * AGENT['step']
    if t >= tf:
        ly = y + 44 + len(AGENT_LINES) * 11 + 2
        blit(cv, 'check', x + 6, ly - 1)
        text(cv, 'SENT BACK: AN ISSUE OR A PULL REQUEST', x + 24, ly, C['green'])
    return cv.a()


def credit_scene(t):
    cv = Cv(night_bg())
    text(cv, 'CREDITED BY NAME', W // 2, 8, C['gold2'], 2, 'c', shadow=C['void'])
    x, y, w, h = 50, 32, 220, 96
    cv.rect(x + 3, y + 3, w, h, C['void'])
    cv.rect(x, y, w, h, C['parch'])
    cv.box(x, y, w, h, C['parchdk'])
    text(cv, 'KEY FROM ADJACENT PLAINTEXT', x + 10, y + 9, C['greendk'])
    text(cv, 'A LETTER IN CIPHER, ' + FT['date'][-4:], x + 10, y + 21, C['sepia'], 1)
    blit(cv, 'seal', x + w - 19, y + 7)
    cv.line(x + 10, y + 32, x + w - 10, y + 32, C['parch3'])
    t0 = .5
    n = typed(t, t0, 26)
    s1, s2, s3 = 'CREDITS: ', 'YOUR NAME', ' · SOLUTION'
    cx = x + 10
    cx = text(cv, s1, cx, y + 38, C['parchdk'], 1, upto=n) + 4
    if n > len(s1):
        nx = text(cv, s2, cx, y + 38, C['red'], 1, upto=n - len(s1))
        if n >= len(s1) + len(s2):
            cv.line(cx, y + 46, nx - 2, y + 46, C['red'])
        cx = nx + 4
    if n > len(s1) + len(s2):
        text(cv, s3, cx, y + 38, C['parchdk'], 1, upto=n - len(s1) - len(s2))
    r = random.Random(4)
    for k in range(4):
        yy = y + 54 + k * 9
        lw = r.randint(150, 196) if k < 3 else 90
        xx = x + 10
        while xx < x + 10 + lw:
            ww = r.randint(4, 16)
            cv.rect(xx, yy, min(ww, x + 10 + lw - xx), 2, C['parch3'])
            xx += ww + 3
    if t > 1.75:
        q = ease_out((t - 1.75) / .3)
        im = sprite(SPRITES['star'], 2)
        cv.im.paste(im, (x + w - 30, y + h - 26 - round((1 - q) * 8)), im)
        for k in range(6):
            ang = k * math.pi / 3 + t * 4
            rr = 16 + 3 * math.sin(t * 6)
            if q > .5:
                cv.px(x + w - 18 + round(math.cos(ang) * rr), y + h - 16 + round(math.sin(ang) * rr), C['goldhi'])
    text_lines(cv, ['ON THE WRITE-UP AND THE CONTRIBUTORS PAGE'], W // 2, 134, t, 1.1, C['ink'], 1, cps=44)
    text_lines(cv, ['YOUR NAME, YOUR WAY: FULL, INITIALS OR A HANDLE'], W // 2, 145, t, 2.1, C['muted'], 1,
               cps=48, cursor=False)
    return cv.a()


CONTRIB_AGENT, CONTRIB_CREDIT = 5.2, 10.6     # seconds into the contribute scene


def scene_contribute(t):
    parts = [(0, pick_scene), (CONTRIB_AGENT, agent_scene), (CONTRIB_CREDIT, credit_scene)]
    i = max(k for k in range(len(parts)) if t >= parts[k][0])
    t0, fn = parts[i]
    a = fn(t - t0)
    if i and t - t0 < .35:
        pt0, pfn = parts[i - 1]
        a = dissolve(pfn(t - pt0), a, (t - t0) / .35)
    dither(a, VIG, C['void'])
    return a


# ---------------------------------------------------------------- the archive

ARCH = dict(click=2.5, foot=3.1)      # seconds into the archive scene


def scene_archive(t):
    """docs/archives.html: the archives with the most open requests; one is taken with "I can do this"."""
    cv = Cv(night_bg())
    text(cv, 'TO THE ARCHIVE', W // 2, 8, C['gold2'], 2, 'c', shadow=C['void'])
    x, y, w, h = 20, 28, 280, 120
    browser(cv, x, y, w, h, URL + 'ARCHIVES.HTML')
    sx = text(cv, f"{plus(LG['requests'])} REQUESTS", x + 8, y + 16, C['gold2'])
    text(cv, fit('THAT NEED THE ORIGINAL', x + w - 8 - sx - 8), sx + 8, y + 16, C['muted'])
    bw = tw('I CAN DO THIS') + 8
    for k, (city, name, n) in enumerate(LG['arch_rows']):
        ti = .3 + k * .22
        if t < ti:
            break
        q = ease_out((t - ti) / .3)
        ry = y + 28 + k * 17 + round((1 - q) * 6)
        cv.rect(x + 6, ry, w - 12, 14, C['night'])
        cx = text(cv, city, x + 11, ry + 4, C['gold2']) + 6
        text(cv, fit(f'{name} · {n}', x + w - 16 - bw - cx), cx, ry + 4, C['ink2'])
        bx = x + w - 10 - bw
        if k == 0 and t >= ARCH['click']:
            cv.rect(bx, ry + 2, bw, 10, C['goldhi'] if t < ARCH['click'] + .08 else C['green'])
            blit(cv, 'check', bx + 3, ry + 1)
            text(cv, 'TAKEN', bx + bw // 2 + 5, ry + 4, C['void'], 1, 'c')
        else:
            cv.box(bx, ry + 2, bw, 10, C['gold'] if k == 0 else C['golddk'])
            text(cv, 'I CAN DO THIS', bx + bw // 2, ry + 4, C['gold'] if k == 0 else C['golddk'], 1, 'c')
    text_lines(cv, ['VISIT, ORDER A SCAN, OR FIND THE BOOK'], W // 2, y + 99, t, ARCH['foot'], C['ink'], 1, cps=44)
    if t >= 1.3:
        target = (x + w - 10 - bw // 2, y + 28 + 7)
        px, py = glide(t, 1.3, 2.3, (160, 176), target)
        pointer(cv, px, py, abs(t - ARCH['click']) < .1)
    a = cv.a()
    dither(a, VIG, C['void'])
    return a


# ---------------------------------------------------------------- the close

def scene_cta(t):
    # the page puts its own buttons over the lower half from here, so the frame keeps it clear
    a = (archive_frame(t + 10, WA - W) * .36).astype(np.uint8)
    cv = Cv(a)
    text_lines(cv, ['PICK A CIPHER.'], W // 2, 26, t, .3, C['gold2'], 2)
    text_lines(cv, ['BREAK IT.'], W // 2, 46, t, 1.0, C['gold2'], 2)
    text_lines(cv, ['WRITE IT UP.'], W // 2, 66, t, 1.7, C['gold2'], 2)
    return cv.a()


# ---------------------------------------------------------------- the two cuts

# Scene changes fall on the score's bar lines (96 bpm, 2.5 s a bar; audio.py builds each cut's score from 'bars'),
# and each voiceover line has room. 'vo' is (line id in vo.json, when its speech starts, whether it is captioned):
# a line the frame already spells out is not captioned again. 'links' are the page's buttons over the video while
# a stretch plays (FEATURED is the week's cipher's write-up); 'end' are the buttons over the close and after it.
FEATURED = 'featured'
CUTS = dict(
    hero=dict(
        # the ledger is short here (its counts are on the page under the video); contributing gets the whole
        # walkthrough, because that is what the front page asks of a visitor
        dur=41.25, page='index.html', out='hero.mp4', poster='hero_poster.png', poster_at=6.4,
        scenes=[(0.0, scene_decipher, 'decipher'), (11.25, ledger_scene(4.4, 99, False), 'ledger'),
                (18.75, scene_contribute, 'contribute'), (32.5, scene_archive, 'archive'), (37.5, scene_cta, 'cta')],
        vo=[('a1', .6, True), ('a2', 3.1, True), ('b1', 11.6, True), ('f1', 19.1, True), ('f2', 24.2, True),
            ('f3', 29.55, True), ('h1', 32.85, True), ('g1', 37.85, False)],
        chapters=[(0, 'The letter'), (11.25, 'The ledger'), (18.75, 'How to contribute'), (32.5, 'To the archive')],
        links=[(0, 11.25, FEATURED, ''), (11.25, 18.75, '#scoreboard', 'See the ledger'),
               (18.75, 32.5, 'catalogue.html', 'Open the catalogue'), (32.5, 37.5, 'archives.html', 'See the requests')],
        end=[('catalogue.html', 'Pick a cipher'), ('#random', 'Random cipher'), ('contribute.html', 'How to contribute')],
        # (section, chord, length in bars): see audio.py
        bars=[('intro', 'AM', 1), ('intro', 'F', 1), ('decipher', 'DM', 1), ('decipher', 'E', 1), ('decipher', 'AM', .5),
              ('ledger', 'AM', 1), ('ledger', 'F', 1), ('ledger', 'G', 1),
              ('tune1', 'F', 1), ('tune2', 'G', 1), ('tune3', 'C', 1), ('tune4', 'AM', 1), ('tune5', 'F', 1),
              ('tune6', 'G', .5), ('drive', 'F', 1), ('drive', 'G', 1), ('close', 'C', 1.5)]),
    full=dict(
        dur=58.75, page='contribute.html', out='hero_full.mp4', poster='hero_full_poster.png', poster_at=6.4,
        scenes=[(0.0, scene_decipher, 'decipher'), (11.25, scene_method, 'method'),
                (21.25, ledger_scene(4.6, 8.6, True), 'ledger'), (36.25, scene_contribute, 'contribute'),
                (50.0, scene_archive, 'archive'), (55.0, scene_cta, 'cta')],
        vo=[('a1', .6, True), ('a2', 3.1, True), ('c1', 11.6, False), ('c2', 16.9, True), ('b1', 21.6, True),
            ('e2', 27.6, True), ('f1', 36.6, True), ('f2', 41.7, True), ('f3', 47.05, True), ('h1', 50.35, True), ('g1', 55.35, False)],
        chapters=[(0, 'The letter'), (11.25, 'How it works'), (21.25, 'The ledger'), (36.25, 'How to contribute'),
                  (50.0, 'To the archive')],
        links=[(0, 11.25, FEATURED, ''), (36.25, 50.0, 'catalogue.html', 'Open the catalogue'),
               (50.0, 55.0, 'archives.html', 'See the requests')],
        end=[('catalogue.html', 'Pick a cipher'), ('further.html', 'Read Further'), ('archives.html', 'To the archive')],
        bars=[('intro', 'AM', 1), ('intro', 'F', 1), ('decipher', 'DM', 1), ('decipher', 'E', 1), ('decipher', 'AM', .5),
              ('build', 'F', 1), ('build', 'G', 1), ('drive', 'AM', 1), ('drive', 'F', 1),
              ('ledger', 'AM', 1), ('ledger', 'F', 1), ('ledger', 'C', 1), ('ledger', 'G', 1), ('ledger', 'AM', 1),
              ('ledger', 'AM', 1),
              ('tune1', 'F', 1), ('tune2', 'G', 1), ('tune3', 'C', 1), ('tune4', 'AM', 1), ('tune5', 'F', 1),
              ('tune6', 'G', .5), ('drive', 'F', 1), ('drive', 'G', 1), ('close', 'C', 1.5)]),
)
CUT = CUTS['hero']
TRANS = .4


def scene_start(name, cut=None):
    return next(t for t, _, n in (cut or CUT)['scenes'] if n == name)


# ---------------------------------------------------------------- captions

_vo = None
TEMPO = 1.05           # audio.py plays every take this much faster


def vo_lines():
    """vo.json's lines by id, each with the length of its take as audio.py plays it."""
    global _vo
    if _vo is None:
        _vo = {}
        for ln in json.loads((HERE / 'vo.json').read_text(encoding='utf8'))['lines']:
            f = HERE / 'vo' / f"{ln['id']}_{ln['take']}.flac"
            d = float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0',
                                      str(f)], capture_output=True, text=True, check=True).stdout)
            _vo[ln['id']] = dict(ln, dur=d / TEMPO)
    return _vo


def wrap(s, width):
    rows, cur = [], ''
    for word in s.split():
        if cur and tw(cur + ' ' + word) > width:
            rows.append(cur)
            cur = word
        else:
            cur = (cur + ' ' + word).strip()
    return rows + [cur] if cur else rows


_cues = {}


def caption_cues(cut=None):
    """(start, end, rows) for every captioned line: two rows at most on screen, a longer line split in turns."""
    cut = cut or CUT
    if id(cut) not in _cues:
        out = []
        for lid, at, on in cut['vo']:
            if not on:
                continue
            ln = vo_lines()[lid]
            rows = wrap(caps(ln['text']), 296)
            chunks = [rows[i:i + 2] for i in range(0, len(rows), 2)]
            n = sum(len(' '.join(c)) for c in chunks)
            t = at
            for c in chunks:
                d = ln['dur'] * len(' '.join(c)) / n
                out.append((t, t + d + (.35 if c is chunks[-1] else 0), c))
                t += d
        _cues[id(cut)] = out
    return _cues[id(cut)]


def captions(a, t):
    cue = next((c for c in caption_cues() if c[0] <= t < c[1]), None)
    if not cue:
        return a
    cv = Cv(a)
    rows = cue[2]
    for i, s in enumerate(rows):
        y = H - 12 - (len(rows) - 1 - i) * 10
        w = tw(s)
        cv.rect((W - w) // 2 - 3, y - 2, w + 6, 11, C['void'])
        text(cv, s, W // 2, y, C['ink'], 1, 'c')
    return cv.a()


# ---------------------------------------------------------------- rendering

def render(t):
    sc = CUT['scenes']
    i = max(k for k in range(len(sc)) if t >= sc[k][0])
    t0, fn, _ = sc[i]
    a = fn(t - t0)
    if i and t - t0 < TRANS:
        pt0, pfn, _ = sc[i - 1]
        a = dissolve(pfn(t - pt0), a, (t - t0) / TRANS)
    if t < .6:
        dither(a, 1 - t / .6, C['void'])
    if t > DUR - .8:
        dither(a, (t - (DUR - .8)) / .7, C['void'])
    return captions(a, t)


def up(a, k=SCALE):
    return np.repeat(np.repeat(a, k, 0), k, 1)


def page_links(cut):
    """The page's buttons over the video, as the figure's data-links: [from, to, href, label]; to null = the end."""
    out = []
    for a, b, href, label in cut['links']:
        if href == FEATURED:
            href, label = FT['href'], FT['label']
        out.append([a, b, href, label])
    end = scene_start('cta', cut)
    return out + [[end, None, href, label] for href, label in cut['end']]


def update_page(cut):
    """Write the cut's chapters, links and a new ?v= into its page, so the page and the file always agree."""
    page = DOCS / cut['page']
    s = page.read_text(encoding='utf8')
    name = re.escape(cut['out'])
    if not re.search(name + r'\?v=\d+', s):
        sys.exit(f"{cut['page']}: no <source src=\"{cut['out']}?v=N\"> to update")
    s = re.sub(name + r'\?v=(\d+)', lambda m: f"{cut['out']}?v={int(m.group(1)) + 1}", s)
    ts = [t for t, _ in cut['chapters']] + [cut['dur']]
    btns = ''.join(f'<button type="button" data-t="{t:g}" style="--w:{ts[i + 1] - t:g}">{html.escape(lab)}</button>'
                   for i, (t, lab) in enumerate(cut['chapters']))
    s, n = re.subn(r'(<div class="hv-ch"[^>]*>).*?(</div>)', lambda m: m.group(1) + btns + m.group(2), s, count=1)
    links = html.escape(json.dumps(page_links(cut), ensure_ascii=False), quote=True)
    s = re.sub(r'(<figure class="herovid[^"]*"[^>]*?) data-links="[^"]*"', r'\1', s, count=1)
    s, k = re.subn(r'(<figure class="herovid[^"]*")', lambda m: f'{m.group(1)} data-links="{links}"', s, count=1)
    if not (n and k):
        sys.exit(f"{cut['page']}: no hero video figure with chapters")
    page.write_text(s, encoding='utf8')


def main():
    global LG, FT, CUT, DUR
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    ap.add_argument('--cut', choices=sorted(CUTS), default='hero')
    ap.add_argument('--featured', help='featured.json slug to decipher (default: the one for this ISO week)')
    ap.add_argument('--out', help="video file (default: the cut's, in docs/)")
    ap.add_argument('--poster', help="poster frame (default: the cut's, in docs/)")
    ap.add_argument('--poster-at', type=float)
    ap.add_argument('--sheet', help='write a contact sheet (one frame every --every seconds) and stop')
    ap.add_argument('--every', type=float, default=2.0)
    ap.add_argument('--still', nargs=2, metavar=('T', 'PNG'), help='write one frame at 2x and stop')
    ap.add_argument('--crf', type=int, default=23)
    ap.add_argument('--audio', help='soundtrack to mux in (audio.py with the same --cut writes it)')
    ap.add_argument('--no-page', action='store_true', help="leave the page's chapters, links and ?v= alone")
    args = ap.parse_args()
    CUT = CUTS[args.cut]
    DUR = CUT['dur']
    LG = {**ledger(), **lists()}
    FT = featured(args.featured)
    if args.still:
        Image.fromarray(up(render(float(args.still[0])), 2)).save(args.still[1])
        return
    if args.sheet:
        ts = [args.every / 2 + k * args.every for k in range(int(DUR / args.every))]
        cols = 5
        rows = math.ceil(len(ts) / cols)
        sheet = Image.new('RGB', (cols * (W + 4), rows * (H + 14)), (40, 40, 40))
        lab = ImageDraw.Draw(sheet)
        for k, t in enumerate(ts):
            x, y = (k % cols) * (W + 4), (k // cols) * (H + 14)
            sheet.paste(Image.fromarray(render(t)), (x, y + 12))
            lab.text((x + 2, y), f'{t:.1f}s', fill=(220, 220, 220))
        sheet.save(args.sheet)
        return
    out = args.out or str(DOCS / CUT['out'])
    poster = args.poster or str(DOCS / CUT['poster'])
    n = int(round(DUR * FPS))
    cmd = ['ffmpeg', '-y', '-loglevel', 'error', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W * SCALE}x{H * SCALE}',
           '-r', str(FPS), '-i', '-']
    cmd += ['-i', args.audio, '-map', '0:v', '-map', '1:a', '-c:a', 'aac', '-b:a', '128k'] if args.audio else ['-an']
    cmd += ['-c:v', 'libx264', '-preset', 'slow', '-tune', 'animation', '-crf', str(args.crf), '-pix_fmt', 'yuv420p',
            '-movflags', '+faststart', out]
    ff = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    for f in range(n):
        ff.stdin.write(up(render(f / FPS)).tobytes())
        if f % (FPS * 5) == 0:
            print(f'  {f / FPS:4.0f}s', flush=True)
    ff.stdin.close()
    if ff.wait():
        sys.exit('ffmpeg failed')
    at = args.poster_at if args.poster_at is not None else CUT['poster_at']
    Image.fromarray(up(render(at))).save(poster, optimize=True)
    default = Path(out).resolve() == (DOCS / CUT['out']).resolve()
    if default and args.cut == 'hero':
        (HERE / 'shown.json').write_text(json.dumps(shown(LG), indent=1) + '\n', encoding='utf8')
    if default and not args.no_page:
        update_page(CUT)
    print(f'wrote {out} and {poster}' + (f", and docs/{CUT['page']}" if default and not args.no_page else ''))


if __name__ == '__main__':
    main()
