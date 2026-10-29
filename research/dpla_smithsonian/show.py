import sys,json
from load import *
rows=json.load(open(sys.argv[1])); hubs=sys.argv[2].split(',')
S=re.compile(r'cipher|cypher|cryptogra|secret writ|\bin code\b|coded|code ?book|secret alphabet|encipher|code (letter|message|telegram|key)',re.I)
for x in rows:
    if hub(x) not in hubs and not (hubs==['*']): continue
    t=text(x); m=S.search(t); a=max(0,m.start()-60)
    print(x['id'][:6],hub(x)[:8],'|',(x['title'] or [''])[0][:60],'|',year(x),'|',','.join(x['type'])[:10],'|',t[a:m.end()+60].replace('\n',' '))
