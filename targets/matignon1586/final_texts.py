"""The merged Cipher-1 key applied to every document of the target: final measure and the full-text files.

key_cipher1.json = key_merged_union.json (merge_keys.py: the union of Brackx's eleven per-leaf keys) + 59 = argent
(the clear copy f. 157r: "prester icy de l'argent a rendre a Paris" where f. 154r has 59).

For each document (profile.json documents[].id) this decodes Brackx's transcription line by line with this project's
beam and 6-gram (brackx_validate.decode), scores it with measure.py's sense rule, runs the set-size-preserving
scrambled control (3 seeds), and writes texts/<doc>.txt: per manuscript line the figures and the decoded text cut
into words, unidentified code groups shown as [code], stretches outside a sense run in lower case between | |.
Leaves with a contemporary clear copy get the copy reading appended. Output final_texts.json.

  python final_texts.py
"""
import json, os, sys
sys.argv = [sys.argv[0]]
import brackx_validate as V
import measure as M
from solve import segment

HERE = V.HERE
B = V.B
K = json.load(open(os.path.join(HERE, 'key_merged_union.json'), encoding='utf-8'))
K['59'] = ['argent']
json.dump(K, open(os.path.join(HERE, 'key_cipher1.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
KEY = V.prep_key(K)

DOCS = [  # profile id, label, cipher files, copy files (kept as the reading of record), summary-free
    ('fr15571-f177', 'fr. 15571 f. 177r-v, Forget, 31 Dec 1585', ['f177r_cipher.txt', 'f177v_cipher.txt'], []),
    ('f110', 'fr. 15572 f. 110, Mayenne to Villeroy, Bellebourg, March 1586', ['f110_cipher.txt'], []),
    ('f123r', 'fr. 15572 f. 123r, Mayenne to the King, Marmande, March 1586', ['f123r_cipher.txt'], []),
    ('f123v', 'fr. 15572 f. 123v (same despatch)', ['f123v_cipher.txt'], []),
    ('f124r', 'fr. 15572 f. 124r (same despatch)', ['f124r_cipher.txt'], []),
    ('f124v', 'fr. 15572 f. 124v (same despatch)', ['f124v_cipher.txt'], []),
    ('f143r', 'fr. 15572 f. 143r, Mayenne to the King, April 1586', ['f143r_cipher.txt'], ['f155r_f143_corr.txt']),
    ('f143v', 'fr. 15572 f. 143v (same despatch)', ['f143v_cipher.txt'], []),
    ('f150r', 'fr. 15572 f. 149v-150r, Forget to Villeroy, April 1586', ['f150r_cipher.txt'], ['f155v_f150r.txt']),
    ('f150', 'fr. 15572 f. 150v (same letter)', ['f150v_cipher.txt'], ['f156_f150v_corr.txt']),
    ('f154', 'fr. 15572 f. 154r, Forget to Villeroy, April 1586', ['f154r_cipher.txt'], ['f157_f154r_corr.txt']),
    ('f154v', 'fr. 15572 f. 154v, two blocks (same letter)', ['f154vA_cipher.txt', 'f154vB_cipher.txt'], ['f157_f154v.txt']),
    ('f173', 'fr. 15572 f. 173, to the King, 1586', ['f173_cipher.txt'], []),
    ('f196', 'fr. 15572 f. 196, to the King, 1586 (first encipherment)', ['f196_cipher.txt'], []),
    ('f201', 'fr. 15572 f. 201, to the King, 1586 (the same despatch re-enciphered)', ['f201_cipher.txt'], []),
]


def render(res):
    text = ''.join(r['text'] for r in res)
    mask = M.sense_mask(text)
    out = []
    p = 0
    for i, r in enumerate(res, 1):
        seg = []
        q = p
        for t, L in zip(r['tokens'], r['lens']):
            s = text[q:q + L]
            if s == '+':
                seg.append(('code', t))
            else:
                seg.append(('txt', s, all(mask[q:q + L]) if L else True))
            q += L
        # join runs of text with the same sense flag, then cut into words
        words = []
        buf, flag = '', None
        for x in seg + [('end',)]:
            if x[0] == 'txt' and (flag is None or x[2] == flag):
                buf += x[1]; flag = x[2]
                continue
            if buf:
                w = segment(buf)
                words.append(w.upper() if flag else '|' + w + '|')
            buf, flag = '', None
            if x[0] == 'txt':
                buf, flag = x[1], x[2]
            elif x[0] == 'code':
                words.append('[' + x[1] + ']')
        out.append(f'{i:2d}  {" ".join(r["tokens"])}\n    {" ".join(words)}')
        p = q
    return '\n'.join(out)


def main():
    os.makedirs(os.path.join(HERE, 'texts'), exist_ok=True)
    rep = {}
    N = R = F = 0
    for doc, label, files, copies in DOCS:
        tag = 'fin_' + doc
        res = V.decode(files, KEY, tag)
        M.KEY = KEY
        n, read, *_ = M.score(res)
        fl = []
        for s in range(3):
            cr = V.decode(files, V.scramble(KEY, s), f'{tag}_s{s}')
            M.KEY = KEY
            fl.append(M.score(cr)[1] / n)
        floor = sum(fl) / 3
        N += n; R += read; F += floor * n
        rep[doc] = {'tokens': n, 'read': read, 'sense': round(read / n, 3), 'floor': round(floor, 3)}
        print(f'{doc:14s} {n:5d} {read:5d} {read / n:.3f} floor {floor:.3f}', flush=True)
        hdr = [f'# {label}: decryption with the merged Cipher-1 key (key_cipher1.json)',
               '# Transcription: Michael Brackx (issues #73, #77-#79, #83), brackx2026/. Decoded here with this',
               "# project's beam and period-French 6-gram (final_texts.py). Per manuscript line: the figures, then the",
               '# decode cut into words. UPPER CASE = inside a run of French (measure.py sense rule); |lower case| =',
               '# outside one (doubtful letters, unknown spellings, slips); [nn] = code group not identified.',
               f'# Measured: {read} of {n} tokens read as sense ({read / n:.1%}); scrambled-key floor {floor:.1%}.', '']
        body = render(res)
        tail = []
        for c in copies:
            tail += ['', '', f'# The contemporary clear copy (brackx2026/copies/{c}), as read by Michael Brackx:', '',
                     open(os.path.join(B, 'copies', c), encoding='utf-8').read()]
        open(os.path.join(HERE, 'texts', doc + '.txt'), 'w', encoding='utf-8').write('\n'.join(hdr) + body + '\n'.join(tail) + '\n')
    rep['total'] = {'tokens': N, 'read': R, 'sense': round(R / N, 4), 'floor': round(F / N, 4),
                    'corrected': round((R / N - F / N) / (1 - F / N), 4)}
    print(rep['total'])
    json.dump(rep, open(os.path.join(HERE, 'final_texts.json'), 'w', encoding='utf-8'), indent=1)


if __name__ == '__main__':
    main()
