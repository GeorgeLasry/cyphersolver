"""Builds candidates.json (Swiss/Austrian/Bohemian/Hungarian sweep, 28 Oct 2026). Run: python -X utf8 build_candidates.py"""
import json, re, collections
SRC = 'Swiss-Austrian-Bohemian portals sweep'
TODAY = '28 Oct 2026'
out = []

def add(**k):
    d = dict(k)
    d.setdefault('source', SRC)
    d.setdefault('decode_ids', [])
    d.setdefault('seen', 'catalogue')
    out.append(d)

HUNG = 'https://archives.hungaricana.hu/en/lear/BecsSeg/%s/'
HSEARCH = {'label': 'Hungaricana search "sifrír*" (non-library hits)', 'href': 'https://www.hungaricana.hu/en/search/results/?query=sifr%C3%ADr*'}

# ---------- 1. HHStA Türkei I, Hungarian regests (Hungaricana) ----------
cl = json.load(open('hung_clusters.json', encoding='utf-8'))
def yrs(rs):
    ys = []
    for r in rs:
        m = re.search(r'(1[5-6]\d\d)', r['ref'].split('Konv')[-1]) or re.search(r'(1[5-6]\d\d)', r['date'])
        if m: ys.append(int(m.group(1)))
    return min(ys), max(ys)
def kts(rs):
    k = [int(m.group(1)) for r in rs for m in [re.search(r'(?:Karton|Kt\.) ?(\d+)', r['ref'])] if m]
    return min(k), max(k)
def links(rs, n=3):
    ls = []
    for r in rs[:n]:
        i = r['href'].rstrip('/').split('/')[-1]
        ls.append({'label': 'Hungaricana regest, ' + re.sub(r'^ÖStA HHStA ', '', r['ref'])[:60], 'href': HUNG % i})
    return ls + [HSEARCH]

