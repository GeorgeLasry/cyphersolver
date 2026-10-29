import json, re
rows = {}
for l in open("hits.jsonl", encoding="utf8"):
    r = json.loads(l)
    rows[r["reference"]] = r


def url(ref):
    r = rows.get(ref)
    return "https://discovery.nationalarchives.gov.uk/details/r/" + r["id"] if r else None


def L(*refs):
    out = []
    for ref in refs:
        u = url(ref)
        if u:
            out.append({"label": "TNA Discovery " + ref, "href": u})
    return out


def grp(pat):
    return sorted([k for k in rows if k and re.match(pat, k)], key=lambda s: rows[s]["numStartDate"])


def lst(refs, n=40):
    s = ", ".join(x.split("/", 1)[1] if "/" in x else x for x in refs[:n])
    return s + (" ... (+%d)" % (len(refs) - n) if len(refs) > n else "")


CHK = "checked 28 Oct 2026: known.py, web search"
out = []


def add(**k):
    d = dict(year=0, date="", title="", correspondents="unknown", place="unknown", language="unknown",
             region="England", period="", shelfmark="", folio_note="", cls="C", status="", why="",
             importance=2, solvability=2, difficulty=3,
             score_note="Scored from the TNA Discovery description during the Oct 2026 TNA Discovery sweep (research/tna_discovery/); not viewed",
             verify="", links=[], seen="catalogue", source="TNA Discovery sweep", prior_art="")
    d.update(k)
    if not d["period"]:
        y = d["year"]
        d["period"] = ("15th century" if y < 1497 else "1497-1559" if y < 1560 else "1560-1589" if y < 1589 else
                       "1589-1598" if y < 1598 else "1598-1610" if y < 1611 else "1611-1650" if y < 1651 else
                       "1651-1700" if y < 1701 else "1701-1800" if y < 1801 else "1801-1900")
    out.append(d)


NOIMG = "Images: TNA Kew (order a copy) or State Papers Online (Gale, subscription); not free."

cw = ["PRO 30/11/3/207-209", "PRO 30/11/6/23", "PRO 30/11/6/25-26", "PRO 30/11/6/54"]
add(year=1781, date="10 Oct 1780 - 5 May 1781",
    title="Cornwallis Papers: four number-cipher letters (Money, Balfour, Rawdon, Craig) the catalogue calls undeciphered",
    correspondents="I. Money to Maj. Wemyss; N. Balfour to Cornwallis; Rawdon to Cornwallis; J. H. Craig to Cornwallis",
    place="Charlotte Town; Charles Town; Camden; Wilmington", language="English", region="Americas",
    shelfmark="TNA PRO 30/11/3/207-209; 30/11/6/23; 30/11/6/25-26; 30/11/6/54",
    folio_note="4 letters, 'in number cipher, not deciphered' / 'mostly cipher and undeciphered'. The same series holds about 100 further 1780-81 letters 'mostly in cipher' (30/11/3-6, 68-69, 81-87) without the note",
    cls="B",
    status="Catalogue: 'not deciphered' / 'undeciphered'. The southern 'Common cipher' was rebuilt by Saberton (JAR 2019) and by targets/balfour1781 here; these four may simply be letters nobody decoded in the 18th c. Not on DECODE (known.py: no hit).",
    why="Southern-campaign despatches of the Carolina garrisons in the months before Yorktown; Saberton's key may read them directly.",
    importance=3, solvability=3, difficulty=2,
    verify="Order TNA images of the four items; test the balfour1781 ring on them; check Saberton, Cornwallis Papers (2010) for printed text.",
    links=L(*cw),
    prior_art="partly known (%s: Saberton JAR 2019 key; balfour1781; Saberton 2010 prints many letters decoded). Not checked whether these four are printed." % CHK)

