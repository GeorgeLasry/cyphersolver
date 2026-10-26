"""Driver for the strict-bar goal loops (from set 518): registers a two-hypothesis seal-size set (auditkit.size_motif,
two-sided, progress only at p < 0.01), commits the registration, runs it, appends the result and a PROGRESS row,
and commits. Usage: python goal_driver.py <set> <loop> <streak_before> <signA> <signB>"""
import subprocess
import sys

import auditkit
import rtools as R

ORD = {518: 'Five-hundred-and-eighteenth'}


def ordinal(n):
    return ORD.get(n, 'Set %d' % n)


def git(msg, paths):
    subprocess.run(['git', 'add'] + paths, cwd='..\..', check=True)
    subprocess.run(['git', 'commit', '-q', '-m', msg + '\n\nCo-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>'], cwd='..\..', check=True)


def main():
    n, loop, streak = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
    a, b = sys.argv[4], sys.argv[5]
    reg = '''

# Set %d, registered before testing (26 October 2026): goal loop %d, signs %s and %s by seal size (two hypotheses)

`auditkit.size_motif` (length band x site x motif), two-sided; progress only at p < 0.01 (rule before set 517)
(`goal_driver.py`).

- **H1** Large and small seals differ in carrying %s.
- **H2** They differ in carrying %s.
- Progress rule: either at p < 0.01.
''' % (n, loop, a, b, a, b)
    with open('PREDICTIONS.md', 'a', encoding='utf-8') as f:
        f.write(reg)
    git('indus: register set %d' % n, ['targets/indus/PREDICTIONS.md'])
    rd = R.Round('Set %d registered predictions: goal loop %d, signs %s and %s by seal size' % (n, loop, a, b), 'predict_test%d' % n)
    res = []
    for k, g in (('H1', a), ('H2', b)):
        o, p = auditkit.size_motif(lambda t, g=g: g in t)
        rd.rec(k, 'large and small seals differ in carrying %s' % g, 'odds ratio %.2f, p = %.4f' % (o, p), p < 0.01)
        res.append((g, o, p))
    prog = any(p < 0.01 for g, o, p in res)
    rd.rec('P', 'progress rule: either at p < 0.01', '', prog)
    rd.finish()
    new_streak = 0 if prog else streak + 1
    txt = '''
## Results of set %d (`goal_driver.py`, `results/predict_test%d.md`)

%s. Progress: %s (goal streak %d).
''' % (n, n, '; '.join('%s odds ratio %.2f (p = %.4f)' % r for r in res), 'yes' if prog else 'none', new_streak)
    with open('PREDICTIONS.md', 'a', encoding='utf-8') as f:
        f.write(txt)
    row = '| G%d | %d | 4.559 | 86.3%% | 16.6%% (M+ 41.4%%) | 0 | 4 (L world 85.1%%) | signs %s / %s by seal size: %s (%s; goal streak %d) |\n' % (
        loop, n, a, b, ', '.join('%s OR %.2f p %.3f' % r for r in res), 'progress' if prog else 'no progress', new_streak)
    with open('PROGRESS.md', 'a', encoding='utf-8') as f:
        f.write(row)
    git('indus: set %d result' % n, ['targets/indus/PREDICTIONS.md', 'targets/indus/PROGRESS.md', 'targets/indus/results/predict_test%d.md' % n])
    print('set %d: %s; streak %d' % (n, res, new_streak))


if __name__ == '__main__':
    main()
