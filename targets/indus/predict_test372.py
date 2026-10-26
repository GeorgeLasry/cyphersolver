"""Set 372 (as run: BASE_DOMAINS then began with region; loopkit since changed) (goal run loop 18): does region still add beyond type + subtype (ablation), and length x subtype. loopkit.py."""
import loopkit as L
import rtools as R


def main():
    region = L.BASE_DOMAINS[0]
    L.BASE_DOMAINS = L.BASE_DOMAINS[1:]
    try:
        L.run_domain_set(372, 'Three-hundred-and-seventy-second registered predictions: goal loop 18 (part 1), region on top of length + type + subtype', [
            ('AB1', 'region re-added on top of the type models', region[0])])
    finally:
        L.BASE_DOMAINS = [region] + L.BASE_DOMAINS
    L.run_domain_set_c(3720, 'Three-hundred-and-seventy-second registered predictions: goal loop 18 (part 2), length x subtype', [
        ('AB2', 'a length x subtype domain model', lambda t, m: (min(max(len(t), 2), 6), L.SUBTYPE.get(t, '')))])


if __name__ == '__main__':
    main()
