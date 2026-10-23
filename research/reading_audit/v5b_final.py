"""v5 (b): for every row of v5_plainbar_b.txt, score the file the entry now names as its reading (else its decryption),
as the v3 sweep does (body after '## Reading', else the whole file), and print state, file, plain and explicit.

    python research/reading_audit/v5b_final.py
"""
import json, pathlib, subprocess, sys
HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[1]
rows = [l.split('\t') for l in (HERE / 'v5_plainbar_b.txt').read_text(encoding='utf8').splitlines() if l.strip()]
for r in rows:
    t, i, lang = r[0], int(r[1]), r[3]
    e = json.loads((ROOT / 'targets' / t / 'profile.json').read_text(encoding='utf8'))['outcome']['texts'][i]
    f = e.get('reading') or (e['decryption'][0] if isinstance(e.get('decryption'), list) else e.get('decryption'))
    lg = e.get('language') or lang
    if lg == 'zh':
        print(f"{t}\t{i}\t{e.get('state','(read)')}\t{f}\tnot scored (Chinese)"); continue
    out = subprocess.run([sys.executable, str(HERE / 'v2_score.py'), str(ROOT / 'targets' / t / f), lg], capture_output=True,
                         text=True, encoding='utf8').stdout.strip().split(': ', 1)[-1]
    print(f"{t}\t{i}\t{e.get('state','(read)')}\t{lg}\t{f}\t{r[6]}/{r[7]} -> {out}")
