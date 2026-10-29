"""Hand-written candidate rows from the DPLA bulk export + Smithsonian Open Access sweep (28 Oct 2026).
Run: python -X utf8 make_candidates.py  -> candidates.json
Every row was checked with research/archive_sweep_2026-10/known.py (no hits unless noted in status)."""
import json

SRC = "DPLA/Smithsonian sweep"
NOTE = "Scored from the hub's catalogue description during the Oct 2026 DPLA/Smithsonian sweep (research/dpla_smithsonian/); not viewed"
rows = []


def add(year, date, title, corr, place, lang, region, period, shelf, folio, cls, status, why, imp, sol, dif, verify,
        links, prior, seen="catalogue", decode_ids=None):
    r = dict(year=year, date=date, title=title, correspondents=corr, place=place, language=lang, region=region,
             period=period, shelfmark=shelf, folio_note=folio, cls=cls, status=status, why=why, importance=imp,
             solvability=sol, difficulty=dif, score_note=NOTE, verify=verify,
             links=[{"label": a, "href": b} for a, b in links], seen=seen, source=SRC, prior_art=prior)
    if decode_ids:
        r["decode_ids"] = decode_ids
    rows.append(r)


CK = "open (checked 28 Oct 2026: web search, Cipherbrain/Schmeh blog, catalogue description; no decipherment found)"

add(1878, "8 Aug 1878; 2 Nov 1883; 23 Apr 1884",
    "Machain (1878), Decoud (1883) and Perousha (1884) → Juan Silvano Godoi, three Paraguayan letters in code",
    "Raymundo Machain (Montevideo), Héctor Francisco Decoud, Sofia Perousha → Juan Silvano Godoi",
    "Montevideo / Buenos Aires / Asunción exile network", "Spanish", "Americas", "1801-1900",
    "UC Riverside, Special Collections, Juan Silvano Godoi papers (MS 003), letters of 1878-08-08 (mostly in code), 1883-11-02 (partly), 1884-04-23 (partly); Calisphere items",
    "Machain 2 leaves mostly code; Decoud and Perousha partial passages", "C",
    "Item-level finding-aid text: 'mostly written in code', 'writes partially in code on the possibility of revolutionary undertaking', 'partly in code'. No key or decipherment noted. Not on DECODE. known.py: no hits for Godoi.",
    "Exile conspiracy letters of Paraguayan politicians after the War of the Triple Alliance; a rare Latin American 19th-century nomenclator with a known plaintext language.",
    3, 3, 3, "View the three Calisphere items; check the other Godoi correspondence in the same folders for sibling letters with glosses or a key.",
    [("Machain 1878 (Calisphere)", "https://calisphere.org/item/a49b049d-f02c-43d2-a23e-e587084e63fd"),
     ("Decoud 1883 (Calisphere)", "https://calisphere.org/item/cd42bc77-7600-420a-85f5-2d45175bbfc2"),
     ("Perousha 1884 (Calisphere)", "https://calisphere.org/item/373fae5b-f04c-498a-b67d-da75e328f858"),
     ("Finding aid (OAC)", "https://oac.cdlib.org/findaid/ark:/13030/kt4779s0t4")], CK)

add(1880, "1879-1880",
    "Charles H. Loud → Annette ('Nettie') Carruth, 54 cipher postcards",
    "Charles H. Loud → Annette P. Carruth (future wife)", "Boston / Wellesley / Newton / Jacksonville FL / New York", "English (probably)",
    "Americas", "1801-1900", "Historic Newton archives, Charles H. Loud postcards (catalogaccess 10132); DPLA via Digital Commonwealth",
    "54 penny postcards, each unique, 'all written in cipher'; one deciphered and transcribed", "A",
    "Archive description: 'Each card is unique. All are written in cipher. One card has been deciphered and transcribed.' So 53 open plus a known-plaintext crib card. Not on DECODE. Not on Schmeh's postcard lists as far as the search showed.",
    "A courting couple's private cipher in 1879-80; one transcribed card gives a crib for the other 53, so a full reading is likely.",
    1, 4, 2, "View the postcards on Historic Newton's catalogue; get the transcribed card, test whether it is a simple substitution, apply to the rest.",
    [("Historic Newton record", "https://historicnewton.catalogaccess.com/archives/10132")],
    "open (checked 28 Oct 2026: web search found nothing on Loud or Carruth; Schmeh's postcard posts do not name them)")

