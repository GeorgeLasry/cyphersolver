"""Decode the coded sentences of Mountflorence to Madison, 18 March 1801.

The code is a one-part code: numbers rise with the alphabet, single letters sit at the head of their
letter's section, and words follow in alphabetical order. Usage:
    python decode.py            # the reading, line by line
    python decode.py check      # alphabetical-order check of the key
    python decode.py tsv        # write validation.tsv
"""
import re
import sys
from pathlib import Path

HERE = Path(__file__).parent

# value, grade (H/C/M/I as in README Conventions; here every value is I, recovered from the text),
# and how it was fixed. 'spell' = fixed by the four spelled names, cross-checked between them.
KEY = {
    207: ('A', 'spell: tuscAny, pArmA (x2)'),
    228: ('at', 'slot 207 A < 228 < 250; "secret Articles at Luneville"'),
    249: ('but', 'slot 228 < 249 < 250; "not Florida, but the ..."'),
    250: ('by', 'slot 249 but < 250 < 251 C; "given by France to Parma"'),
    251: ('C', 'spell: tusCany (251 on the frame; Founders prints 250)'),
    357: ('D', 'spell: Dupont'),
    377: ('E', 'spell: lunevillE (x2)'),
    432: ('Florida', 'slot 377 E < 432 < 434 France; "not Florida"'),
    434: ('France', 'slot 377 E < 434 < 460 I; occurs twice'),
    460: ('I', 'spell: lunevIlle'),
    475: ('L', 'spell: Luneville (x3)'),
    500: ('M', 'spell: parMa'),
    521: ('Mississippi', 'slot 500 M < 521 < 529 N; "the Mississippi with all its Dependencies"'),
    529: ('N', 'spell: dupoNt, luNeville, tuscaNy'),
    544: ('O', 'spell: dupOnt'),
    640: ('P', 'spell: duPont, Parma'),
    660: ('R', 'spell: paRma'),
    664: ('S', 'spell: tuScany'),
    666: ('secret', 'slot 664 S < 666 < 679 Spain; "some of the secret Articles"'),
    679: ('Spain', 'slot 664 S < 679 < 684 T; "Spain has ceded"'),
    684: ('T', 'spell: duponT, Tuscany'),
    688: ('the', 'slot 684 T < 688 < 719'),
    719: ('to', 'slot 688 the < 719 < 723 U; "ceded to France", "to Parma"'),
    723: ('U', 'spell: dUpont, lUneVille (U and V one letter), tUscany'),
    756: ('Y', 'spell: tuscanY'),
}
SINGLE = {k: v for k, v in KEY.items() if len(v[0]) == 1}


def lines():
    for raw in (HERE / 'ciphertext.txt').read_text(encoding='utf-8').splitlines():
        if raw.startswith('#') or not raw.strip():
            continue
        yield raw


def tokens(line):
    """Yield (kind, text, sep): kind 'clear' or 'code'; sep is the separator printed after a code group."""
    for m in re.finditer(r'\[([^\]]*)\]|(\d+)([.,]?)', line):
        if m.group(1) is not None:
            yield 'clear', m.group(1), ''
        else:
            yield 'code', m.group(2), m.group(3)


def reading(line):
    out, run = [], []

    def flush():
        if run:
            out.append(''.join(run).upper())
            run.clear()

    toks = list(tokens(line))
    for i, (kind, text, sep) in enumerate(toks):
        if kind == 'clear':
            flush()
            out.append(text)
            continue
        n = int(text)
        val = KEY[n][0] if n in KEY else f'[{n}]'
        # a run of single-letter groups spells a word
        nxt = toks[i + 1] if i + 1 < len(toks) else None
        if n in SINGLE:
            run.append(val)
            if sep == ',' or not (nxt and nxt[0] == 'code'):
                flush()
            continue
        flush()
        out.append(val)
    flush()
    return ' '.join(out)


def check():
    items = sorted(KEY.items())
    ok = True
    for (a, (va, _)), (b, (vb, _)) in zip(items, items[1:]):
        if va.lower() > vb.lower():
            print(f'ORDER BREAK: {a} {va} > {b} {vb}')
            ok = False
    print('alphabetical order holds for all', len(items), 'values' if ok else 'values: FAIL')


def tsv():
    rows = ['# model: en-modern', '# source: ciphertext.txt via decode.py',
            '# note: one-part code; a token is a code group, reading = its letter or word']
    for line in lines():
        toks = list(tokens(line))
        for i, (kind, text, sep) in enumerate(toks):
            if kind != 'code':
                continue
            n = int(text)
            v = KEY.get(n, ('?',))[0]
            rows.append(f'{n}\t{v.lower()}')
    (HERE / 'validation.tsv').write_text('\n'.join(rows) + '\n', encoding='utf-8')
    print('wrote validation.tsv,', len(rows) - 3, 'tokens')


if __name__ == '__main__':
    arg = sys.argv[1] if len(sys.argv) > 1 else ''
    if arg == 'check':
        check()
    elif arg == 'tsv':
        tsv()
    else:
        for line in lines():
            print(reading(line))
