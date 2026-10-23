"""Apply George Lasry's CTTS key (lasry2021/ctts/key.txt) to his CTTS transcription and count the signs.

  python decode.py            # mechanical decipherment, one line per transcription line
  python decode.py --counts   # sign counts
  python decode.py --tsv      # write validation.tsv for docs/_validate.py
"""
import sys, collections
from pathlib import Path

HERE = Path(__file__).parent
CTTS = HERE / 'lasry2021' / 'ctts'
SKIP_HEAD = {}   # f122b used to repeat the last two lines of f122a; Lasry's PR 85 transcribes them once (from f122b)


def load_key():
    key = {}
    for line in (CTTS / 'key.txt').read_text(encoding='utf8').splitlines():
        if line.startswith('#') or ' - ' not in line:
            continue
        signs, value = line.rsplit(' - ', 1)
        for s in signs.split('|'):
            key[s] = value
    return key


def lines():
    """(image, [(sign, value), ...]) per transcription line, overlap lines dropped."""
    key = load_key()
    for f in sorted((CTTS / 'transcription').glob('*.txt')):
        if f.name == 'all.txt':
            continue
        rows = [l for l in f.read_text(encoding='utf8').splitlines() if l.strip() and not l.startswith('#')]
        for l in rows[SKIP_HEAD.get(f.stem, 0):]:
            yield f.stem, [(t, key.get(t, '?')) for t in l.split(';') if t]


def kind(v):
    if v in ('_', '[null?]'):
        return 'null'
    if v == '?':
        return 'unassigned'
    if v.startswith('['):
        return 'special'
    return 'letter' if len(v) == 1 else 'code'


if __name__ == '__main__':
    if '--counts' in sys.argv:
        c = collections.Counter(kind(v) for _, row in lines() for _, v in row)
        print(dict(c), 'total', sum(c.values()))
    elif '--tsv' in sys.argv:
        out = ['# model: es-golden-age', '# source: decode.py over lasry2021/ctts/transcription with lasry2021/ctts/key.txt (George Lasry)',
               '# note: nulls as -, nomenclator words as their word, special and bracketed signs left unread']
        for _, row in lines():
            for t, v in row:
                k = kind(v)
                out.append(f'{t}\t' + ('-' if k == 'null' else v.lower() if k in ('letter', 'code') else '?'))
        (HERE / 'validation.tsv').write_text('\n'.join(out) + '\n', encoding='utf8')
        print(len(out) - 3, 'tokens written')
    else:
        for img, row in lines():
            print(img, ''.join(v.lower() if kind(v) == 'letter' else f' {v} ' if kind(v) != 'null' else '' for _, v in row))
