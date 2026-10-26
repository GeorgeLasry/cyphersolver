"""Set 374 (goal run loop 20): Harappa period and material as domain models (ICIT fields 8, 13), split C. loopkit.py."""
import loopkit as L


def main():
    per, mat = L.field(8), L.field(13)
    L.run_domain_set_c(374, 'Three-hundred-and-seventy-fourth registered predictions: goal loop 20, period and material', [
        ('PM1', 'a period domain model (Harappa periods)', lambda t, m: per.get(t, '')),
        ('PM2', 'a material domain model', lambda t, m: mat.get(t, ''))])


if __name__ == '__main__':
    main()
