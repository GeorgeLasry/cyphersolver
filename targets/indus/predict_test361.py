"""Set 361 (goal run loop 7): skip-bigram and previous sign x distance from end as context models. loopkit.py."""
import loopkit as L


def main():
    L.run_set(361, 'Three-hundred-and-sixty-first registered predictions: goal loop 7, two context features', [
        ('CX1', 'a skip-bigram', L.ctx_model(lambda t, i: ('skip', t[i - 2] if i >= 2 else '<s>'))),
        ('CX2', 'previous sign x distance from the end', L.ctx_model(lambda t, i: (t[i - 1] if i else '<s>', min(len(t) - i, 4))))])


if __name__ == '__main__':
    main()
