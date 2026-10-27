"""Build candidates.json for the NARA bulk-scan triage, slice C (military, naval, intelligence, law enforcement).

    python research/nara_triage_c/rows.py      # rewrites candidates.json from ROWS below

Every row was checked with research/archive_sweep_2026-10/known.py (no hits) and against
research/nara_military/ and research/nara_catalog/ (catalogue entries 628-648).
"""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
CAT = 'https://catalog.archives.gov/id/'
SRC = 'NARA bulk-scan triage C sweep'
NOTE = ('Scored from the NARA catalogue description during the Oct 2026 NARA bulk-scan triage, slice C '
        '(research/nara_triage_c/); not viewed')
NOTE_OCR = ('Scored from the catalogue description and the OCR snippet of the flagged frame during the Oct 2026 '
            'NARA bulk-scan triage, slice C (research/nara_triage_c/); image not viewed')
PA = 'open (checked 27 Oct 2026: repo known.py, nara_military + nara_catalog READMEs; no published reading found)'


def link(label, naid):
    return {'label': label, 'href': CAT + str(naid)}


ROWS = []


def row(**k):
    base = dict(region='Americas', period='1901-1950', language='unknown', place='unknown', cls='C',
                seen='catalogue', source=SRC, prior_art=PA, score_note=NOTE)
    base.update(k)
    ROWS.append(base)


# ---------------------------------------------------------------- RG 457 (NSA Historic Cryptographic Collection)
row(year=1944, date='1944',
    title='GC&CS Cryptographic Co-ordination and Records section: file of "Unsolved Problems", 1944',
    correspondents='unknown (various unidentified systems; CCR, Government Code & Cipher School)',
    region='Other', language='unknown',
    shelfmark='NARA RG 457, Archival and Historian\'s Source Files, 47647A "Cryptographic Co-ordination and '
              'Records - Unsolved Problems - CCR - 1944" (naId 23891396)',
    folio_note='One file unit; size unknown; not digitised.',
    status='Catalogue title names it as a file of unsolved problems kept by the British CCR section (which logged '
           'unidentified and unread systems). Not digitised (no digital objects). Contents may be mostly machine '
           'or one-time traffic; hand systems among them unknown. Not on DECODE.',
    why='A wartime register of traffic GC&CS could not read; any hand-cipher or code items in it are, by definition, '
        'unsolved at the time.',
    importance=3, solvability=1, difficulty=4,
    verify='Order a copy from NARA College Park (RG 457, entry for Archival and Historian\'s Source Files, item '
           '47647A); list the problems and keep only hand systems before 1951.',
    links=[link('NARA catalogue file unit', 23891396)])

row(year=1937, date='18 Oct 1937', title='Messages studied (by SIS) for a hidden or code message, 1937',
    correspondents='unknown', language='unknown',
    shelfmark='NARA RG 457, Historic Cryptographic Collection, NR 4568 (ZEMA33, 9027A), "Messages Studied for '
              'Hidden or Code Message", 18 Oct 1937 (naId 2811333)',
    folio_note='Size unknown; not digitised.',
    status='Title only: messages examined for concealed text. Outcome of the study not stated. Not digitised.',
    why='A suspected concealment case referred to Friedman\'s SIS; if it was never resolved, the messages are an '
        'open problem with a known context.',
    importance=2, solvability=1, difficulty=3,
    verify='Order NR 4568 from College Park; check whether the file records a finding.',
    links=[link('NARA catalogue file unit', 2811333)])

row(year=1942, date='13 Nov 1942', title='Raphael Pino Roca → Primitivo Yella, coded message, 1942',
    correspondents='Raphael Pino Roca → Primitivo Yella', language='Spanish (probably)',
    shelfmark='NARA RG 457, Historic Cryptographic Collection, NR 4407 (ZEMA191, 5921A), "Coded Message from '
              'Raphael Pino Roca to Primitivo Yella", 13 Nov 1942 (naId 2811167)',
    folio_note='One message; not digitised.',
    status='A private coded message referred to the Army cryptanalysts in 1942 (censorship or FBI case, by its '
           'filing). Whether SIS read it is not stated. Not digitised.',
    why='A wartime suspect message between two named Spanish-speaking individuals; reading it would close a '
        'small counter-intelligence case.',
    importance=2, solvability=1, difficulty=3,
    verify='Order NR 4407; look for a worksheet or solution in the file; search the names in RG 65 / RG 216 '
           'censorship records.',
    links=[link('NARA catalogue file unit', 2811167)])

