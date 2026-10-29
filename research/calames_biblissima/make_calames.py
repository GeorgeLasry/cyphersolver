"""Hand-built Calames candidate rows (from calames_hits.json / calames_detail.json review). Writes calames_rows.json."""
import json

SC = "Scored from the catalogue description during the Oct 2026 Calames/Biblissima/FranceArchives sweep (research/calames_biblissima/); not viewed"
SRC = "Calames/Biblissima/FranceArchives sweep"
PA = "open (checked 28 Oct 2026: repo ledgers and DECODE list via known.py; no web search yet)"


def cal(i):
    return "https://calames.abes.fr/pub/ms/" + i


def row(**k):
    d = dict(language="French", region="France", cls="C", seen="catalogue", source=SRC, score_note=SC,
             prior_art=PA, decode_ids=[], links=[])
    d.update(k)
    if not d['decode_ids']:
        d.pop('decode_ids')
    return d


R = []

# ---- Montpellier H 258: papers of Queen Christina of Sweden -------------------------------------------------
MONT = "Bibliothèque universitaire historique de médecine de Montpellier (Université de Montpellier), H 258 (Manuscrits de la reine Christine)"
R.append(row(year=1669, date="31 Oct 1668 - 19 Apr 1669",
    title="Père Hacki (Jesuit agent in Poland) → Queen Christina of Sweden, c. 18 ciphered letters on the Polish election",
    correspondents="Père Hacki → Christine de Suède", place="Warsaw, Thorn, Danzig, Breslau, Kalisz, Petricovie",
    language="French", region="Poland-Lithuania", period="1651-1700",
    shelfmark=MONT + ", letters nos. 228-234, 236, 240, 241, 246, 248, 250-252 and the 'lettres manquantes' (copies in H 258 bis 1 ff. 55-60)",
    folio_note="each a short autograph sheet 'Lettre chiffrée sur les affaires de Pologne' (ff. 312-352); no. 228 (Petricovie, 28 Feb 1669) has the figures glossed above each group by another hand",
    cls="A",
    status="Catalogue: 'Lettre chiffrée sur les affaires de Pologne'. Eight neighbouring sheets are 'Mise en clair d'une dépêche chiffrée' (nos. 237-239, 242, 244, 245, 249, 253), i.e. clear versions of Hacki's own cipher letters, plus the glossed no. 228: the key can be rebuilt from them. No decipherment of the ciphered sheets themselves is noted. Not on DECODE (known.py, 28 Oct 2026).",
    why="Christina's own campaign for the Polish crown in 1668-69 (Jean Casimir's abdication), told by her agent in cipher.",
    importance=3, solvability=4, difficulty=2,
    verify="Open the Calames notice and the Montpellier digital library images of H 258 ff. 312-353; align nos. 237-253 clear sheets against the cipher sheets.",
    links=[{"label": "Calames notice, 16 Nov 1668", "href": cal("Calames-201911891124348")}, {"label": "Calames notice, 20 Feb 1669", "href": cal("Calames-2019118911243425")}]))

R.append(row(year=1669, date="21 Nov 1668 and 1 May 1669",
    title="Archbishop of Corinth (nuncio) → Queen Christina of Sweden, two ciphered despatches on Polish affairs",
    correspondents="Archevêque de Corinthe → Christine de Suède", place="Warsaw", language="French", region="Poland-Lithuania",
    period="1651-1700", shelfmark=MONT + ", letters nos. 132 (f. 168) and 148 (f. 184)",
    folio_note="two single sheets 'Dépêche chiffrée sur affaires de Pologne'", cls="A",
    status="Catalogue: 'Dépêche chiffrée'. The same volume holds the nuncio's 'mise en clair' of other despatches (nos. 23, 54, 57), so a key may be reconstructible. No decipherment of these two noted.",
    why="Papal nuncio's reports on the Polish election, in the Christina archive.",
    importance=3, solvability=3, difficulty=2,
    verify="Check the images of ff. 168 and 184; compare with the clear versions in nos. 54-57 (ff. 57-61).",
    links=[{"label": "Calames notice, 21 Nov 1668", "href": cal("Calames-20191161611227338")}, {"label": "Calames notice, 1 May 1669", "href": cal("Calames-201911617112493925")}]))

