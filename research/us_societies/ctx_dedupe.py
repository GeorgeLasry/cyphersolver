import sys,re
seen=set(); last={}
for l in open(sys.argv[1],encoding='utf-8'):
    cid,title,ctx=l.rstrip('\n').split('\t',2)
    if re.search(r'ciphering|cyphering|Cypher, [A-Z]\.|swiss code|zip code|code of conduct|honor code|penal code|civil code|decipher(?:ing)? (?:the )?(?:hand|writing)|difficult to decipher|illegible',ctx,re.I) and not re.search(r'in cipher|in code|cipher letter|secret cipher|cryptogram|coded message',ctx,re.I): continue
    mid=ctx[200:330]
    k=(cid,mid[:60])
    if k in seen: continue
    if cid in last and abs(len(last[cid]))>0 and mid[:40] in last[cid]: continue
    seen.add(k); last[cid]=last.get(cid,'')+mid
    print(cid,'|',title[:40],'|',ctx[120:480])