row(year=1862, date='1862-1865', period='1801-1900',
    title='American Civil War letters, messages and cipher instructions, 1862-1865 (NSA historian\'s file)',
    correspondents='unknown (Union and/or Confederate)', language='English',
    shelfmark='NARA RG 457, Archival and Historian\'s Source Files, item 9122 "American Civil War Letters, '
              'Messages, Information, Cipher Instructions, 1862-1865" (naId 23890756)',
    folio_note='Size unknown; not digitised.',
    status='Historian\'s source file; may be copies of known Union route-cipher and Confederate Vigenère material, '
           'or may include messages never read. Not digitised. Distinct from the RG 107 Eckert ledgers and the '
           'Greenhow items already catalogued.',
    why='Civil War cipher messages with keys in the same file would be a quick key alignment; unread ones would '
        'join the Greenhow/Johnston family already in the catalogue.',
    importance=3, solvability=1, difficulty=2,
    verify='Order item 9122; compare any ciphertext with the Union route books and the three Confederate keys.',
    links=[link('NARA catalogue file unit', 23890756)])

row(year=1945, date='16 Jun 1945',
    title='Code messages found in the archives of the former German Embassy, Buenos Aires (report of 1945)',
    correspondents='German Embassy Buenos Aires / German agents in Argentina → Berlin (presumed)',
    language='German (presumed)', place='Buenos Aires',
    shelfmark='NARA RG 457, Historic Cryptographic Collection, NR 2054 (CBLK11, 158A), "Information on Code '
              'Messages Found in Ex-German Embassy Archives - Argentina", 16 Jun 1945 (naId 2808583)',
    folio_note='Size unknown; not digitised.',
    status='Title says code messages were found in the seized embassy archive; whether they were read is not '
           'stated. Related: NR 1403 "German Clandestine Radio Code Messages and Axis Agents in Argentina" (1944, '
           'naId 2807843), most of which the FCC/Coast Guard read at the time. Not digitised.',
    why='Embassy-held code messages of the German network in Argentina; any not matched to a known decrypt would '
        'add to the history of the Argentine Axis networks.',
    importance=3, solvability=1, difficulty=3,
    verify='Order NR 2054 and NR 1403; check against the published Coast Guard (CGI) decrypts of the Argentine '
           'clandestine circuits.',
    links=[link('NR 2054 file unit', 2808583), link('NR 1403 file unit', 2807843)])

row(year=1917, date='7 Dec 1917', title='Cipher forwarded to MI-8 by Major Mauborgne, 1917',
    correspondents='Maj. Joseph O. Mauborgne (Signal Corps) → MI-8 (Yardley)', language='unknown',
    shelfmark='NARA RG 457, Historic Cryptographic Collection, NR 2089 (CBLK15, 8586A), "Cipher Forwarded to M18 '
              'by Major Mauborgne", 7 Dec 1917 (naId 2808618)',
    folio_note='Size unknown; not digitised.',
    status='A cipher sent to MI-8 for solution; outcome not in the title. Could be a proposed US system rather '
           'than an intercept. Not digitised.',
    why='If an intercepted message, it is a WWI item MI-8 was asked to break; if a proposed system, it is a key '
        'lead only.',
    importance=2, solvability=1, difficulty=3,
    verify='Order NR 2089; decide whether it is ciphertext or a system proposal.',
    links=[link('NARA catalogue file unit', 2808618)])

