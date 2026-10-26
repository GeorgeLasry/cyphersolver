"""Marked / base sign pairs from Parpola's sign descriptions (set 351): a sign whose CISI description starts with
another sign's full description and adds to it (P212 'triangle, with serifed T on top, caged by ...' over P211)
is that sign plus a mark. The added text is sorted into device types by keyword. ICIT glyphs through cisi.p2icit."""
import re
from collections import defaultdict

import cisi

TYPES = [('cage', r'\bcaged?\b'), ('cap', r'\bcapped\b|\btable\b|\broof\b|\bhat\b'), ('hatch', r'hatch|stripe'),
         ('leaf', r'\bleaf|\bleaves\b|\btree\b|\bbranch|sprout|sheaf|sheaves'),
         ('stroke', r'\bstrokes?\b|\bbars?\b|\blines?\b|\bdivider\b|\bdots?\b|\bticks?\b'),
         ('attach', r'.')]


def norm(d):
    return re.sub(r'[^a-z ]', ' ', d.lower()).split()


def device(extra):
    for name, rx in TYPES:
        if re.search(rx, extra.lower()):
            return name


def pairs():
    sg = cisi.signs()
    p2i = cisi.p2icit()
    nd = {p: norm(d) for p, (d, ms) in sg.items() if p != 'P000'}
    out = []
    for m, dm in nd.items():
        best = None
        for b, db in nd.items():
            if b != m and len(db) >= 2 and len(dm) > len(db) and dm[:len(db)] == db:
                if best is None or len(db) > len(nd[best]):
                    best = b
        if best:
            extra = ' '.join(dm[len(nd[best]):])
            gm, gb = p2i.get(m, set()), p2i.get(best, set())
            if gm and gb and not gm & gb:
                out.append({'marked': m, 'base': best, 'extra': extra, 'type': device(extra), 'gm': gm, 'gb': gb})
    return out


if __name__ == '__main__':
    by = defaultdict(list)
    for p in pairs():
        by[p['type']].append(p)
    for t, ps in by.items():
        print(t, len(ps))
        for p in ps:
            print('   %s<%s %s / %s : %s' % (p['marked'], p['base'], sorted(p['gm']), sorted(p['gb']), p['extra'][:70]))
