import json, sys
sys.path.insert(0, '.')
from rows_salazar import S

SAL = "https://archive.org/details/salazary-castro-22-nov-2016"
SALQ = "https://archive.org/details/salazary-castro-22-nov-2016?q="
PRIOR_SAL = ("open as far as checked (26-28 Oct 2026: known.py, research/oldest/CANDIDATES.md, DECODE list; web search for "
             "Salazar y Castro + Gran Capitan/cifra general found only the CNI decipherment of the Maqueda letters 1502-03 "
             "(a different archive) and Galende Diaz/Parisi on the cifra general, nothing on this item)")
rows = []

def region_for(place):
    p = place.lower()
    if any(x in p for x in ("naples", "barletta", "milan", "venice", "rome", "camillas", "trebbia", "carrack")): return "Italy"
    if any(x in p for x in ("brussels", "mechelen", "antwerp")): return "Low Countries"
    if any(x in p for x in ("trent",)): return "Central Europe"
    if "london" in p: return "England"
    if "avignon" in p: return "France"
    return "Spain"

for (yr, date, place, snd, rcp, lang, vol, fol, inv, what, kind, imp, sol, dif, cls) in S:
    fam = ("Ferdinand's secretariat: the Catholic Monarchs' cifra general (known from Galende Diaz 1994, Parisi 2020 and the esp318/garcilaso1498 targets in this repo) may apply"
           if yr >= 1495 else
           "Aragonese chancery ciphers of Juan II / Ferdinand, 1470s; no key identified, compare the DECODE R9483-R9485 Salazar A-7 records")
    rows.append({
        "year": yr, "date": date,
        "title": f"{snd} -> {rcp}, {what}" if len(what) < 90 else f"{snd} -> {rcp}",
        "correspondents": f"{snd} -> {rcp}",
        "place": place, "language": lang if 'Latin' not in what else "Latin",
        "region": region_for(place),
        "period": "15th century" if yr <= 1496 else "1497-1559",
        "shelfmark": f"Real Academia de la Historia (Madrid), Coleccion Salazar y Castro, {vol}, {fol} (inventory no. {inv})",
        "folio_note": f"{fol}; catalogue says: {what}",
        "cls": cls,
        "status": ("Listed in the RAH Salazar y Castro catalogue (IA full text) as cipher with no decipherment or translation noted in the entry. "
                   f"Volume {vol} is not among the Salazar volumes on DECODE (only 9/8, 9/17, 9/23-9/31, 9/34 appear). {fam}."),
        "why": "Ferdinand the Catholic's own or ambassadors' cipher correspondence, " + ("pre-1480, among the oldest Spanish ciphertexts" if yr < 1480 else "Italian wars and the Great Captain" if "Cordoba" in snd or "Great Captain" in snd else "diplomacy of the Catholic Monarchs"),
        "importance": imp, "solvability": sol, "difficulty": dif,
        "score_note": "Scored from the RAH catalogue entry during the Oct 2026 Internet Archive non-English printed-sources sweep (research/ia_pass2_c/); not viewed",
        "verify": "Check whether RAH Biblioteca Digital / Salazar images exist for this signatura; if not, request a reproduction; compare the cipher with the cifra general RRCC and the Aragonese key lists",
        "links": [{"label": "RAH Salazar y Castro catalogue (IA full text)", "href": SALQ + f"inventario%20{inv}"},
                  {"label": "IA item", "href": SAL}],
        "seen": "catalogue", "source": "Internet Archive printed-sources sweep (non-English)",
        "prior_art": PRIOR_SAL,
    })

# fix a title that carries an OCR placeholder
for r in rows:
    r["title"] = r["title"].replace(" (Elne? name as printed)", "")
    r["correspondents"] = r["correspondents"].replace(" (Elne? name as printed)", "")

def add(**k):
    base = {"language": "unknown", "cls": "C", "seen": "catalogue", "decode_ids": []}
    base.update(k)
    if not base["decode_ids"]: base.pop("decode_ids")
    rows.append(base)

