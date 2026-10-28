"""python targets/dorabella/run_round.py <round> [...] [--doublet]: run hypothesis rounds from rounds.py."""
import sys
import hyp
import rounds
if '--doublet' in sys.argv:
    hyp.NULLS = 'doublet'
for k in sys.argv[1:]:
    if not k.startswith('--'):
        rounds.ROUNDS[int(k)]()
