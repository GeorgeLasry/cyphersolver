"""b16: keyword-in-context for one or more vich1511 groups across the 1511-12 corpus (N.45, N.57, N.60 and the
deciphered siblings). python b16_vich_kwic.py <group> [...]"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from b16_vich_dec import compact
D = pathlib.Path(__file__).resolve().parents[2] / 'targets' / 'vich1511'
FILES = ['n45_pp03-09_v2.txt', 'n45_pp10-15_v2.txt', 'n57_transcription_v3.txt', 'n60_transcription_v4.txt',
         'n41_transcription.txt', 'n39_transcription.txt', 'n12_transcription.txt']
toks = []
for f in FILES:
    if not (D / f).exists(): continue
    for line in open(D / f, encoding='utf-8'):
        if line.startswith('L') and ':' in line:
            tag, body = line.split(':', 1)
            toks += [(f[:3] + tag, t) for t in body.split()]
sys.stdout.reconfigure(encoding='utf-8')
for g in sys.argv[1:]:
    hits = [i for i, (_, t) in enumerate(toks) if t == g]
    print(f'== {g}: {len(hits)}')
    for i in hits:
        L = compact([t for _, t in toks[max(0, i - 12):i]]); R = compact([t for _, t in toks[i + 1:i + 13]])
        print(f'{toks[i][0]:>9}  {L[-45:]:>45} <{g}> {R[:45]}')
