"""Pixel font and sprites for the hero video. Everything is drawn by hand here, so there is nothing to license.

Glyphs are 7 rows tall; '#' is ink. Empty columns at either side are trimmed, so the font is proportional.
Sprites are rows of palette keys (see PAL in hero_video.py); '.' is transparent.
"""

FONT_SRC = {
'A': """
.###.
#...#
#...#
#####
#...#
#...#
#...#""",
'B': """
####.
#...#
#...#
####.
#...#
#...#
####.""",
'C': """
.###.
#...#
#....
#....
#....
#...#
.###.""",
'D': """
####.
#...#
#...#
#...#
#...#
#...#
####.""",
'E': """
#####
#....
#....
####.
#....
#....
#####""",
'F': """
#####
#....
#....
####.
#....
#....
#....""",
'G': """
.###.
#...#
#....
#.###
#...#
#...#
.####""",
'H': """
#...#
#...#
#...#
#####
#...#
#...#
#...#""",
'I': """
###
.#.
.#.
.#.
.#.
.#.
###""",
'J': """
..###
...#.
...#.
...#.
...#.
#..#.
.##..""",
'K': """
#...#
#..#.
#.#..
##...
#.#..
#..#.
#...#""",
'L': """
#....
#....
#....
#....
#....
#....
#####""",
'M': """
#...#
##.##
#.#.#
#.#.#
#...#
#...#
#...#""",
'N': """
#...#
#...#
##..#
#.#.#
#..##
#...#
#...#""",
'O': """
.###.
#...#
#...#
#...#
#...#
#...#
.###.""",
'P': """
####.
#...#
#...#
####.
#....
#....
#....""",
'Q': """
.###.
#...#
#...#
#...#
#.#.#
#..#.
.##.#""",
'R': """
####.
#...#
#...#
####.
#.#..
#..#.
#...#""",
'S': """
.####
#....
#....
.###.
....#
....#
####.""",
'T': """
#####
..#..
..#..
..#..
..#..
..#..
..#..""",
'U': """
#...#
#...#
#...#
#...#
#...#
#...#
.###.""",
'V': """
#...#
#...#
#...#
#...#
#...#
.#.#.
..#..""",
'W': """
#...#
#...#
#...#
#.#.#
#.#.#
#.#.#
.#.#.""",
'X': """
#...#
#...#
.#.#.
..#..
.#.#.
#...#
#...#""",
'Y': """
#...#
#...#
.#.#.
..#..
..#..
..#..
..#..""",
'Z': """
#####
....#
...#.
..#..
.#...
#....
#####""",
'Ö': """
.#.#.
.....
.###.
#...#
#...#
#...#
.###.""",
'0': """
.###.
#...#
#..##
#.#.#
##..#
#...#
.###.""",
'1': """
.#.
##.
.#.
.#.
.#.
.#.
###""",
'2': """
.###.
#...#
....#
...#.
..#..
.#...
#####""",
'3': """
#####
...#.
..#..
...#.
....#
#...#
.###.""",
'4': """
...#.
..##.
.#.#.
#..#.
#####
...#.
...#.""",
'5': """
#####
#....
####.
....#
....#
#...#
.###.""",
'6': """
..##.
.#...
#....
####.
#...#
#...#
.###.""",
'7': """
#####
....#
...#.
..#..
.#...
.#...
.#...""",
'8': """
.###.
#...#
#...#
.###.
#...#
#...#
.###.""",
'9': """
.###.
#...#
#...#
.####
....#
...#.
.##..""",
'.': """
.
.
.
.
.
.
#""",
',': """
..
..
..
..
..
.#
#.""",
':': """
.
.
#
.
.
.
#""",
';': """
..
..
.#
..
..
.#
#.""",
'!': """
#
#
#
#
#
.
#""",
'?': """
.###.
#...#
....#
...#.
..#..
.....
..#..""",
'-': """
...
...
...
###
...
...
...""",
'–': """
....
....
....
####
....
....
....""",
'+': """
.....
..#..
..#..
#####
..#..
..#..
.....""",
'=': """
....
....
####
....
####
....
....""",
'/': """
....#
....#
...#.
..#..
.#...
#....
#....""",
'(': """
..#
.#.
#..
#..
#..
.#.
..#""",
')': """
#..
.#.
..#
..#
..#
.#.
#..""",
'&': """
.##..
#..#.
#.#..
.#...
#.#.#
#..#.
.##.#""",
"'": """
#
#
.
.
.
.
.""",
'"': """
#.#
#.#
...
...
...
...
...""",
'#': """
.#.#.
.#.#.
#####
.#.#.
#####
.#.#.
.#.#.""",
'·': """
.
.
.
#
.
.
.""",
'→': """
.....
..#..
...#.
#####
...#.
..#..
.....""",
'←': """
.....
..#..
.#...
#####
.#...
..#..
.....""",
'%': """
##..#
##..#
...#.
..#..
.#...
#..##
#..##""",
'*': """
.....
#.#.#
.###.
#####
.###.
#.#.#
.....""",
'_': """
.....
.....
.....
.....
.....
.....
#####""",
'>': """
#...
.#..
..#.
...#
..#.
.#..
#...""",
'<': """
...#
..#.
.#..
#...
.#..
..#.
...#""",
'@': """
.###.
#...#
#.###
#.#.#
#.##.
#....
.###.""",
}

