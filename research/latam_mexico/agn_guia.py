"""Search the AGN México Guía General (guiageneral.agn.gob.mx) for cipher vocabulary and fetch each hit's description.

The Guía's search box calls ajax/arbol2.php?id=%23&buscar=<term>, which returns a flat jstree list of matching
descriptive units; ajax/contenido.php?idref=<id> returns the unit's description (path, title, dates, scope).
Writes agn_hits.json (one object per unit, with the terms that found it). Polite: 1.5 s between requests.

    python research/latam_mexico/agn_guia.py [term ...]
"""
import html, json, os, re, sys, time, urllib.parse, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'agn_hits.json')
BASE = 'https://guiageneral.agn.gob.mx/ajax/'
UA = {'User-Agent': 'Mozilla/5.0 (cipher catalogue research; polite)'}
# The search ORs the words of a phrase ('carta cifrada' = carta OR cifrada: 71,574 hits), so single words only.
TERMS = ['cifra', 'cifrada', 'cifradas', 'cifrado', 'cifrados', 'clave', 'claves', 'criptografía', 'criptograf',
         'jeroglífico', 'jerogl', 'contraseña', 'descifrar', 'descifrado', 'descifrada', 'descifr', 'cifrar',
         'chiffre', 'cifras', 'simpática', 'criptograma', 'cifrador']


def get(url):
    for attempt in range(3):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=90) as r:
                return r.read().decode('utf-8', 'replace')
        except Exception as e:
            print('  retry', attempt, e, flush=True)
            time.sleep(5)
    return ''


def describe(idref):
    t = get(BASE + 'contenido.php?' + urllib.parse.urlencode({'idref': idref}))
    t = re.sub(r'<script.*?</script>|<style.*?</style>', ' ', t, flags=re.S)
    t = html.unescape(re.sub(r'<[^>]+>', ' ', t))
    t = re.sub(r'\s+', ' ', t)
    i = t.find('Archivo General de la Nación')
    t = t[i:] if i >= 0 else t
    j = t.find('(function(){')
    return (t[:j] if j >= 0 else t).strip()


def main(terms):
    hits = json.load(open(OUT, encoding='utf-8')) if os.path.exists(OUT) else {}
    for term in terms:
        js = get(BASE + 'arbol2.php?' + urllib.parse.urlencode({'id': '#', 'buscar': term}))
        time.sleep(1.5)
        try:
            nodes = json.loads(js)
        except Exception:
            print('bad json for', term, js[:200]); continue
        print(f'{term!r}: {len(nodes)} hits', flush=True)
        for n in nodes:
            h = hits.setdefault(n['id'], {'id': n['id'], 'text': n['text'], 'terms': []})
            if term not in h['terms']:
                h['terms'].append(term)
            if 'desc' not in h:
                h['desc'] = describe(n['id'])
                time.sleep(1.0)
                if sum(1 for x in hits.values() if 'desc' in x) % 25 == 0:
                    json.dump(hits, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
        json.dump(hits, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)


if __name__ == '__main__':
    main(sys.argv[1:] or TERMS)
