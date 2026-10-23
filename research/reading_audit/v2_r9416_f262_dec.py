"""v2 verify sweep (23 Oct 2026): decode the sign-label transcription of R9416 f. 262 (targets/r9416/r9416/f262_signs.txt)
with the key of f262_key.md. Multi-valued signs print their first value (U/W u, 4 u, P w); the reading picks b/p/v/o
by the word. Codes print as [X] [T] [G], unread signs as [?].

    python research/reading_audit/v2_r9416_f262_dec.py
"""
import pathlib, re
ROOT = pathlib.Path(__file__).resolve().parents[2]
KEY = {'8': 'g', 'Q': 'e', '9': 'e', '5': 'n', 'D': 'd', 'U': 'u', 'W': 'u', 'r': 'i', 'y': 't', 'R': 'r', '6': 'm',
       '+': 'h', 'O': 'a', 'C': 'a', '7': 'c', 'F': 'f', '3': 'l', 'E': 's', 'o': 'o', '4': 'u', 'k': 'k', 'Z': 'z',
       '2': 'b', 'P': 'w', 'x': 'i', '#': 'ss', 'N': 'n'}
CODES = {'X': '[X]', 'T': '[T]', 'G': '[G]'}
src = (ROOT / 'targets/r9416/r9416/f262_signs.txt').read_text(encoding='utf-8')
n = 0
for line in src.splitlines():
    if not line.strip() or line.startswith('#'): continue
    lab, *words = line.split()
    out = []
    for w in words:
        if set(w) == {'?'}: out.append('[?]'); continue
        out.append(''.join(CODES.get(c) or KEY.get(c, '[?]') for c in w)); n += len(w)
    print(lab, ' '.join(out))
print('signs', n)
