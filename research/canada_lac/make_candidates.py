"""Build candidates.json for the LAC / Canadian-manuscripts sweep (28 Oct 2026).
Rows come from the New France Archives database (nouvelle-france.org; nfa.py, nfa_details.py, nfa_scope.json)
and the McGill AtoM catalogue (atom.py)."""
import json, os

here = os.path.dirname(os.path.abspath(__file__))
NF = 'https://nouvelle-france.org/eng/item/details?id='
SN = ('Scored from the archive description during the Oct 2026 LAC / Canadian manuscripts sweep (research/canada_lac/); '
      'not viewed (LAC image server central.bac-lac.gc.ca returned 503 to scripts)')
PA = ('open (checked 28 Oct 2026: known.py, web search for Vaudreuil/Beauharnois/New France ciphers; '
      'no published decipherment found)')
SRC = 'New France Archives (nouvelle-france.org, LAC/ANOM) sweep'


def nf(year, date, title, corr, place, shelf, folio, cls, status, why, imp, sol, dif, verify, nid, prior=PA):
    return dict(year=year, date=date, title=title, correspondents=corr, place=place, language='French',
                region='Americas', period='1701-1800', shelfmark=shelf, folio_note=folio, cls=cls, status=status,
                why=why, importance=imp, solvability=sol, difficulty=dif, score_note=SN, verify=verify,
                links=[{'label': 'New France Archives record (images)', 'href': NF + str(nid)}],
                seen='catalogue', source=SRC, prior_art=prior)


UNREAD = ('Title only ("Lettre chiffrée ... au ministre"), no content summary, unlike the deciphered despatches '
          'around it: the ANOM/LAC describers apparently could not read it. Not on DECODE, not in repo.')
KEY = ('Key lead: "Chiffre ou code de Montcalm et de Vaudreuil" 1757-58, ANOM COL C11E 10 ff.285-290v '
       '(nouvelle-france.org id 15213, 10 images); Vaudreuil acknowledged receiving the ministry cipher '
       '22 Sept 1756 (C11A 101 f.105).')
VER = ('View images on nouvelle-france.org (LAC image server; retry or use a browser); check the LAC C11A '
       'transcript reels on heritage.canadiana.ca ("Archives des Colonies: Série C 11 A (transcrits)", reels '
       'C-2380 ff.) for a deciphered copy; then test the C11E 10 key.')
SUMM = ('Content summary in the ANOM/LAC description is detailed, so a decipherment probably exists on the page '
        '(interlinear) or was made in the minister\'s bureau; likely read at the time. Not on DECODE, not in repo.')

