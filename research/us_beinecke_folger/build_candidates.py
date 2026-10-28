"""Build candidates.json for the Oct 2026 Beinecke/Folger sweep (rows written by hand from the harvest)."""
import json, os

QS = 'https://search.library.yale.edu/catalog/'
QA = 'https://search.library.yale.edu/archives?q='
FC = 'https://catalog.folger.edu/record/'
DC = 'https://collections.library.yale.edu/catalog/'
B = 'Beinecke sweep'
F = 'Folger sweep'
SN = 'Scored from the archive description during the Oct 2026 {} sweep (research/us_beinecke_folger/); not viewed'
OPEN = 'open (checked 28 Oct 2026: repo known.py, DECODE list)'


def row(**k):
    k.setdefault('seen', 'catalogue')
    k.setdefault('score_note', SN.format('Beinecke' if k['source'] == B else 'Folger'))
    k.setdefault('prior_art', OPEN)
    return k


R = []
R.append(row(year=1858, date='21 Jul 1858', title='Unsigned cipher letter from Great Salt Lake City during the Utah War',
    correspondents='unknown → unknown', place='Great Salt Lake City, Utah Territory', language='English (probably)',
    region='Americas', period='1801-1900', shelfmark='Beinecke, Yale Collection of Western Americana, WA MSS S-4203 Un21',
    folio_note='1 item, two pages entirely in a letter cipher (Schmeh: first line ABCDLMNMOPSTVWXYG)', cls='C',
    status='Catalogued "Undecoded cipher letter"; summary: may relate to the Utah Expedition. Not on DECODE, not in repo. Not in Yale Digital Collections, but Klaus Schmeh posted images (Dec 2020, from Ken Alford, BYU).',
    why='A ciphered letter written from Salt Lake City weeks after the army entered it (Utah War, 1857-58); the writer could be a Mormon leader, an army officer or a federal official.',
    importance=3, solvability=3, difficulty=3,
    verify="Transcribe from the images in Schmeh's post (scienceblogs.de, 11 Dec 2020); request Beinecke scans; test letter substitution and Deseret-alphabet hypotheses.",
    links=[{'label': 'Quicksearch record', 'href': QS + '99155432663408651'},
           {'label': 'Schmeh blog, 11 Dec 2020', 'href': 'https://scienceblogs.de/klausis-krypto-kolumne/2020/12/11/can-you-decipher-an-encrypted-letter-from-the-utah-war/'}],
    source=B, prior_art='open (checked 28 Oct 2026: Schmeh blog 2020 says unsolved, no solution in comments to 2022; repo, DECODE)'))
R.append(row(year=1781, date='3 Aug 1781', title='Barras → Rochambeau, Newport, letter partly in code, "not decoded"',
    correspondents='Jacques-Melchior Saint-Laurent, comte de Barras → Jean-Baptiste de Vimeur, comte de Rochambeau',
    place='Newport, Rhode Island', language='French', region='Americas', period='1701-1800',
    shelfmark='Beinecke, Rochambeau Papers, GEN MSS 146, Series I, Box 4, folder 216',
    folio_note='letter signed, 1 1/2 pp. 4to, partly in code', cls='A',
    status='Archives at Yale: "Partly in code, (not decoded)". Sibling Barras letters of 11 Aug 1781 (folder 218, interlinear decipher; DECODE R2856 "Decrypted") and 17 Aug (folder 221, digitised, interlinear decode) are in the same series, and Series II Box 5 folders 294-298 hold codes and tables (numbered code with a simple substitution; Talmadge; Robert Morris). Not digitised.',
    why='Barras commanded the French squadron at Newport on the eve of the Yorktown campaign; a coded letter of 3 Aug 1781 concerns the junction with de Grasse.',
    importance=4, solvability=3, difficulty=2,
    verify='Request scans of box 4 f. 216; apply the code of the 11 and 17 Aug letters and box 5 f. 296; check Doniol, Histoire de la participation de la France, t. V, for a printed text.',
    links=[{'label': 'Quicksearch archives search', 'href': QA + 'Barras+%22partly+in+code%22'},
           {'label': 'Sibling of 17 Aug 1781 (digitised)', 'href': DC + '2067539'}],
    source=B, prior_art='open (checked 28 Oct 2026: web search, founders.archives.gov; Doniol t. V not checked)'))