# Stand-in shapes for the signs of a cipher line, one per transcription token: the reading is real, the drawn
# shapes are invented (the transcription keeps only a placeholder per sign).
SIGN_SRC = [
"""
#...#
#...#
.###.
..#..
..#..
..#..
.###.""", """
.###.
#...#
..#..
.###.
..#..
..#..
..#..""", """
#####
.#.#.
.#.#.
.#.#.
.#.#.
.#.#.
.#.#.""", """
..#..
.#.#.
#...#
#...#
.#.#.
..#..
..#..""", """
.##..
#..#.
...#.
..#..
.#...
#....
.####""", """
#...#
.#.#.
..#..
.#.#.
#...#
.....
#####""", """
.###.
#.#.#
#.#.#
.###.
..#..
..#..
.###.""", """
#....
#.##.
##..#
#...#
#..#.
#.#..
##...""", """
..##.
.#..#
.#...
.###.
.#...
.#...
##...""", """
#####
#....
#....
###..
#....
#....
#....""", """
.#.#.
#.#.#
#.#.#
#...#
.#.#.
..#..
..#..""", """
#...#
##..#
#.#.#
#..##
#...#
#...#
#####""", """
..#..
..#..
#####
..#..
.###.
#...#
.###.""", """
##.##
#.#.#
#...#
.#.#.
..#..
.#.#.
#...#""", """
.###.
#...#
#.#.#
#...#
.###.
..#..
#####""", """
#...#
#...#
#####
.....
#####
#...#
#...#""", """
..#..
.###.
#.#.#
..#..
..#..
.#.#.
#...#""", """
####.
....#
.###.
#....
#....
#...#
.###.""", """
#.#.#
#.#.#
.###.
..#..
..#..
.....
..#..""", """
.##..
#..#.
#..#.
.###.
...#.
..#..
##...""", """
#####
#...#
.#.#.
..#..
.#.#.
#...#
#####""", """
..#..
.#...
#....
.###.
....#
...#.
..#..""",
]

