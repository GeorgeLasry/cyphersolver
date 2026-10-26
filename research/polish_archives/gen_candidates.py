"""Build candidates.json for the Polish archives sweep (Oct 2026).

    python research/polish_archives/gen_candidates.py

Rows are written by hand from the sources named in README.md (AGAD online inventories, AGAD scan albums on
agadd2.home.net.pl, WBC/Kórnik, the DECODE dump for the Archiwum Narodowe w Krakowie records).
"""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
INV = 'https://www.agad.gov.pl/inwentarze/ZbPopiel12.xml'
ALB = 'http://agadd2.home.net.pl/metrykalia/12/album/{}/index.html'
LST = 'https://www.agad.gov.pl/inwentarze/ZbPop{}.xml'
DEC = 'https://de-crypt.org/decrypt-web/RecordsView/{}'
NOTE = 'Scored from the archive description during the Oct 2026 Polish archives sweep (research/polish_archives/); not viewed'
NOTE_IMG = ('Scored from the archive description and one scan viewed during the Oct 2026 Polish archives sweep '
            '(research/polish_archives/)')
CHK = 'checked 26 Oct 2026: web search, Zielińska & Danilczyk IH PAN edition series, known.py'

rows = []


def add(**k):
    base = dict(score_note=NOTE, seen='catalogue', source='Polish archives sweep (AGAD inventories)',
                language='unknown', place='unknown', region='Poland-Lithuania')
    base.update(k)
    order = ['year', 'date', 'title', 'correspondents', 'place', 'language', 'region', 'period', 'shelfmark',
             'folio_note', 'cls', 'status', 'why', 'importance', 'solvability', 'difficulty', 'score_note', 'verify',
             'links', 'seen', 'source', 'prior_art', 'decode_ids']
    rows.append({f: base[f] for f in order if f in base})


# ---------------------------------------------------------------- Deboli, St Petersburg -> Stanisław August
DEB_KEYS = ('Keys in the same fonds: ZbPop 444 "Cyfra polska posłana do Petersburga Deboliemu" 8 III 1783; 451 '
            '"Chiffre François Nouveau envoyé a Monsieur Deboli" 1780; 453-454 the Cabinet\'s numbered keys 1772-1795 '
            '(not seen online). ')
DEB_PRIOR = ('open as far as checked: Zielińska & Danilczyk print the Deboli correspondence only for 1780, 1781, 1782 '
             '(IH PAN, 2015-2017+); later years unedited, Rolnik 2025 says the Great Sejm reports remain in manuscript. '
             'A contemporary decipherment may survive in the King\'s cabinet copies (cf. ZbPop 320, deciphered register '
             'for 1774-77) (' + CHK + ')')
