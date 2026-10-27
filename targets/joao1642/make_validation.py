"""Write validation.tsv: one cipher letter per line with its reading under key.py (first value), taken from the
NORMALISED lines of transcription_l09.txt and transcription_l13.txt (letters read against their clear copies)."""
import re
from key import CIPHER
out = ['# model: pt-modern', '# source: transcription_l09.txt, transcription_l13.txt (NORMALISED lines)',
       '# note: system A letters; code word ft, symbol (+) and unread [..] left out']
for f in ('transcription_l09.txt', 'transcription_l13.txt'):
    block = False
    for line in open(f, encoding='utf8'):
        if line.startswith('NORMALISED'):
            block = True; text = line.split(':', 1)[1]
        elif block and line.startswith('            '):
            text = line
        else:
            block = False; continue
        for w in text.split():
            if w in ('ft', '(+)', '...') or not re.fullmatch(r'[A-Za-zℓ]+', w):
                continue
            for ch in w:
                if ch in CIPHER:
                    out.append(f'{ch}\t{CIPHER[ch][0]}')
open('validation.tsv', 'w', encoding='utf8').write('\n'.join(out) + '\n')
print(len(out) - 3, 'tokens')
