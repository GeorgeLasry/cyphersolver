"""Letter-level EM aligner (after balbases1677/em.py).

Each cipher group emits 0..MAXL plaintext letters (0 = null); plaintext letters may be
skipped (passages not in the cipher). Hard-EM with a length prior.
Usage: python lem.py <cipher tx> <plain words file> [iters]
"""
import sys, math, collections, json, unicodedata
sys.stdout.reconfigure(encoding='utf-8')
from wem import load_cipher

MAXL = 12
prior = {0: .06, 1: .3, 2: .3, 3: .18, 4: .07, 5: .04, 6: .02, 7: .01, 8: .01, 9: .005, 10: .005, 11: .003, 12: .002}


def norm(s):
    s = unicodedata.normalize('NFD', s)
    return ''.join(ch for ch in s if 'a' <= ch <= 'z')


def run(t, s, iters, skip):
    cnt = collections.defaultdict(collections.Counter)

    def cost(tok, sub):
        c = cnt[tok]; n = sum(c.values()); a = 2.0
        p = (c[sub] + a * prior[len(sub)] * (0.06 ** len(sub))) / (n + a)
        return -math.log(p)

    I, J = len(t), len(s)
    for it in range(iters):
        INF = 1e18
        D = [[INF] * (J + 1) for _ in range(I + 1)]
        B = [[None] * (J + 1) for _ in range(I + 1)]
        D[0][0] = 0
        for i in range(I + 1):
            Di = D[i]
            for j in range(J + 1):
                d = Di[j]
                if d >= INF:
                    continue
                if j < J and d + skip < Di[j + 1]:
                    Di[j + 1] = d + skip; B[i][j + 1] = (i, j)
                if i < I:
                    tok = t[i]; Dn = D[i + 1]; Bn = B[i + 1]
                    for L in range(0, min(MAXL, J - j) + 1):
                        c = d + cost(tok, s[j:j + L])
                        if c < Dn[j + L]:
                            Dn[j + L] = c; Bn[j + L] = (i, j)
        i, j = I, J
        path = []
        while (i, j) != (0, 0):
            pi, pj = B[i][j]
            path.append((pi, pj, i, j))
            i, j = pi, pj
        path.reverse()
        cnt = collections.defaultdict(collections.Counter)
        for pi, pj, i, j in path:
            if i > pi:
                cnt[t[pi]][s[pj:j]] += 1
        tot = sum(sum(c.values()) for c in cnt.values())
        agree = sum(c.most_common(1)[0][1] for c in cnt.values())
        skipped = sum(1 for pi, pj, i, j in path if i == pi)
        print('iter', it, 'consistency', round(agree / tot, 3), 'skipped letters', skipped, flush=True)
    return cnt, path


if __name__ == '__main__':
    t = load_cipher(sys.argv[1])
    s = norm(open(sys.argv[2], encoding='utf-8').read())
    iters = int(sys.argv[3]) if len(sys.argv) > 3 else 8
    skip = float(sys.argv[4]) if len(sys.argv) > 4 else 3.0
    cnt, path = run(t, s, iters, skip)
    json.dump({k: c.most_common(4) for k, c in cnt.items()}, open('lem_key.json', 'w', encoding='utf-8'), indent=0)
    out = []
    for pi, pj, i, j in path:
        out.append(f'{t[pi]}={s[pj:j] or "_"}' if i > pi else f'[{s[pj:j]}]')
    open('lem_path.txt', 'w', encoding='utf-8').write(' '.join(out))
    for k, c in sorted(cnt.items(), key=lambda x: -sum(x[1].values()))[:50]:
        print(k, dict(c.most_common(3)))
