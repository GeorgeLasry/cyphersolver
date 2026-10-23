"""cl consistency pass: move closed items out of a NOTES.md "## Remaining gaps" list (the checker reads every bullet
there as an open gap). Each bullet whose text contains one of the given substrings is removed from the list and
restated below it as a "Closed:" paragraph. Line endings kept.

    python research/reading_audit/cl_gaps.py <folder> "<substring>" ["<substring>" ...]
"""
import re
import sys
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[2]
CR, LF = chr(13), chr(10)
T, subs = sys.argv[1], sys.argv[2:]
f = ROOT / 'targets' / T / 'NOTES.md'
s = open(f, encoding='utf8', newline='').read()
nl = CR + LF if CR + LF in s else LF
m = re.search(r'^##\s+Remaining gaps\b.*?$(.*?)(?=^##\s|\Z)', s, re.M | re.S | re.I)
assert m, T
body = m.group(1)
lines = body.split(nl)
keep, closed = [], []
for l in lines:
    if l.lstrip().startswith(('-', '*')) and any(x in l for x in subs):
        closed.append(re.sub(r'^\s*[-*]\s*', '', l))
    else:
        keep.append(l)
assert len(closed) == len(subs), (T, len(closed), subs)
# insert the closed paragraph after the last bullet of the list
last = max(i for i, l in enumerate(keep) if l.lstrip().startswith(('-', '*')))
para = ['', *('Closed (taken out of the open list, 23 Oct 2026): ' + c for c in closed)]
keep = keep[:last + 1] + para + keep[last + 1:]
s = s[:m.start(1)] + nl.join(keep) + s[m.end(1):]
open(f, 'w', encoding='utf8', newline='').write(s)
print('gaps', T, len(closed), 'closed')
