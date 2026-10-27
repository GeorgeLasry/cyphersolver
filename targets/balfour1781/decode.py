"""Decipher the Balfour letters from the ciphertext alone, with the ring and the setting indicators.

System (Saberton's 'Common cipher'): RING is a fixed cyclic order of 25 numbers turned against a
25-letter alphabet (i = j). The number standing for 'a' is the setting. Numbers >= 30 are fillers.
A setting indicator is a dash group of fillers holding one real number: that number becomes 'a'
(the decipherer bracketed these groups with a brace). The ring was rebuilt by ring.py from the
interlinear; here the interlinear is used only to score the result.

Usage: python decode.py  -> decoded.txt, agreement per page and per letter
"""
import collections
import glob
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
from lang import lm  # noqa: E402

from key_from_interlinear import load, tokens, align

HERE = os.path.dirname(os.path.abspath(__file__))
A = 'abcdefghiklmnopqrstuvwxyz'
RING = [5, 24, 29, 1, 25, 23, 22, 6, 19, 9, 17, 13, 16, 7, 12, 8, 14, 15, 26, 4, 18, 21, 3, 2, 11]
POS = {n: i for i, n in enumerate(RING)}
FILLER_FROM = 30
SENSE = -3.0   # mean log-prob per char; English about -1.5 to -2.5, gibberish below -5
LETTERS = {'A1': range(717, 721), 'A2': range(721, 725), 'A3': range(725, 728),
           'B': range(729, 733), 'C': range(733, 737)}


# the decipherer's own corrections of indicators: (page, line) -> number for 'a'
CORRECTED = {('718', 15): 13}   # p. 718: 25 underlined, 'should be 13'
# setting at the start of a letter that opens without an indicator
START = {'A2': 9, 'A3': 14}   # Nos. 2 and 3 open without an indicator and carry the previous sheet's last setting (p. 720 L15 a=9 -> 'bridge'; p. 724 L20 a=14)


# Balfour to Stewart, 12 Aug 1781, uses a different cipher: one fixed table, fillers 40 and up.
# Rebuilt from its interlinear (key_from_interlinear.py on pp. 733-736, NULL_FROM=40); values
# with a single vote are left out; 2, 3, 19, 30 stay open.
TABLES = {'C': {12: 'b', 13: 'e', 14: 'h', 15: 'l', 16: 'o', 17: 'r', 18: 'u', 22: 'c', 23: 'f',
                24: 'i', 25: 'm', 26: 'p', 27: 's', 28: 'v', 29: 'y', 31: 'a', 32: 'd', 33: 'g',
                35: 'n', 37: 't', 38: 'w',
                34: 'k', 1: 'e'}}   # 34 and 1 from context, three readings each (keep, keep, Monk's; state, depot, the)
TABLE_FILLER_FROM = 40


def letter_of(page):
    return next((g for g, r in LETTERS.items() if int(page) in r), 'other')


def is_indicator(group):
    real = [n for n in group if n is not None and n < FILLER_FROM]
    fill = [n for n in group if n is not None and n >= FILLER_FROM]
    return len(real) == 1 and len(fill) >= 3


def is_candidate(group):
    """One real number and two fillers: an indicator, or a one-letter word padded with fillers."""
    real = [n for n in group if n is not None and n < FILLER_FROM]
    fill = [n for n in group if n is not None and n >= FILLER_FROM]
    return len(real) == 1 and len(fill) >= 2


_MODEL = None


def lm_prefers_switch(groups, gi, a_num, span=40):
    """Decide a two-filler candidate: score the next `span` letters under both readings."""
    global _MODEL
    if _MODEL is None:
        _MODEL = lm.load('en-modern', spaces=False)
    real = next(n for _, (n, _u) in groups[gi] if n is not None and n < FILLER_FROM)
    ahead = [n for g in groups[gi + 1:] for _, (n, _u) in g if n is not None and n < FILLER_FROM][:span]

    def text(a, lead):
        if a not in POS:
            return ''
        return ''.join(A[(POS[n] - POS[a]) % 25] for n in lead + ahead if n in POS)

    keep = text(a_num, [real]) if a_num is not None else ''
    switch = text(real, [])
    sk = _MODEL.per_char(lm.norm(keep, 'modern')) if len(keep) >= 4 else -99
    ss = _MODEL.per_char(lm.norm(switch, 'modern')) if len(switch) >= 4 else -99
    return ss > sk


