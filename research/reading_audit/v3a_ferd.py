"""v3 verify (a), ferdinand1619: join reading.txt (one manuscript line per row, clear text in [..], cipher words the LM
flagged in upper case) into R9426_reading.md. Clear text written in «..» so that it is not taken for supplied words;
flagged words in lower case, the doubtful ones as [?word]; <nnn> nomenclator groups and the clear hand's '...' stay holes.

    python research/reading_audit/v3a_ferd.py
"""
import re, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[2]
T = ROOT / 'targets/ferdinand1619'
L = (T / 'reading.txt').read_text(encoding='utf8').split('\n--- ')[0].splitlines()
DOUBT = {'MERERM', 'TARCEEN', 'PAROICULAR', 'TERRITAROA', 'DERNERSEN', 'GEGAINER', 'SIINEN', 'ION'}
out = ''
for l in L:
    m = re.match(r'^P\d+\.\d+\s+(.*)$', l)
    if not m: continue
    t = m.group(1)
    t = re.sub(r'\[([^\]]*)\]', lambda m: '«' + m.group(1) + '»', t)
    t = re.sub(r'\b[A-ZÄÖÜ]{2,}\b', lambda m: '[?' + m.group(0).lower() + ']' if m.group(0) in DOUBT else m.group(0).lower(), t)
    if out.endswith('-»') and t.startswith('«'):
        out = out[:-2] + t[1:]
    elif out.endswith('-'):
        out = out[:-1] + t
    else:
        out += ' ' + t
out = re.sub(r'» «', ' ', out).strip()
head = """# R9426 - Ferdinand of Bavaria to Maximilian I, Bonn, 22 Dec 1619: reading in running text

Rests on: `reading.txt` (the key-rebuilt decode, one manuscript line per row, 22 Sept 2026). Joined here into running
text for the v3 verification (23 Oct 2026): the clear text of the letter, in brackets there, is written in «...» so
that it is not taken for supplied words; the cipher words the language model flagged (upper case there) are in lower
case, names (Montfart, Erwite, Morres, Lintelo, Herberstorf) as they are, and eight that do not resolve as [?word];
<nnn> are open nomenclator groups (five are nulls per R9425) and "..." the gaps in the clear hand. Spelling as the
figures give it.

## Reading

"""
(T / 'R9426_reading.md').write_text(head + out + '\n', encoding='utf8')
print(out[:1500])
