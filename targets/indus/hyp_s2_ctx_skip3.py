"""Session-2 goal loop: context feature for S, the sign three back (loopkit.ctx_model, S rule with sign tokens, fixed split and A -> B)."""
import loopkit as L
import rtools as R
from famlm import fam

TITLE = 'the sign three back'
REG = """A context model p(sign | the sign three positions back), mixed onto the S base (length, type, subtype, length x subtype); uses only earlier signs
(`hyp_s2_ctx_skip3.py`, `loopkit.ctx_model`).

- **CT1** S on the fixed test falls by 0.005+ and sign-token bits fall.
- **CT2** S on A -> B falls and sign-token bits fall.
- Progress rule: CT1 and CT2."""
SUMMARY = ''


def run(rd):
    global SUMMARY
    (a0, a1, la), (b0, b1, lb) = L.test_pair(L.ctx_model(lambda t, i: ('s3', t[i - 3] if i >= 3 else '<s>')))
    (sa0, sa1), (sb0, sb1) = L.SIGNS_ONLY
    ok1 = a0 - a1 >= 0.005 and sa1 < sa0
    ok2 = b1 < b0 and sb1 < sb0
    rd.rec('CT1', 'fixed test', 'S %.4f -> %.4f (weight %.2f), signs %.4f -> %.4f' % (a0, a1, la, sa0, sa1), ok1)
    rd.rec('CT2', 'A -> B', 'S %.4f -> %.4f (weight %.2f), signs %.4f -> %.4f' % (b0, b1, lb, sb0, sb1), ok2)
    SUMMARY = 'fixed gain %.4f, A -> B gain %.4f.' % (a0 - a1, b0 - b1)
    return ok1 and ok2