cwall = grp(r"PRO 30/11/(3|4|5|6|68|69|81|82|83|84|86|87)/")
cwall = [x for x in cwall if re.search(r"cipher|cypher", rows[x]["description"] or "", re.I)]
add(year=1780, date="Aug 1780 - Nov 1781",
    title="Cornwallis Papers: Southern-campaign letters 'mostly in cipher' (Rawdon, Balfour, Tarleton, Turnbull, Craig, Clinton)",
    correspondents="Rawdon, Balfour, Tarleton, Turnbull, Craig, Clinton to Cornwallis", place="Carolinas / Virginia / New York",
    language="English", region="Americas", shelfmark="TNA PRO 30/11/3-6, 68-69, 81-87 (Cornwallis Papers)",
    folio_note="%d item records marked cipher: %s" % (len(cwall), lst(cwall, 25)), cls="B",
    status="Catalogue says cipher / number cipher with no decipherment noted for most; some have en clair copies. Common-cipher key known (Saberton).",
    why="Large uniform corpus for testing the rebuilt Common cipher and for finding other variants.",
    importance=3, solvability=3, difficulty=2,
    verify="Check Saberton 2010 / Stevens 1888 for which are already printed; sample images from TNA.",
    links=L(*cwall[:3]), prior_art="partly known (%s: Saberton JAR 2019)." % CHK)

hal = grp(r"PRO 30/55/(16|19|22|24|30|32|33|36|42|45|48|51|52|53|59)/")
hal = [h for h in hal if re.search(r"cypher|cipher|code", rows[h]["description"] or "", re.I)]
add(year=1781, date="1779 - 1782", title="Carleton Papers: Clinton, Haldimand, Cornwallis and Leslie letters in cypher",
    correspondents="Clinton / Cornwallis / Robertson / Leslie and Haldimand / Carleton", place="New York; Quebec; Yorktown",
    language="English", region="Americas", shelfmark="TNA PRO 30/55 (Carleton Papers, British Headquarters Papers)",
    folio_note="%d items: %s" % (len(hal), lst(hal, 25)), cls="B",
    status="Descriptions give 'in cypher' / 'in code'; one says 'deciphred'. Mostly the Clinton-Haldimand and Cornwallis-Clinton ciphers of the Yorktown year. Not on DECODE.",
    why="Cornwallis to Clinton from Yorktown (16 Aug, 16-17 Sep, 3 Oct 1781) in cypher: original ciphertexts of famous dispatches.",
    importance=3, solvability=3, difficulty=3,
    verify="Carleton Papers are on microfilm at LAC; check Clements finding aids and the Sheldon guide.",
    links=L(*hal[:4]), prior_art="open (%s: Saberton, Clements sweep)." % CHK)

rup = grp(r"D\(W\)1778/I/i/")
rup = [x for x in rup if re.search(r"code|cipher|cypher", rows[x]["description"] or "", re.I)]
add(year=1645, date="30 Apr 1644 - Aug 1645", title="Prince Rupert to William Legge, letters in code (Dartmouth papers)",
    correspondents="Prince Rupert to William Legge (also Digby to Legge)", place="Oxford / the field", language="English",
    region="England", shelfmark="Staffordshire Record Office, D(W)1778/I/i/37-59",
    folio_note="%d items: %s. One on linen (53). Two noted 'not deciphered' (56 Digby, 59 Rupert); 49 'in code, without translation'" % (len(rup), lst(rup)),
    cls="B",
    status="Staffordshire catalogue: 'in code', several not deciphered. Rupert / Charles I ciphers read by Lasry (SP106-3/5 keys) may apply. Not on DECODE (known.py: no hit).",
    why="Rupert's private letters to the Legge circle in the 1644-45 court quarrels, in his own cipher.",
    importance=4, solvability=3, difficulty=2,
    verify="Request images from Staffordshire RO; test Lasry's Rupert / Charles I keys (hm1645, rupert1645 targets).",
    links=L(*rup[:3]),
    prior_art="open (%s: only an Eric Sams letter mentions asking Ian Roy to try a Rupert-to-Legge cipher; no result found)." % CHK)

add(year=1644, date="15 Aug 1644", title="Duke of Richmond to Prince Rupert, mainly in code",
    correspondents="James Stuart, Duke of Richmond and Lennox, to Prince Rupert", shelfmark="Kresen Kernow RS/1/1054",
    folio_note="one letter", cls="B", status="Catalogue: 'mainly in code'. Same network as the Legge letters.",
    why="Court politics, summer 1644.", importance=3, solvability=3, difficulty=2, verify="Obtain image; try Rupert keys.",
    links=L("RS/1/1054"), prior_art="open (%s)." % CHK)
