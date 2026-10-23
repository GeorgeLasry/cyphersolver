"""v5 (b): potocka1714 - for one section (## R75xx) of reading.md, put each cipher insertion's Interpretation into its
clear anchor (at '...', else after the anchor) and score the resulting phrases with v2_score: the test that each
insertion fits the clear text it sits in.

    python research/reading_audit/v5b_potocka.py <R75xx> <lang> [--show]
"""
import pathlib, re, subprocess, sys
HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[1]
SCR = pathlib.Path(r'C:\Users\dbour\AppData\Local\Temp\claude\C--Users-dbour-cypher\6b6912a8-0ad3-4eda-b63e-c79291f1bcc5\scratchpad\reread\v5\b')
sec, lang = sys.argv[1], sys.argv[2]
t = (ROOT / 'targets' / 'potocka1714' / 'reading.md').read_text(encoding='utf8')
m = re.search(rf'^## {sec}\s*$(.*?)(?=^## |\Z)', t, re.S | re.M)
phr = []
for seg in re.split(r'^### ', m.group(1), flags=re.M)[1:]:
    a = re.search(r'^Clear anchor: (.*)$', seg, re.M)
    i = re.search(r'^Interpretation: (.*)$', seg, re.M)
    if not (a and i): continue
    ins = re.sub(r'\(.*?\)|;.*$|:.*$', '', i.group(1)).strip()
    if re.search(r'verify|doubtful|uncertain', i.group(1), re.I): ins = ' '.join('[?' + w + ']' for w in ins.split())
    anc = a.group(1).strip()
    phr.append(anc.replace('...', ins, 1) if '...' in anc else anc + ' ' + ins)
body = '.\n'.join(phr) + '.'
out = SCR / f'potocka_{sec}.md'
out.write_text('## Reading\n' + body + '\n', encoding='utf8')
if '--show' in sys.argv: print(body)
r = subprocess.run([sys.executable, str(HERE / 'v2_score.py'), str(out), lang], capture_output=True, text=True, encoding='utf8')
print(sec, len(phr), 'insertions |', r.stdout.strip().split(': ', 1)[-1])