R.append(row(year=1648, date='1648 (copied c. 1720)', title='Copies of 66 "secret letters" of Charles I from the Isle of Wight, names in numerical cipher, with George Hopkins\'s petition',
    correspondents='Charles I → William Hopkins (Newport, Isle of Wight)', place='Carisbrooke / Newport, Isle of Wight', language='English',
    region='England', period='1611-1650', shelfmark='Beinecke, Osborn c650',
    folio_note='1 v., 64 pp.; copies of 66 letters, names in numerical cipher', cls='B',
    status='Catalogue: "copies of 66 secret letters written by Charles I in 1648, with names in numerical cipher". Copy of c. 1720. Not on DECODE, not digitised. Originals: 61 letters sold in the UK (Friends of the National Libraries grant), others in BL Egerton 1533 and 1788.',
    why="The King's escape correspondence from Carisbrooke; the number names may share a table with the repo's two unread 1648 letters (targets/charlesi, 22 May 1648 to Worsley).",
    importance=3, solvability=2, difficulty=2,
    verify="Check Sarah Poynting's edition of Charles I's writings and BL Egerton 1788 for the decoded names; request scans; compare with the Biermann/Bosbach/Brown nomenclator in targets/charlesi.",
    links=[{'label': 'Quicksearch record', 'href': QS + '9983427143408651'}],
    source=B, prior_art='possibly read (checked 28 Oct 2026: many Hopkins letters are edited, the name codes not confirmed; repo charlesi target)'))
R.append(row(year=1700, date='15 Apr 1700', title='Earl of Jersey → Earl of Manchester, Whitehall, part in cipher never printed',
    correspondents='Edward Villiers, Earl of Jersey → Charles Montagu, Earl of Manchester', place='Whitehall', language='English',
    region='England', period='1651-1700', shelfmark='Beinecke, Manchester papers, OSB MSS fc37, Box 3, folder 34',
    folio_note='"Partly in cipher. Printed, without the part in cipher, in Cole\'s Memoirs, p. 122"', cls='B',
    status='Not on DECODE (its Manchester records are R2854-R2872), not digitised. Same correspondence and period as R2859/R2860, deciphered here with the THE=454 key (targets/yard1699).',
    why='Secretary of State to the ambassador in Paris on the Partition Treaty ("the great affair was quite finished") and peace in the North; the ciphered part was left out of the print.',
    importance=3, solvability=3, difficulty=2,
    verify='Request scans; decipher with the THE=454 key (targets/stepney, targets/yard1699).',
    links=[{'label': 'Quicksearch archives search', 'href': QA + 'Jersey+Manchester+cipher'}],
    source=B, prior_art="open (checked 28 Oct 2026: Cole 1733 prints it without the cipher part; repo, DECODE)"))
R.append(row(year=1700, date='23 Dec 1700', title="James Vernon → Earl of Manchester, Whitehall, paragraph in cipher (unprinted) on M. Lilienroot's project",
    correspondents='James Vernon → Charles Montagu, Earl of Manchester', place='Whitehall', language='English',
    region='England', period='1651-1700', shelfmark='Beinecke, Manchester papers, OSB MSS fc37, Box 6, folder 52',
    folio_note='"Printed, with the exception of a paragraph in cipher, in Cole\'s Memoirs, p. 275"', cls='B',
    status="Not on DECODE, not digitised. Vernon's other cipher letters to Manchester (Nov-Dec 1700) were deciphered on fly-leaves; this one has no decipher noted.",
    why="The Swedish envoy Lilienroot's project in the weeks after the Spanish succession opened.",
    importance=2, solvability=3, difficulty=2,
    verify='Request scans; decipher with THE=454 (targets/stepney).',
    links=[{'label': 'Quicksearch archives search', 'href': QA + 'Vernon+Lilierote'}],
    source=B, prior_art='open (checked 28 Oct 2026: Cole prints it without the cipher paragraph)'))
