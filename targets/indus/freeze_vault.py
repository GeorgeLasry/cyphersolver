"""Freeze (25 Oct 2026) for the new-finds vault (set 353): the set 350 referent units and the S/SIGN training lines are
written to data/frozen/ before any post-2022 inscription is transcribed. The vault test reads only these files."""
import json
import os

import predict_test304 as C
import predict_test334 as S
import rtools as R
from famlm import learned_classes
from predict_test338 import collapse, objects_typed
from predict_test350 import LM, build
from progress import data

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data', 'frozen')


def main():
    os.makedirs(OUT, exist_ok=True)
    A, B, rowsA, recs, F = R.load_all()
    DL, tr, te = data()
    LM.update(learned_classes(DL, 50, seed=0))
    C.LMAP.update(LM)
    clean, both = objects_typed(F, recs)
    cc, cb = collapse(clean), collapse(both)
    S.ALPHA = 0.002
    S.SIGN = tuple(S.SIGN) + (-3, 5)
    S.FAM = tuple(S.FAM) + (-3,)
    u = build(cc, cb)
    units = [{'label': 'texts' if k == 'texts' else k[0], 'n': None if k == 'texts' else k[1],
              'gram': list(g), 'picture': m} for k, q in u.items() for g, m in q.items()]
    json.dump({'units': units, 'learned_classes': LM}, open(os.path.join(OUT, 'referent_units_set350.json'), 'w'), indent=0)
    fullF = sorted({tuple(ln) for r in F for ln in r['seq'] if ln})
    json.dump({'lines': [list(t) for t in sorted(set(DL) | set(fullF))]}, open(os.path.join(OUT, 'training_lines.json'), 'w'))
    print(len(units), 'units;', len(set(DL) | set(fullF)), 'training lines')


if __name__ == '__main__':
    main()