row(year=1915, date='20 Sep 1915', title='British naval officer asks the US for help in solving ciphers, 1915',
    correspondents='unknown British naval officer → US Navy/War Department', region='Other',
    language='unknown (German traffic presumed)',
    shelfmark='NARA RG 457, Historic Cryptographic Collection, NR 4841 (ZEMA59, 8149A), "British Naval Officer\'s '
              'Request for U.S. Aid in Solving Ciphers", 20 Sep 1915 (naId 2811605)',
    folio_note='Size unknown; not digitised.',
    status='A request, while the US was neutral, for help with ciphers the British had not solved. Whether '
           'specimens are enclosed is not stated. Not digitised.',
    why='Would show which WWI enemy messages the Royal Navy could not read in 1915, before Room 40 matured.',
    importance=3, solvability=1, difficulty=4,
    verify='Order NR 4841; see whether the enclosures carry ciphertext and whether it was later read.',
    links=[link('NARA catalogue file unit', 2811605)])

row(year=1944, date='1942-1945',
    title='Coded messages in German POW letters and the cipher system of German POWs in US camps, 1942-1945',
    correspondents='German prisoners of war in US camps → families/comrades', language='German',
    shelfmark='NARA RG 457, Historic Cryptographic Collection, NR 2892 (CBNK11, 3400A), "Cipher System Used by '
              'German PW\'S in U.S. Camps", 7 Apr 1945 (naId 2809479); NARA RG 38, CNSG serial files 3460/2 '
              '"Coded Messages from German POWs Letters, 1942-1944" (naId 7523906)',
    folio_note='Two files; sizes unknown; not digitised.',
    status='Censorship found coded passages in POW mail; one file describes the system (so at least part was '
           'understood), the Navy file holds the messages. Whether all were read is not stated. Not digitised.',
    why='Hand ciphers improvised in captivity; unread letters would show what prisoners tried to pass out.',
    importance=2, solvability=1, difficulty=2,
    verify='Order both files; test the messages against the system described in NR 2892.',
    links=[link('NR 2892 (RG 457)', 2809479), link('CNSG 3460/2 (RG 38)', 7523906)])

row(year=1935, date='7 May 1935', title='Peruvian coded dispatch (1935) and coded message of the commander of the '
                                         'Peruvian submarine division',
    correspondents='Peruvian government / Peruvian Navy submarine division commander', language='Spanish',
    shelfmark='NARA RG 457, Historic Cryptographic Collection, NR 1478 (CBKH37, 5944A), "Perwian [sic] Coded '
              'Dispatch", 7 May 1935 (naId 2807918); RG 457 SIGINT Operational Analysis files, 9045 "Code Message '
              'Sent by Commander of Peruvian Submarine Division" (naId 7828759, undated)',
    folio_note='Two file units; not digitised.',
    status='Intercepted Peruvian code traffic held by SIS; no solution indicated in the titles. Not digitised.',
    why='Peruvian diplomatic/naval code of the 1930s (Leticia war aftermath); small, but an unread Latin American '
        'state system.',
    importance=2, solvability=1, difficulty=3,
    verify='Order both; check RG 457 "Cryptographic Codes and Ciphers: Peru" files and the commercial code books '
           '(NR 404 Peruvian Commercial Code Book, 1912) as a possible base code.',
    links=[link('NR 1478', 2807918), link('9045', 7828759)])

row(year=1942, date='26 Dec 1942', title='Bolivian commercial cipher cable intercepted in New York, 1942',
    correspondents='unknown (Bolivian commercial sender → New York)', language='Spanish',
    shelfmark='NARA RG 457, Historic Cryptographic Collection, NR 2225 (CBLL24, 5918A), "Bolivian Commercial '
              'Cipher Cable Intercepted in New York", 26 Dec 1942 (naId 2808756)',
    folio_note='One cable (presumed); not digitised.',
    status='Cable censorship intercept; solution not stated. Not digitised.',
    why='Wartime commercial code cables were screened for smuggling and espionage; minor.',
    importance=1, solvability=1, difficulty=3,
    verify='Order NR 2225; try the standard commercial codes (ABC, Bentley, Peterson) first.',
    links=[link('NARA catalogue file unit', 2808756)])

