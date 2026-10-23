"""Decode f. 104r (DECODE R8725) with George Lasry's key "TNA SP106-8" (DECODE R924, file D3089) plus the additions
in f104_key_additions.tsv. Lasry's key file is DECODE's and his work: fetch it with decode_fetch.py into decode/
(git-ignored); it is not in the repository.

    python targets/rupert/f104_decode.py [decode/DOC_R924_D3089_3089.txt]

Prints each manuscript line as group=value; values from the additions are in lower case with a trailing '*'.
"""
import os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))


def lasry(path):
    k = {}
    for line in open(path, encoding='utf-8', errors='replace'):
        m = re.match(r'^([\w|]+)\s*-\s*(.+)$', line.strip())
        if m:
            for c in m.group(1).split('|'): k[c] = m.group(2).strip()
    return k


def additions():
    k = {}
    for line in open(os.path.join(HERE, 'f104_key_additions.tsv'), encoding='utf-8'):
        if line.startswith('#') or not line.strip(): continue
        g, v = line.split('\t')[:2]
        k[g] = v + '*'
    return k


def main(keypath=os.path.join(HERE, 'decode', 'DOC_R924_D3089_3089.txt')):
    k = lasry(keypath); k.update(additions())  # overrides Lasry only for 429 (his ASSUME?) and 116 (BROUGHT -> can)
    for n, line in enumerate(l for l in open(os.path.join(HERE, 'f104_transcription.txt'), encoding='utf-8')
                             if not l.startswith('#')):
        toks = re.findall(r'\d+|[()]', line)
        print(n + 1, '  '.join(t if t in '()' else '%s=%s' % (t, k.get(t, '?')) for t in toks))


if __name__ == '__main__':
    main(*sys.argv[1:2])
