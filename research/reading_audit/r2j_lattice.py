"""r2j (matignon1586c3, fr. 15573 ff. 379-381): word lattice over Burford's sign transcription and key, to PROPOSE
where a sign's key value fails and which single-letter value would give a period word. Nothing here is a reading: every
proposal is checked on the image and a value is adopted only if it holds at several independent places.

Each sign emits its key value(s) at cost 0; any other single letter at cost SUB; nothing (null) at cost DEL; an
unreadable sign ('?', no value) is a hole. Words come from the Henri IV letters corpus (fr-henri4, early norm, period
spelling) plus names. Output: the best segmentation, page by page, with substitutions marked <sign:letter>, and a tally
of substitutions per sign class.

    python research/reading_audit/r2j_lattice.py [SUB] [DEL]
"""
import json, math, os, re, sys, collections, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from lang import lm
D = ROOT / 'targets/matignon1586c3/f379_381'
PAGES = ['f379r', 'f379v', 'f380r', 'f380v', 'f381r', 'f381v']
SUB = float(sys.argv[1]) if len(sys.argv) > 1 else 7.0
DEL = float(sys.argv[2]) if len(sys.argv) > 2 else 8.0
HOLE = 13.0
# extra candidate values to test: XV='p+:b,b:y' (cost XC each)
XV = {}
for _p in os.environ.get('XV', '').split(','):
    if ':' in _p: _s, _v = _p.split(':', 1); XV.setdefault(_s, []).append(_v)
XC = float(os.environ.get('XC', '1.5'))
EXTRA = ('bourdeaulx tolouse garone caumont verdun bazeille clervant poigny lenoncourt brulart villeroy nicullier '
         'agen marmande gourgues castelnau bearnais navarrains castillon bergerac foy duras espaigne chastillon '
         'languedoc conptablie convoy daces utillite soullaigement incomode isle dordoigne').split()

def lexicon():
    cache = ROOT / 'lang/cache/r2j_fr_henri4_words.json'
    if cache.exists():
        return json.load(open(cache, encoding='utf8'))
    t = lm.norm(open(ROOT / 'lang/corpora/fr-henri4.txt', encoding='utf8').read(), 'early')
    c = collections.Counter(re.findall(r'[a-z]+', t))
    c = {w: n for w, n in c.items() if n >= 3 or len(w) <= 2}
    json.dump(c, open(cache, 'w', encoding='utf8'))
    return c

def load_signs():
    out = []
    for p in PAGES:
        d = D / 'burford' / p
        table = json.load(open(d / 'key.json', encoding='utf-8'))['pipeline'][0]['table']
        for raw in open(d / 'signs.txt', encoding='utf-8'):
            if not raw.strip() or raw.startswith('#'): continue
            num, _, signs = raw.rstrip('\n').partition('\t')
            for k, s in enumerate(signs.split()):
                v = (table.get(s) or {}).get('v')
                vals = v if isinstance(v, list) else ([v] if v else [])
                vals = [x.replace('_', '') for x in vals if x]
                out.append(dict(page=p, line=int(num), pos=k, sign=s, vals=vals))
    return out

def main():
    lex = lexicon()
    for w in EXTRA: lex[w] = max(lex.get(w, 0), 5)
    tot = sum(lex.values())
    wcost = {w: -math.log(n / tot) for w, n in lex.items()}
    trie = {}
    for w in wcost:
        n = trie
        for ch in w: n = n.setdefault(ch, {})
        n['$'] = wcost[w]
    S = load_signs()
    N = len(S)
    # state: (node id) -> (cost, backpointer); nodes keyed by id(dict)
    ROOTN = trie
    beams = [dict() for _ in range(N + 1)]
    beams[0][id(ROOTN)] = (0.0, None, ROOTN, '')
    BEAM = 400
    def push(b, node, cost, back, emit):
        k = id(node)
        if k not in b or b[k][0] > cost: b[k] = (cost, back, node, emit)
    for i in range(N):
        cur = beams[i]
        if not cur: continue
        items = sorted(cur.values(), key=lambda x: x[0])[:BEAM]
        sg = S[i]; nxt = beams[i + 1]
        for cost, back, node, emit in items:
            me = (i, id(node))
            # close a word at root? handled when entering: allow word end -> root before consuming
            starts = [(node, cost, '')]
            if '$' in node and node is not ROOTN:
                starts.append((ROOTN, cost + node['$'], ' '))
            for nd, c0, sep in starts:
                opts = []
                for v in sg['vals']:
                    opts.append((v, 0.0, v))
                for v in XV.get(sg['sign'], []):
                    opts.append((v, XC, '<%s=%s>' % (sg['sign'], v)))
                if not sg['vals']:
                    opts.append(('', HOLE * 0.5, '{?}'))
                for ch in 'abcdefghilmnopqrstuxyz':
                    if not any(v == ch for v in sg['vals']):
                        opts.append((ch, SUB, '<%s:%s>' % (sg['sign'], ch)))
                opts.append(('', DEL, '<%s:->' % sg['sign']))
                for v, c1, lab in opts:
                    n2 = nd; ok = True; tmp = c0 + c1
                    # walk v through trie, allowing word breaks inside multi-letter values
                    j = 0
                    while j < len(v):
                        ch = v[j]
                        if ch in n2: n2 = n2[ch]; j += 1
                        elif '$' in n2 and n2 is not ROOTN: tmp += n2['$']; n2 = ROOTN
                        else: ok = False; break
                    if not ok: continue
                    push(nxt, n2, tmp, (i, me, sep, lab), None)
                # hole: consume this sign as an unread one-sign word (only from root)
                if nd is ROOTN:
                    push(nxt, ROOTN, c0 + HOLE, (i, me, sep, '[%s]' % sg['sign']), None)
        # keep store of beams for backtrace
    # finish
    best = None
    for k, (cost, back, node, _) in beams[N].items():
        c = cost + (node['$'] if '$' in node and node is not ROOTN else (0 if node is ROOTN else 99))
        if best is None or c < best[0]: best = (c, k)
    # backtrace
    seq = []; i = N; k = best[1]
    while i > 0:
        cost, back, node, _ = beams[i][k]
        bi, (pi, pk), sep, lab = back
        seq.append((bi, sep, lab)); i = pi; k = pk
    seq.reverse()
    tally = collections.Counter(); where = collections.defaultdict(list)
    lines = collections.OrderedDict()
    for bi, sep, lab in seq:
        sg = S[bi]; key = (sg['page'], sg['line'])
        lines.setdefault(key, '')
        lines[key] += sep + lab
        m = re.fullmatch(r'<(.+)[:=](.*)>', lab)
        if m: tally[(m.group(1), m.group(2) or '-')] += 1; where[(m.group(1), m.group(2) or '-')].append('%s.%d.%d' % (sg['page'], sg['line'], sg['pos']))
    for (p, l), txt in lines.items(): print(p, l, txt)
    print('\nsubstitutions (sign:value count places):')
    for (s, v), n in tally.most_common(): print(f'{s}:{v}\t{n}\t' + ' '.join(where[(s, v)]))

main()
