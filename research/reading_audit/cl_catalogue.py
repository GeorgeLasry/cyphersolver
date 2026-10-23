"""cl consistency pass (23 Oct 2026): catalogue.json entries for targets that no longer read anything after the reading
audit (class not read). An entry taken out of the open catalogue when its target was first claimed read is restored
from git history (its last version before removal), narrowed to the target's own letters where the entry was wider,
and marked 'attempted, open'; entries still present that call such a target read are corrected.

    python research/reading_audit/cl_catalogue.py <restore_src.json>

restore_src.json: {id: last historic version} (from `git log --first-parent -- catalogue.json`).
"""
import json
import sys
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[2]
AS_OF = '2026-10-23'
AUDIT = ('Reading audit 22-23 Oct 2026 (George Lasry\'s test: a reading must build sentences): ')

src = {int(k): v for k, v in json.loads(pathlib.Path(sys.argv[1]).read_text(encoding='utf8')).items()}

R = {}   # id -> dict of field overrides (plus 'slug')

R[30] = dict(
    slug='champagne1590', counted=True,
    year=1590, date='Jun 1590; 1591',
    title='Champagne news-letters to Nevers, June 1590 (fr. 3623 nos. 24, 25, 60) and no. 78',
    correspondents='anonymous (Champagne) → duc de Nevers',
    place='Champagne → Nevers', shelfmark='BnF fr. 3623 nos. 24, 25, 60, 78', ark='btv1b525245007',
    folio_note='Restored 23 Oct 2026. No. 23 (Bienvenut) is bienvenut1590 and Laurière\'s letters are lauriere1593, each a different key.',
    seen='image',
    status=('Attempted 21 Sept 2026 (targets/champagne1590/): the two-digit alphabet of nos. 24, 25 and 60 (one hand, June 1590) '
            'rebuilt from a few letters glossed over single figures and the alphabetical order of its values; 63 of 104 figures '
            'given a value. Taken out of the catalogue entry when first claimed read in part (21 Sept 2026; the entry, narrowed to Laurière, was removed 15 Oct 2026); restored 23 Oct 2026: ' + AUDIT +
            'neither document builds sentences (short runs, six with codes without value), so nothing counts as read. '
            'No. 78 (1591) is one group of about six signs in another code.'),
    known='Two-digit alphabet of nos. 24/25/60 rebuilt from glossed figures (63 of 104 figures valued; champagne1590.html); no decipherment or clear copy found.',
    open=('Nos. 24/25/60: code numbers 12, 16, 17, 19, 39, 89, 99, the plain numbers of no. 24, two passages of no. 24, half the '
          'no. 25 passage, the name in no. 60; none builds sentences. Blocker: no key material. No. 78: too short.'),
    verify='Look for another letter of the same Champagne correspondent in the Nevers papers (fr. 3620-3625, fr. 3985-3995) with an interlinear decipherment; Tomokiyo\'s Nevers keys nos. 1-70 against the code numbers.',
)
R[17] = dict(
    slug='maisse1593', counted=True,
    year=1593, date='1593',
    title='Henri IV to Maisse (Venice), two letters (fr. 16093 ff. 406, 410)',
    shelfmark='BnF fr. 16093 ff. 406, 410',
    folio_note='Restored 23 Oct 2026 for ff. 406 and 410 only; ff. 370 and 373 (maisse1592) are deciphered from the existing decipherment.',
    seen='image',
    status=('Henri IV to Maisse, two letters in Tomokiyo\'s "Maisse\'s Cipher (1592-1593)" (targets/maisse1593/). The content of both is known from '
            'contemporary clear copies in fonds Brienne 13 (BnF NAF 6984, ff. 171r and 193v), but neither copy is transcribed here. '
            'Removed from the catalogue when the four letters were first claimed solved (PR #7, 20 Sept 2026); restored 23 Oct 2026: ' + AUDIT +
            'no text of ff. 406 and 410 is in the repository, so nothing counts as read.'),
    known='Clear copies located in Brienne 13 (NAF 6984 ff. 171r, 193v; maisse1593.html). ff. 370 and 373 deciphered from the existing decipherment (maisse1592).',
    open='ff. 406 and 410: the Brienne 13 clear copies are not transcribed and not aligned with the cipher. Not attempted yet.',
    verify='Transcribe the two Brienne 13 copies (Gallica NAF 6984 canvases 176, 199) and align them with the cipher.',
)
R[21] = dict(
    slug='nevers1593, revol1593', counted=True,
    status=('Attempted 17 Sept 2026 (targets/nevers1593/, targets/revol1593/; split by key 15 Oct 2026). The two Pisany letters (fr. 3985 f. 209, '
            'fr. 3986 f. 168) decode with Tomokiyo\'s Nevers cipher no. 46 (390 of 391 groups given a value); the Revol letters are in the '
            'Court cipher no. 60 (fr. 3995 ff. 108-111), which gives three words on f. 88r and anchors on f. 146v. Removed from the catalogue '
            'when first claimed read in part; restored 23 Oct 2026: ' + AUDIT + 'no passage of either group builds sentences '
            '(f. 209 0.33 on explicit holes), so nothing counts as read.'),
    known='Key no. 46 fits the Pisany letters (nevers1593.html); key no. 60 identified for the Revol letters (revol1593.html); the 31 Aug Instruction is a double crib (Memoires de Nevers ii, 492-499).',
    open=('Pisany: f. 168 garbled stretches (illegible) and the copyist\'s wrong figures on f. 209. Revol: f. 146v (nine lines), f. 157v, '
          'f. 88r-v, f. 115, f. 176, f. 198 not transcribed or not decoded through.'),
    verify='Finish the glyph atlas of the copyist\'s forms from the interlined Instruction (atlas60.md), then transcribe and decode f. 146v, ff. 88, 176, 198 with key no. 60.',
)
R[11] = dict(
    slug='rennes1563', counted=True, seen='image',
    status=('Attempted 20 Sept 2026 (targets/rennes1563/): Tomokiyo\'s reconstruction of the Bishop of Rennes\' cipher (1561-64) applied with per-hand '
            'letter forms from the glossed siblings (fr. 3181 ff. 57-58, Colbert 390) and an LM lattice. Removed from the catalogue when first '
            'claimed read in part; restored 23 Oct 2026: ' + AUDIT + 'fr. 3181 f. 55 (0.50 clean sentences on explicit holes), Colbert 390 '
            'pp. 357-358 (0.27), p. 139 and Colbert 392 p. 231 (0.17) are decoded, not read: no letter reads.'),
    known='Tomokiyo\'s key fits after calibration on the glossed sibling f. 57 (rennes1563.html); La Ferrière 1885 prints f. 55 with the cipher left blank.',
    open=('All five ciphertexts: unread sign runs and slips in most sentences (fr. 3181 f. 55 ll. 2, 4, 8, 9, 12; Colbert 390 pp. 139, 357-358; '
          'Colbert 392 p. 231). Blocker: no key material beyond Tomokiyo\'s table and the glossed siblings.'),
    verify='Re-read the weak lines on the native-resolution IIIF crops against the glossed siblings; look for further glossed letters of the Rennes embassy in Colbert 390-392.',
    writeup='rennes1563.html',
)
R[36] = dict(
    slug='r1955', counted=True, seen='image',
    status=('DECODE R1955: transcribed in full 19 Sept 2026 (targets/michell1751/transcription_r1955.txt, own folder targets/r1955/ since 15 Oct 2026); '
            'ministerial rescript to Michell, 28 Dec 1751, 362 code groups (295 distinct), not in Politische Correspondenz. The envoy-code table '
            'rebuilt from the contemporary decipherments of Michell\'s reports R1050/R1051 matches it but values only 95 of 360 groups. '
            'Removed from the catalogue when first claimed read; restored 23 Oct 2026: ' + AUDIT + 'fragments, no sentences, so nothing counts as read.'),
    known='Envoy-code table from R1050/R1051 matches R1955 (95 of 360 groups valued; r1955.html).',
    open='265 of 360 groups without a value; no sentence builds. Blocker: no key material (needs more decipherments in this code).',
    verify='Look for further Michell reports of 1751-52 with contemporary decipherments (KHA Prins Willem V, DECODE neighbours of R1050-R1051) to extend the table.',
    writeup='r1955.html',
)
R[5] = dict(
    slug='raince', counted=True, seen='image',
    status=('Attempted 17 Sept 2026 (targets/raince/): Tomokiyo\'s 1526 key re-measured off his table image and applied glyph by glyph to the 13 May '
            '(pp. 29-31) and 20 Nov 1526 (p. 105) passages. Removed from the catalogue when first claimed read in part; restored 23 Oct 2026: ' + AUDIT +
            'the passages decode into clauses broken by unresolved stretches in nearly every line, so nothing counts as read. '
            'The other letters of the entry carry contemporary interlinear or printed decipherments (Mignet 1886, Bourrilly 1901, DECODE 3696); '
            'the open residue is the unglossed part of no. 7 (13 May) and of no. 24 (20 Nov).'),
    known='Tomokiyo\'s 1526 key fits after re-measuring (raince.html); the clear close of 13 May transcribed.',
    open='No. 7 (pp. 29-31) and no. 24 (p. 105), the unglossed lines: unresolved glyphs (~13% of letters) and two word signs absent from Tomokiyo\'s key; no sentence builds through.',
    verify='Re-read the unresolved glyphs of pp. 29-31 and p. 105 on full-resolution crops; collect the two word signs from the glossed letters nos. 6, 8, 10, 28.',
    writeup='raince.html',
)
R[131] = dict(
    slug='cobham1588', counted=True, seen='image',
    status=('Attempted 21 Sept 2026 (targets/cobham1588/): the key record R8497 is Bodley\'s 1590 cipher, not this one; about 20 letters of the alphabet '
            'rebuilt from the interlinear decipherments of Cobham\'s Mar-Apr 1588 letters in the same volume (R8488, R8493). Removed from the catalogue '
            'when first claimed read in part; restored 23 Oct 2026: ' + AUDIT + 'the four letters were re-read on the images (b13) and written out as '
            'partial readings; none builds cipher sentences beyond R8490\'s hostages passage, so nothing counts as read.'),
    known='Partial alphabet from the glossed siblings R8488, R8493 (cobham1588.html).',
    open=('R8490 (ff. 80r-v), R8492 (f. 88r), R8495 (f. 92r), R8496 (f. 96v): cipher runs undecoded, codes 22, 27; the clear text of f. 96r and the '
          'secretary-hand words not yet transcribed. Blocker: no key material beyond the partial alphabet.'),
    verify='Transcribe the clear text of f. 96r and the bracketed secretary-hand words; look for another glossed Cobham letter of May-June 1588 (Harley 287, CSP Foreign).',
)
R[172] = dict(
    slug='guise1587', counted=True, seen='image',
    status=('DECODE R4162 (f. 119, 27 May 1587) and R4165 (f. 142, 20 June 1587), letters to Mercœur in the cipher George Lasry solved in 2022 (key table '
            'on cryptiana GL.htm; no plaintext published). Applied sign by sign here 22 Sept 2026 (targets/guise1587/). Removed from the catalogue when '
            'first claimed read; restored 23 Oct 2026: ' + AUDIT + 'f. 119 (0.558 clean sentences after a full re-read) and f. 142 (0.167 on explicit holes) '
            'do not build sentences, so nothing counts as read.'),
    known='Lasry\'s 2022 key table, extended by about a dozen values, gives most letter signs a value (guise1587.html).',
    open='f. 119 ll. 00-03, 29-33 and the close; f. 142 ll. 00-02, 09-10, 13; homophone choices the context does not fix; name codes in Lasry\'s Unknown row. Blocker: no key material beyond Lasry\'s table.',
    verify='Ask George Lasry whether he holds a decipherment of ff. 119 and 142; compare with his f. 27 overlay for the nomenclator groups ffm, ffmm, fbn.',
    writeup='guise1587.html',
)
R[120] = dict(
    slug='harley1582r8499', counted=True, seen='image',
    title='Nicholas Wotton to Queen Mary, 13 June 1554',
    correspondents='Nicholas Wotton → Queen Mary',
    status=('DECODE R8499 (Harley MS 1582 ff. 8-10): Wotton to Queen Mary, 13 June 1554 (targets/harley1582r8499/). The key DECODE R354 (TNA SP 106/2 '
            'f. 162, "France 1554"), filed in another series, was matched and corrected over eight passes. Removed from the catalogue when first '
            'claimed read; restored 23 Oct 2026: ' + AUDIT + 'the decode leaves holes in most sentences, so nothing counts as read. The contemporary '
            'clear copy (Harley 1582 art. 2, ff. 5r-7v) is not digitised.'),
    known='Key DECODE R354 matched (harley1582r8499.html).',
    open='About 31% of non-null signs unread, tentative or not sense; about 40 rare code signs. Blocker: the clear copy needs the BL (not digitised).',
    verify='Get images of Harley 1582 ff. 5r-7v (the clear copy) and align them with the cipher.',
    writeup='harley1582r8499.html',
)
R[121] = dict(
    slug='harley1582r8505', counted=True, seen='image', decode_ids=[8505],
    status=('DECODE R8505 (Harley MS 1582 ff. 263-264): the French memoir "L\'Estat du Roy de Navarre & de son party en France", transcribed in full 22 Sept 2026 '
            '(~3,630 signs; targets/harley1582r8505/). The homophonic alphabet was rebuilt by annealing against a 1530-1600 French model. Removed from the '
            'catalogue when first claimed read; restored 23 Oct 2026: ' + AUDIT + 'three passes on the reading reach 0.53 clean sentences; f. 263r alone '
            'builds, so nothing counts as read. R8501, the other record first grouped here, is a Stafford 1586 letter (harley1582r8500).'),
    known='Homophonic sign alphabet recovered from the ciphertext alone; all clear text transcribed (harley1582r8505.html).',
    open='Ten nomenclator numbers (6, 21, 26, 36, 51, 57, 72, 81, 99, 721) and about 5% of the text illegible; most sentences keep holes. Blocker: no key material.',
    verify='Look for another copy of the memoir in clear (BnF Dupuy and fonds français League collections) to fix the nomenclator and the weak stretches.',
    writeup='harley1582r8505.html',
)
R[19] = dict(
    slug='ibarra1593', counted=True, seen='image',
    title='Diego de Ibarra, Spanish despatch of 1593 (fr. 3984 no. 68)',
    shelfmark='BnF fr. 3984 no. 68 (f. 145)',
    folio_note='Restored 23 Oct 2026 for no. 68 only; the Sessa and Miranda letters of the first entry are sessa1593 (deciphered in part with the office key).',
    status=('Attempted 19 Sept 2026 (targets/sessa1593/, own folder targets/ibarra1593/ since 15 Oct 2026): Tomokiyo\'s '
            'Feria-Mansfeld key, which cites this folio, decodes the syllabic figures, but the three-letter word codes that carry much of the sense '
            'have no table. Removed from the catalogue when the entry was first claimed read in part (PR #8); restored 23 Oct 2026: ' + AUDIT +
            'the letter does not build sentences, so nothing counts as read.'),
    known='Tomokiyo\'s Feria-Mansfeld key decodes the syllabic figures (ibarra1593.html).',
    open='374 of 598 groups unread, mostly three-letter word codes with no table. Blocker: no key material.',
    verify='Look for the word-code table among the Spanish keys of 1589-93 (Simancas, Tomokiyo) or another Ibarra letter with an interlinear decipherment.',
    writeup='ibarra1593.html',
)
R[15] = dict(
    slug='lorraine1592', counted=True,
    status=('Attempted 18 Sept 2026 (targets/lorraine1592/, PR #4): the reciprocal letter-pair key recovered from the ciphertext alone (Tomokiyo had broken '
            'it in 2025 without publishing a text); no. 22 is a plaintext decipherment of the January letter, with no cipher. Removed from the catalogue '
            'when first claimed solved; restored 23 Oct 2026: ' + AUDIT + 'no. 97 decodes into fragments with a gap in almost every line, so nothing counts as read.'),
    known='Letter-pair key recovered from the ciphertext alone (lorraine1592.html).',
    open='Special signs inside words (about 60 tokens), figures 57, 98, 122, 123, 13, 137, 88, 146, 121, 103, garbled runs L12, L13, L20; no sentence builds. Blocker: no key material; a key or duplicate may survive in the Lorraine ducal archive (AD Meurthe-et-Moselle).',
    verify='Re-read the 42 per-line crops with the recovered key to correct the barred, dotted and capital variants; ask AD Meurthe-et-Moselle for the ducal key.',
    writeup='lorraine1592.html',
)
R[57] = dict(
    slug='sp106box10', counted=True, seen='image', decode_ids=[660, 664],
    title='TNA SP 106/10: the codebreaker\'s "Venetian Cifer", c. 1623-24 (R664, R660)',
    correspondents='Unknown sender → unknown recipient (Venetian intercepts)',
    shelfmark='TNA SP 106/10 (DECODE R664, R660; grid R658)',
    status=('Attempted 20-21 Sept 2026 (targets/sp106box10/): about 45 values of the three-figure syllabic code aligned from the codebreaker\'s interlinear '
            'glosses on R664; his own grid R658 rebuilds the code as a systematic syllabary (102 values). The other records first grouped here have their own '
            'entries (R722 catalogue 66, R931 catalogue 58) or are worksheets. Removed from the catalogue when first claimed read in part; restored 23 Oct 2026: ' + AUDIT +
            'R664 is decoded, not read, and no group-by-group reading of R664/R660 exists.'),
    known='The codebreaker\'s grid R658 gives 102 values of the code (sp106box10.html).',
    open='R664 ff. 1-3 and R660: continuous reading not yet made (not attempted); groups 233, 312, 367, 439, 477, 534, 551, 556, 566 without a value; sender and recipient unknown.',
    verify='Transcribe R664 and R660 group by group and decode them through with the R658 grid.',
    writeup='sp106box10.html',
)