T1 = [
 ('T1-1573-77', 'Carolus Rym, David Ungnad and the Constantinople embassy → Maximilian II / Rudolf II, ciphered despatches 1573-77',
  'Carolus Rym, David Ungnad von Sonnegg → Maximilian II and Rudolf II', 'German / Latin', '1560-1589', 3,
  'Overlaps existing catalogue row 342 (Ungnad 12 Mar 1576, key DECODE R392) and Láng 2015; the other entries are not rowed. Ungnad\'s Jan and Aug 1577 despatches were deciphered at the time (per row 342), so they serve as controls.'),
 ('T1-1578-81', 'Ungnad and Sinzendorff, then Sinzendorff and Breuner, Constantinople → Rudolf II, ciphered despatches 1578-81',
  'David Ungnad / Johann Joachim von Sinzendorff / Breuner → Rudolf II', 'German', '1560-1589', 3,
  'Overlaps existing catalogue row 343 (Sinzendorff 3-7 Sept 1578). Candidate keys already transcribed in the repo: DECODE R1384 (Breuner 1575) and R392 (Ungnad). Sinzendorff and Breuner 1581 despatches (Kt. 43-3, 44-2) were deciphered at the time per row 343.'),
 ('T1-1582-83', 'Breuner and Pezzen, Constantinople → Rudolf II, ciphered despatches 1582-83', 'Breuner / Johann Pezzen → Rudolf II', 'German', '1560-1589', 3,
  'Breuner 1583 reserved key is DECODE R1590 (status N/A in the repo queue).'),
 ('T1-1584-87', 'Eizing and Pezzen, Constantinople → Rudolf II, ciphered despatches 1584-87 (many sent in duplicate per Venice)', 'Eizing / Johann Pezzen → Rudolf II', 'German', '1560-1589', 3,
  'Many entries are duplicates sent "per Venedig"; several originals are marked "teilweise sifrír". A 1597 Pezzen item is listed in research/wikisource_commons (not this series).'),
 ('T1-1588-91', 'Dr. Johann Pezzen, Constantinople → Rudolf II, ciphered despatches 1588-91', 'Johann Pezzen → Rudolf II', 'German', '1589-1598', 3,
  'The longest run of one resident: about 60 entries with presentation dockets ("praesentatae ...") dating each despatch. One 1588 entry notes that a sibling letter (fol. 206-209) is deciphered, a built-in control.'),
 ('T1-1592-1610', 'Kreckwitz (1592-93), David Ungnad (1600) and Starzer (1610), Constantinople → Rudolf II / Matthias, ciphered despatches', 'Kreckwitz / Ungnad / Michael Starzer → Rudolf II, Matthias', 'German', '1589-1598', 3,
  'Mostly Kreckwitz, "csak sifrír" (cipher only) in 1592-93; Starzer 1610 begins a second long run (next row).'),
 ('T1-1611-20', 'Michael Starzer, Constantinople → Matthias / Hofkriegsrat, ciphered despatches 1611-20', 'Michael Starzer → Matthias, Hofkriegsrat (Mollart, Katzensteiner)', 'German', '1611-1650', 3,
  'Several entries "almost entirely cipher"; addressed to the Hofkriegsrat president Mollart. Thirty Years War outbreak period.'),
 ('T1-1621-31', 'Radibrati, Lustrier and others, Constantinople / Belgrade → Ferdinand II, ciphered despatches 1621-31', 'Alvisio Radibrati / Sebastian Lustrier / Starzer → Ferdinand II', 'German / Italian', '1611-1650', 3,
  'Lustrier is the main sender; some entries are plain "Sifrír szövegek, mindenfajta feloldás nélkül" (cipher texts without any decipherment).'),
 ('T1-1632-40', 'Johann Rudolf Schmid, Constantinople → Ferdinand II / III, ciphered despatches 1632-40', 'Johann Rudolf Schmid → Ferdinand II, Ferdinand III', 'German', '1611-1650', 3,
  'Schmid is the Habsburg resident at the Porte through the Thirty Years War; several despatches are "nagyobb részben sifrír".'),
 ('T1-1641+', 'Schmid, Greiffenklau and Czernin, Constantinople → Ferdinand III (and his replies), ciphered despatches 1643-48', 'Johann Rudolf Schmid / Alexander von Greiffenklau / Hermann Czernin ↔ Ferdinand III', 'German', '1611-1650', 3,
  'Includes Ferdinand III\'s own ciphered letters to Greiffenklau (Prague and Linz, Apr-Jun 1648) and the Czernin embassy (1644). Entries say "az egyetlen szöveges rész" etc. for partly clear pieces.'),
]
for key, title, corr, lang, per, imp, extra in T1:
    rs = cl[key]
    y0, y1 = yrs(rs); k0, k1 = kts(rs)
    add(year=(y0 + y1) // 2 if key not in ('T1-1573-77',) else 1575,
        date='%d-%d' % (y0, y1), title=title, correspondents=corr, place='Constantinople', language=lang,
        region='Central Europe', period=per,
        shelfmark='HHStA Wien, Staatenabteilungen, Türkei I, Kt. %d-%d (Konv. as listed in the Hungaricana regests)' % (k0, k1),
        folio_note='%d regest entries marked "feloldás nélkül" / "nincs feloldás" (without decipherment), originals and duplicates; each gives Kt., Konv., fol. and date; sibling "feloldva" entries exist in the same Kartons' % len(rs),
        cls='A',
        status=('Hungarian-language regests of the Vienna archive (Bécsi Magyar Levéltári Kirendeltség, on Hungaricana) list these items as ciphered "without decipherment". Not on DECODE (known.py: no hits for these envoys; DECODE has Ungnad R392 and Breuner R1384/R1590 keys only). The AIS (archivinformationssystem.at) records have no scans per earlier repo sessions (row 342/343 notes). ' + extra),
        why='Rudolfine-era Habsburg intelligence from the Porte, a body of ciphertext from one embassy and one cipher family that can be broken together, with deciphered siblings as controls.',
        importance=imp, solvability=2, difficulty=3,
        score_note='Scored from the Hungarian regest descriptions during the Oct 2026 Swiss-Austrian-Bohemian sweep (research/swiss_austrian/); not viewed',
        verify='Check images in HHStA (AIS Türkei I Kt. %d-%d: scans or an order of reproductions), cross-check Láng 2015 / Real Life Cryptology appendix; then try the DECODE keys R392 / R1384 / R1590.' % (k0, k1),
        links=links(rs),
        prior_art='open as far as checked (28 Oct 2026: Láng, Real Life Cryptology 2018, covers Hungarian-related Habsburg ciphers; a web search did not return a Pezzen/Eizing/Kreckwitz/Starzer/Lustrier/Schmid/Greiffenklau decipherment; not checked line by line in the book)')

