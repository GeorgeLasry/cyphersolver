"""Collect ANRI finding-aid PDF links (anri.go.id/download/...) via the site search; writes finding_aids.json."""
import re, json, time
from fetch import get
KW=['inventaris','daftar arsip','algemene secretarie','binnenlands bestuur','residentie','residensi','kabinet','jepang','1942','1945','1946','1947','1948','1949',
 'republik','sekretariat negara','kementerian pertahanan','delegasi','RVO','NEFIS','Rapporten','Mailrapporten','Gouvernements','Hoge Regering','VOC','Raad van Indie',
 'telegram','geheim','Departement','Indonesia Timur','Negara','Oorlog','Leger','KNIL','marine','Politiek','Recomba','Kepolisian','arsip tekstual','guide','sarana bantu','microfilm','K ']
found={}
for kw in KW:
    for page in range(1,6):
        t=get('https://anri.go.id/search',params={'keyword':kw,'page':page}).text
        ls=set(re.findall(r'/download/[a-z0-9.-]+',t))
        new=[l for l in ls if l not in found]
        for l in ls: found.setdefault(l,kw)
        if not new: break
        time.sleep(0.5)
    print(kw,len(found),flush=True)
json.dump(found,open('finding_aids.json','w'),indent=0)
