"""Repeats in the figures of Hann. 9g Nr. 964 ff. 8r-8v, against the interlinear decipherment, with a shuffle control.

    python repeats.py            (from this folder, or with any working directory; standard library only)

Reads 964_f8_cipher.txt (16 runs) and ../texts/964_f6_cipher.txt (the 1734 rescript, for the cross-check).
There is no key, so this is not a decryption. It asks two questions:
  1. Do figure strings repeat between runs more than chance allows, and on the runs whose glosses share words?
  2. Does f. 8 (Vienna -> Hanover) share strings with f. 6 (London -> Hanover)?
The control shuffles the figures inside each run (keeping each run's digit counts) and repeats the count.
"""
import collections, pathlib, random, sys

sys.stdout.reconfigure(encoding='utf-8', errors='replace')
HERE = pathlib.Path(__file__).resolve().parent
GLOSS = {
    'C1': 'dem RhsRaht von Knörre', 'C2': 'dasjenige [?bewürket] w[...]', 'C3': '[?dienstlich]',
    'C4': '[?befürchtet] und hier eingeleitet zu werden', 'C5': 'nunmehr, der von Knörre (tail barred)',
    'C6': 'über sich genommen mit dem', 'C7': 'RVCantzler Grafen von Metsch und dem',
    'C8': 'von Bartenstein, wenn ich mir vorher bey beyden', 'C9': 'man mit Ihr. Kayserl. Mayt.',
    'C10': 'statt würcklicher Stellung gedachten', 'C11': 'Contingents über ein gewisses Quan-',
    'C12': 'tum an Geld übereinkämen (tail barred)', 'C13': 'meinet der von Knörre',
}


def runs(path, labelled=True):
    out = {}
    for i, line in enumerate(l.strip() for l in open(path, encoding='utf-8')):
        if not line or line.startswith('#'):
            continue
        if labelled:
            k, v = line.split(None, 1)
        else:
            k, v = 'f6L%d' % (len(out) + 1), line
        out[k] = ''.join(c for c in v if c.isdigit() or c == '?')
    return out


def shared(R, n):
    occ = collections.defaultdict(set)
    for k, v in R.items():
        for i in range(len(v) - n + 1):
            g = v[i:i + n]
            if '?' not in g:
                occ[g].add(k)
    return {g: s for g, s in occ.items() if len(s) > 1}


def stats(R):
    longest = max((n for n in range(5, 16) if shared(R, n)), default=0)
    five_in_4 = sum(1 for s in shared(R, 5).values() if len(s) >= 4)
    return longest, five_in_4


def cross(A, B, n):
    hits = []
    for ka, a in A.items():
        for kb, b in B.items():
            gb = {b[i:i + n] for i in range(len(b) - n + 1)}
            hits += [(a[i:i + n], ka, kb) for i in range(len(a) - n + 1) if a[i:i + n] in gb and '?' not in a[i:i + n]]
    return hits


def main():
    R = runs(HERE / '964_f8_cipher.txt')
    print('runs', len(R), '| figures', sum(len(v) for v in R.values()))
    for k, v in R.items():
        print('  %-5s %3d  %s' % (k, len(v), GLOSS.get(k, '(barred, no decipherment)')))
    for n in (10, 8, 7, 6):
        sh = shared(R, n)
        print('--- %d-figure strings in more than one run: %d' % (n, len(sh)))
        for g, s in sorted(sh.items(), key=lambda x: (-len(x[1]), x[0])):
            print('   ', g, sorted(s))
    print('--- 5-figure strings in 3 or more runs')
    for g, s in sorted(shared(R, 5).items(), key=lambda x: (-len(x[1]), x[0])):
        if len(s) >= 3:
            print('   ', g, sorted(s))
    real = stats(R)
    print('real: longest shared string %d; 5-figure strings in 4+ runs: %d' % real)
    random.seed(1)
    N = 2000
    dist = collections.Counter()
    ge_long = ge_four = 0
    for _ in range(N):
        S = {k: ''.join(random.sample(v, len(v))) for k, v in R.items()}
        m, c4 = stats(S)
        dist[m] += 1
        ge_long += m >= real[0]
        ge_four += c4 >= real[1]
    print('shuffle control (N=%d): longest shared string %s' % (N, sorted(dist.items())))
    print('  share of shuffles reaching the real longest: %.4f; reaching the real 4+-run count: %.4f'
          % (ge_long / N, ge_four / N))
    F6 = runs(HERE.parent / 'texts' / '964_f6_cipher.txt', labelled=False)
    for n in (7, 6, 5):
        print('f. 6 / f. 8 shared %d-figure strings: %d' % (n, len(cross(F6, R, n))))
    random.seed(2)
    hist = collections.Counter()
    for _ in range(1000):
        S = {k: ''.join(random.sample(v, len(v))) for k, v in R.items()}
        hist[len(cross(F6, S, 6))] += 1
    print('control: shared 6-figure strings, f. 6 against shuffled f. 8 (N=1000):', sorted(hist.items()))


if __name__ == '__main__':
    main()