deb = [
    # sygn, year, letters, folios, scans(album id or None), seen
    ('9', 1783, '75 pieces, k. 326', None),
    ('10', 1784, '82 pieces, k. 272', None),
    ('11', 1785, '88 pieces, k. 253', None),
    ('2', 1786, '88 pieces, k. 228', None),
    ('3', 1787, '83 pieces, k. 184; also letters of Gołuchowski to one of the King\'s ministers in the same key', None),
    ('428', 1788, '111 cipher despatches, 4 Jan-26 Dec 1788', '428'),
    ('17', 1789, '109 cipher despatches, 2 Jan-Dec 1789, k. 348', '17'),
    ('4', 1790, '109 cipher despatches, 2 Jan-31 Dec 1790, k. 350; first one (2 Jan 1790, k. 2) viewed: a whole page of '
               'about 270 numeric groups, 3-4 digits with letter suffixes (a, b), no interlinear decipherment', '4'),
    ('5', 1791, '105 cipher despatches, 4 Jan-30 Dec 1791, k. 369', '5'),
    ('416', 1792, '57-80 cipher despatches of 1792 (list gives 74 items, Feb 1792 onward)', '416'),
]
for sygn, yr, fn, alb in deb:
    links = [{'label': 'AGAD inventory, Zbiór Popielów (fonds 12)', 'href': INV}]
    if alb:
        links = [{'label': f'Scans, ZbPop {sygn}', 'href': ALB.format(alb)},
                 {'label': f'Letter list with scan links, ZbPop {sygn}', 'href': LST.format(alb)}] + links
    viewed = sygn in ('4', '17')
    add(year=yr, date=str(yr),
        title=f'Antoni Augustyn Deboli → King Stanisław August, cipher despatches from St Petersburg, {yr}',
        correspondents='Antoni Augustyn Deboli (Polish envoy at St Petersburg) → Stanisław August',
        place='St Petersburg', language='Polish/French (unknown which; the clear despatches of the same days are in Polish)',
        period='1701-1800',
        shelfmark=f'AGAD Warszawa, Zbiór Popielów (zesp. 12), sygn. {sygn}',
        folio_note=fn,
        cls='B',
        status=('AGAD inventory: "Korespondencja polityczna tajna (pismo cyfrowe) ... Listy zapisane szyfrem"; no '
                'decipherment noted. ' + DEB_KEYS + 'Not on DECODE (list dump searched); not in repo (known.py Deboli, '
                'Popiel: no hits).' + (' Scans online on AGAD\'s own image server.' if alb else
                                        ' No scan album found on agadd2 for this signature; may be on szukajwarchiwach (blocked).')),
        why=('The Polish envoy\'s secret reports from Catherine II\'s court to the King' +
             (' during the Four-Year Sejm and the Russo-Turkish war' if yr >= 1788 else '') +
             '; the ciphered parts carry what he would not put in the open despatch.'),
        importance=4, solvability=4 if alb else 2, difficulty=3,
        score_note=NOTE_IMG if viewed else NOTE,
        verify=('Check the open Polish despatch of the same date (ZbPop 419/420/421/417/415) and any cabinet decipherment; '
                'try the 1780 French key (ZbPop 451) and the 1783 Polish key (ZbPop 444) if obtainable; '
                'Zielińska\'s 1780-82 volumes give plaintext for code-group calibration.'),
        links=links, seen='image' if viewed else 'catalogue',
        prior_art=DEB_PRIOR)

# ---------------------------------------------------------------- Zabłocki, Berlin
ZAB_PRIOR = 'open as far as checked: no edition of the Berlin correspondence found (' + CHK + ')'
for sygn, yrs, y, fn in [
    ('20', '1780-1781, 1783-1785', 1783, '163 pieces (1780: 31, 1781: 62, 1783: 31, 1784: 8, 1785: 31), k. 348'),
    ('19', '1782', 1782, '55 pieces, k. 140; filed among "Bilety króla do JP. Kicińskiego"'),
    ('13', '1786-1789', 1788, '161 pieces (1786: 11, 1787: 20, 1788: 39, 1789: 91), k. 387'),
    ('423', '1789', 1789, '111 cipher pieces from Berlin plus 81 (65) letters from Warsaw to Zabłocki; 192 pieces'),
    ('14', '1790-1792', 1791, '175 pieces (1790: 50, 1791: 61, 1792: 64), k. 428'),
    ('21', '1793-1794', 1793, '73 pieces, k. 327; French and cipher ("pismo francuskie i cyfrowe"), part in cipher'),
]:
    add(year=y, date=yrs,
        title=f'Bernard Zabłocki → King Stanisław August, cipher despatches from Berlin, {yrs}',
        correspondents='Bernard Zabłocki (Polish chargé at Berlin) → Stanisław August / Department of Foreign Affairs',
        place='Berlin', language='unknown (French/Polish)', period='1701-1800',
        shelfmark=f'AGAD Warszawa, Zbiór Popielów (zesp. 12), sygn. {sygn}',
        folio_note=fn, cls='B',
        status=('AGAD inventory: "Korespondencja polityczna tajna (pismo cyfrowe) przesyłana z Berlina ... Listy zapisane '
                'szyfrem"; no decipherment noted. Keys in the same fonds: ZbPop 445/452 "Chiffre François ancien avec '
                'Mr. Kwilecki ... allant a Berlin" 1772, 453-454. No scan album found on agadd2. Not on DECODE; not in repo.'),
        why='Polish reports from Frederick II\'s and Frederick William II\'s court, through the Prussian alliance of 1790 and the Second Partition.',
        importance=4, solvability=2, difficulty=3,
        verify='Find scans on szukajwarchiwach (fonds 1/12, sygn. ' + sygn + '); compare with the clear Zabłocki files ZbPop 372/373 (1790-91, with the King\'s answers).',
        links=[{'label': 'AGAD inventory, Zbiór Popielów (fonds 12)', 'href': INV}],
        prior_art=ZAB_PRIOR)