# ---------- 2. HHStA Ungarische Akten ----------
add(year=1664, date='1664-1668, 1682', title='HHStA Ungarische Akten, Verschwörerakten VII, Fasc. 327 "Chiffres 1664-1668" and Thököly 1682: ciphered letters without decipherment',
    correspondents='Wesselényi conspiracy circle / Pressburger Kommission; Imre Thököly → István Szirmay (1682)', place='unknown', language='unknown (Hungarian/Latin/German?)',
    region='Central Europe', period='1651-1700', shelfmark='HHStA Wien, Ungarische Akten, Specialia, Verschwörerakten VII (Varia, Pressburger Kommission etc.), Fasc. 327 Konv. D, fol. 40-41, 63 and others; Thököly letter 12 Oct 1682',
    folio_note='5 regest entries ("Titkosírásban írt levél, feloldás nélkül"; Thököly 1682 "orig. sifrír, feloldás nélkül"); the same Konvolut holds the cipher keys "Schlüssel zu verschiedenen Chiffres" (central_archives key lead, HHStA Ungarische Akten 327-4)',
    cls='A', status='Hungaricana regests of the Vienna Hungarian files; the keys sit in the same Faszikel, so the ciphertexts can probably be read. Not on DECODE (no hits). The central_archives sweep listed only the keys.',
    why='Wesselényi/Zrinyi/Frangepán conspiracy correspondence of 1664-71 and Thököly\'s first Habsburg-border letters: Hungarian opposition ciphers with keys at hand.',
    importance=3, solvability=3, difficulty=2, score_note='Scored from the Hungarian regest descriptions during the Oct 2026 Swiss-Austrian-Bohemian sweep (research/swiss_austrian/); not viewed',
    verify='Open the AIS entries for Ungarische Akten 327 (look for scans), pair the ciphertexts with the keys of 327-4; read Láng 2018 ch. on the conspiracy ciphers.',
    links=[{'label': 'Hungaricana regest (Fasc. 327 Chiffres)', 'href': HUNG % '147866'}, HSEARCH], prior_art='open (checked 28 Oct 2026: Hungaricana regests only; Láng 2018 not read for these items)')
add(year=1663, date='10 Oct and 20 Nov 1663', title='Ferenc Wesselényi (palatine) → unknown, two letters mostly in cipher, Sztrecsény and Murány 1663',
    correspondents='Ferenc Wesselényi → unknown', place='Sztrecsény; Murány', language='Hungarian', region='Central Europe', period='1651-1700',
    shelfmark='HHStA Wien, Ungarische Akten, Specialia, Verschwörerakten IV (Nádasdysche Akten), Fasc. 310 Konv. A, fol. 36-37 (20 Nov) and one more',
    folio_note='2 letters, "nagyobb részt sifrír, feloldás nélkül"; sibling Nádasdy files include a key ("Titkosírás kulcsa", Fasc. 312 Konv. A) and a letter with its key (Fasc. 314 Konv. B)',
    cls='A', status='Hungarian regests (Hungaricana): original Hungarian letters of the palatine, mostly cipher, no decipherment. Not on DECODE.',
    why='The palatine\'s own letters, before the Wesselényi conspiracy broke (1664-71), in Hungarian; keys of the Nádasdy files may apply.',
    importance=4, solvability=3, difficulty=3, score_note='Scored from the Hungarian regest descriptions during the Oct 2026 Swiss-Austrian-Bohemian sweep (research/swiss_austrian/); not viewed',
    verify='AIS entries Verschwörerakten IV Fasc. 310; compare Fasc. 312/314 keys; check Láng 2018 and Hungarian edition of the Wesselényi papers (Magyar Országgyűlési Emlékek / Wesselényi-összeesküvés iratai) for printed readings.',
    links=[{'label': 'Hungaricana regest, Nádasdy files key', 'href': HUNG % '146641'}, HSEARCH], prior_art='open (checked 28 Oct 2026: regests only; possibly read by Hungarian editors, not verified)')
