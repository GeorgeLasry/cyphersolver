"""b34: hole census of the (b) decode lines of targets/sessa1523/reading_r9660_b34.txt (R9660 after the post-pass-15
key values). A segment is a run between '/' or '.' marks; a word is a hyphen-joined spelled run, a key value or a
bracket; a hole is an open bracket [x] (a bracket with '=' counts as read; tentative values are counted both ways).

    python research/reading_audit/b34_sessa_holes.py
"""
import re, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[2]
T = (ROOT / 'targets/sessa1523/reading_r9660_b34.txt').read_text(encoding='utf-8').splitlines()
segs = []
for ln in T:
    m = re.match(r'\s*\d+\s*b\s(.*)', ln) or re.match(r'\s*[A-Z]?\d*\s*b\s(.*)', ln)
    if not m: continue
    s = re.sub(r'\([^)]*\)', ' ', m.group(1))           # drop editorial glosses
    s = re.sub(r'"[^"]*"', ' | ', s)                      # clear text in quotes: a segment break, not counted
    for seg in re.split(r'[/.|¶]', s):
        ws = [w for w in seg.split() if re.search(r'\w|\[', w)]
        if ws: segs.append(ws)
def holes(ws, strict):
    n = 0
    for w in ws:
        for b in re.findall(r'\[([^\]]*)\]', w):
            if '=' not in b: n += 1
            elif strict and not b.split('=')[0] in ('ruc','li','Jac','le','net','nuh','kch','cap','lec','dug','doh','yol','sud','pand','Jur','kun','gal','hog','kaz'): n += 1
        if re.search(r'\?', w): n += 1
    return n
for strict in (False, True):
    W = sum(len(s) for s in segs); H = sum(holes(s, strict) for s in segs)
    clean = sum(1 for s in segs if holes(s, strict) <= max(1, len(s)//10) - (0 if len(s) >= 10 else 1) or holes(s, strict) == 0)
    print('strict' if strict else 'lenient', 'segments', len(segs), 'words', W, 'holes', H, 'hole rate %.3f' % (H / W),
          'segments with no hole %d (%.2f)' % (sum(1 for s in segs if holes(s, strict) == 0), sum(1 for s in segs if holes(s, strict) == 0) / len(segs)))
