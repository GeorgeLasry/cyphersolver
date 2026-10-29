import json
SC = "Scored from web-search descriptions during the Oct 2026 Canada/Latin America sweep (research/canada_latam/); not viewed"


def row(**k):
    base = dict(region="Americas", seen="catalogue", source="Canada/Latin America sweep", decode_ids=[], score_note=SC)
    base.update(k)
    return base


C = [
    row(year=1759, date="23 Aug 1758 - 25 Jun 1759",
        title="Kerlérec, governor of Louisiana → Ministry of Marine, despatches, some in cipher",
        correspondents="Louis Billouart de Kerlérec → Minister of Marine", place="New Orleans", language="French",
        period="1701-1800",
        shelfmark="Ministère des Armées digital library (bibliotheques-numeriques.defense.gouv.fr), inventory document 2bc715e2-0c87-4ded-899c-253d205989e5; cote not read (host refused connections during the sweep)",
        folio_note="'dont quelques-unes chiffrées' per the inventory; number of cipher pieces unknown", cls="C",
        status="Inventory says some despatches are in cipher; no decipherment mentioned. Not on DECODE (known.py no hits). Sibling Kerlerec cipher items of 1756-57 are already in the catalogue (Huntington sweep). Reached only through a web-search snippet; the page itself was not opened.",
        why="Louisiana's governor reporting on Choctaw alliances and British pressure in the Seven Years' War; a later date in the family of Kerlerec cipher despatches.",
        importance=3, solvability=2, difficulty=3,
        verify="Open the inventory page, read the cote and which despatches are marked chiffrées; compare with ANOM C13A Louisiana registers (clear copies, possible cribs) and the Huntington Kerlerec items.",
        links=[{"label": "Ministère des Armées inventory record", "href": "https://bibliotheques-numeriques.defense.gouv.fr/emd/impression/document/2bc715e2-0c87-4ded-899c-253d205989e5"}],
        prior_art="open as far as checked (28 Oct 2026: web search only; cryptiana not checked)"),
    row(year=1825, date="1825",
        title="Pablo Obregón, Mexican minister in Washington → Foreign Ministry, coded despatches (beyond the two Narváez decodings)",
        correspondents="Pablo Obregón → Secretaría de Relaciones Exteriores", place="Washington", language="Spanish",
        period="1801-1900",
        shelfmark="Archivo Histórico Genaro Estrada (SRE, Mexico), Obregón despatches from Washington; legajo not read",
        folio_note="Narváez examined 'a small sample' of 1825 coded despatches and published two decodings; a further 1826 despatch decoded separately",
        cls="B",
        status="Part published by Roberto Narváez (Historia Mexicana, 'Los despachos codificados de Pablo Obregón desde Washington en 1825'; separate 1826 decoding). That other coded despatches remain unread is an inference from 'small sample', not confirmed. Not on DECODE. Not found digitised online.",
        why="Early Mexican republic's minister reporting on US policy, Cuba and the Panama Congress; Narváez's system would be a key for the rest.",
        importance=3, solvability=1, difficulty=3,
        verify="Read Narváez's article for the system and the list of coded despatches; ask the AHGE which are digitised; check the appendices of Narváez, Criptografía política, diplomática y militar en México (1813-1926).",
        links=[{"label": "Narváez, Historia Mexicana (search hit)", "href": "https://historiamexicana.colmex.mx/index.php/RHM/article/download/1751/1569"},
               {"label": "SRE acervo page", "href": "https://portales.sre.gob.mx/acervo/nuestros-archivos/476"}],
        prior_art="partly read (Narváez; checked 28 Oct 2026, web search only)"),
    row(year=1826, date="23 Jan and 9 Apr 1826",
        title="José Anastasio Torrens, Mexican chargé in Bogotá → Foreign Ministry, reserved notes 2 and 3 in cipher and code",
        correspondents="José Anastasio Torrens → Primera Secretaría de Relaciones", place="Bogotá", language="Spanish",
        period="1801-1900",
        shelfmark="Archivo Histórico Genaro Estrada (SRE, Mexico); legajo not read",
        folio_note="Narváez, Memorias de la Academia Mexicana de la Historia 49 (2007-08) pp. 7-43, describes a cipher and a code; code samples poorly preserved",
        cls="B",
        status="Narváez analysed the cipher system but says his inferences on the code materials were 'escasamente informadas' (little archive information, poor condition). Cipher part probably read; code part possibly open. Not on DECODE.",
        why="Mexico's envoy in Bolívar's Colombia (Panama Congress, Cuba, Bolívar's position) writing in a rarely studied code.",
        importance=3, solvability=2, difficulty=4,
        verify="Read the Memorias article and the 2009 Estudios de Historia Moderna article (n. 38) for which notes are decoded; locate images.",
        links=[{"label": "Narváez 2009, Estudios de Historia Moderna y Contemporánea de México 38", "href": "https://moderna.historicas.unam.mx/index.php/ehm/article/download/17768/16948/25169"}],
        prior_art="partly read (Narváez 2007, 2009; checked 28 Oct 2026)"),
    row(year=1824, date="6 Oct 1824",
        title="Probably José Mariano Michelena, Mexican confidential agent in London → Alamán, cipher letter",
        correspondents="José Mariano Michelena (attributed) → Lucas Alamán", place="England", language="Spanish",
        period="1801-1900",
        shelfmark="AHDSREM leg. 40-11-3 (Mexican Foreign Ministry historical archive, per the citation in Narváez)",
        folio_note="one letter", cls="C",
        status="Narváez (Estudios de Historia Moderna y Contemporánea de México 41, 2011) argues from cryptanalysis and analogy that Michelena probably wrote it; unclear whether the text was fully read or only attributed. Not on DECODE.",
        why="Mexico's first London mission (recognition, loan, Cuba); authorship and content both bear on Alamán's foreign policy.",
        importance=3, solvability=1, difficulty=4,
        verify="Read Narváez 2011 (Redalyc 94120769006) for what was recovered; ask SRE for the scan.",
        links=[{"label": "Narváez 2011 (Redalyc)", "href": "https://www.redalyc.org/pdf/941/94120769006.pdf"}],
        prior_art="partly analysed (Narváez 2011; checked 28 Oct 2026)"),
]
json.dump(C, open('candidates.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(C))
