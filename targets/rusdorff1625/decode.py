"""Apply George Lasry's key (lasry2026/ctts/key.txt) to his CTTS transcription of R4336/R4337.

Prints the mechanical decipherment per image and the token counts used on the page and in profile.json.
  python decode.py            # decipherment
  python decode.py --counts   # counts only
  python decode.py --tokens   # one token per line: image, group, value, class
"""
import re
import sys
from pathlib import Path

HERE = Path(__file__).parent
CTTS = HERE / 'lasry2026' / 'ctts'
IMAGES = ['IMG_R4336_I25992_P1', 'IMG_R4336_I25992_P2',
          'IMG_R4337_I25993_P1', 'IMG_R4337_I25993_P2', 'IMG_R4337_I25993_P3']


def load_key():
    letters, codes, words, clear = {}, {}, {}, {}
    for line in (CTTS / 'key.txt').read_text(encoding='utf8').splitlines():
        if not line or line.startswith('#') or ' - ' not in line:
            continue
        left, right = line.split(' - ', 1)
        if left.startswith('[Plaintext'):
            clear[left] = right
        elif re.fullmatch(r'[\d|]+', left):
            for n in left.split('|'):
                (letters if len(n) == 2 else codes)[n] = right
        else:
            words[left] = right
    return letters, codes, words, clear


def tokens():
    letters, codes, words, clear = load_key()
    for img in IMAGES:
        for line in (CTTS / 'transcription' / f'{img}.txt').read_text(encoding='utf8').splitlines():
            if line.startswith('#'):
                continue
            for t in [t for t in line.split(';') if t]:
                if t in clear:
                    yield img, '', clear[t], 'plain'
                elif t in letters:
                    v = letters[t]
                    yield img, t, v.lower(), 'unc' if v.endswith('?') else ''
                elif t in codes:
                    v = codes[t]
                    cls = 'unk' if v.startswith('[') else ('unc' if v.endswith('?') else 'code')
                    yield img, t, v, cls
                elif t in words:
                    yield img, '', words[t].lower(), 'plain'
                else:
                    yield img, t, '?', 'unk'


def counts():
    n = {'letters': 0, 'codes': 0, 'codes_confident': 0, 'codes_tentative': 0, 'codes_unknown': 0, 'unassigned': 0}
    for _, g, v, cls in tokens():
        if not g:
            continue
        if len(g) == 2:
            n['letters'] += 1
            if v == '?':
                n['unassigned'] += 1
        else:
            n['codes'] += 1
            n['codes_' + {'code': 'confident', 'unc': 'tentative', 'unk': 'unknown'}[cls]] += 1
    return n


if __name__ == '__main__':
    if '--counts' in sys.argv:
        print(counts())
    elif '--tokens' in sys.argv:
        for row in tokens():
            print('\t'.join(row))
    else:
        cur = None
        for img, g, v, cls in tokens():
            if img != cur:
                print(f'\n# {img}')
                cur = img
            print(v if cls == 'plain' else (v.upper() if len(g) == 3 else v), end=' ' if len(g) != 2 else '')
        print()
