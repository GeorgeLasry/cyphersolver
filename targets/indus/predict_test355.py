"""Set 355 (goal run loop 1): the object's field motif and its object type as side information for S. loopkit.py."""
import loopkit as L


def main():
    L.run_set(355, 'Three-hundred-and-fifty-fifth registered predictions: goal loop 1, motif and object type as context', [
        ('GM1', "the field motif conditions the signs", L.unigram_given(lambda t, m: m.get(t, ('', '', ''))[2])),
        ('GM2', "the object type conditions the signs", L.unigram_given(lambda t, m: m.get(t, ('', '', ''))[1]))])


if __name__ == '__main__':
    main()
