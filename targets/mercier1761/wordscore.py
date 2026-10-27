"""Word-level score for an unspaced French stream: best segmentation into dictionary words (unigram log-prob),
unknown stretches charged per character. Dictionary from fr-gutenberg (shared lang corpus)."""
import math, os, re
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
from solve import norm  # noqa: E402

UNK = -12.0     # log-prob per character not covered by a dictionary word


def load_words(nchars=6_000_000):
    text = open(os.path.join(HERE, '..', '..', 'lang', 'corpora', 'fr-gutenberg.txt'), encoding='utf8',
                errors='ignore').read()[:nchars]
    c = Counter(w for w in (norm(x) for x in re.split(r"[\s'’\-]+", text)) if w)
    tot = sum(c.values())
    return {w: math.log(n / tot) for w, n in c.items() if n >= 2}


class WordScorer:
    def __init__(self, words):
        self.lp = words
        self.maxlen = max(map(len, words))

    def score(self, s):
        n = len(s)
        best = [0.0] + [-math.inf] * n
        lp, ml = self.lp, self.maxlen
        for i in range(n):
            b = best[i]
            if b == -math.inf:
                continue
            if b + UNK > best[i + 1]:
                best[i + 1] = b + UNK
            for j in range(i + 1, min(n, i + ml) + 1):
                w = lp.get(s[i:j])
                if w is not None and b + w > best[j]:
                    best[j] = b + w
        return best[n]