add(year=1670, date='29 Aug 1670', title='Fr. Nicolaus Donellan O.Aug. → Ferenc Nádasdy, Latin letter partly in cipher, no decipherment',
    correspondents='Nicolaus Donellan → Ferenc Nádasdy', place='unknown', language='Latin', region='Central Europe', period='1651-1700',
    shelfmark='HHStA Wien, Ungarische Akten, Specialia, Verschwörerakten IV, Fasc. 313 Konv. B (1670)', folio_note='one letter, partly cipher',
    cls='A', status='Hungaricana regest ("nincs feloldása"); Nádasdy keys in neighbouring Faszikel. Not on DECODE.',
    why='Letter to the conspirator Nádasdy a year before the plot was exposed.', importance=3, solvability=3, difficulty=2,
    score_note='Scored from the Hungarian regest descriptions during the Oct 2026 Swiss-Austrian-Bohemian sweep (research/swiss_austrian/); not viewed',
    verify='AIS entry Fasc. 313; try the Fasc. 312/314 keys.', links=[{'label': 'Hungaricana search', 'href': HSEARCH['href']}], prior_art='open (checked 28 Oct 2026: regest only)')
add(year=1543, date='3 Jun 1543', title='Friar George Martinuzzi (Fráter György) → Ferdinand I, letter in secret writing, with an enclosed cipher letter to Archbishop Ferenc Frangepán',
    correspondents='György Fráter → Ferdinand I; enclosure to Ferenc Frangepán', place='Gyulafehérvár (Alba Iulia)', language='unknown', region='Central Europe', period='1497-1559',
    shelfmark='HHStA Wien, Ungarische Akten, Miscellanea, Fasc. 425', folio_note='letter plus enclosure; regest says no decipherment',
    cls='C', status='Hungaricana regest. HHStA Ungarische Akten 425-24 (central_archives key lead) is the 1528 key of King John and Łaski, a different period. Not on DECODE.',
    why='The Transylvanian regent\'s own cipher to Ferdinand during the Hungarian partition.', importance=4, solvability=2, difficulty=4,
    score_note='Scored from the Hungarian regest description during the Oct 2026 Swiss-Austrian-Bohemian sweep (research/swiss_austrian/); not viewed',
    verify='AIS Ungarische Akten Miscellanea 425; Láng 2018 on Fráter György\'s ciphers.', links=[HSEARCH], prior_art='open (checked 28 Oct 2026: regest only)')
add(year=1527, date='22 Aug 1527', title='Hanns Hofmann → Lower Austrian government, German letter in cipher, key enclosed',
    correspondents='Hanns Hofmann → Niederösterreichische Regierung', place='unknown', language='German', region='Central Europe', period='1497-1559',
    shelfmark='HHStA Wien, Ungarische Akten, Allgemeine Akten, Fasc. 5 Konv. B, fol. 133/2-4 (key at 133/3)', folio_note='letter plus key enclosed; regest says "feloldás nélkül, de a kulcs mellékelve"',
    cls='A', status='Hungaricana regest; key in the same item, so a reading is a straight alignment. Not on DECODE.', why='Early Habsburg Hungarian-frontier report (1527, just after Mohács) with its key.',
    importance=2, solvability=3, difficulty=1, score_note='Scored from the Hungarian regest description during the Oct 2026 Swiss-Austrian-Bohemian sweep (research/swiss_austrian/); not viewed',
    verify='AIS Allgemeine Akten Fasc. 5; check for scans.', links=[HSEARCH], prior_art='open (checked 28 Oct 2026: regest only)')

