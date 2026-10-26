"""Set 360 (goal run loop 6): depth band and the line's place on its object as domain models. loopkit.py."""
import loopkit as L


def main():
    L.run_domain_set(360, 'Three-hundredth-and-sixtieth registered predictions: goal loop 6, period and place on the object', [
        ('DP1', 'a depth-band domain model', lambda t, m: L.DEPTH.get(t, '')),
        ('DP2', "a line-place domain model", lambda t, m: L.PLACE.get(t, ''))])


if __name__ == '__main__':
    main()
