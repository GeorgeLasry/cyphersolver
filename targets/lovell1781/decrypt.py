"""Motion in Congress, 10 Aug 1781 (PCC item 59 vol. 1 p. 133): decryption with Lovell's "Jay" key, and controls.

    python decrypt.py              decryption line by line against transcription.txt
    python decrypt.py --controls   the controls quoted in NOTES.md

System (James Lovell's): alphabet a..z plus & (27 signs). A column headed by key letter K runs K, K+1, ... so that
row 1 is K itself; a plaintext letter p (a=0 ... &=26) under K is written (p - K) mod 27 + 1. The "Jay" key on
p. 144 has two columns, B and Y, used letter by letter in turn. Rows 28-30 are numbered on the key sheet but carry
no letter, so 28, 29 and 30 are read as nulls: they give no letter and do not move the alternation on.
The alternation runs on through the clear words between the two cipher stretches.

The cipher numbers are taken from transcription.txt itself: every line that holds a group of point-separated
numbers. "1119" is written without a point; it is split into 11 and 19 (the only intervention).
Python standard library only; paths are relative to this file.
"""
import gzip, json, math, os, random, re, sys
from itertools import permutations

HERE = os.path.dirname(os.path.abspath(__file__))
ALPHA = 'abcdefghijklmnopqrstuvwxyz&'
KEY = 'by'
NULLS = {28, 29, 30}


def dec(n, k):
    """plaintext letter of number n (1-27) in the column headed by key letter k"""
    return ALPHA[(n - 1 + ALPHA.index(k)) % 27]


def stretches():
    """the two cipher stretches as read in transcription.txt, split at the clear words after '1119'"""
    nums = []
    with open(os.path.join(HERE, 'transcription.txt'), encoding='utf-8') as f:
        for line in f:
            if line.startswith('#') or not re.search(r'\d+\.\d+', line):
                continue
            nums += re.findall(r'\d+', line)
    i = nums.index('1119')
    a = [int(t) for t in nums[:i]] + [11, 19]          # "1119" written without a point
    b = [int(t) for t in nums[i + 1:]]
    return a, b


def decrypt(seq, keys, phase=0, nulls=True):
    """letters of seq under the alternating key columns; returns (text, next phase)"""
    out = []
    for n in seq:
        if n in NULLS:
            if nulls:
                out.append('_'); continue
            n -= 27                                     # the solver's first variant: wrap 28-30 onto 1-3
        out.append(dec(n, keys[phase % len(keys)])); phase += 1
    return ''.join(out), phase


def both(keys, restart=False, nulls=True):
    a, b = stretches()
    x, ph = decrypt(a, keys, nulls=nulls)
    y, _ = decrypt(b, keys, 0 if restart else ph, nulls=nulls)
    return x, y


def bigram_model():
    """letter-bigram log-probabilities from the repository's English word list (lang/lexicons/en.json.gz)"""
    lex = json.load(gzip.open(os.path.join(HERE, '..', '..', 'lang', 'lexicons', 'en.json.gz'), 'rt', encoding='utf-8'))
    big, tot = {}, {}
    for w, c in lex.items():
        w = ''.join(ch for ch in w if ch in ALPHA[:26])
        for p, q in zip(w, w[1:]):
            big[p + q] = big.get(p + q, 0) + c
    for pq, c in big.items():
        tot[pq[0]] = tot.get(pq[0], 0) + c
    return {p + q: math.log((big.get(p + q, 0) + 0.5) / (tot.get(p, 0) + 13.5)) for p in ALPHA[:26] for q in ALPHA[:26]}


def score(s, lp):
    """mean bigram log-probability; '&' and nulls are skipped"""
    s = ''.join(c for c in s if c in ALPHA[:26])
    return sum(lp[s[i:i + 2]] for i in range(len(s) - 1)) / max(1, len(s) - 1)