R.append(row(year=1700, date='8 Jan 1700', title='Earl of Jersey → Earl of Manchester, Whitehall, instructions partly in cipher (printed "not quite correctly")',
    correspondents='Edward Villiers, Earl of Jersey → Charles Montagu, Earl of Manchester', place='Whitehall', language='English',
    region='England', period='1651-1700', shelfmark='Beinecke, Manchester papers, OSB MSS fc37, Box 3, folder 2',
    folio_note='2 pp., partly in cipher; digitised (Yale oid 16601191)', cls='B',
    status='DECODE R2868 "Non-decrypted"; listed in research/cryptoole candidates (GB16XX-128) but not in catalogue.json. Cole\'s Memoirs p. 94 prints it "not quite correctly", so the cipher may be partly read in print.',
    why='Instructions to the Paris embassy during the Partition Treaty negotiation.',
    importance=2, solvability=4, difficulty=1,
    verify='Read the images (oid 16601191) with THE=454 and compare with Cole p. 94.',
    links=[{'label': 'Yale Digital Collections', 'href': DC + '16601191'}, {'label': 'DECODE R2868', 'href': 'https://de-crypt.org/decrypt-web/RecordsView/2868'}],
    source=B, prior_art='partly in print (Cole 1733 p. 94, "not quite correctly"); DECODE Non-decrypted', decode_ids=[2868]))
R.append(row(year=1765, date='1764-1766', title='Walter Titley, envoy at Copenhagen, diplomatic correspondence with several letters in cipher',
    correspondents='Walter Titley ↔ Secretaries of State and others', place='Copenhagen', language='English',
    region='Scandinavia', period='1701-1800', shelfmark='Beinecke, OSB MSS 64 (3 boxes)',
    folio_note='letters and retained fair copies, chronological; "several letters in cipher"', cls='C',
    status='Catalogue note "Several letters in cipher". Not digitised, not on DECODE, not in repo.',
    why='British envoy in Denmark during the Russian alliance talks of the 1760s.',
    importance=3, solvability=2, difficulty=3,
    verify="Request scans of the cipher letters; check TNA SP 75 for deciphered copies and the office's key of the period.",
    links=[{'label': 'Quicksearch record', 'href': QS + '9946621933408651'}],
    source=B, prior_art='open (checked 28 Oct 2026: repo, DECODE; TNA SP 75 copies not checked)'))
R.append(row(year=1705, date='19 Apr 1705', title='Richard Hill, envoy to Savoy: copies of letters partly in cipher to "Mons. le duc Fengilea"',
    correspondents='Richard Hill → [Mons. le duc Fengilea] (unidentified)', place='Turin (Savoy)', language='unknown',
    region='Italy', period='1701-1800', shelfmark='Beinecke, Hill papers, OSB MSS 31, Box 1, folder 35',
    folio_note='copies, partly in cipher', cls='C',
    status='Archives at Yale title only. Not digitised (four other OSB MSS 31 folders are). Not on DECODE, not in repo.',
    why="Hill's Savoy embassy in the War of the Spanish Succession (siege of Turin, 1705-06).",
    importance=3, solvability=2, difficulty=3,
    verify='Check Blackley (ed.), The Diplomatic Correspondence of Richard Hill (1845) for a deciphered copy; request scans.',
    links=[{'label': 'Quicksearch archives search', 'href': QA + 'Fengilea'}],
    source=B, prior_art='unclear (checked 28 Oct 2026: repo, DECODE; Blackley 1845 not checked)'))


def matched(year, date, title, corr, place, lang, region, period, shelf, note, why, imp, verify, q, diff=3, sol=1, cls='C', pa=OPEN):
    R.append(row(year=year, date=date, title=title, correspondents=corr, place=place, language=lang, region=region,
        period=period, shelfmark=shelf, folio_note=note, cls=cls,
        status='Found by the cipher-family queries in Quicksearch (the matching note sits on archives.yale.edu, which returned 403, so the cipher is not confirmed). Not digitised, not on DECODE, not in repo.',
        why=why, importance=imp, solvability=sol, difficulty=diff, verify=verify,
        links=[{'label': 'Quicksearch archives search', 'href': QA + q}], source=B, prior_art=pa))


