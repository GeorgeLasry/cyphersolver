# renotate.py: converts the reading (reading_original.md) and the English (translation_en.md) to the notation asked
# for in #94, by aligning each reading line with the tokens it decodes:
#   plain word        carried by firm values
#   [x]               a supplied letter (inside a word)
#   [?word]           a doubtful word (the decode gives it only in part)
#   {?word}           a tentative code-group (or sign) value; inside a word only the tentative part is braced
#   [?n groups]       a run of unread code groups, sized; [?sign] / [?n signs] unvalued signs; [?n letters] decoded
#                     letters that make no word; parts joined by commas
# and writes tokens.tsv (one row per token: line, position, token, split label, value, status, reading word) and
# sin_x_tokens.tsv (every sin/sim and X token: assigned value, basis, model margin).
# Input: work/reading_v1_old_notation.md / work/translation_en_v1_old_notation.md (the earlier notation), transcriptions/n73_tokens.txt, work/v15x.txt,
# work/splitsin.tsv, work/splitx.tsv, keys/groups.json, work/signs.txt. Run from the vich1515 folder.
import json, re, collections

TENT_SIGNS = {'EQ', 'LAM', 'SL', 'OS', 'D'}
IMG = {(12, 1): 'sin', (12, 2): 'sim', (13, 1): 'sin', (17, 1): 'sim', (21, 1): 'sim', (35, 2): 'sin'}  # setsin.py
S = dict(kv.split('=') for kv in open('work/signs.txt').read().split())
G = json.load(open('keys/groups.json'))
orig = [l.split() for l in open('transcriptions/n73_tokens.txt')]
split = [l.split() for l in open('work/v15x.txt')]
isg = lambda t: t.islower() and t.isalpha()


def tok_info(t):
    """(value or None, status) for a split label."""
    if isg(t):
        g = G.get(t)
        if g: return g['value'].lower(), g['status']
        return None, 'unread group'
    if t in S: return S[t].lower(), ('tentative' if t in TENT_SIGNS else 'firm')
    return None, 'unvalued sign'


def block(path):
    t = open(path).read(); a = t.index('```') + 3; b = t.index('```', a)
    lines = {}
    for l in t[a:b].split('\n'):
        m = re.match(r'\s*(\d+)\s{2}(.*)', l)
        if m: lines[int(m.group(1))] = m.group(2)
    return t, lines


ITEM = re.compile(r'\[\?[^\]]*\]|\[[^\]?][^\]]*\]|.', re.S)


def parse(line):
    """Reading line -> list of items: ('H',id) bare hole, ('D',id,word) doubtful bracket, ('S',id,letters), ('C',ch)."""
    out = []; k = 0
    for m in ITEM.finditer(line):
        s = m.group(0)
        if s == '[?]': out.append(('H', k)); k += 1
        elif s.startswith('[?'): out.append(('D', k, s[2:-1])); k += 1
        elif s.startswith('[') and len(s) > 1: out.append(('S', k, s[1:-1])); k += 1
        else: out.append(('C', s))
    return out


def align(items, dec):
    """Align reading letters/holes with decode chars (dec: list of (char, token index)); return per reading unit the
    list of decode positions it covers. Units: one per letter (plain or in a doubtful bracket) and one per bare hole."""
    units = []   # (kind, ref) kind L: letter (ref=(item index, char)), H: hole (ref=item index), S: supplied letter
    for i, it in enumerate(items):
        if it[0] == 'C':
            if it[1].isalpha(): units.append(('L', i, it[1].lower()))
        elif it[0] == 'D':
            for ch in it[2]:
                if ch.isalpha(): units.append(('L', i, ch.lower()))
        elif it[0] == 'S':
            for ch in it[2]:
                if ch.isalpha(): units.append(('S', i, ch.lower()))
        else: units.append(('H', i, None))
    n, m = len(units), len(dec); INF = 1e9
    D = [[INF] * (m + 1) for _ in range(n + 1)]; B = [[None] * (m + 1) for _ in range(n + 1)]
    D[0][0] = 0
    for i in range(n + 1):
        for j in range(m + 1):
            c = D[i][j]
            if c >= INF: continue
            if j < m and c + 2 < D[i][j + 1]: D[i][j + 1] = c + 2; B[i][j + 1] = ('del', i, j)        # decode char unread
            if i < n:
                k, _, ch = units[i]
                if k == 'H':
                    for jj in range(j, min(m, j + 40) + 1):
                        cost = 3 if jj == j else sum(0 if dec[x][0] == '#' else 0.3 for x in range(j, jj))
                        if c + cost < D[i + 1][jj]: D[i + 1][jj] = c + cost; B[i + 1][jj] = ('hole', i, j)
                elif k == 'S':
                    if c < D[i + 1][j]: D[i + 1][j] = c; B[i + 1][j] = ('ins', i, j)
                else:
                    if j < m:
                        cost = 0 if dec[j][0] == ch else 2.5
                        if c + cost < D[i + 1][j + 1]: D[i + 1][j + 1] = c + cost; B[i + 1][j + 1] = ('match', i, j)
                    if c + 2 < D[i + 1][j]: D[i + 1][j] = c + 2; B[i + 1][j] = ('ins', i, j)
    cover = [[] for _ in range(n)]; exact = [True] * n
    i, j = n, m
    while i or j:
        op, pi, pj = B[i][j]
        if op == 'match':
            cover[pi].append(pj)
            if dec[pj][0] != units[pi][2]: exact[pi] = False
        elif op == 'hole': cover[pi].extend(range(pj, j))
        elif op == 'ins' and units[pi][0] == 'L': exact[pi] = False
        i, j = (pi, pj) if op != 'del' else (i, pj)
    return units, cover, exact, D[n][m]