def controls():
    lp = bigram_model()
    x, y = both(KEY)
    print(f'Jay key b/y, nulls, alternation running on:  {x} | {y}   {score(x + y, lp):.3f}')
    res = []
    for p in permutations(ALPHA, 2):
        k = ''.join(p)
        x2, y2 = both(k)
        res.append((score(x2 + y2, lp), k, x2, y2))
    res.sort(reverse=True)
    print(f'all {len(res)} ordered pairs of two different key letters; best five:')
    for s, k, x2, y2 in res[:5]:
        print(f'  {k}  {s:.3f}  {x2} | {y2}')
    print(f'  rank of b/y: {[r[1] for r in res].index(KEY) + 1};  median score {res[len(res) // 2][0]:.3f}')
    print('the other columns of the same sheet (p. 144):')
    others = [('Adams', 'cr'), ('Adams swapped', 'rc'), ('H. Laurens', 'yo'), ('H. Laurens swapped', 'oy'),
              ('Jay swapped', 'yb')]
    others += [('Franklin ' + ''.join(o), ''.join(o)) for o in permutations('cor')]
    others += [('Palfrey ' + ''.join(o), ''.join(o)) for o in permutations('unt')]
    for name, k in others:
        x2, y2 = both(k)
        print(f'  {name:20s} {score(x2 + y2, lp):.3f}  {x2} | {y2}')
    x2, y2 = both(KEY, restart=True)
    print(f'b/y, alternation restarted at b for the second stretch: {score(x2 + y2, lp):.3f}  {x2} | {y2}')
    x2, y2 = both(KEY, nulls=False)
    print(f'b/y, 28-30 wrapped onto 1-3 instead of nulls: {x2[:6]}...  (gives "dy" before "further")')
    rnd = random.Random(1781)
    a, b = stretches()
    real = [n for n in a + b if n not in NULLS]
    sh = []
    for _ in range(200):
        r = real[:]; rnd.shuffle(r)
        sh.append(score(decrypt(r, KEY)[0], lp))
    print(f'200 shuffles of the 55 letter numbers under b/y: best {max(sh):.3f}, mean {sum(sh) / len(sh):.3f}')


def main():
    a, b = stretches()
    if '--controls' in sys.argv:
        controls(); return
    x, ph = decrypt(a, KEY)
    y, _ = decrypt(b, KEY, ph)
    print('# Motion of 10 Aug 1781, PCC 59 vol. 1 p. 133: decryption against transcription.txt (python decrypt.py)')
    print("# Key: Lovell's 'Jay' columns B and Y (key.txt), used in turn; 28-30 are nulls (_), they do not move the key.")
    print('# The plaintext is English; no translation is needed.')
    print()
    for name, seq, txt, start in (('A', a, x, 0), ('B', b, y, ph)):
        print(f'Stretch {name} ({len(seq)} numbers, first key column {KEY[start % 2].upper()}):')
        ks, k = [], start
        for n in seq:
            if n in NULLS:
                ks.append('-')
            else:
                ks.append(KEY[k % 2].upper()); k += 1
        print('  number: ' + ' '.join(f'{n:>2}' for n in seq))
        print('  column: ' + ' '.join(f'{c:>2}' for c in ks))
        print('  letter: ' + ' '.join(f'{c:>2}' for c in txt))
        print()
    print('Stretch A follows "to make such" and ends with 11 19, written "1119";')
    print('the clear words "of these United States to the" stand between A and B.')
    print('A: ' + x + '  ->  [nulls 30, 28] further cessions of the right')
    print('B: ' + y + '  ->  navigation of the river Mississipi')
    print()
    print('With the cipher words in place:')
    print('  "That the said minister be & he is hereby authorised and empowered to make such FURTHER CESSIONS OF THE')
    print('  RIGHT of these United States to the NAVIGATION OF THE RIVER MISSISSIPI as he may think proper and on such')
    print('  terms & conditions as he may think most for the honor & interest of these United States."')


if __name__ == '__main__':
    main()
