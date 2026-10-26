"""Set 362 (goal run loop 8): previous sign x length band; the opening sign's family x position. loopkit.py."""
import loopkit as L
from famlm import fam


def main():
    L.run_set(362, 'Three-hundred-and-sixty-second registered predictions: goal loop 8, previous sign x length, opening family', [
        ('CY1', 'previous sign x length band', L.ctx_model(lambda t, i: (t[i - 1] if i else '<s>', min(max(len(t), 2), 6)))),
        ('CY2', "the opening sign's family x position", L.ctx_model(lambda t, i: ('open', fam(t[0]) if i else '<s>', min(i, 5))))])


if __name__ == '__main__':
    main()
