"""Diversity rounds: rerun each open line with the previous rounds' opening words banned, so the list shows
alternative openings instead of 150 variants of one prefix."""
import os, sys
os.environ.setdefault("KBEST", "60"); os.environ.setdefault("NBEST", "12")
import search2 as search, ads2 as ads
vocab, lp, uniU, biU = search.load_lm()
trie = search.build_trie(vocab)
lines = [int(x) for x in (sys.argv[1] if len(sys.argv) > 1 else "9,26,29,5,21,6,12,19").split(",")]
for ln in lines:
    A, B = ads.BNA[ln]
    print(f"=== line {ln}: {A} / {B}")
    banned = set()
    for rnd in range(5):
        s = search.Searcher(A, B, vocab, lp, uniU, biU, trie)
        orig = s.transitions
        def trans(i, j, orig=orig):
            out = orig(i, j)
            if i == 0 and j == 0:
                out = [t for t in out if t[0] not in banned]
            return out
        s.transitions = trans
        res = s.run()
        if not res: break
        print(f"  -- round {rnd+1}, banned openings: {sorted(banned) or '-'}")
        for sc, words in res:
            print(f"  {sc:8.2f}  {' '.join(words)}")
        banned.add(res[0][1][0])
        sys.stdout.flush()