# ---------- 3. Maffeo da Treviglio, Hungarian National Archives ----------
add(year=1490, date='30 Nov 1490', title='Maffeo da Treviglio (Milanese envoy at Buda) → Thomas Bakócz, bishop of Győr: four-page letter in cipher',
    correspondents='Maffeo da Treviglio → Tamás Bakócz, bishop of Győr', place='Buda', language='Latin (record) / probably Italian', region='Central Europe', period='15th century',
    shelfmark='Magyar Nemzeti Levéltár (MNL OL), Diplomatikai Levéltár, DL 46150 (Q 10, Magyar nemzeti múzeumi törzsanyag, ex Véghely)',
    folio_note='4 paper pages, original, pressed seal; the abstract says "Titkos írással írt"',
    cls='A', status='Hungaricana charter record (regest source: OL regeszta, Bakács). The repo already holds the Maffeo cipher: targets buda1489-maffeo (key from Somogyi, DECODE R5411 and ASMi Sforzesco 1597 nos. 107/111). This Hungarian-side letter is not in the repo (known.py: no hits for 46150).',
    why='A letter from Sforza\'s agent to a Hungarian prelate in the same cipher as the Buda reports of 1489-90 already read, so it is a fresh ciphertext for a known key, and the 15th-century date matters for the oldest-cipher list.',
    importance=3, solvability=4, difficulty=2, score_note='Scored from the Hungaricana record during the Oct 2026 Swiss-Austrian-Bohemian sweep (research/swiss_austrian/); not viewed',
    verify='Open the DL record (MNL DL online images, Hungaricana charter 228061) and test the Maffeo key; check Somogyi 2025 for this letter first.',
    links=[{'label': 'Hungaricana, DL 46150', 'href': 'https://archives.hungaricana.hu/en/charters/228061/'}], prior_art='open (checked 28 Oct 2026: Hungaricana only; Somogyi\'s Maffeo study not rechecked for DL 46150)')

# ---------- 4. Biblioteca Nacional de Portugal (via Manuscriptorium) ----------
MS = lambda pid: 'https://www.manuscriptorium.com/apps/index.php?direct=record&pid=' + pid
add(year=1618, date='18 Jan - 23 Dec 1618', title='Philip III → Ambrogio Spinola, seven letters in cipher, 1618 (Bohemian revolt, Ostend fleet, Nassau, Dutch West India company)',
    correspondents='Philip III of Spain → Ambrogio Spinola (Brussels)', place='Madrid; Aranjuez; San Lorenzo', language='Spanish', region='Spain', period='1611-1650',
    shelfmark='Biblioteca Nacional de Portugal, MSS. 41, n. 5, docs 3, 5b, 6b, 9, 16, 26, 30 (doc 6a announces a change of cipher; doc 1, 1614, comes with a contemporary decipherment)',
    folio_note='7 letters of 2 ff. each, originals with seals; catalogue says "Conteúdo cifrado, estando ausente a decifração"; a docket on the cover gives the subject',
    cls='A', status='Manuscriptorium/BNP record only (Pouze popisný záznam, no images in Manuscriptorium). Not on DECODE (no hits for Spinola other than the 1625 SP106 target).',
    why='Spanish royal instructions to the Flanders commander in the year the Thirty Years War began; doc 1 (1614) with its decipherment and doc 6a on the change of cipher give a crib and key context.',
    importance=4, solvability=3, difficulty=3, score_note='Scored from the BNP catalogue description during the Oct 2026 Swiss-Austrian-Bohemian sweep (research/swiss_austrian/); not viewed',
    verify='Find the BNP digital copies (purl.pt / BNP Digital) for MSS. 41; read Retortillo Atienza 2019 on Spinola\'s ciphers; compare with the Spanish "cifra general" tables on DECODE.',
    links=[{'label': 'Manuscriptorium, MSS. 41 n. 5 doc 3', 'href': MS('BNDPL_-BNDPL_MSS41N5DOC3_0HZCA6B-pt')}, {'label': 'Manuscriptorium, doc 9', 'href': MS('BNDPL_-BNDPL_MSS41N5DOC9_4DDR3Z5-pt')}, {'label': 'Manuscriptorium, doc 6a (change of cipher)', 'href': MS('BNDPL_-BNDPL_MSS41N5DOC6A2NRZ620-pt')}],
    prior_art='open (checked 28 Oct 2026: web search found Retortillo Atienza, Studia Historica 2019, on Spinola\'s ciphers, which may cite these; no decipherment of MSS. 41 found)')
