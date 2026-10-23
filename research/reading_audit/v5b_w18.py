"""v5 (b): windischgraetz1720b - for one '## No. n' section of dec_R5018_letters.md, put each passage's resolved German
(the bold values on its '- ... = **x**' lines) into its quoted clear context in place of the cipher figures, and score
the passages with v2_score (de).

    python research/reading_audit/v5b_w18.py <n> [--show]
"""
import pathlib, re, subprocess, sys
HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[1]
SCR = pathlib.Path(r'C:\Users\dbour\AppData\Local\Temp\claude\C--Users-dbour-cypher\6b6912a8-0ad3-4eda-b63e-c79291f1bcc5\scratchpad\reread\v5\b')
n = sys.argv[1]
t = (ROOT / 'targets' / 'windischgraetz1720b' / 'dec_R5018_letters.md').read_text(encoding='utf8')
sec = re.search(rf'^## No\. {n},.*?\n(.*?)(?=^## |\Z)', t, re.S | re.M).group(1)
phr = []
for item in re.split(r'^\d+\. ', sec, flags=re.M)[1:]:
    q = re.search(r'"(.*?)"', item, re.S)
    if not q: continue
    ctx = q.group(1)
    vals = []
    for l in item.splitlines():
        if l.strip().startswith('- ') and ('=' in l or '\u2192' in l):
            vals += re.findall(r'(?:=|\u2192)\s*\*\*(.*?)\*\*', l)
    k = iter(vals)
    ctx = re.sub(r'\*\*.*?\*\*', lambda m: next(k, '[?]'), ctx)
    ctx = re.sub(r'\[(den|ander|wer|eine)\]', r'\1', ctx).replace('\u2026', ' ')
    phr.append(ctx.strip())
body = '\n'.join(p.rstrip('.') + '.' for p in phr)
out = SCR / f'w18_no{n}.md'
out.write_text('## Reading\n' + body + '\n', encoding='utf8')
if '--show' in sys.argv: print(body)
r = subprocess.run([sys.executable, str(HERE / 'v2_score.py'), str(out), 'de'], capture_output=True, text=True, encoding='utf8')
print('No.', n, len(phr), 'passages |', r.stdout.strip().split(': ', 1)[-1])