# (cipher type, reading) for every token, for docs/_validate.py. A ring token's type is number@setting,
# so that one fixed key covers the whole text; C's types are its table numbers.
PAIRS = []


def decode_letter(lines):
    """lines of one letter in order; groups may run across line ends."""
    stream = []  # (line index, token)
    for li, ln in enumerate(lines):
        toks = tokens(ln['L'])
        # a line that opens with an indicator group: the line end before it is a group break
        head = []
        for t in toks:
            if t == '-':
                break
            head.append(t[0])
        if head and is_indicator(head) and stream and stream[-1][1] != '-':
            stream.append((li, '-'))
        for t in toks:
            stream.append((li, t))
        # a line that closes with an indicator group (often cut at the page edge): break after it
        tail = []
        for t in reversed(toks):
            if t == '-':
                break
            tail.append(t[0])
        if tail and '-' in toks and is_indicator(tail):
            stream.append((li, '-'))
    # split into dash groups, keeping line indices
    groups, cur = [], []
    for li, t in stream:
        if t == '-':
            if cur:
                groups.append(cur)
            cur = []
        else:
            cur.append((li, t))
    if cur:
        groups.append(cur)
    out = collections.defaultdict(list)
    a_num = START.get(letter_of(lines[0]['page']))
    indicators = []
    table = TABLES.get(letter_of(lines[0]['page']))
    for gi, g in enumerate(groups):
        nums = [t[0] for _, t in g]
        if table:
            # a fixed substitution table: no indicators, fillers from TABLE_FILLER_FROM up
            word = collections.defaultdict(str)
            for li, (n, unsure) in g:
                if n is None:
                    word[li] += '?'
                    PAIRS.append(('?', '?'))
                elif n < TABLE_FILLER_FROM:
                    word[li] += table.get(n, f'[{n}]') + ('?' if unsure else '')
                    PAIRS.append((f'C{n}', table.get(n, '?')))
                else:
                    PAIRS.append((f'C{n}', '-'))
            for li in sorted(word):
                out[li].append(word[li])
            continue
        if is_candidate(nums) and (a_num is None or lm_prefers_switch(groups, gi, a_num)):
            a_num = next(n for n in nums if n is not None and n < FILLER_FROM)
            a_num = CORRECTED.get((lines[g[0][0]]['page'], lines[g[0][0]]['line']), a_num)
            indicators.append((lines[g[0][0]]['page'], lines[g[0][0]]['line'], nums, a_num))
            for li, _ in g[:1]:
                out[li].append('|')
            PAIRS.extend((f'i{n}', '?') for n in nums)
            continue
        if len(g) == 1 and nums[0] is not None and nums[0] >= FILLER_FROM and (
                (gi + 1 < len(groups) and is_candidate([t[0] for _, t in groups[gi + 1]]))
                or (gi and is_candidate([t[0] for _, t in groups[gi - 1]]))):
            PAIRS.append((f'i{nums[0]}', '?'))
            continue    # a filler of the neighbouring indicator, split from it at a line end
        if len(g) == 1 and nums[0] is not None and not (
                nums[0] in POS and a_num in POS and A[(POS[nums[0]] - POS[a_num]) % 25] == 'a'):
            # a lone number between dashes is a numeral in clear (regiments, dates, counts),
            # unless it deciphers to the word 'a'
            out[g[0][0]].append(f'<{nums[0]}>')
            PAIRS.append((f'#{nums[0]}', '?'))
            continue
        word = collections.defaultdict(str)
        for li, (n, unsure) in g:
            if n is None:
                word[li] += '?'
                PAIRS.append(('?', '?'))
            elif n >= FILLER_FROM:
                PAIRS.append((f'f{n}', '-'))
                continue
            elif a_num is None or n not in POS or a_num not in POS:
                word[li] += f'[{n}]'
                PAIRS.append((f'{n}@{a_num}', '?'))
            else:
                word[li] += A[(POS[n] - POS[a_num]) % 25] + ('?' if unsure else '')
                PAIRS.append((f'{n}@{a_num}', A[(POS[n] - POS[a_num]) % 25]))
        for li in sorted(word):
            out[li].append(word[li])
    return {li: ' '.join(w) for li, w in out.items()}, indicators


