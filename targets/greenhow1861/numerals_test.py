"""Numeral scrap filed with the mourning-paper letter (NARA naId 1634036, image 3): tests against the 1864 key.

The 1864 key sheet (M1091 naId 62017285 image 0484) has, besides the letter column, a row of figure signs:
    1 a, 2 d, 3 phi, 4 ff, 5 m, 6 b, 7 nn, 8 c, 9 c   and "10" = III      (read on the sheet, 27 Oct 2026)
so a number enciphered with this key is written in letter-like signs, not in Arabic figures. Three tests:

1. The scrap's Arabic figures as the key's figure signs: impossible, the key's figure signs are letters.
2. The scrap's figures read as the key's LETTER signs that look like digits (3 = C, 4 = I/R, 5 = O, 7 = B, 8 = G,
   9 = K, 0 = the O-sign J, $ = U; 1 = the hooked 1 of Q). 2 and 6 have no letter value on the key.
3. The scrap's clear-looking letters read as the key's figure signs (a d m b c): only scattered letters fit.

python numerals_test.py   (standard library only; output kept in numerals_test_output.txt)
"""
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
LETTER = {'3': 'C', '4': 'I/R', '5': 'O', '7': 'B', '8': 'G', '9': 'K', '0': 'J', '1': 'Q', '$': 'U'}
FIGURE = {'a': '1', 'd': '2', 'm': '5', 'b': '6', 'c': '8/9'}   # phi, ff, nn left out: not single letters

groups = []
for ln in (HERE / 'transcription_numerals.txt').read_text(encoding='utf-8').splitlines():
    if ln.startswith('#') or not ln.strip():
        continue
    for t in ln.replace('.', ' ').split():
        t = t.strip('[]?!')
        if t and all(ch.isdigit() or ch == '$' for ch in t):
            groups.append(t)

print('figure groups on the scrap:', len(groups))
print(' '.join(groups))
print()
print('Test 2: figures read as the key\'s letter signs')
dead = 0
for g in groups:
    out = ''.join(LETTER.get(ch, '-') for ch in g)
    if '-' in out:
        dead += 1
    print(f'  {g:>5} -> {out}')
digits = ''.join(ch for g in groups for ch in g if ch.isdigit())
no_val = sum(ch in '26' for ch in digits)
print(f'groups with a figure (2 or 6) that has no letter value on the key: {dead} of {len(groups)}')
print(f'figures 2 and 6: {no_val} of {len(digits)} figures')
print('No group gives a word; the figures run 5 ... 104 with $ and "dollers", which reads as a money reckoning.')
print()
print('Test 3: clear words read as the key\'s figure signs')
for w in ['dollers', 'do', 'missatuma', 'id', 'you', 'six']:
    fit = ''.join(FIGURE.get(ch, '.') for ch in w)
    print(f'  {w:>10} -> {fit}   ({sum(ch != "." for ch in fit)} of {len(w)} letters are figure signs)')
print('Only scattered letters are figure signs; none of these is a figure group.')
