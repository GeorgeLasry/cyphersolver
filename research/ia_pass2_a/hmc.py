import re,json
from show import load
parts={"I":"calendarmanusc01grea","II":"calendarofmanusc02grea_1","III":"calendarmanuscr00unkngoog","IV":"11576077bsb","V":"calendarofmanusc05greauoft","VI":"calendarofmanusc06grea","VII":"calendarofmanusc07greauoft","VIII":"calendarofmanusc08grea_0","IX":"calendarofmanusc09greauoft","X":"calendarofmanusc10grea_0","XI":"calendarofmanusc11greauoft","XII":"calendarofmanusc12grea","XIII":"calendarofmanusc13greauoft","XIV":"calendarofmanusc14grea_0","XV":"calendarofmanusc15grea_0","XVI":"calendarofmanusc16grea_0","XVII":"calendarofmanusc17grea_0","XIX":"calendarofmanusc19grea","XX":"calendarofmanusc20grea","XXI":"calendarofmanusc21grea","XXIII":"calendarofmanusc23grea","XXIV":"calendarofmanusc24grea"}
out=[]
for k,i in parts.items():
    t=load(i); n=len(t); body=t[:int(n*.93)]
    c=0
    for m in re.finditer(r"(?i)\b(in|part|partly|much of it|entirely|wholly|mostly)\s+(?:in\s+)?c[iy]pher\b|\bc[iy]pher\.|\(c[iy]pher",body):
        w=body[max(0,m.start()-600):m.end()+250]
        if re.search(r"(?i)decipher|decypher|unciphered|translat|key",w[400:]) or re.search(r"(?i)decipher|decypher|key to",w[:400]): continue
        c+=1; out.append({"part":k,"id":i,"pos":m.start(),"ctx":re.sub(r"\s+"," ",w)})
    print(k,c)
json.dump(out,open("hmc_nocipher.json","w"))
print(len(out))
