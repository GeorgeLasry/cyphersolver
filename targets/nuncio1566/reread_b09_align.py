"""Align a reading (contemporary decipherment or hand reading) with the figures of one cipher page.

Reread batch "aless" (22 Oct 2026); copied for nuncio1566 as reread batch b09 (22 Oct 2026), with the code values
the R87 decipherment (f. 251r) and the R88/R89/R90 copies attest added to ALIAS, and the dotted group 3 0^. followed by 9 read
as "qua". For each figure the key gives two letters (decrypt.POLY), 0 is a null and X0Y0
groups are nomenclator codes. The script finds the cheapest alignment of the reading's letters with the figures and
prints it word by word, marking every place where the reading and the figures disagree, so that each disagreement
can be looked at on the image.

usage: python reread_aless_align.py <transcription.txt> <image name> <reading.txt> [--codes]

The reading file is plain text; words in [brackets] are notes and are skipped, '|' marks a line end (ignored).
Letters h and q are not in the key: an h is skipped free, a q may be skipped at a small cost (q-words are codes).
Unknown X0Y0 groups may stand for a whole word of the reading (cost 0.3); --codes lists those word assignments.
"""
import os, re, sys, unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import importlib.util
spec = importlib.util.spec_from_file_location('dec', os.path.join(HERE, 'decrypt.py'))
src = open(os.path.join(HERE, 'decrypt.py'), encoding='utf-8').read()
# reuse parse(), POLY and NOM without loading the language model
ns = {"__file__": os.path.join(HERE, "decrypt.py")}
exec(compile(src.split("M = lm.load")[0].replace('from lang import lm', ''), 'decrypt.py', 'exec'), ns)
exec(compile('import re\n' + src[src.index('def parse'):src.index('def decode')], 'decrypt.py', 'exec'), ns)
POLY, NOM, parse = ns['POLY'], ns['NOM'], ns['parse']


# abbreviations the contemporary decipherer wrote for a code word
ALIAS = {'1010': ['ns'], '3010': ['sm', 'suamaesta'], '4030': ['sm'], '1020': ['ss'], '4010': ['ss'], '9010': ['ss'],
         '1090': ['us'], '3060': ['mente'],
         # values first attested by the contemporary decipherments (reread batch aless, 22 Oct 2026)
         '1040': ['lettere'], '3020': ['quando'], '4040': ['milano', 'come'], '6050': ['imbasciatore', 'imbasciatoredifrancia'],
         '7070': ['l', 'il'], '2050': ['spagna'], '2090': ['chi'], '8090': ['hauere']}
# nuncio1566, reread batch b09 (22 Oct 2026): values attested in R85-R90 by the R87 decipherment (f. 251r), the clear
# copy of the R90 passage (f. 302r) and the sense of the copies R88/R89
ALIAS.update({'8010': ['reginadifrancia', 'regina'], '1020': ['ss', 'essere'], '8030': ['religione'],
              '8080': ['heretici'], '1040': ['lettere', 'lettera'], '4010': ['ss', 'suamaesta', 'sm'], '8070': ['ugonotta', 'ugonotto'], '6040': ['fine'],
              '4040': ['milano', 'come'], '7040': ['morviglieri', 'morvilliers']})
# demonstratives: Lasry's glosses for these codes are approximate (6090 'quel' is 'questa' in a decipherment)
QW = {'quel', 'quello', 'quella', 'quelli', 'quelle', 'questo', 'questa', 'questi', 'queste'}


def norm(s):
    s = unicodedata.normalize('NFD', s.lower())
    s = ''.join(c for c in s if unicodedata.category(c) != 'Mn')
    return s.replace('v', 'u').replace('j', 'i').replace('y', 'i').replace('k', 'c').replace('x', 's')


def words_of(reading):
    reading = re.sub(r'\[[^\]]*\]', ' ', reading)
    reading = reading.replace('|', ' ')
    out = []
    for w in re.findall(r"[A-Za-zÀ-ÿ']+", reading):
        for part in w.split("'"):
            if part:
                out.append(norm(part))
    return out


