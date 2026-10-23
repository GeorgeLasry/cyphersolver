"""b24 (bergamo1585): decode R16 (DECODE transcription D1610) with the full Ragazzoni key as printed by Meister (1906)
p. 324-325 no. 2 (the DECODE record's own attachment D3195, never read before), by beam search over the token stream
with the it-cinquecento letter model (no spaces).

Fixes over decode_with_key.py: a lone 8 is a null only when it does not start a code (8 4+ = 84+ denari, 8 6¸ = 86ꜧ
come, 8 0- = 80- mente ...); a dot on the first digit makes a dotted x4 code (3^. 4 = 34̇ heretici); the full mark
families of p. 325 (x4+, x4 stroked, x6 hooked, x8+, x0 struck, x4 dotted) and the plain names (12-98, 10-90).

    python b24_bg_decode.py [transcription] > out.txt       (default: targets/bergamo1585/R16_transcription_decode.txt)
"""
import re, sys, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from lang import lm
M = lm.load('it-cinquecento', spaces=False)
K = M.order

LET = {'01': 'a', '41': 'a', '11': 'b', '21': 'c', '31': 'd', '03': 'e', '43': 'e', '13': 'f', '23': 'g', '33': 'h',
       '05': 'i', '45': 'i', '15': 'l', '25': 'm', '35': 'n', '07': 'o', '67': 'o', '17': 'p', '27': 'q', '37': 'r',
       '47': 's', '57': 't', '09': 'u', '39': 'u', '19': 'z', '29': 'et'}
NAMES = {'14': 'Nostro Signore', '24': 'Imperatore', '34': 'Re Christianissimo', '44': 'Re Catholico', '54': 'Re di Portugallo',
         '64': 'Re di Polonia', '74': 'Regina Madre', '84': 'Regina regnante', '94': 'Regina Catholica', '12': 'Monsignor di Alanson',
         '22': 'Cardinale di Borbone', '32': 'Cardinale di Lorena', '42': 'Cardinale di Armignach', '52': 'Cardinale Rambuglietto',
         '62': 'Cardinale di Sans', '72': 'Cardinale di Guisa', '82': 'Cardinale di Rens', '92': 'Cardinale Birago',
         '16': 'Regina di Scotia', '26': "Regina d'Inghilterra", '36': 'Regina di Navarra', '46': 'Re di Navarra', '56': 'Principe di Conde',
         '66': 'Gran Turco', '76': 'Signori Venetiani', '86': 'Signori Svizzeri', '96': 'Granduca di Toscana', '18': 'Duca di Ferrara',
         '28': "Duca d'Urbino", '38': 'Duca di Mantova', '48': 'Duca di Parma', '58': 'Duca di Guisa', '68': "Don Giovanni d'Austria",
         '78': 'Italia', '88': 'Francia', '98': 'Spagna', '10': 'Germania', '20': 'Fiandra', '30': 'Inghilterra', '40': 'Scotia',
         '50': 'Ibernia', '60': 'Monsignor di', '70': 'Ambasciatore di', '80': 'Nuntio di', '90': 'Principe di'}
MARK = {'+4': ['Cardinale', 'Principi di', 'Marchese di', 'Conte di', 'Baron di', 'Cavalli', 'Fanti', 'denari', 'Galere'],
        '+2': ['Sua Santita', 'Sua Maesta', 'Sua Altezza', 'Sua Signoria illustrissima', 'Sua Signoria', 'Vostra Signoria illustrissima',
               'Vostra Signoria reverendissima', 'Vostra Signoria', "Stato d'Avignone"],       # DECODE '2+' = the stroked 4 (ꝝ)
        '¸6': ['Avignone', 'che', 'per', 'perche', 'ancora', 'accioche', 'quando', 'come', 'tanto'],
        '+8': ['quanti', 'questi', 'quelli', 'qua', 'que', 'qui', 'havere', 'havendo', 'essere'],
        '-0': ['essendo', 'non', 'lettere', 'corriero', 'risposta', 'risolutione', 'lega', 'mente', 'pace'],
        '.4': ['Religione Cattolica', 'Catolici', 'Heretici', 'Guerra', 'Lega', 'Suspensione']}
WORDISH = set(w for v in MARK.values() for w in v if w.islower())


def marked(d1, tok):
    """d1 plain digit + marked token -> word or None."""
    d2, mk = tok[0], tok[1:].replace('?', '')
    fam = {'+': '+', '¸': '¸', '-': '-', '^.': '.'}.get(mk)
    if not fam or not d1.isdigit(): return None
    lst = MARK.get(fam + d2)
    i = int(d1) - 1
    if lst and 0 <= i < len(lst): return lst[i]
    return None


def tokens(path):
    out = []
    global LINEOF; LINEOF = []
    ln = 0
    for l in open(path, encoding='utf8', errors='replace'):
        if l.startswith('#'): continue
        ln += 1
        l = l.replace('<CLEARTEXT', ' <CLEARTEXT')
        for m in re.finditer(r'<CLEARTEXT[^>]*>|<SIGNATURE>|\S+', l):
            t = m.group(0)
            LINEOF.append(ln)
            if t.startswith('<'): out.append(('C', t)); continue
            out.append(('T', t))
    return out


