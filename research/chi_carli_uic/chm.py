import requests,time,json,re
B='https://collections.carli.illinois.edu/digital/bl/dmwebservices/index.php?q='
for t in ['enciphered','encoded','secret','cryptic','telegraphic','shorthand','invisible','symbols','nomenclator','cypher','ciphered','cipher','deciphered','code']:
    for al in ['chm_fa','dom_papal','dom_literary','uni_mmc','uis_msc','lfc_sc001']:
        d=requests.get(f'{B}dmQuery/{al}/CISOSEARCHALL^{t}^all^and/title!date/nosort/50/1/0/0/0/0/json',timeout=60).json()
        tot=d['pager']['total']
        print(al,t,tot, [ (r['pointer'],r['title'][:50]) for r in d['records'][:6]] if 0<int(tot)<=12 else '')
        time.sleep(3)