R.append(row(year=1671, date="13 Dec 1670 and 10 Mar 1671",
    title="Hugues de Terlon (French envoy, Copenhagen) → Queen Christina of Sweden, ciphered despatch on Catholic interests in Denmark",
    correspondents="Hugues de Terlon → Christine de Suède", place="Copenhagen", language="French", region="Scandinavia",
    period="1651-1700", shelfmark=MONT + ", letters nos. 233 (ff. 289-290, mise en clair) and 268 (ff. 377-378, dépêche chiffrée)",
    folio_note="no. 268 marked by a cross; the clear text of an earlier despatch (no. 233) is in the same volume", cls="A",
    status="Catalogue: 'Dépêche chiffrée, sur les intérêts catholiques'; no. 233 is the 'mise en clair' of an earlier one. Not on DECODE. Terlon's cipher letters of 1680s to Feuquières are separate (Sorbonne Richelieu fonds).",
    why="French diplomat's cipher in Christina's papers, Catholic interests in Lutheran Denmark.",
    importance=2, solvability=3, difficulty=2, verify="View ff. 289-290 and 377-378.", links=[{"label": "Calames notice, 10 Mar 1671", "href": cal("Calames-201911811411115657")}]))

R.append(row(year=1672, date="16 Jul - 8 Oct 1672",
    title="Queen Christina of Sweden (Rome) → marquis del Monte and Texeira, four partly ciphered letters",
    correspondents="Christine de Suède → marquis del Monte; Texeira", place="Rome", language="French", region="Scandinavia",
    period="1651-1700", shelfmark=MONT + ", letters nos. 87 (f. 110), 90 (f. 113), 100 (ff. 130-131), 102 (f. 133)",
    folio_note="'Lettre en partie chiffrée', originals with red wax seal; 87 and 102 concern Norrköping and the diet",
    cls="C",
    status="Catalogue: 'Lettre en partie chiffrée'. No decipherment noted. Not on DECODE.",
    why="The ex-queen's own cipher in her Roman years, instructing her Swedish agent.",
    importance=3, solvability=2, difficulty=3, verify="View the images; Christina's cipher may match the Hacki/nuncio key.", links=[{"label": "Calames notice, 1 Oct 1672", "href": cal("Calames-20191231512399811"+"9")}]))

R.append(row(year=1669, date="n.d. (c. 1669)", title="Table of correspondence ciphers with the governor general (key sheet in Christina's papers)",
    correspondents="unknown", place="unknown", language="French", region="Scandinavia", period="1651-1700",
    shelfmark=MONT + ", no. 354 (f. 257, 'Tableau des chiffres de correspondance avec le gouverneur général')",
    folio_note="1 table, 26.6 x 31.2 cm", cls="B",
    status="KEY LEAD, no ciphertext of its own. Listed here because it may read the other H 258 ciphers.",
    why="Possible key for the Christina cipher letters.", importance=2, solvability=2, difficulty=2,
    verify="View f. 257 and test against the Hacki sheets.", links=[{"label": "Calames notice", "href": cal("Calames-201912111512469582")}]))

# ---- Chantilly, Condé papers -------------------------------------------------------------------------------
CH = "Bibliothèque du château de Chantilly (musée Condé), Cabinet des lettres, "
R.append(row(year=1796, date="6 Nov 1795 - 25 Mar 1797",
    title="Prince de Condé's negotiations with General Pichegru and the Coalition agents, ciphered letters with decipherment tables",
    correspondents="Louis Joseph de Bourbon, prince de Condé / Pichegru / baronne de Reich, Klinglin, Badouville, Wickham, Montgaillard",
    place="unknown", region="France", period="1701-1800", shelfmark=CH + "Ms 1967 (Z 34), 424 ff.",
    folio_note="424 ff.; tables at the start of the volume", cls="A",
    status="Catalogue: 'Lettres chiffrées avec tables de déchiffrement en début de volume'; Ernest Daudet used the papers for the Pichegru affair. Class A (tables in the volume); whether every letter was deciphered by Daudet is not stated. Not on DECODE; the wilhelmina1795 target is a different archive.",
    why="The Pichegru conspiracy of 1795-97, in the royalist army's own correspondence.",
    importance=4, solvability=3, difficulty=2,
    verify="Check Daudet's 'Conjuration de Pichegru' for the printed texts; ask Chantilly for the images.",
    links=[{"label": "Calames notice", "href": cal("Calames-20240311151555371302")}]))

