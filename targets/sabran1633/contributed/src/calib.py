# 較正：書き起こし（行ごと、またはCodex の3分割の出力）に鍵を当て、Lasry 氏の解読（calib/lasry_plain.tsv）と文字で比べる。
# 一致率＝difflib の一致ブロックの文字数 ÷ Lasry 氏の文字数（a-z だけ）。3分割の重なりは、前の断片の末尾と次の頭の一致（5記号まで）を落としてつなぐ。
# 使い方: python3 src/calib.py data/key.tsv calib/lasry_plain.tsv calib/transcription_f79.tsv [calib/codex_pass1.txt ...]
import sys, os, re, difflib, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from decode import load_key
key = load_key(sys.argv[1])
lasry = {}
for l in open(sys.argv[2], encoding='utf-8'):
    if l.startswith('#') or not l.strip(): continue
    k, t = l.rstrip('\n').split('\t'); lasry[k] = re.sub(r'[^a-z]', '', t.lower())
def frags(path):
    out = collections.defaultdict(list)
    for l in open(path, encoding='utf-8'):
        if l.startswith('#') or '\t' not in l: continue
        n, s = l.rstrip('\n').split('\t', 1); m = re.match(r'(?:b79_)?(L\d+)', n.strip())
        if not m: continue
        s = re.sub(r'\?\{[^}]*\}', '?', s); s = re.sub(r'\[[^\]]*\]', '', s)
        out[m.group(1)].append([t.split('/')[0] for t in s.split()])
    return out
def join(fs):
    seq = []
    for f in fs:
        k = 0
        for n in range(min(5, len(seq), len(f)), 0, -1):
            if seq[-n:] == f[:n]: k = n; break
        seq += f[k:]
    return seq
def plain(toks):
    out = []; prev = ''
    for t in toks:
        v = key.get(t)
        if v is None: out.append('#'); prev = ''; continue
        val, kind = v
        if kind == 'double': out.append(prev); continue
        if kind == 'word': out.append(re.sub(r'[^a-z]', '', val.split('/')[0])); prev = ''; continue
        out.append(val); prev = val
    return ''.join(out)
for p in sys.argv[3:]:
    F = frags(p); tot = mt = 0
    for k, ref in lasry.items():
        sm = difflib.SequenceMatcher(None, ref, plain(join(F.get(k, []))), autojunk=False)
        tot += len(ref); mt += sum(b.size for b in sm.get_matching_blocks())
    print('%s: %d/%d = %.1f%%' % (os.path.basename(p), mt, tot, 100*mt/tot))
