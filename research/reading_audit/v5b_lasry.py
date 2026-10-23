"""v5 (b): cut the excerpt text out of a lasry_entry.md (George Lasry's report pages: 'Excerpt' / folio line / text /
'Translation') and score it with v2_score.

    python research/reading_audit/v5b_lasry.py <folder> <lang> [--show]
"""
import pathlib, re, subprocess, sys
HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[1]
SCR = pathlib.Path(r'C:\Users\dbour\AppData\Local\Temp\claude\C--Users-dbour-cypher\6b6912a8-0ad3-4eda-b63e-c79291f1bcc5\scratchpad\reread\v5\b')
folder, lang = sys.argv[1], sys.argv[2]
t = (ROOT / 'targets' / folder / 'lasry_entry.md').read_text(encoding='utf8')
parts = []
for m in re.finditer(r'^Excerpt\s*\n(.*?)(?=^Translation\s*$)', t, re.S | re.M):
    ls = m.group(1).strip().split('\n')
    ls = [l for l in ls if not re.match(r'^(f\d+[rv]|.*lines?\s*\d|BnF cipher research|\d+ / \d+|--- PDF)', l.strip())]
    parts.append(' '.join(ls))
body = '\n\n'.join(parts)
SCR.mkdir(parents=True, exist_ok=True)
out = SCR / f'{folder}_excerpt.md'
out.write_text('## Reading\n' + body + '\n', encoding='utf8')
if '--show' in sys.argv: print(body)
r = subprocess.run([sys.executable, str(HERE / 'v2_score.py'), str(out), lang], capture_output=True, text=True, encoding='utf8')
print(r.stdout.strip() or r.stderr[-1500:])
