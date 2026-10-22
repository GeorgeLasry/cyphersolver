# 独立の2回目（second/codex_pass*.txt）と書き起こし（data/transcription.tsv）を、ページ・行ごとに記号の並びで比べる。
# 一致＝書き起こしの記号のうち、difflib の一致ブロックに入った数（Codex が余分に書いた記号は数えない）。
# a/b に分けた画像は、行番号ごとにつないでから比べる。
# 使い方: python3 src/compare.py data/key.tsv data/transcription.tsv second/codex_pass1.txt [...]
import sys, os, re, difflib, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from decode import load_key, load_tr
key = load_key(sys.argv[1])
def val(t): v = key.get(t); return v[0] if v else '#' + t
def lineno(i): m = re.match(r'(c\d+)_L?(\d+)', i); return (m.group(1), int(m.group(2)))
mine = collections.defaultdict(list)
for i, toks in load_tr(sys.argv[2]):
    mine[lineno(i)] += [t.rstrip('?') for t in toks if not t.startswith('[') and t != '|']
def codex(path):
    out = collections.defaultdict(list)
    for l in open(path, encoding='utf-8'):
        if '\t' not in l: continue
        n, s = l.rstrip('\n').split('\t', 1); n = n.strip().replace('.jpg', '')
        if not re.match(r'c\d+_L\d+', n): continue
        out[lineno(n)] += [t.split('/')[0] for t in s.split() if not t.startswith('[') and not t.endswith(']')]
    return out
for p in sys.argv[3:]:
    c = codex(p); tot = same = samev = 0; per = collections.defaultdict(lambda: [0, 0])
    for k, a in sorted(mine.items()):
        b = c.get(k, [])
        m = sum(x.size for x in difflib.SequenceMatcher(None, a, b, autojunk=False).get_matching_blocks())
        mv = sum(x.size for x in difflib.SequenceMatcher(None, [val(t) for t in a], [val(t) for t in b], autojunk=False).get_matching_blocks())
        tot += len(a); same += m; samev += mv; per[k[0]][0] += len(a); per[k[0]][1] += m
    print('%s: %d symbols, same name %d (%.1f%%), same value %d (%.1f%%)' % (os.path.basename(p), tot, same, 100*same/tot, samev, 100*samev/tot))
    print('   ' + '  '.join('%s %d/%d %.1f%%' % (k, v[1], v[0], 100*v[1]/v[0]) for k, v in sorted(per.items())))