# ---------------------------------------------------------------- other Popiel units
other = [
    dict(year=1790, date='1788-1792', sygn='12',
         title='Hennig (Gdańsk) ↔ royal chancery, French letters partly in cipher, 1788-1792',
         corr='Hennig, Polish agent/resident at Gdańsk → Stanisław August\'s chancery (and replies)', place='Gdańsk',
         lang='French', fn='120 pieces in 2 folders (1788-89, 1790-92), k. 357; "Część listów zapisana szyfrem"',
         why='Danzig reports on the Prussian blockade and Baltic trade before the Second Partition (Danzig went to Prussia in 1793).',
         imp=3),
    dict(year=1792, date='1791-1794', sygn='22',
         title='A. Middleton, Polish legation secretary at The Hague → Stanisław August, letters partly in cipher, 1791-1794',
         corr='A. Middleton (secretary of the Polish legation, The Hague) → Stanisław August / foreign department', place='The Hague',
         lang='Polish, some French', fn='177 pieces, k. 433, microfilm 17824; "Część listów zapisana szyfrem"',
         why='Polish diplomacy in the Dutch Republic during the war of the First Coalition and the Kościuszko Rising.', imp=3),
    dict(year=1791, date='1791-1792', sygn='63',
         title='Prince Jabłonowski at Berlin → Stanisław August, French political letters partly in cipher, 1791-1792',
         corr='Prince (Stanisław?) Jabłonowski, Polish envoy at Berlin → Stanisław August', place='Berlin', lang='French',
         fn='123 pieces, k. 273 (k. 152 missing); "częściowo szyfrowa (pismo cyfrowe)"',
         why='The envoy\'s reports from Berlin in the year of the 3 May Constitution and the Prussian volte-face.', imp=4),
    dict(year=1790, date='1789-1792', sygn='90',
         title='Woyna at Vienna → Stanisław August, political correspondence with some cipher items, 1789-1792',
         corr='Woyna (Polish envoy at Vienna) → Stanisław August and the foreign department; replies', place='Vienna',
         lang='Polish, French', fn='book, 111 pieces, k. 462; "Kilka aktów pisanych cyframi"',
         why='Polish reports from Joseph II\'s and Leopold II\'s Vienna during the Four-Year Sejm.', imp=3),
    dict(year=1790, date='1788-1792', sygn='424',
         title='Pokubiatto, Woyna and Corticelli at Vienna ↔ Stanisław August, secret correspondence partly in cipher, 1788-1792',
         corr='X. Pokubiatto, Woyna, Corticelli (Vienna) ↔ Stanisław August / foreign department', place='Vienna',
         lang='unknown (Polish/French/Italian)', fn='316 pieces in three groups (113 + 90 + 113); "częściowo szyfrowana"',
         why='The King\'s Vienna channel (including his Italian agent) in 1788-92.', imp=3),
    dict(year=1791, date='1791', sygn='429',
         title='Polish minister plenipotentiary at Dresden → Stanisław August, cipher despatches, 1791',
         corr='Polish minister at Dresden → Stanisław August / foreign department', place='Dresden', lang='unknown',
         fn='38 pieces, microfilm 17358; "Listy zapisane szyfrem"',
         why='Reports from Dresden in 1791, when the Elector of Saxony was offered the Polish succession under the 3 May Constitution.',
         imp=4),
    dict(year=1769, date='1765, 1769-1770', sygn='84',
         title='Political correspondence from St Petersburg to Ogrodzki, 1765 and 1769-1770, part in cipher, with the key',
         corr='Polish correspondents at St Petersburg → Jacek Ogrodzki (the King\'s secretary)', place='St Petersburg',
         lang='Polish, French', fn='bound 1765 volume k. 1-198 with the cipher key and an explanation of each figure at the end; unbound 1769-70 k. 199-596',
         why='Early Stanisław August diplomacy in Russia (election aftermath, Repnin, the Bar Confederation years).',
         imp=4, cls='A',
         status_extra=' The 1765 volume ends with "szyfrowy klucz z wyjaśnieniem co każda cyfra oznacza" (key bound in).'),
]
for o in other:
    add(year=o['year'], date=o['date'], title=o['title'], correspondents=o['corr'], place=o['place'],
        language=o['lang'], period='1701-1800',
        shelfmark=f"AGAD Warszawa, Zbiór Popielów (zesp. 12), sygn. {o['sygn']}",
        folio_note=o['fn'], cls=o.get('cls', 'B'),
        status=('AGAD inventory says partly in cipher; no decipherment noted.' + o.get('status_extra', '') +
                ' Cabinet keys 1772-1795 in the same fonds (ZbPop 445-454). No scan album found on agadd2. Not on DECODE; not in repo.'),
        why=o['why'], importance=o['imp'], solvability=3 if o.get('cls') == 'A' else 2, difficulty=3,
        verify=f"Find scans on szukajwarchiwach (fonds 1/12, sygn. {o['sygn']}); check how much is cipher and whether interlinear decipherments exist.",
        links=[{'label': 'AGAD inventory, Zbiór Popielów (fonds 12)', 'href': INV}],
        prior_art='open as far as checked (' + CHK + '); the IH PAN "Korespondencja polityczna Stanisława Augusta" series has Vienna volumes: check their years')

