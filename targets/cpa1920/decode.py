"""Catalogue 678: CPA book code, letters seized at 170 Bleecker St. (NARA M1085 roll 940, case 202600).

A token a/b is line a, letter b of one key page, letters counted without spaces. Digits are written by pointing to
the digit characters at the start of a key line (the key page seems to be a numbered list of titles).

This script rebuilds the key grid from the Bureau of Investigation's own decodes only (bureau_decodes.tsv), tests it
run by run (leave one run out), runs three controls, tests the two digit models and decodes every run in
transcription.txt with the full grid.

  python decode.py              print everything (the file decryption.txt is this output)
  python decode.py --key        write key_new.tsv and key_old_p14.tsv from the Bureau decodes

Standard library only. Paths are relative to this folder.
"""
import collections
import json
import os
import random
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def read_runs():
    """transcription.txt -> {run id: (key, [word, ...])}, a word being a list of tokens; {..} is clear text."""
    runs = {}
    with open(os.path.join(HERE, 'transcription.txt'), encoding='utf-8') as fh:
        for line in fh:
            line = line.rstrip('\n')
            if not line or line.startswith('#'):
                continue
            rid, key, text = line.split('\t')
            words, cur = [], []
            text = re.sub(r'\{[^}]*\}', lambda m: ' ' + m.group(0).replace(' ', '_') + ' ', text)
            for part in text.split():
                if part == '-':
                    words.append(cur); cur = []
                else:
                    cur.append(part)
            words.append(cur)
            runs[rid] = (key, words)
    return runs


def read_bureau():
    """bureau_decodes.tsv -> list of (unit, run, as written, [(char, token), ...])."""
    units = []
    with open(os.path.join(HERE, 'bureau_decodes.tsv'), encoding='utf-8') as fh:
        for line in fh:
            line = line.rstrip('\n')
            if not line or line.startswith('#') or line.startswith('unit\t'):
                continue
            unit, run, written, align = line.split('\t')
            pairs = []
            for item in align.split('; '):
                plain, toks = item.split('=')
                toks = toks.split()
                assert len(plain) == len(toks), (unit, item)
                pairs.append((plain, toks))
            units.append((unit, run, written, pairs))
    return units


def check_alignment(runs, units):
    """Every aligned Bureau word must be a stretch of tokens of its run as transcribed."""
    for unit, run, _, pairs in units:
        flat = ' '.join(t for w in runs[run][1] for t in w)
        for plain, toks in pairs:
            assert ' '.join(toks) in flat, (unit, plain, toks)


def flat_pairs(pairs):
    return [(ch, t) for plain, toks in pairs for ch, t in zip(plain, toks)]


def pos(t):
    return int(t.split('/')[1])


def build(units):
    g = collections.defaultdict(collections.Counter)
    for u in units:
        for ch, tok in u:
            if ch != '?':
                g[tok][ch] += 1
    return g


def top(g, t):
    return g[t].most_common(1)[0][0] if t in g else None


def score(g, unit, digits):
    r = collections.Counter(); bad = []
    for ch, tok in unit:
        if ch == '?' or ch.isdigit() != digits:
            continue
        p = top(g, tok)
        if p is None: r['unseen'] += 1
        elif p == ch: r['right'] += 1
        else: r['wrong'] += 1; bad.append(f'{tok}: Bureau {ch}, grid {p}')
    return r, bad


# Clashes inside the Bureau's own decodes, settled for the decoding (not for the tests above it):
# 1/2 is 7 in 773 (A887.1) and I in OHIO (A11); every other digit cell and no letter cell sits at letter position 1-2,
# so 1/2 = 7 and the OHIO token is taken as the writer's slip for 1/3 (I). 5/14 is U six times and Y once (the
# Bureau's SOVRYS): the majority stands. 26/30 is Z in Speizman and L in K-ldas, one each: left open as [Z|L].
RESOLVED = {'1/2': '7'}


