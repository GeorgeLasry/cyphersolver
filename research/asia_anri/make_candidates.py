"""Write candidates.json for the ANRI sweep (hand-picked rows from aid_hits.txt, na_jakarta_hits.jsonl, na_21014_jakarta.jsonl)."""
import json

NOTE = "Scored from the archive description during the Oct 2026 ANRI sweep (research/asia_anri/); not viewed"
NA = 'https://www.nationaalarchief.nl/onderzoeken/archief/'
ANRI_AS = ('https://anri.go.id/download/inventaris-arsip-tekstual-algemene-secretarie-v.d.-nederlandsindische-'
           'regering-en-gedeponeerde-archieven-19421950-1641884401')
SRC = 'Arsip Nasional Republik Indonesia sweep'
XSRC = 'Arsip Nasional Republik Indonesia sweep (cross-lead, Nationaal Archief)'
C = []


def add(**k):
    k.setdefault('score_note', NOTE)
    k.setdefault('seen', 'catalogue')
    k.setdefault('source', SRC)
    C.append(k)


add(year=1948, date="Jun-Dec 1948",
    title="Soerjotjondro (Batavia) → telegraphic address 'Epidnation', Singapore: code telegrams, not decoded",
    correspondents="Soerjotjondro (Republican, Batavia) → 'Epidnation', Singapore", place="Batavia",
    language="unknown", region="Other", period="1901-1950",
    shelfmark=("ANRI, Algemene Secretarie van de Nederlands-Indische Regering en gedeponeerde archieven 1942-1950, "
               "inv. nr. 1406 (= NA 2.10.14 inv. 1406, 'wordt bewaard in het Arsip Nasional te Jakarta')"),
    folio_note="1 omslag; telegrams passed by the telegraph office to the Algemene Secretarie and NEFIS for clearance before transmission",
    cls="C",
    status=("Finding aid: 'De teksten zijn niet gedecodeerd en volstrekt onbegrijpelijk' (not decoded, wholly "
            "unintelligible). Original kept in Jakarta; not scanned (no ANRI image service for this fonds; the NA "
            "description says it is held in Jakarta). Not on DECODE; known.py no hits."),
    why=("Republican-era code traffic out of Batavia that the Dutch censors could not read. Caution: 'Epidnation' looks "
         "like the telegraphic address of the League of Nations (later WHO) Eastern Epidemiological Bureau in Singapore, "
         "so these may be epidemic reports in the published international epidemiological telegraph code rather than "
         "political traffic."),
    importance=2, solvability=2, difficulty=2,
    verify=("Confirm 'Epidnation' = Singapore epidemiological bureau address; identify Soerjotjondro (Republican health "
            "service?); if so, get the published epidemiological code, then ask ANRI for scans of inv. 1406."),
    links=[{"label": "ANRI inventory (PDF), inv. 1406", "href": ANRI_AS},
           {"label": "NA 2.10.14 inventory (same description)", "href": NA + "2.10.14"}],
    prior_art="open (checked 28 Oct 2026: web search 'Epidnation', known.py; no edition)")

add(year=1944, date="1942-1945",
    title="Secret telegrams received by Van Mook, the BSO and the naval commander in Australia, 'often cryptic'",
    correspondents="various → H.J. van Mook / Bevelhebber der Strijdkrachten in het Oosten / Marine Commandant Australië",
    place="Australia", language="Dutch", region="Low Countries", period="1901-1950",
    shelfmark="ANRI, Algemene Secretarie 1942-1950, inv. nr. 24 (= NA 2.10.14 inv. 24, kept in Jakarta)",
    folio_note="size unknown", cls="C",
    status=("Finding aid: 'De inhoud van de telegrammen is veelal cryptisch'. Probably clear telegrams with code words "
            "rather than cipher; not scanned. Not on DECODE."),
    why="Wartime Netherlands Indies government-in-exile traffic; 'cryptic' may hide code-word or code-group passages.",
    importance=3, solvability=1, difficulty=3,
    verify="Ask ANRI whether inv. 24 holds code groups or only clear telegrams with cover names.",
    links=[{"label": "ANRI inventory (PDF), inv. 24", "href": ANRI_AS}],
    prior_art="open (checked 28 Oct 2026: known.py)")

# Hague items found through the cross-check (all PHYSICAL, i.e. not scanned)
add(year=1947, date="1947-1948",
    title="Intercepted Republican telegrams and captured documents, partly in code, with papers on breaking the codes",
    correspondents="Republican authorities (unknown) → unknown", place="Java", language="Indonesian", region="Other",
    period="1901-1950",
    shelfmark="Nationaal Archief 2.10.17 (Procureur-Generaal bij het Hooggerechtshof van Nederlands-Indië), inv. nr. 735",
    folio_note="size unknown; not scanned (availability PHYSICAL)", cls="A",
    status=("Description: 'Onderschepte republikeinse telegrammen en andere buitgemaakte documenten, deels in code, met "
            "stukken over het ontcijferen van deze codes'. Decipherment work attached, extent unknown (may be partial). "
            "Hague, not Jakarta; found while cross-checking. Not on DECODE; known.py no hits."),
    why="Republic code traffic with the Dutch side's own decipherment notes: a sibling key source for other open TNI/Republic code messages.",
    importance=3, solvability=2, difficulty=2,
    verify="Order a scan from the NA; check whether the deciphering papers cover all the coded items.",
    links=[{"label": "NA 2.10.17", "href": NA + "2.10.17"}],
    prior_art="open (checked 28 Oct 2026: known.py)", source=XSRC)