add(1899, "Apr-Dec 1899",
    "Bunker Hill & Sullivan Co.: about 35 coded telegrams Burbidge / Bradley / Granger during the Coeur d'Alene labour troubles",
    "Frederick Burbidge, F. W. Bradley, Alex Granger", "Wardner ID / San Francisco / Seattle", "English (commercial code words)",
    "Americas", "1801-1900", "University of Idaho Special Collections, Bunker Hill Company records MG 367 (bunkerhill items, e.g. bunkerhill162, bunkerhill122)",
    "about 35 telegram records tagged 'Codes'; one carries a handwritten note 'possibly deciphering message'", "A",
    "Records say 'Telegram written in code'; the cataloguers guess topics (hiring, trial, Pinkerton detective). Bunkerhill122 (3 Sep 1899) has a handwritten note possibly deciphering the message, a crib. No codebook found in the series by search. Not on DECODE. known.py: no hits.",
    "Mine-owner telegrams in a commercial code during the 1899 Bunker Hill strike and the Idaho martial-law period; a codebook elsewhere in MG 367 may exist.",
    2, 3, 3, "View bunkerhill122 for the handwritten note; ask Idaho Special Collections whether MG 367 has the telegraph code book (Western Union / Bentley's / private).",
    [("bunkerhill122", "https://www.lib.uidaho.edu/digital/bunkerhill/items/bunkerhill122.html"),
     ("bunkerhill162", "https://www.lib.uidaho.edu/digital/bunkerhill/items/bunkerhill162.html")],
    "open (checked 28 Oct 2026: web search found only the catalogue records, no key)")

add(1892, "1889-1899",
    "Henry Clay Frick → Andrew Carnegie, 19 coded telegrams (Homestead 1892 among them)",
    "H. C. Frick → Andrew Carnegie (and replies)", "Pittsburgh / Scotland", "English (code words)",
    "Americas", "1801-1900", "University of Pittsburgh, Historic Pittsburgh: 'Frick wires Carnegie a coded message' series (pitt:31735064659596 and 18 siblings)",
    "19 records dated 1889-1899; some with a one-line gloss ('possession May first' discernible)", "C",
    "Titles only say 'a coded message'. The series is the Carnegie Steel private code. Not on DECODE. known.py: no hits for Frick or Carnegie telegrams.",
    "Frick-Carnegie telegrams during Homestead (July 1892) are among the best-documented US business cipher traffic; no codebook is known online.",
    3, 2, 4, "View the telegrams; search Frick/Carnegie correspondence at Carnegie Library and Frick Archives for a plain-text copy or the code book.",
    [("First record", "https://historicpittsburgh.org/islandora/object/pitt%3A31735064659596"),
     ("Second record", "https://historicpittsburgh.org/islandora/object/pitt%3A31735064659604")],
    "open (checked 28 Oct 2026: catalogue only)")

add(1870, "May-Jul 1870",
    "Fernández Cavada brothers and Alfaro: Cuban Ten Years' War letters and telegram with cipher lists",
    "Federico, Adolfo and Emilio Fernández Cavada; V. García; Ignacio F. Alfaro", "Cienfuegos / Villas, Cuba and New York", "Spanish",
    "Americas", "1801-1900", "University of Miami Cuban Heritage Collection, Fernando Fernández-Cavada Collection (chc5006), items 1719, 1956, 2200, 2543, 2876, 2912, 2924",
    "letters tagged 'Ciphers; Languages, Secret'; two items 'List of secret codes made up of numbers and letters' (a key?)", "B",
    "Subject headings 'Signs and symbols; Ciphers; Languages, Secret' on 4 letters, a telegram tagged 'Cipher and telegraph codes' (12 Jul 1870) and two 'List of secret codes made up of numbers and letters' sheets in the same collection (id 2876, 2912). Also CHC chc0336 'List of secret codes to deciphering writing'. Not on DECODE; known.py no hits.",
    "Insurgent officers' code letters of the 1868-78 Cuban war, with what look like the code lists in the same file.",
    3, 4, 2, "View items 2876 and 2912 (the lists), then the telegram 2924 of 12 Jul 1870 and the four letters.",
    [("Telegram 12 Jul 1870", "http://cdm17191.contentdm.oclc.org/cdm/ref/collection/chc5006/id/2924"),
     ("List of secret codes", "http://cdm17191.contentdm.oclc.org/cdm/ref/collection/chc5006/id/2876"),
     ("List of secret codes (2)", "http://cdm17191.contentdm.oclc.org/cdm/ref/collection/chc5006/id/2912"),
     ("Letter 23 Jul 1870", "http://cdm17191.contentdm.oclc.org/cdm/ref/collection/chc5006/id/1956")],
    "open (checked 28 Oct 2026: web search on Fernández Cavada ciphers found nothing)")

