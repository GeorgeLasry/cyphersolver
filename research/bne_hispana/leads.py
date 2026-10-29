import requests,json,re
ids=['172694','186678','186690','173169','172763','172678','141369','064262','173419','172732','172704','186680','186675','042230','045663','172697','172729','186643','077600']
out={}
for i in ids:
    i=i.zfill(10).replace('bdh','') if False else i
    rid='/2022717/bnesearch_detalle_bdh'+i.zfill(10)
    d=requests.get('https://api.europeana.eu/record/v2'+rid+'.json',params=dict(wskey='api2demo'),timeout=60).json()
    o=d.get('object',{})
    pc=[p for p in o.get('providedCHOs',[])]
    ag=o.get('aggregations',[{}])[0]
    out[i]=dict(cho=o.get('proxies'),shown=ag.get('edmIsShownAt'),obj=ag.get('edmObject'))
    print(i,'ok' if o else d)
json.dump(out,open('raw/leads.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
