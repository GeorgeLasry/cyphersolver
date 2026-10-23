"""Re-read brief, batch b00 (morosini1588): word-level decoder with a transcription-slip model.

The published decode (targets/morosini1588/decrypt.py) segments the run-on figures with a character model only, so a
single misread figure (an 8 lost, 1 for 7, a doubled digit) turns into a garbled word. This decoder segments into
*words*: a trie of the period vocabulary (Nuntiaturberichte + Guicciardini/Machiavelli word counts, with the
cipher clerk's single-for-double spellings as variants), a word bigram model, Meister no. 40's homophones, the 8x
nulls, and a small slip model (one figure substituted, dropped or added, at a cost; cheaper where DECODE's transcriber
wrote '?'). Words outside the vocabulary are allowed letter by letter under the character model, at a cost.
Every slip it assumes is printed, so it can be checked on the image.

    python reread_b00_decode.py R43 [--page 308r] [--beam 150] [--out FILE] [--trans FILE]

Output per transcription line: the line's figures, then the words that start on it; '{...}' marks an assumed slip
(e.g. {+8} an added null figure, {7>1} a figure read 1 for 7, {-3} a figure dropped), '<...>' a word spelled outside
the vocabulary.
"""
import argparse, collections, gzip, json, math, os, pickle, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
sys.path.insert(0, ROOT)
from lang import lm  # noqa: E402

TDIR = os.path.join(ROOT, 'targets', 'morosini1588')
sys.path.insert(0, TDIR)
import importlib.util  # noqa: E402
_spec = importlib.util.spec_from_file_location('mdec', os.path.join(TDIR, 'decrypt.py'))

LET = {
    'a': '21 212 2', 'b': '24 42', 'c': '25 52', 'd': '26 62', 'e': '35 153 5', 'f': '30 03',
    'g': '40 04', 'h': '41 14', 'i': '17 171 7', 'k': '60 06', 'l': '50 05', 'm': '20 02',
    'n': '10 01 0', 'o': '91 191 9', 'p': '70 07', 'qu': '90 09', 'r': '00 13 1', 's': '54 45 4',
    't': '51 15 6', 'u': '37 173 3', 'x': '11', 'z': '12', 'et': '16 69 75', 'con': '19 76 55',
    'cr': '22', 'fr': '23', 'gr': '59', 'lt': '27', 'mp': '29', 'nt': '31', 'ntr': '32', 'pr': '33',
    'scr': '36', 'sc': '34', 'sf': '57', 'sfr': '39', 'sgr': '43', 'sp': '44', 'spr': '46',
    'st': '47', 'str': '49', 'non': '61 71', 'che': '56', 'chi': '63', 'per': '64', 'perche': '65',
    'percioche': '66', 'accio': '67', 'acchioche': '72', 'nondimeno': '77', 'come': '79',
    'ancora': '92', 'ancorche': '93', 'benche': '94', 'qua': '95', 'que': '96', 'qui': '97',
    'quando': '99',
}
ALT = {'42': ('sg', -2.0), '49': ('tr', -2.0)}
CODES = collections.defaultdict(list)
for pt, cs in LET.items():
    for c in cs.split():
        CODES[c].append((pt, 0.0))
for c, (pt, pen) in ALT.items():
    CODES[c].append((pt, pen))
CODES = dict(CODES)
# codes with one figure missing: '2 1 x' -> full code
MISSING = collections.defaultdict(list)
for c, lst in CODES.items():
    for i in range(len(c)):
        short = c[:i] + c[i + 1:]
        if short:
            for pt, pen in lst:
                MISSING[short].append((c, pt, pen))
