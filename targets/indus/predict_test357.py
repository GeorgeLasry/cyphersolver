"""Set 357 (goal run loop 3): motif and region domain models for S. loopkit.py."""
import loopkit as L
import rtools as R


def main():
    L.run_set(357, 'Three-hundred-and-fifty-seventh registered predictions: goal loop 3, domain models', [
        ('DM1', 'a motif-domain model', L.domain_model(lambda t, m: m.get(t, ('', '', ''))[2])),
        ('DM2', 'a region-domain model', L.domain_model(lambda t, m: R.region(m.get(t, ('', '', ''))[0])))])


if __name__ == '__main__':
    main()
