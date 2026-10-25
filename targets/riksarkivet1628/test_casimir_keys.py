"""Decode R4284 and R4306 with the numeric letter keys of KHA A23-311 (../casimir1618/key_*.tsv) and score them."""
import glob, os, re, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
from lang import lm
HERE = os.path.dirname(os.path.abspath(__file__))
targets = {'R4284': 'r4284_transcription.txt', 'R4306': 'r4306_v2.txt'}
models = {m: lm.load(m, order=4, spaces=False) for m in ['la', 'nl-1600', 'de-1640s', 'fr-1600-letters']}
for kf in sorted(glob.glob(os.path.join(HERE, '..', 'casimir1618', 'key_*.tsv'))):
    key = {}
    for line in open(kf, encoding='utf8'):
        if line.startswith('#') or '\t' not in line: continue
        n, v = line.rstrip('\n').split('\t')[:2]
        v = v.rstrip('?').strip()
        if re.fullmatch(r'[a-z]', v) and n.strip().isdigit():
            key.setdefault(int(n), v)        # first letter value per number
    for t, f in targets.items():
        nums = [int(x) for x in re.findall(r'\b\d{1,3}\b', open(os.path.join(HERE, f), encoding='utf8').read())]
        dec = ''.join(key.get(n, '') for n in nums)
        cov = sum(1 for n in nums if n in key) / len(nums)
        if len(dec) < 20:
            print(os.path.basename(kf), t, f'coverage {cov:.0%}', 'too little'); continue
        sc = {m: round(M.per_char(dec), 2) for m, M in models.items()}
        print(os.path.basename(kf), t, f'coverage {cov:.0%}', sc, dec[:60])