NOM = {
    '111': 'il papa', '113': 'sua maesta', '114': 're di spagna', '112': "l'imperatore",
    '115': 're di polonia', '116': 'regina madre', '117': 'regina regnante', '119': "regina d'inghilterra",
    '121': 'signoria di genova', '122': 'signori venetiani', '123': 're di dania', '124': 're di suetia',
    '125': 'gran turco', '126': 'gran duca di toscana', '127': 'arciduca di', '129': 'duca di',
    '131': 'cardinale di', '132': 'principe di', '133': 'arciuescouo', '134': 'arciuescouado',
    '135': 'uescouo', '136': 'uescouado', '137': 'abbatia', '139': 'priorato', '141': 'clero',
    '142': 'presidente', '143': 'guerra', '144': 'pace', '145': 'triegua', '146': 'danari',
    '147': 'italia', '149': 'italiani', '151': 'francia', '152': 'franzesi', '154': 'spagna',
    '155': 'spagnioli', '156': 'alemagna', '157': 'alemani', '159': 'fiandra', '161': 'quanto',
    '163': 'quantunque', '164': 'qualmente', '165': 'quello', '166': 'questo', '167': 'u.s. ill.ma',
    '169': 'u.s.', '172': 'fiamenghi', '173': 'inghilterra', '174': 'inglesi', '175': 'polonia',
    '176': 'polacchi', '177': 'turco', '179': 'ungaria', '192': 'bascia', '193': 'austria',
    '194': 'austriaci', '195': 'auignone', '196': 'sauoia', '197': 'geneura', '199': 'genoua',
    '211': 'genouesi', '213': 'ambassadore', '214': 'agente', '215': 'secretario', '216': 'auisi',
    '217': 'corriere', '219': 'cifra', '221': 'lettere', '222': 'santo officio', '223': 'inquisitione',
    '224': 'padri del iesu', '225': 'padri capuccini', '226': 'catolici', '227': 'heretici',
    '229': 'ugonotti', '231': 'principe di conde', '232': 'il gia re di nauarra',
}
# figures a transcriber confuses in this hand (DECODE transcriber notes: 8s hard to see, 1/2 and 1/7)
CONF = {'1': '72', '7': '19', '2': '1', '0': '86', '8': '03', '3': '5', '5': '3', '6': '0', '9': '7', '4': ''}
SUB, SUB_UNC, DEL, INS, NULL2, NULL1 = -5.0, -1.5, -6.0, -5.5, -2.5, -3.0
OOV_CHAR, OOV_WORD = -1.2, -6.0
VAR_PEN = -0.4          # single-for-double spelling variant

NAMES = '''guisa ghisa guisi umena umeno nemurs nemours elbeuf gionuilla gionuille lione bles blois parigi borbone
uandomo uandomo nauarra eperno epernone espernone alfonso corso ornano soissons nivers niuers neuers mandelot
gondi montalto morosini saluzzo carmagnola poigni poigny pisani lenoncourt lenoncort giojosa gioiosa ioiosa
mercurio mercoeur aumont angiers amboise tours molins moulins orleans cambrai bressa delfinato marsiglia
rucellai orazio horatio fiorenza lorena sorbona mena maine buglione sciatiglione ciatiglione monpensier
montmorency momoransi momoransi birone biron retz rets villeroi brulart pinart bellieure cheuerni cheuerny
lansac lanzac antraghes entragues dumena sassonia casimiro suizzeri suizzeri lanzichenech lanzi reitri reistri
schombergh sciomberg rambugliet rambouillet larcheuesco'''.split()


def norm(s):
    return lm.norm(s, 'early', False)


def build_lex_model(lang):
    """Unigram vocabulary from lang/lexicons/<lang>.json.gz (no bigrams), e.g. 'es' for R35 (a Spanish copy)."""
    d = json.load(gzip.open(os.path.join(ROOT, 'lang', 'lexicons', f'{lang}.json.gz')))
    vocab = {}
    for w, c in d.items():
        w2 = norm(w)
        if not w2 or (len(w2) <= 2 and c < 2000) or (len(w2) == 3 and c < 40) or c < 5:
            continue
        vocab[w2] = vocab.get(w2, 0) + c
    for w in NAMES:
        vocab[norm(w)] = max(vocab.get(norm(w), 0), 300)
    return dict(vocab=vocab, bi={}, N=sum(vocab.values()))


