"""VERIFY_BRIEF pass 3, morosini1588: profile edits after the word-by-word check.

    PYTHONUTF8=1 python research/reading_audit/verify3_morosini_profile.py <stats.json> [--dry]

stats.json from reread_b00_stats.py (run after verify3_morosini_apply.py). For every enclosure with a reading_review:
the note is rebuilt with reread_b00.note_for (fresh counts and scores) and "verified word by word 22 Oct 2026: N words
bracketed, M replaced" appended (counts from verify3_morosini_apply.E). Records below the bar (DOWN) go to
"decoded, not read" with a note; entries are matched by their label ("R27, ..."), since all share doc "meister40-set".
Saved with relabel_r0.save (only the changed spans are rewritten).
"""
import json, sys, pathlib

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from relabel_r0 import load, save  # noqa: E402
from reread_b00 import note_for  # noqa: E402
from verify3_morosini_apply import E  # noqa: E402

F = 'morosini1588'
DOWN = {'R27', 'R51', 'R57'}


def counts():
    c = {}
    for rec, f, pre, old, new, suf, kind in E:
        if f != 'r':
            continue
        b, m = c.get(rec, (0, 0))
        c[rec] = (b + (kind in 'SLP'), m + (kind == 'R'))
    return c


def main():
    stats = json.load(open(sys.argv[1], encoding='utf-8'))
    dry = '--dry' in sys.argv
    cnt = counts()
    p = load(F)
    for t in p['outcome']['texts']:
        r = t.get('label', '').split(',')[0]
        if r not in stats or 'reading_review' not in t:
            continue
        s = stats[r]
        b, m = cnt.get(r, (0, 0))
        new = (note_for(r, s) + f' Verified word by word 22 Oct 2026 (merged-letter alignment, '
               f'verify3_morosini_diag.py): {b} words bracketed, {m} replaced.')
        old = t['reading_review']['note']
        if dry:
            print('==', r, '\nOLD', old, '\nNEW', new)
        t['reading_review']['note'] = new
        if r in DOWN:
            note = (f"Verified word by word 22 Oct 2026: after bracketing, _check_reading.py on the reading body {s['after']} "
                    f"(below the ~0.58 bar): {s['unread']} unread stretches and {s['partly']} partly carried words in "
                    f"{s['words']} words leave sentences open. Kept as a partial reading (texts/{r}_reading.md, _en.md). "
                    f"Blocker: the transcription (no image pass of the doubtful lines yet); Rome's decipherments "
                    f"(ASV Francia 27) not imaged.")
            items = list(t.items())
            nt = {}
            for k, v in items:
                if k in ('state', 'note'):
                    continue
                nt[k] = v
                if k == 'doc':
                    nt['note'] = note
            nt['state'] = 'decoded, not read'
            # keep the original key order for state where it was
            order = [k for k, _ in items if k != 'note']
            out = {}
            for k in order:
                out[k] = nt[k]
                if k == 'doc':
                    out['note'] = note
            t.clear(); t.update(out)
    if not dry:
        save(F, p)
        print('saved')


if __name__ == '__main__':
    main()