row(year=1921, date='1921', region='Other',
    title='Russian coded messages of 1921 provided by the US High Commissioner at Constantinople',
    correspondents='Soviet or White Russian senders (unknown)', language='Russian', place='Constantinople',
    shelfmark='NARA RG 457, Archival and Historian\'s Source Files, 6707N "Russian Coded Messages, 1921 (Provided '
              'by U.S. High Commissioner Constantinople)" (naId 23890165)',
    folio_note='Size unknown; not digitised.',
    status='Messages passed by Admiral Bristol\'s office to MI-8; whether read is not stated (MI-8 worked on '
           'Soviet traffic 1920-21 with mixed success: see the RG 457 4896 Moscow-Vienna/Berlin worksheets). Not '
           'digitised.',
    why='Constantinople in 1921 was the hub of Wrangel\'s evacuated army and Soviet-Turkish contacts; unread code '
        'here is early Soviet or White diplomatic traffic.',
    importance=3, solvability=1, difficulty=4,
    verify='Order 6707N; compare with the 1920-21 Soviet systems described in TICOM 1036 and the 4896 worksheets.',
    links=[link('NARA catalogue file unit', 23890165)])

row(year=1931, date='1931-1932', region='Other',
    title='Intercepted Russian (Soviet) coded messages, 1931-1932',
    correspondents='Soviet senders (unknown)', language='Russian',
    shelfmark='NARA RG 457, Archival and Historian\'s Source Files, 6616N "Intercepted Russian Coded Messages, '
              '1931-32" (naId 23890161)',
    folio_note='Size unknown; not digitised.',
    status='SIS-era intercepts; Soviet systems of the period were mostly additive codes or one-time pads, so '
           'this may be out of hand-cipher scope. Not digitised.',
    why='Early SIS work on Soviet traffic; only worth pursuing if the file shows a hand system.',
    importance=2, solvability=1, difficulty=5,
    verify='Order 6616N; drop it if the traffic is one-time pad.',
    links=[link('NARA catalogue file unit', 23890161)])

row(year=1917, date='2 Nov 1917', title='Postal censorship and German espionage: codes and ciphers file, 1917',
    correspondents='German agents in the US and Mexico (presumed) → various', language='German / Spanish / English',
    shelfmark='NARA RG 457, Historic Cryptographic Collection, NR 4458 (ZEMA20, 4895A), "Censorship and German '
              'Espionage-Codes and Ciphers", 2 Nov 1917 (naId 2811219)',
    folio_note='Size unknown; not digitised.',
    status='MI-8 / censorship file on codes and ciphers found in suspect mail, 1917. Many such letters were read '
           '(Witzke, von Igel), so some contents will be solved. Not digitised.',
    why='A WWI censorship crypto file; any unread specimen is a German agent cipher with a known context.',
    importance=3, solvability=1, difficulty=3,
    verify='Order NR 4458; set aside items with solutions, list the rest.',
    links=[link('NARA catalogue file unit', 2811219)])

row(year=1942, date='1942', title='"Amateur sends in code to War Department", 1942',
    correspondents='unnamed amateur → War Department', language='English (presumed)',
    shelfmark='NARA RG 457, Archival and Historian\'s Source Files, 47548A "Amateur Sends in Code to War '
              'Department 1942" (naId 23891323)',
    folio_note='Size unknown; not digitised.',
    status='A civilian-submitted cryptogram (challenge or proposed system). Low historical value; listed because '
           'such submissions are sometimes unsolved. Not digitised.',
    why='Minor; only of interest if it is an unsolved challenge cipher.',
    importance=1, solvability=1, difficulty=3,
    verify='Order 47548A.',
    links=[link('NARA catalogue file unit', 23891323)])

