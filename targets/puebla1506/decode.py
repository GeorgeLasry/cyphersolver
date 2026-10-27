"""Decode the cipher passages of AGS PTR leg. 54 doc. 78 with Puebla's First Cipher (Tomokiyo's reconstruction).

    python decode.py            writes decryption.txt and prints the controls

Standard library only. Reads transcription.txt and key_first_cipher.tsv. Clear text [[...]] is copied through,
code groups {...} are looked up, unknown signs stay '?'. The controls repeat the check of 27 Oct 2026: the share of
the decoded letters covered by a small generic Spanish word list (rare content words left out), for the key, for
1000 shuffled keys and for the key on 1000 shuffled texts.
"""
import pathlib, random, re

HERE = pathlib.Path(__file__).resolve().parent
KEY, CODES = {}, {}
for line in (HERE / 'key_first_cipher.tsv').read_text(encoding='utf-8').splitlines():
    if line.startswith('#') or line.startswith('alias'):
        continue
    alias, sign, plain, status = line.split('\t')
    (CODES if alias.startswith('{') else KEY)[alias.strip('{}')] = plain.split(' / ')[0]


def lines():
    out = []
    for line in (HERE / 'transcription.txt').read_text(encoding='utf-8').splitlines():
        if line.startswith('#') or not line.strip():
            continue
        tag, text = line.split(None, 1)
        out.append((tag, text))
    return out


def parts(text):
    """[('clear', s) | ('code', g) | ('sign', t)] in order of the line."""
    out = []
    for m in re.finditer(r'\[\[(.*?)\]\]|\{([^}]*)\}(\[\?\])?|(\S+)', text):
        if m.group(1) is not None:
            out.append(('clear', m.group(1)))
        elif m.group(2) is not None:
            out.append(('code', m.group(2) + ('?' if m.group(3) else '')))
        else:
            out.append(('sign', m.group(4)))
    return out


def dec_sign(t, key):
    doubt = t.endswith('[?]')
    t = t.replace('[?]', '')
    if t.startswith('(') and t.endswith('?)'):
        return '(' + key.get(t[1:-2], '?') + ')'
    if t == '?':
        return '?'
    return key.get(t, '?') + ('[?]' if doubt else '')


def decode(text, key):
    out, run = [], ''
    for kind, x in parts(text):
        if kind == 'sign':
            run += dec_sign(x, key)
            continue
        if run:
            out.append(run)
            run = ''
        if kind == 'clear':
            out.append('[[' + x + ']]')
        else:
            out.append('{' + CODES.get(x.rstrip('?'), '?' + x) + ('?' if x.endswith('?') else '') + '}')
    if run:
        out.append(run)
    return ' '.join(out)


L = lines()
out = ['# Line-by-line decryption of transcription.txt with key_first_cipher.tsv (decode.py).',
       '# T = transcription, D = decryption. Decoded letters run on without word division (see reading.txt);',
       '# clear text in [[ ]], code values in { }, ? = unread sign, x[?] = doubtful sign, (x) = a sign that may be a descender.',
       '']
for tag, text in L:
    out += [f'{tag} T  {text}', f'{tag} D  {decode(text, KEY)}', '']
(HERE / 'decryption.txt').write_text('\n'.join(out) + '\n', encoding='utf-8', newline='\n')
print('\n'.join(out))

# controls
LEX = set('''a al el la lo los las le les de del que por su sus me mi se no y e en con es esta estas este esto aqui
van va veo ver mas muy bien tambien todo toda para como mucho mucha ser fue era sin sobre ya ha han hay pense dize
digo hazer gente rey reyna senor senora seria quien quando donde otro otra cosa cosas tiene tener propio cartas carta
personas algunas alguna ningun ninguna nada pedir dar tan tanto entre hasta despues ante sea son esa ese aquel
aquella'''.split())


def cover(s):
    n = len(s)
    best = [0] * (n + 1)
    for i in range(1, n + 1):
        best[i] = best[i - 1]
        for j in range(max(0, i - 14), i - 1):
            if s[j:i] in LEX:
                best[i] = max(best[i], best[j] + i - j)
    return best[n] / max(n, 1)


SECURE = ('l.14', 'l.15', 'l.16', 'l.17', 'l.18', 'l.19', 'l.20', 'l.24', 'l.25', 'l.26', 'l.29')
signs = []
for tag, text in L:
    if tag in SECURE:
        signs.append([x.replace('[?]', '') for k, x in parts(text)
                      if k == 'sign' and x != '?' and not x.startswith('(')])


def score(key, rows):
    return cover(''.join(key.get(x, '') for r in rows for x in r))


true = score(KEY, signs)
random.seed(1)
al, vals = list(KEY), list(KEY.values())
rk = sorted(score(dict(zip(al, random.sample(vals, len(vals)))), signs) for _ in range(1000))
rt = sorted(score(KEY, [random.sample(r, len(r)) for r in signs]) for _ in range(1000))
print(f'CONTROL word-list cover: key {true:.3f}; 1000 shuffled keys max {rk[-1]:.3f} median {rk[500]:.3f}; '
      f'key on 1000 shuffled texts max {rt[-1]:.3f} median {rt[500]:.3f}')

# Shared language model (lang/README.md): Early Modern Spanish, character 5-grams without spaces, 'early' norm.
# Mean log-prob per character of the decoded runs (ll. 14-29), for the key, 1000 shuffled keys and the key on
# 1000 shuffled texts; and best_language() on the decode. Needs numpy; skipped if lang/ cannot load.
try:
    import sys
    sys.path.insert(0, str(HERE.parent.parent))
    from lang import lm
except Exception as e:  # pragma: no cover
    print('CONTROL lm: skipped,', e)
else:
    M = lm.load('es-golden-age', order=5, spaces=False)

    def lmscore(key, rows):
        tot = n = 0
        for r in rows:
            s = lm.norm(''.join(key.get(x, '') for x in r), 'early')
            if len(s) > 5:
                tot += M.per_char(s) * len(s)
                n += len(s)
        return tot / n

    random.seed(2)
    tl = lmscore(KEY, signs)
    lk = sorted(lmscore(dict(zip(al, random.sample(vals, len(vals)))), signs) for _ in range(1000))
    lt = sorted(lmscore(KEY, [random.sample(r, len(r)) for r in signs]) for _ in range(1000))
    print(f'CONTROL es-golden-age per char: key {tl:.3f}; 1000 shuffled keys best {lk[-1]:.3f} median {lk[500]:.3f}; '
          f'key on 1000 shuffled texts best {lt[-1]:.3f} median {lt[500]:.3f}')
    # language ID needs word division: use the word-divided reading (reading.txt), holes and markup removed
    rd = (HERE / 'reading.txt').read_text(encoding='utf-8').split('## Reading', 1)[1]
    rd = re.sub(r'\[\?[^\]]*\]|\[\.\.\.\]|\{[^}]*\}|ll?\. [\d-]+:', ' ', rd)
    print('CONTROL best_language (reading.txt):', ', '.join(f'{m} {s:.3f}' for s, m in lm.best_language(rd)[:4]))
