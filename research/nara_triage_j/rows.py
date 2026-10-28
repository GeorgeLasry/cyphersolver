"""Write candidates.json for NARA triage slice J (27 Oct 2026): RG 24, RG 29, RG 64. Rows are grounded in the hits named."""
import json, os

SRC = 'NARA bulk_all triage J'
CAT = 'https://catalog.archives.gov/id/'
MEDIA = 'https://catalog.archives.gov/medialz/dc-metro/rg-064/517920038/M1486/M1486-0083/M1486-0083-'
rows = [
    {
        'year': 1895, 'date': '1888-1910 (dated pieces 1891, 1895, 1897, 1902, 1904, 1906, 1910)',
        'title': 'Russian Foreign Ministry cipher circulars to the Imperial Russian Consulate General, New York, with the consulate\'s keys, 1888-1910',
        'correspondents': 'Ministry of Foreign Affairs, St Petersburg (I Expédition / First Department; Obolensky, Shishkin as Adjoint) → Russian Consul General, New York (Olarovsky, Lodyzhensky)',
        'place': 'St Petersburg → New York', 'language': 'Russian or French (cover text French; plaintext unknown)',
        'region': 'Other', 'period': '1801-1900',
        'shelfmark': 'NARA, RG 64 (microfilm M1486, Records of the Russian Consulates in the U.S., 1862-1922), roll 83, target 2 "Cables and Coded Communications, 1893-1910" (original: Russian Consulate New York, box 124); file unit naId 571170362',
        'folio_note': 'Roll 83 frames 0692-1550 (target 2 starts at frame 0692). Ciphertext circulars in 2-digit bigram-key groups: f.0696-0697 (15 Dec 1906), 0698 (10 Mar 1910, No. 63637), 0712 (18 Jun 1902, No. 281), 0732 (1895, No. 4945), 0742-0743 (No. 416), 0749 (1891, No. 3313), 0751-0752 (13 Aug 1891, No. 3902, c. 330 groups, viewed: clean, no interlinear), 0755-0757 (22 Mar 1895, No. 5078), 0769-0770 (10 Mar 1895, No. 5015), 0774 (31 Dec 1904, No. 1201), 0818-0820 (May/Jul 1897, Nos. 5657, 5700), 0823, 0835-0836, 0842, 0847, 0849; the consulate\'s replies in cipher f.0733-0735 (No. 519, 1895, Olarovsky); 5-digit secret circular No. 864 "aux Ambassades, Légations, Consulats" f.0703-0705 (c. 350 groups, viewed: clean, groups split by hand into 3-figure parts); 5-digit cables f.0694 (cable No. 63, 22 Oct 1908), 0800-0801, 0880-0882 (Oustinoff); naval-ministry letter cipher f.0805-0807 (5-letter groups with a repeating 2849284928... key line and Russian clear text: decrypted). Key material on the same roll: instructions and worked examples for the bigram keys No. 381 (1893; f.0780-0793) and No. 389 (1900; f.0713-0727, with the 12 Dec 1865 "Pesth" example in plaintext, transposition sheet and cipher), circular on key No. 400 (1905; f.0731), additions to the dictionary key No. 402 (1910; f.0728, 0802-0803), lozungi to recipher key No. 448 "Lambda" (1915; f.0869), rules on keeping keys (f.0759-0764), Naval Ministry cipher No. 383 (f.0863-0865) and Naval key No. 394 instructions plus dictionary (f.0884-0900, 0928-1073), and decode tables (f.1088-1550, "Разборная таблица No. 404" f.1443).',
        'cls': 'A',
        'status': 'Found in the RG 64 bulk_all hits (frames with 2-digit groups in a Russian consulate file); full roll OCR read and two frames viewed (0703, 0751). Some circulars carry the consulate\'s letter-by-letter decipherment worksheets on the following frames (f.0706-0711 after No. 864; 0758, 0772, 0776, 0794-0796, 0822-0825, 0837), so part of the run was read at the time; others show no worksheet in the OCR of the adjacent frames (1891 No. 3902, 1895 Nos. 4945 and 5078, 1906, 1910). The cipher system is described in full on the roll (bigram table + transposition "transparents" Lit. A/B/D; 3-figure values regrouped in 5s for the telegraph), and keys 381/389 come with plaintext-ciphertext examples. Not on DECODE; known.py: no hit for M1486, Olarovsky, Russian Consulate. Not in catalogue.json or any nara_* folder.',
        'why': 'A run of tsarist Foreign Ministry cipher circulars to a consulate, filed with the consulate\'s own key instructions and worksheets: rare primary evidence of Russian diplomatic bigram ciphers and naval codes of 1890-1910, and the unread circulars can be tested against keys and worked examples on the same roll.',
        'importance': 3, 'solvability': 4, 'difficulty': 3,
        'score_note': 'Scored from the roll OCR (fetched 27 Oct 2026) and two viewed frames during the Oct 2026 NARA bulk_all triage (research/nara_triage_j/)',
        'verify': 'View frames 0692-1100 of M1486 roll 83; pair each cipher circular with any worksheet; check whether the bigram tables for keys 356/375/381/389/400 are filmed (only instructions and examples were seen in the OCR) or can be rebuilt from the worked examples and the read circulars; check Soboleva, "Tainopis v istorii Rossii" (1994) and Russian MFA cipher studies for these keys.',
        'links': [{'label': 'NARA file unit 571170362 (M1486 roll 83)', 'href': CAT + '571170362'},
                  {'label': 'Circular No. 3902, 13 Aug 1891 (f.0751)', 'href': MEDIA + '0751.tif'},
                  {'label': 'Secret circular No. 864 (f.0703)', 'href': MEDIA + '0703.tif'}],
        'seen': 'image', 'source': SRC,
        'prior_art': 'open (checked 27 Oct 2026: known.py, catalogue.json, nara_* sweep folders, web search for M1486 cipher material: nothing found beyond FamilySearch roll listings)',
    },
]

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'candidates.json')
with open(out, 'w', encoding='utf-8', newline='\n') as f:
    f.write(json.dumps(rows, ensure_ascii=False, indent=2) + '\n')
print(len(rows), 'rows ->', out)
