"""Re-read brief, batch b00 (morosini1588): align a reading word by word with its figures.

REREAD_BRIEF step 3: every word of a reading must be carried by its figures; a word nothing carries must be bracketed.
This aligns the "## Reading" body of texts/<R>_reading.md, page by page (the [f. 308r] markers), with DECODE's
transcribed figures under Meister no. 40 and reports, per page, the unbracketed words the figures do not carry.

    python reread_b00_align.py R43 [--trans FILE] [--verbose]

Alignment (dynamic programming, banded): a plaintext unit (letter, cluster, word code) against its homophones
(cost 0), one figure changed (2), one figure missing (2.5) or doubled (2.5); null 8 / 8x (0.3/0.5); a figure left
over (3); a reading letter with no figure (3.5; free inside [supplied], 0.5 inside [?partly]); a dotted code against
1-4 reading words that can expand a nomenclator code (S. M.tà, il Re, duca di, quella ...; 0.2), or against letters
whose figures are its three digits (a spurious dot, 0.5); plain figures against digits written in the reading (0);
[…] absorbs figures (0.2 each). A word is reported SUPPLIED when most of its letters have no figure, PARTLY when
some do or when it needs two or more figure slips.
"""
import argparse, glob, os, re, sys, unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import reread_b00_decode as D  # noqa: E402

def nrm(s):
    s = unicodedata.normalize('NFD', s.lower())
    s = ''.join(c for c in s if unicodedata.category(c) != 'Mn')
    return s.replace('v', 'u').replace('j', 'i').replace('y', 'i')


UNITS = sorted(list(D.LET.items()) + [(pt, c) for c, (pt, pen) in D.ALT.items()], key=lambda kv: -len(kv[0]))
EXP = set('''il la le lo li i gli l s m ta tà re regina reina madre regnante sua suo sue suoi maesta maestà christianissima
christianissimo cristianissima christma n nostro signore signor sig papa santita santità beatitudine sa ss v vs ill illma
ma vostra signoria illustrissima ecc duca duchi di de del della dela d cardinale cardinali card principe principi
arciuescouo arcivescovo arciuescouado uescouo vescovo uescoui vescovi uescouado abbatia priorato clero presidente
guerra pace triegua tregua danari danaro denari italia italiani francia franzesi francesi spagna spagnoli spagnioli
alemagna alemani fiandra quanto quanta quanti quante quantunque qualmente quello quella quelli quelle quel questo
questa questi queste fiamenghi inghilterra inglesi polonia turco ungaria austria auignone avignone sauoia savoia
geneura ginevra genoua genova genouesi ambasciatore ambassadore ambasciatori agente secretario segretario auisi auiso
avisi avviso corriere cifra lettere lettera santo officio ufficio inquisitione padri del iesu gesu capuccini cappuccini
catolici cattolici catolica catolico catoliche cattolica cattolico heretici eretici heretico ugonotti guerre cifre corieri corrieri conde gia già nauarra navarra imperatore polacchi bascia basciá
gran granduca toscana dania suetia arciduca signori venetiani'''.split())
EXP = set(nrm(w) for w in EXP) | {'u', 'us', 'uostra', 'illma', 'ill', 'ss', 'ns', 'sm', 'mta', 'smta'}


def body(path):
    txt = open(path, encoding='utf-8').read()
    m = re.search(r'^## Reading\s*$(.*?)(^## |\Z)', txt, re.S | re.M)
    return m.group(1) if m else txt


def segments(text):
    """[(page, text)] split at [f. 308r] markers (same page twice -> joined)."""
    parts = re.split(r'\[f\.\s*(\d+[rv])\]', text)
    out = []
    if parts[0].strip():
        out.append((None, parts[0]))
    for k in range(1, len(parts), 2):
        out.append((parts[k], parts[k + 1]))
    return out


