import json
SRC = "US societies finding-aid sweep"
NOTE = "Scored from the finding-aid description during the Oct 2026 US societies sweep (research/us_societies/); not viewed"
PA = "open (checked 28 Oct 2026: known.py, web search of the finding aid; no decipherment found)"


def row(**k):
    d = dict(cls="C", seen="catalogue", source=SRC, score_note=NOTE, prior_art=PA, language="English", place="unknown",
             correspondents="unknown", folio_note="", verify="Open the finding aid and request or view the item.")
    d.update(k)
    return d


def L(label, href):
    return {"label": label, "href": href}


H = "https://hollisarchives.lib.harvard.edu/catalog/"
MHS = "https://www.masshist.org/collection-guides/view/"
R = []
R.append(row(year=1712, date="1711-1714 (79 letters)",
 title="Torcy to abbé Gaultier (London), Utrecht peace negotiations: 79 letters, most wholly or partly in cipher, with original keys in the collection",
 correspondents="Jean-Baptiste Colbert, marquis de Torcy -> abbé François Gaultier", place="Versailles -> London", language="French",
 region="France", period="1701-1800",
 shelfmark="University of Pennsylvania, Kislak Center, Ms. Coll. 579 (Colbert correspondence with the abbé Gaultier), 2 boxes, 169 items",
 folio_note="88 Torcy letters, 79 to Gaultier; 'most are entirely or partially in cipher'; original coding/decoding keys in the collection", cls="B",
 status="Finding aid (A. Matytsin 2006) says keys for coding and decoding are present; no decipherment or transcription noted. Not in repo, Cryptoole or DECODE list (known.py: Gaultier no hits; Torcy only other items). Not viewed; whether the keys cover the ciphertexts, and whether the letters were deciphered at the time or printed, is unchecked.",
 why="The secret Anglo-French channel behind the preliminaries of Utrecht, in a cipher whose keys survive beside the letters, so a corpus reading looks feasible.",
 importance=4, solvability=3, difficulty=2,
 verify="Open the finding aid, check digitisation (Penn Colenda), compare with the printed Torcy-Gaultier letters (Legg; Affaires etrangeres copies) and test the keys on 3 letters.",
 links=[L("Penn finding aid", "https://findingaids.library.upenn.edu/records/UPENN_RBML_PUSP.MS.COLL.579")]))
R.append(row(year=1812, date="16 Jun 1812",
 title="Department of State (Monroe) to US Minister to France (Barlow), two pages in 'undeciphered code'",
 correspondents="Department of State (James Monroe) -> Joel Barlow", place="Washington", region="Americas", period="1801-1900",
 shelfmark="Princeton University Library, Manuscripts Division, Andre De Coppet Collection (C0063), Box 26 Folder 12 (Barlow, Joel, 1812 June 16)",
 folio_note="LS, 4 pp. in total, 2 pp. in code; the collection is described item by item", cls="B",
 status="Finding aid: '2 pages in undeciphered code, the rest instructing the Minister to complain ... about the seizure and burning of several American vessels'. Not in repo (the catalogue has Eustis to Barlow 25 Sept 1812 from the Clements; this is a different letter). The Barlow/State Department code of 1811 is keyed at NARA M34 vol. 16 (research/nara_triage_a), so a key alignment may read it; the despatch may also be printed in American State Papers.",
 why="A State Department despatch to the minister in Paris on the eve of the War of 1812, in the same code as the Eustis letter, with a key at NARA.",
 importance=3, solvability=4, difficulty=2,
 verify="Check the Princeton item for digital content; compare the NARA M34 v.16 draft of 16 Jun 1812 and American State Papers.",
 links=[L("De Coppet item (EAD)", "https://findingaids.princeton.edu/catalog/C0063_c02861"), L("Collection", "https://findingaids.princeton.edu/catalog/C0063")]))
R.append(row(year=1782, date="23 Apr 1782",
 title="Letter 'largely in cipher' from Newburgh to Nathanael Greene (probably Washington), digitised",
 correspondents="probably George Washington -> Nathanael Greene", place="Newburgh, New York", region="Americas", period="1701-1800",
 shelfmark="Princeton University Library, De Coppet Collection (C0063), Box 36a Folder 37 (Greene, Nathanael, 1782 April 23)",
 folio_note="LS, 4 pp.; item has digital content", cls="B",
 status="Finding aid: 'LS, Newburgh. Largely in cipher'; no decipherment noted. Writer not named in the item description (Newburgh was Washington's headquarters in April 1782). Washington's cipher letters to Greene are usually printed with the decipherment; the Founders Online text of 23 Apr 1782 was not checked. Not in repo.",
 why="Washington's letter to the southern commander in the army's numerical cipher, with images online.",
 importance=3, solvability=4, difficulty=2,
 verify="Search Founders Online / Papers of Washington (Revolutionary War series, vol. 24) for Washington to Greene 23 Apr 1782; view the Princeton digital object.",
 links=[L("De Coppet item (EAD)", "https://findingaids.princeton.edu/catalog/C0063_c03966")]))
