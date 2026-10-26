"""Set 356 (goal run loop 2): repetition caches for S. loopkit.py."""
import loopkit as L


def main():
    L.run_set(356, 'Three-hundred-and-fifty-sixth registered predictions: goal loop 2, repetition caches', [
        ('RC1', "the line's earlier signs as a cache", L.cache(lambda t, i: t[:i])),
        ('RC2', "the object's other lines as a cache", L.cache(lambda t, i: [g for ln in L.OTHERS.get(t, []) for g in ln]))])


if __name__ == '__main__':
    main()