SRC = "Internet Archive printed-sources sweep (non-English)"
SCN = "Scored from the printed catalogue/edition text during the Oct 2026 Internet Archive non-English printed-sources sweep (research/ia_pass2_c/); not viewed"

# ---- Salazar, later groups ----
VSAL = "Real Academia de la Historia (Madrid), Coleccion Salazar y Castro, "
add(year=1639, date="17 Mar 1638 - 31 Dec 1639 (about 14 letters, many in duplicate)", title="Philip IV -> Antonio Sarmiento de Acuna, letters on the defence of the Franche-Comte, mostly in cipher",
    correspondents="Philip IV -> Antonio Sarmiento de Acuna (also to Charles of Lorraine and Marques de Castaneda)", place="Madrid", language="Spanish", region="Spain", period="1611-1650",
    shelfmark=VSAL + "A-87, ff. 16-140 (inventory nos. 14177-14234)", folio_note="originals 'en cifra' or 'en su mayor parte en cifra', signed by the King, each with its address leaf; duplicates at ff. 20, 29ff, 70, 82, 113, 139",
    cls="C", status="Catalogue lists each as cipher with no decipherment noted; A-87 not on DECODE.", why="Spanish defence of the Franche-Comte against France 1638-39, with the Swiss cantons; a royal cipher of the 1630s.",
    importance=3, solvability=3, difficulty=3, score_note=SCN, verify="Order A-87 images; compare with Gondomar/Sarmiento family ciphers (Real Biblioteca) and the cipher Pedro de Arce sent Sarmiento in 1640 (A-N-48 f. 329)",
    links=[{"label": "RAH Salazar catalogue (IA full text)", "href": SALQ + "inventario%2014177"}], source=SRC,
    prior_art="open (checked 28 Oct 2026: known.py, web search for the Sarmiento/Franche-Comte ciphers found nothing; Gondomar-circle ciphers are studied in Estudios Romanicos)")
add(year=1639, date="12 Mar 1638 - 29 Nov 1639 (about 10 letters, with duplicates)", title="Cardinal-Infante Ferdinand -> Antonio Sarmiento de Acuna (and Diego Saavedra Fajardo), letters in cipher on Franche-Comte",
    correspondents="Cardinal-Infante Ferdinand of Austria -> Antonio Sarmiento de Acuna / Diego Saavedra Fajardo", place="Brussels, Antwerp, camp", language="Spanish", region="Low Countries", period="1611-1650",
    shelfmark=VSAL + "A-87, ff. 256-311 (inventory nos. 14286 ff.)", folio_note="'original, en cifra', 'casi todo en cifra', copies in contemporary hand",
    cls="C", status="Catalogue: cipher, no decipherment noted; not on DECODE.", why="Governor of the Spanish Netherlands directing the Franche-Comte campaign; sister series to the Philip IV letters.",
    importance=3, solvability=3, difficulty=3, score_note=SCN, verify="Order A-87 ff. 256-311; check against Philip IV series for a shared cipher",
    links=[{"label": "RAH Salazar catalogue (IA full text)", "href": SALQ + "inventario%2014286"}], source=SRC, prior_art="open (checked 28 Oct 2026: known.py, web search)")
add(year=1648, date="26 Apr - 5 Jun 1648", title="Don Juan Jose of Austria (Naples) -> Luis Mendez de Haro, long cipher letter and cover note from his secretary Gregorio de Leguia",
    correspondents="Juan Jose of Austria, via Gregorio de Leguia -> Luis Mendez de Haro", place="Naples", language="Spanish", region="Italy", period="1611-1650",
    shelfmark=VSAL + "A-89, ff. 166-175 and 188 (inventory nos. 14452 ff.); A-103 (cipher original of 26 Apr 1648)", folio_note="ten folios in cipher (ff. 166-175)",
    cls="C", status="Catalogue: original in cipher; no decipherment noted; not on DECODE.", why="The Naples revolt of Masaniello, seen by the Spanish commander.",
    importance=4, solvability=3, difficulty=3, score_note=SCN, verify="Order A-89; Juan Jose's cipher with Haro may be the one he mentions receiving new in 1656 (A-107 f. 48)",
    links=[{"label": "RAH Salazar catalogue (IA full text)", "href": SALQ + "inventario%2014452"}], source=SRC, prior_art="open (checked 28 Oct 2026: known.py)")
