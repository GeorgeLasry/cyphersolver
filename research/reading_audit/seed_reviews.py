"""Write research/reading_audit/reviews.json: the reading audit's grade per target (22 Oct 2026).

docs/_texts.py reading_problems() takes a target's audit grade A or B as the reading_review of every 'read' entry
that has none of its own, so the 227 readings the audit passed are not refused for lack of a review. A review recorded
on the entry itself (profile.json outcome.texts[].reading_review) always wins; C, D and N grades are not reviews.
    python research/reading_audit/seed_reviews.py
"""
import glob, json, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent.parent
OUT = ROOT / 'research' / 'reading_audit' / 'reviews.json'
BY = 'Claude Sonnet 5.5 (reading audit, research/reading_audit/)'


def main():
    rows = {}
    for f in sorted(glob.glob(str(ROOT / 'research' / 'reading_audit' / 'llm' / 'out_*.jsonl'))):
        for line in open(f, encoding='utf-8'):
            if not line.strip(): continue
            try: r = json.loads(line)
            except ValueError: continue
            if r.get('grade') in ('A', 'B', 'C', 'D', 'N'): rows[r['folder']] = r
    out = {folder: {'grade': r['grade'], 'by': BY, 'date': '2026-10-22',
                    'docs_read': [str(x) for x in r.get('docs_checked') or []],
                    'note': (r.get('why') or '')[:600], 'fix': r.get('fix') or ''}
           for folder, r in sorted(rows.items())}
    OUT.write_text(json.dumps(out, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print(len(out), 'targets ->', OUT.relative_to(ROOT))


if __name__ == '__main__':
    main()