matched(1666, '23 Sep - 12 Oct 1666', 'Earl of Sandwich → Earl of Carlingford, Madrid, two letters (cipher matched)',
    'Edward Montagu, 1st Earl of Sandwich → Theobald Taaffe, Earl of Carlingford', 'Madrid', 'English', 'Spain', '1651-1700',
    'Beinecke, Carlingford papers, OSB MSS 5, Box 2, folder 58', '2 LS',
    "Sandwich's Madrid embassy (Anglo-Spanish treaty of 1667) writing to Carlingford, envoy at Vienna.", 3,
    'Open the folder on Archives at Yale to confirm cipher; request scans.', 'Carlingford+Sandwich')
matched(1674, '23-24 Jul 1674', 'Earl of Orrery → Earl of Danby, Bath, two letters (cipher matched)',
    'Roger Boyle, 1st Earl of Orrery → Thomas Osborne, Earl of Danby', 'Bath', 'English', 'England', '1651-1700',
    'Beinecke, Danby papers, OSB MSS 6, Box 1, folder 2', '2 ALS', 'Orrery to the Lord Treasurer, Irish and court politics.', 2,
    'Confirm on Archives at Yale; request scans.', 'Orrery+Danby')
matched(1673, '30 Dec 1673', 'Earl of Essex (Lord Lieutenant) → Viscount Latimer (Danby), Dublin Castle (cipher matched)',
    'Arthur Capel, 1st Earl of Essex → Thomas Osborne, Viscount Latimer', 'Dublin Castle', 'English', 'England', '1651-1700',
    'Beinecke, Danby papers, OSB MSS 6, Box 1, folder 4', 'ALS', 'Viceroy of Ireland to the new Lord Treasurer.', 2,
    'Check Essex Papers (Camden Society 1890) for a printed text; confirm on Archives at Yale.', 'Essex+Danby+Dublin',
    pa='unclear (checked 28 Oct 2026: repo, DECODE; Essex Papers not checked)')
matched(1658, '22 Jan 1658?', 'Charles II (in exile) → [Edward Proger], autograph letter (cipher matched)',
    'Charles II → Edward Proger', 'unknown (Bruges?)', 'English', 'England', '1651-1700',
    'Beinecke, Osborn Manuscript Files, OSB MSS FILE 3086 (box 31)', 'AL',
    'Exile-court correspondence; royalist ciphers of 1658 are a known family (Nicholas, Hyde).', 3,
    'Confirm on Archives at Yale; request scan; check the Calendar of Clarendon State Papers.', 'Proger')
matched(1676, '4 Apr 1676', "Toussaint de Forbin-Janson, French ambassador in Poland → Cardinal César d'Estrées, Cracow (cipher matched)",
    "Toussaint de Forbin-Janson, bishop of Marseille → César, Cardinal d'Estrées", 'Cracow', 'French', 'Poland-Lithuania', '1651-1700',
    'Beinecke, Osborn Manuscript Files, OSB MSS FILE 16601 (box 173)', 'ALS',
    "French ambassador at Sobieski's coronation (Feb 1676) writing to d'Estrées in Rome.", 3,
    'Confirm on Archives at Yale; request scan; French Polish-embassy keys are in AE CP Pologne.', 'Forbin-Janson')
matched(1712, '2 Oct 1712', 'Arthur Mainwaring → Lord Coningsby, letter (cipher matched)',
    'Arthur Mainwaring → Thomas, Lord Coningsby', 'unknown', 'English', 'England', '1701-1800',
    'Beinecke, Osborn Manuscript Files, OSB MSS FILE 9630 (box 97)', 'AL',
    'Whig manager to Coningsby in the last Tory years of Queen Anne; Whig letters used number names.', 2,
    'Confirm on Archives at Yale; request scan.', 'Mainwaring+Coningsby', diff=2)
matched(1710, '2 Aug 1710', 'Sarah, Duchess of Marlborough → [Lord Coningsby], letter (cipher matched)',
    'Sarah Churchill, Duchess of Marlborough → Thomas, Lord Coningsby', 'unknown', 'English', 'England', '1701-1800',
    'Beinecke, Osborn Manuscript Files, OSB MSS FILE 9886 (box 99)', 'AL',
    'The Duchess during the fall of the Godolphin ministry (Aug 1710).', 3,
    "Confirm on Archives at Yale; request scan; the Marlborough number-name code is printed in Snyder's Marlborough-Godolphin Correspondence.",
    'Marlborough+Coningsby', diff=2, cls='B')