R.append(row(year=1691, date="29 Aug 1691",
 title="Louis XIV to Marshal Catinat, 'a secret letter, partly in cipher'",
 correspondents="Louis XIV -> Nicolas Catinat", place="Marly", language="French", region="France", period="1651-1700",
 shelfmark="Houghton Library, Harvard: Susan Dwight Bliss autograph collection, 1481-1915, item 'Louis XIV, MS. and A.L.s. to [] Catinat; Marly, 29 Aug 1691'",
 folio_note="item level; amount of cipher not stated", cls="B",
 status="HOLLIS for Archival Discovery: 'A secret letter, partly in cipher.' The repo's catalogue row 354 (Catinat 1702) cites Tomokiyo as saying the 1691 Catinat code does not fit the 1702 letter. Not in repo for this item (known.py: Catinat, Bliss autograph). Not viewed.",
 why="A king's own letter to a marshal in the Piedmont campaign, in a Louis XIV code (Catinat 1691) that Tomokiyo lists as unread.",
 importance=4, solvability=3, difficulty=4,
 verify="Open the Houghton record, check for a digitised copy, compare with the Grand Chiffre and the Catinat 1691 notes on cryptiana (louisxiv.htm).",
 prior_art="open (checked 28 Oct 2026: known.py; the unread status of the 1691 Catinat code is taken from the repo's catalogue row 354, not rechecked on cryptiana)",
 links=[L("HOLLIS for Archival Discovery", H + "hou01258_hou01258c00018")]))
R.append(row(year=1532, date="11 Jun 1532",
 title="Charles V to Lope Hurtado de Mendoza, Regensburg, partly in code",
 correspondents="Charles V -> Lope Hurtado de Mendoza", place="Regensburg (Ratisbone)", language="Spanish", region="Spain", period="1497-1559",
 shelfmark="Houghton Library, Harvard: Autograph File, K, 1717-1968, item 'Karl V, MS.L.s. to Lope Hurtado de Mendoza; Ratisbone, 11 Jun 1532'",
 cls="B",
 status="HOLLIS record: 'Partly in code.' No decipherment noted. Lope Hurtado is the recipient of the repo's 1520s items (targets/lopehurtado1522, lopehurtado1523); the 1532 imperial cipher is a later table. Not viewed.",
 why="An imperial letter during the 1532 Diet and Turkish campaign, in a cipher used with Hurtado, a sibling of the 1522-24 corpus in the repo.",
 importance=3, solvability=3, difficulty=3,
 verify="Open the Houghton record; compare Hurtado's 1532 ciphers in AGS Estado and the Charles V cipher tables (Luo 2021).",
 links=[L("HOLLIS for Archival Discovery", H + "hou01434_hou01434c00014")]))
R.append(row(year=1744, date="20 Mar 1744 and [1742?]",
 title="Chancellor A. P. Bestuzhev-Riumin, two documents written in cipher (the 1742 one also signed by M. I. Vorontsov)",
 correspondents="Aleksei Bestuzhev-Riumin (and Mikhail Vorontsov) -> unknown", place="Russia", language="unknown", region="Other", period="1701-1800",
 shelfmark="Houghton Library, Harvard: S. I. U. Vitte autograph album, 1723-1889 (Ms., 368 f.), two items under Bestuzhev-Riumin",
 status="HOLLIS: 'Written in cipher' (both items); no decipherment noted. Not in repo (known.py: Bestuzhev matches only a Central Archives row about a French consular code). Not viewed.",
 why="Elizabethan-era Russian chancery cipher signed by the chancellor; Russian diplomatic ciphers of the 1740s are almost untouched.",
 importance=3, solvability=2, difficulty=4,
 verify="Open the two Houghton records; look for digitisation of the album; check the Russian cipher literature for the Bestuzhev table.",
 links=[L("HOLLIS, 20 Mar 1744", H + "hou00671_hou00671c00023"), L("HOLLIS, 1742", H + "hou00671_hou00671c00022")]))
