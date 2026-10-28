"""Append rows to candidates.json (Clements Library sweep, Oct 2026). Idempotent on title."""
import json

FA = 'https://findingaids.lib.umich.edu/catalog/umich-wcl-'
NOTE = ('Scored from the archive description during the Oct 2026 Clements Library sweep '
        '(research/us_clements/); not viewed')


def row(**k):
    base = dict(score_note=NOTE, seen='catalogue', source='Clements Library sweep')
    base.update(k)
    return base


rows = [
    row(year=1812, date='25 Sept 1812',
        title="William Eustis (Secretary of War) → Joel Barlow, letter in code on Henry Wilson's secret arms export from Ostend",
        correspondents='William Eustis → Joel Barlow (US minister to France)', place='Washington, War Department',
        language='English', region='Americas', period='1801-1900',
        shelfmark='William L. Clements Library, War of 1812 collection, 1806-1860 (M-855), Box 2, 1812 Sept 25',
        folio_note='2 pages, LS, described as "In code"', cls='B',
        status=('Finding aid: "In code [directs Joel Barlow, an American agent abroad, to assist Henry Wilson. Wilson will '
                'secretly export arms to the United States from Ostend in Belgium]". The bracketed summary may come from a '
                'docket or a clear passage; no decipherment noted. Barlow left Paris for Vilna in Oct 1812 and died 26 Dec 1812, '
                'so the letter may never have been read. Not in the repo; not on DECODE.'),
        why=('A War Department order for covert arms purchases in Europe in the first months of the War of 1812, '
             'probably in the State Department code issued to Barlow.'),
        importance=3, solvability=3, difficulty=2,
        verify=('Request the 2-page scan; test the Barlow 1811 code, whose interlinear decipherment is at NARA M34 vol. 16 '
                'fr. 0011 (research/nara_triage_a/README.md), and the Monroe/Pinkney State Department codes; check the Eustis '
                'letter book (NARA RG 107, M6) for a clear file copy.'),
        links=[{'label': 'Clements finding aid item',
                'href': FA + 'M-855war_al_41482e41cbc610b6b9b1a32260e4d9e8a90a2576'}],
        prior_art=('open (checked 28 Oct 2026: web search Eustis/Barlow/Henry Wilson/Ostend; Founders Online Madison '
                   '1812 letters - not found)')),
    row(year=1866, date='undated [1861-1869?]',
        title='William H. Seward → a correspondent in Copenhagen, copy of a coded letter',
        correspondents='William H. Seward → unknown correspondent in Copenhagen (perhaps the US minister George H. Yeaman, 1865-70)',
        place='Washington (?)', language='English', region='Americas', period='1801-1900',
        shelfmark='William L. Clements Library, William H. Seward collection, 1840-1849 (M-368), additional items',
        folio_note='one copy of a coded letter, undated', cls='B',
        status=('Finding aid: "an undated copy of a coded letter Seward sent to a correspondent in Copenhagen, Denmark". '
                'No decipherment noted. Not in the repo (known.py Seward hits concern other items).'),
        why=("If from Seward's years as Secretary of State, it is probably on the Danish West Indies purchase negotiated "
             'in Copenhagen 1865-67.'),
        importance=3, solvability=2, difficulty=2,
        verify=("Request the scan; test the State Department 'Monroe cipher' and the 1867 Department code (NSA, "
                "\"Seward's Other Folly\"); compare FRUS 1866-68 Denmark despatches and Schmeh's 2019 Danish West Indies "
                'telegram post.'),
        links=[{'label': 'Clements finding aid', 'href': FA + 'M-368sew'},
               {'label': 'Schmeh: encrypted telegram about the sale of the Danish West Indies',
                'href': 'https://scienceblogs.de/klausis-krypto-kolumne/2019/11/15/an-encrypted-telegram-about-the-sales-of-the-danish-west-indies/'}],
        prior_art='open (checked 28 Oct 2026: web search Seward/Copenhagen cipher; FRUS hits are clear letters)'),
    row(year=1781, date='1780-1783',
        title='Intercepted letters between French diplomats and French ministers, 1780-1783 (60 items), Shelburne papers vol. 35',
        correspondents='French diplomats ↔ French ministers (Vergennes, Castries) (unknown)', place='various',
        language='French', region='France', period='1701-1800',
        shelfmark='William L. Clements Library, Shelburne papers (M-66), Colonial Affairs and the 1783 Treaty of Paris, Volume 35',
        folio_note='60 items; volume "currently unavailable" for its physical condition (digital facsimiles exist per the collection note)',
        cls='A',
        status=('Finding aid gives only the title. British intercepts of 1780-83 normally reached ministers as decipherments '
                'by the Deciphering Branch, so the volume may hold decrypts rather than ciphertext; whether cipher groups '
                'are kept is unknown. Not on DECODE; not in the repo.'),
        why=("French diplomatic traffic during the American war and the Paris peace; if cipher groups with decipherments "
             "are present they are siblings of the d'Estaing 1779 code (targets/destaing) and of the Luzerne 1781 code."),
        importance=3, solvability=1, difficulty=3,
        verify=('Ask the Clements for the digital facsimile of vol. 35; check whether items are decrypts or ciphertext; '
                'compare BL Add MS 32258-32308 for the same intercepts.'),
        links=[{'label': 'Clements finding aid component',
                'href': FA + 'M-66she_al_5a9ff6a8766b60f18b24d887ddf4e5113e48e03a'}],
        prior_art='unknown (checked 28 Oct 2026: finding aid only; volume not consultable)'),
    row(year=1767, date='1767-1768',
        title='Intercepted letters between French diplomats and French ministers, 1767-1768 (24 items), Shelburne papers vol. 35',
        correspondents='French diplomats ↔ French ministers (Choiseul, Praslin) (unknown)', place='various',
        language='French', region='France', period='1701-1800',
        shelfmark='William L. Clements Library, Shelburne papers (M-66), European and Mediterranean Politics, Volume 35',
        folio_note='24 items; volume "currently unavailable" for its physical condition', cls='A',
        status=('Finding aid gives only the title; probably Deciphering Branch decrypts sent to Shelburne as Southern '
                'Secretary. Whether ciphertext is present is unknown.'),
        why="French diplomatic intercepts from Shelburne's Southern Department; value depends on cipher groups being present.",
        importance=2, solvability=1, difficulty=3,
        verify='As for the 1780-83 part (vol. 35 facsimile).',
        links=[{'label': 'Clements finding aid component',
                'href': FA + 'M-66she_al_d81def0fec48dc6a04347abdf8ee7b2a96e4252d'}],
        prior_art='unknown (checked 28 Oct 2026: finding aid only)'),
    row(year=1861, date='1861',
        title='Daniel Hewett, Waterbury stonecutter, pocket diary with six pages of an alphabetic substitution or transposition code',
        correspondents='Daniel Hewett (private diary)', place='Waterbury, Vermont', language='English',
        region='Americas', period='1801-1900',
        shelfmark='William L. Clements Library, Daniel Hewett diary, 1861, 1863 (M-7446.3)',
        folio_note='six pages of code in the 1861 diary', cls='C',
        status='Finding aid: "The volume also contains six pages of an alphabetic substitution or transposition code." No reading noted.',
        why='Six pages is enough to read a private substitution; small social-history value.',
        importance=1, solvability=2, difficulty=1,
        verify='Request images of the six pages.',
        links=[{'label': 'Clements finding aid', 'href': FA + 'M-7446.3hew'}],
        prior_art='open (checked 28 Oct 2026: finding aid only)'),
    row(year=1738, date='1738 (letter no. 16 of the series 27 Dec 1737 - 19 Dec 1738)',
        title='Henry Gibbs → Margaret Fitch, courtship letter no. 16 with passages in code',
        correspondents='Henry Gibbs (1709-1759) → Margaret Fitch', place='Salem, Massachusetts', language='English',
        region='Americas', period='1701-1800',
        shelfmark="William L. Clements Library, Gibbs family papers, 1635-1846 (M-2861), Henry Gibbs's copies of courtship letters, letter 16",
        folio_note="several passages in one letter (the author's retained copy)", cls='C',
        status=('Finding aid: "At several crucial junctures in letter 16, Henry resorted to the use of a code to disguise '
                'passages dealing with an apparently embarrassing encounter with a newly married friend." No decipherment noted.'),
        why='Colonial New England private cipher; short and probably simple.',
        importance=1, solvability=2, difficulty=2,
        verify="Request letter 16; the 20 clear sibling letters give the writer's vocabulary.",
        links=[{'label': 'Clements finding aid', 'href': FA + 'M-2861gib'}],
        prior_art='open (checked 28 Oct 2026: finding aid only)'),
    row(year=1825, date='1825-1826',
        title='T. C. Connor journal, references to acquaintances in a pictographic code',
        correspondents='T. C. Connor (private journal)', place='New York / Newark / Cartagena', language='English',
        region='Americas', period='1801-1900',
        shelfmark='William L. Clements Library, T. C. Connor journal, 1825-1833 (M-2494)',
        folio_note='scattered names or references in pictographic signs', cls='C',
        status="Finding aid: \"Some references to Connor's acquaintances are made in a pictographic code.\" No reading noted.",
        why='Private journal signs, probably names; minor.',
        importance=1, solvability=1, difficulty=2,
        verify='Request sample pages.',
        links=[{'label': 'Clements finding aid', 'href': FA + 'M-2494con'}],
        prior_art='open (checked 28 Oct 2026: finding aid only)'),
    row(year=1852, date='May-July 1852',
        title='John H. Tyler → Daniel H. London (Richmond fabric merchant), business letters using a code',
        correspondents='John H. Tyler → Daniel H. London', place='Richmond, Virginia (?)', language='English',
        region='Americas', period='1801-1900',
        shelfmark='William L. Clements Library, Daniel H. London papers, 1839-1910 (M-2215)',
        folio_note='letters of May-July 1852', cls='C',
        status=('Finding aid: "another correspondent, John H. Tyler, utilized a code in his letters from May-July 1852." '
                'Type of code (a few code words or a cipher) not stated.'),
        why='Merchant correspondence code; minor.',
        importance=1, solvability=1, difficulty=2,
        verify='Request the Tyler letters.',
        links=[{'label': 'Clements finding aid', 'href': FA + 'M-2215lon'}],
        prior_art='open (checked 28 Oct 2026: finding aid only)'),
    row(year=1894, date='spring-summer 1894',
        title='Coleman Blach → Rosa Blach, love letters with a code for his clients',
        correspondents='Coleman Blach → Rosa Blach', place='unknown', language='English',
        region='Americas', period='1801-1900',
        shelfmark='William L. Clements Library, Rosa Blach letters, 1894-1896 (M-4439.8)',
        folio_note='code words for named clients in several letters', cls='C',
        status='Finding aid: "using a code when discussing specific clients." No reading noted.',
        why="Trivial salesman's code; listed for completeness.",
        importance=1, solvability=1, difficulty=2,
        verify='Request images.',
        links=[{'label': 'Clements finding aid', 'href': FA + 'M-4439.8bla'}],
        prior_art='open (checked 28 Oct 2026: finding aid only)'),
    row(year=1910, date='2 Apr 1910',
        title='Sara E. Neal → Edward Brown Rogers, love letter with examples of coded text',
        correspondents='Sara E. Neal → Edward Brown Rogers', place='Russellville, Arkansas', language='English',
        region='Americas', period='1901-1950',
        shelfmark='William L. Clements Library, Sara E. Neal letters, 1910-1911 (M-3304.3), letter of 2 Apr 1910',
        folio_note='one letter', cls='C',
        status='Finding aid: "Her letter of April 2, 1910, contains examples of coded text." No reading noted.',
        why='Courtship cipher; minor.',
        importance=1, solvability=2, difficulty=1,
        verify='Request the letter image.',
        links=[{'label': 'Clements finding aid', 'href': FA + 'M-3304.3nea'}],
        prior_art='open (checked 28 Oct 2026: finding aid only)'),
    row(year=1916, date='1916',
        title='Funston, Scott, Pershing and the War Department, Punitive Expedition telegrams, some in code (some with plaintext drafts)',
        correspondents='Maj. Gen. Frederick Funston / Hugh L. Scott / John J. Pershing ↔ War Department',
        place='Fort Sam Houston / El Paso / Mexico', language='English', region='Americas', period='1901-1950',
        shelfmark='William L. Clements Library, Fitzhugh Lee papers, 1914-1927 (M-4551.2)',
        folio_note='part of 77 documents; "a number of pre-coded transmissions are accompanied by their coded versions"',
        cls='A',
        status=('Finding aid: "Some of the communications are confidential or in code. A number of pre-coded transmissions '
                'are accompanied by their coded versions." Coded items without a plaintext draft are the open part.'),
        why='US Army code traffic of the Villa expedition; the paired drafts give the code directly.',
        importance=2, solvability=2, difficulty=1,
        verify='Request the coded items; decode with the War Department Telegraph Code (1915) and the pairs in the folder.',
        links=[{'label': 'Clements finding aid', 'href': FA + 'M-4551.2lee'}],
        prior_art='open (checked 28 Oct 2026: finding aid only)'),
]

cands = json.load(open('candidates.json', encoding='utf-8'))
have = {c['title'] for c in cands}
for r in rows:
    if r['title'] not in have:
        cands.append(r)
json.dump(cands, open('candidates.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print(len(cands))