add(year=1648, date="6 Nov 1648", title="Oglander collection: letter 'partly in code' during the Newport treaty",
    correspondents="unknown (Isle of Wight royalist circle)", place="Isle of Wight", shelfmark="Isle of Wight Record Office OG/BB/492",
    folio_note="one letter, no. 78/5", cls="C", status="Catalogue: partly in code; treaty postponed a fortnight.",
    why="Carisbrooke / Newport treaty month.", importance=3, solvability=2, difficulty=3, verify="Ask IWRO for an image.",
    links=L("OG/BB/492"), prior_art="open (%s)." % CHK)
add(year=1648, date="28 Oct 1648", title="Charles I (Newport) to Ormonde, copy of a cipher letter",
    correspondents="Charles I to James Butler, Duke of Ormonde", place="Newport, Isle of Wight",
    shelfmark="Northumberland Archives ZSW/554/1", folio_note="one copy", cls="B",
    status="Catalogue: copy of cipher letter. Charles I ciphers partly solved (Lasry, Pitt). Not on DECODE.",
    why="The King's secret line to Ormonde during the treaty.", importance=4, solvability=3, difficulty=2,
    verify="Request image; check Carte papers for the original and any decipherment.",
    links=L("ZSW/554/1"), prior_art="open (%s)." % CHK)
add(year=1659, date="Jul - Sep 1659", title="SP 78/114: royalist cipher letters (Bamfylde, 'N.B.', six lines mostly cipher), Paris",
    correspondents="Bamfylde and others to Mr Carol", place="Paris", region="France",
    shelfmark="TNA SP 78/114/218, /227, /287", folio_note="3 items (ff. 274-275, 311, 368)", cls="C",
    status="Catalogue: cipher letter attached; six lines mostly cipher. No decipherment noted.",
    why="Royalist intelligence in Mordaunt's rising year.", importance=3, solvability=2, difficulty=3, verify=NOIMG,
    links=L("SP 78/114/218", "SP 78/114/227", "SP 78/114/287"), prior_art="open (%s)." % CHK)
add(year=1657, date="24 Feb 1657", title="William Swyfte despatch 'largely in cipher'", correspondents="William Swyfte to unknown",
    place="France", region="France", shelfmark="TNA SP 78/113/57 (f. 106)", cls="C", status="Catalogue: largely in cipher.",
    why="Commonwealth-era agent in France.", importance=2, solvability=2, difficulty=3, verify=NOIMG,
    links=L("SP 78/113/57"), prior_art="open (%s)." % CHK)
add(year=1659, date="6/16 Aug 1659", title="Edward Nicholas to Sir L.R. at San Sebastian, in cipher",
    correspondents="Sir Edward Nicholas to Sir L. R. (unidentified)", place="San Sebastian", language="English", region="Spain",
    shelfmark="TNA SP 77/32/289", cls="C", status="Catalogue: in cipher.", why="Royalist exile correspondence.",
    importance=3, solvability=2, difficulty=3, verify=NOIMG, links=L("SP 77/32/289"), prior_art="open (%s)." % CHK)
add(year=1656, date="18 Jul 1656", title="Letter in cipher (or shorthand), Hague series", region="Low Countries",
    shelfmark="TNA SP 84/161/66 (f. 169)", cls="C", status="Catalogue: 'in cipher (or shorthand)'.", why="Interregnum Netherlands.",
    importance=2, solvability=2, difficulty=3, verify=NOIMG, links=L("SP 84/161/66"), prior_art="open (%s)." % CHK)
add(year=1642, date="20/30 Sep 1642 and 1644", title="French letters entirely in cipher, SP 78/111 (Paris)", place="Paris",
    language="French", region="France", shelfmark="TNA SP 78/111/93 (f. 212), SP 78/111/135 (f. 300)", folio_note="2 items",
    cls="C", status="Catalogue: 'entirely in cipher'. Listed in research/oldest hard_targets, not in catalogue.json (known.py: no hit).",
    why="Civil-war era French diplomatic cipher.", importance=3, solvability=2, difficulty=4, verify=NOIMG,
    links=L("SP 78/111/93", "SP 78/111/135"), prior_art="open (%s: hard_targets note)." % CHK)
