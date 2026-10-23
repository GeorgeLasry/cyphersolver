"""rakoczi1711 R483: put the clerk's interlinear stretches and the clear passages in reading order, line by line.
Reads targets/rakoczi1711/tr/R483_p*.txt (or the corrected tr file given as argv[1]); prints one line per manuscript
line: cipher runs replaced by the next '|' segment of the P: line, clear passages in <...>. Flags lines where the
number of cipher runs and of P segments differ (MISMATCH)."""
import re, sys, glob, os
T = r'C:/Users/dbour/cypher/.worktrees/reading-gate/targets/rakoczi1711/tr/'
files = sys.argv[1:] or sorted(glob.glob(T + 'R483_p*.txt'))
for fn in files:
    print('[%s]' % os.path.basename(fn))
    P = None
    n = 0
    for raw in open(fn, encoding='utf-8'):
        line = raw.rstrip('\n')
        if line.startswith('P:'):
            P = line[2:].strip()
        elif line.startswith('C:'):
            n += 1
            c = line[2:].strip()
            parts = re.split(r'(\{clear:.*?\})', c)
            items = []
            for part in parts:
                if part.startswith('{clear:'):
                    items.append(('clr', part[7:-1].strip()))
                elif re.search(r'\d', part):
                    items.append(('cip', part.strip()))
            segs = [] if (P is None or P.startswith('(none)')) else [s.strip() for s in P.split('|')]
            runs = sum(1 for k, _ in items if k == 'cip')
            out = []
            i = 0
            for k, v in items:
                if k == 'clr':
                    out.append('<' + v + '>')
                else:
                    out.append(segs[i] if i < len(segs) else '{' + v + '}')
                    i += 1
            flag = '' if runs == len(segs) else '  ##MISMATCH runs=%d segs=%d' % (runs, len(segs))
            print('%02d %s%s' % (n, ' '.join(out), flag))
            P = None