# ---------------------------------------------------------------- RG 38 (CNO / ONI)
row(year=1935, date='1932-1941',
    title='ONI A6-3 files: coded messages sent in by civilians and the Coast Guard for analysis, 1932-1941',
    correspondents='L. K. Birinyi (1935, "alleged discovery of coded message"); US Coast Guard (1939, coded '
                   'message received, ET14); Uvan Handy (1934); E. De Forest (1941); Walter J. Sosnoski (1939) → '
                   'Office of Naval Intelligence / OP-20-G',
    language='unknown',
    shelfmark='NARA RG 38, Office of the CNO, Formerly Security Classified Administrative Correspondence, A6-3: '
              'Birinyi (naId 481141482), A6-3/ET14 Coast Guard (481141459), Handy (481141488), De Forest '
              '(481141485), Sosnoski (481141480); memos acknowledging civilian ciphers and deciphered messages '
              '1931- (481141495)',
    folio_note='Six small file units; not digitised.',
    status='Requests to the Navy to read messages held by private persons and the Coast Guard. Outcome not stated '
           'in the titles. Birinyi (Louis K. Birinyi, Hungarian-American writer) claimed a discovered coded '
           'message. Not digitised.',
    why='Each is a ciphertext someone could not read in the 1930s; the Coast Guard one may be rum-runner or '
        'smuggling traffic.',
    importance=2, solvability=1, difficulty=3,
    verify='Order the six A6-3 folders from College Park (RG 38 CNO security-classified administrative '
           'correspondence, 1927-1942).',
    links=[link('Birinyi 1935', 481141482), link('Coast Guard 1939', 481141459), link('Handy 1934', 481141488),
           link('De Forest 1941', 481141485), link('Sosnoski 1939', 481141480), link('memos 1931-', 481141495)])

# ---------------------------------------------------------------- RG 165 (War Department General Staff / MID)
row(year=1917, date='27 Aug 1917', title='The "Tampico message": Riverbank reports it cannot solve it, 1917',
    correspondents='unknown sender at Tampico (German agent traffic presumed) / Riverbank Laboratories (Fabyan, '
                   'Friedman) → War College Division / MIS',
    language='German or Spanish (presumed)', place='Tampico',
    shelfmark='NARA RG 165, War College Division general correspondence, file 10020-60 (27 Aug 1917; NARA '
              'microfilm M1024); indexed in M912 (Name Index, roll 34, frame 0947, naId 221122451)',
    folio_note='Index card entries 10020-41 to 10020-64 (July-Sept 1917): "repts. re inability to solve Tampico '
               'message" (10020-60); "fwds. monthly report of Sept. 1-17 undeciphered messages" (10020-64); '
               '"fwds two cipher code messages to be translated" (10020-61).',
    status='The M912 index card (OCR of frame 0947) shows Riverbank reporting that it could not solve a message '
           'from Tampico, and sending monthly lists of undeciphered messages. The M1024 roll for files 10018-10049 '
           '(roll 310, naIds 267255625 + 267257126) was fetched and searched: frame 0051 is a withdrawal card, '
           '"File 10020 ... Transferred to: Military Information Division", so the file is in the MID '
           'correspondence (RG 165 entry 65), which is not digitised.',
    why='Tampico was the centre of German agent activity against the Mexican oil fields in 1917; the message and '
        'the "undeciphered messages" reports are a list of what Friedman\'s first unit could not break.',
    importance=4, solvability=2, difficulty=3,
    score_note=NOTE_OCR,
    verify='Order MID file 10020 (RG 165 entry 65, MID correspondence 1917-41) from College Park, items 10020-41 to '
           '-64; check the Riverbank papers in the George C. Marshall Foundation Friedman collection for the same '
           'monthly reports.',
    links=[link('M912 index card reel (frame 0947)', 221122451),
           link('M1024 roll 310, withdrawal card frame 0051', 267255625)])

row(year=1918, date='20 May 1918',
    title='Letter in code possibly for Gustav Möller, German consul at Guaymas; MID could not decipher it, 1918',
    correspondents='unknown → Gustav Möller (German consul, Guaymas, Sonora) (presumed)', language='German '
    '(presumed)', place='Arizona / Sonora border (presumed)',
    shelfmark='NARA RG 165, MID correspondence 1917-41 (index M1194 roll 159, frame 1644, naId 118288769); MID '
              'file cited on the card as "8-II" / postal censorship',
    folio_note='Index card: "Re ltr. ... written in code which [MID] could not decipher. States it may have been '
               'intended for Gustav Moller, Ger. Consul stationed at Guaymas, Mex."',
    status='Known only from the MID name-index card (OCR). The letter itself sits in the MID case file; whether '
           'it was read later is unknown.',
    why='A German consular-network letter on the Sonora border in 1918.',
    importance=2, solvability=2, difficulty=3,
    score_note=NOTE_OCR,
    verify='Read frame 1644 of M1194 roll 159 for the full file number; locate the MID file (M1194 index → RG 165 '
           'entry 65) and order or find it digitised.',
    links=[link('M1194 index roll 159', 118288769)])