add(year=1653, date="1649-1655 (about 12 letters)", title="Don Juan Jose of Austria -> Luis Mendez de Haro, series of cipher letters from Messina, Barcelona",
    correspondents="Juan Jose of Austria -> Luis Mendez de Haro", place="Messina, Barcelona", language="Spanish", region="Spain", period="1651-1700",
    shelfmark=VSAL + "A-103 ff. 148-183; A-104 ff. 122-123; A-106 f. 34 (inventory nos. 15725, 15728-15729, 15740, 15840, 16016)", folio_note="'original, en cifra': 8 Oct 1649, 28 Feb and 4 Mar 1653, 13 Jul 1653 (siege of Gerona), 20 Feb 1655",
    cls="C", status="Catalogue: cipher originals, no decipherment noted; not on DECODE.", why="Spanish commander in Catalonia in the Franco-Spanish war, complaints on money and troops.",
    importance=3, solvability=3, difficulty=3, score_note=SCN, verify="Order A-103/A-104/A-106; build the key from the pair of cipher originals and their registered summaries",
    links=[{"label": "RAH Salazar catalogue (IA full text)", "href": SALQ + "inventario%2015725"}], source=SRC, prior_art="open (checked 28 Oct 2026: known.py)")
add(year=1655, date="16 Jan 1655 - 22 Nov 1656 (about 14 letters)", title="Cardinals Carlo and Giovan Carlo de' Medici (Rome, Florence) -> Luis Mendez de Haro, letters in cipher on the 1655 conclave",
    correspondents="Cardinal Carlo de' Medici and Cardinal Giovan Carlo de' Medici -> Luis Mendez de Haro", place="Rome, Florence", language="Italian", region="Papacy", period="1651-1700",
    shelfmark=VSAL + "A-109, ff. 135-286 (inventory nos. 16354-16417)", folio_note="'original, en cifra' (24 Apr 1655 election of Alexander VII; 7 Aug 1655 'Squadrone volante'; 1 Oct 1656), others with cipher paragraphs",
    cls="C", status="Catalogue: cipher, no decipherment noted; not on DECODE.", why="The Spanish party in the conclave of 1655 as described by a Medici cardinal.",
    importance=4, solvability=3, difficulty=3, score_note=SCN, verify="Order A-109; the cipher was sent to Carlo de' Medici (A-109, 4 Jul 1654 letter asks for it)",
    links=[{"label": "RAH Salazar catalogue (IA full text)", "href": SALQ + "inventario%2016354"}], source=SRC, prior_art="open (checked 28 Oct 2026: known.py)")
add(year=1654, date="12 Sep 1654", title="Diego de Aragon y Pignatelli, duke of Terranova (Rome) -> Philip IV, letter in cipher",
    correspondents="Duke of Terranova -> Philip IV", place="Rome", language="Spanish", region="Papacy", period="1651-1700",
    shelfmark=VSAL + "A-97, ff. 215-217 (inventory no. 15272)", folio_note="three folios in cipher", cls="C", status="Catalogue: original in cipher; not on DECODE.",
    why="Spanish ambassador at Rome under Innocent X.", importance=3, solvability=3, difficulty=3, score_note=SCN, verify="Order A-97 ff. 215-217",
    links=[{"label": "RAH Salazar catalogue (IA full text)", "href": SALQ + "inventario%2015272"}], source=SRC, prior_art="open (checked 28 Oct 2026: known.py)")

