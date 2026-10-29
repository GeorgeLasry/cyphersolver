"""scopeArchiv full-text search (Swiss cantonal archives). usage: scope.py BASE term -> prints hit count + first page titles"""
import re,sys,html,requests
def hidden(t): return {m.group(1): html.unescape(m.group(2)) for m in re.finditer(r'<input type="hidden" name="([^"]+)" id="[^"]*" value="([^"]*)"', t)}
def fields(t): return re.findall(r'name="(ctl00[^"]*)"',t)
if __name__=='__main__':
    B=sys.argv[1]; s=requests.Session(); s.headers['User-Agent']='Mozilla/5.0 (research)'
    r=s.get(B+'volltextsuche.aspx',timeout=60); print(r.status_code,r.url,len(r.text))
    print([f for f in fields(r.text) if 'txt' in f or 'cmd' in f][:20])
