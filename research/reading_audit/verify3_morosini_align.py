"""VERIFY_BRIEF pass 3, morosini1588: run reread_b00_align.py on every enclosure (4 at a time) into <outdir>.

    PYTHONUTF8=1 python research/reading_audit/verify3_morosini_align.py <outdir> [R..]

Writes <outdir>/<R>.txt and prints each record's TOTAL line plus its flagged words with letters lacking a figure.
"""
import os, subprocess, sys
from concurrent.futures import ThreadPoolExecutor

HERE = os.path.dirname(os.path.abspath(__file__))
from verify3_morosini_score import RECS  # noqa: E402


def run(r, out):
    p = subprocess.run([sys.executable, os.path.join(HERE, 'reread_b00_align.py'), r], capture_output=True, text=True,
                       encoding='utf-8', env=dict(os.environ, PYTHONUTF8='1'), cwd=HERE)
    txt = p.stdout + p.stderr
    open(os.path.join(out, f'{r}.txt'), 'w', encoding='utf-8').write(txt)
    return r, txt


def main():
    out = sys.argv[1]
    os.makedirs(out, exist_ok=True)
    recs = sys.argv[2:] or RECS
    with ThreadPoolExecutor(4) as ex:
        for r, txt in ex.map(lambda r: run(r, out), recs):
            print(f'#### {r}')
            for line in txt.splitlines():
                if line.startswith(('TOTAL', '   SUPPLIED', '   PARTLY', '==')) and ('page not' in line or 'no align' in line or not line.startswith('==')):
                    print(line)


if __name__ == '__main__':
    main()