def restored(i):
    e = dict(src[i])
    ov = dict(R[i])
    ov.pop('slug')
    e.update(ov)
    e['outcome'] = 'attempted, open'
    e['as_of'] = AS_OF
    e.setdefault('known', '')
    e.setdefault('open', '')
    return e


f = ROOT / 'catalogue.json'
raw = open(f, encoding='utf8', newline='').read()
crlf = '\r\n' in raw
d = json.loads(raw)
E = d['entries']
have = {e['id'] for e in E}
for i in sorted(R):
    assert i not in have, i
    e = restored(i)
    pos = next((k for k, x in enumerate(E) if x['id'] > i), len(E))
    E.insert(pos, e)
    print('restored', i, R[i]['slug'])

# entries still present that count one of the targets as deciphered
byid = {e['id']: e for e in E}


def edit(i, field, old, new):
    s = byid[i][field]
    assert s.count(old) == 1, (i, field, old)
    byid[i][field] = s.replace(old, new)


# 9: Espagnol 318 nos. 92 and 94 back in the open entry
e = byid[9]
e['title'] = 'Espagnol 318 nos. 92, 93, 94: Ferdinand\'s secretariat ciphers (Great Captain 1500, Suárez de Figueroa 1504, viceroy of Sicily 1503)'
e['status'] = ('Widened again 23 Oct 2026 (' + AUDIT + 'no. 92 and no. 94 are decoded, not read, so they are back here). ' + e['status'])
e['open'] = (e['open'] + ' No. 92 (targets/esp318/): decoded with the Cifra general (Galende Díaz 1994), not yet built into sentences. '
             'No. 94 (targets/esp318no94/): Michael Brackx\'s key recovered ciphertext-only, about 90 code groups open; his decryption has holes in most sentences.')