add(year=1947, date="31 Jan 1947",
    title="Penilik Djawa Timoer: coded telegram on sabotage of the Malang transmitter, with a Poesat Badan Pengawas Oemoem report",
    correspondents="Penilik Djawa Timoer → Republican authorities", place="Malang", language="Indonesian",
    region="Other", period="1901-1950",
    shelfmark="Nationaal Archief 2.10.62 (NEFIS/CMI archive), inv. nr. 5584 (NEFIS doc. 4257, captured Poerwokerto 12-1-1948)",
    folio_note="original + translation; size unknown; PHYSICAL", cls="C",
    status=("Description: 'met gecodeerd telegram'. A translation is present but may cover only the report. Not on DECODE."),
    why="Republican internal code of early 1947 (Linggadjati period).", importance=2, solvability=2, difficulty=3,
    verify="Scan request at NA; check whether the NEFIS translation renders the coded telegram.",
    links=[{"label": "NA 2.10.62", "href": NA + "2.10.62"}],
    prior_art="open (checked 28 Oct 2026: known.py)", source=XSRC)

add(year=1948, date="30 Jul 1948", title="HK TNI order on general mobilisation and guerrilla units, with a coded message",
    correspondents="Hoofdkwartier TNI → commanders", place="Yogyakarta", language="Indonesian", region="Other",
    period="1901-1950",
    shelfmark="Nationaal Archief 2.10.62 (NEFIS/CMI archive), inv. nr. 6271 (NEFIS doc. 4945, captured 25-8-1948)",
    folio_note="original + translation; PHYSICAL", cls="C",
    status="Description: 'en gecodeerd bericht'. Decoding not mentioned. Not on DECODE.",
    why="TNI headquarters code on the eve of the second Dutch offensive (Dec 1948).", importance=3, solvability=2,
    difficulty=3,
    verify=("Scan request at NA; compare with the TNI radio code sheet 2.10.62 inv. 5470 and the CMI Afd. VIII decodes "
            "(2.13.132 inv. 938; 2.10.14 inv. 3904-3952)."),
    links=[{"label": "NA 2.10.62", "href": NA + "2.10.62"}],
    prior_art="open (checked 28 Oct 2026: known.py)", source=XSRC)

add(year=1947, date="Jan 1947", title="Documents captured by the KNIL at Bandjermasin with intelligence information partly in code",
    correspondents="Republican intelligence, South Borneo → unknown", place="Bandjermasin", language="Indonesian",
    region="Other", period="1901-1950",
    shelfmark="Nationaal Archief 2.10.62 (NEFIS/CMI archive), inv. nr. 4720 (NEFIS doc. 3391)",
    folio_note="original + translation; PHYSICAL", cls="B",
    status=("Description: 'met intelligence-informatie (deels in code)'. Code sheets captured in the same region in 1947 "
            "(inv. 4693 Sampit, inv. 4678) may be the key. Not on DECODE."),
    why="Local Republican intelligence code in Kalimantan, with possible keys among sibling captured sheets.",
    importance=2, solvability=2, difficulty=2,
    verify="Scan request; pair with inv. 4693 (code found at Sampit, 24-4-1947) and inv. 4678.",
    links=[{"label": "NA 2.10.62", "href": NA + "2.10.62"}],
    prior_art="open (checked 28 Oct 2026: known.py)", source=XSRC)

add(year=1947, date="1946-1948", title="Codings used by Republican groups, intercepted by Bk. Makassar",
    correspondents="Republican groups, South Celebes → unknown", place="Makassar", language="Indonesian",
    region="Other", period="1901-1950",
    shelfmark="Nationaal Archief 2.10.62 (NEFIS/CMI archive), inv. nr. 2914",
    folio_note="PHYSICAL; size unknown", cls="B",
    status=("Description: 'Stukken betreffende door Bk. Makassar onderschepte, bij Republikeinse groeperingen gebruikte "
            "coderingen'. May be code tables only (then a key lead) or coded messages. Not on DECODE."),
    why="Republican codes in East Indonesia; with the 1947 'Code voor Boeginees en Makassaars' (inv. 4678) it could read local intercepts.",
    importance=2, solvability=2, difficulty=2, verify="Scan request; check whether ciphertexts are included.",
    links=[{"label": "NA 2.10.62", "href": NA + "2.10.62"}],
    prior_art="open (checked 28 Oct 2026: known.py)", source=XSRC)

json.dump(C, open('candidates.json', 'w', encoding='utf8'), ensure_ascii=False, indent=1)
print(len(C))