R.append(row(year=1795, date="16 Jul 1790 - 22 Apr 1800",
    title="Condé correspondence with de Pradt, Preissac, Roll, Saint-Simon, Vernègues and the Salon français: letters ciphered as musical scores",
    correspondents="Louis Joseph de Bourbon, prince de Condé / his agents", place="unknown", region="France", period="1701-1800",
    shelfmark=CH + "Ms 1988 (Z 55), 397 ff.", folio_note="the Salon français letters are pieces 63-155", cls="C",
    status="Catalogue: 'Lettres chiffrées sous forme de partitions musicales'. A musical-notation cipher; the catalogue gives no key. Not on DECODE (known.py).",
    why="An unusual cipher form (letters disguised as musical scores) in the émigré army's correspondence.",
    importance=3, solvability=2, difficulty=4,
    verify="Look for a key in Ms 2157 (Chiffres et clés de l'Armée de Condé) and Ms 2080 p. 389 (table de déchiffrement).",
    links=[{"label": "Calames notice", "href": cal("Calames-20240311151555371323")}]))

R.append(row(year=1792, date="1792", title="Le Salon français: bulletins of Le Traisme, La Chèze and others to Gambert and the comte de Dammartin, with a decipherment table",
    correspondents="Le Traisme, La Chèze (Salon français) → Gambert, comte de Dammartin", place="Paris", region="France", period="1701-1800",
    shelfmark=CH + "Ms 2080 (Z 147), 502 ff.", folio_note="p. 389: 'Table de déchiffrement' in the hand of Gustave Macon", cls="A",
    status="Catalogue mentions only a decipherment table (modern hand); that the bulletins are ciphered is inferred. Verify.",
    why="Royalist news agency of 1792.", importance=2, solvability=3, difficulty=2, verify="View p. 389 and a few bulletins.",
    links=[{"label": "Calames notice", "href": cal("Calames-20240311151555371415")}]))

R.append(row(year=1698, date="25 Sep 1697 - 28 Dec 1698",
    title="Louis XIV, Châteauneuf, Pontchartrain, Le Tellier and others → duc de Vendôme and Campistron, with a decipherment table",
    correspondents="Louis XIV and ministers → Louis-Joseph de Bourbon, duc de Vendôme", place="Versailles / Catalonia", region="France",
    period="1651-1700", shelfmark=CH + "Ms 1905 (S 2), 355 ff.", folio_note="decipherment table mentioned in the title", cls="A",
    status="Catalogue: 'avec une table de déchiffrement'; ciphered portions inferred. Class A. Not on DECODE.",
    why="Last year of the Nine Years' War in Catalonia.", importance=2, solvability=3, difficulty=2,
    verify="View the table and the letters of the first months.",
    links=[{"label": "Calames notice", "href": cal("Calames-20240304154016920236")}]))

R.append(row(year=1655, date="29 Jun 1655, 22 Jun 1656, 4 Jul 1656",
    title="Cardinal Mazarin → Jean Talon, three ciphered letters from La Fère",
    correspondents="Cardinal Mazarin → Jean Talon (intendant)", place="La Fère", region="France", period="1651-1700",
    shelfmark=CH + "Ms 1485, ff. 276-277, 304-305, 308-309 (Recueil pour servir à l'histoire du maréchal de Turenne)",
    folio_note="3 letters of 2 ff. each", cls="C",
    status="Catalogue: 'Lettre chiffrée du cardinal Mazarin à M. Talon'; no decipherment mentioned. The three are copies of Turenne-campaign papers, so they may be printed in Mazarin's Lettres. Check the Chéruel edition first.",
    why="Mazarin's cipher in the Flanders campaign of 1655-56.", importance=3, solvability=3, difficulty=3,
    verify="Grep Chéruel (Lettres du cardinal Mazarin, vol. 8) for 29 Jun 1655 etc.; then view the images.",
    links=[{"label": "Calames notice, 29 Jun 1655", "href": cal("Calames-202406101472031354")}]))