WINDOW = 24
WINDOW_SENSE = -3.3


def window_measure(by_letter):
    """Share of deciphered letters that sit in English: a letter counts when the best 24-letter window
    covering it scores at least WINDOW_SENSE. Flagged spans go to unread_spans.txt for review."""
    model = lm.load('en-modern', spaces=False)
    with open(os.path.join(HERE, 'unread_spans.txt'), 'w', encoding='utf8') as f:
        for let, lns in by_letter.items():
            dec, _ = decode_letter(lns)
            text = ''.join(c for li in sorted(dec) for c in dec[li] if c in A)
            n = len(text)
            best = [-99.0] * n
            for i in range(max(1, n - WINDOW + 1)):
                sc = model.per_char(lm.norm(text[i:i + WINDOW], 'modern'))
                for j in range(i, min(n, i + WINDOW)):
                    best[j] = max(best[j], sc)
            ok = sum(b >= WINDOW_SENSE for b in best)
            print(f'{let}: letters {n}, in sense windows {ok} = {ok / max(n, 1):.1%}')
            span = ''
            for c, b in zip(text, best):
                if b < WINDOW_SENSE:
                    span += c
                elif span:
                    f.write(f'{let}: {span}\n')
                    span = ''
            if span:
                f.write(f'{let}: {span}\n')


def main():
    lines = load(sorted(glob.glob(os.path.join(HERE, 'transcription', 'p*.txt'))))
    by_letter = collections.defaultdict(list)
    for ln in lines:
        by_letter[letter_of(ln['page'])].append(ln)
    stat = collections.Counter()
    model = lm.load('en-modern', spaces=False)
    with open(os.path.join(HERE, 'decoded.txt'), 'w', encoding='utf8') as f:
        for let, lns in by_letter.items():
            dec, inds = decode_letter(lns)
            f.write(f'===== {let}\nindicators: ' + '; '.join(f'p{p} L{l:02d} {g} -> a={a}' for p, l, g, a in inds) + '\n\n')
            for li, ln in enumerate(lns):
                d = dec.get(li, '')
                il = [('i' if c == 'j' else c) for c in ln['I'].lower() if c.isalpha()]
                dl = [c for c in d if c.isalpha()]
                pairs = align(dl, il)
                ok = sum(x == y for x, y in pairs)
                for key in (ln['page'], let):
                    stat[key, 'a'] += ok
                    stat[key, 't'] += max(len(dl), len(il))
                x = lm.norm(''.join(dl), 'modern')
                sc = model.per_char(x) if len(x) >= 4 else 0.0
                for key in (ln['page'], let):
                    stat[key, 'tok'] += len(dl)
                    stat[key, 'sense'] += len(dl) if sc >= SENSE else 0
                flag = '' if sc >= SENSE else '   <-- no sense'
                f.write(f"p{ln['page']} L{ln['line']:02d}  lm={sc:.2f}{flag}\n  L | {ln['L']}\n  I | {ln['I']}\n  D | {d}\n")
            f.write('\n')
    window_measure(by_letter)
    del PAIRS[:]
    for lns in by_letter.values():
        decode_letter(lns)
    with open(os.path.join(HERE, 'validation.tsv'), 'w', encoding='utf8') as f:
        f.write('# model: en-modern\n# source: decode.py over transcription/ (A, B: type = number@setting; C: table number)\n')
        f.write('# note: indicator groups and numerals in clear are left unread (?); fillers are nulls (-)\n')
        for t, r in PAIRS:
            f.write(f'{t}\t{r}\n')
    for k in sorted({ln['page'] for ln in lines}) + list(by_letter):
        print(f"{k}: agreement {stat[k, 'a']}/{stat[k, 't']} = {stat[k, 'a'] / max(stat[k, 't'], 1):.1%}"
              f"   letters in sense lines {stat[k, 'sense']}/{stat[k, 'tok']} = {stat[k, 'sense'] / max(stat[k, 'tok'], 1):.1%}")


if __name__ == '__main__':
    main()
