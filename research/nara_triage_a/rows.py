"""Candidate rows for the NARA RG 59 1789-1906 triage (slice A). `python rows.py` writes candidates.json."""
import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
CAT = 'https://catalog.archives.gov/id/'
MED = 'https://catalog.archives.gov/medialz/dc-metro/rg-059/603720/'
NOTE = ('Scored from the NARA OCR and the frame image(s) named in folio_note during the Oct 2026 NARA bulk-scan '
        'triage (research/nara_triage_a/)')
ROWS = []


def row(**k):
    k.setdefault('source', 'NARA RG 59 bulk-scan triage (slice A, 1789-1906)')
    k.setdefault('score_note', NOTE)
    ROWS.append(k)


row(year=1797, date='25 Messidor an V (13 July 1797); enclosed in King No. 53, London, 12 Nov 1797',
    title='Delacroix (French Foreign Minister) → Létombe (French consul general, Philadelphia), despatch No. 5 '
          'entirely in a French numeric code, copy sent by Rufus King',
    correspondents='Charles Delacroix → Philippe de Létombe (copy forwarded by Rufus King to Timothy Pickering)',
    place='Paris', language='French', region='France', period='1701-1800',
    shelfmark='NARA RG 59, Despatches from US Ministers to Great Britain, vol. 5 (10 Aug 1796-28 Dec 1797) '
              '= microfilm M30 roll 5, catalog naId 188512917',
    folio_note='frames 0244-0245 (about 470 code groups, 1-1171, in a clerk\'s copy marked "Dup." and "(Copy)"; '
               'heading and close "Salut et fraternité, Delacroix" in clear); King\'s covering No. 53 at frames '
               '0239-0241',
    cls='B',
    status='Frame 0244 viewed: a clean copy of the whole despatch in code, no interlinear or appended decipherment; '
           'the OCR of 0245 and the neighbouring frames shows none either. Not on DECODE; known.py: no hit for '
           'Létombe/Delacroix.',
    why='A Directory instruction to the French chargé/consul general in Philadelphia days before Delacroix left office '
        'and on the eve of the XYZ mission, which Rufus King obtained in London (probably from Grenville\'s '
        'decipherers); its content is not known from the US side.',
    importance=4, solvability=3, difficulty=3,
    verify='Read frames 0244-0245 in full; look for the plaintext in the French ministerial register (AMAE '
           'Correspondance politique États-Unis vol. 47-48) or Nasatir & Monell\'s calendar (1967); otherwise a '
           'codebook-style attack on ~470 groups of a French 1100-group nomenclator.',
    links=[{'label': 'NARA M30 vol. 5', 'href': CAT + '188512917'},
           {'label': 'frame 0244', 'href': MED + 'M30/M30-004/M30-004-0244.jpg'},
           {'label': 'frame 0245', 'href': MED + 'M30/M30-004/M30-004-0245.jpg'}],
    seen='image',
    prior_art='open as far as checked (27 Oct 2026: web search for Delacroix/Létombe 25 Messidor an V found only '
              'calendars; Turner, Correspondence of the French Ministers 1791-97 not checked for this letter; the '
              'French register copy, if kept, would be in clear)')

row(year=1814, date='c. Nov 1813 - 1815 (one leaf dated 14 Jan 1814)',
    title='Anthony Morris (US confidential agent at Cadiz/Madrid) → James Monroe, despatches largely in an '
          'unidentified State Department code (the = 285?)',
    correspondents='Anthony Morris → James Monroe, Secretary of State',
    place='Cadiz; Madrid', language='English', region='Spain', period='1801-1900',
    shelfmark='NARA RG 59, Despatches from US Ministers to Spain, vol. 12 (28 May 1813-13 Apr 1816) = microfilm '
              'M31 roll 14, catalog naId 188606645',
    folio_note='code runs on frames 0036-0039 (Triplicate, Cadiz), 0050, 0052-0057, 0124-0125 and 0191-0192 (two '
               'copies of the same despatch: a built-in check), about 3,000 groups in all; frame 0058 is a Morris '
               'account sheet',
    cls='C',
    status='Frame 0039 viewed: page after page of numeric code with a few clear words ("would induce them to", '
           '"an offer was made by them", "the intention of holding it"), groups 1-1600 with marks (subscript 5/s, '
           'c, underline, arrow) as in the JQA-type syllabic codes; no interlinear decipherment, none in the OCR '
           'of the neighbouring frames. Signature groups do not match the JQA (the=1385), Armstrong (972), Pinckney '
           '(1651) or Code No. 11 tables; 285 and 76 are the most frequent groups. Not on DECODE; known.py: no hit.',
    why='Morris negotiated with Cevallos over Florida and seized ships in the last years of the Peninsular War; '
        'the coded passages are the confidential part of the only US channel to the Regency and to Ferdinand VII '
        'in 1813-15.',
    importance=3, solvability=3, difficulty=3,
    verify='Check Woolfley, A Quaker Goes to Spain (2013), and Manning 1925 vol. 3 for printed decodes; look for '
           'a decipherment bound elsewhere in vol. 12; otherwise rebuild the code from the two copies and the '
           'clear-text islands (syllabic code of ~1,600 groups, partly alphabetical).',
    links=[{'label': 'NARA M31 vol. 12', 'href': CAT + '188606645'},
           {'label': 'frame 0039', 'href': MED + 'M31/M31-014/M31-014-0039.jpg'}],
    seen='image',
    prior_art='open as far as checked (27 Oct 2026: web search found Woolfley 2013 on the mission, no mention of '
              'cipher; Founders has only his private letters to Madison)')