def tokenize(seg):
    """Words with their units. Unit: (kind, text, word_index); kinds: 'c' letter, 'd' digit, 'H' hole,
    with a mode 'n' normal / 's' supplied / 'p' partly."""
    words, units = [], []
    # tokens: [..] groups, words with internal [..] parts, digits
    for m in re.finditer(r"\[[^\]]*\]|[^\s\[\],.;:!?()«»“”\"'’]+(?:\[[^\]]*\][^\s\[\],.;:!?()«»“”\"'’]*)*", seg):
        tok = m.group(0)
        wi = len(words)
        if tok.startswith('[') and tok.endswith(']') and tok.count('[') == 1:
            inner = tok[1:-1].strip()
            if inner in ('…', '...', '') or inner.startswith('…'):
                words.append(dict(text=tok, kind='hole', start=len(units)))
                units.append(('H', '', wi, 'n'))
                words[-1]['end'] = len(units)
                continue
            if re.fullmatch(r'\d+(\s*=.*)?', inner):     # [716] unknown code, [250 = Bles?]
                words.append(dict(text=tok, kind='code', start=len(units)))
                units.append(('H', '', wi, 'n'))
                words[-1]['end'] = len(units)
                continue
            mode = 'p' if inner.startswith('?') else 's'
            inner = inner.lstrip('?')
            words.append(dict(text=tok, kind='partly' if mode == 'p' else 'supplied', start=len(units)))
            for sub in inner.split():
                for ch in nrm(sub):
                    if ch.isalpha():
                        units.append(('c', ch, wi, mode))
                    elif ch.isdigit():
                        units.append(('d', ch, wi, mode))
            words[-1]['end'] = len(units)
            continue
        words.append(dict(text=tok, kind='word', start=len(units)))
        mode = 'n'
        for piece in re.split(r'(\[[^\]]*\])', tok):
            if piece.startswith('['):
                pm = 'p' if piece[1:2] == '?' else 's'
                for ch in nrm(piece[1:-1].lstrip('?')):
                    if ch.isalpha():
                        units.append(('c', ch, wi, pm))
                continue
            for ch in nrm(piece):
                if ch.isalpha():
                    units.append(('c', ch, wi, mode))
                elif ch.isdigit():
                    units.append(('d', ch, wi, mode))
        words[-1]['end'] = len(units)
    return words, units


def page_items(rec, trans=None):
    if trans:
        path = trans
    else:
        c = glob.glob(os.path.join(D.TDIR, 'decode', f'DOC_{rec}_D1[67]*.txt'))
        path = c[0] if c else os.path.join(D.TDIR, f'{rec}_transcription_decode.txt')
    pages = {}
    for p, items in D.parse(path):
        if p:
            pages.setdefault(p.lstrip('0').lower(), []).extend(items)
    return pages


