"""Verification pass 2 (22 Oct 2026), nunzio1736: cut each Spagna 423 reading's body (header and notes off) to a
scratch file and score it with docs/_check_reading.py --file.

    python research/reading_audit/verify2_nunzio_score.py <scratch-dir> [tag]
"""
import os
import pathlib
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'research' / 'reading_audit'))
from verify2_nunzio_align import body  # noqa: E402

DOCS = ['1', '2', '4', '5', '6', '7', '8', '9', '10', '11']


def main(out, tag='x'):
    out = pathlib.Path(out); out.mkdir(parents=True, exist_ok=True)
    for n in DOCS:
        p = out / f'423-{n}_{tag}.md'
        p.write_text(body(int(n)), encoding='utf8')
        r = subprocess.run([sys.executable, str(ROOT / 'docs' / '_check_reading.py'), '--file', str(p)],
                           capture_output=True, text=True, encoding='utf8', env={**os.environ, 'PYTHONUTF8': '1'})
        print(f'423/{n:3s} {tag}: ' + ' '.join(r.stdout.split())[:220])


if __name__ == '__main__':
    main(*sys.argv[1:])
