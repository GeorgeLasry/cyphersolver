"""Set 358 (goal run loop 4): site and object-type domain models on top of the region base. loopkit.py."""
import loopkit as L


def main():
    L.run_domain_set(358, 'Three-hundred-and-fifty-eighth registered predictions: goal loop 4, site and object type on top of region', [
        ('DS1', 'a site-domain model', lambda t, m: m.get(t, ('', '', ''))[0]),
        ('DS2', 'an object-type domain model', lambda t, m: m.get(t, ('', '', ''))[1])])


if __name__ == '__main__':
    main()
