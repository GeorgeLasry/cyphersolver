"""Cipher of João IV's letters to the marquês de Nisa, 1642-43 (ANTT MSLIV 1017).

Monoalphabetic substitution with a few homophones, written as pseudo-words in Latin letters,
word divisions kept. Rebuilt from two cipher/clear pairs in the letter-book itself:
letter 8 (25 Oct 1642, f. 15, scan m0019) with its 'Papel junto à dita carta', and
letter 13 (31 Dec 1642, ff. 20-21, scans m0024-25) with its 'Carta inclusa' (m0025-26).

CIPHER maps a cipher letter to its plain values (first = most frequent).
Capital E is a distinct sign (a large looped E) for plain f.
"""
import sys

PLAIN_TO_CIPHER = {
    'a': 'o', 'b': 'g', 'c': 'e', 'd': 'f', 'e': 'c', 'f': 'E', 'g': 'd', 'h': 'b',
    'i': 'a', 'l': 'p', 'm': 'z', 'n': 'i', 'o': 'u', 'p': 'g', 'q': 's', 'r': 't',
    's': 'rv', 't': 'n', 'u': 'x', 'v': 'xz', 'z': 'l',
}

CIPHER = {}
for p, cs in PLAIN_TO_CIPHER.items():
    for c in cs:
        CIPHER.setdefault(c, []).append(p)

SYMBOLS = {'⊕': '[Castela / ElRei de Castela]'}

# System B (letters of Sept 1644 - Feb 1645: 00153 f. 153, Carta 187 f. 174, Carta 212 f. 185), a second alphabet with
# Greek-shaped signs, labelled here by the Latin letter each sign resembles. Rebuilt from m0276, the volume's own list
# of deciphered passages, against the same phrases in cipher on m0179 and m0190. Cipher label -> plain.
# Homophones: plain i also t/s, plain p also t, plain l also v, plain a also o (in 'qotpbx'); r = u.
KEY_B = {
    'E': 'o', 'b': 'm', 'e': 'n', 'f': 'i', 'i': 'p', 'm': 'r', 'n': 's', 'p': 'a', 'u': 'd', 'x': 'e',
    'z': 'f', 'q': 'c', 'a': 'l', 'c': 'h', 'v': 'u', 'o': 't', 't': 'z', 'r': 'u', 'd': 'g', 'g': 'c',
}


def decode_b(text):
    return ''.join(KEY_B.get(ch, ch.upper() if ch.isalpha() else ch) for ch in text)


def decode(text):
    out = []
    for ch in text:
        if ch in SYMBOLS:
            out.append(SYMBOLS[ch])
        elif ch in CIPHER:
            v = CIPHER[ch]
            out.append(v[0] if len(v) == 1 else '(' + '/'.join(v) + ')')
        elif ch.isalpha():
            out.append('?' + ch)
        else:
            out.append(ch)
    return ''.join(out)


if __name__ == '__main__':
    for line in (sys.argv[1:] or sys.stdin.read().splitlines()):
        print(decode(line))
