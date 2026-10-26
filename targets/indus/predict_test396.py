"""Set 396 (goal run loop 42): Wells's dividers (set 395) in the grammar and the roles. Writes results/predict_test396.md."""
import inspect

import progress as P
import rtools as R

DIV = {'2', '1', '60'}


def main():
    rd = R.Round('Three-hundred-and-ninety-sixth registered predictions: goal loop 42, dividers in the grammar and roles', 'predict_test396')
    DL, tr, te = P.data()
    g0 = P.grammar_margin(DL)
    src = inspect.getsource(P.grammar_margin).replace(
        "    f = lambda t: parse11(t, heads, hc, mc, labels, low, endp, openp) is not None",
        "    f0 = lambda t: parse11(t, heads, hc, mc, labels, low, endp, openp) is not None\n"
        "    def f(t):\n"
        "        if f0(t):\n"
        "            return True\n"
        "        cuts = [i for i in range(1, len(t) - 1) if t[i] in DIV and t[i - 1] not in R.NUMS and t[i + 1] not in R.NUMS]\n"
        "        if not cuts:\n"
        "            return False\n"
        "        segs, a = [], 0\n"
        "        for c in cuts:\n"
        "            segs.append(tuple(t[a:c]))\n"
        "            a = c + 1\n"
        "        segs.append(tuple(t[a:]))\n"
        "        return all(len(s) >= 1 and (f0(s) or len(s) == 1) for s in segs)")
    ns = dict(P.__dict__)
    ns['DIV'] = DIV
    ns['R'] = R
    exec(src, ns)
    g1 = ns['grammar_margin'](DL)
    ok1 = g1[0] > g0[0] and g1[1] > g0[1]
    rd.rec('GD1', 'the divider-split rule raises the G margin on A and B', 'A %.1f -> %.1f, B %.1f -> %.1f' % (100 * g0[0], 100 * g1[0], 100 * g0[1], 100 * g1[1]), ok1)
    r0 = P.roles(DL, edges=True, head2=True)[0]
    src2 = inspect.getsource(P.roles).replace("            num_before = g in R.NUMS\n            tot += 1",
        "            if role is None and g == '60' and 0 < i < len(t) - 1 and t[i - 1] not in R.NUMS and t[i + 1] not in R.NUMS:\n                role = 'divider'\n            num_before = g in R.NUMS\n            tot += 1")
    ns2 = dict(P.__dict__)
    exec(src2, ns2)
    r1, by, tot = ns2['roles'](DL, edges=True, head2=True)
    ok2 = r1 > r0
    rd.rec('GD2', "a 'divider' role for mid-line 60 raises R", 'R %.2f%% -> %.2f%% (%d tokens)' % (100 * r0, 100 * r1, by['divider']), ok2)
    rd.rec('P', 'progress rule: GD1 (the G benchmark moves on A and B)', 'GD1 %s' % ok1, ok1)
    rd.finish()


if __name__ == '__main__':
    main()