add(year=1827, date='Apr 1827 - Dec 1830', title='Miguelist agents → António Ribeiro Saraiva, about 60 letters partly in cipher (Madrid, London, Lisbon, Paris), 1827-30',
    correspondents='Joaquim Severino Gomes, Ricardo Chá, duke of Cadaval, princess of Beira, G.B.S.M. and others → António Ribeiro Saraiva', place='Madrid; London; Lisbon; Ciudad Rodrigo', language='Portuguese / Spanish', region='Portugal', period='1801-1900',
    shelfmark='Biblioteca Nacional de Portugal, Arquivo António Ribeiro Saraiva, MSS. 99, 100, 101 (e.g. MSS. 99 n. 71, 77, 85, 89, 135, 262; MSS. 100 n. 91, 119, 175, 194, 286)',
    folio_note='each letter 1-2 ff.; catalogue says "parcialmente cifrada", "inclui uma linha em cifra" or "pedindo ... em cifra"; at least 10 are marked as partly ciphered text, others mention cipher',
    cls='C', status='Manuscriptorium/BNP catalogue records only; no key mentioned. Not on DECODE.', why='The exile network of the absolutist Miguelists during the succession struggle, with the princess of Beira writing; a nineteenth-century Portuguese/Spanish code family.',
    importance=3, solvability=2, difficulty=3, score_note='Scored from the BNP catalogue descriptions during the Oct 2026 Swiss-Austrian-Bohemian sweep (research/swiss_austrian/); not viewed',
    verify='Check BNP Digital for scans of MSS. 99-101; the Saraiva diary MSS. 169 n.1-13 also mentions cipher.',
    links=[{'label': 'Manuscriptorium, MSS. 99 n. 71', 'href': MS('BNDPL_-BNDPL_MSS_99_N_71_32L8GN8-pt')}, {'label': 'Manuscriptorium, MSS. 100 n. 175', 'href': MS('BNDPL_-BNDPL_MSS100N175__12RPDOB-pt')}],
    prior_art='open (checked 28 Oct 2026: not searched beyond the catalogue)')
add(year=1731, date='15 Nov 1731, 18 Jun 1733, 14 Dec 1734', title='José Correia de Abreu → José Maria da Fonseca e Évora, bishop of Porto: three ciphered letters on political matters (Lisbon, 1731-34)',
    correspondents='José Correia de Abreu → José Maria da Fonseca e Évora', place='Lisbon', language='Portuguese', region='Portugal', period='1701-1800',
    shelfmark='Biblioteca Nacional de Portugal, MSS. 41, n. 7, docs 46a, 66, 84 (lot of 83 letters on politics and the Mafra convent)', folio_note='3 letters of 2 ff., each with a separate sheet of topics',
    cls='C', status='BNP catalogue only; the separate "esboço com os tópicos" for 46a is a possible crib. Not on DECODE.', why='Court politics under John V reported to a bishop; plain-language topic list beside each letter.',
    importance=2, solvability=3, difficulty=3, score_note='Scored from the BNP catalogue description during the Oct 2026 Swiss-Austrian-Bohemian sweep (research/swiss_austrian/); not viewed',
    verify='Locate BNP scans; compare the topic sheet with the cipher.', links=[{'label': 'Manuscriptorium, MSS. 41 n. 7 doc 46a', 'href': MS('BNDPL_-BNDPL_MSS41N7DOC4619BPS26-pt')}], prior_art='open (checked 28 Oct 2026: not searched beyond the catalogue)')
add(year=1643, date='15 Dec 1643; 1644', title='John IV → Álvaro Pires de Castro, marquis of Cascais (ambassador in France): letter in cipher, and a ciphered copy of French instructions for Münster',
    correspondents='João IV → Álvaro Pires de Castro', place='Lisbon', language='Portuguese', region='Portugal', period='1611-1650',
    shelfmark='Biblioteca Nacional de Portugal, MSS. 14, n. 4 ("carta em linguagem cifrada") and n. 120; sibling MSS. 13, nos. 19-23 hold cipher plus deciphered text pairs (Luís Pereira de Castro, 1643)',
    folio_note='2 items; MSS. 13 n. 21 and n. 23 give ciphered and deciphered copies side by side', cls='A',
    status='BNP/Manuscriptorium catalogue only. HistoCrypt has a paper on Portuguese 1649 ciphertexts ("Prey to a Privateer"), a different set. Not on DECODE.',
    why='Portuguese Restoration diplomacy during the Westphalia talks; sibling pairs give a ready crib.', importance=3, solvability=3, difficulty=2,
    score_note='Scored from the BNP catalogue descriptions during the Oct 2026 Swiss-Austrian-Bohemian sweep (research/swiss_austrian/); not viewed',
    verify='Find BNP scans of MSS. 13-14; use MSS. 13 n. 21 pair to build the key.', links=[{'label': 'Manuscriptorium, MSS. 14 n. 4', 'href': MS('BNDPL_-BNDPL_MSS_14_N_4__30C2ICA-pt')}, {'label': 'Manuscriptorium, MSS. 13 n. 21 (pair)', 'href': MS('BNDPL_-BNDPL_MSS_13_N_21_1MS2GZC-pt')}],
    prior_art='open (checked 28 Oct 2026: catalogue only; HistoCrypt "Prey to a Privateer" concerns 1649 ciphertexts, not these)')
