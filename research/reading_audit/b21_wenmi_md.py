"""b21: write targets/numeric1916/texts/<family>_reading.md and _en.md from b21_wenmi.py's body, and score the body.

    python -I -X utf8 research/reading_audit/b21_wenmi_md.py <scratch_dir> <family>

Score (Chinese is 'not scored' by _check_reading.py): the explicit-hole measure of b17_score.py HOLES=1, with each
character taken as a word (classical telegram Chinese is close to one word per character): sentences cut at 。？！；
(and at the end of each telegram), a hole is [?x] or […]; a sentence is clean when holes <= max(1, chars // 10).
"""
import json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
S, fam = Path(sys.argv[1]), sys.argv[2]
TEXTS = ROOT / 'targets' / 'numeric1916' / 'texts'
page = json.loads((S / f'page_{fam}.json').read_text(encoding='utf-8'))['messages']
blocks = re.findall(r'^### (\S+)\t([^\n]*)\n(.*?)\n\n', (S / f'{fam}_reading_body.txt').read_text(encoding='utf-8'), re.S | re.M)

HOLE = re.compile(r'\[\?[^\]]*\]|\[…\]')


def score(text):
    sents = [x for x in re.split(r'[。？！；]', text) if x.strip()]
    clean = n_h = n_c = 0
    for s in sents:
        h = len(HOLE.findall(s))
        c = len(re.findall(r'[㐀-鿿]', HOLE.sub('', s))) + h
        n_h += h; n_c += c
        if c and h <= max(1, c // 10): clean += 1
    return clean, len(sents), n_h, n_c


NAME = {'gongmi': '共密', 'rongmi': '容密'}
tot = [0, 0, 0, 0]
body, en = [], []
for mid, meta, txt in blocks:
    p = page[mid]
    c = score(txt)
    tot = [a + b for a, b in zip(tot, c)]
    body.append(f'### {mid}\n\n{txt}\n')
    tr = p['translation'] or ''
    en.append(f'### {mid}\n\n{tr}\n')
    print(mid, c)
share = tot[0] / tot[1]
print('TOTAL clean', tot[0], '/', tot[1], round(share, 3), 'holes', tot[2], 'chars', tot[3])
hdr = f"""# {NAME[fam]} ({fam}), {len(blocks)} telegrams, June-July 1916: reading

Re-read 23 Oct 2026 (Claude Opus 5.5; REREAD_BRIEF, batch b21). What it rests on: Brice Dudout's proposed readings on
his Wenmi pages (bdudout.github.io/wenmi/en/{fam}.html, fetched 23 Oct 2026; CC BY 4.0, attributed), checked group by
group against our independent decoder (`decode.py`) on the digits of his page tables, which are newer than the
repository's `groups.tsv` (see `{fam}_reread_log.md`). Every character of the reading is the figure's own value under the
key, except: a character in [brackets] is supplied from context (no one-digit variant of its group gives it); [?x] is
the figure's value kept but not understood, or a partly carried conjecture; […] is an illegible group. Characters
that rest on a one-digit alternate of the group (a digit read differently from the police copy, often 一/二/三) are
unbracketed and listed in `{fam}_align.tsv` (kind 'one-digit alternate'). Punctuation is Dudout's.

Score of the body: Chinese is not scored by `_check_reading.py`; explicit holes only, one character = one word
(`research/reading_audit/b21_wenmi_md.py`): {tot[0]}/{tot[1]} sentences clean ({share:.2f}), {tot[2]} holes in {tot[3]} characters.

## Reading

"""
(TEXTS / f'{fam}_reading.md').write_text(hdr + '\n'.join(body), encoding='utf-8')
(TEXTS / f'{fam}_en.md').write_text(f"""# {NAME[fam]} ({fam}): English

Brice Dudout's translations from his Wenmi page (bdudout.github.io/wenmi/en/{fam}.html, CC BY 4.0), copied 23 Oct 2026 and
adjusted where the b21 reading differs (noted per telegram). Holes as in `{fam}_reading.md`.

""" + '\n'.join(en), encoding='utf-8')