# ---- Institut de France, Fonds Masson ----------------------------------------------------------------------
R.append(row(year=1816, date="1815-1818", title="Signeul (Bernadotte's agent) correspondence with Count Engestrom and Löwenhielm, ciphered",
    correspondents="Signeul / Löwenhielm / Hochschild → Engeström", place="Stockholm", language="French", region="Scandinavia",
    period="1801-1900", shelfmark="Institut de France, Bibliothèque Thiers, Ms Masson 291 (3 liasses, 260 + 132 + 58 ff.)",
    folio_note="'correspondance chiffrée'", cls="C",
    status="Catalogue title: 'correspondance chiffrée de Signeul, agent de Bernadotte'. No decipherment noted. Fonds Masson = Frédéric Masson's Napoleonic papers (Desroches, Cabinet noir). Not on DECODE.",
    why="Bernadotte's agent in the post-Napoleonic years.", importance=3, solvability=3, difficulty=3,
    verify="Check whether the Desroches papers (Ms 302/305) hold the Swedish key.",
    links=[{"label": "Calames notice", "href": cal("IF3B50221")}]))

R.append(row(year=1800, date="1785-1817",
    title="Spanish ambassadors' ciphered letters intercepted by Desroches, Cabinet noir (Berlin, Dresden, Hamburg ...)",
    correspondents="Spanish ambassadors → Spanish foreign minister", place="Berlin etc.", language="Spanish", region="Spain",
    period="1701-1800", shelfmark="Institut de France, Bibliothèque Thiers, Ms Masson 302 (850 ff.), with the tables in Ms Masson 305",
    folio_note="'la plupart des lettres sont en chiffre, avec déchiffrement partiel' (ff. 1-234 Berlin ...)", cls="A",
    status="Catalogue: 'traduites', most letters in cipher 'avec déchiffrement partiel': a partial decipherment by the Black Chamber is attached; the archives_nationales README had written this off as deciphered. Completing the unread parts is the opportunity. Key tables in Ms 305.",
    why="Spain's diplomatic cipher read by the French Cabinet noir.", importance=3, solvability=3, difficulty=2,
    verify="View Ms 302 images; compare the partial translations with the ciphers.",
    links=[{"label": "Calames notice", "href": cal("IF3B50232")}]))

# ---- Sorbonne, fonds Richelieu --------------------------------------------------------------------------------
SR = "Bibliothèque de la Sorbonne, fonds Richelieu, "
R.append(row(year=1747, date="10 Oct - 5 Dec 1747",
    title="Marquis de L'Hospital (French envoy, Naples) → maréchal de Richelieu, seven partly ciphered letters",
    correspondents="Marquis de L'Hospital → maréchal de Richelieu", place="Naples", region="Italy", period="1701-1800",
    shelfmark=SR + "MSRIC 41 ff. 184-186 (10 Oct), 337-338 (17 Oct); MSRIC 42 ff. 94-96 (7 Nov), 159-161 (14 Nov), 266-269 (28 Nov); MSRIC 43 ff. 7-9 (5 Dec)",
    folio_note="each 'Lettre partiellement chiffrée'; no interlinear decipherment is mentioned (unlike the 1725-27 and 1757 letters of the same fonds)", cls="C",
    status="Catalogue: 'Lettre partiellement chiffrée'. Contrast the same fonds' 1726-27 and 1757 letters, which carry 'texte déchiffré entre les lignes' (excluded). Not on DECODE.",
    why="Richelieu's Genoa expedition year (1747-48), Naples's neutrality.", importance=3, solvability=3, difficulty=3,
    verify="Look at an image of MSRIC 42 f. 94; compare the 1757 deciphered pages for the same hand and cipher family.",
    links=[]))

