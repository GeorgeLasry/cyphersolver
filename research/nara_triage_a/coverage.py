"""Per-publication coverage table for the README: items, flagged frames, frame classes, phrase hits kept."""
import csv, json, os, re, collections
HERE = os.path.dirname(os.path.abspath(__file__))
rows = list(csv.DictReader(open(os.path.join(HERE, 'frames.tsv'), encoding='utf-8'), delimiter='\t', quoting=csv.QUOTE_NONE))
items = collections.defaultdict(set); cls = collections.defaultdict(collections.Counter); par = {}
for r in rows:
    items[r['pub']].add(r['naId']); cls[r['pub']][r['cls']] += 1
ph = collections.Counter(); phk = collections.Counter()
BOIL = re.compile(r'obscure|obseure|errors? in|unrepeated|repeated|liable|tariff|transmission|non-delivery|delays|'
                  r'RECEIVED\s+IN\s+CI|SENT\s+IN\s+CI|TELEGRAM\s+RECEIVED', re.I)
for l in open(os.path.join(HERE, 'slice.jsonl'), encoding='utf-8'):
    d = json.loads(l)
    par.setdefault(d['pub'], ' > '.join(d.get('ancestors') or [])[-70:])
    if d['kind'] == 'phrase':
        ph[d['pub']] += 1
        if not BOIL.search(d['snippet']):
            phk[d['pub']] += 1
pubs = sorted(set(items) | set(ph), key=lambda p: -(sum(cls[p].values()) + ph[p]))
with open(os.path.join(HERE, 'coverage.tsv'), 'w', encoding='utf-8') as f:
    f.write('pub\tseries\titems\tframes\ttable\tcode\tmixed\tprose\tfew\tphrase_hits\tphrase_kept\n')
    for p in pubs:
        c = cls[p]
        f.write(f"{p}\t{par.get(p,'')}\t{len(items[p])}\t{sum(c.values())}\t{c['table']}\t{c['code']}\t{c['mixed']}\t"
                f"{c['prose']}\t{c['few']}\t{ph[p]}\t{phk[p]}\n")
print(len(pubs))