matched(1701, '2 Sep 1701 - Sep 1702', 'William Blathwayt → George Stepney, three letters from Loo, Dieren and Dyrham (cipher matched)',
    'William Blathwayt → George Stepney', 'Loo; Dieren; Dyrham Park', 'English', 'England', '1701-1800',
    'Beinecke, Blathwayt papers, OSB MSS 2, Box 2, folders 33a, 34a, 36', '3 ALS',
    "Secretary at War with the King in Holland to the envoy at Vienna; may share the key that targets/stepney (24 groups open) lacks. The same papers hold 'Memorandum of cipher used by Stanhope / Poley' (box 8 f. 179, box 6 f. 142).", 3,
    'Confirm on Archives at Yale; request scans; compare with the targets/stepney groups.', 'Blathwayt+Stepney', diff=2, cls='B')
matched(1698, '9/19 Aug - 6 Dec 1698', 'William Blathwayt → John Robinson (envoy in Sweden), four drafts and a copy (cipher matched)',
    'William Blathwayt → John Robinson', 'Loo; The Hague', 'English', 'England', '1651-1700',
    'Beinecke, Blathwayt papers, OSB MSS 2, Box 1, folder 27', '4 AL (drafts), 1 copy',
    'First Partition Treaty months; Robinson was envoy at Stockholm; drafts may give clear text of passages sent in cipher.', 2,
    'Confirm on Archives at Yale; request scans.', 'Blathwayt+Robinson', diff=2)

R.append(row(year=1712, date='3 Mar - 11 Aug 1712', title='Giovanni Emo (Venetian, Paris) → Carlo Ruzzini at the Congress of Utrecht, letters partly in code',
    correspondents='Giovanni Emo → Carlo Ruzzini', place='Paris', language='Italian',
    region='Italy', period='1701-1800', shelfmark='Beinecke, GEN MSS VOL 105',
    folio_note='1 v., [168] pp.; "Chiefly in Italian; some letters in code"', cls='C',
    status='Catalogue note. Not digitised, not on DECODE, not in repo.',
    why='Venetian diplomatic reporting from Paris to the Venetian plenipotentiary at Utrecht.',
    importance=3, solvability=2, difficulty=3, verify='Request scans; Venetian ciphers of 1712 may survive in ASVe (Capi del Consiglio dei X, cifre).',
    links=[{'label': 'Quicksearch record', 'href': QS + '9939437263408651'}], source=B))
R.append(row(year=1712, date='11 Mar 1712 - 4 Aug 1713', title='Pietro Grimani (Venetian ambassador, London) → Carlo Ruzzini at Utrecht, letters (code noted)',
    correspondents='Pietro Grimani → Carlo Ruzzini', place='London', language='Italian',
    region='Italy', period='1701-1800', shelfmark='Beinecke, GEN MSS 177',
    folio_note='1 v., c. 200 pp.; companion of GEN MSS VOL 105', cls='C',
    status='Matched "in code"; record note truncated, catalogued like the Emo volume. Not digitised, not on DECODE.',
    why='Venetian reporting from London on the Utrecht peace.',
    importance=3, solvability=2, difficulty=3, verify='Confirm code in the volume; request scans.',
    links=[{'label': 'Quicksearch record', 'href': QS + '9939439083408651'}], source=B))
for yr, box, note in [(1805, 'Box 1', 'Encrypted diary'), (1825, 'Box 3', 'Encrypted diary'), (1830, 'Box 3', 'Partially encrypted diary')]:
    R.append(row(year=yr, date=str(yr), title=f'Joseph von Chlingensperg auf Berg, {note.lower()} ({yr})',
        correspondents='Joseph von Chlingensperg auf Berg (diarist)', place='Bavaria (probably)', language='German',
        region='Germany', period='1801-1900', shelfmark=f'Beinecke, Chlingensperg family diaries, GEN MSS 1495, Series II, {box}',
        folio_note=note, cls='B',
        status=f'Archives at Yale title "{note}". The same series holds a 20th-century "Translation of 1811 diary, with related papers" (Box 2), which may give the system. Not digitised, not on DECODE, not in repo.',
        why='A Bavarian noble diary of the Napoleonic and Restoration years kept partly in cipher.',
        importance=2, solvability=2, difficulty=2,
        verify='Request scans; check the Box 2 translation papers for the key.',
        links=[{'label': 'Quicksearch archives search', 'href': QA + 'Chlingensperg+encrypted'}], source=B))
