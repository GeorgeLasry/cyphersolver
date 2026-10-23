"""Re-reading decoder for Barb.lat. 6960 (reread batch b01, 22 Oct 2026).

Differences from key6956/apply.py:
  * the digits 1 and 8 are never part of a code group (no group in the 6956 key contains them), so they only
    separate; apply.py let unknown three-digit groups such as [983] swallow them;
  * the segmentation of each 1/8-delimited run into 2- and 3-digit groups is chosen by an Italian 5-gram letter
    model (Viterbi with the model context as state), not by fixed weights;
  * uncertain digits in DECODE's transcription ('5/8?', '2?', '?') are kept as alternatives and the model picks;
  * clear text (<CLEARTEXT ...>) and decipherments on the page (<PLAINTEXT ...>) are kept in document order;
  * extra groups learnt in this batch (EXTRA below, each with the evidence in the reread log) are added to the key;
  * 44 = f, 45 = h (Bosbach; Biermann's x does not fit), 92 = st.

Output: for each document, a list of segments ('clear'|'plain'|'cipher', text). Cipher text shows nulls as '|',
key words in {braces}, unknown groups as [nnn].

    python reread_b01_decode.py R292 [R293 ...]       print the decode
    python reread_b01_decode.py --all                 write reread_b01/R*_dec.txt
"""
import itertools, json, math, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, ROOT)
from lang import lm  # noqa

KEY2 = {
    '00': 'a', '02': 'a', '20': 'a', '24': 'b', '34': 'b', '32': 'c', '42': 'c', '33': 'd', '09': 'e', '30': 'e',
    '90': 'e', '44': 'f', '99': 'g', '45': 'h', '55': 'h', '05': 'i', '40': 'i', '50': 'i', '66': 'l', '77': 'm',
    '29': 'n', '39': 'n', '03': 'o', '07': 'o', '70': 'o', '22': 'p', '27': 'qu', '36': 'r', '46': 'r', '23': 's',
    '43': 's', '25': 't', '35': 't', '04': 'u', '06': 'u', '60': 'u', '26': 'z', '37': 'gli', '47': 'che',
    '49': 'chi', '52': 'con', '53': 'non', '54': 'dal', '56': 'del', '57': 'per', '59': 'nel', '62': 'ma',
    '63': 'mi', '64': 'se', '65': 'si', '67': 'da', '69': 'di', '72': 'al', '73': 'la', '74': 'le', '75': 'lo',
    '76': 'il', '79': 'et', '92': 'st', '93': 'to', '94': 'io', '95': 'ne', '96': 'no', '97': 'in',
}
KEY3 = {
    '200': 'Commissario Imperiale', '202': 'consiglio', '232': 'Ambasciatore di Spagna', '293': 'Conte',
    '299': 'commissario', '340': 'Casale', '354': 'duca', '360': 'Duca di Mantova', '369': 'Duca di Nivers',
    '376': 'diligenza', '422': 'Francia', '436': 'Germania', '437': 'guerra', '447': 'lettera', '460': 'Imperatore',
    '470': 'impresa', '474': 'Italia', '502': 'Marchese', '504': 'Mantova', '520': 'munitione', '522': 'Monsignore',
    '534': 'Moravia', '545': 'negotiatione', '549': 'nuntio', '567': 'ordinatione', '569': 'ordine',
    '577': 'principe', '606': 'Praga', '623': 'possesso', '633': 'provincia', '635': 'Re', '643': "Re d'Ungheria",
    '670': 'Sua Maestà', '672': 'Sua Maestà Cesarea', '675': 'Sua Altezza', '692': 'Signor', '696': 'Savoia',
    '732': 'anche', '733': 'ancora', '737': 'come', '740': 'essere', '747': 'havere', '749': 'havendo',
    '753': 'molto', '755': 'mente', '763': 'però', '766': 'perché', '767': 'quale', '769': 'qualche',
    '772': 'quando', '773': 'quanto', '774': 'quello', '775': 'questo', '776': 'quanto', '793': 'Signor Ghibellino',
    '923': 'Stato Cattolico', '925': 'Spagna', '926': 'Spagnolo', '999': 'V.S. Ill.ma',
}
EXTRA_FILE = os.path.join(HERE, 'reread_b01', 'extra_groups.json')
EXTRA = json.load(open(EXTRA_FILE, encoding='utf-8')) if os.path.exists(EXTRA_FILE) else {}
for c, v in EXTRA.items():
    (KEY2 if len(c) == 2 else KEY3)[c] = v['value'] if isinstance(v, dict) else v

