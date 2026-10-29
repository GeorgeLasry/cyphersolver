"""Filter hits.jsonl (RecordSearch title hits) to pre-1951 items that might hold ciphertext; writes review.tsv."""
import json, re
rows = [json.loads(l) for l in open('hits.jsonl', encoding='utf-8')]
def y0(r):
    m = re.search(r'\d{4}', r['dates']); return int(m.group()) if m else 9999
NOISE = re.compile(r'personnel|establishment|staff|clerk|officer|equipment|machine|typex|accommodation|salary|salaries|'
    r'allowance|appointment|promotion|recruit|training|course|vacanc|position|classification|pay\b|duties|overtime|'
    r'postcode|post code|zip|tariff|customs|bar ?code|colour code|morse|telegraph code|commercial code|'
    r'bentley|acme|a\.?b\.?c\.? code|furniture|building|room|safe\b|security of|procedure|instructions for|'
    r'distribution of|supply of|issue of|printing of|destruction|custody|accounting|charges|cost|rates|traffic code|'
    r'road|vehicle|music|film|sound|broadcast|police code|code of|award|signal code|flag|naval code of signals|'
    r'encoded archival|software|computer|electronic', re.I)
keep = []
for r in rows:
    if r['term'] == 'Somerton' or y0(r) > 1950: continue
    r['noise'] = bool(NOISE.search(r['title']))
    keep.append(r)
keep.sort(key=lambda r: (r['noise'], r['series'], r['ctrl']))
with open('review.tsv', 'w', encoding='utf-8') as f:
    for r in keep:
        f.write('\t'.join([r['bc'], r['series'], r['ctrl'], r['dates'], r['access'][:8], 'D' if r['dig'] else '', 'N' if r['noise'] else '', r['term'], r['title']]) + '\n')
print(len(rows), 'hits;', len(keep), 'pre-1951;', sum(not r['noise'] for r in keep), 'not noise')
