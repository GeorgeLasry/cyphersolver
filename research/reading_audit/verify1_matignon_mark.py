"""Verification pass (22 Oct 2026), matignon1586: bracket the words of the readings that the figures do not carry,
found with verify1_matignon_align.py and checked by hand against the line's figures and letter sets.
Each edit is a phrase with the target word in {}; the word becomes [word] (supplied) or [?word] (partly carried).
Each phrase must match exactly once (across line breaks).

    python research/reading_audit/verify1_matignon_mark.py
"""
import pathlib
import re

T = pathlib.Path(__file__).resolve().parents[2] / 'targets' / 'matignon1586' / 'texts'

# (file, phrase, kind)  kind: 's' = supplied [w], 'p' = partly carried [?w]
EDITS = [
    # f. 110 l. 17: o o ? H m dd = e-[i/a][i/a][illegible]-c-t-s: the ff is not carried
    ('reading_f110.md', 'de meilleurs {effects}, qu\'il', 'p'),
    ('reading_f110_en.md', 'has not had better {results}, that', 'p'),
    # f. 124v l. 8-9: 17 B t | y t 7 E2 | 12 = car ie ueoi il: no figure for qu'
    ('reading_f124.md', 'veoi {qu\'il} n\'y a ordre', 'p'),
    ('reading_f124_en.md', 'see {that} there is no order', 'p'),
    # f. 124v l. 19: 14 qs | E2 E2 | tm 3 = (Pas)ques i i me: the e of je is not carried
    ('reading_f124.md', 'Pasques, {je} me suis', 'p'),
    ('reading_f124_en.md', 'Easter, {I} have resolved', 'p'),
    # f. 124v l. 19-20: w | he x L = d l e r: the a and one l of d'aller are not carried
    ('reading_f124.md', 'résolu [l. 20] {d\'aller} attacquer', 'p'),
    ('reading_f124_en.md', '[l. 20] to {go} and attack', 'p'),
    # f. 124v l. 27: y x v th | 8 s x fe t = gens guere: no figure for de
    ('reading_f124.md', 'gens {de} guerre [l. 28] dedans', 's'),
]

# (file, old phrase, new phrase): a word the figures give otherwise
REPLACE = [
    # f. 110 l. 24-25: L ao 3 e h | H 7 6 8 ff 7 3 qu m e B = faire congnoistre; no figures for the re- of recongnoistre
    ('reading_f110.md', 'faire recongnoistre que', 'faire congnoistre que'),
    ('reading_f110_en.md', 'make it recognised that', 'make it known that'),
]


def replace():
    for fn, old, new in REPLACE:
        f = T / fn
        s = f.read_text(encoding='utf8')
        if new in s and old not in s:
            print('already applied:', fn, new); continue
        assert s.count(old) == 1, (fn, old)
        f.write_text(s.replace(old, new), encoding='utf8', newline='')
        print(fn, old, '->', new)


def apply():
    n_all = 0
    for fn, phrase, kind in EDITS:
        f = T / fn
        s = f.read_text(encoding='utf8')
        pat, n = '', 0
        for tok in re.split(r'(\{[^}]*\}|\s+)', phrase):
            if not tok:
                continue
            if tok.isspace():
                pat += r'\s+'
            elif tok.startswith('{'):
                pat += '(' + re.escape(tok[1:-1]) + ')'; n += 1
            else:
                pat += re.escape(tok)
        ms = list(re.finditer(pat, s))
        if not ms:
            print('already applied or not found:', fn, phrase)
            continue
        assert len(ms) == 1, (fn, phrase, len(ms))
        m = ms[0]
        out, last = [], m.start()
        for g in range(1, n + 1):
            w = m.group(g)
            out.append(s[last:m.start(g)] + ('[' + w + ']' if kind == 's' else '[?' + w + ']'))
            last = m.end(g)
        s = s[:m.start()] + ''.join(out) + s[last:]
        f.write_text(s, encoding='utf8', newline='')
        n_all += n
        print(fn, phrase, kind)
    return n_all


if __name__ == '__main__':
    print(apply())
    replace()