add(1894, "28 Jan 1894",
    "J. Norma letter on the Cuban independence war effort (subject: Ciphers; Gómez, Máximo)",
    "J. Norma → unknown", "unknown", "Spanish (probably)", "Americas", "1801-1900",
    "University of Miami Cuban Heritage Collection, chc0347, item 11716", "letter-length; amount of cipher unknown", "C",
    "Subject headings only: 'Gómez, Máximo; Ciphers; War; Autonomy'. No further description. Not on DECODE.",
    "Pre-1895 Cuban independence correspondence tagged as cipher, Gómez's circle.", 2, 2, 3,
    "View the scan; confirm that there is cipher text and not just a keyed phrase.",
    [("CONTENTdm item", "http://cdm17191.contentdm.oclc.org/cdm/ref/collection/chc0347/id/11716")], CK)

add(1807, "1807",
    "Sir George Barlow (Calcutta) → Lord Grenville, official and private reports 'written in a curious cipher'",
    "Sir George Barlow → Thomas Grenville (Lord Grenville) and George Tierney", "Calcutta", "English (probably)", "Other",
    "1801-1900", "Cleveland Public Library, John G. White / Zamboni collection, p4014coll9 id 50900 (Zamboni note #159)",
    "reports 'written in a curious cipher with covering letters'", "C",
    "Cleveland description: 'Two letters to Thomas Grenville (in cipher) and to George Tierney on affairs in India'; Zamboni note adds 'official, private and confidential reports written in a curious cipher'. Not on DECODE. known.py: no useful hits.",
    "East India Company Governor-General's confidential cipher reports, 1807 (Barlow acting GG 1805-07).",
    3, 2, 4, "View the CPL scans; check Grenville (Dropmore) papers and Historical Manuscripts Commission print for a clear copy.",
    [("Cleveland Public Library", "http://cplorg.contentdm.oclc.org/cdm/ref/collection/p4014coll9/id/50900")], CK)

add(1796, "10 Jul 1796",
    "Unsigned (Cincinnati) → Robert Baldwin c/o H. H. Breckenridge, Pittsburgh: Northwest Territory letter with names in code",
    "unknown → Robert Baldwin", "Cincinnati", "English", "Americas", "1701-1800",
    "Indiana Historical Society, Northwest Territory collection (ONWT) id 1583", "names in code, with a key in another hand on the address leaf", "A",
    "Description: letter presumably intercepted by Zebulon Pike; 'names ... appear to be in code and the corresponding names are written in another's hand' on the address side. Probably already readable from the gloss.",
    "Intercepted 1796 letter on Anthony Wayne's movements; the glosses give the whole key.", 2, 5, 1,
    "View the scan and transcribe the key hand.", [("IHS image", "http://images.indianahistory.org/cdm/ref/collection/ONWT/id/1583")], CK)

add(1864, "c. 1864",
    "L. P. Milligan coded message, evidence in the 1864 Indianapolis treason trial",
    "unknown", "Indianapolis", "English", "Americas", "1801-1900",
    "Indiana State Library, p16066coll13 id 3133", "one coded message (image)", "C",
    "Description: 'A coded message used as evidence in the case of treason against Lambdin P. Milligan and other Confederate sympathizers in Indianapolis, Indiana in 1864' (Ex parte Milligan). No decipherment noted; the trial record may contain one.",
    "Famous treason trial (Ex parte Milligan); the Sons of Liberty message was presumably read for the court.", 3, 3, 2,
    "View the image; compare with the trial transcript (Pitman, Trials for Treason at Indianapolis 1865).",
    [("Indiana Memory", "http://indianamemory.contentdm.oclc.org/cdm/ref/collection/p16066coll13/id/3133")], CK)

