"""Render the [22 Nov 1806] extract with values from weber_key.tsv filled in for the open groups.

weber_key.tsv: one line per group, "<number>\t<value>" (from Weber 1979 pp. 419-30). Lines starting with # are skipped.
Usage: python render.py
"""
import re
from pathlib import Path

HERE = Path(__file__).parent
OPEN = [10, 19, 30, 33, 35, 36, 39, 41, 51, 61, 65, 77]
CONJ = {18: 'army', 46: 'separation', 54: 'officers', 67: 'president', 71: 'Union', 73: 'West'}


def load_key():
    key = {}
    p = HERE / 'weber_key.tsv'
    if p.exists():
        for line in p.read_text(encoding='utf-8').splitlines():
            if line.strip() and not line.startswith('#'):
                n, v = line.split('\t', 1)
                key[int(n)] = v.strip()
    return key


def main():
    key = load_key()
    text = [l for l in (HERE / 'founders_22nov.txt').read_text(encoding='utf-8').splitlines() if not l.startswith('#')]
    body = '\n'.join(text)

    def open_group(m):
        n = int(m.group(1))
        return f'[{n}={key[n]}]' if n in key else m.group(0)

    def conj_group(m):
        n = int(m.group(2))
        return f'[{n}={key.get(n, "?")} | ed. {m.group(1)}]'

    body = re.sub(r'<([A-Za-z]+)\?>=(\d+)', conj_group, body)
    body = re.sub(r'(?<![=\d])\b(\d{2})\.', open_group, body)
    print(body)
    print()
    for n in sorted(OPEN + list(CONJ)):
        print(f'{n:>3}  weber={key.get(n, "-"):<15} editors={CONJ.get(n, "(none)")}')


if __name__ == '__main__':
    main()