def build_model(cache=os.path.join(HERE, 'llm', '_b00_wordmodel.pkl')):
    if os.path.exists(cache):
        return pickle.load(open(cache, 'rb'))
    os.makedirs(os.path.dirname(cache), exist_ok=True)
    corp = []
    for root in (os.path.join(ROOT, 'lang', 'corpora'), r'C:\Users\dbour\cypher\lang\corpora'):
        for f in ('it-nunziature.txt', 'it-renaissance.txt'):
            p = os.path.join(root, f)
            if os.path.exists(p) and f not in [os.path.basename(x) for x in corp]:
                corp.append(p)
    uni, bi = collections.Counter(), collections.Counter()
    for p in corp:
        txt = open(p, encoding='utf-8', errors='replace').read()
        words = re.findall(r"[a-z]+", lm.norm(txt, 'early', True).replace("'", ' '))
        uni.update(words)
        bi.update(zip(words, words[1:]))
    SHORT = set('a e i o d di da de del dal la le li lo il in un una et se si ne ni no non ha ho hа al ai co con per'
                '  me mi te ti ui uo su re fu fa fo ma ad ed da ce ci'.split())
    def keep(w, c):
        if len(w) <= 2:
            return w in SHORT
        if len(w) == 3:
            return c >= 40
        return c >= 4 and len(w) <= 18
    vocab = {w: c for w, c in uni.items() if keep(w, c)}
    for w in NAMES:
        vocab[norm(w)] = max(vocab.get(norm(w), 0), 300)
    for pt in list(LET) + [w for v in NOM.values() for w in re.findall('[a-z]+', v)]:
        if pt.isalpha() and len(pt) > 1:
            vocab.setdefault(pt, 5)
    bi = {k: v for k, v in bi.items() if v >= 2 and k[0] in vocab and k[1] in vocab}
    model = dict(vocab=vocab, bi=bi, N=sum(vocab.values()))
    pickle.dump(model, open(cache, 'wb'))
    return model


class Trie:
    def __init__(self, model):
        self.kids = [dict()]
        self.word = [None]
        words = sorted(model['vocab'])
        self.wid = {w: i for i, w in enumerate(words)}
        self.words = words
        cnt = model['vocab']
        N = model['N']
        self.uni = [math.log((cnt[w] + 0.5) / N) for w in words]
        self.cnt = cnt
        self.bi = model['bi']
        self.ctx_tot = collections.Counter()
        for (a, b), c in self.bi.items():
            self.ctx_tot[a] += c
        for w in words:
            self.add(w, w, 0.0)
            dg = re.sub(r'(.)\1', r'\1', w)
            if dg != w:
                self.add(dg, w, VAR_PEN)

    def add(self, spelled, w, pen):
        n = 0
        for ch in spelled:
            nxt = self.kids[n].get(ch)
            if nxt is None:
                nxt = len(self.kids)
                self.kids.append(dict())
                self.word.append(None)
                self.kids[n][ch] = nxt
            n = nxt
        old = self.word[n]
        wid = self.wid[w]
        if old is None:
            self.word[n] = [(wid, pen)]
        elif wid not in [x[0] for x in old]:
            old.append((wid, pen))

    def walk(self, n, s):
        for ch in s:
            n = self.kids[n].get(ch)
            if n is None:
                return None
        return n

    def logp(self, wid, prev):
        w = self.words[wid]
        u = self.uni[wid]
        if prev is not None and prev >= 0:
            pw = self.words[prev]
            tot = self.ctx_tot.get(pw, 0)
            if tot:
                c = self.bi.get((pw, w), 0)
                return math.log(0.55 * c / tot + 0.45 * math.exp(u))
        return u


def parse(path, page=None):
    """Items: dicts with kind 'd' (figure) or 'N' (dotted code), val, line (1-based within page), page, unc."""
    pages, cur, items, lineno = [], None, [], 0
    for raw in open(path, encoding='utf-8', errors='replace'):
        raw = raw.rstrip('\n')
        m = re.match(r'#\s*(?:IMAGE NAME:)?\s*(\d+[rRvV])(?:\.jpg)?(?![-\w])(.*)', raw)
        if raw.startswith('#') and re.search(r'\d[rRvV](\.jpg)?\s*-\s*\d', raw):
            continue
        if m:
            if items or cur:
                pages.append((cur, items))
            cur, items, lineno = m.group(1), [], 0
            raw = m.group(2)
            if not raw.strip():
                continue
        elif raw.startswith('#'):
            continue
        lineno += 1
        line = re.sub(r'<[^>]*>', ' ', raw)
        toks = line.split()
        i = 0
        while i < len(toks):
            t = toks[i]
            if '^.' in t and i + 1 < len(toks):
                prev = items.pop()['val'] if items and items[-1]['kind'] == 'd' else '?'
                d = re.sub(r'\D', '', t)
                nxt = re.sub(r'\D', '', toks[i + 1])
                items.append(dict(kind='N', val=prev + d + nxt[:1], line=lineno, unc=False))
                for ch in nxt[1:]:
                    items.append(dict(kind='d', val=ch, line=lineno, unc=False))
                i += 2
                continue
            for k, ch in enumerate(t):
                if ch.isdigit():
                    items.append(dict(kind='d', val=ch, line=lineno, unc=False))
                elif ch == '?' and items:
                    items[-1]['unc'] = True
            i += 1
    if items or cur:
        pages.append((cur, items))
    if page:
        pages = [p for p in pages if p[0] and p[0].startswith(page)]
    return pages


