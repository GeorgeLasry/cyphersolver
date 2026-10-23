"""Run reread_b01_align.py on every record against the edition window its hits point to (reread batch b01)."""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import reread_b01_align as A
WIN = {  # edition line windows from reread_b01_match2.py (bins with >= 20 hits, widened)
 'R286': (22900, 23060), 'R287': (22990, 23170), 'R288': (23260, 23340), 'R289': (23330, 23560),
 'R290': (23460, 23580), 'R291': (23560, 23660), 'R292': (23780, 24010), 'R293': (23990, 24180),
 'R294': (24100, 24200), 'R295': (24150, 24230), 'R297': (24380, 24520), 'R298': (23620, 23740),
 'R299': (24500, 24580), 'R301': (24540, 24620), 'R302': (24600, 24700), 'R305': (24830, 24990),
 'R306': (25440, 25920), 'R307': (25740, 25940), 'R309': (25930, 26060), 'R310': (26250, 26460),
 'R311': (26600, 26860), 'R312': (26780, 26990), 'R313': (26990, 27060),
}
allg = []
for r in sys.argv[1:] or sorted(WIN):
    out, g = A.run(r, *WIN[r]); allg += g
    good = [l for l in out if 'cost/letter' in l]
    print(r, len(g), 'groups;', ' '.join(l.split('cost/letter ')[1].split(',')[0] for l in good))
json.dump(allg, open(os.path.join(HERE, 'reread_b01', 'all_groups.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
