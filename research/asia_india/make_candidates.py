"""Write candidates.json from the hand-screened Abhilekh Patal hits (Oct 2026 sweep).

Rows are curated by hand from hits/*.jsonl and details.jsonl; this script only fills shared fields and writes JSON.
"""
import json

IT = 'https://www.abhilekh-patal.in/Category/ItemDetails/ItemDetails?itemId='
NOTE = ('Scored from the archive description during the Oct 2026 Abhilekh Patal sweep (research/asia_india/); '
        'not viewed (page images need an Abhilekh Patal login)')
SRC = 'National Archives of India, Abhilekh Patal sweep'


def period(y):
    if y < 1497: return '15th century'
    for lo, hi, p in [(1497, 1559, '1497-1559'), (1560, 1589, '1560-1589'), (1589, 1598, '1589-1598'),
                      (1598, 1610, '1598-1610'), (1611, 1650, '1611-1650'), (1651, 1700, '1651-1700'),
                      (1701, 1800, '1701-1800'), (1801, 1900, '1801-1900'), (1901, 1950, '1901-1950')]:
        if lo <= y <= hi:
            return p
    return 'unknown'


def link(label, iid):
    return {'label': label, 'href': IT + iid}


ROWS = [
    dict(year=1879, date='Mar-Nov 1879',
         title='Court of Mandalay ↔ Italian and Swiss agents (Genoa), cipher telegrams watched by the Government of India',
         correspondents='Burmese court at Mandalay (King Thibaw\'s ministers) ↔ Italian and Swiss agents; correspondent at Genoa named as Durazzo Adorno',
         place='Mandalay / Genoa', language='unknown (Italian or French likely)',
         shelfmark='NAI, Foreign Department, Secret Proceedings, Nov 1879, Nos. 233-234 (steps to decipher) and Nos. 276-278 (exchange of cipher telegrams); Foreign Dept Notes C-983 (1879)',
         folio_note='3 + 3 + 2 digitised pages (NAIDLF02188873, NAIDLF02188881 = PR_000001122390, NAIDLF03366898); whether the ciphertext is copied into the file is not stated',
         cls='C',
         status='Catalogue titles: "Steps taken to decipher certain telegrams which have passed between Italy and Mandalay" and "Exchange of Cipher Telegrams between Italy and Mandalay"; a Viceroy\'s telegram says they "probably refer to purchase of warlike material". No decipherment recorded in the titles. Not on DECODE; not in the repo (known.py, 28 Oct 2026).',
         why='Burmese arms purchases through Italy before the Third Anglo-Burmese War; a non-European court\'s own cipher traffic, rarely preserved.',
         importance=3, solvability=2, difficulty=4,
         verify='Log in to Abhilekh Patal and open the three files; check whether the telegram texts (groups) are copied and whether the Telegraph Department or Indian Office produced a decipher. Check IOR/L/PS (QDL) for the London side.',
         links=[link('Secret Progs Nov 1879 Nos. 233-34 (steps to decipher)', '9836e528-4a2d-4550-ab76-f6675b016b47'),
                link('Secret Progs Nov 1879 Nos. 276-78', 'fb011a76-d4bc-499f-8afb-92609803b27a'),
                link('Notes C-983, Viceroy telegram', 'f645db1d-0ac7-4df5-9ac3-6ccc2e7c4703')],
         prior_art='open (checked 28 Oct 2026: web search on Mandalay/Italy cipher telegrams 1879, nothing found)'),
    dict(year=1802, date='23 Jun 1802 (consultation date)',
         title='Barry Close (Resident at Poona) → Marquess Wellesley, on Jaswant Rao Holkar coming to Poona, partly in cypher',
         correspondents='Lt-Col Barry Close, Resident at Poona → Richard, Marquess Wellesley, Governor-General',
         place='Poona', language='English',
         shelfmark='NAI, Foreign Department, Secret Consultations, 23 June 1802, Nos. 90 and 91',
         folio_note='9 + 9 digitised pages (NAIDLF01002013, NAIDLF01002014); "partly in cypher code"',
         cls='B',
         status='Catalogue: "partly in cypher code"; no decipherment noted. The consultation copy may carry the Calcutta decipher interlined, which the title would not mention. Not on DECODE; not in the repo.',
         why='Resident\'s secret reporting on Holkar and the Peshwa in the months before the Treaty of Bassein; an East India Company residency cipher of 1802.',
         importance=3, solvability=3, difficulty=3,
         verify='Open the two files (login); check for an interlined decipher; compare with Martin, Despatches of the Marquess Wellesley vol. 2-3 and IOR/H/618 (Close correspondence 1802-03) for a printed or decyphered text.',
         links=[link('Secret Cons 23 Jun 1802 No. 90', '7e82bd87-84d0-406e-bccc-d121f1cab34d'),
                link('Secret Cons 23 Jun 1802 No. 91', '0eceff13-4c03-413e-a542-0fe83b99db00')],
         prior_art='open (checked 28 Oct 2026: web search, BL IOR/H/618 description does not mention cipher; Martin\'s Wellesley Despatches not grepped)'),
    dict(year=1787, date='25 Sep 1787',
         title='Persian original letter received by the Governor-General, mentioning a "secret code"',
         correspondents='unknown Indian correspondent → Governor-General (Cornwallis)',
         place='unknown', language='Persian',
         shelfmark='NAI, Foreign Department, Persian Original Letters Received, No. 483 (issued 25 September 1787)',
         folio_note='4 digitised pages (NAIDLF02169924); the English title is a garbled machine rendering that names a "secret code"',
         cls='C',
         status='Catalogue title (machine translation) speaks of "our prescription in the secret code"; auto keywords include Sultan, Secret. Whether any part is in ramz (cipher) or the phrase is figurative is unknown. Not on DECODE.',
         why='Possible Persian-language ramz in Mughal/successor-state diplomatic correspondence with the Company; very few such pieces are catalogued anywhere.',
         importance=2, solvability=2, difficulty=4,
         verify='Open the 4 pages (login) and see whether any lines are in cipher signs or numerals; check the Calendar of Persian Correspondence vol. 7 (1785-87) for No. 483.',
         links=[link('Persian Original Letters Received No. 483', '4c737020-59c6-4988-aefc-06778718752a')],
         prior_art='open (checked 28 Oct 2026: not grepped in the Calendar of Persian Correspondence)'),
    dict(year=1910, date='Aug 1910',
         title='Suspicious code and cipher telegrams between India and Europe (Telegraph Department file)',
         correspondents='private senders in India ↔ Europe (unknown); Telegraph Department and Government of India',
         place='India / Europe', language='unknown',
         shelfmark='NAI, Department of Commerce and Industry, Telegraphs A, Proceedings Nos. 25-26, August 1910',
         folio_note='7 digitised pages (NAIDLF03772670)',
         cls='C',
         status='Catalogue: "Treatment of suspicious code and cipher telegrams passing between India and Europe"; may only be a policy file. Bombay named in the keywords. Not on DECODE.',
         why='1908-10 was the peak of revolutionary activity (Savarkar, India House, Paris); intercepted suspicious cipher telegrams would be early revolutionary traffic.',
         importance=2, solvability=1, difficulty=4,
         verify='Open the file (login) and see whether specimen telegrams are copied.',
         links=[link('Telegraphs A Aug 1910 Nos. 25-26', '3b42ef68-6644-488a-be14-5aa2132471b7')],
         prior_art='open (checked 28 Oct 2026: none)'),
    dict(year=1812, date='3 Jan 1812',
         title='"Undeciphered documents" in a Home (Public) consultation, 1812',
         correspondents='unknown',
         place='Calcutta', language='English',
         shelfmark='NAI, Home Department, Public Branch, Consultation 3 January 1812, No. 86',
         folio_note='3 digitised pages (NAIDLF00330538)',
         cls='C',
         status='Catalogue title is the cataloguer\'s: "Undeciphered documents from early 19th century consultations". Most likely means illegible rather than enciphered; listed so it can be checked once. Not on DECODE.',
         why='Only of interest if it really is cipher.',
         importance=1, solvability=2, difficulty=3,
         verify='Open the 3 pages (login); drop if it is just illegible handwriting.',
         links=[link('Home Public 3 Jan 1812 No. 86', 'f5873b0c-127d-4009-8a6f-d95e4a621edc')],
         prior_art='open (not checked: description too vague)'),
]

