"""Set 376 (goal run loop 22): object size band (ICIT field 31, longest dimension, mm) and workmanship (field 22). loopkit.py."""
import loopkit as L


def band(v):
    try:
        x = float(v)
    except ValueError:
        return ''
    return '' if x <= 0 else ('small' if x < 20 else ('medium' if x < 30 else 'large'))


def main():
    size, work = L.field(31), L.field(22)
    L.run_domain_set_c(376, 'Three-hundred-and-seventy-sixth registered predictions: goal loop 22, size and workmanship', [
        ('SZ1', 'a size-band domain model', lambda t, m: band(size.get(t, ''))),
        ('SZ2', 'a workmanship domain model', lambda t, m: work.get(t, '').lower())])


if __name__ == '__main__':
    main()