R.append(row(year=1747, date="23 and 30 Dec 1747", title="Cardinal de La Rochefoucauld (Rome) → maréchal de Richelieu, two partly ciphered letters (gunpowder supply)",
    correspondents="Cardinal de La Rochefoucauld → maréchal de Richelieu", place="Rome", region="Papacy", period="1701-1800",
    shelfmark=SR + "MSRIC 43 ff. 177-179 and 240-241", folio_note="'Lettre partiellement chiffrée, relative à une fourniture de poudre'", cls="C",
    status="Catalogue: partially ciphered; no decipherment noted.", why="Supply of powder to the army before Genoa, 1747.",
    importance=2, solvability=3, difficulty=3, verify="View images of MSRIC 43 ff. 177-179, 240-241.", links=[]))

R.append(row(year=1757, date="1 Sep 1757", title="Hamburg letter to maréchal de Richelieu (Hanover campaign): ciphered ff. 72-74 with two accompanying documents",
    correspondents="unknown → maréchal de Richelieu", place="Hamburg", region="Germany", period="1701-1800",
    shelfmark=SR + "MSRIC 58 (June-Oct 1757), ff. 69-74 (in the 23 letters of ff. 31-326)", folio_note="'Lettre chiffrée (feuillets 72-74)'; the many neighbouring letters of this series say 'texte déchiffré entre les lignes', this one does not", cls="B",
    status="Catalogue: cipher on ff. 72-74, no decipherment mentioned. Sibling letters of the series carry interlinear decipherments, so the key is probably recoverable.",
    why="Convention of Klosterzeven season, Hanover 1757.", importance=2, solvability=4, difficulty=2,
    verify="View ff. 72-74.", links=[{"label": "Calames notice", "href": cal("Calames-20182191821649424")}]))

R.append(row(year=1773, date="1773", title="Ciphered letter in the Richelieu papers (no addressee given)",
    correspondents="unknown", place="unknown", region="France", period="1701-1800", shelfmark=SR + "MSRIC 37, ff. 135-137",
    folio_note="3 ff. 'Lettre chiffrée'", cls="C", status="Catalogue: 'Lettre chiffrée [1773]'; nothing more.", why="Late Richelieu fonds, unattributed.",
    importance=1, solvability=2, difficulty=3, verify="View ff. 135-137.", links=[{"label": "Calames notice", "href": cal("Calames-201742912446843105")}]))

# ---- Godefroy collection (Institut de France) ------------------------------------------------------------
GD = "Institut de France, Bibliothèque, Collection Godefroy, "
GST = "Catalogue: original 'en partie chiffré' (or 'en grande partie chiffré'); no decipherment noted"
def god(year, date, title, corr, place, shelf, note, imp, why, printed=None, cid=None, region="France", lang="French"):
    st = GST + (f"; {printed}" if printed else "") + ". Not on DECODE (known.py)."
    return row(year=year, date=date, title=title, correspondents=corr, place=place, language=lang, region=region,
               period=None, shelfmark=GD + shelf, folio_note=note, cls="C", status=st, why=why, importance=imp,
               solvability=3, difficulty=3,
               verify="Check the printed edition if one is named; then request the Institut's images. Cipher may be Henri IV-era royal nomenclator (Sillery/Villeroy family keys appear in Ms Godefroy 168).",
               links=[{"label": "Calames notice", "href": cal(cid)}] if cid else [])