rows = [
    nf(1759, '8 Apr 1759', 'Vaudreuil → the minister (Berryer), cipher letter, Montréal, eve of the Quebec campaign',
       'Pierre de Rigaud de Vaudreuil de Cavagnial → minister of the Marine', 'Montréal',
       'ANOM, COL C11A 104, ff.54-66 (CABAC_PIAF_60891)', '13 images; whole letter described as "chiffrée"', 'B',
       UNREAD + ' ' + KEY,
       "The governor-general's secret despatch on the defence of Canada in spring 1759, before Wolfe's siege of Quebec.",
       4, 3, 3, VER, 27478),
    nf(1759, '10 Apr 1759', 'Vaudreuil → the minister, cipher letter, Montréal',
       'Pierre de Rigaud de Vaudreuil de Cavagnial → minister of the Marine', 'Montréal',
       'ANOM, COL C11A 104, ff.68-72 (CABAC_PIAF_60892)', '5 images', 'B', UNREAD + ' ' + KEY,
       'Companion secret despatch of spring 1759 on the defence of the colony.', 4, 3, 3, VER, 27479),
    nf(1759, '16 Apr 1759', 'Vaudreuil → the minister, cipher letter, Montréal',
       'Pierre de Rigaud de Vaudreuil de Cavagnial → minister of the Marine', 'Montréal',
       'ANOM, COL C11A 104, ff.75-76 (CABAC_PIAF_60895)', '2 images', 'B', UNREAD + ' ' + KEY,
       'Third of the April 1759 ciphered despatches; short, a test case for the key.', 3, 3, 3, VER, 27482),
    nf(1760, '13 Aug 1760', 'Vaudreuil → the minister, cipher letter, Montréal, weeks before the capitulation',
       'Pierre de Rigaud de Vaudreuil de Cavagnial → minister of the Marine', 'Montréal',
       'ANOM, COL C11A 105, ff.147-152 (CABAC_PIAF_61062)', '6 images', 'B',
       UNREAD + ' ' + KEY + ' Possibly related to the "Vaudreuil to Berryer announcing in figures the loss of the '
       'colony" row in research/calames_biblissima (different series; check whether it is a copy).',
       'One of the last secret despatches from New France before the capitulation of Montréal (8 Sept 1760).',
       5, 3, 3, VER, 27665),
    nf(1759, '6 Nov 1759', 'Trémais → the minister, cipher letter, Montréal',
       'Charles-François Pichot de Querdisien Trémais (commissaire sent to audit Bigot) → minister of the Marine',
       'Montréal', 'ANOM, COL C11A 104, ff.346-347v (CABAC_PIAF_60950)', '3 images', 'B',
       UNREAD + " Trémais was sent in 1758 to investigate the Bigot frauds; his cipher may differ from Vaudreuil's.",
       'Secret report of the investigator behind the "Affaire du Canada" (Bigot trial), just after the fall of Quebec.',
       4, 3, 3, VER, 27542),
    nf(1757, '22 Oct 1757', 'Drucourt and Prévost → the minister, cipher despatch, Louisbourg, plan to destroy Halifax',
       'Augustin de Boschenry de Drucourt and Jacques Prévost de La Croix → minister of the Marine', 'Louisbourg',
       'ANOM, COL C11B 37, f.25-25v (CABAC_PIAF_179777)', '2 images', 'A',
       'Description gives a short content summary ("moyens de détruire ... les nouveaux bâtiments ... à Halifax"), '
       'so it was probably deciphered at the time; check whether the decipherment is on the page. '
       'Not on DECODE, not in repo.',
       "Île Royale's secret plan against Halifax the year before the fall of Louisbourg.", 3, 3, 3, VER, 12539),
    nf(1740, '1 Dec 1740', 'Duquesnel → the minister, cipher despatch on the defence of Île Royale',
       'Jean-Baptiste-Louis Le Prévost Duquesnel → minister of the Marine', 'Louisbourg',
       'ANOM, COL C11B 22, ff.98-101 (CABAC_PIAF_178338)', '8 images', 'A',
       '"Dépêche chiffrée concernant la défense de l\'Ile Royale"; one-line summary only. Not on DECODE, not in repo.',
       "Louisbourg defence planning before King George's War.", 3, 3, 3, VER, 11102),
    nf(1740, '3 Aug 1740', 'Bourville → the minister, cipher despatch on measures in case of war with England',
       'François Le Coutre de Bourville → minister of the Marine', 'Louisbourg',
       'ANOM, COL C11B 22, ff.114-115v (CABAC_PIAF_178343)', '4 images', 'A',
       '"Dépêche chiffrée concernant les mesures à prendre en cas d\'une rupture avec l\'Angleterre"; one-line '
       'summary only. Not on DECODE, not in repo.',
       'Île Royale war contingency planning, 1740.', 2, 3, 3, VER, 11107),
    nf(1734, '28 Oct 1734', 'Saint-Ovide → the minister, cipher despatch on a coming war with England',
       'Joseph de Monbeton de Brouillan dit Saint-Ovide → minister of the Marine', 'Louisbourg',
       'ANOM, COL C11B 15, ff.121-138v (CABAC_PIAF_177772)',
       '35 images; note: "Les folios 137-138v ne sont pas transcrits"', 'A',
       SUMM + ' Beauharnois received the same ministry cipher for correspondence with Saint-Ovide '
       '(C11A 61 f.282, 30 Sept 1734).',
       'Long secret memorandum proposing an offensive against Port Royal and Placentia; ff.137-138v untranscribed.',
       3, 3, 3, VER, 10538),
    nf(1744, '15 Apr 1744', 'Beauharnois → the minister, cipher letter on the western posts and English designs',
       'Charles de Beauharnois de La Boische → minister of the Marine (Maurepas)', 'Montréal',
       'ANOM, COL C11A 81, ff.114-116v (CABAC_PIAF_48349)', '4 images', 'A', SUMM,
       "Governor's secret correspondence at the outbreak of King George's War.", 2, 3, 3, VER, 23886),
    nf(1744, '20 Apr 1744', 'Beauharnois → the minister, cipher letter on the Iroquois and the English at Oswego',
       'Charles de Beauharnois de La Boische → minister of the Marine', 'Montréal',
       'ANOM, COL C11A 81, ff.117-118v (CABAC_PIAF_48350)', '3 images', 'A', SUMM,
       'Iroquois diplomacy, 1744.', 2, 3, 3, VER, 23887),
    nf(1744, '30 Jun 1744', 'Beauharnois → the minister, cipher letter on defence measures after the declaration of war',
       'Charles de Beauharnois de La Boische → minister of the Marine', 'Montréal',
       'ANOM, COL C11A 81, ff.122-125v (CABAC_PIAF_49517)', '5 images', 'A', SUMM,
       "Canada's war measures, 1744.", 2, 3, 3, VER, 25047),
    nf(1744, '15 Oct 1744', 'Beauharnois → the minister, two cipher letters sending the militia census',
       'Charles de Beauharnois de La Boische → minister of the Marine', 'Québec',
       'ANOM, COL C11A 81, ff.174-176v (CABAC_PIAF_48355 and 48356)', '3 + 2 images', 'A',
       SUMM + ' Two letters of the same date (nouvelle-france.org ids 23892, 23893).',
       'Militia strength of New France, 1744.', 2, 3, 3, VER, 23892),
    nf(1745, '18 Jun 1745', 'Hocquart → the minister, cipher letter on the Boston expedition against Louisbourg',
       'Gilles Hocquart (intendant) → minister of the Marine', 'Québec',
       'ANOM, COL C11A 83, ff.164-170v (CABAC_PIAF_49633)', '8 images', 'A', SUMM,
       "Intendant's secret report during the 1745 siege of Louisbourg.", 3, 3, 3, VER, 25163),
    nf(1745, '21 Jun 1745', 'Hocquart → the minister, cipher letter on the consequences of the attack on Île Royale',
       'Gilles Hocquart → minister of the Marine', 'Québec',
       'ANOM, COL C11A 83, ff.171-172v (CABAC_PIAF_49634)', '3 images', 'A', SUMM,
       'Same, 1745.', 2, 3, 3, VER, 25164),
    nf(1745, '4 Nov 1745', 'Beauharnois → the minister, cipher letter expecting an English attempt on Canada in 1746',
       'Charles de Beauharnois de La Boische → minister of the Marine', 'Québec',
       'ANOM, COL C11A 83, ff.114-118 (CABAC_PIAF_48496)', '5 images', 'A',
       SUMM + ' Sibling with decipherment: Beauharnois & Hocquart 31 Oct 1746, "Lettre chiffrée, traduite", '
       'COL C11D 8 ff.119-127v (id 7665), a crib for the 1744-46 key.',
       "Governor's secret warning after the loss of Louisbourg.", 3, 3, 3, VER, 24031),
    dict(year=1892, date='1891-1892',
         title='G. M. Dawson correspondence with A. P. Sherwood and C. H. Tupper (Bering Sea / Alaska boundary), '
               'file matching "cypher"',
         correspondents='George Mercer Dawson ↔ A. P. Sherwood, C. H. Tupper and others',
         place='Victoria; London; Ottawa', language='English', region='Americas', period='1801-1900',
         shelfmark='McGill University Archives, Dawson-Harrington Families Fonds, MG1022-6-126 (Bundle 5-B)',
         folio_note='20 letters, digitised PDF (49.9 MB); "cypher" matches the OCR text, place unknown',
         cls='C',
         status='McGill AtoM full-text hit for "cypher" and "cipher"; the description does not mention a cipher. '
                'Could be a cypher telegram or only the word. Not on DECODE, not in repo.',
         why='Possible Colonial Office cypher telegram text from the Bering Sea preparations; probably minor.',
         importance=1, solvability=2, difficulty=2,
         score_note='Scored from the catalogue hit during the Oct 2026 LAC / Canadian manuscripts sweep '
                    '(research/canada_lac/); not viewed',
         verify='Open the PDF and search for the cypher passage; it may be a deciphered telegram or a mention only.',
         links=[{'label': 'McGill record',
                 'href': 'https://archivalcollections.library.mcgill.ca/index.php/correspondence-from-victoria-london-etc'},
                {'label': 'PDF',
                 'href': 'http://digitalarchives.library.mcgill.ca/MUA/MG1022/series6/mua_dawson_fonds_MUAMG1022-6-126.pdf'}],
         seen='catalogue', source='McGill Archival Collections (AtoM) sweep', prior_art='not checked (importance 1)'),
]
json.dump(rows, open(os.path.join(here, 'candidates.json'), 'w', encoding='utf8'), ensure_ascii=False, indent=2)
print(len(rows))
