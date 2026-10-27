"""Backfill the 'posted' timestamp in docs/_dates.json from git history.

'posted' (UTC, to the second) is when a write-up was submitted. _build_site.py stamps it the first time a build
sees a new page; pages older than that field get the commit time of the commit that first added docs/<slug>.html.
Pages that already have 'posted' are left alone. Needs the full history (not a shallow clone).

    python tools/backfill_posted.py            # fill missing 'posted' fields
    python tools/backfill_posted.py --dry-run  # show what would change
"""
import datetime, json, pathlib, subprocess, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATES = ROOT / 'docs' / '_dates.json'


def first_added():
    """{slug: unix time} of the earliest commit that added docs/<slug>.html."""
    out = subprocess.run(['git', 'log', '--diff-filter=A', '--name-only', '--format=@%ct', '--', 'docs/*.html'],
                         cwd=ROOT, capture_output=True, text=True, encoding='utf-8', check=True).stdout
    seen, t = {}, None
    for line in out.splitlines():
        if line.startswith('@'):
            t = int(line[1:])
        elif line.startswith('docs/') and line.endswith('.html') and line.count('/') == 1:
            slug = line[5:-5]
            seen[slug] = t if slug not in seen else min(seen[slug], t)   # log is newest first; keep the earliest
    return seen


def main():
    dry = '--dry-run' in sys.argv
    d = json.loads(DATES.read_text(encoding='utf-8'))
    added = first_added()
    n = missing = 0
    for slug, rec in d['pages'].items():
        if rec.get('posted'):
            continue
        t = added.get(slug)
        if t is None:
            missing += 1
            continue
        rec['posted'] = datetime.datetime.fromtimestamp(t, datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
        n += 1
    print(f'{n} pages given a posted time; {missing} without a commit adding them')
    if not dry:
        DATES.write_text(json.dumps(d, indent=1, sort_keys=True, ensure_ascii=False) + '\n', encoding='utf-8')


if __name__ == '__main__':
    main()
