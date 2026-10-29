"""Crude Spanish/Italian syllabifier for counts (not for hyphenation): one vowel run per syllable, a single
consonant or a stop+liquid / ch / ll / rr cluster opens the next syllable."""
import re

ONSETS = ('bl', 'br', 'cl', 'cr', 'dr', 'fl', 'fr', 'gl', 'gr', 'pl', 'pr', 'tr', 'ch', 'll', 'rr')


def syl(w):
    parts = re.findall(r'[^aeiou]*[aeiou]+', w)
    if not parts:
        return [w]
    parts[-1] += w[len(''.join(parts)):]
    out = [parts[0]]
    for p in parts[1:]:
        cl, rest = re.match(r'([^aeiou]*)(.*)', p).groups()
        k = len(cl) - 2 if len(cl) >= 2 and cl[-2:] in ONSETS else max(0, len(cl) - 1)
        out[-1] += cl[:k]
        out.append(cl[k:] + rest)
    return out
