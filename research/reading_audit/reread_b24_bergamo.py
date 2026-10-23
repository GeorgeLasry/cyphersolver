"""Re-read brief (REREAD_BRIEF.md), batch b24: bergamo1585 (R16). Targeted profile edits, one save per change.
    python research/reading_audit/reread_b24_bergamo.py
Helpers: b24_fetch.py, b24_bg_line.py (line crops), b24_bg_fix.py (corrections), b24_bg_decode.py (beam decode with the
full Meister key), b24_bg_check.py (word check)."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from relabel_r0 import load, save  # noqa: E402
T = 'bergamo1585'


def put(path, value):
    p = load(T); o = p
    for k in path[:-1]: o = o[k] if not isinstance(k, int) else o[k]
    o[path[-1]] = value; save(T, p)


p = load(T); e = p['outcome']['texts'][0]; e.pop('note', None); e['state'] = 'read'; save(T, p)
for k, v in [
    ('transcription', ['R16_transcription_decode.txt', 'R16_transcription_corrected.txt', 'R16_corrections.tsv']),
    ('decryption', ['R16_decode_b24.txt', 'R16_decryption.txt']),
    ('reading', 'R16_reading.md'), ('translation', 'R16_en.md'),
    ('label', 'R16, Francia 18/2, f. 206r-v, 7 March 1586'),
    ('summary', "The nuncio in Paris to Rome, 7 March 1586: Guise sends word through the Ferrarese ambassador that the King means to make peace with the heretics once he has the money from the sale under the bull, and that he will never consent; Guise would accept the peace for Metz and a good sum of money; the King's heart does not match his show of confidence, and Guise is about to leave; the clergy's congregation, discontent with the alienation, inclines to appeal to a future council; the nuncio offers to send their letters in his cipher."),
    ('reading_review', {'grade': 'B', 'by': 'Claude Opus 5.5', 'date': '2026-10-22', 'note': "Read 23 Oct 2026 (b24): the DECODE record's attachment D3195 is Meister p. 324-325 with the whole Ragazzoni nomenclator (mark families x4+, stroked x4, hooked x6, x8+, struck x0, dotted x4), never read before; the old decoder also ate the 8 of 84+, 86ꜧ, 80- as a null. Beam decode with the it-cinquecento model (b24_bg_decode.py) on TimB's transcription with 16 labels corrected on the images (R16_corrections.tsv); 29 = et per Meister. Every word carried by the figures (b24_bg_check.py: 428 words, one, Ferrara, carried by a group the beam dropped and the image shows); 5 letters rest on a look-alike (si [?e], [?ocorendo], [?l'aleenatione], [?fata], [?vedo]). Body 0.757 clean (28/37), explicit holes 1.00. Open: [?futurum] (an abbreviation the key lacks) and the last eleven digits. The heading is 7 (not 3) March 1586."}),
]:
    p = load(T); p['outcome']['texts'][0][k] = v; save(T, p)
p = load(T); p['documents'][0]['read'] = 'read'; save(T, p)
for k, v in [
    ('class', 'read'), ('method', 'read with known key'),
    ('method_basis', "R16 read with the Ragazzoni key: Lasry's F18 letter alphabet (DECODE D3103/D3105) and the whole nomenclator printed by Meister (1906) p. 324-325 no. 2, which the DECODE record carries as attachment D3195; 16 transcription labels corrected on the images (b24, 23 Oct 2026). R15 had already been read by Lasry (2020)."),
    ('key', 'recovered'),
    ('key_file', ['key_F18_lasry.txt', 'meister324_nomenclator.txt', 'key_ragazzoni_meister_full.txt']),
    ('codes_open', {'open': 0}),
    ('gaps', [{'item': "R16 '[?futurum]' (futu + a dotted 3 and 9) and the last eleven digits of f. 206v", 'blocker': 'no-key-material', 'detail': 'neither is in Meister\'s table; the tail sits before the signature flourish and gives no word'},
              {'item': "R16 five letters on look-alike digits (si [?e], [?ocorendo], [?l'aleenatione], [?fata], [?vedo])", 'blocker': 'illegible', 'detail': 'the writer\'s 5 closes like an 8 and his 7 takes a hook; read on the DECODE images, the alternative gives no word'}]),
    ('notes', "R15 read before (Lasry). R17 was split off to morosini1588 on 14 Oct 2026. 22 Oct 2026, reading audit: R16 relabelled decoded, not read (run-on decode). 23 Oct 2026 (b24): R16 read with the whole Meister nomenclator (DECODE attachment D3195), 16 labels corrected on the images; 18 and 48 were not open codes but decoder misparses (18 = Duca di Ferrara after 70 'Ambasciatore di' fits; 48 was 'uers[o]' misread); body 0.757 clean."),
]:
    p = load(T); p['outcome'][k] = v; save(T, p)
for s in [
    {'date': '2026-10-23', 'kind': 'access', 'what': "Re-read (REREAD_BRIEF, b24): DECODE R15 and R16 fetched with the shared cookie. R16 carries attachments never opened before: D3195, a PDF of Meister p. 324-325 with the whole Ragazzoni nomenclator (names, the x4+, stroked x4, hooked x6, x8+, struck x0 and dotted x4 families); D984-D987, the clear covering letter of Paris 7 March 1586 ('con cifra duplicata'), not a decipherment; D1792, TimB's transcription again.", 'result': 'worked'},
    {'date': '2026-10-23', 'kind': 'key from source', 'technique': ['manual reconstruction'], 'what': "Full nomenclator transcribed from D3195 (key_ragazzoni_meister_full.txt). 29 = et (Meister) replaces Lasry's 'che'; 26 with the hook = che/chi. DECODE's '2+' is the stroked 4 (14 Sua Santita, 24 Sua Maesta), its '3^. 4' the dotted 34 (Heretici).", 'result': 'worked'},
    {'date': '2026-10-23', 'kind': 'solver', 'technique': ['beam/DP decoding', 'language-model scoring'], 'what': "b24_bg_decode.py: beam search over the token stream with the it-cinquecento model; a lone 8 is null only when it does not begin a marked code (84+ denari, 86ꜧ come, 80- mente were eaten as nulls by decode_with_key.py). 'con gli 48' becomes 'con gli Heretici come prima', 'il cuore di 22+' 'il cuore di Sua Maesta'.", 'result': 'worked'},
    {'date': '2026-10-23', 'kind': 'transcription', 'what': "Breaks checked on line crops of the DECODE images (b24_bg_line.py): 16 labels corrected (R16_corrections.tsv), e.g. l.4 1? = 7 ('fermo'), l.34 'uers·48' = 'uerso' and 'ogni', l.42 0^. = 0 ('resistere'), l.44 a dotted 0 ('congreg.'); five are look-alikes (5 closed like 8, 7 with a hook). Heading 7 (not 3) March 1586.", 'result': 'worked'},
    {'date': '2026-10-23', 'kind': 'reading', 'what': "R16_reading.md and R16_en.md written on the figures (words divided, v for the key's u|v, the clerk's spelling kept); word check: 428 words all carried (b24_bg_check.py). _check_reading.py on the body 0.757 (28/37); before 0.00. Set read, grade B.", 'result': 'worked'},
]:
    p = load(T); p['solution'].append(s); save(T, p)
print('ok')