def align(F, U, words, band=260):
    n, m = len(F), len(U)
    INF = 1e18
    best = {}
    back = {}
    wstart = set(w['start'] for w in words)

    def get(i, j):
        return best.get((i, j), INF)

    def relax(i, j, i2, j2, c, info):
        if i2 > n or j2 > m:
            return
        v = best[(i, j)] + c
        if v < best.get((i2, j2), INF):
            best[(i2, j2)] = v
            back[(i2, j2)] = (i, j, info)

    def figs(i, L):
        if i + L > n:
            return None
        seg = F[i:i + L]
        if any(x['kind'] != 'd' for x in seg):
            return None
        return ''.join(x['val'] for x in seg)

    best[(0, 0)] = 0.0
    ratio = m / max(1, n)
    for i in range(n + 1):
        jc = int(i * ratio)
        for j in range(max(0, jc - band), min(m, jc + band) + 1):
            if (i, j) not in best:
                continue
            # figures without reading
            if i < n:
                it = F[i]
                if it['kind'] == 'd' and it['val'] == '8':
                    relax(i, j, i + 1, j, 0.3, ('null',))
                    if i + 1 < n and F[i + 1]['kind'] == 'd':
                        relax(i, j, i + 2, j, 0.5, ('null',))
                relax(i, j, i + 1, j, 3.0 if it['kind'] == 'd' else 4.0, ('extra',))
            if j >= m:
                continue
            u = U[j]
            kind, ch, wi, mode = u
            if kind == 'H':
                relax(i, j, i, j + 1, 0.0, ('hole',))
                if i < n:
                    relax(i, j + 0, i + 1, j, 0.2, ('holefig',)) if False else None
                    # absorb figures while staying on the hole unit
                    k = i
                    cost = 0.0
                    while k < n and k - i < 60:
                        k += 1
                        cost += 0.2
                        relax(i, j, k, j + 1, cost, ('hole',))
                continue
            # reading unit with no figure
            relax(i, j, i, j + 1, 0.0 if mode == 's' else (0.5 if mode == 'p' else 3.5), ('nofig',))
            if kind == 'd':
                if i < n and F[i]['kind'] == 'd' and F[i]['val'] == ch:
                    relax(i, j, i + 1, j + 1, 0.0, ('ok',))
                continue
            # dotted code against expansion words
            if i < n and F[i]['kind'] == 'N' and j in wstart:
                k = j
                w = wi
                for nw in range(1, 5):
                    if w >= len(words) or words[w]['kind'] not in ('word', 'partly', 'supplied'):
                        break
                    wt = nrm(re.sub(r'[\[\]?]', '', words[w]['text']))
                    if wt not in EXP and not wt.rstrip('.') in EXP:
                        break
                    k = words[w]['end']
                    relax(i, j, i + 1, k, 0.2, ('code', F[i]['val']))
                    w += 1
            # plain three figures as a code (dot lost) against expansion words
            f3 = figs(i, 3)
            if f3 in D.NOM and j in wstart:
                w = wi
                for nw in range(1, 5):
                    if w >= len(words) or words[w]['kind'] not in ('word', 'partly', 'supplied'):
                        break
                    wt = nrm(re.sub(r'[\[\]?]', '', words[w]['text']))
                    if wt not in EXP:
                        break
                    relax(i, j, i + 3, words[w]['end'], 0.6, ('code', f3 + '(nodot)'))
                    w += 1
            rest = ''.join(U[t][1] for t in range(j, min(m, j + 10)) if U[t][0] == 'c')
            for pt, cs in UNITS:
                if not rest.startswith(pt):
                    continue
                # units must be consecutive letters
                if any(U[t][0] != 'c' for t in range(j, min(m, j + len(pt)))):
                    continue
                for c in cs.split():
                    L = len(c)
                    # spurious dot: a dotted item whose digits are this code's (whole or part)
                    if i < n and F[i]['kind'] == 'N' and F[i]['val'] == c:
                        relax(i, j, i + 1, j + len(pt), 0.5, ('ok',))
                    f = figs(i, L)
                    if f == c:
                        relax(i, j, i + L, j + len(pt), -0.01 * L, ('ok',))
                    elif f is not None and sum(a != b for a, b in zip(f, c)) == 1:
                        relax(i, j, i + L, j + len(pt), 2.0, ('sub', c, f))
                    if L > 1:
                        for k in range(L):
                            short = c[:k] + c[k + 1:]
                            if figs(i, L - 1) == short:
                                relax(i, j, i + L - 1, j + len(pt), 2.5, ('miss', c, short))
                                break
                    f2 = figs(i, L + 1)
                    if f2 is not None:
                        for k in range(L + 1):
                            if f2[:k] + f2[k + 1:] == c and f2[k] != '8':
                                relax(i, j, i + L + 1, j + len(pt), 2.5, ('dbl', c, f2))
                                break
            # a dotted item that is really a letter group: consume it against 1-3 reading units whose codes concatenate
            if i < n and F[i]['kind'] == 'N':
                v = F[i]['val']
                for L1 in range(1, 4):
                    for L2 in range(0, 3):
                        a1, b1 = v[:L1], v[L1:L1 + L2] if L2 else ''
                        if L1 + L2 > 3:
                            continue
                        if L1 + L2 == 3 or True:
                            pass
                # (handled loosely: allow the dotted item to be skipped at a moderate cost)
                relax(i, j, i + 1, j, 2.0, ('extra',))
    # end state: all units consumed, figures may remain at the end (cost 0.05 each)
    endv, endi = INF, 0
    for i in range(n + 1):
        v = best.get((i, m), INF)
        if v < INF:
            v += 0.05 * (n - i)
            if v < endv:
                endv, endi = v, i
    if endv >= INF:
        return None
    # backtrace: per unit, how it was matched
    umatch = ['?'] * m
    uslip = [None] * m
    i, j = endi, m
    while (i, j) in back:
        pi, pj, info = back[(i, j)]
        k = info[0]
        if pj < j:
            for t in range(pj, j):
                umatch[t] = k
                if k in ('sub', 'miss', 'dbl'):
                    uslip[t] = info
        i, j = pi, pj
    return umatch, uslip, endv, endi


