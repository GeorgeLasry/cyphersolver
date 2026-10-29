"""How long would a deciphered sibling letter in the same code need to be?  Resample the 1702 letter's own group
distribution (Good-Turing mass for unseen groups) and count what share of its 591 tokens a sibling of L tokens
would give values for, averaged over 200 draws."""
import json, collections, random, os
here = os.path.dirname(os.path.abspath(__file__))
t = json.load(open(os.path.join(here, 'tokens.json'))); c = collections.Counter(t); n = len(t)
n1 = sum(1 for v in c.values() if v == 1); unseen = n1 / n
probs = {g: v / n * (1 - unseen) for g, v in c.items()}
groups = list(probs); w = [probs[g] for g in groups] + [unseen]
rnd = random.Random(0)
for L in (100, 200, 400, 600, 1000, 2000):
    cov = []
    for _ in range(200):
        s = set(rnd.choices(groups + [None], weights=w, k=L))
        cov.append(sum(v for g, v in c.items() if g in s) / n)
    print('sibling of %4d tokens -> %.0f%% of the 1702 tokens get a value' % (L, 100 * sum(cov) / len(cov)))