IDS = {
    'NAIDLF00947849': '4d1f25db-9832-4666-92e7-da401bb0937a',
    'NAIDLF00943300': 'c10ba110-0f26-4558-ae6a-d898f561fb4e',
    'NAIDLF00943149': 'be64f39e-da67-462c-a7ef-600490851022',
    'NAIDLF00950238': '8b5c3969-ca78-4691-877d-3ff7f1571aee',
    'NAIDLF00945474': '086d41c6-6ca3-4ea5-9853-8e0949448df5',
    'NAIDLF00826189': 'c60c90ef-eaff-4377-9c24-2952b3f786b7',
    'NAIDLF00829027': 'fa871cdf-6f23-4c96-b155-e4ea6bb88cf3',
    'NAIDLF00824821': 'f76c2648-c819-40e5-8d8a-96f6a5ffc95b',
    'NAIDLF01546081': '976e3da1-ef09-4da1-8799-ad88389f19ac',
    'NAIDLF01946321': 'fb74b520-ae95-4225-a0e8-e933ecc0e53a',
    'NAIDLF02179604': '3505b7f4-2c51-44ce-be91-138fa181b968',
    'NAIDLF02289159': 'd1987e20-7706-4082-b782-a6df8361f039',
}

OCR = ('Found only through the portal\'s auto-extracted keywords (from the page OCR), which include "cypher"; the title '
       'does not mention cipher, so the file may only refer to a cipher rather than contain one. ')


