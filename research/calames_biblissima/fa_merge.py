import json,re,glob
allh={}
for f in ['fa_hits.json']+sorted(glob.glob('fa_hits_*.json')):
    for c in json.load(open(f,encoding='utf-8')):
        allh.setdefault(c['url'],c).setdefault('terms',[])
json.dump(list(allh.values()),open('fa_all.json','w',encoding='utf-8'),ensure_ascii=False)
print(len(allh))
rx=re.compile(r"chiff|chifr|cifra|déchiff|écriture secr|cryptog",re.I)
noise=re.compile(r"chiffre d.affaire|chiffres? (clés?|arabes?|romains?)|en chiffres? (absolu|ronds)|statisti|recensement|monogramme|tableau chiffré|état chiffré|budget|devis|comptab|évaluation chiffrée|données chiffrées|résultats? chiffr|bilan chiffr|relevé chiffr|estimation chiffr|situation chiffrée|barème|rapport chiffré|données en chiffre|en chiffres$|Marque|Marqueur|numérot|activité chiffrée|étude chiffrée|liste.*chiffrée|documentation chiffrée|réponse chiffrée|comparaison chiffrée|signature|date.*chiffre",re.I)
def yr(c):
    m=re.match(r'(\d{4})',c.get('Période','')); return int(m.group(1)) if m else None
sel=[]
for c in allh.values():
    if c.get('Lieu de conservation','')=='Archives nationales': continue
    y=yr(c)
    if y and y>1950: continue
    s=c['title']+' '+c.get('Extrait de la notice','')
    if rx.search(s) and not noise.search(s): sel.append(c)
json.dump(sel,open('fa_sel2.json','w',encoding='utf-8'),ensure_ascii=False,indent=0)
print(len(sel))
