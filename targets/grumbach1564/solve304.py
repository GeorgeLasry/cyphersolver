"""Anneal a sign->letter map for f. 304r (monoalphabetic, homophones allowed) on de-1500s.

python targets/grumbach1564/solve304.py [transcription] [restarts]
Words holding numbers or Latin-script tokens are left out of the score.
"""
import math, random, re, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from lang import lm

ALPHA = 'abcdefghiklmnopqrstuwz'   # 16th-c. German: i/j, u/v merged; x, y rare


def words_of(path):
    out = []
    for line in Path(path).read_text(encoding='utf8').splitlines():
        if line.startswith('#') or ':' not in line:
            continue
        body = line.split(':', 1)[1]
        for w in body.split('|'):
            toks = w.split()
            if not toks or not all(re.fullmatch(r'[A-Z368]', t) for t in toks):
                continue
            if len(toks) == 1 and toks[0] in '368':
                continue   # a lone 3/6/8 is a code number, not a letter
            out.append(toks)
    return out


def run(words, model, restarts=20, steps=20000, seed=1):
    """One-to-one map (each letter at most one sign), swap moves over the 22 letters."""
    signs = sorted({t for w in words for t in w})
    rnd = random.Random(seed)
    def text(m):
        return ' '.join(''.join(m[t] for t in w) for w in words)
    def sc(m):
        return model.score(text(m))
    best = (-1e9, None)
    letters = list(ALPHA) + ['x', 'y'] * 4   # spare slots so the map can leave letters unused
    for r in range(restarts):
        perm = letters[:]
        rnd.shuffle(perm)
        m = {s: perm[i] for i, s in enumerate(signs)}
        pool = perm[len(signs):]
        cur = sc(m)
        T = 3.0
        for i in range(steps):
            a = rnd.choice(signs)
            if rnd.random() < 0.5:
                b = rnd.choice(signs)
                m[a], m[b] = m[b], m[a]
                new = sc(m)
                if new >= cur or rnd.random() < math.exp((new - cur) / T):
                    cur = new
                else:
                    m[a], m[b] = m[b], m[a]
            else:
                j = rnd.randrange(len(pool))
                m[a], pool[j] = pool[j], m[a]
                new = sc(m)
                if new >= cur or rnd.random() < math.exp((new - cur) / T):
                    cur = new
                else:
                    m[a], pool[j] = pool[j], m[a]
            T = max(0.05, 3.0 * (1 - i / steps))
        if cur > best[0]:
            best = (cur, dict(m))
        print(f'restart {r}: {cur:.1f}  {text(m)[:110]}', flush=True)
    return best, text(best[1])


def run_homo(words, model, restarts=20, steps=40000, seed=1, pen=6.0):
    """Homophones allowed: each sign takes any letter, minus `pen` per extra sign on one letter."""
    signs = sorted({t for w in words for t in w})
    rnd = random.Random(seed)
    def text(m):
        return ' '.join(''.join(m[t] for t in w) for w in words)
    def sc(m):
        from collections import Counter
        c = Counter(m.values())
        return model.score(text(m)) - pen * sum(v - 1 for v in c.values())
    best = (-1e9, None)
    for r in range(restarts):
        m = {s: rnd.choice(ALPHA) for s in signs}
        cur = sc(m)
        for i in range(steps):
            T = max(0.05, 3.0 * (1 - i / steps))
            a = rnd.choice(signs)
            old = m[a]
            m[a] = rnd.choice(ALPHA)
            new = sc(m)
            if new >= cur or rnd.random() < math.exp((new - cur) / T):
                cur = new
            else:
                m[a] = old
        if cur > best[0]:
            best = (cur, dict(m))
        print(f'restart {r}: {cur:.1f}  {text(m)[:110]}', flush=True)
    return best, text(best[1])


if __name__ == '__main__' and '--homo' in sys.argv:
    sys.argv.remove('--homo')
    path = sys.argv[1]
    words = words_of(path)
    model = lm.load('de-1500s')
    (score, m), t = run_homo(words, model, int(sys.argv[2]))
    print('BEST', round(score, 1), round(score / len(t), 3))
    print(' '.join(f'{k}={v}' for k, v in sorted(m.items())))
    print(t)
    sys.exit()

if __name__ == '__main__':
    path = sys.argv[1] if len(sys.argv) > 1 else str(Path(__file__).with_name('f304r_transcription.txt'))
    restarts = int(sys.argv[2]) if len(sys.argv) > 2 else 20
    words = words_of(path)
    print(len(words), 'words', sum(map(len, words)), 'signs')
    model = lm.load('de-1500s')
    (score, m), t = run(words, model, restarts)
    print('BEST', round(score, 1), round(score / len(t), 3))
    print(' '.join(f'{k}={v}' for k, v in sorted(m.items())))
    print(t)
