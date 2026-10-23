"""Match each 6960 cipher sheet to the Kiewning 1897 number that prints its text (reread batch b01).

For each record, every 9-letter window of the decode that contains no unknown group is looked up in the letters of
the edition (early-modern normalisation, no spaces); hits are mapped to the edition's line and its document number
(the last 'Nr. NNN:' running head above the line). Prints, per record, the numbers with most hits and the hit lines.
"""
import collections, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import reread_b01_decode as D
from lang import lm

ED = os.path.join(HERE, 'ed', 'pallotto_bd2_1629.txt')
W = 9

def edition_index():
    lines = open(ED, encoding='utf-8').read().split('\n')
    letters = []; owner = []; nr = None; numof = []
    for i, ln in enumerate(lines):
        m = re.match(r'^\s*Nr\.\s*(\d+)', ln)
        if m: nr = int(m.group(1))
        m = re.match(r'^\s*(?:\d{4}\s+)?(\d{2,3})\s?\.\s*Pa.{1,4}otto an Bar', ln)
        if m: nr = int(m.group(1))
        s = lm.norm(ln, 'early', False)
        letters.append(s); owner.extend([i] * len(s)); numof.append(nr)
    text = ''.join(letters)
    idx = collections.defaultdict(list)
    for p in range(len(text) - W + 1):
        idx[text[p:p + W]].append(p)
    return lines, text, owner, numof, idx

def doc_strings(rec):
    doc = D.decode_doc(rec)
    out = []
    for kind, val in doc:
        if kind != 'cipher': continue
        cur = ''
        for k, code, t in val:
            if k in ('l', 'w'):
                cur += D.letters(t)
            elif k == 'null':
                continue
            else:
                if cur: out.append(cur)
                cur = ''
        if cur: out.append(cur)
    return out

if __name__ == '__main__':
    lines, text, owner, numof, idx = edition_index()
    recs = sys.argv[1:] or [f[:-4] for f in sorted(os.listdir(os.path.join(HERE, 'decode')))]
    for r in recs:
        hits = collections.Counter(); where = collections.defaultdict(set); nwin = 0
        for s in doc_strings(r):
            for p in range(len(s) - W + 1):
                nwin += 1
                ps = idx.get(s[p:p + W], [])
                if 0 < len(ps) <= 3:
                    for q in ps:
                        ln = owner[q]; hits[numof[ln]] += 1; where[numof[ln]].add(ln)
        top = hits.most_common(4)
        print(r, 'windows', nwin, 'top', top)
        for nr, c in top[:2]:
            ls = sorted(where[nr])
            print('   Nr', nr, 'lines', ls[0] + 1, '-', ls[-1] + 1, 'n', len(ls))
