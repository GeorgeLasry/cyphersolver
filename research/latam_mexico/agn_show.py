"""Print AGN Guía hits compactly, skipping the 20th-c. DGIPS 'Telegrama cifrado' boilerplate: python agn_show.py [term]"""
import json, re, sys
sys.stdout.reconfigure(encoding='utf-8')
h = json.load(open('agn_hits.json', encoding='utf-8'))
term = sys.argv[1] if len(sys.argv) > 1 else None
kw = re.compile(r'(?i)(cifr|clave|descifr|cripto|jerogl|simp[aá]tic|contrase)')
for k, v in h.items():
    if term and term not in v['terms']:
        continue
    d = v.get('desc', '')
    if 'Investigaciones Políticas y Sociales' in d:
        continue
    i = d.find('Título'); path = d[:i].replace('Archivo General de la Nación / ', '')
    f = re.search(r'Fecha\(s\): ([^,]*)', d)
    m = kw.search(d[i:]); j = i + m.start() if m else i
    print(f"* {path[-120:]}| {d[i:i+45]} | {f.group(1) if f else ''} | {v['terms']}\n   {d[max(i,j-220):j+160]}\n   id={k}")
