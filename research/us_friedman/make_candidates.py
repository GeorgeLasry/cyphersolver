"""Write candidates.json for the Marshall Foundation Friedman Collection sweep (Oct 2026)."""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
G = ("http://web.archive.org/web/20220124223550/http://www.marshallfoundation.org/library/wp-content/"
     "uploads/sites/16/2014/09/Friedman_Collection_Guide_September_2014.pdf")
GL = {"label": "Sheldon, The Friedman Collection: An Analytical Guide (2014), Wayback copy", "href": G}
NSA = "https://www.nsa.gov/Portals/75/documents/news-features/declassified-documents/friedman-documents/"
SRC = "Marshall Foundation Friedman Collection sweep"
SN = ("Scored from the Friedman Collection guide entry during the Oct 2026 Marshall Foundation Friedman sweep "
      "(research/us_friedman/); not viewed")
C = []


def add(**k):
    k.setdefault("source", SRC)
    k.setdefault("score_note", SN)
    k.setdefault("seen", "catalogue")
    C.append(k)


add(year=1781, date="1780-1781",
    title="Cornwallis ↔ Clinton cipher letters left undeciphered (Friedman's photostats and worksheets)",
    correspondents="Charles, Earl Cornwallis ↔ Sir Henry Clinton", place="Carolinas / Virginia / New York",
    language="English", region="Americas", period="1701-1800",
    shelfmark=("George C. Marshall Foundation, William F. Friedman Collection, Item 796.6 (photostats of originals in "
               "the Sir Henry Clinton Papers, William L. Clements Library, Ann Arbor)"),
    folio_note="Folder of photostats with WFF's worksheets; number of letters not stated",
    cls="B",
    status=("Guide (Sheldon 2014, p. 284): 'copies of undeciphered correspondence between Cornwallis and Henry Clinton "
            "... WFF's work sheets'. The same folder holds the British ciphers Lovell deciphered. Not on DECODE "
            "(known.py: no hit beyond the read Cornwallis-Balfour target balfour1781)."),
    why=("The commanders-in-chief's own cipher traffic in the Yorktown campaign; any letter still unread would add to "
         "the best-studied campaign of the war."),
    importance=4, solvability=3, difficulty=2,
    verify=("Identify the letters in the Clinton Papers finding aid (Clements Library) and test them against the "
            "Clinton/Cornwallis systems Lovell broke (balfour1781 rebuilt the southern Common cipher)."),
    links=[GL, {"label": "Clements Library, Spy Letters: secret code",
                "href": "https://clements.umich.edu/exhibit/spy-letters-of-the-american-revolution/secret-methods/secret-code"}],
    prior_art=("open as far as checked (28 Oct 2026: known.py, web search on Clinton Papers ciphers; the Balfour-"
               "Cornwallis intercepts are read in targets/balfour1781, which gives a key family)"))

add(year=1781, date="1780-1781",
    title="Rochambeau → La Luzerne, intercepted French cipher letter that New York could not decipher and sent to London",
    correspondents="Comte de Rochambeau → Chevalier de La Luzerne (French minister, Philadelphia)",
    place="Newport, Rhode Island", language="French", region="Americas", period="1701-1800",
    shelfmark=("Sir Henry Clinton Papers, William L. Clements Library (uncatalogued in 1945); cited in Marshall "
               "Foundation Friedman Collection Item 796.7 (Willcox offprint annotated for ESF)"),
    folio_note="Intercepted letter(s); count unknown",
    cls="B",
    status=("Willcox, 'Rhode Island in British Strategy, 1780-1781', J. Mod. Hist. 17 (1945), summarised in the guide "
            "p. 284: the intercepted letter 'at first could not be deciphered in New York and was sent to London. The "
            "cipher is among the uncatalogued Clinton papers. The author could not find the deciphered version.' Not "
            "on DECODE; no repo hit."),
    why=("The French expeditionary army's cipher to the French minister in the year before Yorktown; reading it shows "
         "what Rochambeau reported and whether the British ever read it."),
    importance=4, solvability=2, difficulty=3,
    verify=("Find the letter in the Clinton Papers (Clements finding aid, 1780-81 volumes); compare with Rochambeau's "
            "army codes ('Chiffre de Robt. Morris', Beinecke GEN MSS 146 box 5, see research/us_beinecke_folger) and "
            "the La Luzerne 1781 code on cryptiana."),
    links=[GL],
    prior_art=("open (checked 28 Oct 2026: web search Rochambeau/Luzerne intercepted cipher + Clinton Papers, Founders "
               "Online; nothing found)"))

