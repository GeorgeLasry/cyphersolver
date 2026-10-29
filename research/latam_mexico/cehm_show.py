"""Print CEHM hits compactly: python cehm_show.py [regex-filter]"""
import json, re, sys, html
sys.stdout.reconfigure(encoding='utf-8')
o = json.load(open('cehm_hits.json', encoding='utf-8'))
pat = re.compile(sys.argv[1], re.I) if len(sys.argv) > 1 else None
def field(t, a, b):
    m = re.search(a + r' (.*?) (?:' + b + r')', t)
    return m.group(1).strip() if m else ''
for k, v in sorted(o.items(), key=lambda x: int(x[0])):
    t = html.unescape(v['text'])
    if pat and not pat.search(t):
        continue
    fondo = field(t, 'Fondo', 'Clasificaci')
    cl = field(t, r'Clasificaci\S+ \S+', 'Asunto|T\S+tulo')
    asunto = field(t, 'Asunto', 'Dirigido a|Firmado por|Lugar y Fecha|Tema|Tipo de documento|Formato')
    to = field(t, 'Dirigido a', 'Firmado por|Lugar y Fecha|Tema|Tipo')
    by = field(t, 'Firmado por', 'Lugar y Fecha|Tema|Tipo')
    lf = field(t, 'Lugar y Fecha', 'Tema|Tipo|Formato')
    print(f"{k} | {fondo[:40]} | {cl} | {by} -> {to} | {lf} | {v['terms']}\n   {asunto[:500]}")