def align(items, words):
    tgt = ''.join(words)
    wstart = set()
    pos = 0
    for w in words:
        wstart.add(pos); pos += len(w)
    wend = {}
    pos = 0
    for w in words:
        wend[pos] = pos + len(w); pos += len(w)
    nomv = {k: [norm(v.replace(' ', ''))] for k, v in NOM.items()}
    for k, al in ALIAS.items():
        nomv.setdefault(k, []).extend(al)
    n, m = len(items), len(tgt)
    INF = 1e9
    cost = [[INF] * (m + 1) for _ in range(n + 1)]
    back = [[None] * (m + 1) for _ in range(n + 1)]
    cost[0][0] = 0.0
    for i in range(n + 1):
        for j in range(m + 1):
            c = cost[i][j]
            if c >= INF:
                continue

            def relax(i2, j2, add, why):
                if i2 <= n and j2 <= m and c + add < cost[i2][j2]:
                    cost[i2][j2] = c + add
                    back[i2][j2] = (i, j, why)
            if j < m:
                ch = tgt[j]
                if ch == 'h':
                    relax(i, j + 1, 0.0, 'h')
                elif ch == 'q':
                    relax(i, j + 1, 0.4, 'q')
                relax(i, j + 1, 1.0, 'missing')          # reading letter with no figure
            if i < n:
                it = items[i]
                if isinstance(it, tuple):
                    g = it[1]
                    # a dotted zero is z; parse() pairs it with the figure before it (7 0^. = r z)
                    if len(g) == 2 and g[1] == '0' and g[0] in POLY and j + 1 < m and tgt[j] in POLY[g[0]] \
                            and tgt[j + 1] == 'z':
                        relax(i + 1, j + 2, 0.0, 'dot:z')
                    if g == '00' and tgt.startswith('z', j):
                        relax(i + 1, j + 1, 0.1, 'dot:z')
                    if g == '00' and tgt.startswith('et', j):
                        relax(i + 1, j + 2, -0.2, 'dot:et')
                    # 3 0^. 9: the dotted group 30 and the figure 9 together are "qua" (R87 249r, R85)
                    if g == '30' and i + 1 < n and items[i + 1] == '9' and tgt.startswith('qua', j):
                        relax(i + 2, j + 3, -0.3, 'dot:qua')
                    if g == '39' and tgt.startswith('qua', j):
                        relax(i + 1, j + 3, 0.0, 'dot:qua')
                    relax(i + 1, j, 0.2, 'dot:' + g)
                elif it == '0':
                    relax(i + 1, j, 0.0, 'null')
                elif it == '?':
                    relax(i + 1, j, 0.3, 'illeg')
                    if j < m:
                        relax(i + 1, j + 1, 0.3, 'illeg')
                else:
                    relax(i + 1, j, 1.0, 'extra')
                    if j < m:
                        ok = tgt[j] in POLY[it]
                        relax(i + 1, j + 1, 0.0 if ok else 1.0, 'ok' if ok else 'bad')
                        # the clerk writes a doubled letter once (pasati, alegati)
                        if ok and j + 1 < m and tgt[j + 1] == tgt[j]:
                            relax(i + 1, j + 2, 0.05, 'dbl')
                    seg = items[i:i + 4]
                    if len(seg) == 4 and all(isinstance(x, str) and x.isdigit() for x in seg):
                        code = ''.join(seg)
                        vs = nomv.get(code)
                        for v in vs or []:
                            if tgt.startswith(v, j):
                                relax(i + 4, j + len(v), -0.5, 'code:' + code)
                        if (vs is None or set(vs) & QW) and seg[1] == '0' and seg[3] == '0' and j in wend and tgt[j:wend[j]] in QW \
                                and tgt[j:wend[j]] not in (vs or []):
                            relax(i + 4, wend[j], 0.2, 'qcode:' + code)
                        if vs is None and seg[1] == '0' and seg[3] == '0' and seg[0] != '0' and seg[2] != '0' \
                                and j in wend:
                            relax(i + 4, wend[j], 0.3, 'newcode:' + code)
                    seg = items[i:i + 3]
                    if len(seg) == 3 and all(isinstance(x, str) and x.isdigit() for x in seg) and seg[1] == '0':
                        code = ''.join(seg)
                        if code == '309' and tgt.startswith('qua', j):
                            relax(i + 3, j + 3, -0.3, 'code:309')
                        for v in nomv.get(code + '0', []):
                            if tgt.startswith(v, j):
                                relax(i + 3, j + len(v), -0.3, 'code3:' + code + '0')
                    if it == '9' and tgt.startswith('con', j):
                        relax(i + 1, j + 3, 0.0, 'con9')
    # backtrack
    path = []
    i, j = n, m
    while (i, j) != (0, 0):
        pi, pj, why = back[i][j]
        path.append((pi, i, pj, j, why))
        i, j = pi, pj
    path.reverse()
    return cost[n][m], path, tgt


def show(items, words, path, tgt, codes=False):
    # map each target position to its word index
    widx = []
    for k, w in enumerate(words):
        widx += [k] * len(w)
    per_word = [[] for _ in words]
    bad_words = set()
    newcodes = []
    stray = []
    for pi, i, pj, j, why in path:
        fig = ''.join(x if isinstance(x, str) else x[1] + '.' for x in items[pi:i])
        if j > pj:
            k = widx[pj]
            per_word[k].append((fig, tgt[pj:j], why))
            if why in ('bad', 'missing'):
                bad_words.add(k)
            if why.startswith('newcode') or why.startswith('qcode') or why == 'con9':
                newcodes.append((why, tgt[pj:j]))
        else:
            k = widx[pj] if pj < len(widx) else len(words) - 1
            if why == 'extra':
                bad_words.add(k)
                per_word[k].append((fig, '', why))
            elif why.startswith('dot'):
                per_word[k].append((fig, '', why))
            elif why == 'null':
                per_word[k].append(('0', '', 'null'))
    lines = []
    for k, w in enumerate(words):
        mark = '!!' if k in bad_words else '  '
        segs = ' '.join(('%s=%s' % (f, t) if t else ('(%s)' % f if why != 'null' else '0'))
                        + ('*' if why in ('bad', 'missing', 'extra') else '')
                        for f, t, why in per_word[k])
        lines.append('%s %-18s %s' % (mark, w, segs))
    return lines, bad_words, newcodes


def main():
    tr, img, rd = sys.argv[1:4]
    pages = dict(parse(tr))
    items = pages[img]
    text = open(rd, encoding='utf-8').read()
    if rd.endswith('.md'):
        # only the reading itself: the lines under '## Reading' up to the next heading
        text = text.split('## Reading', 1)[1].split(chr(10) + '## ', 1)[0]
    words = words_of(text)
    c, path, tgt = align(items, words)
    lines, bad, newcodes = show(items, words, path, tgt)
    print('\n'.join(lines))
    print('# cost %.1f; %d words, %d disagree (%.1f%%)' % (c, len(words), len(bad), 100.0 * len(bad) / max(1, len(words))))
    if '--codes' in sys.argv or newcodes:
        for code, w in newcodes:
            print('# %s = %s' % (code, w))


if __name__ == '__main__':
    main()
