"""Apply George Lasry's key (lasry2022/ctts/key.txt) to his CTTS transcription of the 43 Sabran images.

  python decode.py            # mechanical decipherment per image
  python decode.py --counts   # sign counts, overall and per manuscript
  python decode.py --tokens   # image, sign, value, class (one per line)
"""
import collections
import sys
from pathlib import Path

CTTS = Path(__file__).parent / 'lasry2022' / 'ctts'
SKIP = {'PLAINTEXT', 'ERASED'}


def source(img):
    if img.startswith('a'):
        return 'Baluze 155'
    return 'fr. 4134' if int(''.join(ch for ch in img if ch.isdigit())) < 100 else 'fr. 4135'


def images():
    names = [p.stem for p in (CTTS / 'transcription').glob('*.txt') if p.stem != 'all']
    key = lambda n: (source(n), int(''.join(ch for ch in n if ch.isdigit()) or 0), n)
    return sorted(names, key=key)


def load_key():
    k = {}
    for line in (CTTS / 'key.txt').read_text(encoding='utf8').splitlines():
        if line.startswith('#ORIGIN') or ' - ' not in line:
            continue
        left, right = line.split(' - ', 1)
        for s in left.split('|'):
            k[s] = right
    return k


def cls(value):
    if value == '?':
        return 'unk'
    if len(value) == 1:
        return 'letter'
    if value.startswith('['):
        return 'unc' if value.endswith('?]') else 'code'
    return 'code'


def tokens():
    k = load_key()
    for img in images():
        for line in (CTTS / 'transcription' / f'{img}.txt').read_text(encoding='utf8').splitlines():
            if line.startswith('#'):
                continue
            for s in [s for s in line.split(';') if s]:
                if s in SKIP:
                    yield img, '', s.lower(), 'plain'
                elif s in k:
                    v = k[s]
                    yield img, s, v.lower() if len(v) == 1 else v, cls(v)
                else:
                    yield img, s, '?', 'missing'


def counts():
    tot = collections.Counter()
    per = collections.defaultdict(collections.Counter)
    for img, s, v, c in tokens():
        if not s:
            continue
        for bucket in (tot, per[source(img)]):
            bucket['signs'] += 1
            bucket[c] += 1
    return tot, dict(per)


if __name__ == '__main__':
    if '--counts' in sys.argv:
        tot, per = counts()
        print('all', dict(tot))
        for k, v in per.items():
            print(k, dict(v))
    elif '--tokens' in sys.argv:
        for row in tokens():
            print('\t'.join(row))
    else:
        cur = None
        for img, s, v, c in tokens():
            if img != cur:
                print(f'\n# {img}')
                cur = img
            print(v if c == 'letter' else f' {v} ', end='')
        print()
