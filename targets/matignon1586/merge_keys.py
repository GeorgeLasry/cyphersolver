"""One Cipher-1 key across Brackx's per-leaf keys (brackx2026/key_*.json), and a test of it.

Step 1, union: every figure gets the union of the letter sets the per-leaf keys give it; a code group takes every
value any leaf gives it (a '+' in one leaf and a word in another is the word). -> key_merged_union.json
Step 2, prune: decode every leaf with the union key (brackx_validate's beam, this project's 6-gram), count which
letter each figure actually took across the whole target, and drop a letter a figure took in fewer than PRUNE of
its occurrences (never dropping a figure's commonest letter). -> key_merged.json
Step 3, test: decode every leaf with key_merged.json and score it exactly as brackx_validate.py does (sense, copy
agreement, scrambled-key control, 3 seeds), side by side with the per-leaf keys. -> merge_keys.json

  python merge_keys.py          (decodes cached in measure_cache/mk_*)
"""
import json, os, sys, collections
sys.argv = [sys.argv[0]]
import brackx_validate as V

HERE = V.HERE
B = V.B
PRUNE = 0.05


def load(kf):
    return json.load(open(os.path.join(B, kf), encoding='utf-8'))


def union_key():
    keys = sorted({kf for _, _, kf, _, _ in V.LEAVES})
    out = {}
    for kf in keys:
        for t, v in load(kf).items():
            cur = out.setdefault(t, [])
            for x in v:
                if x not in cur:
                    cur.append(x)
    for t, v in out.items():
        if len(v) > 1 and '+' in v:   # a value from one leaf beats '+' (unknown) from another
            v.remove('+')
    return out


def usage(key, tag):
    """letter taken by each figure over the whole target, decoded with key."""
    cnt = collections.defaultdict(collections.Counter)
    for name, files, _, _, _ in V.LEAVES:
        res = V.decode(files, V.prep_key(key), f'{tag}_{name.replace(" ", "_").replace(".", "")}')
        for r in res:
            p = 0
            for t, L in zip(r['tokens'], r['lens']):
                cnt[t][r['text'][p:p + L]] += 1
                p += L
    return cnt


def prune(key, cnt):
    out = {}
    for t, v in key.items():
        if len(v) < 2 or t.isdigit() or any(len(x) > 2 for x in v):
            out[t] = v
            continue
        c = cnt.get(t, collections.Counter())
        tot = sum(c.values())
        if not tot:
            out[t] = v
            continue
        top = c.most_common(1)[0][0]
        keep = [x for x in v if x.replace('v', 'u') == top or c[x.replace('v', 'u')] / tot >= PRUNE]
        out[t] = keep or v
    return out


def score_key(key, tag):
    rep = {}
    for name, files, _, copies, issue in V.LEAVES:
        k = V.prep_key(key)
        t = f'{tag}_{name.replace(" ", "_").replace(".", "")}'
        real, _ = V.leaf_scores(name, files, k, copies, t)
        ctl = [V.leaf_scores(name, files, V.scramble(k, s), copies, f'{t}_s{s}')[0] for s in range(3)]
        floor = {x: round(sum(c[x] for c in ctl) / 3, 3) for x in real if x not in ('tokens', 'letters')}
        rep[name] = {'real': real, 'scrambled_mean': floor}
        print(f"{tag} {name:18s} sense {real['sense']:.3f} (floor {floor['sense']:.3f})" + ''.join(
            f" | {x[5:]} {real[x]:.3f}" for x in real if x.startswith('copy:')), flush=True)
    return rep


def main():
    u = union_key()
    json.dump(u, open(os.path.join(HERE, 'key_merged_union.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
    cnt = usage(u, 'mku')
    m = prune(u, cnt)
    json.dump(m, open(os.path.join(HERE, 'key_merged.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
    dropped = {t: [x for x in u[t] if x not in m[t]] for t in u if u[t] != m[t]}
    print('pruned:', dropped)
    per_leaf = json.load(open(os.path.join(HERE, 'brackx_validate.json'), encoding='utf-8'))
    rep = {'union': score_key(u, 'mku'), 'merged': score_key(m, 'mkm'), 'pruned_letters': dropped,
           'usage': {t: dict(c) for t, c in cnt.items()}}
    tot = collections.Counter()
    for which in ('union', 'merged'):
        for name, r in rep[which].items():
            n = r['real']['tokens']
            tot[which + '_n'] += n
            tot[which + '_read'] += r['real']['sense'] * n
            tot[which + '_floor'] += r['scrambled_mean']['sense'] * n
    for name, r in per_leaf.items():
        if isinstance(r.get('real'), dict):
            n = r['real']['tokens']
            tot['leaf_n'] += n
            tot['leaf_read'] += r['real']['sense'] * n
    rep['totals'] = {w: {'tokens': tot[w + '_n'], 'read': round(tot[w + '_read']),
                         'sense': round(tot[w + '_read'] / tot[w + '_n'], 3),
                         'floor': round(tot.get(w + '_floor', 0) / tot[w + '_n'], 3)}
                     for w in ('union', 'merged', 'leaf')}
    print(rep['totals'])
    json.dump(rep, open(os.path.join(HERE, 'merge_keys.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)


if __name__ == '__main__':
    main()
