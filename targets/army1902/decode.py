"""Japanese Army numeric kana cipher, 1902-04 (JACAR, NIDS holdings): decoder and checks.

Table as stated by Harumi-Matsuba (issue #58, kagigo1901-public), re-implemented here from the description only:
  first digit  = vowel row of the gojuon: a 0, i 1, u 2, e 3, o 4; +5 for a voiced kana
  second digit = consonant column in reverse gojuon order: a 9, ka 8, sa 7, ta 6, na 5, ha 4, ma 3, ya 2, ra 1, wa 0;
                 voiced: ga 9, za 8, da 7, ba 6
  10 = n;  a final 80 = end mark (conjecture)
e.g. ka = 08, shi = 17, ga = 59, bu = 76.

  python decode.py            decode the four telegrams (ct_*.txt) and score them against the contemporary renderings
  python decode.py control    permutation control: shuffle the row and column digits 1,000 times
"""
import glob, os, random, sys

HERE = os.path.dirname(os.path.abspath(__file__))
COLS = {9: 'アイウエオ', 8: 'カキクケコ', 7: 'サシスセソ', 6: 'タチツテト', 5: 'ナニヌネノ', 4: 'ハヒフヘホ',
        3: 'マミムメモ', 2: 'ヤ?ユ?ヨ', 1: 'ラリルレロ', 0: 'ワヰ?ヱヲ'}
VOICED = {9: 'ガギグゲゴ', 8: 'ザジズゼゾ', 7: 'ダヂヅデド', 6: 'バビブベボ'}

# The contemporary renderings in kana, aligned pair by pair (the contributor's alignment; checked here for 0110 and 0026).
# C09122911500: frame 0108 本職帰京迄本部ノ事務ハ貴官宜シク取計ハレタシ.  C09122909900: furigana of the outgoing draft
# C09122909800 (カイグン, エンシウ) + 見学.  C03020059400: 辛碇泊場司令部 (場 spelt ジウ).  C09123116600: none (reply draft
# frame 0025 sends maps of Korea; the reading is checked only for sense).
REF = {
    'C09122911500': 'ホンシヨクキキヨウマデホンブノジムハキクワンヨロシクトリハカラハレタシ',
    'C09122909900': 'カイグンエンシウケンガク',
    'C03020059400': 'シンテイハクジウシレイブ',
}


def value(p, rows=(0, 1, 2, 3, 4), cols=tuple(range(10))):
    """kana for a digit pair; rows/cols permute the digits (identity by default)."""
    if p == '10': return 'ン'
    if p == '80': return '|'
    a, b = int(p[0]), int(p[1])
    voiced = a >= 5
    r, c = rows[a % 5], cols[b]
    if voiced:
        return VOICED[c][r] if c in VOICED else '?'
    return COLS[c][r]


def load():
    out = {}
    for f in sorted(glob.glob(os.path.join(HERE, 'ct_*.txt'))):
        ref = os.path.basename(f)[3:-4]
        pairs = []
        for l in open(f, encoding='utf8'):
            if l.startswith('#') or l.startswith('=='): continue
            pairs += l.split()
        out[ref] = pairs
    return out


def score(pairs, ref, **kw):
    got = ''.join(value(p, **kw) for p in pairs if p != '80')
    return sum(a == b for a, b in zip(got, ref)), got


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    T = load()
    if len(sys.argv) > 1 and sys.argv[1] == 'control':
        random.seed(1902)
        for ref, pairs in T.items():
            if ref not in REF: continue
            real, _ = score(pairs, REF[ref])
            best = hits = 0
            for _ in range(1000):
                rows = list(range(5)); random.shuffle(rows)
                cols = list(range(10)); random.shuffle(cols)
                s, _ = score(pairs, REF[ref], rows=rows, cols=cols)
                best = max(best, s); hits += s >= real
            print(f'{ref}: real {real}/{len(REF[ref])}; 1000 shuffled tables: max {best}, at or above real {hits}')
    else:
        for ref, pairs in T.items():
            got = ''.join(value(p) for p in pairs)
            line = f'{ref}: {len(pairs)} pairs  {got}'
            if ref in REF:
                s, g = score(pairs, REF[ref])
                diff = [f'{i}:{p}={x}/{y}' for i, (p, x, y) in enumerate(zip([q for q in pairs if q != '80'], g, REF[ref])) if x != y]
                line += f'  | agrees {s}/{len(REF[ref])} {" ".join(diff)}'
            print(line)
