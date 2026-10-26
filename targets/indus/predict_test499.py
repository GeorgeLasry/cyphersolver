"""Set 499 (goal run loop 145): audit of set 430's core size signs with motif strata. Writes results/predict_test499.md."""
import auditkit
import rtools as R


def main():
    rd = R.Round('Four-hundred-and-ninety-ninth registered predictions: goal loop 145, audit of the core size signs against the animal', 'predict_test499')
    o1, p1 = auditkit.size_motif(lambda t: '706' in t)
    rd.rec('CS1', '706 leans to large seals with motif held', 'odds ratio %.2f, p = %.4f' % (o1, p1), o1 > 1 and p1 < 0.05)
    o2, p2 = auditkit.size_motif(lambda t: bool({'156', '400', '590'} & set(t)))
    rd.rec('CS2', '156 / 400 / 590 lean to small seals with motif held', 'odds ratio %.2f, p = %.4f' % (o2, p2), o2 < 1 and p2 < 0.05)
    rd.rec('P', 'progress rule: none (audit of set 430)', '', False)
    rd.finish()


if __name__ == '__main__':
    main()