_LM = None
def LM():
    global _LM
    if _LM is None:
        cache = os.path.join(ROOT, 'lang', 'cache', 'pallotto1629_it_lm5')  # git-ignored
        if os.path.exists(cache + '.npy'):
            import numpy as np
            meta = json.load(open(cache + '.json'))
            _LM = lm.DenseLM(np.load(cache + '.npy'), meta['order'], meta['alpha'], meta)
        else:
            txt = ''
            for f in ('it-renaissance.txt', 'it-gutenberg.txt'):
                for d in (os.path.join(ROOT, 'lang', 'corpora'), os.path.join(ROOT, '..', '..', 'lang', 'corpora')):
                    p = os.path.join(d, f)
                    if os.path.exists(p):
                        txt += open(p, encoding='utf-8', errors='replace').read(); break
            t = lm.norm(txt, 'early', False)
            _LM = lm.DenseLM.build(t, 5, lm.alphabet('early', False), {'sources': 'it-renaissance+it-gutenberg'})
            os.makedirs(os.path.dirname(cache), exist_ok=True)
            _LM.save(cache)
    return _LM

def letters(v):
    return lm.norm(v, 'early', False)

# ------------------------------------------------------------------ parsing DECODE transcriptions

def parse(path):
    """Segments in order: ('clear', text) | ('plain', text) | ('cipher', [alts...]) where alts is a list of
    digit-option strings; a gap (illegible) is the option '#'."""
    segs = []
    cur = []
    def flush():
        if cur:
            segs.append(('cipher', cur[:])); cur.clear()
    for line in open(path, encoding='utf-8', errors='replace'):
        s = line.rstrip('\n')
        if s.startswith('#'):
            continue
        s = re.sub(r'#COMMENT.*$', '', s)
        pos = 0
        # tags may nest one level: <CLEARTEXT IT xx <IL> yy >
        for m in re.finditer(r'<(CLEARTEXT|PLAINTEXT)\s+\w+\s+((?:[^<>]|<[^<>]*>)*)>|<IL>|<[^<>]*>', s):
            pre = s[pos:m.start()]
            _digits(pre, cur)
            tag = m.group(0)
            if m.group(1):
                flush(); segs.append(('clear' if m.group(1) == 'CLEARTEXT' else 'plain', m.group(2).strip()))
            elif tag == '<IL>':
                cur.append('#')
            pos = m.end()
        _digits(s[pos:], cur)
    flush()
    return segs

P08 = -7.0   # DECODE's transcription often reads the null 8 of this hand as 0 (checked on the R286 scan)
P80 = -9.0

def _digits(s, out):
    """Append one option dict {digit: penalty} per written digit."""
    s = s.replace('^', ' ')
    for t in s.split():
        if set(t) <= set('?'):
            out.extend([{d: -4.0 for d in '0123456789'}] * len(t)); continue
        unsure = t.endswith('?')
        t = t.rstrip('?')
        if '/' in t:
            alts = [a.rstrip('?') for a in t.split('/')]
            if all(len(a) == 1 and a.isdigit() for a in alts):
                out.append({a: -0.7 for a in alts}); continue
            t = alts[0]
        ds = [ch for ch in t if ch.isdigit()]
        for i, ch in enumerate(ds):
            o = {ch: (-0.3 if unsure else 0.0)}
            if ch == '0': o['8'] = P08
            if ch == '8': o['0'] = P80
            out.append(o)

# ------------------------------------------------------------------ decoding

UNK = -13.0      # log-prob charged for an unknown three-digit group, eased for groups frequent in the corpus
FREQ_FILE = os.path.join(HERE, 'reread_b01', 'group_freq.json')
FREQ = json.load(open(FREQ_FILE)) if os.path.exists(FREQ_FILE) else {}
def unk_cost(c):
    return UNK + min(7.0, 1.5 * math.log(1 + FREQ.get(c, 0)))
SLIP = -14.0     # a digit that fits no code
NULL = 0.0
WORD = -9.0     # a known nomenclator word, scored as one unit

