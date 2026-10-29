import json, urllib.parse
def period(y):
    if y<1497: return "15th century"
    if y<=1559: return "1497-1559"
    if y<=1589: return "1560-1589"
    if y<=1598: return "1589-1598"
    if y<=1610: return "1598-1610"
    if y<=1650: return "1611-1650"
    if y<=1700: return "1651-1700"
    if y<=1800: return "1701-1800"
    if y<=1900: return "1801-1900"
    return "1901-1950"
V={ # id: (short volume name)
 "11001939bsb":"Letters and Papers, Foreign and Domestic, Henry VIII, vol. IV pt 2 (1526-28), ed. Brewer 1872",
 "11332111bsb":"Letters and Papers, Foreign and Domestic, Henry VIII, vol. IV pt 3 (1529-30), ed. Brewer 1876",
 "10278829bsb":"Letters and Papers, Foreign and Domestic, Henry VIII, vol. II pt 2 (1517-18), ed. Brewer 1864",
 "calendarofclaren01bodluoft":"Calendar of the Clarendon State Papers, vol. I (to 1649), ed. Ogle & Bliss 1872",
 "calendarofclaren04bodluoft":"Calendar of the Clarendon State Papers, vol. IV (1657-60), ed. Routledge 1932",
 "calendarofclaren05bodl":"Calendar of the Clarendon State Papers, vol. V (1660-62), ed. Routledge 1970",
 "cu31924091770432":"Calendar of State Papers, Domestic, Commonwealth, 1655-56 (Mary Anne Everett Green 1882)",
 "cu31924028043614":"Calendar of State Papers, Foreign, Edward VI (Turnbull 1861)",
 "cu31924028043622":"Calendar of State Papers, Foreign, Mary (Turnbull 1861)",
 "calendarofstatep00lond":"Calendar of State Papers, Foreign, Edward VI (Turnbull 1861)",
 "calendarofstatep00grea_0":"Calendar of State Papers, Foreign, Elizabeth 1569-71 (Crosby 1874)",
 "calendarstatepa03britgoog":"Calendar of State Papers, Foreign, Elizabeth 1562 (Stevenson 1867)",
 "10278871bsb":"Calendar of State Papers, Foreign, Elizabeth 1560-61 (Stevenson 1865)",
 "calendarofstatep10grea":"Calendar of State Papers, Foreign, Elizabeth 1572-74 (Crosby 1876)",
 "calendarofstatep08grea":"Calendar of State Papers relating to Scotland and Mary Queen of Scots, vol. VIII (1585-86)",
 "cu31924091775274":"Calendar of State Papers, Domestic, Elizabeth 1591-94 (Green 1867)",
 "cu31924091775373":"Calendar of State Papers, Domestic, Elizabeth 1581-90 (Green 1865)",
 "cu31924091775316":"Calendar of State Papers, Domestic, Elizabeth, Addenda 1566-79 (Green 1871)",
 "1967calendarofstatep10greauoft":"Calendar of State Papers, Domestic, James I 1611-18 (Green 1858)",
 "1903calendarofstatep09greauoft":"Calendar of State Papers relating to Ireland, Elizabeth, 1599-1600 (Mahaffy 1899)",
 "1905calendarofstatep10greauoft":"Calendar of State Papers relating to Ireland, Elizabeth, 1600-01 (Mahaffy 1905)",
 "cu31924028044646":"Report on the Manuscripts of J. M. Heathcote, Esq., Conington Castle (HMC 1899)",
 "gri_33125005958521":"A Catalogue of the Manuscripts in the Cottonian Library (Planta 1802)",
 "fordsjohnadams04adamrich":"Writings of John Quincy Adams, vol. IV 1811-1813 (Ford 1914)",
 "correspondancese00kaun":"Correspondance secrete entre le comte A. W. Kaunitz-Rietberg et le baron Koch (Lasry-Koch ed. 1899)",
}
R=[]
def add(year,date,title,corr,place,lang,region,vol,pos,cls,status,why,imp,sol,dif,verify,shelf=None,folio="",prior=None,q="cipher",extra_links=None):
    link="https://archive.org/details/%s?q=%s"%(vol,urllib.parse.quote_plus(q))
    links=[{"label":"Printed volume, full text search ("+q+")","href":link},{"label":"Plain-text OCR","href":"https://archive.org/download/%s/%s_djvu.txt"%(vol,vol)}]
    if extra_links: links+=extra_links
    R.append(dict(year=year,date=date,title=title,correspondents=corr,place=place,language=lang,region=region,period=period(year),
      shelfmark=shelf or V[vol]+" - "+pos,folio_note=folio or pos,cls=cls,status=status,why=why,importance=imp,solvability=sol,difficulty=dif,
      score_note="Scored from the printed calendar text during the Oct 2026 Internet Archive full-text sweep (research/ia_fulltext/); not viewed against the original",
      verify=verify,links=links,seen="catalogue",source="Internet Archive full-text sweep",
      prior_art=prior or "open (checked 28 Oct 2026: editor's note in the printed volume says undeciphered; no later page of the same edition deciphers it, per full-text search of the volume; web search not run, importance below 3)"))
exec(open("rows.py",encoding="utf8").read())
json.dump(R,open("candidates.json","w",encoding="utf8"),ensure_ascii=False,indent=1)
print(len(R))