R += [
 god(1580, "30 Oct 1580", "Henri III → Bellièvre and Villeroy on Portuguese affairs, partly ciphered original", "Henri III → Pomponne de Bellièvre, Nicolas de Villeroy", "Ollainville", "Ms Godefroy 260, f. 52", "1 letter", 3, "Henri III on the Portuguese succession crisis of 1580.", cid="IF1B10467"),
 god(1580, "18 and 22 Dec 1580", "Blatier (agent in Flanders) → Henri III and Crosne, three letters largely ciphered", "Blatier → Henri III, Crosne", "Mons", "Ms Godefroy 260, ff. 60, 62, 64", "3 letters 'en grande partie chiffrés'", 3, "French intelligence in the Low Countries during Anjou's enterprise.", cid="IF1B10474"),
 god(1586, "22 Jan 1586", "Berthier → Henri III on Turkish affairs, partly ciphered original", "Berthier → Henri III", "Constantinople (Pera)", "Ms Godefroy 261, f. 48", "1 letter", 2, "French agent at the Porte, 1586.", region="Other", cid="IF1B10596"),
 god(1597, "13 Dec 1597", "Henri IV → Sillery on his resolve to recover Calais, partly ciphered", "Henri IV → Nicolas Brûlart de Sillery", "Saint-Germain-en-Laye", "Ms Godefroy 262, f. 281", "1 letter", 3, "Henri IV's Amiens-Calais campaign.", printed="printed in part in Guadet, Recueil des lettres missives de Henri IV, VIII p. 685 (check whether the cipher is given)", cid="IF1B10833"),
 god(1600, "14 Aug 1600", "Letter on the Saluces affair (Henri IV's negotiations), Grenoble, with a ciphered passage", "unknown → Sillery", "Grenoble", "Ms Godefroy 263, f. 21", "1 letter 'avec passage chiffré'", 3, "Treaty of Lyon (1601) negotiations over the marquisate of Saluzzo.", printed="printed in Guadet VIII p. 774", cid="IF1B10857"),
 god(1606, "28 Mar 1606", "Landgrave Maurice of Hesse-Cassel → Henri IV on the duc de Bouillon, partly ciphered", "Maurice of Hesse-Cassel → Henri IV", "Kassel", "Ms Godefroy 264, f. 120", "1 letter", 3, "The Bouillon affair of 1606; a Hessian cipher letter to the French king.", printed="printed from the minute in Rommel, Correspondance inédite de Henri IV avec Maurice-le-Savant, p. 297", region="Germany", cid="IF1B11028"),
 god(1610, "22 Aug 1610", "Maréchal de La Châtre → Villeroy on the Jülich expedition, partly ciphered", "Claude de La Châtre → Villeroy", "Jülich (camp)", "Ms Godefroy 266, f. 50", "1 letter", 3, "Jülich-Cleves succession war, three months after Henri IV's death.", region="Germany", cid="IF1B11142"),
 god(1616, "24 Feb - 6 Apr 1616", "Jeannin → Villeroy on the negotiations with the princes (Loudun), c. 10 partly ciphered letters", "Pierre Jeannin → Villeroy", "Tours", "Ms Godefroy 268, ff. 83, 86, 88, 90, 92, 95, 96, 99, 104", "9-10 letters 'en partie chiffrés'", 3, "The Peace of Loudun, Marie de Médicis's regency.", cid="IF1B11345"),
 god(1616, "14 Jan 1616 and 5 Oct 1617", "Puysieulx → Villeroy (army affairs, Poitiers) and Épernon (Bordeaux), partly ciphered", "Puysieulx → Villeroy; Épernon → ?", "Poitiers; Bordeaux", "Ms Godefroy 268, ff. 73 and 175", "2 letters", 2, "Regency politics.", cid="IF1B11337"),
 god(1634, "14 Mar - 25 Apr 1634", "Manassès de Feuquières → baron de Rorté on German affairs, six letters largely ciphered", "Manassès de Pas, marquis de Feuquières → Claude de Salles, baron de Rorté", "Frankfurt", "Ms Godefroy 271, ff. 110, 112, 114, 117, 123, 125", "6 letters 'en grande partie chiffrés' (14, 18, 25 Mar; 8, 22, 25 Apr 1634)", 4, "Feuquières' mission to the Heilbronn League, Thirty Years' War.", region="Germany", cid="IF1B11835"),
]
for r in R[-10:]:
    r['period'] = "1560-1589" if r['year'] < 1589 else "1589-1598" if r['year'] < 1598 else "1598-1610" if r['year'] < 1611 else "1611-1650"

