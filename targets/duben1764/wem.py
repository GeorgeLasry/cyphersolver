"""Word-level EM aligner: cipher groups against the contemporary decipherment.

Each group is either a null or stands for one word; a word may also be spelled by
several groups (handled as word skips, so those groups are learned as nulls/partials).
Usage: python wem.py <cipher tx> <plain words> [iterations]
"""
import sys, re, math, collections, json
sys.stdout.reconfigure(encoding='utf-8')


def load_cipher(path):
    toks = []
    for l in open(path, encoding='utf-8'):
        parts = l.split()
        if not parts:
            continue
        for t in parts[1:]:
            if t.startswith('[del'):
                continue
            t = t.strip("'?+")
            if t.isdigit():
                toks.append(t)
    return toks


def run(toks, words, iters=12):
    vocab = set(words)
    cnt = collections.defaultdict(collections.Counter)
    SKIPW, NULL = 6.0, 4.0

    def cost(t, w):
        c = cnt[t]
        n = sum(c.values())
        return -math.log((c[w] + 1.0 / len(vocab)) / (n + 1.0))

    for it in range(iters):
        I, J = len(toks), len(words)
        INF = 1e18
        D = [[INF] * (J + 1) for _ in range(I + 1)]
        B = [[None] * (J + 1) for _ in range(I + 1)]
        D[0][0] = 0
        band = max(60, abs(I - J) + 40)
        for i in range(I + 1):
            lo = max(0, int(i * J / I) - band)
            hi = min(J, int(i * J / I) + band)
            for j in range(lo, hi + 1):
                d = D[i][j]
                if d >= INF:
                    continue
                if j < J and d + SKIPW < D[i][j + 1]:
                    D[i][j + 1] = d + SKIPW; B[i][j + 1] = (i, j, 'skipw')
                if i < I:
                    nc = d + NULL + (0 if it == 0 else cost(toks[i], '<null>') * 0.3)
                    if nc < D[i + 1][j]:
                        D[i + 1][j] = nc; B[i + 1][j] = (i, j, 'null')
                    if j < J:
                        mc = d + (2.0 if it == 0 else cost(toks[i], words[j]))
                        if mc < D[i + 1][j + 1]:
                            D[i + 1][j + 1] = mc; B[i + 1][j + 1] = (i, j, 'match')
        i, j = I, J
        path = []
        while (i, j) != (0, 0):
            pi, pj, k = B[i][j]
            path.append((pi, pj, k))
            i, j = pi, pj
        path.reverse()
        cnt = collections.defaultdict(collections.Counter)
        for pi, pj, k in path:
            if k == 'match':
                cnt[toks[pi]][words[pj]] += 1
            elif k == 'null':
                cnt[toks[pi]]['<null>'] += 1
    return cnt, path


if __name__ == '__main__':
    toks = load_cipher(sys.argv[1])
    words = open(sys.argv[2], encoding='utf-8').read().split()
    iters = int(sys.argv[3]) if len(sys.argv) > 3 else 12
    cnt, path = run(toks, words, iters)
    key = {t: c.most_common(3) for t, c in cnt.items()}
    json.dump(key, open('wem_key.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
    # consistency: share of matched tokens whose word equals the token's top word
    tot = agree = 0
    for t, c in cnt.items():
        n = sum(c.values()); top = c.most_common(1)[0][1]
        tot += n; agree += top
    print('tokens', len(toks), 'words', len(words), 'consistency', round(agree / tot, 3))
    out = []
    for pi, pj, k in path:
        if k == 'match':
            out.append(f'{toks[pi]}={words[pj]}')
        elif k == 'null':
            out.append(f'{toks[pi]}=_')
        else:
            out.append(f'-={words[pj]}')
    open('wem_path.txt', 'w', encoding='utf-8').write(' '.join(out))
    for t, c in sorted(cnt.items(), key=lambda x: -sum(x[1].values()))[:45]:
        print(t, dict(c.most_common(3)))
