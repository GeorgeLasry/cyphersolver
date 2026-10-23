"""v5 (b): windischgraetz1720(b) - from a passage table (| | clear text before | numbers | key values | reading |), build
one phrase per cipher passage: the clear words before it + the bold reading (bracketed comments kept as clear text when
they are the letter's own words in parentheses, dropped when they are notes), and score them with v2_score.

    python research/reading_audit/v5b_wtable.py <file> <lang> [--section REGEX] [--show] [--out NAME]
"""
import pathlib, re, subprocess, sys
HERE = pathlib.Path(__file__).resolve().parent
SCR = pathlib.Path(r'C:\Users\dbour\AppData\Local\Temp\claude\C--Users-dbour-cypher\6b6912a8-0ad3-4eda-b63e-c79291f1bcc5\scratchpad\reread\v5\b')
f, lang = sys.argv[1], sys.argv[2]
t = pathlib.Path(f).read_text(encoding='utf8')
if '--section' in sys.argv:
    rx = sys.argv[sys.argv.index('--section') + 1]
    m = re.search(rf'^(#+) [^\n]*{rx}[^\n]*\n(.*?)(?=^\1 |\Z)', t, re.S | re.M)
    t = m.group(2)
phr = []
for l in t.splitlines():
    c = [x.strip() for x in l.strip().strip('|').split('|')]
    if len(c) < 5 or not re.fullmatch(r'[A-Z]{1,2}\d*', c[0]): continue
    before, reading = c[1], c[-1]
    rb = ' '.join(re.findall(r'\*\*(.*?)\*\*', reading))
    aft = re.findall(r'\(([^)]*)\)\s*$', reading)
    after = aft[0] if aft and not re.search(r'[A-Z][a-z]+ed |key|sense|read|unsure|the |Emperor|envoy', aft[0]) else ''
    before = re.sub(r'\(.*?\)|…', ' ', before)
    phr.append(f'{before} {rb} {after}'.strip())
body = '.\n'.join(phr) + '.'
name = sys.argv[sys.argv.index('--out') + 1] if '--out' in sys.argv else pathlib.Path(f).stem + '_phr.md'
out = SCR / name
out.write_text('## Reading\n' + body + '\n', encoding='utf8')
if '--show' in sys.argv: print(body)
r = subprocess.run([sys.executable, str(HERE / 'v2_score.py'), str(out), lang], capture_output=True, text=True, encoding='utf8')
print(len(phr), 'passages |', r.stdout.strip().split(': ', 1)[-1])
