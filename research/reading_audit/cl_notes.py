"""cl consistency pass: exact-string edits to a target's NOTES.md (line endings kept).
    python research/reading_audit/cl_notes.py <folder> <edits.json>   edits: [[old, new], ...]; old "" = append new at end
"""
import json
import sys
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[2]
CR, LF = chr(13), chr(10)
T, path = sys.argv[1], sys.argv[2]
f = ROOT / 'targets' / T / 'NOTES.md'
s = open(f, encoding='utf8', newline='').read()
crlf = CR + LF in s
nl = CR + LF if crlf else LF
for old, new in json.loads(pathlib.Path(path).read_text(encoding='utf8')):
    if crlf:
        old, new = old.replace(LF, nl), new.replace(LF, nl)
    if old == '':
        s = s.rstrip(CR + LF) + nl + new + ('' if new.endswith(LF) else nl)
        continue
    assert s.count(old) == 1, (T, old[:80], s.count(old))
    s = s.replace(old, new)
open(f, 'w', encoding='utf8', newline='').write(s)
print('notes', T)