add(year=1781, date="1775-1782 (worked by ESF 1952)",
    title="British cipher messages in the Clinton Papers left part-solved by Elizebeth Friedman (1952 worksheets)",
    correspondents="British commanders and agents (Clinton Papers), unknown", place="unknown",
    language="English", region="Americas", period="1701-1800",
    shelfmark=("Marshall Foundation, William F. Friedman Collection, Item 796.8 (photostats from the Sir Henry Clinton "
               "Collection, Clements Library, with ESF worksheets)"),
    folio_note="Photostats + worksheets; extent unknown",
    cls="B",
    status=("Guide p. 284: 'work sheets and notes ... in connection with some uncompleted work done by ESF in 1952 on "
            "British revolutionary cryptographic systems found in the Clements Library.' Which messages stayed unread is "
            "not stated."),
    why=("Revolutionary British messages that the Friedmans themselves did not finish; each one left open has a known "
         "key family."),
    importance=3, solvability=2, difficulty=2,
    verify=("Ask the Marshall Library for scans of Item 796.8 (with 796.6), or match the photostats to Clinton Papers "
            "volumes."),
    links=[GL],
    prior_art="open (checked 28 Oct 2026: guide only)")

add(year=1781, date="c. 1779-1782",
    title=("Continental Congress diplomatic letters: cipher passages still undeciphered in 1956 (Wharton, Revolutionary "
           "Diplomatic Correspondence vols. 4-5)"),
    correspondents="American commissioners and ministers abroad ↔ Continental Congress / Secretary for Foreign Affairs",
    place="Europe / Philadelphia", language="English", region="Americas", period="1701-1800",
    shelfmark=("Marshall Foundation, William F. Friedman Collection, Item 14 (extracts from Wharton, Revolutionary "
               "Diplomatic Correspondence of the United States, vols. 4 and 5, 1889); originals in Papers of the "
               "Continental Congress (NARA RG 360, M247)"),
    folio_note="Extracts marking the cipher passages Wharton printed as undeciphered",
    cls="B",
    status=("Guide p. 26: 'These extracts refer to passages in cipher which had not yet been deciphered in 1956.' The repo "
            "has one sibling (targets/dana1783, Wharton vol. 6). Founders Online editions may have decoded some since."),
    why=("Each passage is a ciphered sentence from the Paris/Madrid/St Petersburg diplomacy of 1780-82; the Lovell and "
         "Livingston ciphers are known keys."),
    importance=3, solvability=4, difficulty=2,
    verify=("Grep Wharton vols. 4-5 (archive.org/HathiTrust) for '(cipher)'/'undeciphered' notes and check each letter on "
            "Founders Online and in PCC M247 for a later decipherment."),
    links=[GL, {"label": "Wharton, Revolutionary Diplomatic Correspondence (HathiTrust record)",
                "href": "https://catalog.hathitrust.org/Record/001263590"}],
    prior_art=("partly checked (28 Oct 2026: dana1783 in the repo covers a vol. 6 letter; the vol. 4-5 passages were not "
               "checked one by one)"))

add(year=1783, date="1776-1792",
    title=("American Revolutionary syllabary (code) letters in three categories 'which cannot be solved by any of the "
           "systems in present archives'"),
    correspondents="Jefferson, Madison, Monroe, Adams and other American officials (unknown)", place="unknown",
    language="English", region="Americas", period="1701-1800",
    shelfmark=("Marshall Foundation, William F. Friedman Collection, Item 796.1 (worksheets and photostats, 'uncompleted "
               "work of WFF')"),
    folio_note="Folder of worksheets, solutions and photostats; the unsolved categories are not listed",
    cls="B",
    status=("Guide p. 281: 'a folder containing the work sheets and solutions on cipher messages and three categories of "
            "syllabaries which cannot be solved by any of the systems in present archives.'"),
    why=("Friedman's own list of early American code letters with no known key; the repo has rebuilt several "
         "Jefferson-era codes (catalogue 483/484), so these may now be within reach."),
    importance=3, solvability=2, difficulty=3,
    verify=("Request scans of Item 796.1 from the Marshall Library; compare the photostats with the Force Book of Cyphers "
            "and the UVA code list (Thurlow-Berkeley 1950)."),
    links=[GL],
    prior_art="open (checked 28 Oct 2026: guide only; cf. repo catalogue 483/484 Jefferson codes)")

