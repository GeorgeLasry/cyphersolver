"""Run the capped homophonic annealer (homo304.run_cap) on f. 304r."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
sys.path.insert(0, str(Path(__file__).parent))
from lang import lm
from solve304 import words_of
from homo304 import run_cap
words = words_of(Path(__file__).with_name('f304r_transcription.txt'))
model = lm.load('de-1500s')
(score, m), t = run_cap(words, model, restarts=int(sys.argv[1]) if len(sys.argv) > 1 else 16, seed=int(sys.argv[2]) if len(sys.argv) > 2 else 1, verbose=True)
print('BEST', round(model.score(t) / len(t), 3))
print(' '.join(f'{k}={v}' for k, v in sorted(m.items())))
print(t)