# ---- Lope de Soria archive (BRAH 98, 1931) ----
BR = "https://archive.org/details/boletindelareala98madr"
SOR = "Catalogue of the archive of Lope de Soria offered to the Real Academia de la Historia in 1931 (Boletin de la Real Academia de la Historia 98, 1931, pp. 363ff), no. "
sor = [
 (19,1523,"23 Aug 1523","Valladolid","Charles V","Lope de Soria, ambassador at Genoa","duplicate of no. 18; the cipher part untranslated",3),
 (20,1523,"24 Aug 1523","Valladolid","Charles V","Lope de Soria (letters for a Count and Antoniotto Adorno)","cipher part untranslated",3),
 (36,1524,"3 Oct 1524","Aniago","Charles V","Lope de Soria","duplicate of no. 35, cipher parts untranslated",3),
 (37,1524,"15 Nov 1524","Espinar","Charles V","Lope de Soria","army movements and 100,000 ducats; cipher parts untranslated",3),
 (44,1526,"14 Aug 1526 (?)","unknown","Charles V","Lope de Soria","entirely cipher, untranslated; date uncertain in the catalogue",3),
 (49,1527,"7 Aug 1527","Valladolid","Charles V","Antonio de Leyva, governor of Milan","several cipher lines untranslated",3),
 (71,1533,"30 Aug 1533","Monzon","Charles V","Lope de Soria, ambassador at Venice","peace between the King of the Romans and the Turk; cipher part untranslated",3),
 (94,1535,"23 Oct 1535","Messina","Charles V","Lope de Soria","mostly cipher, untranslated; after the Tunis campaign",4),
 (99,1536,"29 Jan 1536","Naples","Charles V","Lope de Soria","almost entirely cipher, untranslated; talks with the Venetian ambassadors",4),
 (103,1537,"21 Mar 1537","Valladolid","Charles V","Lope de Soria","almost entirely cipher, untranslated",3),
 (120,1535,"last day of Feb 1535","Znaim (as printed 'Zenam')","Ferdinand, King of the Romans","Lope de Soria","cipher part untranslated; one cipher line translated on p. 1",3),
 (121,1535,"9 Apr 1535","Vienna","Ferdinand, King of the Romans","Lope de Soria","cipher part untranslated (a separate translation sheet exists, 2 leaves)",2),
 (124,1535,"28 May 1535","Vienna","Ferdinand, King of the Romans","Lope de Soria","examination of the prisoners Casal and Corsino; cipher passage untranslated",3),
 (126,1535,"15 Jul 1535","Vienna","Ferdinand, King of the Romans","Lope de Soria","Venetian intentions, Montalcone dispute; cipher part untranslated",3),
 (129,1535,"12 Oct 1535","Vienna","Ferdinand, King of the Romans","Lope de Soria","Turkish envoys, truce in Hungary; cipher part untranslated",3),
 (137,1537,"26 Apr 1537","Prague","Ferdinand, King of the Romans","Lope de Soria","news of the Emperor and the war; cipher passage untranslated",3),
 (173,1523,"10 Sep 1523","Naples","Charles de Lannoy, viceroy of Naples","Lope de Soria","much of the letter in a cipher the catalogue calls 'not deciphered'",3),
 (204,1528,"11 Jul 1528","unknown","Antonio de Leyva","Lope de Soria","entirely cipher, untranslated",3),
 (212,1533,"2 Nov 1533","Marseille","Count of Cifuentes","Lope de Soria","marriage of the Pope's niece to the Duke of Orleans; cipher passage untranslated",3),
 (214,1536,"19 Aug 1536","Rome","Count of Cifuentes","Lope de Soria","cipher passages, some untranslated, some translated in the margin; French army preparations",3),
]
for (n, yr, date, place, snd, rcp, what, imp) in sor:
    lang = "Spanish"
    add(year=yr, date=date, title=f"{snd} -> {rcp}, {date}: {what}", correspondents=f"{snd} -> {rcp}", place=place, language=lang,
        region="Central Europe" if snd.startswith("Ferdinand") else ("Italy" if place in ("Naples", "Rome", "Messina", "Marseille") and snd != "Charles V" else "Spain"),
        period="1497-1559",
        shelfmark=f"Archive of Lope de Soria, offered to the Real Academia de la Historia 1931 (present location to confirm), item {n} of the 1931 catalogue",
        folio_note=SOR + f"{n}: {what}", cls="B",
        status="The 1931 catalogue states the cipher part is not translated/deciphered. This is the incoming correspondence of Lope de Soria; his outgoing letters to Charles V are RAH Salazar A-28 (DECODE R9488-R9498) and are already worked in this repo (targets/soria1527, 1523 key A/B).",
        why="Charles V's and Ferdinand's own cipher to their ambassador at Genoa and Venice; the repo already holds Soria's 1523-27 keys for the other direction.",
        importance=imp, solvability=2, difficulty=3, score_note=SCN,
        verify="Find where the Lope de Soria archive is now (RAH? Archivo Historico Nacional?); check whether any images exist; compare Charles V's 1520s-30s ciphers (Lasry/Tomokiyo keys)",
        links=[{"label": "BRAH 98 (1931) on IA, Catalogo del archivo de Lope de Soria", "href": BR + "?q=Lope+de+Soria"}, {"label": "plain-text OCR", "href": "https://archive.org/download/boletindelareala98madr/boletindelareala98madr_djvu.txt"}],
        source=SRC, prior_art="open (checked 28 Oct 2026: known.py; Charles V/Soria ciphers of the 1520s are covered by this repo's soria1527 target, but not these letters)")

