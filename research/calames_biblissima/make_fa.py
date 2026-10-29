"""Hand-built FranceArchives (non-AN) candidate rows, from fa_all.json review. Writes fa_rows.json."""
import json, re

SC = "Scored from the catalogue description during the Oct 2026 Calames/Biblissima/FranceArchives sweep (research/calames_biblissima/); not viewed"
SRC = "Calames/Biblissima/FranceArchives sweep"
PA = "open (checked 28 Oct 2026: repo ledgers and DECODE list via known.py; no web search yet)"
ALL = json.load(open('fa_all.json', encoding='utf-8'))


def find(cote, sub=None, lieu=None):
    out = []
    for c in ALL:
        if c.get('Cote', '').startswith(cote) and (sub is None or sub.lower() in (c['title'] + c.get('Extrait de la notice', '')).lower()) \
                and (lieu is None or lieu in c.get('Lieu de conservation', '')):
            out.append(c['url'])
    return out


def L(cote, sub=None, lieu=None, label=None, n=2):
    return [{"label": label or ("FranceArchives " + cote), "href": u} for u in find(cote, sub, lieu)[:n]]


def row(**k):
    d = dict(language="French", region="France", cls="C", seen="catalogue", source=SRC, score_note=SC,
             prior_art=PA, links=[])
    d.update(k)
    return d


ANOM = "Archives nationales d'outre-mer (Aix-en-Provence), "
R = []

R.append(row(year=1745, date="10 Nov 1744 - 2 Jun 1746",
    title="Cayenne governor → Navy minister, four letters 'chiffrée en entier' and further ciphered passages not translated (Guiana, War of the Austrian Succession)",
    correspondents="Governor of Guiana (Cayenne) → minister of the Navy", place="Cayenne", region="Americas", period="1701-1800",
    shelfmark=ANOM + "COL C14 19 (letters of 10 Nov 1744, 16 Jul 1745, 5 Oct 1745, 18 Feb 1746; 2 Jun 1746 with 'passage chiffré non traduit')",
    folio_note="the ANOM calendar marks each: 'lettre chiffrée en entier'", cls="C",
    status="ANOM calendar (via FranceArchives): 'lettre chiffrée en entier'; 2 Jun 1746 'passage chiffré non traduit'. Same series as the repo's orvilliers1759 target (COL C14 21-25), earlier volume; ANOM C14 19 not covered by research/central_archives. Not on DECODE (known.py 28 Oct 2026).",
    why="Earlier Cayenne cipher letters (1744-46); could give the governor's key two decades before d'Orvilliers.",
    importance=3, solvability=3, difficulty=3,
    verify="Check the ANOM digital images (Anom 'Autres fonds numérisés'?) and whether the same cipher recurs in COL C14 21-25.",
    links=L("COL C14 19", "chiffr", n=3)))

R.append(row(year=1747, date="28 May 1747 and 14 Mar 1748",
    title="Cayenne letter 'entièrement chiffrée' (troops, munitions, medicine lacking) and receipt of a ciphered ministerial despatch of 2 Dec 1747",
    correspondents="Governor of Guiana → minister of the Navy", place="Cayenne", region="Americas", period="1701-1800",
    shelfmark=ANOM + "COL C14 20 (28 May 1747; no. 3 of 14 Mar 1748)", folio_note="2 items", cls="C",
    status="ANOM calendar: 'lettre entièrement chiffrée'; the 1748 letter acknowledges a ciphered despatch from the minister (which should be in COL B, clear minute of it likely). Not on DECODE.",
    why="Cayenne cipher during the war; the minister's ciphered reply gives a possible crib.", importance=3, solvability=3, difficulty=3,
    verify="Look for the minister's 2 Dec 1747 despatch in ANOM COL B.", links=L("COL C14 20", "chiffr", n=2)))