e['as_of'] = AS_OF
# 336: Siena nos. 4, 14, 15 back among the open pieces
e = byid[336]
e['title'] = e['title'].replace('(nos. 7, 19, 21;', '(nos. 4, 7, 14, 15, 19, 21;')
assert 'nos. 4, 7, 14, 15, 19, 21' in e['title']
edit(336, 'status', 'nos. 20/23, 12, 6/24, 4, 14, 25, 11, 18, 17, 15, 5?, 9, 13/16, 10 and 8', 'nos. 20/23, 12, 6/24, 25, 11, 18, 17, 5?, 9, 13/16, 10 and 8')
e['status'] += (' 23 Oct 2026, ' + AUDIT + 'no. 4 (R4793, Borghesi 1456; targets/borghesi1456/), no. 14 (R4802; targets/siena14/) and no. 15 '
                '(R4803; targets/siena15/) are decoded, not read, and are back among the open pieces.')
e['open'] += (' No. 4 (R4793, 144 signs): key rebuilt from an alphabet fragment and the glosses, 114 signs given a value, no sentences. '
              'No. 14 (R4802): key recovered from the ciphertext alone, L01-L26 decoded, not read. No. 15 (R4803): partly deciphered by George Lasry by crib guessing (no key filed), decoded, not read.')