row(year=1814, date='14 June 1814 (Duplicate)',
    title='Joel R. Poinsett → James Monroe, despatch with code passages on Britain, the Plate and the Portuguese, '
          'sibling of the 1813 Santiago despatch already in the catalogue',
    correspondents='Joel Roberts Poinsett → James Monroe',
    place='unknown (Buenos Aires/Chile mission; "Duplicate")', language='English', region='Americas',
    period='1801-1900',
    shelfmark='NARA RG 59, Despatches from Special Agents, vol. 3 (Poinsett 1813-18) = microfilm M37 roll 2, '
              'catalog naId 213803757',
    folio_note='frames 0097-0099 (code passages on 0098, about 60 groups, e.g. "1385, 415 ... rupture between G. '
               'Britain ..."); the catalogued 20 Feb 1813 Santiago letter is frame 0093 (located here: both pages '
               'carry long code passages, no decipherment) with the 1813 table of contents at 0091',
    cls='B',
    status='OCR only for 0098; frame 0093 viewed (the 1813 letter): code in Poinsett\'s hand, no interlinear '
           'decipherment. 1355 is the commonest group in both. Same code and volume as the catalogue\'s Poinsett '
           '1813 row, which this row should be merged with or added to as a second letter.',
    why='A second coded Poinsett letter gives the 1813 code more text and its own content on Britain and the '
        'Plate in 1814.',
    importance=3, solvability=3, difficulty=3,
    verify='View frames 0097-0099; transcribe both letters together and test the 1810-era State Department codes '
           '(Weber 1979 tables) once available.',
    links=[{'label': 'NARA M37 vol. 3', 'href': CAT + '213803757'},
           {'label': 'frame 0093 (1813 letter)', 'href': MED.replace('603720/', '') + '876974/M37-02/M37-02-0093.jpg'},
           {'label': 'frame 0098', 'href': MED.replace('603720/', '') + '876974/M37-02/M37-02-0098.jpg'}],
    seen='image',
    prior_art='Manning 1925 prints Poinsett 1813 with "(undeciphered cipher)"; the 1814 letter not checked in Manning')

