"""v5 (b): list the words the plain word list does not know, per failing sentence, after v2_score's hole marking.

    python research/reading_audit/v5b_unk.py <file> <lang> [--all]

Prints each sentence that fails the plain measure with its unknown words in <<...>>, then a count of the unknown
words over the whole body (names, abbreviations and period spellings stand out at the top).
"""
import collections, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import v2_score as v
cr = v.cr

f, lang = sys.argv[1], sys.argv[2]
b = v.holes(v.body_of(pathlib.Path(f).read_text(encoding='utf8')))
lex = cr.lexicon(lang)
text = cr.CODE.sub(' CODEWORD ', cr.clean_text(b))
c = collections.Counter()
nf = 0
for s in cr.sentences(text):
    ws = [(w, g) for tok in s for w, g in cr.words_of(tok)]
    unk = [w for w, g in ws if g or (w not in lex and w != 'codeword')]
    c.update(w for w, g in ws if not g and w not in lex and w != 'codeword')
    bad = len(unk) > max(1, len(ws) // 10)
    if bad or '--all' in sys.argv:
        nf += bad
        print(('FAIL ' if bad else 'ok   ') + f'{len(unk)}/{len(ws)}: ' + ' '.join(
            (f'<<{w}>>' if (g or (w not in lex and w != 'codeword')) else w) for w, g in ws))
print('fail', nf, '| unknown:', ', '.join(f'{w}{"x"+str(n) if n > 1 else ""}' for w, n in c.most_common(60)))