row(year=1918, date='26 Jan 1918',
    title='Message enclosed in a letter from San Luis Potosí that the postal censor could not decipher, 1918',
    correspondents='unknown writer (San Luis Potosí, Mexico) → his wife', language='Spanish (presumed)',
    place='San Luis Potosí',
    shelfmark='NARA RG 165, MID file 10632-27 (postal censor report, 26 Jan 1918); index M1194 roll 251, frame '
              '0196 (naId 118524655)',
    folio_note='Index card: "Postal Censor Rept: letr. fr. --- to his wife Jan. 26-18 enclos. message which he '
               'could not decipher" (the report concerns pro-German propaganda in El Heraldo de México).',
    status='Known from the MID index card only. File 10632 is in the MID series (not yet traced to a digitised '
           'reel).',
    why='Minor WWI Mexico censorship item.',
    importance=1, solvability=2, difficulty=3,
    score_note=NOTE_OCR,
    verify='Locate MID file 10632-27 (RG 165 entry 65); check whether the enclosure survives.',
    links=[link('M1194 index roll 251', 118524655)])

row(year=1918, date='May 1918', region='Central Europe',
    title='German agent\'s correspondence in cipher via Sweden and Switzerland (St. Gall intermediary), 1918',
    correspondents='German agent in the US → Berlin, via a Swiss intermediary at St. Gallen', language='German',
    shelfmark='NARA RG 165, MID correspondence, index M1194 roll 154, frame 0328 (naId 118276148), card dated '
              '17 May 1918',
    folio_note='Index card: "memo repts re active & authoritative Ger. agent corresp. in cypher via Sweden & '
               'Switz with Berlin; Swiss intermediary St. Gall".',
    status='Index card only; whether specimens are in the MID file and whether MI-8 read them is unknown.',
    why='A German intelligence line from the US to Berlin in 1918; if specimens exist they fall in MI-8\'s period.',
    importance=2, solvability=1, difficulty=3,
    score_note=NOTE_OCR,
    verify='Read the full card (frame 0328) for the name and file number; trace the MID file.',
    links=[link('M1194 index roll 154', 118276148)])

# ---------------------------------------------------------------- RG 65 (Bureau of Investigation, Old German Files)
row(year=1921, date='Sep 1920 - Apr 1921',
    title='Communist Party of America underground: book-cipher addresses and names in letters seized at 170 '
          'Bleecker St., New York, 1920-21',
    correspondents='District organizers and members (signing D.O. 5, J. Mortin, Frederick Mayer ...) ↔ the '
                   'Executive Secretary ("EXSEC", Paul Holt), Communist Party of America', language='English',
    place='New York and district offices (Milwaukee, Philadelphia, Sandusky, Los Angeles, Phoenix ...)',
    shelfmark='NARA RG 65, Investigative Case Files of the Bureau of Investigation 1908-1922, Old German Files '
              '(M1085) roll 940, case 202600 ("202600-1775 THRU 202600-1949-1 (4 of 4)", naId 369272950), '
              'multi-page PDFs M1085-940A, -940B, -940C ("Copies of Letters & Documents Found at 170 Bleecker St.")',
    folio_note='OCR count: 77 runs of line/letter fraction groups (e.g. "(New code) 3/3 3/4 2/8 3/7 1/14 - 7/3 '
               '2/7 4/4 ...", "Old code P 14 ... 14/15 2/1 6/4"), about 2,400 fraction tokens over the three PDFs. '
               '27 runs are followed by a Bureau "Decode:" or "the above code reads as follows" line; about 50 '
               'runs show no decode nearby. 940C also copies the party\'s own instruction for the system (count '
               'lines down, letters across on a set page; a dash between words).',
    status='Seen in the OCR of the digitised reel: Bureau agents copied the seized letters and decoded many of '
           'the coded addresses (class A: decodes in the same file give cribs for the page). The undecoded runs '
           'are names, addresses and telegraph covers. Not on DECODE; nothing in the repo.',
    why='The early US Communist underground (after the Palmer raids) hid its contact network in a book code; the '
        'undecoded runs would name more of that network, and the system is a clean example of a period book cipher.',
    importance=2, solvability=4, difficulty=2, cls='A',
    score_note=NOTE_OCR,
    verify='Open M1085-940A/B/C from the reel record, pair each decoded run with its plaintext to rebuild the key '
           'page(s) ("old code" P 14 and the "new code"), then read the runs without a decode; check the other '
           'parts of case 202600 on roll 940 for more.',
    links=[link('M1085 roll 940, case 202600 (4 of 4)', 369272950)])