add(year=1638, date="1600 - 1639", title="Stuart embassy cipher passages: Roe 1638, Palatine/France 1639, Mansfelt 1625, Gerbier 1638, Stanning 1631, Kendall 1600",
    correspondents="Roe, Gerbier, Vane, Kendall to the Secretary of State", place="Constantinople / Hague / Brussels",
    language="English", shelfmark="TNA SP 81/44/225; SP 81/46/273; SP 84/130/27; SP 77/28/643; SP 81/37/284; SP 81/38/250; SP 77/6/229",
    folio_note="7 items, each a postscript or portion in cipher", cls="C",
    status="Catalogue 'in cipher'; the Roe / Gerbier ciphers to Elizabeth of Bohemia are catalogued separately.",
    why="Palatine affair ciphers; keys may sit in SP 106/5 and the Roe sibling set.", importance=3, solvability=2, difficulty=3,
    verify=NOIMG + " Compare with the catalogue entry for Elizabeth of Bohemia correspondence.",
    links=L("SP 81/44/225", "SP 81/46/273", "SP 84/130/27", "SP 77/28/643"), prior_art="open (%s)." % CHK)
add(year=1622, date="[? 1622]", title="Venice: letter in cipher from '159'", correspondents="agent '159' to unknown", place="Venice",
    region="Italy", shelfmark="TNA SP 99/24/251", cls="C",
    status="Catalogue: letter in cipher. Venetian 3-figure keys exist in SP 106/10 (sp106box10).",
    why="Possible Venetian code fitting the codebreaker's grid.", importance=2, solvability=2, difficulty=3, verify=NOIMG,
    links=L("SP 99/24/251"), prior_art="open (%s)." % CHK)
add(year=1634, date="26 Aug 1634", title="Venice, anonymous letter partly in cipher (Feilding embassy period)", place="Venice",
    region="Italy", shelfmark="TNA PRO 30/25/6", cls="B",
    status="Catalogue: partly in cipher. Warwickshire RO CR 2017/C89 'The cypher used by Lord Feilding and Peter Morton' (1635) and C157/1-4 'Codes and ciphers' are key leads.",
    why="A key lead exists.", importance=2, solvability=3, difficulty=2, verify="Fetch CR 2017/C89 and C157/1-4 from Warwickshire RO.",
    links=L("PRO 30/25/6", "CR 2017/C89"), prior_art="open (%s)." % CHK)
add(year=1600, date="14 Jan 1600", title="Sir Henry Neville papers: letter partly in cipher", correspondents="unknown to Neville",
    region="France", shelfmark="TNA PRO 30/50/70/8", cls="C", status="Catalogue: partly in cipher; enclosure to 70/7.",
    why="Neville's Paris embassy 1599-1600.", importance=2, solvability=2, difficulty=3, verify=NOIMG,
    links=L("PRO 30/50/70/8"), prior_art="open (%s)." % CHK)
add(year=1693, date="1693 - 1694", title="Stepney in Vienna: SP 105/58-60, 82, 84 letters with cipher passages",
    correspondents="Stepney, Paget, Vernon, Blathwayt, Colt", place="Vienna / Dresden / Constantinople", language="English",
    region="Central Europe", shelfmark="TNA SP 105/58/27, /58/137v, /59/79, /59/97v, /60/7v/1, /60/121, /60/123, /60/135 ...",
    folio_note="about 15 items; SP 105/59/79 says the 'most considerable parts' of intercepted letters are 'undeciphered'", cls="B",
    status="Stepney's Vienna cipher family THE=454 is in the repo (targets/stepney, yard1699). Catalogue says some intercepts undeciphered.",
    why="Grand Alliance diplomacy in a cipher family already read.", importance=3, solvability=3, difficulty=2,
    verify="Match with the THE=454 key.", links=L("SP 105/59/79", "SP 105/60/121"), prior_art="partly known (%s: repo stepney)." % CHK)