CM = None


def charlm():
    global CM
    if CM is None:
        m = lm.load('it-cinquecento', spaces=False)
        CM = (m.lp.reshape(-1, m.A), m.A, m.order, m.index)
    return CM


def decode(items, trie, beam=150):
    LP, A, K, IDX = charlm()
    MOD = A ** (K - 1)
    n = len(items)
    ROOTN = 0
    # state key: (node, prev, oovctx) ; node>=0 trie node ; node==-1 OOV word in progress with oov ctx and letters
    states = [dict() for _ in range(n + 1)]
    states[0][(ROOTN, -1, None)] = (0.0, None)

    def push(q, key, sc, back):
        old = states[q].get(key)
        if old is None or sc > old[0]:
            states[q][key] = (sc, back)

    def close(p):
        """word ends at position p: add root states."""
        for key, (sc, back) in list(states[p].items()):
            node, prev, oc = key
            if node > 0 and trie.word[node]:
                for wid, pen in trie.word[node]:
                    push(p, (ROOTN, wid, None), sc + trie.logp(wid, prev if prev >= 0 else None) + pen,
                         (p, key, ('W', wid, pen != 0)))
            if node == -1:
                letters = oc[1]
                push(p, (ROOTN, -2, None), sc + OOV_WORD, (p, key, ('O', letters)))

    def advance(key, sc, p, q, pieces, tag):
        node, prev, oc = key
        for pt, pen in pieces:
            if node >= 0:
                nn = trie.walk(node, pt)
                if nn is not None:
                    push(q, (nn, prev, None), sc + pen, (p, key, ('P', pt, tag)))
            if node == ROOTN or node == -1:
                # OOV path: start or continue an out-of-vocabulary word
                if node == ROOTN:
                    ctx, letters = 0, ''
                    for x in [IDX[c] for c in 'ente']:
                        ctx = (ctx * A + x) % MOD
                else:
                    ctx, letters = oc
                s = 0.0
                for c in pt:
                    x = IDX.get(c)
                    if x is None:
                        continue
                    s += float(LP[ctx, x]) + OOV_CHAR
                    ctx = (ctx * A + x) % MOD
                if len(letters) + len(pt) <= 14:
                    push(q, (-1, prev, (ctx, letters + pt)), sc + pen + s, (p, key, ('P', pt, tag)))

    for p in range(n):
        close(p)
        if not states[p]:
            continue
        best = sorted(states[p].items(), key=lambda kv: -kv[1][0])[:beam]
        it = items[p]
        for key, (sc, _) in best:
            node, prev, oc = key
            if it['kind'] == 'N':
                if node == ROOTN:
                    phrase = NOM.get(it['val'])
                    txt = phrase if phrase else f"<{it['val']}?>"
                    push(p + 1, (ROOTN, -3, None), sc + (-1.0 if phrase else -8.0), (p, key, ('N', txt)))
                push(p + 1, key, sc + DEL * 5, (p, key, ('D', it['val'] + '.')))
                continue
            # normal codes, lengths 1-3
            for L in (1, 2, 3):
                seg = items[p:p + L]
                if len(seg) < L or any(x['kind'] != 'd' for x in seg):
                    break
                code = ''.join(x['val'] for x in seg)
                if code in CODES:
                    advance(key, sc, p, p + L, CODES[code], code)
                # one substituted figure
                for j in range(L):
                    d = code[j]
                    alts = CONF.get(d, '')
                    cost = SUB_UNC if seg[j]['unc'] else SUB
                    if seg[j]['unc']:
                        alts = '0123456789'.replace(d, '')
                    for a in alts:
                        c2 = code[:j] + a + code[j + 1:]
                        if c2 in CODES:
                            advance(key, sc + cost, p, p + L, CODES[c2], f'{code}[{d}>{a}]')
                if L == 2 and code[0] == '8':
                    push(p + 2, key, sc + NULL2, (p, key, ('Z', code)))
                # a figure missing in the transcription
                if code in MISSING and L <= 2:
                    for full, pt, pen in MISSING[code]:
                        advance(key, sc + INS + pen, p, p + L, [(pt, 0.0)], f'{code}[+>{full}]')
            if it['val'] == '8':
                push(p + 1, key, sc + NULL1, (p, key, ('Z', '8')))
            # a spurious figure in the transcription
            push(p + 1, key, sc + DEL, (p, key, ('D', it['val'])))
        states[p] = {k: v for k, v in best}  # keep only beam for backtrace memory
    close(n)
    fin = [(v[0], k) for k, v in states[n].items() if k[0] == ROOTN]
    if not fin:
        fin = [(v[0], k) for k, v in states[n].items()]
    sc, key = max(fin)
    # backtrace
    ops, q = [], n
    while True:
        sc_, back = states[q][key]
        if back is None:
            break
        p, pkey, op = back
        ops.append((p, q, op))
        q, key = p, pkey
    ops.reverse()
    return ops, sc