R.append(row(year=1837, date="9 Jan 1837",
 title="Achille Bazaine to Comte Harispe, Miranda de Ebro, letter partly in cipher (First Carlist War)",
 correspondents="Achille Bazaine -> Jean Isidore Harispe", place="Miranda de Ebro", language="French", region="Spain", period="1801-1900",
 shelfmark="Houghton Library, Harvard: E. B. Washburne autograph collection, 1766-1888, item 'Bazaine ... A.L.s. to Harispe; Miranda de Ebro, 9 Jan 1837'",
 status="HOLLIS: 'Partly in cipher.' Not viewed; the repo has Bazaine's 1866 Mexican cable but not this item.",
 why="Young Bazaine writing to the French commander of the Pyrenean army during the Carlist War.",
 importance=2, solvability=3, difficulty=3, verify="Open the Houghton record and any digital image.",
 links=[L("HOLLIS for Archival Discovery", H + "hou01549_hou01549c00007")]))
R.append(row(year=1778, date="18 Jun 1778",
 title="Lord Grantham (British ambassador in Spain) to Thomas Thynne, Marquess of Bath, duplicate, part in code",
 correspondents="Thomas Robinson, 2nd Baron Grantham -> Thomas Thynne", place="Spain", region="Spain", period="1701-1800",
 shelfmark="Houghton Library, Harvard: Autograph File, G, 1641-2009, item 'Grantham ... letter signed (duplicate) to Thomas Thynne; [Spain] 18 Jun 1778'",
 status="HOLLIS: 'Part of text in code.' Probably a Grantham family or Foreign Office code; research/tna_discovery notes Grantham to Frederick Robinson 1778-79 (Bedfordshire L 30/15/54) as a private family code, importance 1. Not viewed.",
 why="An ambassador's private cipher during the French entry into the American war; a possible sibling of the Bedfordshire Grantham letters.",
 importance=2, solvability=3, difficulty=3, verify="Open the Houghton record; compare with Bedfordshire L 30/15/54.",
 links=[L("HOLLIS for Archival Discovery", H + "hou01430_hou01430c00499")]))
R.append(row(year=1925, date="1921-1932",
 title="Georgian Social-Democratic government in exile: correspondence with the underground in Georgia, many letters and telegrams 'in cipher'",
 correspondents="Georgian Political Commissions (Paris, Constantinople, Berlin), Jordania, Kautsky and others <-> underground parties in Georgia",
 place="Paris / Constantinople / Tbilisi", language="Georgian / Russian / French", region="Other", period="1901-1950",
 shelfmark="Houghton Library, Harvard: Georgia (Republic) records [microform], 1914-1958, series 'Activity of the Georgian Government in Exile' (hou01502; dozens of folders marked 'Letters in cipher', 1921-1932)",
 folio_note="folder-level notes 'Letters in cipher', 'Cipher telegrams', 'Cipher letters' (e.g. Mdivani, Angora, Feb-Mar 1921; Constantinople Commission 1922-23)",
 status="HOLLIS folder titles only; microform; no decipherment noted. Not in repo (known.py: Georgia (Republic), Kandelaki no hits). Not viewed.",
 why="Letters between the exiled Menshevik government and the Soviet-occupied republic; the cipher would open a clandestine network.",
 importance=3, solvability=2, difficulty=4,
 verify="Open the series; check which folders carry cipher texts and whether decipherments sit beside them (the folder titles read like summaries of deciphered content).",
 links=[L("HOLLIS, example folder", H + "hou01502_hou01502c01297")]))
R.append(row(year=1940, date="1919-1976 (ledgers about 1935-1959)",
 title="John Covert's financial ledgers and day books written in a code based on his Social Security number; not yet deciphered; fully digitised",
 correspondents="John Raphael Covert (artist, 1882-1960) -> himself", place="United States", region="Americas", period="1901-1950",
 shelfmark="Philadelphia Museum of Art Archives, John Raphael Covert Papers (JRC), Financial records series; key in the 'Word and number puzzles' series",
 folio_note="all pages of the volumes digitised; about half the papers are in code", cls="B",
 status="Finding aid: 'written primarily in code. This code has not yet been deciphered'; the web-indexed finding aid says the key sits in the puzzles series. The series runs to 1959, so part falls after the 1950 limit. Not in repo, Cryptoole or DECODE list (known.py: Covert gives only Humphrey Covert 1601). Not viewed.",
 why="A named avant-garde artist's private numerical code, with images online and a key apparently supplied, so a full reading is realistic.",
 importance=2, solvability=4, difficulty=2,
 prior_art="open (checked 28 Oct 2026: web search found only the finding aid; no decipherment report)",
 verify="Open the digitised ledgers (pmalibrary.libraryhost.com) and the puzzles series with the key; test on one page.",
 links=[L("PMA finding aid", "https://pmalibrary.libraryhost.com/repositories/3/resources/287"), L("Financial records (digital object)", "https://pmalibrary.libraryhost.com/repositories/3/digital_objects/22426")]))
