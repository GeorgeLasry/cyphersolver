"""verify2 (ronquillo1676): cut each reading's body (the header comment and title off, the Notes off) to a scratch
file and score it with docs/_check_reading.py --file.

    python research/reading_audit/verify2_ronquillo_score.py <scratch-dir> [tag]
"""
import os
import pathlib
import re
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
R = ROOT / 'targets' / 'ronquillo1676' / 'read'
DOCS = ['R966', 'R967', 'R968', 'R969', 'R970', 'R971', 'R972', 'R973', 'R974', 'R975', 'R976', 'R977', 'R978',
        'R979', 'R980', 'R981', 'R982', 'R983', 'R984', 'R1001']


def main(out, tag='x'):
    out = pathlib.Path(out); out.mkdir(parents=True, exist_ok=True)
    for doc in DOCS:
        s = (R / f'{doc}_reading.md').read_text(encoding='utf8')
        s = re.sub(r'<!--.*?-->', '', s, flags=re.S).split('## Notes')[0]
        s = '\n'.join(l for l in s.splitlines() if not l.startswith('#'))
        p = out / f'{doc}_{tag}.md'
        p.write_text(s.strip() + '\n', encoding='utf8')
        r = subprocess.run([sys.executable, str(ROOT / 'docs' / '_check_reading.py'), '--file', str(p)],
                           capture_output=True, text=True, encoding='utf8', env={**os.environ, 'PYTHONUTF8': '1'})
        print(f'{doc:6s} {tag}: ' + ' '.join(r.stdout.split())[:220])


if __name__ == '__main__':
    main(*sys.argv[1:])