def ocr_row(year, date, title, corr, place, shelf, ident, pages, why, imp=2, solv=2, diff=3, lang='English', kw=''):
    return dict(year=year, date=date, title=title, correspondents=corr, place=place, language=lang, shelfmark=shelf,
                folio_note=f'{pages} digitised pages ({ident}); OCR keywords: {kw}', cls='B' if lang == 'English' else 'C',
                status=OCR + 'No decipherment noted. Not on DECODE; not in the repo (known.py, 28 Oct 2026).',
                why=why, importance=imp, solvability=solv, difficulty=diff,
                verify='Open the pages (login) and see whether any passage is in cipher and whether a decipher is interlined; the 1777 Cypher Code Book (PR_000006128785) and the 1788 decyphered Sindia letter (NAIDLF00942662) are the first keys to try.',
                links=[link(shelf.split('NAI, ')[-1][:60], IDS[ident])],
                prior_art='open (checked 28 Oct 2026: catalogue only)')


ROWS += [
    dict(year=1930, date='1930',
         title='Chinese government (Nanking) → Dalai Lama at Lhasa, cypher telegrams intercepted by the Government of India',
         correspondents='Nationalist Government, Nanking (via Nanking telegraph office) → 13th Dalai Lama, Lhasa',
         place='Nanking / Lhasa', language='Chinese or Tibetan (unknown)',
         shelfmark='NAI, External Affairs Department, Sikkim (Political), file 5-P of 1930',
         folio_note='49 digitised pages (NAIDLF03824535)',
         cls='C',
         status='Catalogue: "Interception of cypher telegrams addressed to Dalai Buddha, Lhasa, from Nanking ... telegraph office". Keywords name the General Staff, Sikkim, Lhasa. Whether the British read them (Chinese telegraph code is easy; an enciphered code is not) is not stated. Not on DECODE; not in the repo.',
         why='Sino-Tibetan war of 1930-32: Nanking\'s direct traffic with the Dalai Lama, routed over the British line through Sikkim and Gyantse.',
         importance=3, solvability=2, difficulty=3,
         verify='Open the file (login): see whether the groups are copied, whether they are plain Chinese Standard Telegraph Code (then trivially read) or enciphered, and whether a General Staff decipher is attached.',
         links=[link('External Affairs, Sikkim (Political) 5-P 1930', '38d98244-cd8f-4566-8bfe-305fd6d3e03c')],
         prior_art='open (checked 28 Oct 2026: web search on 1930 Nanking-Lhasa telegrams, nothing found)'),
    dict(year=1799, date='21 Mar 1799 (consulted 8 Apr 1799)',
         title='Enclosure from the Persian Translator, eve of the Fourth Mysore War, with cypher (OCR keywords: Colonel, Vieux)',
         correspondents='unknown; forwarded by the Persian Translator (N. B. Edmonstone) to the Governor-General in Council',
         place='Calcutta / Mysore (unknown)', language='unknown (French or Persian possible)',
         shelfmark='NAI, Foreign Department, Secret Consultations, 8 April 1799, No. 29',
         folio_note='5 digitised pages (NAIDLF00947849); OCR keywords include Cypher, Colonel, Vieux',
         cls='C',
         status=OCR + 'The French word "Vieux" and the Persian Translator\'s office suggest an intercepted letter from Tipu Sultan\'s French connection; Wellesley\'s papers print a Tipu name cipher (key captured 1799) used with the Carnatic Nawabs. No decipherment noted. Not on DECODE.',
         why='If it is an intercepted Tipu or French letter in cipher, it belongs to the Seringapatam intelligence file of 1799.',
         importance=3, solvability=2, difficulty=3,
         verify='Open the 5 pages (login); compare with Martin, Despatches of the Marquess Wellesley vol. 1-2 (Tipu cypher keys, printed 1836) and the Carnatic Inquiry papers.',
         links=[link('Secret Cons 8 Apr 1799 No. 29', IDS['NAIDLF00947849'])],
         prior_art='open (checked 28 Oct 2026: Martin\'s Wellesley Despatches vol. 2 prints the Tipu/Carnatic name cipher, not this enclosure)'),
    ocr_row(1788, '12 Jul 1788 (consulted 28 Jul 1788)',
            'Enclosure in a private letter of Capt. John Kennaway (mission to Hyderabad), partly in cypher',
            'Capt. John Kennaway → Governor-General (Cornwallis), enclosing a letter (Campbell named)', 'Hyderabad',
            'NAI, Foreign Department, Secret Consultations, 28 July 1788, No. 5', 'NAIDLF00943300', 4,
            'Kennaway\'s 1788 mission to the Nizam over the Guntur Circar; the same year the Company read a residency letter "decyphered" (NAIDLF00942662).',
            imp=3, solv=2, diff=3, kw='Letter, Campbell, Kennaway, Private, Cypher'),
    ocr_row(1788, '18 May 1788 (received 7 Jun 1788)',
            'Governor-General in Council → Fort St George (Madras), secret letter mentioning cypher',
            'Supreme Government, Calcutta → Government of Fort St George', 'Calcutta',
            'NAI, Foreign Department, Secret Consultations, 9 June 1788, No. 1', 'NAIDLF00943149', 3,
            'Calcutta-Madras secret correspondence of 1788; possibly cipher passages on Mysore or the Nizam.',
            kw='References, Council, Cypher, Secret'),
    ocr_row(1779, '22 Oct 1779 (consulted 28 Oct 1779)',
            'Governor-General and Council (Hastings) → Fort St George, secret letter mentioning cypher',
            'Supreme Government, Calcutta → Government of Fort St George', 'Calcutta',
            'NAI, Foreign Department, Secret Consultations, 28 October 1779, No. 8', 'NAIDLF00950238', 4,
            'Hastings\'s secret correspondence with Madras on the eve of Haidar Ali\'s 1780 invasion; the Company\'s 1777 cypher code book (PR_000006128785) is the likely key.',
            imp=3, kw='cypher, references, turkey'),
    ocr_row(1796, '24 May 1796 (received 1 Aug 1796)',
            'Supreme Government → Admiral G. K. Elphinstone (HMS Monarch, Simon\'s Bay), letter mentioning cypher',
            'Governor-General in Council → Vice-Admiral George Keith Elphinstone', 'Calcutta / Cape of Good Hope',
            'NAI, Foreign Department, Secret Consultations, 1 August 1796, No. 5', 'NAIDLF00945474', 5,
            'Naval coordination after the capture of the Cape (1795) against the Dutch and French in the Indian Ocean.',
            kw='Madras, Monarch, Forces, Cypher, Admiral'),
    ocr_row(1807, '5 Oct 1807',
            'Supreme Government → Government of Bombay, secret letter on naval matters, mentioning cypher',
            'Governor-General in Council (Minto) → Government of Bombay', 'Calcutta',
            'NAI, Foreign Department, Secret Consultations, 5 October 1807, No. 5', 'NAIDLF00826189', 12,
            '1807: Franco-Persian alliance and the Malcolm/Jones missions to Persia; cipher used with Bombay and the Gulf residents.',
            kw='Cypher, Naval, State, Expediency, Resident'),
    ocr_row(1808, '13 Dec 1807 (received 1 Feb 1808)',
            'Secretary at Prince of Wales Island (Penang) → Supreme Government, secret letter mentioning cypher',
            'Government of Prince of Wales Island → Governor-General in Council', 'Penang',
            'NAI, Foreign Department, Secret Consultations, 1 February 1808, No. 2', 'NAIDLF00829027', 4,
            'Penang\'s secret reports during the war with the French and Dutch in the eastern seas.',
            kw='Secret, Original, Cypher'),
    ocr_row(1813, '30 Mar 1813 (received 24 Apr 1813)',
            'Chief Secretary, Prince of Wales Island → Supreme Government, secret letters mentioning cypher',
            'Government of Prince of Wales Island → Governor-General in Council', 'Penang',
            'NAI, Foreign Department, Secret Consultations, 30 April 1813, No. 1', 'NAIDLF00824821', 4,
            'Raffles-era Java and Straits affairs; cipher between Penang and Calcutta.',
            kw='Cypher, Letters, Council, Secret'),
    ocr_row(1809, '29 Jul 1809',
            'Political consultation with a Resident\'s report mentioning cypher (a Khan named)',
            'a Resident → Governor-General in Council (unknown)', 'unknown',
            'NAI, Foreign Department, Political Consultations, 29 July 1809, No. 22', 'NAIDLF01546081', 4,
            '1809 residency reporting (Persia, Sind, Punjab or Kabul missions were all active that year).',
            kw='Khan, Resident, Cypher'),
    ocr_row(1853, '19 Sep 1853 (received 1 Oct 1853)',
            'Supreme Government ↔ Chief Secretary, Bombay, on Russian letters, mentioning cypher',
            'Government of India, Foreign Department ↔ Government of Bombay', 'Calcutta / Bombay',
            'NAI, Foreign Department, Political Consultations, 14 October 1853, No. 111', 'NAIDLF01946321', 6,
            'Eve of the Crimean War; "Russian letters" in the keywords suggests intercepted or suspicious correspondence.',
            kw='Letters, Russian, Cypher, Bombay, Secret, Commissioner'),
    ocr_row(1808, '22 Feb 1808',
            'Persian letter received by the Governor-General, OCR keywords "Deciphe(r)", "Broken"',
            'unknown Indian correspondent → Governor-General (Minto)', 'unknown',
            'NAI, Foreign Department, Persian Letters Received, No. 327 (issued 22 February 1808)', 'NAIDLF02179604', 2,
            'Possible ramz (cipher) in Persian diplomatic correspondence; more likely an illegible or damaged letter.',
            imp=1, solv=2, diff=4, lang='Persian', kw='Subject, Persian, Original, Letter, Foreign, Deciphe, Broken'),
    ocr_row(1828, '7 Jan 1828',
            'Persian letter copy received, OCR keyword "Cipher"',
            'unknown → Governor-General (unknown)', 'unknown',
            'NAI, Foreign Department, Persian Copies of Letters Received, No. 26 (issued 7 January 1828)', 'NAIDLF02289159', 3,
            'Possible ramz in Persian correspondence; the English title is a garbled machine rendering.',
            imp=1, solv=2, diff=4, lang='Persian', kw='Point, Coherent, Cipher, Board'),
]


def main():
    out = []
    for r in ROWS:
        r = dict(r)
        r.setdefault('region', 'Other')
        r['period'] = period(r['year'])
        r.setdefault('score_note', NOTE)
        r.setdefault('seen', 'catalogue')
        r.setdefault('source', SRC)
        out.append(r)
    keys = ['year', 'date', 'title', 'correspondents', 'place', 'language', 'region', 'period', 'shelfmark', 'folio_note',
            'cls', 'status', 'why', 'importance', 'solvability', 'difficulty', 'score_note', 'verify', 'links', 'seen',
            'source', 'prior_art']
    out = [{k: r[k] for k in keys + (['decode_ids'] if 'decode_ids' in r else [])} for r in out]
    with open('candidates.json', 'w', encoding='utf8') as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
    print(len(out), 'rows')


if __name__ == '__main__':
    main()