# 16x16-ish icons and props. Keys: k outline, G gold, g dark gold, H gold highlight, P parchment, p parchment
# shade, d parchment dark, R seal red, r seal dark, W white, w light grey, n ink, E green, e dark green,
# B blue, b dark blue, V violet, s steel, S steel light, o orange, y yellow flame
SPRITES = {
'key': """
................
................
..kkkk..........
.kGHHGk.........
kGHkkGGk........
kGk..kGkkkkkkkk.
kGk..kGGGGGGGGGk
kGGkkGgkkkGkGkk.
.kGGGgk..kGkGk..
..kkkk....kkkk..
................""",
'scroll': """
..kkkkkkkkkkkk..
.kPPPPPPPPPPPPk.
kpkPPPPPPPPPPkpk
kpkPnnnnnnnnPkpk
.kkPPPPPPPPPPkk.
..kPnnnnnnnPPk..
..kPPPPPPPPPPk..
..kPnnnnn...Pk..
..kPPPP.....Pk..
..kP........Pk..
..kP.........k..
.kkkkkkkkkkkkkk.
kpkPPPPPPPPPPkpk
.kkkkkkkkkkkkkk.""",
'envelope': """
kkkkkkkkkkkkkkkk
kPdPPPPPPPPPPdPk
kPPdPPPPPPPPdPPk
kPPPdPPPPPPdPPPk
kPPPPdPPPPdPPPPk
kPPPPPdRRdPPPPPk
kPPPPPPRrPPPPPPk
kPPPPPPPPPPPPPPk
kpPPPPPPPPPPPPpk
kppppppppppppppk
kkkkkkkkkkkkkkkk""",
'envq': """
kkkkkkkkkkkkkkkk.....
kPdPPPPPPPPPPdPk.kkk.
kPPdPPPPPPPPdPPkkBBBk
kPPPdPPPPPPdPPPkk..Bk
kPPPPdPPPPdPPPPk..Bk.
kPPPPPdRRdPPPPPk.Bk..
kPPPPPPRrPPPPPPk.k...
kPPPPPPPPPPPPPPk.B...
kpPPPPPPPPPPPPpk.....
kppppppppppppppk.....
kkkkkkkkkkkkkkkk.....""",
'envkey': """
kkkkkkkkkkkkkkkk.....
kPdPPPPPPPPPPdPk.....
kPPdPPPPPPPPdPPk.kkk.
kPPPdPPPPPPdPPPkkGHGk
kPPPPdPPPPdPPPPkGk.Gk
kPPPPPdRRdPPPPPkkGGk.
kPPPPPPRrPPPPPPk.kGk.
kPPPPPPPPPPPPPPk.kGGk
kpPPPPPPPPPPPPpk.kGk.
kppppppppppppppk.kGGk
kkkkkkkkkkkkkkkk..k..""",
'check': """
...........kkk.
..........kEEk.
.........kEEk..
..kk....kEEk...
.kEEk..kEEk....
.kEEEkkEEk.....
..kEEEEEk......
...kEEEk.......
....kkk........""",
'glass': """
...kkkkk.......
..kSSSSSk......
.kSWB...Sk.....
kSB......Sk....
kS.......Sk....
kS.......Sk....
kS.......Sk....
.kS.....Sk.....
..kSSSSSkk.....
...kkkkkGgk....
.........kGgk..
..........kGgk.
...........kGgk
............kk.""",
'form': """
....kkkkkk......
.kkkkGGGGkkkkk..
kddkkkkkkkkddk..
kdPPPPPPPPPPdk..
kdPnnnnnnPPPdk..
kdPPPPPPPPPPdk..
kdPkkPnnnnnPdk..
kdPkEPPPPPPPdk..
kdPPPPPPPPPPdk..
kdPkkPnnnnPPdk..
kdPkEPPPPPPPdk..
kdPPPPPPPPPPdk..
kdddddddddddkk..
.kkkkkkkkkkkk...""",
'merge': """
..kkk.......kkk.
.kVVVk.....kVVVk
.kVWVk.....kVWVk
.kVVVk.....kVVVk
..kVk.......kVk.
..kVk.......kVk.
..kVk......kVk..
..kVk....kkVk...
..kVk..kkVVk....
..kVkkkVVkk.....
..kVVVVkk.......
..kVkkk.........
..kVk...........
.kVVVk..........
.kVWVk..........
.kVVVk..........
..kkk...........""",
'star': """
.....kk.....
.....kGk....
....kGHk....
kkkkkGHGkkkk
kGGGGHHGGGGk
.kGGGHHGGGk.
..kGGGGGGk..
..kGGkkGGk..
.kGGk..kGGk.
.kkk....kkk.""",
'quill': """
..........kkk
.........kWwk
........kWwwk
.......kWwwk.
......kWwwk..
.....kWwwk...
....kWwwk....
...kWwwk.....
...kwwk......
..kGk........
.kGk.........
kGk..........
kk...........""",
'seal': """
..kkkkk..
.kRRRRRk.
kRRrrrRRk
kRrRRRrRk
kRrRWRrRk
kRrRRRrRk
kRRrrrRRk
.kRRRRRk.
..kkkkk..""",
'candle': """
..kk..
.kPPk.
.kPPPk
.kPPPk
.kPPpk
.kPPpk
.kPPpk
.kPPpk
.kPPpk
.kPPpk
kGGGGGGk
.kgggk..""",
}

FLAMES = [
"""
..y..
..y..
.yWy.
.yWy.
oyWyo
.oyo.""",
"""
.y...
.yy..
.yWy.
oyWy.
oyWyo
.oyo.""",
"""
...y.
..yy.
.yWy.
.yWyo
oyWyo
.oyo.""",
"""
.....
..y..
.yWy.
.yWy.
oyWyo
.oyo.""",
]


def parse(src):
    rows = [r for r in src.strip('\n').split('\n')]
    w = max(len(r) for r in rows)
    return [r.ljust(w, '.') for r in rows]


def glyph(src):
    rows = parse(src)
    cols = [x for x in range(len(rows[0])) if any(r[x] == '#' for r in rows)]
    if not cols:
        return rows, 0
    a, b = min(cols), max(cols)
    rows = [r[a:b + 1] for r in rows]
    return rows, b - a + 1


FONT = {ch: glyph(src) for ch, src in FONT_SRC.items()}
SIGNS = [glyph(src) for src in SIGN_SRC]