# ---- Farnese inventory (Cauchie & van der Essen, 1911) ----
FI = "https://archive.org/details/inventairedesarc00cauc"
FIQ = "https://archive.org/details/inventairedesarc00cauc?q="
FN = "Archivio di Stato di Napoli, Carte Farnesiane (fascio {f}, as grouped in Cauchie and Van der Essen, Inventaire des archives farnesiennes de Naples, Brussels 1911, no. {n}; fascio number read from the OCR, to confirm)"
far = [
 (187,104,1583,"20 Apr 1583","Jean-Baptiste de Tassis -> Alexander Farnese, and Farnese's reply","very long letter and answer, entirely in cipher, 'sans dechiffre'; plus cipher minutes of 1582","Spanish ambassador at Paris, Farnese in the Netherlands",3,"France"),
 (187,107,1588,"1588 (three letters)","Bernardino de Mendoza (Paris) -> Alexander Farnese","three letters entirely in cipher, 'non dechiffrees'","Mendoza's cipher letters at the time of the Armada and the League",4,"France"),
 (187,109,1588,"1588","Juan Yniguez (Rouen) -> Alexander Farnese","letters entirely in cipher (inventory does not say whether deciphered)","agent's reports from Normandy in the Armada year",2,"France"),
 (258,133,1584,"8 Oct 1584","Philip II (Pardo) -> Alexander Farnese","entirely in cipher, 'sans dechiffre'","Philip II to his governor after the fall of Ghent and before Antwerp",4,"Spain"),
 (258,136,1590,"1 Oct and 11 Nov 1590","Philip II -> Alexander Farnese","two long letters in cipher, 'sans dechiffre', in triplicate","the king's answer on the French expedition and Farnese's complaints",4,"Spain"),
 (404,260,1580,"1576-1584 (three letters)","Alexander Farnese -> Cardinal Alessandro Farnese","three ciphered letters whose decipherment is lost","Farnese's account of the Netherlands war to his uncle",3,"Low Countries"),
 (1671,1101,1588,"1588 (voluminous bundle of notes)","Mazio (Paris) -> Alexander Farnese","bundle of billets entirely in cipher, 'sans dechiffre'","intelligence from Paris during the League crisis",3,"France"),
 (1678,1162,1592,"1592","Adonio Salvi (Spa) -> Alexander Farnese","ciphered letters, 'non dechiffrees'","Farnese's last year; Salvi's reports",3,"Low Countries"),
 (1715,1520,1558,"1557-1559","Octavio Farnese -> Ardinghello, his agent in Spain","ciphered letters, 'sans dechiffre'","Farnese claim to Piacenza during the Spanish-French settlement",3,"Spain"),
 (1716,1529,1569,"undated (c. 1560s-70s)","Margaret of Parma, undated apology 'Bel modo di procedere che ha tenuto...' (copy)","8-page copy with some cipher groups not deciphered","Margaret's justification of her government of the Netherlands",3,"Low Countries"),
 (1717,1580,1580,"1578-1585","Alexander Farnese -> his father Octavio Farnese","several letters in cipher, 'sans dechiffre', on the Netherlands war and the Claudio Landi plot","the Farnese family cipher correspondence",3,"Low Countries"),
 (1720,1614,1590,"1590 (bundle)","Secretary Garnier -> Alexander Farnese","bundle of letters entirely in cipher, 'sans dechiffre'","Farnese's French campaign of 1590",3,"France"),
 (1721,1678,1581,"1581-1582","Pietro Aldobrandino (Lisbon) -> Margaret of Parma","ciphered letters, decipherment missing; apparently on Margaret's rivalry with her son for the Netherlands government","Portuguese succession and the Parma family",3,"Spain"),
 (1735,1801,1564,"6 Aug 1564","Philip II -> Cardinal Granvelle","original entirely in cipher, 'sans dechiffre'","Philip II to Granvelle at the moment of his removal from the Netherlands",4,"Spain"),
 (1766,1857,1570,"1562-1584 (several letters)","Philip II -> Margaret of Parma","several ciphered letters, decipherment often missing","Philip II's cipher with his half-sister governor",3,"Spain"),
]
for (fa, n, yr, date, cor, what, why, imp, reg) in far:
    add(year=yr, date=date, title=f"{cor}: {what}", correspondents=cor, place="unknown", language="Spanish or Italian", region=reg,
        period="1560-1589" if 1560 <= yr <= 1589 else ("1589-1598" if 1589 < yr <= 1598 else "1497-1559"),
        shelfmark=FN.format(f=fa, n=n), folio_note=f"inventory entry [{n}]: {what}", cls="B",
        status="Inventory says the decipherment is missing; Farnese fascio 397 holds key tables for many cipher correspondences and fascio 1624 the key for Alexander's letters to his mother 1578-79 (per the inventory introduction). Not on DECODE (known.py: no hits).",
        why=why, importance=imp, solvability=2, difficulty=3, score_note=SCN,
        verify="Ask the Archivio di Stato di Napoli for the fascio list; fascio 397 key tables are the first thing to see",
        links=[{"label": "Inventaire des archives farnesiennes de Naples (IA)", "href": FIQ + "sans+d%C3%A9chiffr%C3%A9"}], source=SRC,
        prior_art="open (checked 28 Oct 2026: known.py, no repo hit; Gachard/Correspondance de Granvelle and Alexandre Farnese's published Netherlands letters not compared)")