add(year=1643, date='1641-1645', title='Portuguese Restoration embassies: letters "em cifra" in the Nisa and Gama codices (Marquês de Nisa, Vasco Luís da Gama, Francisco de Sousa Coutinho)',
    correspondents='Marquês de Nisa / Vasco Luís da Gama / Francisco de Sousa Coutinho and correspondents', place='Paris; The Hague', language='Portuguese', region='Portugal', period='1611-1650',
    shelfmark='Biblioteca Nacional de Portugal, COD. 2665 (f. 179-180 Taquet letter), COD. 7162, COD. 7164, COD. 2666 (f. 135-136, 319-323 missing)', folio_note='scattered ciphered letters within bound diplomatic correspondence volumes',
    cls='C', status='BNP catalogue ("diversas cartas com o texto em cifra"). Unclear which have decipherments. Not on DECODE.', why='Portuguese diplomacy for recognition 1641-46; a 17th-century Portuguese cipher family.',
    importance=3, solvability=2, difficulty=3, score_note='Scored from the BNP catalogue descriptions during the Oct 2026 Swiss-Austrian-Bohemian sweep (research/swiss_austrian/); not viewed',
    verify='Locate scans; look at COD. 2665 f. 179-180 first.', links=[{'label': 'Manuscriptorium, COD. 2665', 'href': MS('BNDPL_-BNDPL_COD_2665____3I410W2-pt')}, {'label': 'Manuscriptorium, COD. 7162', 'href': MS('BNDPL_-BNDPL_COD_7162____1S9W5D6-pt')}],
    prior_art='open (checked 28 Oct 2026: catalogue only)')
add(year=1766, date='Mar-Apr 1766', title='"Motim de Madrid": narration and court news of the Esquilache riots, final parts in cipher (Portuguese envoy\'s papers)',
    correspondents='unknown (Portuguese diplomatic reports; Ayres de Sá letter of 11 Apr 1766 in the same bundle)', place='Madrid; Aranjuez', language='Portuguese / Spanish', region='Portugal', period='1701-1800',
    shelfmark='Biblioteca Nacional de Portugal, PBA. 636, f. 273-359 (cipher at f. 320 and f. 326)', folio_note='two cipher passages, "parte final cifrada"', cls='C',
    status='BNP catalogue only. Not on DECODE.', why='Eyewitness reporting of the 1766 Madrid riots by a Portuguese observer.', importance=2, solvability=2, difficulty=3,
    score_note='Scored from the BNP catalogue description during the Oct 2026 Swiss-Austrian-Bohemian sweep (research/swiss_austrian/); not viewed',
    verify='Find PBA 636 scans.', links=[{'label': 'Manuscriptorium, PBA. 636', 'href': MS('BNDPL_-BNDPL_PBA636F273351QE2L92-pt')}], prior_art='open (checked 28 Oct 2026: catalogue only)')
