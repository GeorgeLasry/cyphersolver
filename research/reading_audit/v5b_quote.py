"""v5 (b): score the blockquote ('> ' lines) of the first section of a reading file (up to the next '## ' heading
after the first quote), with v2_score; bold marks and struck-word brackets removed.

    python research/reading_audit/v5b_quote.py <file> <lang> [--all-quotes] [--unk] [--out NAME]
"""
import pathlib, re, subprocess, sys
HERE = pathlib.Path(__file__).resolve().parent
SCR = pathlib.Path(r'C:\Users\dbour\AppData\Local\Temp\claude\C--Users-dbour-cypher\6b6912a8-0ad3-4eda-b63e-c79291f1bcc5\scratchpad\reread\v5\b')
f, lang = sys.argv[1], sys.argv[2]
ls = pathlib.Path(f).read_text(encoding='utf8').splitlines()
q, started = [], False
for l in ls:
    if l.startswith('> '):
        started = True; q.append(l[2:]); continue
    if started and l.startswith('## ') and '--all-quotes' not in sys.argv: break
b = '\n'.join(q).replace('**', '')
b = re.sub(r'\u27e6[^\u27e7]*\u27e7', ' ', b)
name = sys.argv[sys.argv.index('--out') + 1] if '--out' in sys.argv else pathlib.Path(f).parent.name + '_quote.md'
out = SCR / name
out.write_text('## Reading\n' + b + '\n', encoding='utf8')
r = subprocess.run([sys.executable, str(HERE / 'v2_score.py'), str(out), lang], capture_output=True, text=True, encoding='utf8')
print(r.stdout.strip() or r.stderr[-1500:])
if '--unk' in sys.argv:
    r = subprocess.run([sys.executable, str(HERE / 'v5b_unk.py'), str(out), lang], capture_output=True, text=True, encoding='utf8')
    print(r.stdout.strip())