R.append(row(year=1779, date="13 Jul and 29 Aug 1779",
    title="Cayenne letters of 1779 with ciphered passages and a ciphered piece 'non traduits'", correspondents="Governor of Guiana → minister of the Navy",
    place="Cayenne", region="Americas", period="1701-1800", shelfmark=ANOM + "COL C14 51 (13 Jul 1779; 29 Aug 1779 'pièce chiffrée non traduite')",
    folio_note="2 items", cls="C", status="ANOM calendar: 'passage chiffré non traduit'; 'pièce chiffrée non traduite'. Not on DECODE.",
    why="Guiana during the American war; would extend the d'Orvilliers cipher family to 1779.", importance=2, solvability=3, difficulty=3,
    verify="Compare with the cipher of COL C14 25.", links=L("COL C14 51", "chiffr", n=2)))

R.append(row(year=1778, date="17 Sep and 5 Dec 1778",
    title="Martinique (Bouillé) letters 'chiffrée non décryptée': 17 Sep 1778 and 5 Dec 1778 with ciphered enclosures",
    correspondents="Governor of Martinique (marquis de Bouillé) → minister of the Navy", place="Fort-Royal, Martinique", region="Americas", period="1701-1800",
    shelfmark=ANOM + "COL C8 A 77, f° 88 (no. 238, 17 Sep 1778) and f° 101 (no. 259, 5 Dec 1778)", folio_note="2 letters + enclosures", cls="C",
    status="ANOM calendar states explicitly 'Lettre chiffrée non décryptée' and 'Lettre et pièces jointes chiffrées non décryptées'. The same volume holds the minister's ciphered minutes (ff. 31, 43) and the Martinique series COL C8 A 78-81 has 20 more 'chiffrée' letters of 1779-82. Not on DECODE.",
    why="Martinique at the opening of France's war for American independence (1778): Bouillé's own cipher, undeciphered at the time.",
    importance=4, solvability=3, difficulty=3,
    verify="View the ANOM images; the minutes of f. 31/43 (ciphered, minister to Bouillé) may share the key.", links=L("COL C8 A 77", "chiffr", n=3)))

R.append(row(year=1779, date="8 Mar 1779 - 24 Nov 1782",
    title="Martinique/Guadeloupe despatches 'chiffrée' 1779-82 (Bouillé, Damas, d'Estaing's war): about 18 letters",
    correspondents="Governor of Martinique (Bouillé; Damas) → minister of the Navy", place="Fort-Royal, Martinique", region="Americas", period="1701-1800",
    shelfmark=ANOM + "COL C8 A 78 ff. 1, 3, 5, 31, 112, 123, 144; COL C8 A 79 ff. 4, 19, 24, 70; COL C8 A 81 ff. 97, 104, 114; COL C8 B 15 no. 61 bis; 211 MIOM 60-61 (microfilm)",
    folio_note="letters marked '(chiffrée)' or '(en partie chiffrée)' in the ANOM calendar; whether they were deciphered on the page is not stated", cls="C",
    status="ANOM calendar: '(chiffrée)'. Not stated as undeciphered, but COL C8 A 77 shows ciphered letters left undecrypted, so the later ones may be too. Not on DECODE.",
    why="French West Indies campaigns of 1779-82 (Grenada, St Eustatius, the Saintes).", importance=3, solvability=3, difficulty=3,
    verify="Look at a sample image to see whether a clear decipherment is interlined.", links=L("COL C8 A 78", "chiffr", n=2) + L("COL C8 A 79", "chiffr", n=1)))

R.append(row(year=1744, date="21 Dec 1740 - 14 Nov 1751",
    title="Martinique despatches '(chiffrée)' in King George's War (11 letters, Longueville and Fort-Royal) and 1740-51",
    correspondents="Governor of Martinique → minister of the Navy", place="Fort-Royal, Martinique", region="Americas", period="1701-1800",
    shelfmark=ANOM + "COL C8 A 56 ff. 13, 40, 44, 54, 63, 67, 73, 79, 85, 253, 323; COL C8 A 51 ff. 109, 116; COL C8 A 58 f. 33; COL C8 A 59 f. 158",
    folio_note="~16 letters marked '(chiffrée)'", cls="C",
    status="ANOM calendar: '(chiffrée)'. No statement on decipherment. Not on DECODE.", why="Defence of Martinique and Saint Lucia in 1744-48.",
    importance=2, solvability=3, difficulty=3, verify="Sample images of COL C8 A 56 ff. 13, 54.", links=L("COL C8 A 56", "chiffr", n=3)))

