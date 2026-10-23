"""v5 (b): score the body of a reading file that has a prose header and no '## Reading' heading: the body starts after
the first blank line that follows a line matching --after (default '^Marks:'), and ends at the next '## ' heading.

    python research/reading_audit/v5b_after.py <file> <lang> [--after REGEX] [--unk] [--show]
"""
import argparse, pathlib, re, subprocess, sys
HERE = pathlib.Path(__file__).resolve().parent
SCR = pathlib.Path(r'C:\Users\dbour\AppData\Local\Temp\claude\C--Users-dbour-cypher\6b6912a8-0ad3-4eda-b63e-c79291f1bcc5\scratchpad\reread\v5\b')
a = argparse.ArgumentParser(); a.add_argument('file'); a.add_argument('lang'); a.add_argument('--after', default=r'^Marks:')
a.add_argument('--unk', action='store_true'); a.add_argument('--show', action='store_true'); a.add_argument('--out')
o = a.parse_args()
ls = pathlib.Path(o.file).read_text(encoding='utf8').splitlines()
i = next(k for k, l in enumerate(ls) if re.search(o.after, l))
while i < len(ls) and ls[i].strip(): i += 1
body = []
for l in ls[i:]:
    if l.startswith('## '): break
    body.append(l)
out = SCR / (o.out or (pathlib.Path(o.file).parent.parent.name + '_' + pathlib.Path(o.file).stem + '_body.md'))
out.write_text('## Reading\n' + '\n'.join(body) + '\n', encoding='utf8')
if o.show: print('\n'.join(body))
r = subprocess.run([sys.executable, str(HERE / 'v2_score.py'), str(out), o.lang], capture_output=True, text=True, encoding='utf8')
print(r.stdout.strip() or r.stderr[-1500:])
if o.unk:
    r = subprocess.run([sys.executable, str(HERE / 'v5b_unk.py'), str(out), o.lang], capture_output=True, text=True, encoding='utf8')
    print(r.stdout.strip())
