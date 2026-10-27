"""Slice E triage: classify the cipher-word pass (kind 'word') snippets of RG 165 and RG 65.

    python research/nara_triage_e/triage.py            # writes strong.txt, weak.txt, counts to stdout

Every snippet is deduplicated on (objectId, word) and put in one class:
  strong  - names a message/letter in code or cipher that was intercepted, seized, submitted, found, enclosed,
            or not deciphered (regex STRONG within the snippet)
  boiler  - telegraph-form clause, cryptography training/personnel/course/code-book administration (regex BOILER)
  weak    - everything else (read by eye in weak.txt, shorter context)
"""
import json, re, os, collections

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, '..', 'nara_reels', 'out')

STRONG = re.compile(r"""(could\s*n[o']?t|couldn.t|unable\s+to|cannot|can\s*not|not\s+(?:be\s+|been\s+)?(?:deciph|decod|read|solv)
 |failed\s+to|impossible|undeciph|indeciph|undecod|not\s+yet\s+deciph|no\s+key
 |for\s+(?:decipher|decod|solution|translation|examination|analysis)|to\s+(?:be\s+)?(?:decipher|decod)|submitted|sent\s+for
 |intercept|seized|found\s+(?:on|in|among)|taken\s+from|confiscated|captured|enclosed?|encl\.
 |(?:letter|ltr|message|msg|telegram|wire|card|note|postcard|document)s?\s+(?:written\s+)?in\s+(?:code|cipher|cypher)
 |(?:cipher|cypher|code)\s+(?:letter|ltr|message|msg|telegram|note|card)s?
 |cryptogram|suspect\w*\s+(?:of\s+being\s+)?(?:code|cipher)|symbols|hieroglyph|mysterious)""", re.I | re.X)

BOILER = re.compile(r"""(errors\s+in\s+cipher|obscure\s+messages|repeated\s+telegram|unrepeated
 |course\s+in\s+cryptograph|school\s+of\s+(?:cryptograph|code)|instruction\s+in\s+(?:code|cipher|cryptograph)
 |commission(?:ed)?\s+.*cryptograph|appointment\s+as|applies?\s+for|application\s+for|commission\s+as)""", re.I | re.X)


def load(name):
    seen, rows = set(), []
    for l in open(os.path.join(OUT, name + '.jsonl'), encoding='utf-8'):
        d = json.loads(l)
        k = (d['objectId'], d['word'])
        if k in seen:
            continue
        seen.add(k)
        d['_src'] = name
        rows.append(d)
    return rows


def main():
    rows = load('rg_165_words') + load('rg_65_words')
    cls = collections.Counter()
    out = {'strong': [], 'weak': [], 'boiler': []}
    for d in rows:
        s = d['snippet'].replace('\n', ' ')
        if STRONG.search(s):
            c = 'strong'
        elif BOILER.search(s):
            c = 'boiler'
        else:
            c = 'weak'
        cls[(d['_src'], (d.get('microform') or ['-'])[0], c)] += 1
        out[c].append(d)
    for c, L in out.items():
        with open(os.path.join(HERE, c + '.txt'), 'w', encoding='utf-8') as f:
            for d in L:
                f.write(f"{d['_src']}\t{d['naId']}\t{d['file']}\t{d['title'][:50]}\t{d['word']}\t{d['snippet'].replace(chr(10), ' ')}\n")
    for k, v in sorted(cls.items()):
        print(*k, v)
    print({c: len(L) for c, L in out.items()})


if __name__ == '__main__':
    main()
