"""v5 (b): insert a markdown heading into a reading file so the scorers find the reading body ('## Reading' ... next
'## '), without touching the text: the heading goes on its own line before the first line matching --before, or after
the first line matching --after (then after the blank line that follows it, if --para). Idempotent: does nothing if
the heading is already there. Line endings kept.

    python research/reading_audit/v5b_heading.py <file> "<heading>" (--before REGEX | --after REGEX) [--para]
"""
import argparse, pathlib, re
a = argparse.ArgumentParser(); a.add_argument('file'); a.add_argument('heading')
a.add_argument('--before'); a.add_argument('--after'); a.add_argument('--para', action='store_true')
o = a.parse_args()
p = pathlib.Path(o.file)
raw = p.read_bytes().decode('utf8')
nl = '\r\n' if '\r\n' in raw else '\n'
ls = raw.split(nl)
if any(l.strip() == o.heading.strip() for l in ls):
    print('already', p); raise SystemExit
if o.before:
    i = next(k for k, l in enumerate(ls) if re.search(o.before, l))
    ins = [o.heading, '']
    if i > 0 and ls[i - 1].strip(): ins = [''] + ins
    ls[i:i] = ins
else:
    i = next(k for k, l in enumerate(ls) if re.search(o.after, l)) + 1
    if o.para:
        while i < len(ls) and ls[i].strip(): i += 1
    ls[i:i] = ['', o.heading] if (i < len(ls) and not ls[i].strip()) else ['', o.heading, '']
p.write_bytes(nl.join(ls).encode('utf8'))
print('heading', o.heading, '->', p)
