"""b24 (vanreede1787): key R1024 from the DECODE transcription, with the number-column slips fixed by page order
(an entry whose number breaks the run n-1, ?, n+1 by one digit takes n) and the 'Nonvaleurs' (null) ranges read off
the key images P6, P11, P12, P19, P21, P25."""
import re, pathlib
D = pathlib.Path(r'C:/Users/dbour/cypher/targets/vanreede1787/decode')
NULLS = [(1, 50), (331, 370), (1201, 1250), (2751, 2800), (3131, 3160), (3621, 3660)]
def is_null(v): return any(a <= v <= b for a, b in NULLS)
def load():
    rows = []
    for l in (D / 'DOC_R1024_D2881_2881.txt').read_text(encoding='utf8', errors='replace').splitlines():
        m = re.match(r'^\s*(\d+)\s+-\s+(.*?)\s*$', l)
        if m: rows.append([int(m.group(1)), m.group(2)])
    fixes = []
    for i in range(1, len(rows) - 1):
        p, n, q = rows[i - 1][0], rows[i][0], rows[i + 1][0]
        if n != p + 1 and q == p + 2:
            a, b = str(n), str(p + 1)
            if len(a) == len(b) and sum(x != y for x, y in zip(a, b)) == 1:
                fixes.append((n, p + 1, rows[i][1])); rows[i][0] = p + 1
    k = {}
    for n, w in rows: k[n] = w
    k.update(KEYFIX)
    return k, fixes
# word-column slips of the DECODE key transcription, read on the key images (b24):
#   54 'es' -> 'est' (P12, '53. es / 54. est'); 2142 'paroitre' -> 'paroit' and the missing 2143 = 'paroitre'
#   (P15: '2141 paroissoit, 2142 parôit, 2143 paroitre, 2144 parole'); 4910 'quo' -> 'que' (P33, '4909 Q. 4910 que')
KEYFIX = {54: 'est', 2142: 'paroit', 2143: 'paroitre', 4910: 'que'}
if __name__ == '__main__':
    k, f = load()
    for x in f: print('fixed', x)
    print(len(k))