RUN_NOTES = {
    'A11': 'S[3/17][3/13][3/18]L: the Bureau also left these three letters open, and no other run uses the cells. '
           'OH7O: 1/2 is 7 in 773 (A887.1); the Bureau reads OHIO, so the writer most likely typed 1/2 for 1/3 (I).',
    'A13': 'The final x of PHOENIX is typed in clear.',
    'A15.1': 'KRGA: 3/4 = R is attested 8 times; the Bureau wrote "Ki?ga" and struck "S. K". G (5/5) comes only from '
             'HUGO. The name stays doubtful.',
    'A15.2': '18/6 has no value. 26/30 is Z in Speizman and L here (Bureau "K-ldas"), so the name is K?LDAS or K?ZDAS. '
             '14/2 is at a digit position but has no attested value: the Bureau wrote "23-8"; 2308 if 14/2 is 0 [?].',
    'A15.4': '3/1 has no value; the Bureau wrote "48 -". The third digit is open.',
    'A706.1': '5/29 has no value; ATWOOD is the likely name [?], W is not attested at 5/29.',
    'A706.2': '5/12 has no value. If 5/12 is C, the five runs read UCP and CP (two parties); C at 5/12 is not attested.',
    'A706.3': 'U = 11/15 and P = 6/13 come only from the Bureau decode of A887.2 (SUPERIOR, POLTN).',
    'A706.4': 'Typed "5/12 and 6/13/": the clear "and" between the tokens is most likely a slip.',
    'A706.5': 'Typed 5/13, not 5/12, and again with "and" between the tokens.',
    'A880.1': 'Old code page 14. Its grid has only the one Bureau decode (A14), so three cells are open. A typed word '
              'of about 8 letters, starting with s, follows and is struck through; it is not read.',
    'A880.2': 'Followed by the typed word "arden", struck through. The grid gives A R from the Bureau decodes; '
              'D E N rest on that struck word alone (2/8-2/12 = ARDEN, as in ENOCH ARDEN on line 2).',
    'A886.1': 'The first token of the number is cut at the edge; the Bureau read 1320.',
    'A886.2': 'The last token of SMI[..] is cut; the Bureau read Smith (h).',
    'A886.3': 'The page is torn before 2/3: a token may be lost, so the first name ends in ERIC (very likely Eric). '
              'The Bureau decode is torn too ("[..]hlin").',
    'A887.2': '?/16 has an unreadable line number. S[?]R is STR, as in other runs; the Bureau wrote St.',
    'A887.3': 'The last token is 9/2 plus an unreadable figure, or a slip; WI[S].',
    'A888': '1148 S. 8[th] St. (Philadelphia).',
    'A939.1': 'I. W., most likely the I.W.W., which the same letter names in clear.',
    'A939.2': 'The Bureau wrote SOVRYS; 5/14 is U in six other Bureau words. SOV. RUS. = the magazine Soviet Russia.',
    'B494': 'B = 10/15 comes from BARRY; every other cell is in two or more Bureau words.',
}


def value(g, t):
    """The value of a token for decoding: None when unknown, 'X|Y' when two Bureau values tie."""
    if t in RESOLVED and t in g:
        return RESOLVED[t]
    if t not in g:
        return None
    mc = g[t].most_common()
    if len(mc) > 1 and mc[0][1] == mc[1][1]:
        return '|'.join(sorted(k for k, v in mc if v == mc[0][1]))
    return mc[0][0]


def decode_word(g, word):
    out = []
    for t in word:
        if t.startswith('{'):
            out.append(t.strip('{}').replace('_', ' ').lower())
        elif t.startswith('[cut]'):
            out.append('[..]')
        else:
            v = value(g, t)
            out.append('[' + t + ']' if v is None else '[' + v + ']' if '|' in v else v)
    return ''.join(out)


