"""Capped homophonic annealer: each sign -> one letter, at most CAP signs per letter (3 for e, n).
Moves: reassign one sign, or swap two signs' letters. Fixed cribs optional.

import: run_cap(words, model, fix={}, restarts, steps)
"""
import math, random, sys
from collections import Counter
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from solve304 import ALPHA

CAP = {c: 2 for c in ALPHA}
CAP.update(e=3, n=3)


def run_cap(words, model, fix=None, restarts=12, steps=30000, seed=1, verbose=False):
    fix = fix or {}
    signs = sorted({t for w in words for t in w})
    free = [s for s in signs if s not in fix]
    rnd = random.Random(seed)
    def text(m): return ' '.join(''.join(m[t] for t in w) for w in words)
    best = (-1e9, None)
    for r in range(restarts):
        m = dict(fix)
        cnt = Counter(m.values())
        for s in free:
            opts = [c for c in ALPHA if cnt[c] < CAP[c]]
            m[s] = rnd.choice(opts); cnt[m[s]] += 1
        cur = model.score(text(m))
        for i in range(steps):
            T = max(0.05, 4.0 * (1 - i / steps))
            a = rnd.choice(free)
            if rnd.random() < 0.5:
                b = rnd.choice(free)
                if m[a] == m[b]: continue
                m[a], m[b] = m[b], m[a]
                new = model.score(text(m))
                if new >= cur or rnd.random() < math.exp((new - cur) / T): cur = new
                else: m[a], m[b] = m[b], m[a]
            else:
                c = rnd.choice(ALPHA); old = m[a]
                if c == old or cnt[c] >= CAP[c]: continue
                m[a] = c; cnt[old] -= 1; cnt[c] += 1
                new = model.score(text(m))
                if new >= cur or rnd.random() < math.exp((new - cur) / T): cur = new
                else: m[a] = old; cnt[old] += 1; cnt[c] -= 1
        if verbose: print(f'restart {r}: {cur/len(text(m)):.3f} {text(m)[:100]}', flush=True)
        if cur > best[0]: best = (cur, dict(m))
    return best, text(best[1])
