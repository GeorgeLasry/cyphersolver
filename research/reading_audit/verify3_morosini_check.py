"""VERIFY_BRIEF pass 3, morosini1588: second opinion on each word verify3_morosini_diag.py flags.

    PYTHONUTF8=1 python research/reading_audit/verify3_morosini_check.py <diag.txt> [...]

For each flagged word, the figures shown around it (dots and braces dropped, so a spurious dot or a left-over group
counts) are searched for the whole word spelt in Meister's homophones, null 8 allowed between letters. EXACT: the
figures spell the word (the aligner gave a figure to a neighbour); else the word with each uncarried letter dropped is
tried (DROP: the figures spell the word without those letters, i.e. the letters are supplied).
"""
import os, re, sys, unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import reread_b00_decode as D  # noqa: E402

CODES = {}
for pt, cs in D.LET.items():
    CODES[pt] = cs.split()


def nrm(s):
    s = unicodedata.normalize('NFD', s.lower())
    s = ''.join(c for c in s if unicodedata.category(c) != 'Mn')
    return s.replace('v', 'u').replace('j', 'i').replace('y', 'i')


def word_re(w):
    parts, i = [], 0
    while i < len(w):
        opts = []
        for pt, cs in CODES.items():
            if w.startswith(pt, i):
                opts.append((pt, cs))
        # prefer allowing every unit that matches here: build alternation over (unit, rest) is costly; use letters,
        # plus multi-letter units as alternatives for the same span
        single = [cs for pt, cs in opts if len(pt) == 1]
        if w[i] == 'q':
            single = [CODES['qu']]
            parts.append('(?:' + '|'.join(CODES['qu']) + ')')
            i += 2
            continue
        if not single:
            return None
        parts.append('(?:' + '|'.join(single[0]) + ')')
        i += 1
    return '8?'.join(parts)


def check(word, shown, figs):
    w = nrm(re.sub(r'\[[^\]]*\]', '', word))
    w = re.sub(r'[^a-z]', '', w)
    digits = re.sub(r'[^0-9]', '', figs)
    rx = word_re(w)
    if rx and re.search(rx, digits):
        return 'EXACT'
    # drop the uncarried letters (upper case in `shown`)
    kept = ''.join(c for c in shown if not c.isupper()).lower()
    kept = re.sub(r'[^a-z]', '', nrm(kept))
    rx2 = word_re(kept) if kept else None
    if rx2 and re.search(rx2, digits):
        return 'DROP'
    return 'NONE'


def main():
    for p in sys.argv[1:]:
        for line in open(p, encoding='utf-8'):
            m = re.match(r'(\w+)\s+(R\d+)\s+(\S+)\s+(\S+)\s+(.+?)\s+(\S+)\s+::(.*?)«(.*)»', line.rstrip())
            if not m:
                continue
            verdict, rec, pg, loc, word, shown, figs, ctx = m.groups()
            print(f'{check(word, shown, figs):5s} {verdict:7s} {rec} {loc:10s} {word:16s} {shown:16s} «{ctx}»')


if __name__ == '__main__':
    main()
