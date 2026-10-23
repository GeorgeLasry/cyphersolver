"""Mine the target profiles for patterns and new questions (Tao, Nature 22 Oct 2026: use AI to search a structured
set of problems for patterns and let those suggest what to try next, rather than only solving faster).

  python research/patterns/mine.py            writes research/patterns/REPORT.md and leads.csv

Reads every valid targets/<folder>/profile.json (famous targets skipped, as in the paper export) and docs/keys.json.
Three passes:
  1. leads     - for every open target (not read / read in part), the keys that read look-alike targets
                 (same country, within 15 years, same symbol kind) and have not been tried on it (keys.json "tried").
  2. systems   - how cipher features drift by country and quarter-century (homophones, nomenclator size, nulls,
                 word division), from the read targets only, so the numbers describe real systems.
  3. attacks   - which attack and which outcome method go with which system features, and how often a reading
                 already existed (the contamination question), per method.
Nothing here is a finding until a person checks it: a lead is a key worth trying, not a reading.
"""
import sys, csv, json, pathlib, collections as C, statistics as S

sys.stdout.reconfigure(encoding='utf-8', errors='replace')
ROOT = pathlib.Path(__file__).resolve().parents[2]
OUT = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / 'docs'))
import _check_profile as cp

OPEN = {'not read', 'read in part'}
READ = {'read', 'read in part', 'already solved'}

def num(v):
    try: return float(v)
    except (TypeError, ValueError): return None

def load():
    profs = {}
    for p in sorted((ROOT / 'targets').glob('*/profile.json')):
        f = p.parent.name
        if f in cp.cw.FAMOUS or cp.check(f, quiet=True)[0] != 'valid': continue
        profs[f] = json.loads(p.read_text(encoding='utf-8'))
    return profs

def obj(v):
    return v if isinstance(v, dict) else {}             # "unknown" stands in for an object in some profiles

def features(prof):
    sysm, docs = prof.get('system') or {}, prof.get('documents') or []
    years = [int(y) for d in docs if (y := num(d.get('year'))) and 1200 < y < 2000]
    countries = C.Counter(d.get('country') for d in docs if d.get('country') not in (None, '', 'unknown'))
    return {
        'year': round(S.median(years)) if years else None,
        'country': countries.most_common(1)[0][0] if countries else None,
        'symbols': sysm.get('symbol_kind'),
        'homophones': obj(sysm.get('homophones')).get('used'),
        'vowel_h': num(obj(sysm.get('homophones')).get('max_per_vowel')),
        'nomen': num(obj(sysm.get('nomenclator')).get('entries')),
        'nulls': obj(sysm.get('nulls')).get('present'),
        'words': sysm.get('word_division'),
        'class': (prof.get('outcome') or {}).get('class'),
        'method': (prof.get('outcome') or {}).get('method'),
        'attack': (prof.get('conditions') or {}).get('attack'),
        'prior': obj((prof.get('conditions') or {}).get('prior_solution')).get('exists'),
    }

def leads(profs, feat, kw):
    keys = {k['id']: k for k in kw['keys']}
    read_by = C.defaultdict(set)                            # key -> targets it read or helped read
    for l in kw['links']:
        if l['target'] in feat and feat[l['target']]['class'] in READ: read_by[l['key']].add(l['target'])
    tried = {(t['key'], t['target']) for t in kw['tried']} | {(l['key'], l['target']) for l in kw['links']}
    rows = []
    for t, f in feat.items():
        if f['class'] not in OPEN or not f['country'] or not f['year']: continue
        for k, done in read_by.items():
            if (k, t) in tried: continue
            near = [d for d in done if feat[d]['country'] == f['country'] and feat[d]['year']
                    and abs(feat[d]['year'] - f['year']) <= 15]
            if not near: continue
            same_sym = [d for d in near if feat[d]['symbols'] == f['symbols'] and f['symbols'] not in (None, 'unknown')]
            gap = min(abs(feat[d]['year'] - f['year']) for d in near)
            score = 2 * len(same_sym) + len(near) + (15 - gap) / 15
            rows.append({'target': t, 'class': f['class'], 'country': f['country'], 'year': f['year'],
                         'symbols': f['symbols'], 'key': k, 'key_label': keys.get(k, {}).get('label', ''),
                         'via': '; '.join(sorted(same_sym or near)), 'year_gap': gap, 'score': round(score, 2)})
    rows.sort(key=lambda r: (r['target'], -r['score']))
    best = C.defaultdict(list)
    for r in rows:
        if len(best[r['target']]) < 5: best[r['target']].append(r)
    return [r for t in sorted(best, key=lambda t: -best[t][0]['score']) for r in best[t]]

