# Catalogue 641 (revenga1822): mechanical decryption of transcription.txt with the substitution key, and controls.
# Standard library only. Run from this folder:
#   python decrypt.py              -> decryption, group by group (decryption.txt is this output)
#   python decrypt.py --controls   -> share of decrypted words in the Spanish word list, against random keys and shuffles
#   python decrypt.py --pairs      -> writes validation.tsv (one cipher sign per line with its value) for docs/_validate.py
# Contributed by WAINUT, 27 Oct 2026.
import random
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent

# cipher sign -> plain. 'S' stands for the cipher digraph ll (one sign, plain s). Cipher 'a' is the word space.
# Main values (>= 50 occurrences): a t v p g S m e z.  Rare values are uncertain (see key.txt).
KEY = {
    'a': ' ', 't': 'e', 'v': 'a', 'p': 'o', 'g': 'i', 'S': 's', 'm': 'r', 'e': 'n', 'z': 'd',
    'b': 'u', 'y': 'c', 'l': 't', 'ñ': 'l', 'd': 'm', 'o': 'p', 'n': 'q', 'x': 'b', 'h': 'y',
    's': 'g', 'j': 'v', 'c': 'll', 'u': 'f', 'r': 'h', 'f': 'ñ', 'i': 'x', 'k': 'z',
    ',': ',',
}


def signs(cipher):
    """Split a group into cipher signs: ll greedily as one sign (so lll = ll + l), [..] as one unread sign."""
    out, i = [], 0
    while i < len(cipher):
        if cipher[i] == '[':
            j = cipher.index(']', i)
            out.append('?'); i = j + 1
        elif cipher.startswith('ll', i):
            out.append('S'); i += 2
        else:
            out.append(cipher[i]); i += 1
    return out


def decrypt(cipher, key=KEY):
    return ''.join(key.get(s, '[?]') if s != '?' else '[?]' for s in signs(cipher))


def groups():
    rows = []
    for line in open(HERE / 'transcription.txt', encoding='utf-8'):
        if line.startswith('C') and '\t' in line:
            gid, place, cipher, clear = (line.rstrip('\n').split('\t') + [''])[:4]
            rows.append((gid, place, cipher, clear))
    return rows


def lexicon():
    """The repository's Spanish word list (lang/lexicons/es.json.gz), words of three letters or more."""
    import gzip, json, unicodedata
    lex = json.load(gzip.open(HERE.parent.parent / 'lang' / 'lexicons' / 'es.json.gz', 'rt', encoding='utf-8'))
    strip = lambda w: ''.join(c for c in unicodedata.normalize('NFD', w) if not unicodedata.combining(c))
    return {strip(w) for w, n in lex.items() if len(w) >= 3 and n >= 5}


LEX = None


def hit_rate(texts):
    """Share of decrypted words of three letters or more that are in the Spanish word list."""
    global LEX
    if LEX is None: LEX = lexicon()
    words = [w.replace('ñ', 'n') for t in texts for w in re.findall(r'[a-zñ]+', t) if len(w) >= 3]
    return sum(w in LEX for w in words) / max(1, len(words))


def controls(rows, n=2000, seed=641):
    rnd = random.Random(seed)
    true = hit_rate(decrypt(c) for _, _, c, _ in rows)
    print(f'true key: Spanish-word share {true:.3f} over {len(rows)} groups')
    cipher_signs = [k for k in KEY if k != ',']
    plains = [KEY[k] for k in cipher_signs]
    best = tot = 0.0
    for _ in range(n):
        perm = plains[:]; rnd.shuffle(perm)
        key = dict(zip(cipher_signs, perm)); key[','] = ','
        r = hit_rate(decrypt(c, key) for _, _, c, _ in rows); best = max(best, r); tot += r
    print(f'control A, {n} random permutations of the key (space included): max {best:.3f}, mean {tot / n:.3f}')
    best = tot = 0.0
    for _ in range(n):
        texts = []
        for _, _, c, _ in rows:
            s = signs(c); rnd.shuffle(s)
            texts.append(''.join(KEY.get(x, '[?]') if x != '?' else '[?]' for x in s))
        r = hit_rate(texts); best = max(best, r); tot += r
    print(f'control B, {n} shuffles of the signs inside each group (true key): max {best:.3f}, mean {tot / n:.3f}')
    order = [k for k in cipher_signs if k != 'a']
    rot = {k: KEY[order[(i + 1) % len(order)]] for i, k in enumerate(order)}; rot['a'] = ' '; rot[','] = ','
    print(f'control C, key rotated by one place (space kept): {hit_rate(decrypt(c, rot) for _, _, c, _ in rows):.3f}')


def pairs(rows):
    """validation.tsv for docs/_validate.py: one cipher sign per line, TAB, its value. The word space a and the
    comma-like mark read as nothing ('-'); unread signs and the sign q without a value are '?'."""
    out = ['# model: es-modern', '# source: transcription.txt with KEY in decrypt.py (python decrypt.py --pairs)',
           '# note: ll is one sign (written ll); cipher a = word space and the comma-like mark are given as nulls']
    for _, _, c, _ in rows:
        for s in signs(c):
            tok = 'll' if s == 'S' else s
            val = '?' if s == '?' or s not in KEY else '-' if s in ('a', ',') else KEY[s]
            out.append(f'{tok}\t{val}')
    (HERE / 'validation.tsv').write_text('\n'.join(out) + '\n', encoding='utf-8', newline='\n')
    print(f'validation.tsv: {len(out) - 3} signs')


def main(argv):
    rows = groups()
    if '--pairs' in argv:
        pairs(rows); return
    if '--controls' in argv:
        controls(rows); return
    print('# Catalogue 641 (revenga1822): mechanical decryption of transcription.txt, group by group.')
    print('# Output of python decrypt.py. Cipher a = word space, ll = s (lll read as ll + l), c = ll, ñ = l.')
    print('# Each group: id, frame, the cipher as transcribed, the mechanical plaintext, then the clear text that')
    print('# follows it in the letter. The misspellings come from the first-pass transcription (see NOTES.md);')
    print('# reading.md gives the text as sentences.')
    print()
    for gid, place, cipher, clear in rows:
        print(f'{gid}  {place}')
        print(f'  cipher: {cipher}')
        print(f'  plain:  {decrypt(cipher)}')
        print(f'  clear:  {clear}')
        print()


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    main(sys.argv[1:])
