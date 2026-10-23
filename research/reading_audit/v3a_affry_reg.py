"""v3 verify (a), affry1757: join the checked Fagel register lines (wainut/register_clear.txt) of one letter into
running text (hyphenated line ends joined, MARGIN and % lines dropped). Prints the text; the reading files
read/<R>_reading.md were written from it.

    python research/reading_audit/v3a_affry_reg.py <first line> <last line>     (line numbers in register_clear.txt)
"""
import pathlib, sys, re
ROOT = pathlib.Path(__file__).resolve().parents[2]
L = (ROOT / 'targets/affry1757/wainut/register_clear.txt').read_text(encoding='utf8').splitlines()
a, b = int(sys.argv[1]), int(sys.argv[2])
out = ''
for l in L[a - 1:b]:
    if not l.strip() or l.startswith(('@', '%', 'MARGIN', '#')):
        continue
    l = l.strip()
    if out.endswith('-'):
        out = out[:-1] + l
    else:
        out += (' ' if out else '') + l
print(out)
