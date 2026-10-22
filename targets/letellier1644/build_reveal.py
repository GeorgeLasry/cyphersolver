"""Write docs/reveal/letellier1644.json: f. 50v lines v01-v09 decoded sign by sign with the contributor's key.

Each sign gets the key value (main or other) that the DP alignment with the contributor's line reading uses; a sign
whose value does not stand in the reading is marked 'unc' with its main value, a sign without a value 'unk'.
Code groups are 'code'; words written in clear are 'plain'. Run: PYTHONUTF8=1 python targets/letellier1644/build_reveal.py
"""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import measure as M

LINES = ['v01', 'v02', 'v03', 'v04', 'v05', 'v06', 'v07', 'v08', 'v09']


def assign(us, target):
    n, m = len(us), len(target)
    NEG = -10 ** 9
    dp = [[NEG] * (m + 1) for _ in range(n + 1)]
    bk = [[None] * (m + 1) for _ in range(n + 1)]
    for j in range(m + 1): dp[0][j] = 0
    for i in range(1, n + 1):
        for j in range(m + 1):
            best, b = dp[i - 1][j], ('skip', None, 0)
            if j and dp[i][j - 1] > best: best, b = dp[i][j - 1], ('gap', None, 0)
            for c in us[i - 1][1]:
                L = len(c)
                if L and j >= L:
                    ok = target[j - L:j] == c
                    v = dp[i - 1][j - L] + (1 if ok else 0)
                    if v > best: best, b = v, ('take', c, L if ok else -L)
            dp[i][j], bk[i][j] = best, b
    out, i, j = [None] * n, n, m
    while i > 0:
        kind, c, L = bk[i][j]
        if kind == 'gap': j -= 1; continue
        if kind == 'take': out[i - 1] = (c, L > 0); j -= abs(L)
        i -= 1
    return out


def raw_val(key, sign, normed):
    for v in key.get(sign, []):
        if M.norm(v) == normed: return v
    return normed


def main():
    key, rd = M.load_key(), M.load_reading()
    tx = dict(M.load_tx())
    toks = []
    for lid in LINES:
        raw = tx[lid]
        us = M.units(raw, key)
        got = assign(us, rd[lid])
        k = 0
        i = 0
        while i < len(raw):
            t = raw[i]
            if t.startswith('['):
                w = t.strip('[]')
                toks.append({'g': '', 'p': ' (struck out) ' if w == '消' else ' ' + w + ' ', 'cls': 'plain'}); i += 1; continue
            g, cands = us[k]
            ch = got[k]
            if not cands: toks.append({'g': g, 'p': '?', 'cls': 'unk'})
            elif g in M.CODES or g == '=11 =o':
                word = {'=y': 'Monsieur le Mareschal', '=3': 'de La Motte', '=32': 'Barcelone', '=11 =o': 'la Reyne',
                        '39': 'Catalogne'}.get(g, cands[0])
                toks.append({'g': g, 'p': ' ' + word + ' ', 'cls': 'code' if (ch and ch[1]) else 'unc'})
            elif ch and ch[1]: toks.append({'g': t, 'p': raw_val(key, t, ch[0]), 'cls': ''})
            else: toks.append({'g': t, 'p': key[t][0], 'cls': 'unc'})
            i += 2 if g == '=11 =o' else 1
            k += 1
        toks.append({'g': '', 'p': ' / ', 'cls': 'plain'})
    toks.pop()
    d = {
        'slug': 'letellier1644',
        'anchor': 'reading',
        'title': 'f. 50v, lines 1-9: the opened packets',
        'caption': "Le Tellier to Marca, 26 April 1644, BnF Baluze 103 f. 50v lines 1-9, in Harumi-Matsuba's transcription "
                   "and key (issue #54), decoded sign by sign; / marks a line end.",
        'unit': 'signs',
        'key_note': "Tomokiyo's Le Tellier-Marca table of 1644 with the contributor's additions (contributed/data/key.tsv); "
                    "a sign marked uncertain has a key value that the contributor's reading does not keep.",
        'tokens': toks,
    }
    p = os.path.join(HERE, '..', '..', 'docs', 'reveal', 'letellier1644.json')
    open(p, 'w', encoding='utf-8').write(json.dumps(d, ensure_ascii=False, indent=1) + '\n')
    n = sum(1 for t in toks if t['g'])
    print(f'{n} signs; unc {sum(1 for t in toks if t["cls"] == "unc")}; unk {sum(1 for t in toks if t["cls"] == "unk")}')
    print(''.join(t['p'] for t in toks))


if __name__ == '__main__':
    main()
