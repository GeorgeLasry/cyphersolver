"""v5 (b): nunzio1718 - join the <PLAINTEXT IT ...> rows of a DECODE/Lasry file (lasry/364D-<n>.txt: the DECODE
transcriber's copy of the interlinear decipherment) into running text and score it with v2_score; also the decode
row (Lasry's values) joined.

    python research/reading_audit/v5b_nunzio.py <n> [<n> ...] [--show]
"""
import pathlib, re, subprocess, sys
HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[1]
SCR = pathlib.Path(r'C:\Users\dbour\AppData\Local\Temp\claude\C--Users-dbour-cypher\6b6912a8-0ad3-4eda-b63e-c79291f1bcc5\scratchpad\reread\v5\b\nunzio1718')
SCR.mkdir(parents=True, exist_ok=True)
for n in [a for a in sys.argv[1:] if not a.startswith('--')]:
    t = (ROOT / 'targets' / 'nunzio1718' / 'lasry' / f'364D-{n}.txt').read_text(encoding='utf8', errors='replace')
    pl = [m.group(1).strip() for m in re.finditer(r'^<PLAINTEXT \w+ (.*)>\s*$', t, re.M)]
    body = ' '.join(pl)
    body = re.sub(r'\s+', ' ', body)
    out = SCR / f'364D-{n}_plain.md'
    out.write_text('## Reading\n' + body + '\n', encoding='utf8')
    if '--show' in sys.argv: print(body)
    r = subprocess.run([sys.executable, str(HERE / 'v2_score.py'), str(out), 'it'], capture_output=True, text=True, encoding='utf8')
    print(n, len(pl), 'rows |', r.stdout.strip().split(': ', 1)[-1])