# ---------------------------------------------------------------- RG 38 naval attaché registers
row(year=1917, date='unknown (c. 1913-1939)',
    title='ONI naval attaché reports filed as "Miscellaneous Code Messages" and "German/Italian Wireless '
          'Communications and Code Messages"',
    correspondents='US naval attachés → Office of Naval Intelligence (intercepted foreign messages, presumed)',
    region='Other', language='German / Italian / unknown',
    shelfmark='NARA RG 38, ONI Secret and Confidential Reports of Naval Attachés: P-10-c 23197, 23197-A, 23197&A '
              '"Miscellaneous Code Messages" (naIds 117834699, 117834700, 117840664); P-10-c 4435 and 4435-A '
              '"German Wireless Communications & Code Messages" (117834691, 117834692, 117840658; also Naval '
              'Attache Reports 196047419); P-10-c 23080 "Italian Wireless Communications & Code Messages" '
              '(117834698, 117840661)',
    folio_note='File units; sizes unknown; not digitised.',
    status='Titles only. Register numbers place 4435 early (WWI era) and 23080/23197 later (1920s-30s). Whether '
           'the messages were read is not stated. Not digitised.',
    why='Attaché-collected foreign code messages; any unread ones are interwar naval or diplomatic codes.',
    importance=2, solvability=1, difficulty=4,
    verify='Order P-10-c 4435 and 23197 from College Park; date them from the ONI register (M975 index).',
    links=[link('P-10-c 23197', 117834699), link('P-10-c 4435', 117834691), link('P-10-c 23080', 117834698)])

# ---------------------------------------------------------------- RG 393 (Army continental commands)
row(year=1867, date='1865-1868', period='1801-1900',
    title='Army cipher telegrams of the Middle Department (1865), Department of the Gulf and Fifth Military '
          'District (1866-68)',
    correspondents='Department / district commanders (Hancock, Sheridan, ...) ↔ War Department and posts',
    language='English', place='Baltimore; New Orleans',
    shelfmark='NARA RG 393, Records of U.S. Army Continental Commands: "Press Copies of Cipher Telegrams Sent", '
              'Middle Department, Jan-Jun 1865 (series naId 4486363, 0.5 in.); "Telegrams Sent in Cipher", Dept. '
              'of the Gulf / Fifth Military District, Dec 1866-Apr 1867 (5081118, 2 in.; scope note: "These '
              'records are in cipher"); "Cipher Telegrams Sent and Received", Fifth Military District, Office of '
              'Civil Affairs, Feb-Jun 1868 (5131597, 1 in.)',
    folio_note='Three small series; not digitised.',
    status='Series level only. If the volumes hold the enciphered texts without plain copies (the 5081118 scope '
           'note says they are in cipher), they are Union route-cipher telegrams of Reconstruction, readable with '
           'the War Department route books. Overlaps the nara_catalog README "Union Army cipher telegram books" '
           'note (not a row there).',
    why='Reconstruction-era military government traffic from New Orleans (Sheridan, Hancock) in cipher; '
        'probably readable with known route books, adding texts not in the War Department plain copies.',
    importance=2, solvability=2, difficulty=2, cls='B',
    verify='Order the three series; compare against the RG 107 M473 plain copies and the route books in the '
           'Eckert papers / Plum (1882).',
    links=[link('Middle Dept 1865', 4486363), link('Dept of the Gulf 1866-67', 5081118),
           link('Fifth Mil. Dist. 1868', 5131597)])


if __name__ == '__main__':
    with open(os.path.join(HERE, 'candidates.json'), 'w', encoding='utf-8') as f:
        json.dump(ROWS, f, ensure_ascii=False, indent=1)
    print(len(ROWS), 'rows')
