# 対照：key.tsv の文字の記号の値をかき混ぜた鍵（1000回）と、本物の鍵とで、平文のフランス語らしさを比べる。
# フランス語らしさ＝wordfreq の仏語上位5万語から作った文字3連の対数尤度の平均（j→i、v→u に寄せる）。
# 語の数字・重ね記号・読めない記号・平文の語で連なりを切り、1文字の記号の連なりだけを採点する。
# 使い方: python3 control.py key.tsv tr.tsv [ID の頭（例 c100）] [試行回数] [--strict]
import sys, os, random, math, collections
from wordfreq import top_n_list, word_frequency
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from decode import load_key, load_tr
def build_model():
    tri = collections.Counter(); bi = collections.Counter()
    for w in top_n_list('fr', 50000):
        w2 = ''.join(c for c in w.lower() if c.isalpha())
        w2 = w2.replace('œ', 'oe').translate(str.maketrans('éèêëàâäîïôöùûüç', 'eeeeaaaiioouuuc'))
        w2 = w2.replace('j', 'i').replace('v', 'u')   # 当時の表には j・v がない
        if not w2: continue
        f = word_frequency(w, 'fr')
        s = '^' + w2 + '$'
        for i in range(len(s) - 2):
            tri[s[i:i+3]] += f; bi[s[i:i+2]] += f
    alpha = 'abcdefghilmnopqrstuxyz^$'
    def lp(a, b, c):
        return math.log((tri[a+b+c] + 1e-7) / (bi[a+b] + 1e-7 * len(alpha)))
    return lp

key = load_key(sys.argv[1]); rows = load_tr(sys.argv[2])
pref = sys.argv[3] if len(sys.argv) > 3 else ''
N = int(sys.argv[4]) if len(sys.argv) > 4 else 1000
STRICT = '--strict' in sys.argv  # 末尾 ? の付いた（読みの不確かな）記号も区切りにする
letters = {k: v[0] for k, v in key.items() if v[1] == 'letter'}
runs = []
for i, toks in rows:
    if not i.startswith(pref): continue
    cur = []
    for t in toks:
        t0 = t.rstrip('?') if t != '?' else t
        if STRICT and t.endswith('?'): t0 = None
        if t0 in letters: cur.append(t0)
        else:
            if cur: runs.append(cur); cur = []
    if cur: runs.append(cur)
lp = build_model()
def score(m):
    tot = n = 0
    for r in runs:
        s = '^' + ''.join(m[k] for k in r) + '$'
        for j in range(len(s) - 2): tot += lp(s[j], s[j+1], s[j+2]); n += 1
    return tot / n
real = score(letters)
names = list(letters); vals = [letters[k] for k in names]
random.seed(1); ge = 0; sc = []
for _ in range(N):
    random.shuffle(vals); m = dict(zip(names, vals)); s = score(m); sc.append(s); ge += s >= real
sc.sort()
print(('strict ' if STRICT else '') + '%s runs=%d symbols=%d real=%.3f shuffled median=%.3f max=%.3f >=real %d/%d' % (pref or 'all', len(runs), sum(map(len, runs)), real, sc[N//2], sc[-1], ge, N))