def size_label(toks, letters, line_toks):
    g = sum(1 for t in toks if tok_info(line_toks[t])[1] == 'unread group')
    s = sum(1 for t in toks if tok_info(line_toks[t])[1] == 'unvalued sign')
    parts = []
    if g: parts.append(f'{g} group' + ('s' if g > 1 else ''))
    if s: parts.append('sign' if s == 1 and not g and not letters else f'{s} sign' + ('s' if s > 1 else ''))
    if letters: parts.append(f'{letters} letter' + ('s' if letters > 1 else ''))
    return '[?' + ', '.join(parts) + ']' if parts else '[?]', (g, s, letters)


def convert_line(n, line):
    line_toks = split[n - 1]
    dec = []
    for ti, t in enumerate(line_toks):
        v, st = tok_info(t)
        if v is None: dec.append(('#', ti))
        else: dec.extend((c, ti) for c in v)
    items = parse(line)
    units, cover, exact, cost = align(items, dec)
    # per item: tokens covered, letters covered, per-letter token status
    item_tok = collections.defaultdict(list); item_exact = collections.defaultdict(lambda: True)
    letter_tok = {}   # unit index -> token index
    for ui, (k, ii, ch) in enumerate(units):
        for p in cover[ui]: item_tok[ii].append(p)
        if k == 'L':
            if not exact[ui]: item_exact[ii] = False
            if cover[ui]: letter_tok[ui] = dec[cover[ui][0]][1]
    # token -> reading unit, for tokens.tsv
    tok_unit = {}
    for ui in range(len(units)):
        for p in cover[ui]: tok_unit.setdefault(dec[p][1], ui)
    # render
    out = []; ui = 0; hole_info = {}   # item index -> (label, sizes)
    # hole runs: consecutive H items separated only by spaces/punctuation, not glued to letters
    runs = []; cur = []
    for i, it in enumerate(items):
        if it[0] == 'H':
            def word_like(x):
                return 0 <= x < len(items) and (items[x][0] in 'DS' or (items[x][0] == 'C' and items[x][1].isalpha()))
            glued = word_like(i - 1) or word_like(i + 1)
            if glued: runs.append([i]); cur = []
            elif cur and cur[-1] < i and all(items[x][0] == 'C' and items[x][1] == ' ' for x in range(cur[-1] + 1, i)):
                cur.append(i)
            else:
                cur = [i]; runs.append(cur)
        elif it[0] != 'C' or it[1].isalpha(): cur = []
    run_of = {i: r for r in runs for i in r}
    unit_of_item = {}
    for u, (k, ii, ch) in enumerate(units): unit_of_item.setdefault(ii, []).append(u)
    done = set(); res = []; i = 0
    while i < len(items):
        it = items[i]
        if it[0] == 'H':
            r = run_of[i]
            if i == r[0]:
                toks = sorted({dec[p][1] for x in r for p in item_tok[x]})
                letters = sum(1 for x in r for p in item_tok[x] if dec[p][0] != '#')
                lab, sz = size_label(toks, letters, line_toks)
                for x in r: hole_info[x] = (lab, sz, r)
                res.append(lab)
                # skip the rest of the run (and the separators between)
                i = r[-1] + 1; continue
            i += 1; continue
        if it[0] == 'D':
            us = unit_of_item.get(i, [])
            toks = [letter_tok.get(u) for u in us]
            st = [tok_info(line_toks[t])[1] if t is not None else None for t in toks]
            if item_exact[i] and us and all(t is not None for t in toks) and any(s == 'tentative' for s in st):
                # tentative value(s): brace only the tentative stretch(es); the rest plain
                word = it[2]; letters_iter = iter(range(len(us))); s_out = ''; open_ = False; li = 0
                for ch in word:
                    if not ch.isalpha(): s_out += ch; continue
                    tnt = st[li] == 'tentative'; li += 1
                    if tnt and not open_: s_out += '{?'; open_ = True
                    if not tnt and open_: s_out += '}'; open_ = False
                    s_out += ch
                if open_: s_out += '}'
                res.append(s_out); hole_info[i] = ('T', None, None)
            else:
                res.append(f'[?{it[2]}]'); hole_info[i] = ('D', None, None)
            i += 1; continue
        if it[0] == 'S': res.append(f'[{it[2]}]'); hole_info[i] = ('S', None, None); i += 1; continue
        # plain char: a plain letter that rests on a tentative value (a tentative sign such as SL, or a tentative group
        # read as part of a plain word) is braced like a tentative value
        if it[1].isalpha() and i in unit_of_item:
            u = unit_of_item[i][0]; t = letter_tok.get(u)
            tnt = t is not None and tok_info(line_toks[t])[1] == 'tentative'
            prev_open = bool(res) and res[-1] == '\x00'
            if tnt:
                if prev_open: res.pop(); res.append(it[1]); res.append('\x00')
                else: res.append('{?'); res.append(it[1]); res.append('\x00')
            else:
                if prev_open: res.pop(); res.append('}')
                res.append(it[1])
            i += 1; continue
        if res and res[-1] == '\x00': res.pop(); res.append('}')
        res.append(it[1]); i += 1
    if res and res[-1] == '\x00': res.pop(); res.append('}')
    new = ''.join(res).replace('\x00', '}')
    # plain words resting on tentative tokens
    flagged = []
    for u, (k, ii, ch) in enumerate(units):
        if k == 'L' and items[ii][0] == 'C' and u in letter_tok and tok_info(line_toks[letter_tok[u]])[1] == 'tentative':
            flagged.append(u)
    return new, items, hole_info, tok_unit, units, cost, flagged