R.append(row(year=1912, date="1912",
 title="Archibald Johnston letterbook: about 770 ciphered or coded confidential telegrams with Charles Schwab and Eugene Grace (Bethlehem Steel, South America)",
 correspondents="Archibald Johnston <-> Charles M. Schwab, Eugene G. Grace", place="South America / Bethlehem, PA", language="English / Spanish",
 region="Americas", period="1901-1950", shelfmark="Lehigh University Special Collections, SCMS 0137 (Archibald Johnston Letterbook)",
 folio_note="55 letters and notes, c. 770 telegrams, some in code, some partial; one ledger volume",
 status="Finding aid says the telegrams are 'ciphered, coded'; likely a commercial telegraph code that a published code book would key. Not in repo (known.py: no hits). Not viewed.",
 why="Business-intelligence telegrams of Bethlehem Steel during its Latin American push; a commercial-code case for the corpus.",
 importance=2, solvability=3, difficulty=3, verify="Open the finding aid; check for digitisation; identify the code book (Bentley's, ABC 5th ed., Lieber's).",
 links=[L("PACSCL finding aid", "https://findingaids.library.upenn.edu/records/LEHIGH_SCMS0137")]))
R.append(row(year=1856, date="20 Jan 1856", title="Joel Cadbury to his brother, student letter with a passage in cipher",
 correspondents="Joel Cadbury -> his brother", region="Americas", period="1801-1900",
 shelfmark="Haverford College Quaker & Special Collections, HCS.003.125 (Joel Cadbury letter)",
 status="Finding aid: 'The letter includes text written in a cipher.' One letter; not viewed; no reading noted.",
 why="A short boarding-school cipher; a quick solve if images are online.", importance=1, solvability=4, difficulty=1,
 verify="Open the Haverford record for images.", links=[L("PACSCL finding aid", "https://findingaids.library.upenn.edu/records/HAVERFORD_HCS.003.125")]))
R.append(row(year=1864, date="Oct 1864", title="Confederate soldier Isaac L. McIntosh: letters end in code (hospital in Richmond)",
 correspondents="Isaac L. McIntosh -> Harriet R. McIntosh", place="Virginia", region="Americas", period="1801-1900",
 shelfmark="UNC Southern Historical Collection, Harriet R. McIntosh Papers, 1861-1874 (#4794), McIntosh, Isaac L., 1861-1865",
 status="UNC finding aid: 'Several of McIntosh's letters end in code.' No decoding noted; not viewed.",
 why="A soldier's private code endings in Civil War letters.", importance=1, solvability=3, difficulty=2,
 verify="Check whether the scans are online (DocSouth / UNC digital).", links=[L("UNC finding aid", "https://finding-aids.lib.unc.edu/catalog/04794")]))
R.append(row(year=1863, date="1862-1876", title="George W. Gift (Confederate naval officer): letter containing a substitution cipher devised by Gift",
 correspondents="George W. Gift -> Ellen Gift", region="Americas", period="1801-1900",
 shelfmark="UNC Southern Historical Collection, George W. Gift Papers, 1862-1876 (#1152)",
 status="UNC finding aid: 'a letter containing a substitution cipher, evidently devised by Gift'; no reading noted; not viewed. Also four letters from Canada signed O. P. Fannin.",
 why="A named officer's own substitution cipher, probably short.", importance=1, solvability=3, difficulty=1,
 verify="Open the finding aid and the folder.", links=[L("UNC finding aid", "https://finding-aids.lib.unc.edu/catalog/01152")]))
R.append(row(year=1877, date="24 Jul 1877", title="Copy of a coded message from Charles George Gordon (Gordon Pasha) about imperial business",
 correspondents="Charles George Gordon -> unknown", place="Sudan / Egypt", region="Other", period="1801-1900",
 shelfmark="UNC Southern Historical Collection, Jane Hyde Hall Liddell Battle Papers, 1693-1930 (#2769), item dated 24 July 1877",
 status="UNC component note: 'copy of a coded message from Charles George Gordon (Gordon Pasha)'; no reading noted; not viewed. Probably a telegraph code; Gordon's 1877 telegrams are in print.",
 why="Gordon as governor in the Sudan, in a copy kept by a North Carolina family.", importance=2, solvability=2, difficulty=3,
 verify="Open the folder; compare Gordon's 1877 telegrams (Gordon Papers, BL Add MS 51291 ff.).", links=[L("UNC finding aid", "https://finding-aids.lib.unc.edu/catalog/02769")]))