# ---- others ----
add(year=1631, date="28 Mar 1631", title="Magdeburg (Dietrich von Falkenberg's circle) -> Gustavus Adolphus, letter 'almost wholly in figures, unfortunately not resolved'",
    correspondents="Dietrich von Falkenberg (?) -> Gustavus Adolphus", place="Magdeburg", language="German", region="Germany", period="1611-1650",
    shelfmark="Riksarkivet, Stockholm (Gustav Adolf correspondence; as cited in the edition 'Beitraege zur Geschichte' IA beitrgezurgesch00dittgoog, no. 33 of the Magdeburg series)", folio_note="the editor's no. 33; no. 34 may be the plaintext, per Kirchhoff's guess",
    cls="C", status="Editor: 'Fast ganz in Ziffern, die leider nicht aufgeloest sind'; the editor notes elsewhere that the other ciphered letters of the series were decipheringly transcribed in the originals.", why="Last weeks before the sack of Magdeburg, the commandant's appeal to the Swedish king.",
    importance=4, solvability=3, difficulty=3, score_note=SCN, verify="Identify the edition's title page (IA beitrgezurgesch00dittgoog) and the Riksarkivet volume; Stallman's strips (undated, April 1631) and his 29 Dec 1630 cipher letter are companions",
    links=[{"label": "IA volume", "href": "https://archive.org/details/beitrgezurgesch00dittgoog?q=nicht+aufgel%C3%B6st"}], source=SRC,
    prior_art="open (checked 28 Oct 2026: known.py no hit on Falkenberg/Stallman; research/scandinavia mentions a Falkenberg key at VALA 02038 but that is another person)")
