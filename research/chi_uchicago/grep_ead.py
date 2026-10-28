"""Full-text grep of the downloaded UChicago EAD finding aids for cipher terms.
Writes ead_hits.json: per hit, file, collection title, term, and the enclosing <c0x> component text."""
import glob, json, os, re, sys, html
here = os.path.dirname(os.path.abspath(__file__))
TERMS = [r'\bcipher', r'\bcypher', r'\bciphered\b', r'\bdecipher', r'\bdecypher', r'\bin code\b', r'\bcoded\b',
         r'\bcode (?:letter|telegram|message|book)', r'\bcryptogra', r'\bsecret writing', r'\bnomenclat',
         r'\bchiffr', r'\bcifra', r'\bcifrad', r'\bcryptic', r'\bcodebook', r'\bcode-book', r'\bsympathetic ink',
         r'\binvisible ink', r'\bencipher', r'\bencrypt', r'\bcryptanaly', r'\bgeheimschrift', r'\bverschl']
rx = re.compile('|'.join(TERMS), re.I)
tag = re.compile(r'<[^>]+>')
out, counts = [], {}
for p in sorted(glob.glob(os.path.join(here, 'ead', '*.xml'))):
    s = open(p, encoding='utf-8', errors='replace').read()
    t = re.search(r'<titleproper[^>]*>(.*?)</titleproper>', s, re.S)
    title = re.sub(r'\s+', ' ', tag.sub('', t.group(1))).strip() if t else ''
    for m in rx.finditer(s):
        term = m.group(0).lower()
        counts[term] = counts.get(term, 0) + 1
        a = max(s.rfind('<c0', 0, m.start()), s.rfind('<c ', 0, m.start()), s.rfind('<p>', 0, m.start()), m.start() - 600)
        b = min(x for x in [s.find('</c0', m.end()), s.find('</p>', m.end()), m.end() + 600] if x > 0)
        ctx = re.sub(r'\s+', ' ', html.unescape(tag.sub(' ', s[a:b]))).strip()
        out.append({'file': os.path.basename(p), 'title': title, 'term': term, 'ctx': ctx[:700]})
json.dump(out, open(os.path.join(here, 'ead_hits.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(out), 'hits in', len({o['file'] for o in out}), 'files')
print(sorted(counts.items(), key=lambda x: -x[1]))