add(year=1708, date="Jan 1707 - Oct 1708", title="Whitworth (Moscow) to Harley / Boyle, letters 'partly in cipher'",
    correspondents="Charles Whitworth to Robert Harley / Henry Boyle", place="Moscow", language="English", region="Other",
    shelfmark="TNA SP 91/5 (about 50 folios)",
    folio_note="refs: %s; ff. 163, 108 'partly undeciphered'; ff. 298, 300 undeciphered duplicates" % lst(grp(r"SP 91/5/"), 12), cls="A",
    status="Catalogue says partly in cipher; decipherments for some are in the volume (f.180 for f.163, f.294), others undeciphered. BL Add MS 37354-60 hold Whitworth's papers.",
    why="Russian court and Charles XII's invasion as seen by the English envoy.", importance=3, solvability=3, difficulty=2,
    verify="View SP 91/5 images; the deciphered siblings give cribs.", links=L("SP 91/5/163", "SP 91/5/108", "SP 91/5/298"),
    prior_art="open (%s)." % CHK)
add(year=1722, date="1722 - 1724", title="Atterbury Plot and Jacobite cipher letters (Plunket numeral cypher; numbered letters 10-19 'in cypher and French')",
    correspondents="Jacobite agents to Plunket, Layer, Kelly, Compton", place="Paris / Boulogne / London", language="French/English",
    shelfmark="TNA SP 35/45/78; 35/50/8, /51; 35/53/17, /76; 35/46/59 (undecyphered); 35/47/52, 35/73/50-52 (Plunket cipher copies)",
    folio_note="letters plus key leads: Plunket's numeral cypher no. 3 (35/47/52) and numerical equivalents (35/73/52)", cls="B",
    status="Willes / Ashfield decoded much at the time; SP 35/46/47 says one paper cannot be decyphered without more text; SP 35/46/59 'Undecyphered paper'. Keys in the same volumes and BL Add MS 32256.",
    why="Jacobite plot ciphers with keys in the same file.", importance=4, solvability=4, difficulty=2,
    verify="View SP 35/45-53 and 73; apply the 35/73/52 and 35/47/52 keys to the 35/50 and 35/53 numbered letters.",
    links=L("SP 35/45/78", "SP 35/46/59", "SP 35/73/52"),
    prior_art="open (%s: Cruickshanks & Erskine-Hill 2004 is the likely edition; no online decipherment found)." % CHK)
add(year=1745, date="Nov - Dec 1745", title="Jacobite 1745 intercepts: Ball letters in cipher, Moor-Gager number cipher, MacLean letters",
    correspondents="Z. Ball, S. Moor, Charles Edward Stuart ('Burnet') and others", place="London / Scotland", language="English",
    shelfmark="TNA SP 36/74/1/60; SP 36/75/1/29; SP 36/76/3/79; SP 36/78/1/39; SP 36/78/2/119; SP 54/25/5-8B; SP 54/26/125, /136",
    folio_note="about 10 items", cls="C",
    status="Catalogue 'in cipher' / 'partly in cipher'; SP 36/73/3 has a deciphered copy of the O'Brien letter (excluded). SP 36/74/1/60 also in oldest hard_targets.",
    why="Forty-Five correspondence.", importance=3, solvability=3, difficulty=3, verify=NOIMG,
    links=L("SP 36/74/1/60", "SP 54/25/8B", "SP 54/26/136"), prior_art="open (%s)." % CHK)
add(year=1662, date="Jan - May 1662", title="Richard Chauran to Williamson: Spanish cipher letters, 'partly in cipher'",
    correspondents="Richard Chauran to Joseph Williamson", place="Netherlands", language="French", region="Low Countries",
    shelfmark="TNA SP 84/165/1-114", folio_note="10 items; the agent says he must write completely in cipher", cls="C",
    status="Catalogue: partly in cipher, ciphers transmitted; key may be on SP 84/165/36 and /70.",
    why="Restoration intelligence on Dutch-Spanish papers.", importance=2, solvability=3, difficulty=2, verify=NOIMG,
    links=L("SP 84/165/75", "SP 84/165/36"), prior_art="open (%s)." % CHK)
