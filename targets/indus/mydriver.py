"""Driver for this session's continued goal loops (from set 536, 26 Oct 2026): python mydriver.py <set> <loop> <streak>
<module>. The module (loops/gNNN.py style, here hyp_<name>.py) defines TITLE, REG (registration text: the hypotheses and
the progress rule) and run(rd) -> bool (progress). Registers and commits before running; records result, PROGRESS row
(S unchanged unless the module sets S) and commits."""
import importlib
import subprocess
import sys

import rtools as R


def git(msg, paths):
    subprocess.run(['git', 'add'] + paths, cwd='../..', check=True)
    subprocess.run(['git', 'commit', '-q', '-m', msg + '\n\nCo-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>'], cwd='../..', check=True)


def main():
    n, loop, streak, mod = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
    M = importlib.import_module(mod)
    with open('PREDICTIONS.md', 'a', encoding='utf-8') as f:
        f.write('\n\n# Set %d, registered before testing (26 October 2026): session-2 goal loop %d, %s (two hypotheses)\n\n%s\n' % (n, loop, M.TITLE, M.REG.strip()))
    git('indus: register set %d' % n, ['targets/indus/PREDICTIONS.md', 'targets/indus/%s.py' % mod])
    rd = R.Round('Set %d registered predictions: session-2 goal loop %d, %s' % (n, loop, M.TITLE), 'predict_test%d' % n)
    prog = bool(M.run(rd))
    rd.rec('P', 'progress rule', '', prog)
    rd.finish()
    ns = 0 if prog else streak + 1
    held = [k for k, ok in rd.res if ok and k != 'P']
    summary = getattr(M, 'SUMMARY', '')
    with open('PREDICTIONS.md', 'a', encoding='utf-8') as f:
        f.write('\n## Results of set %d (`%s.py`, `results/predict_test%d.md`)\n\nHeld: %s. %s Progress: %s (session-2 goal streak %d).\n' % (
            n, mod, n, ', '.join(held) or 'none', summary, 'yes' if prog else 'none', ns))
    with open('PROGRESS.md', 'a', encoding='utf-8') as f:
        f.write('| S2-%d | %d | %s | 86.3%% | 16.6%% (M+ 41.4%%) | 0 | 4 (L world 85.1%%) | %s: %s (%s; session-2 goal streak %d) |\n' % (
            loop, n, getattr(M, 'S', '4.559'), M.TITLE, summary.strip() or ('held ' + (', '.join(held) or 'none')), 'progress' if prog else 'no progress', ns))
    git('indus: set %d result (session-2 loop %d, streak %d)' % (n, loop, ns), ['targets/indus/PREDICTIONS.md', 'targets/indus/PROGRESS.md', 'targets/indus/results/predict_test%d.md' % n])
    print('STREAK', ns)


if __name__ == '__main__':
    main()
