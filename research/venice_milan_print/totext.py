import re,sys,html
for f in sys.argv[1:]:
    t=open(f,'rb').read().decode('utf-8','replace')
    t=re.sub(r'(?is)<(script|style).*?</\1>','',t)
    t=re.sub(r'(?i)<br\s*/?>|</p>|</li>|</h\d>|</tr>','\n',t)
    t=re.sub(r'(?i)<a [^>]*href="([^"]+)"[^>]*>',r' [\1] ',t)
    t=html.unescape(re.sub(r'<[^>]+>','',t))
    t=re.sub(r'[ \t]+',' ',t); t=re.sub(r'\n\s*\n+','\n',t)
    open(f.replace('.htm','.txt'),'w',encoding='utf-8').write(t)
