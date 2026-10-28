"""Decode the transcription with a key file (label value per line; 0 = null; ? or missing = unknown).
Prints each line as label=value pairs and as a letter string with unknowns shown as [label]."""
import sys


def main():
    tr, keyf = sys.argv[1], sys.argv[2]
    key = {}
    for l in open(keyf):
        l = l.split(';', 1)[0].strip()
        if not l: continue
        p = l.split()
        if len(p) >= 2: key[p[0]] = p[1]
    for l in open(tr):
        if l.startswith('#') or ':' not in l or l[:1] not in 'ABC': continue
        k, v = l.split(':', 1)
        out = []
        for t in v.split():
            if t.startswith('['): out.append(' ' + t.strip('[]').upper() + ' '); continue
            c = key.get(t, '?')
            out.append('' if c == '0' else (c if c != '?' else f'[{t}]'))
        print(f'{k}: {"".join(out)}')


if __name__ == '__main__':
    main()

