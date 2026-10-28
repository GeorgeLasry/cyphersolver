"""Alphabetical-position fit of the page.row anchors to a dictionary edition.

OCR of these editions misses many headwords, so instead of looking for the word on
the page, each leaf gets an alphabetical span from its headword-like tokens (a token
followed by a comma and a part-of-speech mark). An anchor (page p, word w) is
predicted onto the leaf whose span holds w; the edition's page offset is the
median of (leaf - p). A correct edition puts nearly all of one system's
anchors at residual 0 or +-1.
Usage: python alpha_fit.py CACHE_DIR ID [ID ...]
"""
import re, sys, json, statistics
from collections import Counter
import test_editions as t

HEAD = re.compile(r"([a-z][a-z'’`\"]{1,20})[,.]\s*(?:[sſvaj/|]\.?|ad\.?|n\.)\s", re.I)


def key(w):
    return re.sub(r"[^a-z]", "", w.lower().replace('ſ', 's'))


def spans(leaves):
    out = []
    for text in leaves:
        hs = sorted(k for k in (key(m.group(1)) for m in HEAD.finditer(text.replace('ſ', 's'))) if len(k) >= 3)
        out.append(hs[len(hs) // 2] if len(hs) >= 15 else None)
    # running median over 5 leaves smooths OCR noise; span = (this, next) medians
    sm = []
    for i in range(len(out)):
        win = sorted(x for x in out[max(0, i - 2):i + 3] if x)
        sm.append(win[len(win) // 2] if len(win) >= 3 and out[i] else None)
    return [(m, None) if m else None for m in sm]


def predict(sp, w):
    """Leaf whose span holds w; between spans, the earlier leaf."""
    # first leaf after which the smoothed medians stay above w (allowing noise)
    idx = [i for i, s in enumerate(sp) if s]
    best, score = None, -1
    for j, i in enumerate(idx):
        sc = sum(1 for k in idx[:j] if sp[k][0] <= w) + sum(1 for k in idx[j:] if sp[k][0] > w)
        if sc > score:
            best, score = i, sc
    return best


def fit(ident, cache):
    leaves, _ = t.pages(cache, ident)
    sp = spans(leaves)
    res = [(p, w, predict(sp, w) - p) for p, r, c, w in t.anchors() if predict(sp, w) is not None]
    off = Counter(d for _, _, d in res).most_common(1)[0][0]
    near = [(p, w) for p, w, d in res if abs(d - off) <= 1]
    return dict(id=ident, leaves=len(leaves), offset=off, within1=len(near), n=len(res),
                pages=sorted(p for p, w in near))


if __name__ == '__main__':
    for i in sys.argv[2:]:
        try:
            r = fit(i, sys.argv[1])
            r['pages'] = f"{min(r['pages'])}-{max(r['pages'])}" if r['pages'] else ''
            print(json.dumps(r), flush=True)
        except Exception as e:
            print(i, repr(e), flush=True)
