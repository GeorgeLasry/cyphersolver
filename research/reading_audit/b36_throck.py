"""b36: throck1559 R2988 lines 5-15 - decode the sign transcription (targets/throck1559/texts/R2988_signs.tsv) with
Tomokiyo's Cipher 1 (DECODE R2988 key image) plus the project's corrections (texts/key.md) and the code values read in
b36, and count the letters that rest on a look-alike choice (label:value).

    python research/reading_audit/b36_throck.py
"""
import pathlib, re
T = pathlib.Path(__file__).resolve().parents[2] / 'targets' / 'throck1559' / 'texts' / 'R2988_signs.tsv'
# letters: Tomokiyo's table, with the project's corrections (x, υ = i; y = f/h; z = m; ρ = d/t; ſt = w; б = a)
L = {'H': 'a', '6': 'a', 'б': 'a', '┘': 'a', '⊔': 'b', 'M': 'b', 'L': 'c', 'ε': 'c', '⊐': 'd', '℘': 'd', 'v': 'e', '□': 'e',
     'a': 'e', 'V': 'e', '⊏': 'f', 'y': 'f', '¬': 'g', 'ω': 'g', '⊓': 'h', 'μ': 'h', 'υ': 'i', 'x': 'i', 'θ': 'i', 'π': 'k',
     'b': 'l', '1': 'l', 'd': 'm', 'z': 'm', 'e': 'n', '3': 'n', '4': 'o', '⊥': 'o', 'ϱ': 'p', '5': 'p', 'k': 'r', '7': 'r',
     'l': 's', '8': 's', 'ρ': 't', '9': 't', 'q': 'u', 'λ': 'u', 'εt': 'w', 'ſt': 'w', 'T': 'x', ';': 'p', 's': 'p'}
NULLS = {'%', 'Ω', 'δ'}
# codes: key values (Tomokiyo) and b36 values; ? = sense only, ?? = open
CODES = {'á': 'it', 'à': 'it', 'q̇': 'may', 'ἰ': 'in', 'ξ': 'your Majesty', 'ζ': 'your Majesty', 'б̄': 'have', 'r̄': 'had',
         'K': 'all', 'O': 'at', 'Q': 'be', 'G': 'as', 'б': 'as', 'ṭ': 'whom', 'ḟ': 'upon', 'g̲': 'so', 'б̲': 'this',
         'q̄': 'hath?', 'ō': 'good?', 'π̄': 'God?', 'ῡ': 'his?', 'ꝗ̲': 'so?', 'ϱ̲': 'time?', 'δ': 'this?', 'V': 'I?',
         '1̲': '??', 'k̲': '??', 'ť': '??', 'r̲': '??', 'f̄': 'here', 'v̲': '??', 'ℓ̄': '??', '?': 'please?'}
letters = alike = 0
for row in T.read_text(encoding='utf-8').splitlines():
    if row.startswith('#') or row.startswith('line'): continue
    n, signs = row.split('\t')
    out = []
    for s in signs.split():
        if s.startswith('{'):
            out.append('[' + CODES.get(s.strip('{}'), '??') + ']'); continue
        if ':' in s and len(s) > 1:
            g, v = s.split(':', 1)
            if v == '-': continue
            out.append(v); alike += 1; letters += 1; continue
        if s in NULLS: continue
        if s == '●': out.append('?'); continue
        out.append(L.get(s, '<%s>' % s)); letters += 1
    print(n, ''.join(x if len(x) == 1 else ' ' + x + ' ' for x in out))
print('letters', letters, 'look-alike choices', alike, 'share %.3f' % (alike / letters))