# ---- misc single items ---------------------------------------------------------------------------------------------
R.append(row(year=1781, date="June 1781", title="Anonymous cipher sent to M. Haüy, Académie royale d'écriture, for the reading of 'strange characters'",
    correspondents="anonymous → Haüy (writing master)", place="Paris", region="France", period="1701-1800",
    shelfmark="BULAC Paris, MS.ARA.52 (Caussin de Perceval, Manuscrits arabes inv. 21474), item 14 (Danon no. 5)",
    folio_note="1 leaf 278 x 200 mm; 'Texte chiffré', with the note that the evaluation and explanation will appear in the Journal de Paris",
    cls="C", status="Catalogue: 'Texte chiffré'; the solution was promised in the Journal de Paris. Document fully digitised on BULAC (per notice). Not on DECODE.",
    why="A public cipher challenge of 1781 whose solution printed in the Journal de Paris could be checked.", importance=2, solvability=4, difficulty=2,
    seen="catalogue", verify="Open BULAC digital copy (ark:/73193/b2rc0w...), read the cipher and search the Journal de Paris for June-July 1781.",
    links=[{"label": "Calames notice", "href": cal("Calames-20164419421438205")}]))

R.append(row(year=1893, date="4 May 1893", title="Louis Mizon's ciphered despatch for the Dalziel agency, refused by the Porto-Novo telegraph",
    correspondents="Louis Mizon → Dalziel agency", place="Porto-Novo", region="Other", period="1801-1900",
    shelfmark="Institut de France, Bibliothèque, Ms 5892 II (Comité de l'Afrique française, correspondence of Hippolyte Percher / Harry Alis), pièces 189-190",
    folio_note="1 letter and 1 dépêche chiffrée", cls="C", status="Catalogue: 'dépêche chiffrée de Louis Mizon ... refusée par le télégraphe de Porto-Novo'. Cipher likely a commercial telegraph code.",
    why="The Mizon Niger expedition of 1890-93 vs British press agency.", importance=1, solvability=2, difficulty=3, verify="View pièces 189-190.",
    links=[{"label": "Calames notice", "href": cal("Calames-20124241542842162")}]))

R.append(row(year=1752, date="1700s", title="Ciphered letter without signature from one churchman to another (Moustiers monks, chevalier Chappe, cardinal de Rohan)",
    correspondents="unknown → unknown", place="unknown", region="France", period="1701-1800",
    shelfmark="Bibliothèque Sainte-Geneviève, Ms 2571 (Suppl. Z in-4° 831bis), letter listed after fol. 55", folio_note="1 letter in a volume of 61 ff.",
    cls="C", status="Catalogue: 'Lettre chiffrée, sans signature'; contents summarised (so presumably deciphered when catalogued, which would make it class A). Verify.",
    why="Unattributed Jansenist-period letter.", importance=1, solvability=2, difficulty=3, verify="Read the Calames notice in full for the decipherment.",
    links=[{"label": "Calames notice", "href": cal("BSGC10141")}]))


R.append(row(year=1850, date="19th century", title="'Manuscrit cryptographique' (115 ff.), ex-libris Émile Staat and Adelchino de Montalto",
    correspondents="unknown", place="unknown", language="unknown", region="Other", period="1801-1900",
    shelfmark="Bibliothèque nationale et universitaire de Strasbourg, Ms.1.833 (Varia I)", folio_note="115 ff., 203 x 168 mm, calf binding; owner names on ff. 1 and 115v",
    cls="C", status="Calames: 'Manuscrit cryptographique' with subject headings Cryptographie. Could be a cipher treatise, or a ciphered text; the notice does not say. Not on DECODE.",
    why="A whole 19th-century volume catalogued as cryptographic.", importance=2, solvability=2, difficulty=4,
    verify="Open the BNU notice (and digitised copy if any) to see whether the text is enciphered or a treatise.",
    links=[{"label": "Calames notice", "href": cal("D47B14175")}]))

json.dump(R, open('calames_rows.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R))