add(year=1742, date='1735-1742', title='Luís da Cunha (ambassador in France) and Marco António de Azevedo Coutinho: letters with ciphered passages (BNP COD. 4417, COD. 1750)',
    correspondents='Marco António de Azevedo Coutinho ↔ Luís da Cunha', place='Paris; The Hague', language='Portuguese', region='Portugal', period='1701-1800',
    shelfmark='Biblioteca Nacional de Portugal, COD. 4417 (p. 33-37 cipher), COD. 1750; COD. 4419 (Cunha Brochado) carries decipherments (f. 138-144) and is left out',
    folio_note='p. 33-37 of COD. 4417; COD. 1750 "em cifra" in several places', cls='B', status='BNP catalogue only. Neighbouring COD. 4419 and COD. 6441 hold deciphered versions, which may share the cipher. Not on DECODE.',
    why='Portuguese diplomacy at the peak of Cunha\'s career (Political Testament period).', importance=2, solvability=2, difficulty=3,
    score_note='Scored from the BNP catalogue descriptions during the Oct 2026 Swiss-Austrian-Bohemian sweep (research/swiss_austrian/); not viewed',
    verify='Check BNP scans and the Cunha letters printed in Cartas de D. Luís da Cunha.', links=[{'label': 'Manuscriptorium, COD. 4417', 'href': MS('BNDPL_-BNDPL_COD_4417____1CGQUTB-pt')}], prior_art='open (checked 28 Oct 2026: catalogue only)')

# ---------- 5. Zürich State Archives ----------
SZ = 'https://suche.staatsarchiv.djiktzh.ch/detail.aspx?ID=%s'
add(year=1515, date='21 Nov 1515', title='Francesco Turreo (agent) → Francesco de Laveno, ciphered letter from Roveredo (Eschental campaign, Domodossola)',
    correspondents='Francesco Turreo → Francesco de Laveno', place='Roveredo', language='Italian', region='Italy', period='1497-1559',
    shelfmark='Staatsarchiv Zürich, A 225.1, Nr. 182 (Urkunde, original on paper, microfilm)', folio_note='one letter; scribe Michele di Casasco (?)', cls='C',
    status='Zürich online catalogue: "Chiffriertes Schreiben", keyword Geheimschrift. Edition with a facsimile in Karl Tanner, Der Kampf ums Eschental (Zürich 1917), Beilagen pp. 649-650; whether Tanner printed a decipherment is not stated. Not on DECODE.',
    why='Milan-Swiss frontier intelligence from the Eschental war, a short Italian cipher with a published facsimile.', importance=2, solvability=3, difficulty=3,
    score_note='Scored from the Staatsarchiv Zürich description during the Oct 2026 Swiss-Austrian-Bohemian sweep (research/swiss_austrian/); not viewed',
    verify='Look at Tanner 1917 pp. 649-650 (digitised on e-rara / archive.org?) for a printed reading; if none, request the microfilm.', links=[{'label': 'Staatsarchiv Zürich A 225.1 Nr. 182', 'href': SZ % '5421134'}],
    prior_art='unclear (checked 28 Oct 2026: catalogue only; Tanner 1917 not opened)')
add(year=1633, date='1632-1635', title='Antistes Johann Jakob Breitinger and the Swedish agent Peblis: letters in Breitinger\'s secret writing, Zürich 1632-35',
    correspondents='Johann Jakob Breitinger ↔ Peblis (Swedish agent)', place='Zürich', language='German / Latin', region='Central Europe', period='1611-1650',
    shelfmark='Staatsarchiv Zürich, E II 399 (fol. 105, 128, 130, 137, 250, 287, 307, 360) and E II 400 (fol. 8, 46, 76, 103, 122, 126, 278, 287, 295, 300, 305, 312, 329, 335, 337, 348)', folio_note='about 24 folios across two volumes',
    cls='B', status='The catalogue cites Emil Usteri, "Über Chiffrierung in früherer Zeit, insbesondere Antistes Breitingers Geheimschrift im Verkehr mit dem schwedischen Agenten Peblis", Zürcher Taschenbuch 80 (1960), pp. 11-28, which analyses exactly these folios and probably gives the key. Kept only as a verify item.',
    why='Thirty Years War Swiss-Swedish contacts; a Usteri key may unlock a ready reading.', importance=2, solvability=4, difficulty=2,
    score_note='Scored from the Staatsarchiv Zürich description during the Oct 2026 Swiss-Austrian-Bohemian sweep (research/swiss_austrian/); not viewed',
    verify='Read Usteri 1960; if it prints the key and readings, drop this row.', links=[{'label': 'Staatsarchiv Zürich E II 400', 'href': SZ % '324948'}, {'label': 'Staatsarchiv Zürich E II 399', 'href': SZ % '324946'}],
    prior_art='probably analysed in print (Usteri 1960); not checked')

json.dump(out, open('candidates.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(out), 'candidates')