add(1862, "29 Sep 1862", "Unknown author → Jacob Ammen, coded letter", "unknown → Jacob Ammen", "unknown", "English", "Americas", "1801-1900",
    "Henry County Historical Society (via Ball State Digital Media Repository, LSTACivWar id 2072)", "one letter", "C",
    "Title says 'Coded letter'; no description. Ammen was a Union brigadier general in Ohio and Kentucky in 1862. Not on DECODE.",
    "Union cipher letter to a general in the Kentucky campaign, likely a Stager-style cipher.", 2, 3, 2,
    "View the scan; try the Stager/Huntington Civil War cipher families.",
    [("Ball State DMR", "http://dmr.bsu.edu/cdm/ref/collection/LSTACivWar/id/2072")], CK)

add(1862, "16 Aug 1862",
    "Fitz-John Porter (Falmouth) → G. B. McClellan, letter in code with arithmetic in another hand",
    "F. J. Porter → George B. McClellan", "Falmouth VA", "English", "Americas", "1801-1900",
    "Lehigh University, I Remain: letter 1862 August 16, 6:30 pm", "one letter; calculations in a different hand at foot", "B",
    "Lehigh description: 'A letter written in code during the Civil War bearing mathematical calculations at the bottom in a different hand'; probably a Stager cipher (the 6 pm telegram is in the Official Records). No decipherment noted.",
    "Peninsula-to-Second-Bull-Run correspondence, Stager route cipher family already known from the Huntington collection.", 3, 4, 2,
    "View the scan; compare with the O.R. text of Porter's 6 pm telegram and the Stager route-cipher tables (us_huntington).",
    [("Lehigh item", "https://preserve.lehigh.edu/digital-special-collections/i-remain/letter-1862-august-16-630-pm-general-gb-mcclellan-washington")],
    "open (checked 28 Oct 2026: catalogue only)")

add(1785, "21 Dec 1784; 11 May 1785",
    "Lafayette → Washington, two letters with ciphers (21 Dec 1784 with an enclosed cipher; 11 May 1785 'ciphers but no deciphering')",
    "Lafayette → George Washington", "New York harbour (La Nymphe); Paris", "French/English", "Americas", "1701-1800",
    "Lafayette College, Marquis de Lafayette letters mdlh109 (xk81jn011) and mdlh113 (dv13zv892)", "short cipher passages", "B",
    "Catalogue: 1785 letter 'contains ciphers but no deciphering from Washington'. The Lafayette-Jay/Washington cipher is attested in the Papers of George Washington, which may print a solution. Not on DECODE; known.py shows only a different Lafayette cipher hit.",
    "Lafayette's postwar private cipher with Washington.", 2, 3, 3,
    "Check Founders Online Washington Confederation Series for these two letters and any footnoted decipherment.",
    [("1784-12-21 letter", "https://ldr.lafayette.edu/concern/images/xk81jn011"),
     ("1785-05-11 letter", "https://ldr.lafayette.edu/concern/images/dv13zv892")], CK)

add(1778, "7 Dec 1778",
    "Arthur Lee (Paris) → Henry Laurens, letter in cipher on foreign affairs",
    "Arthur Lee → Henry Laurens", "Paris", "English", "Americas", "1701-1800",
    "University of South Carolina, South Caroliniana Library, amerrevsc id 1888", "one letter", "B",
    "USC description: 'Letter in cipher and concerns foreign affairs.' The Papers of Henry Laurens (vol. 14) probably print it decoded. Lee's cipher (cf. his 1779 'cipher code for correspondence', NYPL) is the key lead.",
    "Commissioner Lee's cipher letter to the President of Congress at the height of the Lee-Deane quarrel.", 3, 3, 2,
    "Check Papers of Henry Laurens vol. 14 and Founders Online; view the NYPL 1779 cipher code (items 37d37320-0e21-0134-db03-00505686d14e).",
    [("USC item", "http://digital.tcl.sc.edu/cdm/ref/collection/amerrevsc/id/1888"),
     ("NYPL Lee cipher code 1779", "https://digitalcollections.nypl.org/items/37d37320-0e21-0134-db03-00505686d14e")], CK)

