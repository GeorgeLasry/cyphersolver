"""Parse Mazzatinti, Inventario dei manoscritti italiani ... t. II (1887), the Archivio Sforzesco codices
(BnF italien 1583-1596), and list the items marked "In cifre" with codex, year and folio.
Input: archive.org OCR text (InventarioDeiManoscrittiItalianiT2_djvu.txt). Output: sforza_cifre.json."""
import json, re, sys
src, out = sys.argv[1], sys.argv[2]
lines = open(src, encoding='utf-8', errors='replace').read().split('\n')
start = next(i for i, l in enumerate(lines) if l.strip().startswith('(Cod. 1583)'))
end = next(i for i, l in enumerate(lines) if l.strip().startswith('Cod. 1596'))
cod, year, items, cur = 1583, None, [], None
noise = re.compile(r'Digitized by|^\s*\d{3}\s*$|APPENDICE|INVENT[AÀ]RIO', re.I)
for l in lines[start:end]:
    s = l.strip()
    m = re.match(r'\(?Cod\. (15\d\d)\)?\.?', s)
    if m:
        cod = int(m.group(1)); continue
    m = re.match(r'a\. (1[45]\d\d)\.?', s)
    if m:
        year = int(m.group(1)); continue
    if not s or noise.search(s):
        continue
    m = re.match(r'(?:f\s*[.,#]\s*|£\s*|^)(\d{1,3}(?:\s*-\s*\d{1,3})?)\s*\.\s+(.*)', s)
    if m and (s.startswith(('f', '£')) or re.match(r'\d', s)):
        if cur: items.append(cur)
        cur = {'cod': cod, 'year': year, 'f': m.group(1).replace(' ', ''), 'text': m.group(2)}
    elif cur:
        cur['text'] += ' ' + s
if cur: items.append(cur)
for it in items:
    it['text'] = re.sub(r'-\s+', '', it['text'])
cif = [it for it in items if re.search(r'cifr', it['text'], re.I)]
json.dump({'all': len(items), 'cifre': cif}, open(out, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(items), 'items;', len(cif), 'with cifr')

# second pass: flag a cipher item whose next item is a "Traduzione" (decipherment filed after it)
for i, it in enumerate(items):
    it['cipher'] = bool(re.search(r'cifr', it['text'], re.I)) and not re.match(r'(Traduzione|Spiegazion|Alfabeto)', it['text'])
    nxt = items[i + 1]['text'] if i + 1 < len(items) else ''
    it['trad_next'] = bool(re.match(r'Traduzione', nxt))
    it['is_trad'] = bool(re.match(r'Traduzione', it['text']))
json.dump(items, open(out.replace('.json', '_all.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
c = [it for it in items if it['cipher']]
print('cipher items', len(c), 'with Traduzione next', sum(it['trad_next'] for it in c),
      'Traduzione items', sum(it['is_trad'] for it in items))
