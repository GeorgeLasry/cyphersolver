"""b22: rakoczi1704, print each cipher line of tr/<file> as group=value pairs with the corrected R639 table of
decode_tr.py, and the contemporary interlinear ('# above:' lines) where there is one. Scaffold for the re-reading.

    python -X utf8 research/reading_audit/b22_rk_lines.py R922_p1.txt [...]
"""
import re, sys, importlib.util
from pathlib import Path
T = Path(__file__).resolve().parents[2] / 'targets' / 'rakoczi1704'
spec = importlib.util.spec_from_file_location('dtr', T / 'decode_tr.py'); dtr = importlib.util.module_from_spec(spec)
spec.loader.exec_module(dtr)
for name in sys.argv[1:]:
    print('==', name); k = 0
    for line in (T / 'tr' / name).read_text(encoding='utf-8').splitlines():
        if line.startswith('# above:'): print('     ABOVE:', line[8:].strip()); continue
        if line.startswith('#') or not line.strip(): continue
        k += 1
        out = []
        for g in line.replace('-', ' ').split():
            d = re.sub(r'\D', '', g)
            if not d: out.append(g); continue
            v = dtr.key.get(d)
            out.append(f'{g}={v if v else ("_" if v == "" else "[?]")}')
        print('%02d' % k, ' '.join(out))
