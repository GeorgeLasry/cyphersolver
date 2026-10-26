"""Set 359 (goal run loop 5): line-length band and writing direction as domain models on top of region. loopkit.py."""
import loopkit as L


def main():
    L.run_domain_set(359, 'Three-hundred-and-fifty-ninth registered predictions: goal loop 5, line length and writing direction', [
        ('DL1', 'a length-band domain model', lambda t, m: min(max(len(t), 2), 6)),
        ('DL2', 'a writing-direction domain model', lambda t, m: L.DIRECTION.get(t, ''))])


if __name__ == '__main__':
    main()
