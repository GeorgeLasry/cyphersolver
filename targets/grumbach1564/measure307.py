"""Measure the f. 307 read share from f307_reading.tsv: signs per status (F firm, T tentative, O open)."""
import re
from collections import Counter
from pathlib import Path
c = Counter()
for line in Path(__file__).with_name('f307_reading.tsv').read_text(encoding='utf8').splitlines():
    if line.startswith('#') or not line.strip():
        continue
    run, signs, reading, status = line.split('\t')[:4]
    n = 1 if signs.startswith('[name:') else len(re.sub(r'[^a-z?]', '', signs))
    c[status] += n
tot = sum(c.values())
print(f'signs {tot}: firm {c["F"]} ({c["F"]/tot:.1%}), tentative {c["T"]} ({c["T"]/tot:.1%}), open {c["O"]} ({c["O"]/tot:.1%})')
print(f'give sense (F+T): {(c["F"]+c["T"])/tot:.1%}')