def decode_run(alts, ctx0=''):
    """Viterbi over one cipher segment. alts: list of option strings per position. Returns token list
    [(kind, code, text)] with kind in null|l|w|u|slip|gap and the end context."""
    m = LM(); A = m.A; idx = m.index; lp = m.lp; k = m.order
    n = len(alts)
    def score_letters(ctx, s):
        sc = 0.0
        c = ctx
        for ch in s:
            if ch not in idx: continue
            full = (c + ch)[-k:]
            if len(full) < k:
                c = c + ch; continue
            code = 0
            for x in full: code = code * A + idx[x]
            sc += float(lp[code]); c = full[1:]
        return sc, (ctx + s)[-(k - 1):]
    # states: dict ctx -> (score, backptr)
    states = [dict() for _ in range(n + 1)]
    states[0][ctx0[-(k - 1):]] = (0.0, None)
    for i in range(n):
        if not states[i]: continue
        for ctx, (sc, _) in list(states[i].items()):
            cands = []
            o = alts[i]
            if o == '#':
                cands.append((1, 'gap', '#', '', -6.0, ctx))
            else:
                for nd in '18':
                    if nd in o:
                        cands.append((1, 'null', nd, '', NULL + o[nd], ctx))
                for L in (2, 3):
                    if i + L > n or '#' in alts[i:i + L]: continue
                    opts = [[(d, p) for d, p in x.items() if d not in '18'] for x in alts[i:i + L]]
                    for combo in itertools.product(*opts):
                        c = ''.join(d for d, _ in combo); pen = sum(p for _, p in combo)
                        if L == 2 and c in KEY2:
                            cands.append((2, 'l', c, KEY2[c], pen, None))
                        elif L == 3 and c in KEY3:
                            cands.append((3, 'w', c, KEY3[c], pen - 1.0, None))
                        elif L == 3 and c[0] != '0':
                            cands.append((3, 'u', c, '', pen + unk_cost(c), ctx))
                best = max(o, key=o.get)
                cands.append((1, 'slip', best, '', SLIP, ctx))
            for L, kind, code, text, pen, newctx in cands:
                if kind == 'l':
                    s2, c2 = score_letters(ctx, letters(text))
                    tot = sc + s2 + pen
                elif kind == 'w':     # a whole key word: flat cost, context continues from its last letters
                    c2 = (ctx + letters(text))[-(k - 1):]
                    tot = sc + WORD + pen + 1.0
                else:
                    c2 = ctx if newctx is None else newctx
                    tot = sc + pen
                st = states[i + L]
                if c2 not in st or st[c2][0] < tot:
                    st[c2] = (tot, (i, ctx, kind, code, text))
        # prune
        for j in (i + 1, i + 2, i + 3):
            if j <= n and len(states[j]) > 60:
                states[j] = dict(sorted(states[j].items(), key=lambda kv: -kv[1][0])[:60])
    end = max(states[n].items(), key=lambda kv: kv[1][0])
    toks = []; j = n; ctx = end[0]
    while j > 0:
        sc, bp = states[j][ctx]
        i, pctx, kind, code, text = bp
        toks.append((kind, code, text)); j, ctx = i, pctx
    return list(reversed(toks)), end[0]

def render(toks):
    out = []
    for kind, code, text in toks:
        if kind == 'null': out.append('|')
        elif kind == 'l': out.append(text)
        elif kind == 'w': out.append('{' + text + '}')
        elif kind == 'u': out.append('[' + code + ']')
        elif kind == 'slip': out.append('?' + code)
        elif kind == 'gap': out.append('[…]')
    s = ''.join(out)
    s = re.sub(r'\|+', ' ', s)
    return re.sub(r'\s+', ' ', s).strip()

def decode_doc(rec):
    segs = parse(os.path.join(HERE, 'decode', rec + '.txt'))
    out = []
    for kind, val in segs:
        if kind == 'cipher':
            toks, _ = decode_run(val)
            out.append(('cipher', toks))
        else:
            out.append((kind, val))
    return out

def text_of(doc, codes=False):
    lines = []
    for kind, val in doc:
        if kind == 'cipher':
            lines.append('C: ' + render(val))
        elif kind == 'clear':
            lines.append('T: ' + val)
        else:
            lines.append('P: ' + val)
    return '\n'.join(lines)

if __name__ == '__main__':
    args = sys.argv[1:]
    if args == ['--all']:
        args = [f[:-4] for f in sorted(os.listdir(os.path.join(HERE, 'decode')))]
        os.makedirs(os.path.join(HERE, 'reread_b01'), exist_ok=True)
        for r in args:
            d = decode_doc(r)
            open(os.path.join(HERE, 'reread_b01', r + '_dec.txt'), 'w', encoding='utf-8').write(
                f'# {r}: reread_b01_decode.py (6956 key + reread_b01/extra_groups.json), LM-chosen segmentation.\n'
                '# C: cipher decode (spaces = nulls 1/8, {key word}, [nnn] unknown group, ?d slip)  '
                'T: clear text as transcribed by DECODE  P: on-page decipherment\n\n' + text_of(d) + '\n')
            print(r, 'done')
    else:
        for r in args:
            print('==', r); print(text_of(decode_doc(r)))
