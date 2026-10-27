"""Johnston to Seddon, Jackson, 16 June 1863 (catalogue 629, NARA naId 3854726).

Vigenere (tabula recta), key MANCHESTERBLUFF, running across the five cipher words only and advancing by the
length of each plaintext word. The crib is the "Translation of Cypher" on image 3 of the same NARA item.

    python check.py            prints the line-by-line decryption, the key stream implied by cipher - crib,
                               the alignment variants and the controls (output kept in check_output.txt)

Python standard library only. Seeded, so the output repeats.
"""
import itertools
import random

A = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
KEY = 'MANCHESTERBLUFF'
CIPHER = ['UNIEK', 'CXNKVNED', 'JJTRRK', 'ISLX', 'KFYHJEER']    # as read on image 1
CRIB = ['INVADE', 'KENTUCKY', 'EXTEND', 'EAST', 'TENNESSEE']   # image 3, the words underscored "in Cypher"


def n(c): return ord(c) - 65
def ch(i): return A[i % 26]
def stream(key, start, length): return ''.join(key[(start + i) % len(key)] for i in range(length))
def enc(p, k): return ''.join(ch(n(a) + n(b)) for a, b in zip(p, k))
def dec(c, k): return ''.join(ch(n(a) - n(b)) for a, b in zip(c, k))


def run(key, advance='plain', ciph=CIPHER, crib=CRIB):
    """Positional matches of the expected encipherment against the written cipher."""
    k, hit, tot, rows = 0, 0, 0, []
    for c, p in zip(ciph, crib):
        ks = stream(key, k, len(p))
        e = enc(p, ks)
        m = sum(a == b for a, b in zip(c, e))
        hit, tot = hit + m, tot + len(e)
        rows.append((p, ks, e, c, dec(c, stream(key, k, len(c))), m))
        k = 0 if advance == 'restart' else k + (len(p) if advance == 'plain' else len(c))
    return hit, tot, rows


def main():
    print('== 1. Decryption, key MANCHESTERBLUFF advancing by plaintext length ==')
    h, t, rows = run(KEY)
    for p, ks, e, c, d, m in rows:
        print(f'{p:10s} key {ks:10s} expected {e:10s} written {c:9s} written deciphered {d:10s} matches {m}')
    print(f'positional matches {h}/{t}')
    for adv in ('cipher', 'restart'):
        print(f'  variant: key advancing by {adv if adv == "cipher" else "nothing (restart per word)"}: {run(KEY, adv)[0]}/{t}')

    print('\n== 2. Key stream implied by cipher - crib (no key assumed) ==')
    for c, p in zip(CIPHER, CRIB):
        print(f'{p:10s} {c:9s} C-P = {dec(c, p[:len(c)])}')
    print(f'{"TENNESEE":10s} {"KFYHJEER":9s} C-P = {dec("KFYHJEER", "TENNESEE")}   (one S of TENNESSEE dropped)')

    print('\n== 3. Controls ==')
    for key in ['COMPLETEVICTORY', 'COMERETRIBUTION', 'MANCHESTER', 'BLUFF', 'VICKSBURG', 'RICHMOND']:
        hh, _, rr = run(key)
        print(f'  key {key:16s} {hh}/{t}  written deciphered: ' + ' '.join(r[4] for r in rr))
    random.seed(629)
    scores = [run(''.join(random.choice(A) for _ in range(15)))[0] for _ in range(20000)]
    print(f'  20000 random 15-letter keys: mean {sum(scores) / len(scores):.2f}/{t}, max {max(scores)}/{t}')
    sh = [run(KEY, ciph=[CIPHER[i] for i in perm])[0] for perm in itertools.permutations(range(5)) if perm != (0, 1, 2, 3, 4)]
    print(f'  119 shuffled cipher-word orders, right key: mean {sum(sh) / len(sh):.2f}/{t}, max {max(sh)}/{t}')
    print('  15 start offsets of the key:', [run(KEY[i:] + KEY[:i])[0] for i in range(15)])

    print('\n== 4. Alternative sign readings ==')
    for alt in (['UNICK', 'CXNKVNED', 'JJTRRK', 'ISLX', 'KFYHJEER'],
                ['UNIEK', 'CXNKVNED', 'JJTRRK', 'ISDX', 'KFYHJEER'],
                ['UNIEK', 'CXNKVNED', 'JJTRRK', 'ISLX', 'KTYHJEER']):
        print('  reading', ' '.join(alt), '->', run(KEY, ciph=alt)[0], f'/{t}')

    print('\n== 5. The two C positions of the key ==')
    for p, ks, e, c, d, m in rows:
        for i, kl in enumerate(ks):
            if kl == 'C' and i < len(c):
                print(f'  {p} position {i + 1}: key C gives {e[i]}, written {c[i]} = {p[i]} + {ch(n(c[i]) - n(p[i]))}')


if __name__ == '__main__':
    main()