R.append(row(year=1838, date='28 Jun 1838 - 31 Dec 1839', title='P. R. Shield diary (London, Switzerland, Milan, Tynemouth) with notes in an unidentified cypher',
    correspondents='P. R. Shield (diarist)', place='London; Switzerland; Milan; Tynemouth', language='English',
    region='England', period='1801-1900', shelfmark='Beinecke, Osborn d520', folio_note='c. 140 pp.; "Brief notes in an unidentified cypher are appended to some entries"',
    cls='C', status='Catalogue note. Not on DECODE, not in repo; Quicksearch lists the format as Images too, so it may be digitised.',
    why="Private notes of a traveller at Victoria's coronation and Ferdinand I's Milan coronation.",
    importance=1, solvability=3, difficulty=2, verify='Look for the volume in Yale Digital Collections; transcribe the cypher notes.',
    links=[{'label': 'Quicksearch record', 'href': QS + '99155871393408651'}], source=B))
R.append(row(year=1682, date='c. 1682', title='Commonplace book (sermon notes, verse, a comedy) with several pages of shorthand and cipher',
    correspondents='Edward Sheperd? (owner)', place='London (Aldersgate)', language='English',
    region='England', period='1651-1700', shelfmark='Beinecke, Osborn b216', folio_note='400 pp.; "several pages of shorthand and cipher"',
    cls='C', status='Catalogue note. Not digitised, not on DECODE.', why='Private cipher in a Restoration household book.',
    importance=1, solvability=2, difficulty=2, verify='Request scans; separate shorthand from cipher.',
    links=[{'label': 'Quicksearch record', 'href': QS + '9970402513408651'}], source=B))
R.append(row(year=1700, date='c. 1682-1720 (book dated 1658)', title='Cipher passages on the fly-leaf and inside J. Fairfax\'s "Exposison on the 75 Psalm"',
    correspondents='unknown (owners Jacob Caley 1682, Mary Cross 1683, Thomas Flindell 1719/20)', place='Ipswich?, England', language='English',
    region='England', period='unknown', shelfmark='Beinecke, Osborn b253', folio_note='two passages "in the same cipher" (fly-leaf verso and later)',
    cls='C', status='Catalogue note. Not digitised, not on DECODE.', why="An owner's private cipher in a Puritan sermon book.",
    importance=1, solvability=2, difficulty=2, verify='Request scans of the fly-leaf.',
    links=[{'label': 'Quicksearch record', 'href': QS + '9970402913408651'}], source=B))
R.append(row(year=1697, date='1697', title='William Stanton, "Cases and discourses controversial in matters divine", with passages in cipher',
    correspondents='William Stanton (b. 1673), compiler', place='England', language='English',
    region='England', period='1651-1700', shelfmark='Beinecke, Osborn b77', folio_note='cipher on pp. 79-80, 96, 97, 100 (not among the digitised pp. 14-21)',
    cls='C', status='Catalogue: "Portions of text in cipher on p. 79-80, 96, 97, and 100". Partially digitised (oid 10001763), cipher pages not. Not on DECODE.',
    why="Private cipher in a dissenter's theological letter-book.",
    importance=1, solvability=2, difficulty=2, verify='Request scans of pp. 79-100.',
    links=[{'label': 'Yale Digital Collections', 'href': DC + '10001763'}], source=B))