# ---------------------------------------------------------------- other AGAD inventories
add(year=1782, date='1782',
    title='Letters to Ignacy Potocki left undeciphered or partly undeciphered, 1782',
    correspondents='various → Ignacy Potocki (later Grand Marshal of Lithuania)', place='unknown', language='Polish',
    period='1701-1800',
    shelfmark='AGAD Warszawa, Archiwum Publiczne Potockich (zesp. 335), sygn. 279a/480a',
    folio_note='2 pages ("akta luźne, s. 2"); part of 279a, 509 files split by sender, scanned',
    cls='C',
    status=('AGAD inventory title: "Listy różnych nierozszyfrowane, lub nierozszyfrowane częściowo" (letters of various '
            'people, not deciphered or only partly). Neighbouring 279a/480b and the sender files (e.g. d\'Aloy, Polish '
            'legation secretary at Berlin, 279a/001-002, 1782) may share the key. Scans: gallery for 279a on agadd2. '
            'Not on DECODE; not in repo.'),
    why='The archivist\'s own label says these were never deciphered; Potocki\'s 1782 correspondents were the patriotic opposition and his Berlin contacts.',
    importance=3, solvability=3, difficulty=3,
    verify='Open the 279a gallery and find 480a (near the end of the 509 files); check the d\'Aloy files for a shared key.',
    links=[{'label': 'Scans, APP 279a', 'href': 'http://agadd2.home.net.pl/metrykalia/335/sygn.%20279a/indeks.htm'},
           {'label': 'AGAD inventory, Archiwum Publiczne Potockich', 'href': 'https://www.agad.gov.pl/inwentarze/APP335.xml'}],
    prior_art='open (' + CHK + ')')

add(year=1789, date='12 Sept-30 Dec 1789',
    title='Garnysz and Małachowski (Deputation for Foreign Affairs) ↔ the Polish envoy at Dresden, partly in cipher, 1789',
    correspondents='Maciej Grzegorz Garnysz, Crown vice-chancellor, and Małachowski (?) ↔ Polish envoy at Dresden',
    place='Warsaw / Dresden', language='Polish', period='1701-1800',
    shelfmark='AGAD Warszawa, Nabytki I (zesp. 420), sygn. 125 (old Nab. Stan. 53)',
    folio_note='bound booklet, 66 pp.; "Korespondencja częściowo szyfrowana"', cls='C',
    status='AGAD inventory: correspondence partly in cipher; no decipherment noted. Probably a register/letter-book. Not on DECODE; not in repo.',
    why='The Four-Year Sejm\'s foreign deputation corresponding with Dresden about the Saxon succession project.',
    importance=3, solvability=2, difficulty=3,
    verify='Find scans on szukajwarchiwach (1/420/125); a letter-book may hold the clear outgoing text beside the cipher.',
    links=[{'label': 'AGAD inventory, Nabytki I', 'href': 'https://www.agad.gov.pl/inwentarze/NabytkI420.xml'}],
    prior_art='open (' + CHK + ')')

