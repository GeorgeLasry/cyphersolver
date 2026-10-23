"""Verification pass (22 Oct 2026), matignon1586: cut each reading's body (header and notes off) to a scratch file
and score it with docs/_check_reading.py --file.

    python research/reading_audit/verify1_matignon_score.py <scratch-dir> [tag]
"""
import pathlib
import re
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
T = ROOT / 'targets' / 'matignon1586' / 'texts'
BODIES = {
    'f173': ('reading_f173.md', '## The clear opening', 'Files:'),
    'f196+f201': ('reading_f196_201.md', '## The fever', None),
    'f196v': ('reading_f196v.md', '## The siege', '(The signature'),
    'f177': ('reading_f177.md', '## The cipher', '## What stays open'),
    'f110': ('reading_f110.md', '## The cipher', 'Files:'),
    'f123v': ('reading_f123.md', '## The cipher, f. 123v', '## Notes on the reading'),
    'f124v': ('reading_f124.md', '## f. 124v', '## What stays open'),
    'f143v-tail': ('reading_f143v_tail.md', '## The cipher, from', '## Notes on the words'),
}


def main(out, tag='x'):
    out = pathlib.Path(out); out.mkdir(parents=True, exist_ok=True)
    for doc, (fn, a, b) in BODIES.items():
        s = (T / fn).read_text(encoding='utf8')
        i = s.index(a)
        j = s.index(b, i) if b else len(s)
        p = out / f'{doc}_{tag}.md'
        p.write_text(s[i:j], encoding='utf8')
        r = subprocess.run([sys.executable, str(ROOT / 'docs' / '_check_reading.py'), '--file', str(p)],
                           capture_output=True, text=True, encoding='utf8', env={'PYTHONUTF8': '1', **__import__('os').environ})
        m = re.search(r'clean share ([\d.]+)', r.stdout) or re.search(r'clean[^\n]*?([01]\.\d+)', r.stdout)
        print(f'{doc:12s} {tag}: ' + ' '.join(r.stdout.split())[:200])


if __name__ == '__main__':
    main(*sys.argv[1:])
