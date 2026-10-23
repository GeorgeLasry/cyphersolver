"""v3 verify (b): append one outcome.gaps item (splice saver).  python v3b_gap.py <folder> <item> <blocker> <detail>"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from relabel_r0 import load, save  # noqa: E402
T, item, blocker, detail = sys.argv[1:5]
p = load(T)
g = p['outcome'].get('gaps')
if not isinstance(g, list):
    p['outcome']['gaps'] = [dict(item=item, blocker=blocker, detail=detail)]
else:
    g.append(dict(item=item, blocker=blocker, detail=detail))
save(T, p); print('gap', T, blocker)
