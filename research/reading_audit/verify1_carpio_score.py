"""verify1 (carpio1677): cut the reading body of each read/R*_reading.md (no HTML comment, no title, no Notes) to a
scratch file and score it with docs/_check_reading.py --file.

    python research/reading_audit/verify1_carpio_score.py <scratch_dir> [doc ...]
"""
import pathlib
import re
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
R = ROOT / 'targets' / 'carpio1677' / 'read'
DOCS = ['R1002', 'R1003', 'R1006', 'R1007', 'R1008', 'R1009', 'R1010', 'R1011']


def body(doc):
    s = (R / f'{doc}_reading.md').read_text(encoding='utf8')
    s = re.sub(r'<!--.*?-->', '', s, flags=re.S)
    s = s.split('## Notes')[0]
    return '\n'.join(l for l in s.splitlines() if not l.startswith('#')).strip() + '\n'


if __name__ == '__main__':
    out = pathlib.Path(sys.argv[1])
    out.mkdir(parents=True, exist_ok=True)
    for doc in sys.argv[2:] or DOCS:
        f = out / f'carpio_{doc}_body.md'
        f.write_text(body(doc), encoding='utf8')
        r = subprocess.run([sys.executable, str(ROOT / 'docs' / '_check_reading.py'), '--file', str(f)],
                           capture_output=True, text=True, encoding='utf8', env={'PYTHONUTF8': '1', **__import__('os').environ})
        line = [l for l in r.stdout.splitlines() if 'clean' in l]
        print(doc, '|', ' / '.join(line) or r.stdout.strip()[-300:] or r.stderr[-300:])
