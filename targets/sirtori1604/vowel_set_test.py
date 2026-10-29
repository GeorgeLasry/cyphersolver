"""Syllable hypothesis test: is there a set of 4-6 signs that occurs exactly once in nearly every word group?

If each space-separated group is a Spanish syllable spelled letter for letter, the vowel signs must occur exactly
once per group (diphthongs aside). Exhaustive search over sign sets on Caballero's word-divided f. 85 (his letters
used only as sign labels), compared with (a) real Spanish syllables of the same count and (b) groups whose signs
are shuffled across the text (same group lengths, same sign frequencies).

    python targets/sirtori1604/vowel_set_test.py
"""
import os, re, sys, random, itertools
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..'))


def groups_f85():
    L = open(os.path.join(HERE, 'transcription', 'caballero2012_f85.txt')).read().split('\n')[:13]
    g = [re.sub(r'[^A-Z]', '', w) for l in L for w in l.split()]
    return [x for x in g if x]


def best_set(groups, sizes=(4, 5, 6)):
    syms = sorted(set(''.join(groups)))
    best = (0, None)
    for k in sizes:
        for S in itertools.combinations(syms, k):
            S = set(S)
            f = sum(sum(c in S for c in g) == 1 for g in groups) / len(groups)
            if f > best[0]:
                best = (f, ''.join(sorted(S)))
    return best


def main():
    g = groups_f85()
    print('f85 groups', len(g), 'best set', best_set(g))
    rng = random.Random(0)
    flat = list(''.join(g))
    sh = []
    for r in range(5):
        rng.shuffle(flat)
        it = iter(flat)
        s = [''.join(next(it) for _ in x) for x in g]
        sh.append(best_set(s)[0])
    print('shuffled controls', [round(x, 3) for x in sh])
    from lang import lm, corpora
    sys.path.insert(0, HERE)
    import importlib
    spec = lm.registry()[0]['es-golden-age']
    words = lm.norm(corpora.text(spec['sources'])[2_000_000:2_010_000], spec['norm'], True).split()
    from syll import syl
    S = [s for w in words for s in syl(w)][:len(g)]
    print('spanish syllables', len(S), 'best set', best_set(S))


if __name__ == '__main__':
    main()