R.append(row(year=1713, date='1710-1716', title="Thomas Fossey's notebook of veterinary recipes, sections in a vowel-to-digit cipher",
    correspondents='Thomas Fossey (owner; also John and William Fossey)', place='England', language='English',
    region='England', period='1701-1800', shelfmark='Beinecke, GEN MSS VOL 855', folio_note='76 images; e.g. p. 16 recto margin "sh37", "St4ff" (vowels as digits)',
    cls='C', status='Catalogue: "Some sections are completed in a cryptographic code". Fully digitised. Seen 28 Oct 2026: vowels replaced by digits, trivially readable. Not on DECODE.',
    why='Farm remedies hidden by a simple vowel cipher; a test item rather than a historical find.',
    importance=1, solvability=5, difficulty=1, verify='Read the cipher sections from the IIIF images.',
    links=[{'label': 'Yale Digital Collections', 'href': DC + '33569870'}], seen='image',
    score_note='Scored from the archive description and two scans (pp. 4r, 16r) during the Oct 2026 Beinecke sweep (research/us_beinecke_folger/)',
    source=B))
R.append(row(year=1725, date='c. 1700-1750', title='German recipe and charm book with several pages apparently in cipher',
    correspondents='unknown', place='Germany', language='German', region='Germany', period='1701-1800',
    shelfmark='Beinecke, GEN MSS FILE 413', folio_note='24 pp.; "several pages apparently in cipher"', cls='C',
    status='Catalogue note. Not digitised, not on DECODE.', why='Folk-magic charms hidden in cipher (a Sator square in the same book).',
    importance=1, solvability=2, difficulty=2, verify='Request scans.',
    links=[{'label': 'Quicksearch record', 'href': QS + '9985863163408651'}], source=B))
R.append(row(year=1863, date='30 Dec 1863', title='J. M. Morris → "Sister Hatty", Minersville, California, letter in a colour cipher',
    correspondents='J. M. Morris → Hatty (sister)', place='Minersville, California', language='English',
    region='Americas', period='1801-1900', shelfmark='Beinecke, Peter E. Palmquist papers, WA MSS S-2965, Box 176',
    folio_note='letter "in color cipher"', cls='C', status='Archives at Yale title. Not digitised, not on DECODE.',
    why='An unusual colour-based private cipher from a Civil War-era California mining camp.',
    importance=1, solvability=2, difficulty=3, verify='Request a scan of box 176.',
    links=[{'label': 'Quicksearch archives search', 'href': QA + '%22color+cipher%22'}], source=B))
R.append(row(year=1878, date='5 Feb 1878', title='Latham & King, San Francisco → Carson Bank, enciphered telegram',
    correspondents='Latham & King (brokers) → Carson Bank, Carson City', place='San Francisco', language='English',
    region='Americas', period='1801-1900', shelfmark='Beinecke, WA MSS S-2457 L346', folio_note='1 leaf', cls='C',
    status='Catalogue only. Not digitised, not on DECODE. Probably a commercial code (Comstock mining-stock trading).',
    why='Comstock-era banking telegram in a private commercial code.',
    importance=1, solvability=2, difficulty=3, verify='Request a scan; check 1870s telegraph code books.',
    links=[{'label': 'Quicksearch record', 'href': QS + '9962190273408651'}], source=B))
for yr, d, t, box, why, region, period in [
    (1597, '12 Jan 1597', 'Philip II of Spain, item filed under "Codes and Ciphers"', 'Box 48 Oversize', 'A cipher item of Philip II from the last years of the reign.', 'Spain', '1589-1598'),
    (1548, '1548', 'Emperor Charles V, item filed under "Codes and Ciphers"', 'Box 17', 'A Charles V cipher item of the Interim year.', 'Spain', '1497-1559'),
    (1623, '1623', 'Cardinal Richelieu, item filed under "Codes and Ciphers"', 'Box 17', 'An early Richelieu cipher item.', 'France', '1611-1650'),
    (1750, '18th century', 'Substitution cipher, filed under "Codes and Ciphers"', 'Box 17', 'An unidentified 18th-century substitution cipher.', 'Other', '1701-1800')]:
    R.append(row(year=yr, date=d, title=t + ' (Pforzheimer intelligence collection)', correspondents='unknown', place='unknown',
        language='unknown', region=region, period=period,
        shelfmark=f'Beinecke, Walter L. Pforzheimer papers, GEN MSS 817, {box} (Historical Manuscripts > Codes and Ciphers)',
        folio_note="collector's item; may be a letter in cipher or a key", cls='C',
        status='Archives at Yale title only. Not digitised (9 GEN MSS 817 items are, none of these). Not on DECODE.',
        why=why, importance=2 if yr == 1750 else 3, solvability=1, difficulty=3,
        verify='Open the component on Archives at Yale; if ciphertext, request scans; Spanish keys of 1548 and 1597 are on DECODE and cryptiana.',
        links=[{'label': 'Quicksearch archives search', 'href': QA + 'Pforzheimer+cipher'}], source=B))