add(year=1631, date="2 Mar 1631", title="Unsigned letter (Falkenberg?) -> Gustavus Adolphus, 'mostly in figures', on the Saxon marriage project",
    correspondents="Falkenberg (?) -> Gustavus Adolphus", place="Magdeburg", language="German", region="Germany", period="1611-1650",
    shelfmark="Riksarkivet, Stockholm (as in the edition IA beitrgezurgesch00dittgoog, no. 31)", folio_note="editor extracts the sense of the marriage project from it, so partly read",
    cls="C", status="Editor read the gist; ciphertext not resolved in print.", why="Marriage of Gustavus' daughter to the Saxon prince as a means of holding the Elbe lands.",
    importance=3, solvability=3, difficulty=3, score_note=SCN, verify="As above", links=[{"label": "IA volume", "href": "https://archive.org/details/beitrgezurgesch00dittgoog?q=Ziffern"}], source=SRC,
    prior_art="open (checked 28 Oct 2026: known.py)")
add(year=1792, date="28 Feb 1792", title="Gustavus III of Sweden (Stockholm) -> Count Axel von Fersen, letter in cipher 'non dechiffree'",
    correspondents="Gustavus III -> Axel von Fersen", place="Stockholm", language="French", region="Scandinavia", period="1701-1800",
    shelfmark="Fersen papers (Stafsund / Riksarkivet), as cited by Klinckowstroem, Le comte de Fersen et la cour de France, vol. 1, p. 156 note (IA lecomtedefersen01klingoog)", folio_note="the editor prints the Empress's postscript and says the Swedish letter is in cipher, not deciphered",
    cls="B", status="Edition note only; the cipher letter itself is not printed. Gustavus III's chiffre-klaver is documented in the Uppsala/Riksarkivet material in research/scandinavia.", why="Weeks before the king's assassination, on the intervention in France.",
    importance=4, solvability=2, difficulty=3, score_note=SCN, verify="Locate the original in the Fersen collection (Riksarkivet) and the Gustavian cipher key",
    links=[{"label": "IA volume", "href": "https://archive.org/details/lecomtedefersen01klingoog?q=non+d%C3%A9chiffr%C3%A9e"}], source=SRC,
    prior_art="open (checked 28 Oct 2026: known.py; research/scandinavia/README.md notes the Gustav III green portfolio with a chiffre-klaver)")
add(year=1556, date="24 Jun 1556", title="Ruy Gomez de Silva, count of Melito (Brussels) -> Simon Renard, copy 'en chiffre non traduit'",
    correspondents="Ruy Gomez de Silva -> Simon Renard", place="Brussels", language="Spanish", region="Low Countries", period="1497-1559",
    shelfmark="Bibliotheque municipale de Besancon, papers of Simon Renard (Catalogue general des manuscrits des bibliotheques publiques de France, Departements XXXIII, Besancon II.1, Castan, 1900); volume number to confirm; Fol. 63", folio_note="Fol. 63; copy in untranslated cipher",
    cls="B", status="Catalogue: 'Copie, en chiffre non traduit'. Simon Renard's other ciphers are in this repo (renard1554).", why="Truce of Vaucelles negotiation, Philip II's minister to the ambassador to France.",
    importance=3, solvability=3, difficulty=3, score_note=SCN, verify="Check Besancon's online manuscripts; compare Renard-Philip cipher family",
    links=[{"label": "Castan catalogue (IA)", "href": "https://archive.org/details/cataloguegnr33011900fran?q=chiffre+non+traduit"}], source=SRC,
    prior_art="open (checked 28 Oct 2026: known.py (renard1554 is a different letter))")