add(year=1780, date="Sept 1780",
    title="Benedict Arnold's 'treasonable cow letter', open code never deciphered",
    correspondents="Benedict Arnold → unknown (British side of the West Point plot)",
    place="West Point / Robinson House, New York", language="English", region="Americas", period="1701-1800",
    shelfmark=("Marshall Foundation, William F. Friedman Collection, Item 611 (facsimile printed by Hampshire Paper Co., "
               "South Hadley Falls, 193?, 6 copies); also NSA Friedman Collection A62872, lecture slide 6.8"),
    folio_note="One letter in open code (veiled language), no cipher symbols",
    cls="C",
    status=("Guide p. 220: dated two weeks before André's capture, 'in code that has never been deciphered ... open "
            "code'. Friedman's lecture slide (A62872) calls it 'indecipherable'. Repo: no hit."),
    why=("An Arnold message from the last fortnight of the plot; matching its veiled terms to the Arnold-André "
         "correspondence would add a step to the best-known treason in US history."),
    importance=3, solvability=2, difficulty=4,
    verify=("Locate the original (source of the Hampshire Paper Co. facsimile: Clements Clinton Papers or a private "
            "collection) and read it against the July-Sept 1780 Arnold-André letters."),
    links=[GL, {"label": "NSA Friedman Collection A62872 lecture notes (slide 6.8)",
                "href": NSA + "lectures-speeches/FOLDER_170/41759009079814.pdf"}],
    prior_art=("open (checked 28 Oct 2026: web search 'cow letter' Arnold; only Friedman's slide and a VIAF/LoC note "
               "saying never deciphered)"))

add(year=1855, date="c. 1852-1870",
    title="Cipher texts painted on a Winterhalter canvas (French Second Empire), never deciphered",
    correspondents="Franz Xaver Winterhalter (painter) / Second Empire court (unknown)", place="Paris (probably)",
    language="unknown", region="France", period="1801-1900",
    shelfmark=("Marshall Foundation, William F. Friedman Collection, Item 1040 (photograph of the painting given by Brig. "
               "John Tiltman, WFF worksheets, extract of Vizetelly, Court Life of the Second French Empire 1852-1887, "
               "pp. 70-75)"),
    folio_note="A series of cipher texts on one painting; length unknown",
    cls="C",
    status=("Guide p. 357: 'a series of cipher texts never deciphered. WFF has spent a few hours in an attempt to solve "
            "the cipher texts ... but without success.' The painting is not named; the Vizetelly extract presumably "
            "tells the story."),
    why="A Tiltman-and-Friedman failure on a court painting; reading it would explain a Second Empire court curiosity.",
    importance=2, solvability=2, difficulty=3,
    verify=("Read Vizetelly 1908 pp. 70-75 (archive.org) to identify the painting, then find a high-resolution image of "
            "it."),
    links=[GL, {"label": "Vizetelly, Court Life of the Second French Empire (archive.org search)",
                "href": "https://archive.org/search?query=Court+Life+of+the+Second+French+Empire"}],
    prior_art="open (checked 28 Oct 2026: web search Winterhalter cipher painting; nothing)")

add(year=1917, date="1917-1918 (inquiry 1963-1969)",
    title="'Burdick ciphers': cipher evidence of the German-Mexican conspiracy, World War I",
    correspondents="German agents in Mexico (unknown); WFF ↔ Dr Glenn G. Morgan", place="Mexico / unknown",
    language="unknown (German or Spanish)", region="Americas", period="1901-1950",
    shelfmark=("Marshall Foundation, William F. Friedman Collection, Item 1931 (WFF correspondence with Glenn G. Morgan, "
               "'also re Burdick Ciphers 1963-1969')"),
    folio_note="Correspondence; whether ciphertext copies are enclosed is not stated",
    cls="C",
    status=("Guide p. 616: 'Recent inquiry on cryptographic evidence of Mexican-German conspiracy in WWI (Burdick "
            "Ciphers).' Probably material from Charles B. Burdick's research on German operations in Mexico. Solution "
            "status unknown."),
    why=("German-Mexican plot traffic after the Zimmermann telegram; Burdick worked from German archives, so the texts "
         "may be unpublished."),
    importance=3, solvability=1, difficulty=3,
    verify=("Request Item 1931 from the Marshall Library; check Burdick's publications for the ciphers and whether Morgan "
            "published on them."),
    links=[GL],
    prior_art="open (checked 28 Oct 2026: web search 'Burdick ciphers' Morgan; nothing)")

add(year=1930, date="unknown (1920s-1950s)",
    title="Symbol cipher sent to the Army Signal Corps with a challenge to 'anyone in the world' to solve it",
    correspondents="unknown inventor → U.S. Army Signal Corps / WFF", place="unknown",
    language="English (presumably)", region="Americas", period="1901-1950",
    shelfmark="Marshall Foundation, William F. Friedman Collection, Item 1956 (folder of cipher and code messages, part K)",
    folio_note=("One challenge message; the same folder has L) a symbol cipher used by the German spy Rumrich (1938) and "
                "M) a Playfair message, Spanish espionage"),
    cls="C",
    status=("Guide p. 623: folder of items 'many of them sent to him for solutions'; K) 'A symbol cipher method sent to "
            "Army Signal Corps with the developer challenging anyone in the world to solve it.' No solution noted for K, "
            "L or M."),
    why=("A challenge cipher on file with WFF, minor in itself; L and M (Rumrich 1938, Spanish espionage Playfair) are "
         "real espionage traffic."),
    importance=1, solvability=2, difficulty=3,
    verify="Request scans of Item 1956 K-M; check the Rumrich case files (FBI/NARA) for the symbol cipher.",
    links=[GL],
    prior_art="not checked beyond the guide (28 Oct 2026)")

