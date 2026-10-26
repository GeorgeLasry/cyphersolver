"""Set 377 (goal run loop 23): seal-size band and number of sides as domain models, split C. loopkit.py."""
import loopkit as L


def band(v):
    try:
        x = float(v)
    except (TypeError, ValueError):
        return ''
    return '' if x <= 0 else ('s' if x < 20 else ('m' if x < 30 else 'l'))


def main():
    sz, sides = L.field(31), L.field(21)
    L.run_domain_set_c(377, 'Three-hundred-and-seventy-seventh registered predictions: goal loop 23, size and sides', [
        ('SZ1', 'a size-band domain model', lambda t, m: band(sz.get(t))),
        ('SZ2', 'a number-of-sides domain model', lambda t, m: sides.get(t, ''))])


if __name__ == '__main__':
    main()
