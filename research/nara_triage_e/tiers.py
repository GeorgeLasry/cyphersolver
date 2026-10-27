"""Split the deduplicated word-pass snippets into reading tiers (after triage.py's classes).

    python research/nara_triage_e/tiers.py

tier1.txt  failure phrases (could not / unable to / undeciphered / not deciphered / no key ...) near cipher vocabulary
tier2.txt  submitted / for decipherment / seized / found on / intercepted / enclosed letter|message in code|cipher,
           within 150 chars of cipher vocabulary
rest.txt   everything else (read in chunks)
Near-identical windows (the same card summary repeated on cross-reference cards) are collapsed; the count of
repeats and every file name are kept.
"""
import json, re, os, collections
from triage import load, HERE

VOC = re.compile(r'cipher|cypher|\bcode|cryptogra|decod|secret\s+writ|symbols|hieroglyph|invisible|sympathetic|secret\s+ink', re.I)
FAIL = re.compile(r"could\s*n[o']?t|couldn.t|unable\s+to|cannot|can\s*not|not\s+(?:be\s+|been\s+|yet\s+)?(?:deciph|decod|solv|read)"
                  r"|failed|impossible|undeciph|indeciph|undecod|no\s+key|without\s+(?:the\s+)?key|unsolved|not\s+succe", re.I)
ACT = re.compile(r"for\s+(?:decipher|decod|solution|translation|examination|analysis)|to\s+(?:be\s+)?(?:decipher|decod)|submit"
                 r"|sent\s+for|intercept|seized|found\s+(?:on|in|among)|taken\s+from|confiscat|captured|enclos|encl\b|encl\."
                 r"|(?:letter|ltr|message|msg|telegram|wire|card|note|postcard|document)s?\s+(?:written\s+)?in\s+(?:code|cipher|cypher)"
                 r"|(?:cipher|cypher|code)\s+(?:letter|ltr|message|msg|telegram|note|card)s?|cryptogram|suspect", re.I)


def near(s, a, b, w=150):
    va = [m.start() for m in a.finditer(s)]
    vb = [m.start() for m in b.finditer(s)]
    return any(abs(x - y) <= w for x in va for y in vb)


def norm(s):
    return re.sub(r'[^a-z]', '', s.lower())[:160]


def main():
    rows = load('rg_165_words') + load('rg_65_words')
    tiers = {'tier1': collections.OrderedDict(), 'tier2': collections.OrderedDict(), 'rest': collections.OrderedDict()}
    for d in rows:
        s = d['snippet'].replace('\n', ' ')
        t = 'tier1' if near(s, FAIL, VOC) else 'tier2' if near(s, ACT, VOC) else 'rest'
        k = norm(s)
        e = tiers[t].setdefault(k, {'d': d, 'files': []})
        e['files'].append(f"{d['naId']}:{d['file']}")
    for t, od in tiers.items():
        with open(os.path.join(HERE, t + '.txt'), 'w', encoding='utf-8') as f:
            for i, e in enumerate(od.values()):
                d = e['d']
                f.write(f"#{i} {d['_src']} {(d.get('microform') or ['-'])[0]} {d['title'][:60]} | {' '.join(e['files'][:6])}"
                        f"{' +%d' % (len(e['files']) - 6) if len(e['files']) > 6 else ''}\n   {d['snippet'].replace(chr(10), ' ')}\n")
        print(t, len(od), sum(len(e['files']) for e in od.values()))


if __name__ == '__main__':
    main()