add(year=1927, date="c. 1927",
    title="'Historic code message' on Nelson's Trafalgar signal: a Navy cryptanalyst's challenge to Friedman",
    correspondents="Claus Bogel (U.S. Navy, ex-Black Chamber) → WFF", place="Washington",
    language="English", region="Americas", period="1901-1950",
    shelfmark=("Marshall Foundation, William F. Friedman Collection, Item 212 (Part I challenge message; Part II Coast "
               "Guard Circular June 1927; 'Lord Chesterfield cipher')"),
    folio_note="One challenge message",
    cls="C",
    status=("Guide p. 105: 'A navy cryptanalyst challenges WFF with a cryptographic message.' Whether WFF solved it is not "
            "stated."),
    why="A practitioner's challenge from the Black Chamber circle; low historical weight.",
    importance=1, solvability=2, difficulty=2,
    verify="Request Item 212; check whether the solution is in the folder.",
    links=[GL],
    prior_art="not checked beyond the guide (28 Oct 2026)")

add(year=1930, date="unknown (c. 1920s-1930s)",
    title=("'Cryptograms submitted to Brigman': a poem solution to prove, and a second 46-group cryptogram 'in the same "
           "key'"),
    correspondents="unknown → Brigman (challenge); copy in WFF's files", place="unknown",
    language="English", region="Americas", period="1901-1950",
    shelfmark=("NSA William F. Friedman Collection of Official Papers, A273674 (Patent and Equipment Records, folder 116), "
               "14 pp."),
    folio_note=("p. 1: cryptogram 1 (word-length groups) with a fitted poem, cryptogram 2 (46 five-letter groups); "
                "pp. 4-13 handwritten worksheets"),
    cls="A",
    status=("Viewed 28 Oct 2026: the worksheets check the poem against cryptogram 1 and carry long handwritten letter "
            "runs that may be the solution of cryptogram 2; not confirmed. Probably a puzzle, not a real message."),
    why="Low historical weight; listed because it is a challenge cryptogram in Friedman's files with no solution stated.",
    importance=1, solvability=5, difficulty=2,
    verify=("Read worksheet pp. 6-13 of A273674 to see whether cryptogram 2 is solved; if not, solve it with the key "
            "from cryptogram 1."),
    links=[{"label": "NSA A273674 PDF", "href": NSA + "patent-equipment/FOLDER_116/41763399080253.pdf"}],
    seen="image",
    score_note=("Scored from the NSA PDF (pp. 1 and 6 viewed) during the Oct 2026 Marshall Foundation Friedman sweep "
                "(research/us_friedman/)"),
    prior_art="not checked (28 Oct 2026); likely a modern puzzle")

add(year=1953, date="c. 1953",
    title="A 16th-century book 'allegedly in cipher' that Major Rhea M. Smith (Rollins College) was trying to solve",
    correspondents="Maj. Rhea M. Smith (USAR, ex-ASA Historical Branch) ↔ WFF", place="Winter Park, Florida",
    language="unknown", region="Other", period="1497-1559",
    shelfmark="NSA William F. Friedman Collection of Official Papers, A67868 (Correspondence, folder 028), 2 pp.",
    folio_note="Letter only; the book is not named (Smith withheld author and title)",
    cls="C",
    status=("Read 28 Oct 2026 (OCR): WFF lends Smith manuals and hopes he is 'on the right track toward a complete "
            "solution'. The book is unidentified; probably a hidden-cipher claim of the Baconian kind."),
    why=("Only a lead: if Smith's papers name the book it may be a real early printed cipher text, more likely a "
         "steganographic claim."),
    importance=1, solvability=1, difficulty=4,
    verify="Look for Rhea M. Smith papers in the Rollins College archives for the book's identity.",
    links=[{"label": "NSA A67868 PDF", "href": NSA + "correspondence/FOLDER_028/41786929082593.pdf"}],
    seen="image",
    score_note="Scored from the NSA PDF text during the Oct 2026 Marshall Foundation Friedman sweep (research/us_friedman/)",
    prior_art="not checked (28 Oct 2026)")

json.dump(C, open(os.path.join(HERE, "candidates.json"), "w", encoding="utf8"), ensure_ascii=False, indent=1)
print(len(C))