def holes_seq(items):
    """Marked items in order: bare holes and doubtful brackets ('q'), supplied ('s')."""
    return [(i, 'q' if it[0] in 'HD' else 's') for i, it in enumerate(items) if it[0] in 'HDS']


def convert_en(line, r_items, r_info):
    e_items = parse(line)
    rq = [i for i, k in holes_seq(r_items) if k == 'q']
    eq = [i for i, k in holes_seq(e_items) if k == 'q']
    if len(rq) != len(eq): return None
    emap = dict(zip(eq, rq))
    res = []; i = 0
    while i < len(e_items):
        it = e_items[i]
        if it[0] == 'H':
            ri = emap[i]; info = r_info.get(ri)
            if info and info[0] == 'T': res.append('{?}'); i += 1; continue
            if info and info[0] not in 'TDS':
                lab, sz, run = info
                # merge following English bare holes mapped to the same reading run, separated by spaces only
                j = i; members = [ri]
                while True:
                    k = j + 1
                    while k < len(e_items) and e_items[k][0] == 'C' and e_items[k][1] == ' ': k += 1
                    if k < len(e_items) and e_items[k][0] == 'H' and emap[k] in run and emap[k] not in members:
                        members.append(emap[k]); j = k
                    else: break
                if set(members) == set(run): res.append(lab)
                else:   # the English splits the run: give this piece its own share (whole run size on the first piece)
                    res.append(lab if ri == run[0] else '[?]')
                i = j + 1; continue
            res.append('[?]'); i += 1; continue
        if it[0] == 'D':
            ri = emap[i]; info = r_info.get(ri)
            res.append('{?' + it[2] + '}' if info and info[0] == 'T' else f'[?{it[2]}]'); i += 1; continue
        if it[0] == 'S': res.append(f'[{it[2]}]'); i += 1; continue
        res.append(it[1]); i += 1
    return ''.join(res)