def systems(feat):
    rows = C.defaultdict(list)
    for f in feat.values():
        if f['class'] in READ and f['year'] and f['country']:
            rows[(f['country'], f['year'] // 25 * 25)].append(f)
    out = []
    for (c, q), fs in sorted(rows.items()):
        if len(fs) < 3: continue
        vh = [f['vowel_h'] for f in fs if f['vowel_h'] is not None]
        nm = [f['nomen'] for f in fs if f['nomen'] is not None]
        pct = lambda key, val=True: f"{100 * sum(1 for f in fs if f[key] == val) // len(fs)}%"
        out.append((c, f'{q}-{q + 24}', len(fs), pct('homophones'), f'{S.median(vh):g}' if vh else '-',
                    f'{S.median(nm):g}' if nm else '-', pct('nulls'), pct('words', 'kept')))
    return out

def attacks(feat):
    by = C.defaultdict(C.Counter)
    for f in feat.values():
        if f['method'] in (None, 'not applicable'): continue
        tag = ('homophonic' if f['homophones'] else 'monoalphabetic or unknown') + \
              (', nomenclator > 100' if (f['nomen'] or 0) > 100 else '')
        by[tag][f['method']] += 1
    prior = C.defaultdict(C.Counter)
    for f in feat.values():
        if f['method'] not in (None, 'not applicable'): prior[f['method']][f['prior'] or 'unknown'] += 1
    return by, prior

def table(head, rows):
    return '\n'.join(['| ' + ' | '.join(head) + ' |', '|' + '---|' * len(head)] +
                     ['| ' + ' | '.join(str(x) for x in r) + ' |' for r in rows])

def main():
    profs = load()
    feat = {f: features(p) for f, p in profs.items()}
    kw = json.loads((ROOT / 'docs' / 'keys.json').read_text(encoding='utf-8'))
    L = leads(profs, feat, kw)
    with open(OUT / 'leads.csv', 'w', newline='', encoding='utf-8') as fh:
        w = csv.DictWriter(fh, fieldnames=list(L[0]) if L else ['target'])
        w.writeheader(); w.writerows(L)
    sysrows = systems(feat)
    by, prior = attacks(feat)
    methods = sorted({m for c in by.values() for m in c})
    top = []
    for r in L:
        if r['target'] not in {x[0] for x in top}: top.append((r['target'], r['class'], r['country'], r['year'], r['key'], r['via'], r['score']))
    md = [
        '# Patterns across the target profiles', '',
        f'Generated by `research/patterns/mine.py` from {len(profs)} valid profiles and `docs/keys.json`. '
        'Regenerate after profile changes. A lead is a key worth trying on a target, not a reading: '
        'record every trial in the target\'s profile and in `keys.json` "tried" or "links", whatever the result.', '',
        '## 1. Untried keys for open targets', '',
        f'{len({r["target"] for r in L})} open targets have at least one untried key that read a look-alike target '
        '(same country, within 15 years; same symbol kind scores double). Best lead per target, strongest first; '
        'all leads (up to five per target) are in `leads.csv`.', '',
        table(['target', 'state', 'country', 'year', 'key', 'read look-alikes', 'score'], top[:40]), '',
        '## 2. How systems change by country and period', '',
        'Read targets only, groups of three or more. Vowel homophones and nomenclator size are medians.', '',
        table(['country', 'years', 'n', 'homophonic', 'max homophones per vowel', 'nomenclator entries', 'nulls', 'word division kept'], sysrows), '',
        '## 3. Which route works on which system', '',
        table(['system'] + methods, [[t] + [by[t][m] for m in methods] for t in sorted(by)]), '',
        '### Did a reading already exist? (by outcome method)', '',
        table(['method', 'no', 'in archive', 'in print', 'online', 'partial', 'unpublished', 'unknown'],
              [[m] + [prior[m][k] for k in ('no', 'in archive', 'in print', 'online', 'partial', 'unpublished', 'unknown')]
               for m in sorted(prior)]), '',
        '## Questions this raises', '',
        '- Work down section 1: each top lead is one decode run with an existing key file.',
        '- Section 2 dates cipher habits per chancery; an undated target whose features match a row is a dating hypothesis.',
        '- Section 3 says where ciphertext-only attacks actually succeeded; the paper should report it next to the '
        'contamination table, since a reading that already existed weakens a ciphertext-only claim.',
    ]
    (OUT / 'REPORT.md').write_text('\n'.join(md) + '\n', encoding='utf-8')
    print(f'{len(profs)} profiles, {len(L)} leads on {len({r["target"] for r in L})} open targets, '
          f'{len(sysrows)} country/period groups -> research/patterns/REPORT.md, leads.csv')

if __name__ == '__main__':
    main()
