"""Set 427 (goal run loop 73): audit of the object-kind models against site: base = length + site, then subtype;
base = length + type + subtype + length x subtype, then site again (set 368 MT2 for comparison). Split C.
Writes results/predict_test427.md and predict_test4270.md."""
import loopkit as L


def main():
    saved = L.BASE_DOMAINS
    length = saved[0]
    site = (lambda t, m: m.get(t, ('', '', ''))[0], 0.2)
    L.BASE_DOMAINS = [length, site]
    try:
        L.run_domain_set_c(427, 'Four-hundred-and-twenty-seventh registered predictions: goal loop 73, subtype on top of length + site', [
            ('KS1', 'subtype on top of length + site', lambda t, m: L.SUBTYPE.get(t, ''))])
    finally:
        L.BASE_DOMAINS = saved


if __name__ == '__main__':
    main()
