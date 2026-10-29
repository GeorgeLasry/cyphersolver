import json,re
m=json.load(open("matched.json",encoding="utf8"))
def yr(r): return r["numStartDate"]//10000
def text(r): return ((r["title"] or "")+" "+(r["description"] or "")).replace("\n"," ")
NEG=re.compile(r"royal cipher|monogram|cipher of (?:the )?(?:king|queen)|his cipher|her cipher|crowned|initials|nomenclature|code of regulations|cipher[- ]?(?:clerk|branch)|code of (?:conduct|practice|law)|codes? of (?:signals|practice)|telegraphic code|royal cypher",re.I)
DEC=re.compile(r"decipher|decypher|deciphered|decyphered|with (?:a )?(?:translation|decode)|decode",re.I)
PART=re.compile(r"not decipher|undecipher|partly decipher|part(?:ly)? decypher|without (?:a )?decipher|decipher\w* (?:in part|partly|incomplete)|no decipher",re.I)
POS=re.compile(r"in (?:cipher|cypher|cyphers|ciphers|code|figures|characters|secret)|cipher|cypher|ciphered|cyphered|written in (?:cipher|cypher)",re.I)
def keep(r):
    t=text(r)
    if NEG.search(t): return False
    if DEC.search(t) and not PART.search(t): return False
    return bool(POS.search(t)) and re.search(r"ciph|cyph|in code|in figures|in characters|secret writ|cryptogra",t,re.I)
if __name__=="__main__":
    k=[r for r in m if keep(r)]
    print(len(k))
    import collections
    print(sorted(collections.Counter((yr(r)//50)*50 for r in k).items()))
    json.dump(k,open("kept1.json","w",encoding="utf8"),ensure_ascii=False)
