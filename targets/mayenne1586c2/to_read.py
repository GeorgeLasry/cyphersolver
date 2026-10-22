"""Put the three contributed Cipher-2 readings into one line format, so they can be measured with the same rule as
matignon1586c3 (targets/matignon1586c3/f276/scripts/measure.py: a sign counts read only inside a run of >= 3 lexicon
words totalling >= 10 letters, fr-1600-letters lexicon, shuffled-key control).

  f385_burford/   Brett Burford v0.2: signs.txt + key.json per page; a two-valued sign takes the value his decoder
                  recorded at that occurrence ('choices'), as his decode/decode.py does.
  f218_219_harumi/, f120_harumi/   Harumi-Matsuba: decoded_<page>.txt, the mechanical decode per line. Upper-case runs
                  are code or word signs (one token '=word'), lower-case letters one token each, [?] an unvalued
                  sign ('?'); in (a|b) the first alternative is kept.

Output: read_<page>.txt (L01: tokens). Then, for each page:
    python ../matignon1586c3/f276/scripts/measure.py read_<page>.txt 20
"""
import json, os, re

HERE = os.path.dirname(os.path.abspath(__file__))


def burford(page):
    d = os.path.join(HERE, 'f385_burford', page)
    step = json.load(open(os.path.join(d, 'key.json'), encoding='utf-8'))['pipeline'][0]
    table, choices = step['table'], step.get('choices', {})
    used, rows = {}, []
    for raw in open(os.path.join(d, 'signs.txt'), encoding='utf-8'):
        if not raw.strip() or raw.startswith('#'):
            continue
        _, _, signs = raw.rstrip('\n').partition('\t')
        toks = []
        for s in signs.split():
            e = table.get(s) or {}
            v = e.get('v')
            if isinstance(v, list):
                k = used.get(s, 0); used[s] = k + 1
                lst = choices.get(s, [])
                v = lst[k] if k < len(lst) else None
            if e.get('type') == 'divider' or v == '':
                continue
            if not v:
                toks.append('?')
            elif len(v) == 1:
                toks.append(v)
            else:
                toks.append('=' + v.replace('_', ''))
        rows.append(toks)
    return rows


def harumi(path):
    rows = []
    for raw in open(path, encoding='utf-8'):
        m = re.match(r'^c\d+\s+(.*)$', raw.rstrip('\n'))
        if not m:
            continue
        s = re.sub(r'\(([^|)]*)\|[^)]*\)', r'\1', m.group(1))      # (a|b) -> a
        s = re.sub(r'\[\?[^\]]*\]', ' ? ', s)                       # [?] -> ?
        toks = []
        for chunk in s.split():
            for run in re.findall(r'[A-Z]+|[a-z]|\?', chunk):
                if run == '?':
                    toks.append('?')
                elif run.isupper():
                    toks.append('=' + run.lower())
                else:
                    toks.append(run)
        rows.append(toks)
    return rows


def write(name, rows, note):
    with open(os.path.join(HERE, f'read_{name}.txt'), 'w', encoding='utf-8') as f:
        f.write(f'# {note} (to_read.py)\n')
        for i, toks in enumerate(rows, 1):
            f.write(f'L{i:02d}: ' + ' '.join(toks) + '\n')
    print(name, len(rows), 'lines', sum(len(t) for t in rows), 'tokens')


def main():
    docs = {'f385': [], 'f218_219': [], 'f120': []}
    for p in ('f385r', 'f385v'):
        rows = burford(p); docs['f385'] += rows
        write(p, rows, f'fr. 15573 {p[1:]}: Burford v0.2 signs through his key and recorded choices')
    for p in ('f218r', 'f218v', 'f219r'):
        rows = harumi(os.path.join(HERE, 'f218_219_harumi', f'decoded_{p}.txt')); docs['f218_219'] += rows
        write(p, rows, f'fr. 15572 {p[1:]}: Harumi-Matsuba mechanical decode')
    for p in ('f120r', 'f120v'):
        rows = harumi(os.path.join(HERE, 'f120_harumi', f'decoded_{p}.txt')); docs['f120'] += rows
        write(p, rows, f'fr. 15573 {p[1:]}: Harumi-Matsuba mechanical decode')
    for d, rows in docs.items():          # one file per document, pages in order (line numbers run on)
        write(d, rows, f'{d}: all pages of the document in order')


if __name__ == '__main__':
    main()