R_text, R = block('work/reading_v1_old_notation.md')
E_text, E = block('work/translation_en_v1_old_notation.md')
newR, newE = {}, {}; rows = []; bad = []; flagged_all = []; costs = []
for n in sorted(R):
    new, items, info, tok_unit, units, cost, flagged = convert_line(n, R[n])
    newR[n] = new; costs.append((cost, n))
    if flagged: flagged_all.append(n)
    en = convert_en(E.get(n, ''), items, info)
    if en is None: bad.append(n); en = E.get(n, '')
    newE[n] = en
    # tokens.tsv rows: reading word for each token
    words = []   # map unit -> word text in the new line is hard; use the old item text as the reading word
    for ti, (o, s) in enumerate(zip(orig[n - 1], split[n - 1])):
        v, st = tok_info(s)
        u = tok_unit.get(ti)
        if u is None: rw = ''
        else:
            k, ii, ch = units[u]; it = items[ii]
            if it[0] == 'H': rw = info[ii][0] if info.get(ii) and info[ii][0] not in 'TDS' else '[?]'
            elif it[0] == 'D': rw = ('{?' + it[2] + '}') if info.get(ii, ('',))[0] == 'T' else f'[?{it[2]}]'
            else:
                # the plain word containing this letter in the old line
                pos = sum(len(x[1]) if x[0] == 'C' else len(x[2]) + 3 if x[0] == 'D' else len(x[2]) + 2 if x[0] == 'S' else 3 for x in items[:ii])
                old = R[n]; a = pos
                while a > 0 and not old[a - 1].isspace(): a -= 1
                b = pos
                while b < len(old) and not old[b].isspace(): b += 1
                rw = old[a:b].strip(',.;:')
        look = ''
        if o in ('sin', 'sim'): look = 'look-alike sin/sim' if o == 'sin' else ''
        if o == 'X': look = 'look-alike X'
        rows.append((n, ti + 1, o, s, v if v is not None else '', st + (f' ({look})' if look else ''), rw))

open('work/renotate_check.txt', 'w').write(
    'lines whose English holes could not be mapped: ' + ' '.join(map(str, bad)) + '\n'
    + 'lines with plain words resting on tentative values: ' + ' '.join(map(str, flagged_all)) + '\n'
    + 'worst alignment costs: ' + ' '.join(f'{n}:{c:.1f}' for c, n in sorted(costs, reverse=True)[:15]) + '\n')


def rebuild(text, lines):
    a = text.index('```') + 3; b = text.index('```', a)
    body = '\n' + '\n'.join(f'{n:3d}  {lines[n]}' for n in sorted(lines)) + '\n'
    return text[:a] + body + text[b:]


# English lines adjusted by hand where the reading marks a word the English carries differently (checked with
# holecheck2.py): a size label glued to a partial word, and plain words resting on a tentative sign or group.
EN_FIX = {
    55: ("that if some [?1 group, 1 letter]", "that if some[?1 group, 1 letter]"),
    71: ("and from this was born", "and from {?this} was born"),
    76: ("him; I, for", "him; I, be-"),
    77: ("my part, am very {?ill}-content", "cause I am {?of this} very {?ill}-content"),
    99: ("without some delay [?1 group] [?1 group] with", "without delay some[?1 group] [?1 group] with"),
    103: ("thrown out of Italy", "{?thrown} out of Italy"),
    121: ("some [?1 group] and", "some[?1 group] and"),
}
for n, (x, y) in EN_FIX.items():
    assert x in newE[n], (n, newE[n]); newE[n] = newE[n].replace(x, y)
open('work/reading_body_v2.txt', 'w').write('\n'.join(f'{n:3d}  {newR[n]}' for n in sorted(newR)) + '\n')
open('work/english_body_v2.txt', 'w').write('\n'.join(f'{n:3d}  {newE[n]}' for n in sorted(newE)) + '\n')
with open('tokens.tsv', 'w') as f:
    f.write('line\tposition\ttoken\tsplit_label\tvalue\tstatus\treading_word\n')
    for r in rows: f.write('\t'.join(map(str, r)) + '\n')

# sin/sim and X tokens
ssin = {(int(a), int(b)): (float(m), c) for a, b, l, r, m, c in (x.rstrip('\n').split('\t') for x in open('work/splitsin.tsv'))}
sx = {int(k): (c, float(m)) for k, l, r, c, m in (x.rstrip('\n').split('\t') for x in open('work/splitx.tsv'))}
with open('sin_x_tokens.tsv', 'w') as f:
    f.write('line\tposition\ttoken_as_transcribed\tassigned\tvalue\tbasis\tmodel_margin\n')
    k = -1
    for n, (o_line, s_line) in enumerate(zip(orig, split), 1):
        nsin = 0
        for j, (o, s) in enumerate(zip(o_line, s_line), 1):
            k += 1
            if o == 'sin':
                nsin += 1
                if (n, nsin) in IMG: basis = 'image-checked'
                else: basis = 'model-assigned'
                m = ssin.get((n, j), (None, None))[0]
                f.write(f'{n}\t{j}\tsin\t{s}\t{G[s]["value"]}\t{basis}\t{"" if m is None else f"{m:+.2f} (es-en)"}\n')
            elif o == 'sim':
                f.write(f'{n}\t{j}\tsim\tsim\ten\ttranscribed sim\t\n')
            elif o == 'X':
                c, m = sx[k]
                f.write(f'{n}\t{j}\tX\t{s}\t{c}\tmodel-assigned\t{m:.2f} (best-second)\n')
print('done; unmapped English lines:', bad, '; tentative-plain lines:', flagged_all)
