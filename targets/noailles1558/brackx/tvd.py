"""Raw decode of the transcription with a key, three lines per cipher line (nothing edited by hand):
T: the sign labels, V: the value of each sign (0 null, ? none, {x} tentative), D: the decoded letters
(unknowns as [label], tentative stretches as {x}). Also writes the key as a TSV with a status column.
usage: tvd.py transcription key out_decode out_key_tsv"""
import sys


def load(keyf):
    key = {}
    for l in open(keyf):
        if not l.strip() or l.lstrip().startswith(';'): continue
        body, _, basis = l.partition(';')
        p = body.split()
        if len(p) >= 2: key[p[0]] = (p[1], basis.strip(), 'tentative' in basis.lower() and 'tentative there' not in basis.lower())
    return key


def main():
    tr, keyf, out, outk = sys.argv[1:5]
    key = load(keyf)
    lines, used, tent_tok, tok, valued = [], {}, 0, 0, 0
    for l in open(tr):
        if l.startswith('#') or ':' not in l or l[:1] not in 'ABC': continue
        name, seq = l.split(':', 1)
        T, V, D = [], [], []
        for t in seq.split():
            if t.startswith('['):
                T.append(t); V.append(t); D.append(' ' + t.strip('[]').upper() + ' '); continue
            tok += 1; used[t] = used.get(t, 0) + 1
            v, _, tent = key.get(t, ('?', '', False))
            T.append(t)
            if v == '?': V.append('?'); D.append(f'[{t}]'); continue
            valued += 1
            shown = '' if v == '0' else v
            if tent: tent_tok += 1; V.append('{' + v + '}'); D.append('{' + shown + '}' if shown else '')
            else: V.append(v); D.append(shown)
        w = max(len(x) for x in T + V)
        lines += [f'{name}', 'T: ' + ' '.join(x.ljust(w) for x in T).rstrip(),
                  'V: ' + ' '.join(x.ljust(w) for x in V).rstrip(), 'D: ' + ''.join(D), '']
    head = [f'# raw decode of {tr} with {keyf}; {tok} sign tokens, {valued} with a value, '
            f'{tent_tok} of them on tentative values; nothing edited by hand', '']
    open(out, 'w').write('\n'.join(head + lines))
    with open(outk, 'w') as f:
        f.write('label\tvalue\tstatus\ttokens\tbasis\n')
        for k, (v, b, tent) in key.items():
            f.write(f'{k}\t{v}\t{"tentative" if tent else "firm"}\t{used.get(k, 0)}\t{b}\n')
    print(tok, valued, tent_tok, sum(1 for v in key.values() if v[2]))


if __name__ == '__main__':
    main()

