"""Set 367 (goal run loop 13): object type and motif domain models, replicated on split C (Mahadevan's lines carry no
type or motif). loopkit.py."""
import loopkit as L


def main():
    L.run_domain_set_c(367, 'Three-hundred-and-sixty-seventh registered predictions: goal loop 13, object type and motif on split C', [
        ('OT1', 'an object-type domain model', lambda t, m: m.get(t, ('', '', ''))[1]),
        ('OT2', 'a motif domain model', lambda t, m: m.get(t, ('', '', ''))[2])])


if __name__ == '__main__':
    main()
