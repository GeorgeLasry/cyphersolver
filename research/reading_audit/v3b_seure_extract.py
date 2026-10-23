import re, sys, html
from html.parser import HTMLParser
class P(HTMLParser):
    def __init__(s):
        super().__init__(); s.letter=None; s.stack=[]; s.cur=None; s.out={}
    def handle_starttag(s,tag,a):
        a=dict(a)
        if tag=='section' and (a.get('id') or '').startswith('letter-'): s.letter=a['id'][7:]
        if tag=='div':
            cls=a.get('class') or ''
            if s.cur is None and 'passage' in cls.split() and a.get('lang') in ('fr','en'):
                s.cur={'lang':a.get('lang'),'cipher':'cipher-passage' in cls,'text':[],'depth':0}
            if s.cur is not None: s.cur['depth']+=1
        if tag in('p','br') and s.cur is not None: s.cur['text'].append('\n')
    def handle_endtag(s,tag):
        if tag=='div' and s.cur is not None:
            s.cur['depth']-=1
            if s.cur['depth']==0:
                s.out.setdefault(s.letter,[]).append((s.cur['lang'],s.cur['cipher'],''.join(s.cur['text'])))
                s.cur=None
    def handle_data(s,d):
        if s.cur is not None: s.cur['text'].append(d)
p=P(); p.feed(open(sys.argv[1],encoding='utf8').read())
import json; json.dump(p.out,open(sys.argv[2],'w',encoding='utf8'),ensure_ascii=False,indent=0)
for k,v in p.out.items(): print(k,len(v),sum(1 for l,c,_ in v if c))
