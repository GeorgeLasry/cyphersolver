"""b32: build targets/raince/trans/residue1526_reading.md from trans/reading_v3.txt (the 5 Oct 2026 glyph-by-glyph
re-reading), in the reading-file conventions of REREAD_BRIEF.md.

- A word with unresolved glyphs ('?' inside it, e.g. 'respo??', 'e??r') becomes '[...]'; a bare '?' (one unresolved
  token) becomes '[...]'; 'word(?)' becomes '[?word]'.
- A word broken at a manuscript line end is joined onto the line where it starts, when the join is a word of the
  checker's French list or one of the two halves is not a word (the manuscript breaks words freely); else the line
  break is kept as a word break. Every join is listed in the log (stdout).
- Word signs of the key ([roy], [pape], [le pape], [l empereur]) are kept; the unidentified signs stay [X], [X2], [Y].

    python research/reading_audit/b32_raince_build.py > <log>
"""
import re, sys, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'docs')); sys.path.insert(0, str(ROOT))
import _check_reading as cr
LEX = cr.lexicon('fr')
src = (ROOT / 'targets/raince/trans/reading_v3.txt').read_text(encoding='utf8').splitlines()

pages, cur = [], None
for l in src:
    m = re.match(r'## (p\. \d+)\s+\((.*)\)', l)
    if m:
        cur = [m.group(1), m.group(2), []]; pages.append(cur); continue
    m = re.match(r'(\d\d) [RH] \| (.*)$', l)
    if m and cur:
        cur[2].append((m.group(1), m.group(2)))


def conv(w):
    if w.startswith('['):
        return w
    if w.endswith('(?)'):
        core = w[:-3]
        return '[...]' if '?' in core else '[?%s]' % core
    if '?' in w:
        return '[...]'
    return w.replace('(con)', 'con')


def isword(w):
    return lm_norm(w) in LEX


def lm_norm(w):
    return cr.lm.norm(w, 'early').replace(' ', '')


# breaks the heuristic gets wrong, checked by hand: keep the line break as a word break
SKIP = {('p. 29', '19'), ('p. 30', '01'), ('p. 30', '12'), ('p. 30', '30'), ('p. 31', '04'), ('p. 31', '14'),
        ('p. 31', '24'), ('p. 105', '05'), ('p. 105', '10')}
out_pages = []
for name, desc, lines in pages:
    toks = [[conv(w) for w in re.findall(r'\[[^\]]*\]|\S+', txt)] for _, txt in lines]
    for i in range(len(toks) - 1):
        a, b = toks[i], toks[i + 1]
        if not a or not b: continue
        x, y = a[-1], b[0]
        if x.startswith('[') or y.startswith('['): continue
        if (name, lines[i][0]) == ('p. 30', '03') and a[-2:] == ['mes', 'm'] and y == 'ement':
            a[-2:] = ['mesmement']; b.pop(0); print('join p. 30 l.03: mes m + ement -> mesmement'); continue
        if (name, lines[i][0]) in SKIP: print('kept break %s l.%s: %s | %s' % (name, lines[i][0], x, y)); continue
        j = x + y
        if isword(j) or not (isword(x) and isword(y)):
            a[-1] = j; b.pop(0)
            print('join %s l.%s: %s + %s -> %s' % (name, lines[i][0], x, y, j))
    out_pages.append((name, desc, [(n, ' '.join(t)) for (n, _), t in zip(lines, toks)]))

hdr = """# Raince, BnF fr. 2984, the ciphered residue of 13 May 1526 (pp. 29-31) and 20 Nov 1526 (p. 105): reading

Built 23 Oct 2026 (batch b32, research/reading_audit/b32_raince_build.py) from `trans/reading_v3.txt`, the 5 Oct 2026
re-reading of all 106 lines glyph by glyph off the numbered-token images of the Gallica microfilm against Tomokiyo's
1526 key as re-measured (CALIBRATION.md). Spelling as the glyphs give it; one line per manuscript line, a word broken
at a line end written whole on the line where it starts. Word signs of the key: [roy], [pape], [le pape],
[l empereur]; unidentified signs [X] (two-crossbar stem, a person), [X2] (circled cross), [Y] (cursive ell with a
ring, a name or title); `[...]` unresolved glyphs; `[?word]` doubtful. p. 29 ll. 1-10 (glossed at the time) are not
part of this residue.

## Reading
"""
body = []
for name, desc, lines in out_pages:
    body.append('')
    for n, t in lines:
        body.append(t)
    body.append('')
(ROOT / 'targets/raince/trans/residue1526_reading.md').write_text(hdr + '\n'.join(body) + '\n## Notes\n\nPage breaks: '
    + '; '.join('%s (%s): %d lines' % (n, d, len(l)) for n, d, l in out_pages) + '.\n', encoding='utf8')
