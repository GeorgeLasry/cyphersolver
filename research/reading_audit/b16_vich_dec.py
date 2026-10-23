"""b16: compact decode of a vich1511 transcription for building a reading.

Letters run together; code-group values in UPPER CASE (so word/syllable codes stay visible); unknown groups as
[grp]; '.' for the sentence marks. Usage: python b16_vich_dec.py <transcription> [out]"""
import sys, pathlib, re
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / 'targets' / 'vich1511'))
from decode import LET, CODE, MARK

def compact(tokens):
    out = []
    for t in tokens:
        if t in MARK: out.append(' '); continue
        if t in CODE:
            v = CODE[t]
            out.append(v if v == '.' else v.upper().replace(' ', '_'))
        elif t in LET: out.append(LET[t])
        else: out.append('[' + t + ']')
    return ''.join(out)

if __name__ == '__main__':
    lines = []
    for line in open(sys.argv[1], encoding='utf-8'):
        if not line.startswith('L'): continue
        tag, body = line.split(':', 1)
        lines.append(f'{tag} {compact(body.split())}')
    txt = '\n'.join(lines) + '\n'
    if len(sys.argv) > 2: open(sys.argv[2], 'w', encoding='utf-8').write(txt)
    else: sys.stdout.reconfigure(encoding='utf-8'); print(txt)
