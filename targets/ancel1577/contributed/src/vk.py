# Vulcob/Ancel cipher (Colbert 398): token key, decoder and shuffled-key control.
# Transcription format (data/transcription/*.txt): one cipher line per row, "LINE_ID<TAB>tokens".
#   tokens are space-separated symbol names (see TOKENS below); "|" = word gap as written;
#   {word} = plain-letter group (null or nomenclature), kept as is; "?" = unreadable symbol;
#   a token may carry "?" suffix (e.g. "9?") = uncertain reading.
# Usage:
#   python3 src/vk.py decode data/transcription/p539.txt
#   python3 src/vk.py control data/transcription/p539.txt [N] [--table-only]
import sys, re, math, random, collections

# symbol name -> plaintext. src: T = Tomokiyo's table (key.tsv), C = added from calibration on
# p.33 (contemporary marginal decipherment), I = inferred from context in this work.
TOKENS = {
    '4': ('a', 'T'), '7': ('a', 'T'), 'al': ('a', 'T'),
    'o': ('b', 'T'),
    '8': ('c', 'T'), '6': ('c', 'T'),
    '9': ('d', 'T'),            # same shape is also used for l (Tomokiyo's L9); use 'q' when it reads l
    'T': ('d', 'T'),
    'w': ('e', 'T'), 'pi': ('e', 'T'),
    'p': ('f', 'T'),
    'g': ('g', 'T'),
    'h': ('h', 'T'),
    'i': ('i', 'T'), 'mu': ('i', 'T'),
    'ne': ('l', 'T'), 'q': ('l', 'T'), 'qx': ('l', 'T'),
    '3': ('m', 'T'), 'phi': ('m', 'T'),
    'dl': ('n', 'T'), 'fl': ('n', 'T'),
    'oc': ('o', 'T'), 'lz': ('o', 'T'), 'oo': ('o', 'T'),
    'P': ('p', 'T'),
    'qa': ('q', 'T'),
    'b': ('r', 'T'), 'z': ('r', 'C'),
    'S': ('s', 'T'), 'n': ('s', 'T'),
    'D': ('t', 'T'), 'di': ('t', 'T'), 't4': ('t', 'T'),
    'x': ('u', 'T'), 'up': ('u', 'T'), 'uw': ('u', 'T'), 'bow': ('u', 'T'),
    '2': ('y', 'T'), '-': ('y', 'T'),
    'th': ('z', 'T'),
    # double letters
    'hash': ('ss', 'T'), 'box': ('tt', 'T'), 'Ldot': ('pp', 'T'), 'at': ('rr', 'T'),
    'L': ('g', 'C'),   # flat L-like sign: g (seigneur, Borgia, gendarmerie, magesté on p.561); NOT Tomokiyo's pp (Λ with dot = Ldot)
    'm': ('uu', 'C'), 'dq': ('mm', 'T'), 'qq': ('nn', 'T'), 'M': ('cc', 'T'),
    'ffx': ('ff', 'T'),   # Tomokiyo's 'ff?' (q with crossbar); confirmed in affaire/affection/officier (p.562)
    # nomenclature written as letter groups / signs
    'ucl': ('est', 'T'), 'ros': ('pour', 'T'), 'plus': ('que', 'T'), 'guod': ('guerre', 'T'),
    'VM': ('Vostre Majeste', 'T'),
    'c': ('', 'C'),   # lone plain 'c' used as a null (p.33 l.6, p.539 l.4)
}


def load(path):
    rows = []
    for ln in open(path, encoding='utf-8'):
        ln = ln.rstrip('\n')
        if not ln.strip() or ln.startswith('#'):
            continue
        lid, _, toks = ln.partition('\t')
        rows.append((lid, toks.split()))
    return rows


def val(tok, key):
    if tok == '|':
        return ' '
    if tok.startswith('{') and tok.endswith('}'):
        return '{' + tok[1:-1] + '}'
    unsure = tok.endswith('?') and len(tok) > 1
    t = tok[:-1] if unsure else tok
    if t == '?':
        return '·'
    if t not in key:
        return '<' + t + '>'
    v = key[t]
    if len(v) > 1:
        v = '[' + v + ']'
    return v.upper() if unsure else v


def decode(rows, key):
    return [(lid, ''.join(val(t, key) for t in toks)) for lid, toks in rows]


def build_model():
    from wordfreq import top_n_list, word_frequency
    tri = collections.Counter(); bi = collections.Counter()
    for w in top_n_list('fr', 50000):
        w2 = ''.join(c for c in w.lower() if c.isalpha())
        w2 = w2.replace('œ', 'oe').translate(str.maketrans('éèêëàâäîïôöùûüç', 'eeeeaaaiioouuuc'))
        w2 = w2.replace('j', 'i').replace('v', 'u')
        if not w2:
            continue
        f = word_frequency(w, 'fr')
        s = '^' + w2 + '$'
        for i in range(len(s) - 2):
            tri[s[i:i + 3]] += f; bi[s[i:i + 2]] += f
    def lp(a, b, c):
        return math.log((tri[a + b + c] + 1e-7) / (bi[a + b] + 1e-7 * 24))
    return lp


def runs(rows, key):
    # maximal runs of single-letter symbols (broken by |, codes, {words}, unknowns)
    out = []
    for _, toks in rows:
        cur = []
        for tok in toks:
            t = tok[:-1] if tok.endswith('?') and len(tok) > 1 else tok
            if t in key and len(key[t]) == 1:
                cur.append(t); continue
            if cur:
                out.append(cur); cur = []
        if cur:
            out.append(cur)
    return out


def score(rs, key, lp):
    tot = n = 0
    for r in rs:
        s = '^' + ''.join(key[k] for k in r) + '$'
        for i in range(len(s) - 2):
            tot += lp(s[i], s[i + 1], s[i + 2]); n += 1
    return tot / n


if __name__ == '__main__':
    cmd, path = sys.argv[1], sys.argv[2]
    table_only = '--table-only' in sys.argv
    key = {k: v for k, (v, src) in TOKENS.items() if not (table_only and src != 'T')}
    rows = load(path)
    if cmd == 'decode':
        for lid, s in decode(rows, key):
            print(f'{lid}\t{s}')
    elif cmd == 'control':
        args = [a for a in sys.argv[3:] if not a.startswith('--')]
        N = int(args[0]) if args else 1000
        lp = build_model()
        rs = runs(rows, key)
        letters = [k for k in key if len(key[k]) == 1]
        used = {t for r in rs for t in r}
        real = score(rs, key, lp)
        random.seed(1)
        sh = []
        for _ in range(N):
            vals = [key[k] for k in letters]; random.shuffle(vals)
            k2 = dict(key); k2.update(zip(letters, vals))
            sh.append(score(rs, k2, lp))
        sh.sort()
        print(f'scored symbols: {sum(len(r) for r in rs)}, letter-symbol types in key: {len(letters)}, used: {len(used)}')
        print(f'real key: {real:.3f}')
        print(f'shuffled x{N}: min {sh[0]:.3f} / median {sh[N // 2]:.3f} / max {sh[-1]:.3f}')
        print(f'shuffled >= real: {sum(1 for x in sh if x >= real)} / {N}')