R.append(row(year=1770, date="16 Nov and 4 Dec 1770", title="Martinique letters 'en partie chiffrée' on the defence of Guadeloupe", correspondents="Governor of Martinique → minister of the Navy",
    place="Fort-Royal / Saint-Pierre", region="Americas", period="1701-1800", shelfmark=ANOM + "COL C8 A 69 ff. 354, 357", folio_note="2 letters", cls="C",
    status="ANOM calendar: 'en partie chiffrée'.", why="War scare of 1770.", importance=1, solvability=3, difficulty=3, verify="View.", links=L("COL C8 A 69", "chiffr", n=2)))

R.append(row(year=1755, date="9, 10 and 18 Oct 1755", title="Louisiana despatches 'Dépêche chiffrée' (Kerlérec, 1755)", correspondents="Governor of Louisiana (Kerlérec) → minister of the Navy",
    place="New Orleans", region="Americas", period="1701-1800", shelfmark=ANOM + "COL C13 A 39 (9, 10 and 18 Oct 1755)", folio_note="3 despatches", cls="C",
    status="ANOM calendar: 'Dépêche chiffrée'. No decipherment mentioned. Not on DECODE; not in research/central_archives.",
    why="Louisiana and the Seven Years' War, ciphered by the governor.", importance=3, solvability=3, difficulty=3, verify="View images; check ANOM COL C13 A 39 for interlined clear.",
    links=L("COL C13 A 39", "chiffr", n=3)))

R.append(row(year=1759, date="17 Sep 1759 - 12 Jun 1760", title="Louisiana letters 'Lettre chiffrée' 1759-60 (Kerlérec) and 1 Sep 1736 campaign date", correspondents="Governor of Louisiana → minister of the Navy",
    place="New Orleans", region="Americas", period="1701-1800", shelfmark=ANOM + "COL C13 A 41 (17 Sep, 3 Jul, 10 Nov 1759), COL C13 A 42 (12 Jun 1760), COL C13 A 21 (1 Sep 1736, '(chiffrée)')",
    folio_note="5 items", cls="C", status="ANOM calendar: 'Lettre chiffrée'. COL C13 A 12 (1 Apr 1729) holds a 'traduction d'une lettre chiffrée', so some Louisiana ciphers were deciphered at the time.",
    why="Louisiana 1759-60, fall of New France.", importance=3, solvability=3, difficulty=3, verify="Compare with COL C13 A 12 translation (1729) as a possible key crib.",
    links=L("COL C13 A 41", "chiffr", n=2) + L("COL C13 A 42", "chiffr", n=1)))

R.append(row(year=1760, date="1760", title="Vaudreuil to Berryer announcing in figures the loss of the colony (Canada)", correspondents="Pierre de Rigaud de Vaudreuil → Berryer",
    place="Montréal", region="Americas", period="1701-1800", shelfmark=ANOM + "COL F3 16 (Collection Moreau de Saint-Méry)", folio_note="1 letter", cls="C",
    status="ANOM: 'annonçant en chiffres la perte de la colonie'. Neighbouring COL F3 15 (Montcalm 1758) is already in the Archives nationales sweep. Whether 'en chiffres' = in cipher is plausible but not certain.",
    why="Vaudreuil's announcement of the fall of New France.", importance=4, solvability=2, difficulty=3,
    verify="Check Vaudreuil's printed correspondence; view the item.", links=L("COL F3 16", n=1)))

