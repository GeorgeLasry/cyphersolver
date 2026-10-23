"""Publish the target profiles as an open dataset in docs/data/ (Tao, Nature 22 Oct 2026: a structured set of problems
others can mine for patterns, and open tooling the field does not have to get from an AI company).

  python docs/_export_dataset.py

Writes docs/data/targets.csv (one row per document), docs/data/profiles.jsonl (one profile per line, as recorded),
docs/data/codebook.md and docs/data/README.md. Unlike the paper export it keeps contributed results (flagged by
outcome.provenance), but it only takes targets that are already public: a published page (a live PAGES entry, or a
README results row linking a page) and no withheld texts (outcome.texts_withheld; fr. 3029/3092 and the like).
"""
import sys, csv, json, pathlib, datetime

sys.stdout.reconfigure(encoding='utf-8', errors='replace')
HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent
OUT = HERE / 'data'
sys.path.insert(0, str(HERE))
import _check_profile as cp
import _export_profiles as ep
cw = cp.cw

def published():
    """Folders whose result is on the site: a live page named after the folder, or a README row linking a live page."""
    pages, _, _ = cw.manifest()
    live = {s for s in pages if (HERE / f'{s}.html').exists()}
    out = {s for s in live}
    for r in cw.readme_rows():
        if r['slugs'] & live:
            out |= {d.rstrip('/').split('/')[-1] for d in r['dirs']}
    return out

def main():
    OUT.mkdir(exist_ok=True)
    live = published()
    rows, kept, left = [], [], {'withheld': [], 'not published': [], 'invalid': []}
    for p in sorted((ROOT / 'targets').glob('*/profile.json')):
        f = p.parent.name
        if f in cw.FAMOUS: continue
        prof = json.loads(p.read_text(encoding='utf-8'))
        if (prof.get('outcome') or {}).get('texts_withheld'): left['withheld'].append(f); continue
        if f not in live: left['not published'].append(f); continue
        if cp.check(f, quiet=True)[0] != 'valid': left['invalid'].append(f); continue
        kept.append(prof)
        base = {'target': f, 'title': prof['title'], 'page': f'{cw.SITE}{f}.html'
                if (HERE / f'{f}.html').exists() else ''}
        for sect in ('system', 'conditions', 'outcome'): ep.flat(prof[sect], sect, base)
        steps = prof['solution'] if isinstance(prof['solution'], list) else []
        base['solution.steps'] = len(steps)
        base['solution.kinds'] = '; '.join(s.get('kind', '') for s in steps if isinstance(s, dict))
        base['solution.failed_steps'] = sum(1 for s in steps if isinstance(s, dict) and s.get('result') in ('failed', 'ruled out'))
        base['documents.count'] = len(prof['documents'])
        for d in prof['documents']: rows.append({**base, **ep.flat(d, 'doc', {})})
    cols = []
    for r in rows:
        for k in r:
            if k not in cols: cols.append(k)
    with open(OUT / 'targets.csv', 'w', newline='', encoding='utf-8') as fh:
        w = csv.DictWriter(fh, fieldnames=cols); w.writeheader(); w.writerows(rows)
    with open(OUT / 'profiles.jsonl', 'w', encoding='utf-8') as fh:
        for prof in kept: fh.write(json.dumps(prof, ensure_ascii=False) + '\n')
    (OUT / 'codebook.md').write_text(ep.codebook(cols), encoding='utf-8')
    (OUT / 'README.md').write_text(f"""# cyphersolver profiles dataset

{len(kept)} historical cipher targets, {len(rows)} documents. Exported {datetime.date.today().isoformat()} by
`docs/_export_dataset.py` from `targets/<folder>/profile.json` (schema: `profile.schema.json`).

- `profiles.jsonl`: one profile per line, as recorded: the cipher system, the documents, what the model was given,
  every solution step (failed ones included), and the outcome with George Lasry's method categories.
- `targets.csv`: the same flattened to one row per document; `codebook.md` explains every column.

Only targets with a published write-up are included, and none whose texts are withheld. `"unknown"` means the field
could not be established; it is never a guess. `outcome.provenance` says whether the result is the project's own or
was contributed. `conditions.prior_solution` records whether a reading existed before the attempt. Readings are
claims to check against the images linked from each page, not settled facts.

Patterns mined from these profiles: `research/patterns/REPORT.md` in the repository.
""", encoding='utf-8')
    print(f'{len(kept)} profiles, {len(rows)} document rows -> docs/data/')
    for k, v in left.items():
        if v: print(f'left out ({k}, {len(v)}): ' + ', '.join(v[:12]) + (' ...' if len(v) > 12 else ''))

if __name__ == '__main__':
    main()
