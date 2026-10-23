"""Re-read brief (REREAD_BRIEF.md), batch b06: kurtz1639 (Kurz von Senftenau, Hamburg 1639; DECODE R3811-R3815,
R4625, R4645, R4734, R4736).

Targeted profile edits with the splice saver of relabel_r0.py (only changed spans are rewritten); one save per
appended solution step.

    python research/reading_audit/reread_b06.py
Helpers: b06_crop.py (crops of the DECODE images, scratchpad only), b06_align.py (word-by-word alignment of each
reading with its decode), b06_body_score.py (_check_reading.py on the reading body), b06_fix.py (logged label fixes),
b06_diag.py (failing sentences).
"""
import json
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from relabel_r0 import load, save  # noqa: E402

F = 'kurtz1639'
DATE = '2026-10-22'
BY = 'Claude Opus 5.5'
ROOT = pathlib.Path(__file__).resolve().parent.parent.parent
BASIS = ('the key decode (key.json as corrected 22 Oct 2026: 38 = d, Δ = nu, #dot = su, #s-long = ti, m = a) of the '
         'tr/ transcription after the label fixes in read/<rec>_corrections.tsv, made on full-resolution crops of the '
         'DECODE images; words separated and the reading aligned word by word with the decode (b06_align.py), '
         'supplied letters and words bracketed')

# filled in from the results: doc -> (grade, clean share, note)
READ = json.loads((pathlib.Path(__file__).parent / 'reread_b06_results.json').read_text(encoding='utf-8'))


def tokens():
    """Cipher tokens per record in the current tr/ files (parse.load, as decode.py reads them)."""
    sys.path.insert(0, str(ROOT / 'targets' / F))
    from parse import load as tload, ORDER
    return {r: [sum(len(x[1]) for x in tload([r])[0])] for r in ORDER}


def main():
    cov = tokens()
    total = sum(v[0] for v in cov.values())
    for d in [k for k in READ if not k.startswith('_')]:   # one save per document (the splice saver misorders several)
        p = load(F)
        t = [x for x in p['outcome']['texts'] if x['doc'] == d][0]
        r = READ[d]
        t['reading'] = 'read/%s_reading.md' % d
        t['translation'] = 'read/%s_en.md' % d
        extra = ['read/R3811_interlinear.md'] if d == 'R3811' else []   # corrections tsv sit beside, not listed
        t['decryption'] = [x for x in t['decryption'] if x not in extra] + [x for x in extra
                                                                            if (ROOT / 'targets' / F / x).exists()]
        if r.get('label'):
            t['label'] = r['label']
        if r['state'] == 'read':
            t['state'] = 'read'
            t.pop('note', None)
            t['reading_review'] = {'grade': r['grade'], 'by': BY, 'date': DATE,
                                   'note': r['note'] + ' Rests on ' + BASIS + '.'}
        else:
            t['state'] = 'decoded, not read'
            t['note'] = r['note']
        save(F, p)
    p = load(F)
    o = p['outcome']
    read_docs = ['R4734'] + [d for d, r in READ.items() if not d.startswith('_') and r['state'] == 'read']
    read_tok = sum(cov[d][0] for d in read_docs)
    frac = round(read_tok / total, 3)
    o['fraction_read'] = frac
    o['fraction_read_method'] = 'measured'
    o['fraction_read_source'] = (
        '22 Oct 2026, re-read batch b06: cipher tokens (parse.load over the corrected tr/ files) of the letters that read as sentences / all: '
        '%d / %d (%s). Before: 0.021 (R4734 only, reading audit). Withdrawn earlier: 0.999 (tokens with a value).'
        % (read_tok, total, ', '.join(sorted(read_docs))))
    o['gaps'] = READ['_gaps'][:1]
    o['notes'] = READ['_notes']
    if all(t.get('state', 'read') == 'read' for t in o['texts']):
        o['class'] = 'read'
    save(F, p)
    for g in READ['_gaps'][1:]:   # one save per appended gap
        p = load(F)
        if g not in p['outcome']['gaps']:
            p['outcome']['gaps'].append(g)
            save(F, p)
    for s in READ['_steps']:
        p = load(F)
        if any(x.get('what') == s['what'] for x in p['solution']):
            continue
        p['solution'].append(s)
        save(F, p)
    print('fraction_read', frac, read_tok, total, read_docs)


if __name__ == '__main__':
    main()
