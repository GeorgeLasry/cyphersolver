"""Check the hand-made reading against the table-built raw stream.

decode.py writes decryption/report_61005_raw.txt (values joined per manuscript line, [n] for an open group,
[?value] for a grade M value). decryption/report_61005_reading.txt is the French made from it by hand. This
script cuts both at their holes ([...]) and compares the stretches between holes on a consonant skeleton (vowels
dropped, repeated letters collapsed, accents off), so spelling choices (ri/re, ss/s, accents, apostrophes, word
division) are free but a word the table does not give is caught. It also compares the number of holes.

    python reading.py
"""
import os
import re
import sys
import unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
HOLE = re.compile(r'\[[^\]]*\]')


def skeleton(text):
    text = unicodedata.normalize('NFD', text.lower())
    letters = ''.join(c for c in text if c.isalpha() and not unicodedata.combining(c))
    letters = re.sub(r'[aeiouy]', '', letters)
    return re.sub(r'(.)\1+', r'\1', letters)


def body(path):
    return ' '.join(l.strip() for l in open(path, encoding='utf-8') if l.strip() and not l.startswith('#'))


def main():
    raw = ' '.join(re.sub(r'^L\d+\s', '', l.strip()) for l in open(
        os.path.join(HERE, 'decryption', 'report_61005_raw.txt'), encoding='utf-8')
        if l.strip() and not l.startswith('#'))
    reading = body(os.path.join(HERE, 'decryption', 'report_61005_reading.txt'))
    rc, rd = HOLE.split(raw), HOLE.split(reading)
    rh, dh = HOLE.findall(raw), HOLE.findall(reading)
    bad = 0
    if len(rh) != len(dh):
        print(f'hole count differs: raw {len(rh)}, reading {len(dh)}')
        bad += 1
    for i, (a, b) in enumerate(zip(rc, rd)):
        if skeleton(a) != skeleton(b):
            bad += 1
            print(f'chunk {i} (after hole {rh[i - 1] if i else "start"}): raw "{a.strip()}" vs reading "{b.strip()}"')
    for i, (a, b) in enumerate(zip(rh, dh)):
        da, db = re.sub(r'\D', '', a), re.sub(r'\D', '', b)
        if db and da != db:      # a reading hole may name a group only if it is that group; [?word] stands in for any
            print(f'hole {i}: raw {a} vs reading {b}')
            bad += 1
    words = len(re.findall(r"[^\W\d_]+(?:['’-][^\W\d_]+)*", HOLE.sub(' ', reading)))
    print(f'{len(rh)} holes in raw, {len(dh)} in reading; {words} words outside the holes; '
          + ('reading consistent with the table' if not bad else f'{bad} problem(s)'))
    return 1 if bad else 0


if __name__ == '__main__':
    sys.exit(main())
