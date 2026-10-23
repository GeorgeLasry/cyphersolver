"""verify2 (smith1562): cut each reading's body (the comment header and the title line off) to a scratch file and score
it with docs/_check_reading.py --file.

    python research/reading_audit/verify2_smith_score.py <scratch-dir> [tag]
"""
import os
import pathlib
import re
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
T = ROOT / 'targets' / 'smith1562'
DOCS = ['no01', 'no03', 'no04', 'no05', 'no06', 'no08', 'no09', 'no11', 'no13', 'no15', 'no16', 'no17', 'no18',
        'no19', 'no20', 'no22']


def main(out, tag='x'):
    out = pathlib.Path(out); out.mkdir(parents=True, exist_ok=True)
    for doc in DOCS:
        s = (T / f'{doc}_reading.md').read_text(encoding='utf8')
        s = re.sub(r'<!--.*?-->', '', s, flags=re.S)
        s = '\n'.join(l for l in s.splitlines() if not l.startswith('#')).strip() + '\n'
        p = out / f'{doc}_{tag}.md'
        p.write_text(s, encoding='utf8')
        r = subprocess.run([sys.executable, str(ROOT / 'docs' / '_check_reading.py'), '--file', str(p)],
                           capture_output=True, text=True, encoding='utf8', env={**os.environ, 'PYTHONUTF8': '1'})
        print(f'{doc} {tag}: ' + ' '.join((r.stdout + r.stderr).split())[:220])


if __name__ == '__main__':
    main(*sys.argv[1:])