# Folger
R.append(row(year=1645, date='27 Apr 1645', title='George, Lord Digby → Prince Rupert (or Maurice), Oxford, catalogued as a cryptogram',
    correspondents='George Digby, 2nd Earl of Bristol → Prince Rupert (or Prince Maurice)', place='Oxford', language='English',
    region='England', period='1611-1650', shelfmark='Folger Shakespeare Library, X.c.125 (MS Add 1285)',
    folio_note='bifolium; genre term "Cryptograms"', cls='B',
    status="Folger catalogue tags it \"Cryptograms\" (the notes do not mention cipher). Docket: Cromwell took Bletchington House; the King wants Rupert to march to Oxford. Not on DECODE. The repo's targets/rupert and rupert1645 hold 1644-45 royalist keys (Lasry SP106 keys; Digby-coach keys).",
    why='Royal headquarters to Rupert in the weeks before Naseby.',
    importance=4, solvability=2, difficulty=2,
    verify="Compare with Warburton, Memoirs of Prince Rupert (1849) iii, which prints a Digby letter of 27 April 1645; Folger images sit behind a Cloudflare Turnstile check, so ask the Folger for scans; try Lasry's SP106 keys.",
    links=[{'label': 'Folger catalogue', 'href': FC + '184910'}], source=F,
    prior_art="possibly in print (Warburton 1849 prints Digby's letter of 27 Apr 1645; not compared)"))
R.append(row(year=1665, date='1639?-1689', title='Goodricke family of Ribston Hall papers: one letter partly in cipher',
    correspondents='Sir John / Sir Henry Goodricke and correspondents', place='Yorkshire / London / Tangier', language='English',
    region='England', period='1651-1700', shelfmark='Folger Shakespeare Library, V.b.333 (1-39)',
    folio_note='39 items in a volume; which item is in cipher not stated', cls='C',
    status='Catalogue: "Another letter is partially written in cipher". Not on DECODE, not in repo.',
    why='Royalist and Restoration family papers (Sir Henry Goodricke was envoy to Spain, 1678-82).',
    importance=2, solvability=1, difficulty=3, verify='Ask the Folger which item; request a scan.',
    links=[{'label': 'Folger catalogue', 'href': FC + '232776'}], source=F))
R.append(row(year=1662, date='c. 1662', title='Mary Smith\'s culinary and medicinal recipe book, catalogued "Ciphers (codes)"',
    correspondents='Mary Smith (owner)', place='England', language='English', region='England', period='1651-1700',
    shelfmark='Folger Shakespeare Library, V.a.682', folio_note='tête-bêche volume, leaves 1-149; where the cipher is not stated', cls='C',
    status='Catalogue genre term "Ciphers (codes)"; notes do not say where. Not on DECODE.',
    why='Household recipe cipher, minor.', importance=1, solvability=2, difficulty=2,
    verify='Check Folger digital images (if reachable) for the cipher leaf.',
    links=[{'label': 'Folger catalogue', 'href': FC + '353749'}], source=F))
R.append(row(year=1625, date='1616-1634', title="Hawarden sessions orders on former end-leaves of Dalton's Countrey Justice: one note in cipher (leaf 1r)",
    correspondents='unknown (Cheshire / Flintshire owner; Peter Wilbraham?)', place='Flintshire / Cheshire', language='English',
    region='England', period='1611-1650', shelfmark='Folger Shakespeare Library, X.d.542 (MS Add 908)', folio_note='leaf 1r, one aphorism in cipher',
    cls='C', status='Catalogue note. Not on DECODE.', why='Minor private cipher note.',
    importance=1, solvability=2, difficulty=1, verify='Request a scan of leaf 1r.',
    links=[{'label': 'Folger catalogue', 'href': FC + '128984'}], source=F))

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'candidates.json')
with open(out, 'w', encoding='utf-8') as fh:
    json.dump(R, fh, ensure_ascii=False, indent=1)
print(len(R), 'rows')