add(year=1728, date='25 Dec 1728',
    title='Emperor Charles VI → Franz Wilhelm Kinner, secretary of the imperial legation at the Polish-Saxon court, cipher letter, 1728',
    correspondents='Charles VI → Franz Wilhelm Kinner', place='Vienna', language='German', region='Central Europe',
    period='1701-1800',
    shelfmark='AGAD Warszawa, Zbiór dokumentów papierowych (zesp. 2), nr 3001 (old IV 5.4.D. Nr 58)',
    folio_note='poszyt, 6 leaves, 206 x 334 mm; catalogued as "[Szyfr]"', cls='C',
    status='AGAD calendar (c02p): "[Szyfr]. Karol VI ... do Franciszka Wilhelma Kinnera ... w sprawach politycznych", German. Scan status unknown. Not on DECODE; not in repo.',
    why='An imperial instruction to the Vienna legation at Augustus II\'s court in 1728 (Polish succession and Saxon alliance diplomacy).',
    importance=3, solvability=2, difficulty=3,
    verify='Check scans (szukajwarchiwach, 1/2/0/3001); Austrian keys of the period are on DECODE (Windischgrätz 1720-21 targets) — try them.',
    links=[{'label': 'AGAD calendar, Zbiór dokumentów papierowych', 'href': 'https://www.agad.gov.pl/inwentarze/c02p.xml'}],
    prior_art='open (' + CHK + ')')

# ---------------------------------------------------------------- Kórnik (WBC)
add(year=1700, date='1697-1708',
    title='"List nominata Inflant": letter of the bishop-nominate of Livonia, cipher, in Szembek-era political correspondence, 1697-1708',
    correspondents='the bishop-nominate of Inflanty (unnamed) → unknown (Szembek circle)', place='unknown',
    language='Polish', period='1651-1700',
    shelfmark='PAN Biblioteka Kórnicka, BK 00401 (Mf 2441), item "List nominata Inflant"',
    folio_note='one item in a volume of originals and copies 1697-1708 (Czacki collection, arranged by Ł. Gołębiowski); described "szyfrowany"',
    cls='C',
    status='WBC record (edition 428430): correspondence on Augustus II, the Great Northern War, Dolgorukii, Mazepa, Leszczyński; "oryg., kop. ; szyfrowany". DjVu scans online, public domain. Not on DECODE; not in repo (BK 401 / nominat: no hits).',
    why='A ciphered letter from the start of the Great Northern War in Polish Livonia.',
    importance=3, solvability=3, difficulty=3,
    verify='Open the DjVu; check how much is cipher and whether BK 1560-3 "Szyfry do listów politycznych" (Szembek keys) fits.',
    links=[{'label': 'WBC edition 428430', 'href': 'https://www.wbc.poznan.pl/dlibra/publication/522120/edition/428430'}],
    source='Polish archives sweep (WBC / Biblioteka Kórnicka)',
    prior_art='open (' + CHK + ')')

