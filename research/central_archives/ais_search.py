"""Full-text search of the Austrian State Archives Archivinformationssystem (scopeArchiv ASP.NET postback).
python ais_search.py TERM [outdir]  -> writes the result-list HTML pages and prints hits (title, date, VEID link)."""
import re, sys, os, html, requests
B = 'https://www.archivinformationssystem.at/'
def hidden(t):
    return {m.group(1): html.unescape(m.group(2)) for m in re.finditer(r'<input type="hidden" name="([^"]+)" id="[^"]*" value="([^"]*)"', t)}
def search(term):
    s = requests.Session(); s.headers['User-Agent'] = 'Mozilla/5.0 (research)'
    r = s.get(B + 'volltextsuche.aspx', timeout=60)
    d = hidden(r.text); d['ctl00$cphMainArea$txtMitAllenWoertern'] = term; d['ctl00$cphMainArea$cmdSuchen'] = 'Suchen'
    r = s.post(B + 'volltextsuche.aspx', data=d, timeout=120)
    return s, r
if __name__ == '__main__':
    s, r = search(sys.argv[1])
    out = sys.argv[2] if len(sys.argv) > 2 else '.'
    open(os.path.join(out, 'ais_' + re.sub(r'\W', '_', sys.argv[1]) + '.html'), 'w', encoding='utf-8').write(r.text)
    print(r.url, len(r.text))
