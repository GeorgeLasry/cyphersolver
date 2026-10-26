"""Set 375 (goal run loop 21): secondary motif and workmanship (ICIT fields 19, 22), split C. loopkit.py."""
import loopkit as L


def main():
    sec, wk = L.field(19), L.field(22)
    L.run_domain_set_c(375, 'Three-hundred-and-seventy-fifth registered predictions: goal loop 21, secondary motif and workmanship', [
        ('SM1', 'a secondary-motif domain model', lambda t, m: sec.get(t, '')),
        ('SM2', 'a workmanship domain model', lambda t, m: wk.get(t, ''))])


if __name__ == '__main__':
    main()
