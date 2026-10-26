"""Set 375 (goal run loop 20): shape and secondary motif (ICIT fields 15, 19), split C. loopkit.py."""
import loopkit as L


def main():
    per, mat = L.field(15), L.field(19)
    L.run_domain_set_c(375, 'Three-hundred-and-seventy-fifth registered predictions: goal loop 21, shape and secondary motif', [
        ('SH1', 'a shape domain model', lambda t, m: per.get(t, '')),
        ('SH2', 'a secondary-motif domain model', lambda t, m: mat.get(t, ''))])


if __name__ == '__main__':
    main()
