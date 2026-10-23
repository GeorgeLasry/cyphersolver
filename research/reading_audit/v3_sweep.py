"""v3 sweep (23 Oct 2026): rescore every read document with v2_score (conjectures and supplied words as holes).

    python research/reading_audit/v3_sweep.py > research/reading_audit/v3_sweep.tsv

One row per outcome.texts entry whose state is read: folder, index, doc, language, reading file, plain score,
explicit-hole score, hole rate, words, flag. flag is "below" when the explicit-hole score is under 0.60, "plain-only"
when only the plain score is under 0.60, "no-reading" when the entry names no reading file, "missing" when the file
is not there.
"""
import json, pathlib, sys
ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'docs')); sys.path.insert(0, str(ROOT / 'research' / 'reading_audit'))
import _texts, v2_score as v2
import _check_reading as cr

print('folder\tidx\tdoc\tlang\treading\tplain\tholes\thole_rate\twords\tflag')
for p in sorted((ROOT / 'targets').glob('*/profile.json')):
    try:
        d = json.loads(p.read_text(encoding='utf8'))
    except Exception:
        continue
    for i, t in enumerate((d.get('outcome') or {}).get('texts') or []):
        if _texts.entry_state(t) != 'read':
            continue
        lang = (t.get('language') or '').split('-')[0] or None
        files = cr.listify(t.get('reading')) or cr.listify(t.get('decryption'))
        row = [p.parent.name, str(i), '/'.join(map(str, cr.listify(t.get('doc')))), lang or '?', '']
        best = None
        for r in files:
            f = p.parent / str(r)
            if str(r).startswith('http') or not f.exists() or f.suffix.lower() in ('.pdf', '.json'):
                continue
            b = v2.holes(v2.body_of(f.read_text(encoding='utf8', errors='replace')))
            lg = lang or cr.score_text(b)['lang']
            if not lg:
                continue
            cr.lexicon(lg)
            try:
                pl, h = v2.score(b, lg, False), v2.score(b, lg, True)
            except Exception:
                continue
            if h['clean_share'] is None or pl['clean_share'] is None:
                continue
            if best is None or h['clean_share'] > best[2]['clean_share']:
                best = (str(r), pl, h, lg)
        if not files:
            print('	'.join(row + ['', '', '', '', 'no-text'])); continue
        if best is None:
            print('	'.join(row[:4] + ['|'.join(map(str, files)), '', '', '', '', 'unscored'])); continue
        r, pl, h, lg = best
        row[3], row[4] = lg, r
        flag = 'below' if h['clean_share'] < 0.60 else ('plain-only' if pl['clean_share'] < 0.60 else '')
        print('	'.join(row + [str(pl['clean_share']), str(h['clean_share']), str(h['hole_rate']), str(h['words']), flag]))
