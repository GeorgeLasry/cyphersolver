"""r2b: restore the writer's spelling in chomentowski1713 R7476_reading.txt.
For each page, the letter stream the figures carry (gloss value, else syllabary value; clear words as written, from
R7476.txt with the pass-5/6/7 overrides below) is aligned (difflib, letters folded: diacritics off, y/j -> i) with the
modernised pass-3 reading. Each reading word is re-spelt from the stream letters aligned to it; a letter of the modern
word that no figure carries is printed in [brackets] (supplied or emended). Holes and (?) marks are carried over.
Prints the restored body (python r2b_chom_restore.py > draft) for review by hand."""
import re, sys, difflib, unicodedata, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from r2b_chom_stream import parse
ROOT = pathlib.Path(__file__).resolve().parents[2]

# pass 5-7 overrides: (page, line, code position among the line's codes) -> value
OVR = {(31, 19, 9): 'na', (31, 24, 13): 'się', (31, 26, 5): 'Porty', (31, 28, 2): 'Porta', (31, 29, 11): 'e',
       (31, 33, 13): 'Porta', (31, 36, 13): 'na', (32, 12, 4): 'na', (32, 12, 5): 'd', (32, 12, 0): 'lw',
       (32, 12, 1): 'wy', (32, 16, 8): 'p', (32, 18, 8): 'le', (32, 19, 0): 'te', (32, 21, 1): 'to', (32, 21, 6): 'nu',
       (32, 21, 8): 'ba', (32, 21, 5): 're', (32, 25, 3): 't', (32, 27, 3): 'le', (32, 28, 2): 'Choc', (32, 33, 11): 'u',
       (32, 35, 13): 'm', (33, 16, 1): 'x', (33, 21, 0): 'Pu', (33, 21, 1): 'Kanclerz', (33, 25, 4): 'mo',
       (32, 29, 4): 's', (32, 29, 5): 'z'}
FOLD = str.maketrans('ąęłżźćśńóyjÿ', 'aelzzcsnoiii')

def fold(s): return s.lower().translate(FOLD)

def value(G, K, key):
    if key in OVR: return OVR[key]
    g = G.strip('^')
    if g not in ('[?]', '-') and not g.startswith('['): return g
    k = re.sub(r'\[[^\]]*\]|\^', '', K)
    return '' if k in ('?',) else k

def stream(page):
    out = []          # list of (char, clear?)
    for l in parse():
        if l['page'] != page: continue
        G, K = list(l['G']), list(l['K'])
        if (page, l['line']) == (33, 25): del G[2]; del K[2]
        i = 0
        for c in l['C']:
            if c.startswith('"'):
                t = c.strip('"')
                if re.fullmatch(r'\[.*\]', t): continue
                out += [(ch, True) for ch in t] + [(' ', True)]
            else:
                v = value(G[i], K[i], (page, l['line'], i)); i += 1
                out += [(ch, False) for ch in v]
    return out

def restore(mod, st):
    s_chars = [c for c, _ in st if c.strip()]
    s = ''.join(fold(c) for c in s_chars)
    toks = re.findall(r'\S+', mod)
    # modern letters with token index
    m_chars, m_tok = [], []
    for ti, t in enumerate(toks):
        if t.startswith('[...') or t == '[...]': continue
        for ch in re.sub(r'\(\?\)|[^\w]', '', t):
            m_chars.append(ch); m_tok.append(ti)
    m = ''.join(fold(c) for c in m_chars)
    sm = difflib.SequenceMatcher(None, m, s, autojunk=False)
    rend = {}                                   # token index -> list of output pieces
    for op, a1, a2, b1, b2 in sm.get_opcodes():
        if op == 'equal':
            for k in range(a2 - a1): rend.setdefault(m_tok[a1 + k], []).append(s_chars[b1 + k])
        elif op == 'insert':                    # stream letters the modern reading drops: give them to the previous word
            ti = m_tok[a1 - 1] if a1 else m_tok[0]
            rend.setdefault(ti, []).append(''.join(s_chars[b1:b2]))
        elif op == 'delete':                    # modern letters no figure carries
            for k in range(a1, a2): rend.setdefault(m_tok[k], []).append('[' + m_chars[k] + ']')
        else:                                   # replace: figures' letters kept where same length, else both shown
            if a2 - a1 == b2 - b1:
                for k in range(a2 - a1):
                    rend.setdefault(m_tok[a1 + k], []).append(s_chars[b1 + k] if fold(s_chars[b1 + k]) == fold(m_chars[a1 + k]) else '{' + s_chars[b1 + k] + '>' + m_chars[a1 + k] + '}')
            else:
                rend.setdefault(m_tok[a1], []).append('{' + ''.join(s_chars[b1:b2]) + '>' + ''.join(m_chars[a1:a2]) + '}')
    out = []
    for ti, t in enumerate(toks):
        if ti not in rend: out.append(t); continue
        w = ''.join(rend[ti]).replace('][', '')
        pre = re.match(r'^[^\w\[]*', t).group(0); post = re.search(r'(\(\?\))?[^\w\]]*$', t).group(0)
        if t[:1].isupper() and w[:1].islower(): w = w[0].upper() + w[1:]
        out.append(pre + w + post)
    return ' '.join(out)

if __name__ == '__main__':
    body = (ROOT / 'targets/chomentowski1713/R7476_reading.txt').read_text(encoding='utf8').split('## Reading', 1)[1].split('## Notes')[0]
    pages = re.split(r'^p\. (\d+)\s*$', body, flags=re.M)
    for i in range(1, len(pages), 2):
        pg, txt = int(pages[i]), pages[i + 1]
        txt = txt.split('[Clear postscript')[0]
        print(f'p. {pg}'); print(restore(' '.join(txt.split()), stream(pg))); print()
