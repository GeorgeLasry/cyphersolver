"""r2l: the sign values of Maffeo's 1489 cipher (key R5411 + values carried across V2831), as lattice alternatives.

    python research/reading_audit/r2l_signs.py <raw.txt> > groups.txt

raw.txt lines: ID § left context § signs as written in trans/*_r2e.md / *_b25.md § right context
Each sign is replaced by its alternatives (key value first; '!' marks a look-alike reading, '_' a null).
"""
import sys, pathlib

S = {
    '//': 'e', '4': 'e', 'ε': 'o/!b', 'E': 'o/!b', '3': 'o/!r', 'ʒ': 'r', 'z': 'r', 'r': 'a', '1': 'a', 'f': 'a',
    'i': 'a', 'a': 'm', 'n': 'i', '5': 'i', 'g': 'n/!x/!h', '8': 'g/n/!x', 'v': 'n', '6': 'u/!o', 'c': 'p', 'e': 'p',
    'ɔ': 'q', ')': 'q', 'C': 'q', 'o': 'b/t', 'o-bar': 't/b', 'p̸': 't', 'x': 'd', 'd': 'l/s', 's': 'c/u', 'δ': 's',
    '9': 'h', 'L': 'to/h', 'L:': 'te', 'L.': 'te', 'Lᵉ': 'te', 'L^a': 'ta', '7': 'f', 'm': 'f', 'q': 'e', 'q^a': 'ra',
    'q^e': 're', 'q^s': 'ro', 'q^o': 're', 'q̥': 'ri', 'b': 'co', 'b̶': 'ca', 'b̶·': 'ce/ca', 'b.': 'ce', 'ƀ': 'fa',
    'đ': 'fe', 'd:': 'fi', 'b^a': 'na', 'b^e': 'ne', 'b^o': 'no', 'bˣ': 'ni', 'b^u': 'nu', 'm^a': 'sa', 'm^e': 'se',
    'm^o': 'si', 'm^u': 'so', 'm:': 'bi', 'x̄': 'ma/et', 'xo': 'ma', 'x̸': 'et', 'ꭗ': 'et', "x'": 'do', 'n#': 'ss',
    'n+4': 'ss', 'n̶': 'tt', 'n^e': 'll', 'nⁱ': 'mm', 'n^o': 'pp', 'nᵒ': 'pp', 'n^u': 'rr', 'n:': 'cc', 'ƒ': 'ff',
    'ρ': 'n/ff', 'np̸': 'ff', 'd-o': 'st/lt', 'd-o-bar': 'st/lt', '÷': '_', 'w': '_', '=': '_', 'B': '_', 'ꝏ': '_',
    'a:': 'gli', 'ā': 'm', 'o·': 'b/t', 'z·': 'r/to', 'e·': 'p', 'b:': 'ca/ce', 'n^ε': 'll', 'ŝ': 'c',
    'σ': 'mi', 'x^a': 'de', 'x^u': 'du', 'a·': 'm', 'r̸': 'et', 'ñ': 'i', 'r̥': '_/a', 'ẋ': 'd',
}


def conv(signs):
    out = []
    for t in signs.split():
        if t == '|':
            continue
        if t not in S:
            raise SystemExit(f'unknown sign {t!r} in {signs!r}')
        out.append(S[t])
    return ' '.join(out)


if __name__ == '__main__':
    for line in pathlib.Path(sys.argv[1]).read_text(encoding='utf8').splitlines():
        if not line.strip() or line.startswith('#'):
            print(line); continue
        gid, left, signs, right = [x.strip() for x in line.split('§')]
        print(f'{gid} | {left} | {conv(signs)} | {right}')
