import json,urllib.request,time
ids=[]
for n in range(18,25):
    for pre in ["calendarofmanusc%02dgrea","calendarofmanusc%02dgrea_0","calendarofmanusc%02dgrea_1","calendarofmanusc%02dgreauoft","calendarmanuscr%02dofgoog","calendarmanuscr%02dgiusgoog","calendarofmanusc00%02dgrea","calendarofmanusc%04dgrea"]:
        ids.append(pre%n)
for i in ids:
    try:
        d=json.load(urllib.request.urlopen(urllib.request.Request("https://archive.org/metadata/"+i,headers={"User-Agent":"Mozilla/5.0"}),timeout=30))
    except Exception as e: continue
    t=d.get("metadata",{}).get("title")
    if t: print(i,"|",str(t)[-90:],flush=True)
    time.sleep(.3)