R.append(row(year=1781, date="22 Dec 1781", title="Montigny to Baudouin (Poona, India): ciphered passage not translated", correspondents="Montigny → Baudouin",
    place="Poona", region="Other", period="1701-1800", shelfmark=ANOM + "COL C5 B 3 (Inde, Pondichéry)", folio_note="1 passage", cls="C",
    status="ANOM calendar: 'Passage chiffré non traduit'.", why="French agent at the Maratha court during the Anglo-Maratha war, 1781.",
    importance=2, solvability=2, difficulty=3, verify="View item.", links=L("COL C5 B 3", "chiffr", n=1)))

R.append(row(year=1848, date="1847-1850", title="Governor Lavaud's despatches from Tahiti: 'Dépêches chiffrées (1847-1850) avec table des matières'", correspondents="Governor Lavaud (Tahiti) → Navy ministry",
    place="Papeete", region="Other", period="1801-1900", shelfmark=ANOM + "OCEA 10", folio_note="ciphered despatches with table of contents", cls="C",
    status="ANOM: 'Dépêches chiffrées (1847-1850)'; no key mentioned. Not on DECODE.", why="French Polynesia after the Pritchard affair.",
    importance=2, solvability=3, difficulty=3, verify="View.", links=L("OCEA 10", n=1)))

R.append(row(year=1678, date="1677-1678", title="The King and Colbert → comte de Blénac, ciphered ministerial despatches (Antilles)", correspondents="Louis XIV; Colbert → comte de Blénac",
    place="Versailles", region="Americas", period="1651-1700", shelfmark=ANOM + "COL B / 201 MIOM 3 (three items, 1677-78, 'chiffrée')", folio_note="3 despatches, one in two copies", cls="C",
    status="ANOM calendar: 'Chiffrée'. Probably clear minutes of ciphered letters (outgoing). Not on DECODE.",
    why="Dutch war in the Caribbean (Estrées 1678).", importance=2, solvability=2, difficulty=3, verify="View.", links=L("201 MIOM 3", "chiffr", n=3)))

R.append(row(year=1884, date="1883-1885", title="Brazza's mission papers: ciphered correspondence with the Foreign Ministry and the letter revealing the cipher", correspondents="Pierre Savorgnan de Brazza → Foreign Ministry",
    place="Paris / Congo", region="Other", period="1801-1900", shelfmark=ANOM + "16 PA III 4 (Fonds Brazza, Relations avec les ministères)", folio_note="'la lettre dévoilant le code chiffré' (28 May 1884 - 25 Nov 1885)", cls="B",
    status="ANOM inventory lists ciphered correspondence and the letter explaining the cipher: key and ciphertext in one box.", why="Brazza's Congo mission 1883-85, Berlin Conference period.",
    importance=2, solvability=4, difficulty=2, verify="View; the explaining letter is the key.", links=L("16 PA III 4", n=1)))

# ---- departmental archives / SHD ------------------------------------------------------------------------------
R.append(row(year=1651, date="1651-1652", title="Armand du Lau du Chambon's papers: ciphered correspondence of Louis II de Bourbon, prince de Condé (Fronde)", correspondents="Prince de Condé → Du Lau du Chambon",
    place="unknown", region="France", period="1651-1700", shelfmark="Archives départementales de la Dordogne, 2 E 1841-18", folio_note="inventory: 'correspondance chiffrée'", cls="B",
    status="Departmental inventory: 'correspondance chiffrée de Louis de Bourbon, prince de Condé'. SHD GR 1KT 211 (Brianson papers) holds five ciphered Condé letters of 1651 with transcription and method: a possible key, so class B. Not on DECODE.",
    why="Condé's cipher in the 1651-52 Fronde campaigns.", importance=3, solvability=3, difficulty=2,
    verify="Get the SHD 'transcription and method' (GR 1KT 211) and view the Dordogne letters.", links=L("2 E 1841", "Condé", n=1) + L("GR 1KT 211", "Condé", n=1)))

