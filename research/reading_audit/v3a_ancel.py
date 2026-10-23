"""v3 verify (a), ancel1577: pull the reading column of contributed/READING.en.md into running text per letter.

    python research/reading_audit/v3a_ancel.py <section start text>     e.g. "p.525"

Hyphenated line ends are joined. Marks (◎ ○ △) dropped. Prints the raw joined reading column.
"""
import pathlib, sys, re
ROOT = pathlib.Path(__file__).resolve().parents[2]
s = (ROOT / 'targets/ancel1577/contributed/READING.en.md').read_text(encoding='utf8')
parts = re.split(r'^## ', s, flags=re.M)
sec = [p for p in parts if p.startswith(sys.argv[1])][0]
out = ''
for l in sec.splitlines():
    if not l.startswith('|') or l.startswith('| line') or l.startswith('|---'):
        continue
    c = [x.strip() for x in l.strip('|').split('|')]
    r = c[2]
    if out.endswith('-') and r.startswith('-'):
        out = out[:-1] + r[1:]
    elif out.endswith('-'):
        out = out[:-1] + r
    else:
        out += ' ' + (r[1:] if r.startswith('-') else r)
print(out.strip())