add(year=1556, date="17 Sep 1556", title="Ruy Gomez de Silva (Flushing) -> Simon Renard, signed letter in cipher 'non traduite'",
    correspondents="Ruy Gomez de Silva -> Simon Renard", place="Flushing (Vlissingen)", language="Spanish", region="Low Countries", period="1497-1559",
    shelfmark="Bibliotheque municipale de Besancon, papers of Simon Renard (Castan 1900); volume number to confirm; Fol. 115", folio_note="Fol. 115, signed original",
    cls="B", status="Catalogue: 'Lettre chiffree et non traduite. Sign.'", why="Philip II's departure for Spain, Renard at Paris after Vaucelles.",
    importance=3, solvability=3, difficulty=3, score_note=SCN, verify="As for 24 Jun 1556",
    links=[{"label": "Castan catalogue (IA)", "href": "https://archive.org/details/cataloguegnr33011900fran?q=chiffr%C3%A9e+et+non+traduite"}], source=SRC, prior_art="open (checked 28 Oct 2026: known.py)")
add(year=1708, date="5 Jan 1708", title="Anonymous ciphered letter in a volume of copies of political pieces, 'chiffree, non dechiffree'",
    correspondents="unknown (the printed heading gives none)", place="unknown", language="unknown", region="France", period="1701-1800",
    shelfmark="Bibliotheque de l'Arsenal, Paris, ms 6829 (196 ter H.F.), Recueil de pieces, item 57, fol. 296 (Catalogue des manuscrits de la Bibliotheque de l'Arsenal, vol. 2; ms number from OCR, to confirm)", folio_note="item 57, fol. 296",
    cls="C", status="Catalogue: 'Lettre chiffree, non dechiffree. 5 janvier 1708.'", why="Lies in a Louis XIV compilation of the War of the Spanish Succession; the heading gives no sender.",
    importance=2, solvability=2, difficulty=4, score_note=SCN, verify="Look at fol. 296 on Gallica/Arsenal; sender unknown in the catalogue",
    links=[{"label": "Arsenal catalogue (IA)", "href": "https://archive.org/details/cataloguedesman02funcgoog?q=Lettre+chiffr%C3%A9e+non+d%C3%A9chiffr%C3%A9e"}], source=SRC, prior_art="open (checked 28 Oct 2026: known.py)")
for (d, y, who, what, ref) in [
    ("1 Mar 1697", 1697, "Empress Eleonora -> Elector Palatine", "in German and 'largely not deciphered'", "St. A. K. bl. 44/y (Vienna), BRAH 96"),
    ("14 Aug 1698", 1698, "Count Ferdinand Bonaventura von Harrach (Madrid) -> Emperor Leopold I", "in Spanish and 'in part not deciphered'", "HHStA Span. Corr. Fasz. 82 (Vienna), BRAH 97"),
    ("6 Sep 1699", 1699, "Count Sinzendorf (Paris) -> Count Aloys Harrach", "in German and 'in part undecipherable'", "HHStA Span. Varia Fasz. 4x (Vienna), BRAH 98")]:
    add(year=y, date=d, title=f"{who}: {what}", correspondents=who, place="Madrid or Paris", language="German or Spanish", region="Central Europe", period="1651-1700",
        shelfmark=f"Haus-, Hof- und Staatsarchiv Vienna, as calendared in {ref} (Boletin de la Real Academia de la Historia, Austrian documents on the Spanish succession)", folio_note="a single calendar line; the cipher extent is not stated",
        cls="C", status="Calendar note only; overlaps the broader catalogue.json entry on the Harrach/Trautson letters ('teilweise verschluesselt'), so merge there if wanted.", why="Spanish succession politics 1697-99 from the Imperial side.",
        importance=2, solvability=2, difficulty=3, score_note=SCN, verify="Compare with the catalogue.json Harrach entry; HHStA Spanien Korrespondenz",
        links=[{"label": "BRAH volume on IA", "href": "https://archive.org/details/boletindelareala96madr?q=sin+descifrar"}], source=SRC, prior_art="open (checked 28 Oct 2026: known.py)")

for r in rows:
    r.setdefault("seen", "catalogue")
json.dump(rows, open("candidates.json", "w", encoding="utf8"), ensure_ascii=False, indent=1)
print(len(rows))
import collections
print(collections.Counter(r["cls"] for r in rows), collections.Counter(r["importance"] for r in rows))