def render(ops, items, trie):
    """Group ops into tokens: (start_item, end_item, text, flags)."""
    toks, cur, start, flags = [], [], None, []
    for p, q, op in ops:
        kind = op[0]
        if kind == 'P':
            if start is None:
                start = p
            cur.append(op[1])
            if '[' in op[2]:
                flags.append(op[2])
        elif kind == 'Z':
            if op[1] == '8' or True:
                pass
        elif kind == 'D':
            flags.append(f'-{op[1]}')
            if start is None:
                start = p
        elif kind == 'W':
            w = trie.words[op[1]]
            spelled = ''.join(cur)
            toks.append((start if start is not None else p, q, spelled if spelled else w, w, flags))
            cur, start, flags = [], None, []
        elif kind == 'O':
            toks.append((start if start is not None else p, q, '<' + op[1] + '>', None, flags))
            cur, start, flags = [], None, []
        elif kind == 'N':
            toks.append((p, q, '[' + op[1].upper() + ']', None, []))
    return toks


def show(pagename, items, toks, out):
    byline = collections.defaultdict(list)
    for s, e, txt, w, fl in toks:
        ln = items[min(s, len(items) - 1)]['line'] if items else 0
        t = txt + ('{' + ','.join(fl) + '}' if fl else '')
        byline[ln].append(t)
    figs = collections.defaultdict(list)
    for it in items:
        figs[it['line']].append(it['val'] + ('?' if it['unc'] else '') if it['kind'] == 'd' else it['val'] + '.')
    print(f'[IMG {pagename}]', file=out)
    for ln in sorted(set(figs) | set(byline)):
        print(f'  {ln:2d}| ' + ' '.join(byline.get(ln, [])), file=out)
    print(file=out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('rec')
    ap.add_argument('--page')
    ap.add_argument('--beam', type=int, default=150)
    ap.add_argument('--out')
    ap.add_argument('--trans', help='transcription file (default: the DECODE D16xx/D17xx one)')
    ap.add_argument('--figs', action='store_true', help='also print each word with its figures')
    ap.add_argument('--lex', help="use lang/lexicons/<lex>.json.gz unigrams instead (e.g. es for R35)")
    a = ap.parse_args()
    import glob
    if a.trans:
        path = a.trans
    else:
        c = [f for f in glob.glob(os.path.join(TDIR, 'decode', f'DOC_{a.rec}_D1[67]*.txt'))]
        path = c[0] if c else os.path.join(TDIR, f'{a.rec}_transcription_decode.txt')
    trie = Trie(build_lex_model(a.lex) if a.lex else build_model())
    out = open(a.out, 'w', encoding='utf-8') if a.out else sys.stdout
    for pagename, items in parse(path, a.page):
        if not items:
            continue
        ops, sc = decode(items, trie, a.beam)
        toks = render(ops, items, trie)
        show(pagename, items, toks, out)
        if a.figs:
            for s, e, txt, w, fl in toks:
                figs = ' '.join(x['val'] + ('.' if x['kind'] == 'N' else '') for x in items[s:e])
                print(f'    {items[s]["line"]:2d} {txt:20s} {figs}  {",".join(fl)}', file=out)
        out.flush()


if __name__ == '__main__':
    main()
