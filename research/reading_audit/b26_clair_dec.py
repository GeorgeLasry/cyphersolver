"""b26: decode clair357 figure runs (two-digit homophonic, Tomokiyo's table as extended in targets/clair357/texts/key.md).

    python research/reading_audit/b26_clair_dec.py "74 24 34 28 29 72 22 26 43 28 27"

Prints the letter values; word signs in capitals, unknown groups as <nn>, nulls as '.'.
"""
import sys

KEY = {}
for letters, groups in [('a', '14 20 71'), ('b', '16'), ('c', '18'), ('d', '25 73'), ('e', '28 72 87'), ('f', '17 35'),
                        ('g', '12 74'), ('h', '86'), ('i', '34 67 98'), ('l', '13 51 70'), ('m', '42 64'), ('n', '19 29'),
                        ('o', '23 37'), ('p', '40 68'), ('q', '85'), ('r', '43 88'), ('s', '27 36 82'), ('t', '26 47'),
                        ('u', '24 63'), ('x', '77'), ('z', '41')]:
    for g in groups.split(): KEY[g] = letters
KEY.update({'78': ' VOUS ', '81': ' QUE ', '83': ' IL ', '92': ' ET ', '45': '.', '31': '.', '66': '.', '22': '.'})


def dec(s):
    return ''.join(KEY.get(g, f'<{g}>') if g.isdigit() else f' [{g}] ' for g in s.split())


if __name__ == '__main__':
    for a in sys.argv[1:]: print(dec(a))
