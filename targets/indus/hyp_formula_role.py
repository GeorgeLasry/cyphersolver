"""Session-2 loop 1: the closing formula 705/706 33 520 (sets 445-457) as a role."""
import inspect

import progress as P
import rtools as R
from signs import load

TITLE = 'the closing formula as a role'
REG = '''The other run found the closing formula '705 / 706 33 520' to be the long form of the fish name class (sets 445-457).
Its tokens not already given a role get a 'closing formula' role (`hyp_formula_role.py`, `mydriver.py`).

- **FR1** The role raises R by 0.5 points or more on the distinct lines.
- **FR2** The formula closes the line (last, or followed only by 400 / 90) in 80%+ of its occurrences on A and on B.
- Progress rule: FR1 and FR2.'''
SUMMARY = ''
F = {('705', '33', '520'), ('706', '33', '520')}


def run(rd):
    global SUMMARY
    DL, tr, te = P.data()
    src = inspect.getsource(P.roles).replace("            num_before = g in R.NUMS\n            tot += 1",
        "            if role is None and any(tuple(t[j:j + 3]) in FORM and j <= i < j + 3 for j in range(max(0, i - 2), i + 1)):\n                role = 'closing formula'\n            num_before = g in R.NUMS\n            tot += 1")
    ns = dict(P.__dict__)
    ns['FORM'] = F
    exec(src, ns)
    r0 = P.roles(DL, edges=True, head2=True)[0]
    r1, by, tot = ns['roles'](DL, edges=True, head2=True)
    ok1 = r1 - r0 >= 0.005
    rd.rec('FR1', 'the role raises R by 0.5 points', 'R %.2f%% -> %.2f%% (%d tokens)' % (100 * r0, 100 * r1, by['closing formula']), ok1)
    A, B, *_ = R.load_all()
    DA = sorted({tuple(t) for t in A})
    DB = sorted({tuple(ln) for r in load(only_m77=True) for ln in r['seq'] if ln} - set(DA))
    out = []
    for S in (DA, DB):
        occ = [(t, j) for t in S for j in range(len(t) - 2) if tuple(t[j:j + 3]) in F]
        fin = sum(all(g in ('400', '90') for g in t[j + 3:]) for t, j in occ)
        out.append((fin, len(occ)))
    ok2 = all(n and f / n >= 0.8 for f, n in out)
    rd.rec('FR2', 'the formula closes the line on A and B', 'A %d of %d, B %d of %d' % (out[0] + out[1]), ok2)
    SUMMARY = 'R %.2f%% -> %.2f%%; final A %d/%d, B %d/%d.' % ((100 * r0, 100 * r1) + out[0] + out[1])
    return ok1 and ok2