row(year=1813, date='3 Sept 1813 (No. 1, private) to 1814',
    title='William H. Crawford → James Monroe, Paris despatches with long coded passages in the JQA-type '
          'Department code (the = 1385), no decipherment on the filmed copies',
    correspondents='William Harris Crawford (US minister to France) → James Monroe, Secretary of State',
    place='Paris', language='English', region='France', period='1801-1900',
    shelfmark='NARA RG 59, Despatches from US Ministers to France, vol. 17 (25 July 1813-17 Aug 1814) = microfilm '
              'M34 roll 17, catalog naId 188672892',
    folio_note='coded runs on frames 0027-0029 (No. 1, 3 Sept 1813: 0028 alone about 410 groups, 70 OCR words), '
               '0031-0033, 0047-0049, 0065-0067, 0072, 0086-0090, 0199-0201, 0213-0214 (1814); several thousand '
               'groups in all',
    cls='B',
    status='OCR only (frames not viewed): the coded frames carry few words, so no interlinear decipherment is '
           'likely; signature groups 1385/1576/668/1384/1401 occur 6-43 times per frame, so this is the code '
           'rebuilt in targets/jqa. A trial decode of frame 0028 with targets/jqa/code_table.tsv already gives '
           'phrases ("I am ignorant ... support ... the Emperor ... negotiation ... it is generally ..."), despite '
           'the noisy OCR. Monroe to Madison [Nov 1813] (Founders Madison/03-07-02-0011): the 3 Sept letter came '
           '"in cypher" and was to be deciphered, so a contemporary decode existed but is not on the film.',
    why='Crawford reported from Napoleon\'s capital during the 1813-14 campaigns and the first Restoration; the '
        'coded parts hold his talks with Bassano/Talleyrand on the Berlin and Milan decrees and a settlement.',
    importance=3, solvability=5, difficulty=1,
    verify='View frames 0027-0033 to confirm no decipherment; transcribe and decode with targets/jqa/code_table.tsv; '
           'check whether the Madison or Monroe Papers print the deciphered text.',
    links=[{'label': 'NARA M34 vol. 17', 'href': CAT + '188672892'},
           {'label': 'frame 0028', 'href': MED + 'M34/M34-017/M34-017-0028.jpg'},
           {'label': 'Monroe to Madison, Nov 1813', 'href': 'https://founders.archives.gov/documents/Madison/03-07-02-0011'}],
    seen='catalogue',
    prior_art='a decipherment was made in 1813 (Monroe to Madison); no printed text found (27 Oct 2026 web search); '
              'Crawford Papers not checked')

row(year=1836, date='1836 (Ellis\'s first mission) and 16 Nov 1839 (No. 9)',
    title='Powhatan Ellis → John Forsyth, Mexico City despatches in the JQA-type Department code on the Texas war '
          'and Mexican politics, pure code on the filmed copies',
    correspondents='Powhatan Ellis (US chargé, then minister, in Mexico) → John Forsyth, Secretary of State',
    place='Mexico City', language='English', region='Americas', period='1801-1900',
    shelfmark='NARA RG 59, Despatches from US Ministers to Mexico, vol. 7 (23 Mar-29 Oct 1836) = M97 roll 8, '
              'naId 189101351; vol. 8 (Nov 1836-Feb 1837) = M97 roll 9, naId 189101765; vol. 9 (12 June 1837-28 '
              'July 1840) = M97 roll 10, naId 189102194',
    folio_note='vol. 7 frames 0014 (mirror-image exposure) to 0019, 0025-0027 (a despatch of 8 May 1836 "in cypher"), '
               '0066-0071, 0078, 0123, 0204, 0323: about 3,000 groups with 0-25 OCR words per frame; vol. 8 frames '
               '0098-0099, 0208-0211; vol. 9 frames 0298-0303 (No. 9, 16 Nov 1839, about 500 groups, no words)',
    cls='B',
    status='OCR only: no interlinear words on the coded frames. Trial decodes with targets/jqa/code_table.tsv read '
           'as sense: vol. 9 frame 0302 "a war with Texas ... under such circumstances will be decidedly popular '
           '... the insurgents who were lately in arms against this government have either capitulated ... or have '
           'been dispersed"; vol. 7 frame 0015 "... the interior ... this movement ... the President ... a '
           'proclamation ... the party ...". Not on DECODE; known.py: no hit.',
    why='Coded reports from the US legation in Mexico during the Texas Revolution and the 1839 crisis, the '
        'confidential side of a relationship that led to war in 1846.',
    importance=3, solvability=5, difficulty=1,
    verify='Check Manning, Diplomatic Correspondence ... Inter-American Affairs vol. 8 (Mexico 1831-48; HathiTrust, '
           'behind a bot check here) for printed decodes; if absent, transcribe from the frames and decode with '
           'targets/jqa/code_table.tsv.',
    links=[{'label': 'NARA M97 vol. 7', 'href': CAT + '189101351'},
           {'label': 'NARA M97 vol. 9', 'href': CAT + '189102194'},
           {'label': 'vol. 9 frame 0302', 'href': MED + 'M97/M97-010/M97-010-0302.jpg'}],
    seen='catalogue',
    prior_art='unchecked: Manning Inter-American Affairs vol. 8 (1937) may print these decoded (it prints cipher '
              'passages in small capitals when a Department decipherment exists); not reachable 27 Oct 2026')


if __name__ == '__main__':
    json.dump(ROWS, open(os.path.join(HERE, 'candidates.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(len(ROWS), 'rows')