add(year=1709, date="Mar 1709", title="Malknecht extract partly in cipher, and two letters in cipher (Blencowe, Derby)",
    shelfmark="TNA SP 34/10/120A, /122; SP 34/24/86-87 (translations at 84-85)", cls="A",
    status="Translations of the cipher parts exist at SP 34/24/84-85, so those are read; the SP 34/10 pair is not.",
    why="Jacobite letters of Anne's reign.", importance=2, solvability=3, difficulty=2, verify="View SP 34/10 images.",
    links=L("SP 34/10/120A", "SP 34/10/122"), prior_art="open (%s)." % CHK)
add(year=1795, date="1795 - 1804", title="Drake papers (Devon): letters 'in cypher' from Bute, Jackson, Wynne",
    correspondents="Lord Bute, Jackson, Henry Wynne to Francis Drake", place="Genoa / Munich / Karlsbad", language="English",
    region="Central Europe", shelfmark="Devon Heritage Centre 1700m-0/C/P/398, /453, /661, /674, /701",
    folio_note="5 items; the Drake-Stuart Munich 1803 letter is catalogue id 833", cls="B",
    status="Catalogue 'in cypher'. Drake cipher family appears in catalogue.json id 833.", why="Revolutionary-war intelligence.",
    importance=2, solvability=2, difficulty=3, verify="Request images; compare with id 833.", links=L("1700m-0/C/P/674"),
    prior_art="open (%s)." % CHK)
add(year=1795, date="1795 - 1797", title="Wickham papers: foreign correspondence 'some in cipher'",
    correspondents="William Wickham and correspondents", place="Switzerland / Germany", language="French/English",
    region="Central Europe", shelfmark="Hampshire Archives 38M49/1/3/1-9; 38M49/1/10/1-51; 38M49/1/141/4 (Plan of a cypher)",
    cls="B", status="Catalogue: some in cipher; 38M49/1/141/4 'Plan of a cypher' may be a key lead.",
    why="Wickham ran the Swiss secret-service network.", importance=3, solvability=2, difficulty=3,
    verify="Hampshire RO images.", links=L("38M49/1/10/1-51", "38M49/1/141/4"), prior_art="open (%s)." % CHK)
add(year=1800, date="1800 - 1804", title="Prince de Bouillon's correspondents: Paris agent signed in cipher; Bouillon to Cooke on a cipher error",
    correspondents="[?Roznel] to Bouillon; Bouillon to Cooke", place="Paris / Jersey", language="English", region="France",
    shelfmark="TNA WO 1/923/115; WO 1/924/499", cls="C", status="Catalogue: signed in cipher; error in reading the cipher.",
    why="Royalist intelligence on Bonaparte.", importance=2, solvability=2, difficulty=3, verify=NOIMG,
    links=L("WO 1/923/115", "WO 1/924/499"), prior_art="open (%s)." % CHK)
k57 = grp(r"PRO 30/57/(4|11)/")
add(year=1884, date="Jul 1884 - May 1885", title="Kitchener papers: Nile Expedition telegrams 'in code' / 'part in code', Wolseley and Wilson",
    correspondents="Wolseley, Wilson, Stewart, Rundle, Baker Pasha", place="Dongola / Wadi Halfa / Korosko", language="English",
    region="Other", shelfmark="TNA PRO 30/57/4/16-207B; key lead PRO 30/57/11/25 ('Six code cipher'), 4/77-78 (Arabic cipher)",
    folio_note="%d items: %s" % (len(k57), lst(k57, 18)), cls="B",
    status="Catalogue: code telegrams; some translations ('part in code and translation', 4/35).",
    why="Gordon relief; key lead in the same fonds.", importance=2, solvability=2, difficulty=3,
    verify="Compare 30/57/11/25 key; telegrams may be commercial code, not cipher.",
    links=L("PRO 30/57/4/36", "PRO 30/57/11/25"), prior_art="open (%s)." % CHK)

json.dump(out, open("candidates.json", "w", encoding="utf8"), ensure_ascii=False, indent=1)
print(len(out))
