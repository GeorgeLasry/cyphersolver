"""Alphabetical bracketing of the open report groups: for each group with no value in codetable.tsv, the nearest
firm table entries below and above it. The code is roughly alphabetical (words and syllables interleaved), so
the bracket bounds what the group can be; nothing here is a reading.

    python slots.py
"""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
table = {}
for line in open(os.path.join(HERE, 'codetable.tsv'), encoding='utf-8'):
    if line[0] != '#' and line.strip():
        g, v, grade = line.split('\t')[:3]
        if v != '_' and grade == 'H':
            table[int(g)] = v
known = sorted(table)
seen = {}
for line in open(os.path.join(HERE, 'transcription', 'report_61005_tokens.txt'), encoding='utf-8'):
    if line[0] == '#':
        continue
    label, *groups = line.split()
    for g in groups:
        if int(g) not in table:
            seen.setdefault(int(g), []).append(label)
for g in sorted(seen):
    lo = max((k for k in known if k < g), default=None)
    hi = min((k for k in known if k > g), default=None)
    print(f'{g:>5}  in {",".join(seen[g]):<8} between {lo}={table.get(lo)} and {hi}={table.get(hi)}')