add(1903, "16 Feb 1903; 8 Apr 1904",
    "John Hay ↔ Henry White: cipher telegrams of 12 Feb 1903 (Tower, Berlin) and 8 Apr 1904",
    "Charlemagne Tower → John Hay → Henry White; Hay → White", "Washington / Berlin / London", "English", "Americas", "1901-1950",
    "Hampton National Historic Site (NPS), Hay-White papers, collections.digitalmaryland.org hawp id 170 and 216", "3-page cipher telegram attached; one cipher reply", "B",
    "Descriptions: the 12 Feb 1903 telegram 'received in cipher' from Tower is attached (Venezuela blockade), and Hay's 8 Apr 1904 reply 'sent in cipher'. State Department code of the period; FRUS 1903 prints the text, so the pairing gives a plaintext crib.",
    "A crib pair for the US State Department cipher of 1903-04 (Venezuela claims; Washington post office lease).", 2, 4, 2,
    "View both PDFs; match against FRUS 1903 (Venezuela) text of Tower's telegram.",
    [("Hay to White 16 Feb 1903", "http://collections.digitalmaryland.org/cdm/ref/collection/hawp/id/170"),
     ("Hay to White 8 Apr 1904", "http://collections.digitalmaryland.org/cdm/ref/collection/hawp/id/216")],
    "open (checked 28 Oct 2026: catalogue only; the existing catalogue row Roosevelt → Hay 27 May 1903 is a different item)")

add(1920, "1916-1924",
    "H. F. Sinclair, Zevely, Stanford, Chandler, Parham, Wahlberg: eight ciphered telegrams in a telegraphic commercial code (Teapot Dome period)",
    "Harry F. Sinclair, Edwin H. Chandler, G. T. Stanford, J. W. Zevely, N. D. Parham, A. E. Watts, M. M. Doan", "various US/France", "English (code words)",
    "Americas", "1901-1950", "Portal to Texas History / Rice University Woodson Research Center, Zevely and Sinclair papers (metapth1891647 and siblings)",
    "eight telegrams, 1916-1924, each a 'ciphered' or 'partially ciphered message expressed in telegraphic commercial code'", "C",
    "Titles and summaries only. Zevely and Sinclair figure in the Teapot Dome scandal (Zevely to Fall, 12 Mar 1923). The commercial code is probably an off-the-shelf book (Bentley's, A.B.C., Lieber's), so a book key may open them. Not on DECODE; known.py not hit.",
    "Sinclair Oil telegrams around the Teapot Dome lease; the commercial code books are online.",
    3, 3, 3, "View the telegrams; test Bentley's/ABC/Lieber's code books from Archive.org against the five-letter groups.",
    [("Sinclair to Chandler, 14 Dec 1916", "https://texashistory.unt.edu/ark:/67531/metapth1891647/")],
    "open (checked 28 Oct 2026: catalogue only)")

add(1150, "c. 1150",
    "Greek menologion/hagiographical manuscript: scribe's prayer in the bottom margin 'written in a cryptographic system'",
    "scribe → unknown", "unknown (Byzantine)", "Greek", "Other", "unknown",
    "New York Public Library, Spencer Collection, Greek manuscript (digitalcollections.nypl.org item 9205bfb0-c62b-012f-3b65-58d385a7bc34)",
    "one marginal prayer", "C",
    "NYPL record: 'A prayer by the scribe in bottom margin written in a cryptographic system', dated 1150; the incipit given is of the page text (feast of St Symeon Stylites), not of the prayer. Greek scribal cryptography is usually a simple letter substitution. No reading noted; not searched in the Greek-manuscript literature.",
    "A c. 1150 scribal cipher in a Byzantine codex, older than every cipher the project lists except those in the oldest-cipher search.",
    3, 3, 2, "View the scan (NYPL IIIF); compare with known Byzantine cryptographic colophon alphabets (Bischoff, Gardthausen).",
    [("NYPL Digital Collections", "https://digitalcollections.nypl.org/items/9205bfb0-c62b-012f-3b65-58d385a7bc34")],
    "open (checked 28 Oct 2026: catalogue only; Greek palaeographic literature not searched)")