def report(rec, words, U, res, page, verbose=False):
    umatch, uslip, cost, endi = res
    flagged = []
    for w in words:
        if w['kind'] != 'word':
            continue
        us = [t for t in range(w['start'], w['end']) if U[t][3] == 'n']
        if not us:
            continue
        nofig = sum(1 for t in us if umatch[t] == 'nofig')
        slips = len(set(id(uslip[t]) for t in us if uslip[t]))
        shown = ''.join(U[t][1].upper() if (U[t][3] == 'n' and umatch[t] == 'nofig') else U[t][1]
                        for t in range(w['start'], w['end']))
        if nofig * 2 > len(us) or (nofig and len(us) <= 3):
            flagged.append(('SUPPLIED', w['text'] + ' ' + shown, nofig, len(us), slips))
        elif nofig or slips >= 2:
            flagged.append(('PARTLY', w['text'] + ' ' + shown, nofig, len(us), slips))
    return flagged


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('rec')
    ap.add_argument('--trans')
    ap.add_argument('--reading')
    ap.add_argument('--verbose', action='store_true')
    a = ap.parse_args()
    rpath = a.reading or os.path.join(D.TDIR, 'texts', f'{a.rec}_reading.md')
    pages = page_items(a.rec, a.trans)
    segs = segments(body(rpath))
    merged = {}
    order = []
    for p, s in segs:
        if p is None:
            continue
        key = p.lstrip('0').lower()
        if key not in merged:
            order.append(key)
            merged[key] = ''
        merged[key] += ' ' + s
    total_w = total_s = total_p = 0
    verbose = a.verbose
    for key in order:
        if key not in pages:
            print(f'== {a.rec} {key}: page not in the transcription')
            continue
        words, U = tokenize(merged[key])
        F = pages[key]
        res = align(F, U, words)
        if res is None:
            res = align(F, U, words, band=600)
        if res is None:
            print(f'== {a.rec} {key}: no alignment')
            continue
        fl = report(a.rec, words, U, res, key)
        nw = sum(1 for w in words if w['kind'] == 'word')
        ns = sum(1 for f in fl if f[0] == 'SUPPLIED')
        npt = sum(1 for f in fl if f[0] == 'PARTLY')
        total_w += nw
        total_s += ns
        total_p += npt
        verbose = a.verbose
        print(f'== {a.rec} {key}: {nw} words, {ns} supplied, {npt} partly; figures used {res[3]} of {len(F)}, cost {res[2]:.0f}')
        for f in fl:
            if f[2] or verbose:
                print(f'   {f[0]:8s} {f[1]}  ({f[2]}/{f[3]} letters without figure, {f[4]} slips)')
    print(f'TOTAL {a.rec}: {total_w} words, {total_s} supplied, {total_p} partly')


if __name__ == '__main__':
    main()
