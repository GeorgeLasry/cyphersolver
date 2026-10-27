"""Capped homophonic annealer on f. 304r under several language models (language check)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
sys.path.insert(0, str(Path(__file__).parent))
import homo304
from lang import lm
from solve304 import words_of
words = words_of(Path(__file__).with_name('f304r_transcription.txt'))
for mid in sys.argv[1:]:
    model = lm.load(mid)
    alpha = 'abcdefghilmnopqrstuvxz' if not mid.startswith('de') else homo304.ALPHA
    homo304.ALPHA = alpha
    homo304.CAP = {c: 2 for c in alpha}; homo304.CAP.update(e=3, n=3)
    (s, m), t = homo304.run_cap(words, model, restarts=10, steps=30000)
    print(mid, round(model.score(t) / len(t), 3), t[:220], flush=True)