R.append(row(year=1757, date="1757 and Jul 1760", title="Robert Treat Paine's friend 'Lavinia': note in 'undeciphered code' and a reply in shorthand not deciphered",
 correspondents="Robert Treat Paine <-> 'Lavinia'", place="Massachusetts", region="Americas", period="1701-1800",
 shelfmark="Massachusetts Historical Society, Papers of Robert Treat Paine vol. 2 (docs RTP2d054 and RTP2d191); collection guide fa0271",
 status="MHS edition notes: 'a brief note in undeciphered code' (1757) and 'in shorthand and has not been deciphered' (1760). Tiny items.",
 why="Student flirtation ciphers; low value but short and solvable if images are online.", importance=1, solvability=2, difficulty=2,
 verify="Open the two edition pages for the transcription of the symbols.", links=[L("MHS collection guide", MHS + "fa0271")]))
R.append(row(year=1790, date="1771-1948", title="Winthrop Sargent papers: 'brief cipher notations' among the papers of the Northwest Territory secretary",
 correspondents="Winthrop Sargent", place="Northwest Territory / Massachusetts", region="Americas", period="1701-1800",
 shelfmark="Massachusetts Historical Society, Winthrop Sargent Papers, 1771-1948 (fa0261)",
 status="Collection guide: 'brief cipher notations about his ...'. Collection-level only; not viewed; no reading noted.",
 why="A territorial official's private notations.", importance=1, solvability=2, difficulty=2, verify="Open the collection guide for the folder.",
 links=[L("MHS collection guide", MHS + "fa0261")]))
R.append(row(year=1870, date="from 1869", title="Kimball-Griswold family papers: portions of the diary entries written in code",
 place="Massachusetts", region="Americas", period="1801-1900", shelfmark="Massachusetts Historical Society, Kimball-Griswold Family Papers, 1770-1945 (fa0549)",
 status="Collection guide: 'Beginning in 1869, portions of the diary entries are written in code.' Not viewed.",
 why="A private diary code; short passages.", importance=1, solvability=2, difficulty=2, verify="Open the guide and the diary volume.",
 links=[L("MHS collection guide", MHS + "fa0549")]))
R.append(row(year=1780, date="late 18th century", title="DeGrasse-Howard papers: a journal 'written in code'",
 place="Massachusetts", region="Americas", period="1701-1800", shelfmark="Massachusetts Historical Society, DeGrasse-Howard Papers, 1776-1976 (fa0153)",
 status="Collection guide: 'is written in code, and the journal also contains some transcriptions of poems and notes about medical ...'. Not viewed.",
 why="A coded journal of a physician or student.", importance=1, solvability=2, difficulty=2, verify="Open the guide for the volume.",
 links=[L("MHS collection guide", MHS + "fa0153")]))
R.append(row(year=1919, date="1919", title="Vincent E. Keegan: journal pages in code",
 correspondents="Vincent E. Keegan", region="Americas", period="1901-1950",
 shelfmark="Schlesinger Library, Harvard (sch01461, item 'Vincent E. Keegan: journal pages? (in code), 1919')",
 status="HOLLIS item title only; not viewed.", why="Coded journal pages of 1919.", importance=1, solvability=2, difficulty=2,
 verify="Open the HOLLIS record.", links=[L("HOLLIS for Archival Discovery", H + "sch01461_sch01461c0021")]))
R.append(row(year=1750, date="1720-1767", title="William Parker legal daybooks: several pages of unidentified symbols, possibly a cipher",
 correspondents="William Parker (lawyer)", region="Americas", period="1701-1800",
 shelfmark="Baker Library, Harvard Business School: William Parker legal daybooks, and an account book of an unidentified lawyer, 1720-1767 (bak00823)",
 status="Finding aid: 'several pages filled with unidentified symbols, possibly a cipher.' Not viewed.", why="Possible colonial symbol cipher in an account book.",
 importance=1, solvability=2, difficulty=3, verify="Open the HOLLIS record for digitisation.", links=[L("HOLLIS for Archival Discovery", H + "bak00823")]))

json.dump(R, open('candidates.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(R))