add(1550, "16th century",
    "Walters Ms. W.88, Book of Hours (Cambrai, c. 1300-10): owner's request for return written in code on fol. 1v",
    "owner → finder", "Cambrai (book); unknown (note)", "unknown", "Other", "1497-1559",
    "Walters Art Museum, Ms. W.88, fol. 1v", "a few lines in code", "C",
    "Walters description: 'A priest in the sixteenth century wrote a message in code on fol. 1v asking that the book be returned to him if lost.' Plaintext purpose is stated; language and system unknown.",
    "Tiny but certain 16th-century ownership cipher with a known plaintext meaning.", 1, 4, 2,
    "View fol. 1v on thedigitalwalters.org (W88); identify the code.",
    [("Walters Digital", "http://www.thedigitalwalters.org/Data/WaltersManuscripts/html/W88")], CK)

add(1776, "1776-1780", "Charles Herbert, Revolutionary War prisoner's journal (subject heading Cryptography)",
    "Charles Herbert (Newburyport sailor, Mill Prison)", "Plymouth / Mill Prison", "English", "Americas", "1701-1800",
    "University of Delaware Library, Charles Herbert journal (digitalcollections.udel.edu documents 302236)", "unknown amount", "C",
    "Only the subject heading 'Cryptography--History--18th century' marks it; the description is empty. Needs viewing to see whether there is cipher text.",
    "A prisoner's journal that may hold cipher passages.", 1, 2, 2, "View the journal images.",
    [("Delaware digital collections", "https://digitalcollections.udel.edu/documents/detail/302236")], CK)

add(1796, "1796-1800", "Elias Mann, Harvard student diary: the name of the woman he loved is always written in code",
    "Elias Mann", "Cambridge MA", "English", "Americas", "1701-1800", "Harvard University Archives, Diary of Elias Mann 1796-1800",
    "a single recurring name", "C", "Description: 'Mann loved a woman whose name is always written in code'. A tiny cipher; online images. Not on DECODE.",
    "Short repeated cipher word in an American college diary.", 1, 4, 1, "View the diary; read the repeated word.",
    [("Harvard Curiosity", "https://id.lib.harvard.edu/curiosity/worlds-of-change/149-990075728710203941_HUL.ARCH:10870313")], CK)

add(1720, "1720-1767", "William Parker legal daybooks: several pages filled with unidentified symbols, possibly a cipher",
    "William Parker (New Hampshire attorney)", "New Hampshire", "unknown", "Americas", "1701-1800",
    "Baker Library, Harvard Business School, William Parker legal daybooks and an account book (Hollis 990146986160203941)",
    "several pages of symbols", "C", "Description: 'several pages filled with unidentified symbols, possibly a cipher'. Online at Harvard Library Curiosity.",
    "Possibly a private symbol cipher in an 18th-century lawyer's account books.", 1, 2, 3, "View the pages; check whether the symbols are shorthand rather than cipher.",
    [("Harvard Curiosity", "https://id.lib.harvard.edu/curiosity/worlds-of-change/149-990146986160203941_HBS.BAKER.GEN:32064577-2017")], CK)

add(1800, "18th-19th century", "D. A. Buckingham's hymn book: two hymns and several signatures written in code",
    "D. A. Buckingham", "unknown", "English", "Americas", "1801-1900",
    "Winterthur Museum, Garden and Library, digitalcollections.winterthur.org documents 2310", "two hymns plus endings", "C",
    "Description: 'Two hymns are written in code, and something (a name?) is written in code at the end of some hymns.' Not on DECODE.",
    "Folk-art hymnal with a private cipher, probably a simple substitution.", 1, 4, 1, "View the pages.",
    [("Winterthur", "https://digitalcollections.winterthur.org/documents/detail/2310")], CK)

add(1849, "1849-1856", "George Augustus Elliott papers (Duke): diary with loose items on ciphers and codes",
    "George A. Elliott (British officer, India, Burma, Crimea)", "India / Crimea", "English", "Other", "1801-1900",
    "Duke University Rubenstein Library, George Augustus Elliott papers", "a few loose leaves, one 1852 pencil drawing", "C",
    "Finding aid: 'a few diary pages pertain to ciphers and codes'. Low value; needs viewing.", "Army officer's private ciphers in the Second Burmese War and Crimea.",
    1, 2, 2, "View the finding aid and loose items.",
    [("Duke finding aid", "https://idn.duke.edu/ark:/87924/r4q52nd66")], CK)

with open("candidates.json", "w", encoding="utf8") as f:
    json.dump(rows, f, ensure_ascii=False, indent=1)
print(len(rows))