def step(ctx, text):
    """log-prob of text after context string ctx (letters only)."""
    s = 0.0; c = ctx
    for ch in lm.norm(text, 'early', spaces=False):
        if ch not in M.index: continue
        x = M.encode((c + ch)[-K:])
        if len(x) == K: s += M.score_idx(x)
        c = (c + ch)[-(K - 1):]
    return s, c


def decode(path, beam=300):
    toks = tokens(path)
    global TOKS; TOKS = toks
    beams = {(0, ''): (0.0, [])}
    n = len(toks)
    final = []
    while beams:
        nb = {}
        def push(i, ctx, sc, out):
            key = (i, ctx[-(K - 1):])
            if key not in nb or nb[key][0] < sc: nb[key] = (sc, out)
        for (i, ctx), (sc, out) in beams.items():
            if i >= n: final.append((sc, out)); continue
            kind, t = toks[i]
            if kind == 'C':
                push(i + 1, ctx, sc, out + [('clear', t)]); continue
            plain = lambda x: re.fullmatch(r'\d\??', x) is not None
            dig = lambda x: x[0]
            nxt = toks[i + 1][1] if i + 1 < n and toks[i + 1][0] == 'T' else None
            if t == '.':
                push(i + 1, ctx, sc - 1, out); continue
            # null 8
            if t == '8':
                push(i + 1, ctx, sc - 0.5, out + [('sep', '')])
            # con
            if t.startswith('0^.') :
                d, c2 = step(ctx, 'con'); push(i + 1, c2, sc + d, out + [('w', 'con', t)])
            if plain(t) and nxt is not None:
                code = dig(t) + (dig(nxt) if plain(nxt) else '')
                unc = ('?' in t) or ('?' in nxt)
                pen = -1.5 if unc else 0
                if plain(nxt):
                    if code in LET:
                        for v in (['che', 'et'] if code == '29' else [LET[code]]):
                            d, c2 = step(ctx, v); push(i + 2, c2, sc + d + pen, out + [('l', v, t + ' ' + nxt)])
                    if code in NAMES:
                        push(i + 2, '', sc - 14 + pen, out + [('n', NAMES[code], t + ' ' + nxt)])
                else:
                    w = marked(dig(t), nxt)
                    if w:
                        if w in WORDISH:
                            d, c2 = step(ctx, w); push(i + 2, c2, sc + d + pen, out + [('w', w, t + ' ' + nxt)])
                        else:
                            push(i + 2, '', sc - 14 + pen, out + [('n', w, t + ' ' + nxt)])
            # dot on the first digit: 3^. 4 = 34 dotted
            if re.fullmatch(r'\d\^\.', t) and nxt and plain(nxt):
                w = marked(t[0], nxt[0] + '^.')
                if w: push(i + 2, '', sc - 14, out + [('n', w, t + ' ' + nxt)])
            # slips: drop a token, or an unreadable pair
            push(i + 1, ctx, sc - 12, out + [('drop', t)])
            if nxt is not None:
                push(i + 2, ctx, sc - 16, out + [('unk', '<%s %s>' % (t, nxt))])
        beams = dict(sorted(nb.items(), key=lambda kv: -kv[1][0])[:beam])
    final.sort(key=lambda x: -x[0])
    return final[0]


if __name__ == '__main__':
    path = sys.argv[1] if len(sys.argv) > 1 else str(ROOT / 'targets' / 'bergamo1585' / 'R16_transcription_decode.txt')
    sc, out = decode(path)
    words, cur, stats = [], '', {'drop': 0, 'unk': 0}
    for it in out:
        if it[0] in ('drop', 'unk'): stats[it[0]] += 1
        if it[0] == 'l': cur += it[1]
        elif it[0] == 'sep': words.append(cur); cur = ''
        elif it[0] in ('w', 'n'): words.append(cur); words.append('[%s]' % it[1] if it[0] == 'n' else it[1]); cur = ''
        elif it[0] == 'clear': words.append(cur); words.append(it[1]); cur = ''
        elif it[0] == 'unk': cur += '‹?›'
        elif it[0] == 'drop': cur += '·'
    words.append(cur)
    print(' '.join(w for w in words if w))
    print('\n# score %.1f, dropped tokens %d, unreadable pairs %d' % (sc, stats['drop'], stats['unk']))
    print('# trace:')
    for it in out: print('#  ', it)

    # per transcription line: the decode of that line's tokens
    if len(sys.argv) > 2 and sys.argv[2] == 'lines':
        pos, perline = 0, {}
        for it in out:
            n = {'l': 2, 'n': 2, 'w': 2 if ' ' in (it[2] if len(it) > 2 else '') else 1, 'sep': 1, 'drop': 1, 'unk': 2, 'clear': 1}[it[0]]
            ln = LINEOF[pos]
            txt = {'l': it[1], 'n': '[%s]' % it[1] if it[0] == 'n' else it[1], 'w': ' %s ' % it[1], 'sep': ' ', 'drop': '·', 'unk': '‹?›', 'clear': ''}[it[0]]
            if it[0] == 'n': txt = ' [%s] ' % it[1]
            perline[ln] = perline.get(ln, '') + txt
            pos += n
        for ln in sorted(perline): print('L%02d' % ln, ' '.join(perline[ln].split()))
