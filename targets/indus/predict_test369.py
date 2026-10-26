"""Set 369 (goal run loop 15): object subtype and region x type as domain models on top of type (split C). loopkit.py."""
import loopkit as L
import rtools as R


def main():
    L.run_domain_set_c(369, 'Three-hundred-and-sixty-ninth registered predictions: goal loop 15, subtype and region x type', [
        ('ST1', 'an object-subtype domain model', lambda t, m: L.SUBTYPE.get(t, '')),
        ('ST2', 'a region x type domain model', lambda t, m: (R.region(m.get(t, ('', '', ''))[0]), m.get(t, ('', '', ''))[1]))])


if __name__ == '__main__':
    main()