# ---------------------------------------------------------------- AN Kraków records on DECODE (status N/A), not in repo
krk = [
    dict(ids=[7502, 7503, 7504, 7505, 7506, 7508, 7509, 7510, 7511], year=1662, date='21 Oct 1662 (DECODE date for all; 1662-1669)',
         title='Ludwik Wąsowicz, stolnik of Łomża → Aleksander Lubomirski, cipher letters, 1662-1669',
         corr='Ludwik Wąsowicz → Aleksander Michał Lubomirski', sm='Archiwum Narodowe w Krakowie, Archiwum Krzeszowickie Potockich (AKPot) 3227, pp. 81-268',
         fn='nine records, 1-7 pp. each (about 38 pp.); R7507 (item 7) is mentioned in targets/sieniawski1708 as a sibling only',
         cls='A', why='Letters to Aleksander Lubomirski in the years of the Lubomirski rokosz (1665-66), from a Mazovian noble.',
         imp=3, sol=4, dif=2,
         extra='DECODE R7501 (AKPot 3227 pp. 81-268 item 1) is a key record in the same file (record type key).'),
    dict(ids=[7512], year=1669, date='20 Mar 1669',
         title='Michał Kazimierz Radziwiłł, Lithuanian vice-chancellor → Aleksander Lubomirski, letter with cipher, 1669',
         corr='Michał Kazimierz Radziwiłł → Aleksander Michał Lubomirski', sm='Archiwum Narodowe w Krakowie, AKPot 3227, pp. 1191-1194',
         fn='4 pp.; DECODE cleartext Polish, cipher passages', cls='A',
         why='The Lithuanian vice-chancellor writing in the interregnum/election year 1669.', imp=3, sol=3, dif=3,
         extra='Same file as the Wąsowicz letters and key R7501.'),
    dict(ids=[7517, 7518, 7519], year=1662, date='1660s (DECODE 1600-1799)',
         title='Jan Andrzej Morsztyn → Jerzy Sebastian Lubomirski, letters with cipher',
         corr='Jan Andrzej Morsztyn → Jerzy Sebastian Lubomirski', sm='Archiwum Narodowe w Krakowie, Archiwum Sanguszków (ASang), teka 247/13',
         fn='three records, 2-4 pp.; cleartext Polish with cipher', cls='C',
         why='The poet and later Crown treasurer, a French-party courtier, writing to the Crown marshal before the rokosz.',
         imp=4, sol=3, dif=3, extra=''),
    dict(ids=[7520, 7521, 7522], year=1662, date='Aug 1662',
         title='Unknown → Jerzy Sebastian Lubomirski, cipher slips, August 1662',
         corr='unknown → Jerzy Sebastian Lubomirski', sm='Archiwum Narodowe w Krakowie, ASang teka 282/2',
         fn='three records of 1 p. each; symbols graphic + letters + numbers', cls='C',
         why='Ciphered intelligence to the Crown marshal in the year of the army confederation.', imp=3, sol=2, dif=4,
         extra=''),
    dict(ids=[7513], year=1662, date='31 Jul 1662',
         title='Unknown correspondent, cipher letter, 31 July 1662 (Sanguszko archive)',
         corr='unknown → unknown', sm='Archiwum Narodowe w Krakowie, ASang teka 134/8',
         fn='2 pp.; symbols graphic + letters + numbers', cls='C',
         why='Same month as the Lubomirski cipher slips (ASang 282/2); may share a key.', imp=2, sol=2, dif=4, extra=''),
    dict(ids=[7523, 7532, 7533], year=1765, date='c. 1760-1781 (DECODE 1600-1799; Józef Paulin Sanguszko 1740-1781 writing to his mother)',
         title='Józef Paulin Sanguszko → Barbara Sanguszkowa, letters with cipher',
         corr='Józef Paulin Sanguszko → Barbara Sanguszkowa (née Dunin)', sm='Archiwum Narodowe w Krakowie, ASang teka 288/5 and 408/17',
         fn='three records, 2-3 pp.; cleartext Polish with cipher passages', cls='B',
         why='Family letters to Barbara Sanguszkowa, whose own Dunin correspondence is the potocka1714 target; may share its key family.',
         imp=2, sol=3, dif=3, extra=' Related: targets/potocka1714 (Barbara Dunin letters, same archive).'),
    dict(ids=[7531], year=1760, date='mid-18th c. (Barbara Sanguszkowa 1718-1791)',
         title='Wojciech Jakubowski (?) → Barbara Sanguszkowa, letter with cipher',
         corr='Wojciech Jakubowski (?) → Barbara Sanguszkowa', sm='Archiwum Narodowe w Krakowie, ASang teka 406/1',
         fn='4 pp.; cleartext Polish', cls='B', why='Same circle as the Sanguszko/Dunin letters.', imp=2, sol=3, dif=3,
         extra=' Related: targets/potocka1714.'),
    dict(ids=[7516], year=1760, date='mid-18th c.',
         title='Marianna Sanguszkówna → Anna Jabłonowska (?), letter with cipher',
         corr='Marianna Sanguszkówna → Anna Jabłonowska (?)', sm='Archiwum Narodowe w Krakowie, ASang teka 414/14',
         fn='4 pp.; cleartext Polish and French', cls='C', why='Private aristocratic cipher in the Sanguszko papers.',
         imp=2, sol=3, dif=3, extra=''),
    dict(ids=[7514], year=1763, date='23 Apr 1763',
         title='Unknown, cipher document, 23 April 1763 (Sanguszko archive)',
         corr='unknown → unknown', sm='Archiwum Narodowe w Krakowie, ASang teka 163/6',
         fn='4 pp.; symbols graphic + letters + numbers', cls='C',
         why='A 1763 cipher from the last year of Augustus III, in a magnate archive.', imp=2, sol=2, dif=4, extra=''),
    dict(ids=[7463, 7464, 7465], year=1700, date='undated (DECODE 1600-1799)',
         title='Unidentified cipher sheets, Sanguszko archive ASang 85/3 items 4-6',
         corr='unknown', sm='Archiwum Narodowe w Krakowie, ASang 85/3, items 4-6',
         fn='three 1-p. records; siblings R7460-R7461 in the same unit are keys (graphic signs), R7462 a further sheet',
         cls='A', why='Short ciphertexts filed with two keys; a quick match test.', imp=1, sol=3, dif=2,
         extra=' R7460/R7461 (keys) were checked against other targets in targets/potocka1714 and sieniawski1708, not against these sheets.'),
    dict(ids=[7466], year=1700, date='undated',
         title='Unidentified cipher letter, Kraków UNK 1',
         corr='unknown', sm='Archiwum Narodowe w Krakowie, unidentified (DECODE Krakow_UNK_1)',
         fn='2 pp.; letters + numbers', cls='C', why='Unplaced cipher in the Kraków DECODE upload.', imp=1, sol=2, dif=3, extra=''),
]
for k in krk:
    add(year=k['year'], date=k['date'], title=k['title'], correspondents=k['corr'], place='unknown',
        language='Polish (cleartext)' if 'Polish' in k['fn'] or k['ids'][0] in (7512,) else 'unknown',
        period='1651-1700' if k['year'] < 1701 else '1701-1800',
        shelfmark=k['sm'], folio_note=k['fn'], cls=k['cls'],
        status=('DECODE ' + ', '.join(f'R{i}' for i in k['ids']) + ' (status N/A, cipher type unknown, private ciphertext, '
                'uploaded by the Archiwum Narodowe w Krakowie 2023; no key or decryption file on the records).' + k['extra'] +
                ' Not in repo (known.py on each R-number: no hits).'),
        why=k['why'], importance=k['imp'], solvability=k['sol'], difficulty=k['dif'],
        score_note='Scored from the DECODE metadata dump (research/catalogue_harvest/decode) during the Oct 2026 Polish archives sweep (research/polish_archives/); not viewed',
        verify='Log in to DECODE and open the images; for AKPot 3227 try key R7501 first.' if k['ids'][0] in range(7502, 7513)
        else 'Log in to DECODE and open the images; check sibling keys in the same teka.',
        links=[{'label': f'DECODE R{i}', 'href': DEC.format(i)} for i in k['ids'][:4]],
        source='Polish archives sweep (DECODE, Archiwum Narodowe w Krakowie)',
        prior_art='open (checked 26 Oct 2026: known.py, web search for Wąsowicz/Lubomirski cipher: nothing)',
        decode_ids=k['ids'])

with open(os.path.join(HERE, 'candidates.json'), 'w', encoding='utf-8') as fh:
    json.dump(rows, fh, ensure_ascii=False, indent=1)
print(len(rows), 'rows')