e['as_of'] = AS_OF
# 161: R9367 back among the open records
e = byid[161]
e['status'] += (' 23 Oct 2026, ' + AUDIT + 'R9367 (r9367, known key) is decoded, not read and is open again.')
edit(161, 'known', 'r9367 (known key, 55%)', 'r9367 (known key; decoded, not read since 23 Oct 2026)')
e['open'] += ' R9367 (r9367.html): decoded with the known key, does not build sentences.'
e['as_of'] = AS_OF
# 97: Throckmorton's 10 July 1559 letter back to open
e = byid[97]
edit(97, 'status', 'is read in part in targets/throck1559/', 'was deciphered in part in targets/throck1559/; since 23 Oct 2026 (' + AUDIT.rstrip(': ') + ') it is decoded, not read, and open again')
edit(97, 'known', 'deciphered about 85% here', 'decoded about 85% here (decoded, not read since 23 Oct 2026)')
e['open'] += ' The 10 July 1559 letter (throck1559): decoded with Cipher 1, does not build sentences.'
e['as_of'] = AS_OF

out = json.dumps(d, ensure_ascii=False, indent=1) + '\n'
if crlf:
    out = out.replace('\n', '\r\n')
open(f, 'w', encoding='utf8', newline='').write(out)
print('entries', len(E))
