"""Set 368 (goal run loop 14): motif on top of region + length + type (split C), and site (split A -> B). loopkit.py."""
import loopkit as L
import rtools as R


def main():
    L.run_domain_set_c(368, 'Three-hundred-and-sixty-eighth registered predictions: goal loop 14 (part 1), motif on top of type', [
        ('MT1', 'a motif domain model on top of type', lambda t, m: m.get(t, ('', '', ''))[2])])
    L.run_domain_set(3680, 'Three-hundred-and-sixty-eighth registered predictions: goal loop 14 (part 2), site on top of type', [
        ('MT2', 'a site domain model on top of type', lambda t, m: m.get(t, ('', '', ''))[0])])


if __name__ == '__main__':
    main()