R.append(row(year=1700, date="1659-1890", title="Pièces isolées of the Faubournet de Montferrand fonds: 3 ciphered pieces 'sans clé de déchiffrement'", correspondents="unknown",
    place="unknown", region="France", period="unknown", shelfmark="Archives départementales de la Dordogne, 56 J 199 (Fonds Faubournet de Montferrand)", folio_note="3 pieces", cls="C",
    status="Inventory: 'sans clé de déchiffrement [3 pièces]'. Very uncertain dating (1659-1890).", why="Family papers of the Périgord nobility.",
    importance=1, solvability=2, difficulty=3, verify="Open the inventory entry and view the pieces.", links=L("56 J 199", n=1)))

R.append(row(year=1832, date="1832", title="Duchess of Berry's ciphered letter (Vendée uprising year), in the Régis de Gatimel autograph collection", correspondents="Duchesse de Berry → unknown",
    place="unknown", region="France", period="1801-1900", shelfmark="Archives départementales du Gard, 74 J 38 (Fonds de Régis de Gatimel, Autographes)", folio_note="1 letter", cls="C",
    status="Inventory: 'lettre chiffrée de la duchesse de Berry (1832)'.", why="Cipher of the legitimist rising, 1832.", importance=2, solvability=2, difficulty=3,
    verify="View the item; royalist cipher keys of 1832 are in print.", links=L("74 J 38", n=1)))

R.append(row(year=1752, date="1751-1753", title="Valory family papers: letters of Thoumone / Baquencourt, some ciphered", correspondents="Thoumone, de Baquencourt → Valory",
    place="unknown", region="France", period="1701-1800", shelfmark="Archives départementales de l'Essonne, E/3749 (Titres de famille, Famille Valory)", folio_note="'quelques unes de ces lettres sont chiffrées'", cls="C",
    status="Inventory: some letters ciphered. Sibling of the Yvelines E/3756 (1754) entry in research/central_archives.", why="Family of the Valory diplomats.",
    importance=1, solvability=2, difficulty=3, verify="View; compare with E/3756.", links=L("E/3749", n=1)))

R.append(row(year=1655, date="1642-1670", title="Papers of Richard Forster (English Benedictines of Pontoise): one ciphered piece", correspondents="unknown",
    place="Pontoise", language="English", region="England", period="1651-1700", shelfmark="Archives départementales du Val-d'Oise, 68 H 19", folio_note="'une pièce chiffrée'", cls="C",
    status="Inventory: 'une pièce chiffrée' among English and French papers; a sealed piece of Queen Henrietta Maria also there.",
    why="English royalist exile circle, treasurer of Henrietta Maria.", importance=2, solvability=2, difficulty=3, verify="View.", links=L("68 H 19", n=1)))

R.append(row(year=1855, date="1855", title="Maréchal Pélissier's telegraphic despatches 'chiffrées' (Crimea)", correspondents="Maréchal Pélissier → War ministry",
    place="Crimea", region="Other", period="1801-1900", shelfmark="Service historique de la Défense, 1 M 2294 (Papiers Pélissier, D. 4)", folio_note="dépêches télégraphiques chiffrées", cls="C",
    status="SHD catalogue: 'dépêches télégraphiques chiffrées'. Telegraph codes of 1855 are fully recorded in other archives.", why="Siege of Sevastopol.",
    importance=2, solvability=2, difficulty=3, verify="View.", links=L("1 M 2294", n=1)))

R.append(row(year=1931, date="1909-1934", title="Landanger family business records: loose sheets in cipher at the end of the journal and cash books", correspondents="unknown",
    place="Haute-Marne", region="France", period="1901-1950", shelfmark="Archives départementales de la Haute-Marne, 129 J 23 (Journal 1931-34), 129 J 35 (Livre de caisse 1909-13), 129 J 37 (1920-21)", folio_note="'feuille volante chiffrée' / '5 feuilles volantes chiffrées'", cls="C",
    status="Inventory remarks only.", why="Private commercial cipher.", importance=1, solvability=2, difficulty=3, verify="View.", links=L("129 J 23", n=1)))

json.dump(R, open('fa_rows.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R), sum(1 for r in R if not r['links']), [r['shelfmark'][:40] for r in R if not r['links']])
