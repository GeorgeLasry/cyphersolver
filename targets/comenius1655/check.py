"""Comenius to Klobusiczky, 1655: rebuild the 4 Aug 1655 key from Patera's footnote, decrypt, report the one
conflict, run two controls, and try the key on the other cipher passages.

    python check.py

Standard library only. Ciphertexts as printed in Patera (1892) and MHH XXIII (1874); see ct_*.txt.
"""
import random

# 4 Aug 1655 (Patera CLIV p. 182; MHH XXIII no. CXXIX p. 219). "et" is written in clear.
CT_AUG = "Cyhyqbma cgzbbttg et CmCasda 69 655m"
PT_AUG = "poloniam periisse et papatum in illa"      # Patera's footnote: "Značí: Poloniam periisse et papatum in illa."

# 24 May 1655 (Patera CLII p. 178; MHH XXIII no. CIII p. 178). Long s written as s. Last word: Patera / MHH.
CT_MAY_PATERA = "Lmqsxmyo 7 Gpdlmuoyqnotlses Pnofeyprp 865 ap 73 pys pdyp Xyopatus"
CT_MAY_MHH = "Lmqsxmyo 7 Gpdlmuoyqnotlses Pnofeyprp 865 ap 73 pys pdyp Xyoapus"

# a word in the clear text of 4 Aug: "Mire angitur bonus vir (iyy) de tantis sibi injectis remoris" (italic in MHH)
CT_IYY = "iyy"


def build_key(ct, pt):
    """cipher -> plain from the aligned crib; collects conflicts (position, sign, first value, new value)."""
    key, conflicts = {}, []
    words_c, words_p = ct.lower().split(), pt.split()
    pos = 0
    for wc, wp in zip(words_c, words_p):
        if wc == wp:                              # clear word ("et")
            pos += len(wc); continue
        for c, p in zip(wc, wp):
            pos += 1
            if c in key and key[c] != p:
                conflicts.append((pos, c, key[c], p))
            else:
                key.setdefault(c, p)
    return key, conflicts


def dec(ct, key, clear=('et',)):
    return ' '.join(w if w.lower() in clear else ''.join(key.get(ch, '?') for ch in w.lower()) for w in ct.split())


def main():
    key, conflicts = build_key(CT_AUG, PT_AUG)
    # The conflict: the 4th letter of CmCasda is cipher 'a' (= plain m elsewhere) but Patera reads plain 'a'.
    # Build the key without that one letter, so 'a' keeps its value m from "Cyhyqbm-a".
    print('key cipher -> plain (first value kept):')
    print('  ' + ', '.join(f'{c}={p}' for c, p in sorted(key.items())))
    print('conflicts (position in cipher letters, sign, value, value at this place):', conflicts)
    strict = dec(CT_AUG, key)
    print('strict decryption :', strict)
    print("Patera's footnote :", PT_AUG)
    diff = [(i, a, b) for i, (a, b) in enumerate(zip(strict, PT_AUG)) if a != b]
    print('letters that differ:', diff)

    pairs = sorted({tuple(sorted((c, p))) for c, p in key.items() if c.isalpha()})
    both = [(a, b) for a, b in pairs if key.get(a) == b and key.get(b) == a]
    print('pairs attested in both directions (reciprocal):', both)
    print('plain -> cipher:', ', '.join(f'{p}={"/".join(sorted(c for c in key if key[c] == p))}'
                                        for p in sorted(set(key.values()))))

    random.seed(1)
    vals = list(key.values()); random.shuffle(vals)
    print('control 1, shuffled key      :', dec(CT_AUG, dict(zip(key, vals))))
    sh = []
    for w in CT_AUG.split():
        l = list(w)
        if w != 'et': random.shuffle(l)
        sh.append(''.join(l))
    print('control 2, letters shuffled  :', dec(' '.join(sh), key))

    inv = {}
    for c, p in key.items():
        if c.isalpha(): inv.setdefault(p, c)
    print()
    print('24 May with the 4 Aug key     :', dec(CT_MAY_PATERA, key, clear=()))
    print('24 May with the inverse key   :', dec(CT_MAY_PATERA, inv, clear=()))
    recip = dict(key)
    for a, b in pairs: recip.setdefault(a, b); recip.setdefault(b, a)
    print('24 May with the pairs as a reciprocal table:', dec(CT_MAY_PATERA, recip, clear=()))
    print("'iyy' with the 4 Aug key / reciprocal table:", dec(CT_IYY, key), '/', dec(CT_IYY, recip))
    letters = ''.join(ch for ch in CT_MAY_PATERA.lower() if ch.isalpha())
    print('24 May: letters', len(letters), 'distinct', len(set(letters)),
          '| MHH variant last word differs:', CT_MAY_PATERA.split()[-1], 'vs', CT_MAY_MHH.split()[-1])


if __name__ == '__main__':
    main()
