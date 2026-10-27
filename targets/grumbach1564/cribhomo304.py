"""Capped homophonic annealer on f. 304r with the strong German cribs fixed (und, -en, machen, sachen, knecht, ersparen)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
sys.path.insert(0, str(Path(__file__).parent))
from lang import lm
from solve304 import words_of
from homo304 import run_cap
FIX = dict(V='e', S='n', G='d', P='m', L='c', H='k', T='t', Y='s', F='r', C='p', **{'6': 'u', '3': 'h'})
words = words_of(Path(__file__).with_name('f304r_transcription.txt'))
model = lm.load('de-1500s')
(s, m), t = run_cap(words, model, fix=FIX, restarts=16, steps=20000, seed=int(sys.argv[1]) if len(sys.argv) > 1 else 1)
print('BEST', round(model.score(t) / len(t), 3))
print(' '.join(f'{k}={v}' for k, v in sorted(m.items()) if k not in FIX))
print(t)
