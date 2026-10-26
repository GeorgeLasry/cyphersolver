"""Set 373 (goal run loop 19): the opening sign's family / the opening sign as domain keys (position 0 unseen). loopkit.py."""
import loopkit as L
from famlm import fam


def main():
    L.run_domain_set(373, 'Three-hundred-and-seventy-third registered predictions: goal loop 19, opening-sign domains', [
        ('OD1', "the opening sign's family as domain", lambda t, m: fam(t[0])),
        ('OD2', 'the opening sign as domain', lambda t, m: t[0])], skip0=True)


if __name__ == '__main__':
    main()
