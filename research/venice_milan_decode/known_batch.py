"""Which DECODE ids are referenced in the repo outside the raw DECODE dumps? Usage: known_batch.py 1862 1871 ..."""
import os, re, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'archive_sweep_2026-10'))
import known
SKIP = ('views', 'hcportal', 'cryptoole', 'venice_milan_decode')
corpus = [(n, t) for n, t in known.texts() if not any(s in n for s in SKIP)]
import glob
extra = []
for p in glob.glob(os.path.join(known.ROOT, 'targets', '*', 'profile.json')) + glob.glob(os.path.join(known.ROOT, 'research', 'catalogue_harvest', 'decode', '*.json*')):
    if 'views' in p or 'list' in os.path.basename(p): continue
    extra.append((os.path.relpath(p, known.ROOT), open(p, encoding='utf-8', errors='replace').read()))
corpus += extra
for i in sys.argv[1:]:
    rx = re.compile(rf'\bR{i}\b|RecordsView/{i}\b|(?<![\d.])"?{i}"?(?=[,\]\s])(?<=\d)')
    hits = sorted({n for n, t in corpus if re.search(rf'\bR{i}\b|RecordsView/{i}\b', t)})
    hits2 = sorted({n for n, t in corpus if n.endswith('.json') and re.search(rf'[\[,\s]{i}[,\]]', t)})
    print(i, hits[:6], ('json:' + str(hits2[:4])) if hits2 else '')