def main(argv):
    runs = read_runs()
    allunits = read_bureau()
    check_alignment(runs, allunits)
    new_units = [(u, r, w, p) for u, r, w, p in allunits if runs[r][0] == 'new']
    old_units = [(u, r, w, p) for u, r, w, p in allunits if runs[r][0] == 'old']
    BUREAU = collections.OrderedDict((u, flat_pairs(p)) for u, r, w, p in new_units)
    full = build(BUREAU.values())
    old = build(flat_pairs(p) for u, r, w, p in old_units)

    if '--key' in argv:
        for fname, g, units in (('key_new.tsv', full, new_units), ('key_old_p14.tsv', old, old_units)):
            seen = collections.defaultdict(list)
            for u, r, w, p in units:
                for ch, t in flat_pairs(p):
                    if ch != '?' and u not in seen[t]:
                        seen[t].append(u)
            with open(os.path.join(HERE, fname), 'w', encoding='utf-8', newline='\n') as fh:
                fh.write('cell\tvalue\tuses\tattested_in\tclash\n')
                for t in sorted(g, key=lambda x: tuple(map(int, x.split('/')))):
                    c = g[t]
                    clash = ', '.join(f'{k} x{v}' for k, v in c.most_common()) if len(c) > 1 else ''
                    fh.write(f'{t}\t{value(g, t)}\t{sum(c.values())}\t{" ".join(seen[t])}\t{clash}\n')
        print('wrote key_new.tsv and key_old_p14.tsv')
        return 0

    out = []
    P = out.append
    P('# decode.py output: grid from the Bureau decodes, tests, and every run decoded')
    P('')
    P(f'new-code cells from Bureau decodes: {len(full)}; old-code (page 14) cells: {len(old)}')
    P('cells with two different Bureau values: ' + json.dumps({k: dict(v) for k, v in full.items() if len(v) > 1}))

    P('\n== leave one run out: grid from the OTHER Bureau runs predicts this run (R right, W wrong, U unseen) ==')
    TL = collections.Counter(); TD = collections.Counter()
    for name, unit in BUREAU.items():
        g = build([u for n, u in BUREAU.items() if n != name])
        rl, bl = score(g, unit, False); rd, bd = score(g, unit, True)
        TL += rl; TD += rd
        P(f"{name:8s} letters R{rl['right']:2d} W{rl['wrong']} U{rl['unseen']:2d} | digits R{rd['right']} W{rd['wrong']} "
          f"U{rd['unseen']}  {'; '.join(bl + bd)}")
    P(f"TOTAL letters R{TL['right']} W{TL['wrong']} U{TL['unseen']} | digits R{TD['right']} W{TD['wrong']} U{TD['unseen']}")

    random.seed(7); C = collections.Counter()
    for rep in range(500):
        for name, unit in BUREAU.items():
            g = build([u for n, u in BUREAU.items() if n != name])
            ks = list(g); vs = [g[k] for k in ks]; random.shuffle(vs); gs = dict(zip(ks, vs))
            for ch, tok in unit:
                if ch == '?': continue
                p = top(gs, tok)
                C['unseen' if p is None else ('right' if p == ch else 'wrong')] += 1
    P(f"CONTROL shuffled grid, 500 repetitions: right {C['right']}, wrong {C['wrong']}, unseen {C['unseen']}; "
      f"right rate {C['right'] / (C['right'] + C['wrong']):.3f}")
    for lab, f in (('one line down', lambda t: f"{int(t.split('/')[0]) + 1}/{t.split('/')[1]}"),
                   ('one letter along', lambda t: f"{t.split('/')[0]}/{int(t.split('/')[1]) + 1}")):
        S = collections.Counter()
        for name, unit in BUREAU.items():
            g = build([u for n, u in BUREAU.items() if n != name]); sh = {f(k): v for k, v in g.items()}
            for ch, tok in unit:
                if ch == '?': continue
                p = sh[tok].most_common(1)[0][0] if tok in sh else None
                S['unseen' if p is None else ('right' if p == ch else 'wrong')] += 1
        P(f"CONTROL grid shifted {lab}: right {S['right']}, wrong {S['wrong']}, unseen {S['unseen']}")
    P('A880 run 2 (2/8 2/9 2/10 2/11 2/12), followed by the struck typed word "arden": the grid gives '
      + ''.join(value(full, t) or '.' for t in '2/8 2/9 2/10 2/11 2/12'.split()))

    P('\n== digits ==')
    dig = [(ch, t) for u in BUREAU.values() for ch, t in u if ch.isdigit()]
    let = [(ch, t) for u in BUREAU.values() for ch, t in u if ch.isalpha()]
    P(f'digit tokens {len(dig)}, at letter position 1-2 of their line: {sum(pos(t) <= 2 for _, t in dig)}')
    P(f'letter tokens {len(let)}, at letter position 1-2: {sum(pos(t) <= 2 for _, t in let)} '
      + str([(c, t) for c, t in let if pos(t) <= 2]))
    dcell = collections.defaultdict(set)
    for ch, t in dig: dcell[t].add(ch)
    P('digit cells: ' + ', '.join(f"{t}={''.join(sorted(v))}" for t, v in
                                   sorted(dcell.items(), key=lambda x: tuple(map(int, x[0].split('/'))))))
    P('cells used for two different digits: ' + (str([t for t, v in dcell.items() if len(v) > 1]) or 'none'))
    P('first-letter-of-the-number-word rule (1=O, 2/3=T, 4/5=F, 6/7=S, 8=E, 0=Z) against the data:')
    for a, b in (('4', '5'), ('6', '7'), ('2', '3')):
        ca = sorted({t for c, t in dig if c == a}); cb = sorted({t for c, t in dig if c == b})
        P(f'  {a} and {b} would share a letter; cells for {a}: {ca}, for {b}: {cb}, shared: {sorted(set(ca) & set(cb))}')
    INIT = {'0': 'Z', '1': 'O', '2': 'T', '3': 'T', '4': 'F', '5': 'F', '6': 'S', '7': 'S', '8': 'E'}
    for d, L in sorted(INIT.items()):
        n = sum(1 for t in full if pos(t) >= 3 and top(full, t) == L)
        P(f"  digit {d} -> '{L}': {n} known '{L}' cells at position 3 or later could serve; used for a digit: 0")

    P('\n== grid rows (letter positions 1-34) from the Bureau decodes; "." = no value ==')
    for L in range(1, 28):
        row = ''.join((value(full, f'{L}/{p}') or '.')[:1] if '|' not in (value(full, f'{L}/{p}') or '') else '?'
                      for p in range(1, 35))
        if row.strip('.'): P(f'line {L:2d}: {row}')

    P('\n== every run, decoded with the full grid ==')
    P('Each word: tokens, then the value of each token. [a/b] = cell with no value; [..] = cut or torn; lower case = '
      'typed in clear.')
    bureau_of = {r: w for u, r, w, p in allunits}
    total = valued = 0
    for rid, (key, words) in runs.items():
        g = full if key == 'new' else old
        P(f'\n{rid} ({key} code)' + (f'   Bureau: {bureau_of[rid]}' if rid in bureau_of else '   no Bureau decode'))
        for w in words:
            toks = [t for t in w if not t.startswith('{')]
            for t in toks:
                if t.startswith('[cut]'): continue
                v = value(g, t)
                total += 1; valued += v is not None and '|' not in v
            P(f"  {' '.join(w).replace('_', ' '):45s} {decode_word(g, w)}")
        P('  = ' + ' - '.join(decode_word(g, w) for w in words))
        if rid in RUN_NOTES: P('  note: ' + RUN_NOTES[rid])
    P(f'\ntokens (cut markers not counted): {total}; with a value from the grid: {valued} ({valued / total:.3f})')

    text = '\n'.join(out)
    print(text)
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
