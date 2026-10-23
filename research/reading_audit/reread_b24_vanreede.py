"""Re-read brief (REREAD_BRIEF.md), batch b24: vanreede1787 (R1026, R1027).

Targeted profile edits with the splice saver of relabel_r0.py; one save per change.

    python research/reading_audit/reread_b24_vanreede.py texts|documents|outcome|steps
Helpers: b24_fetch.py (DECODE record files to the scratchpad), b24_crop.py / b24_strips.py (zoomed image strips),
b24_vr_key.py (key R1024 with slips fixed and the null blocks), b24_vr_decode.py, b24_vr_build.py (corrected group
files, corrections, group-by-group decodes), b24_vr_align.py (word check, look-alike count), b17_score.py (body score).
"""
import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from relabel_r0 import load, save  # noqa: E402

T = 'vanreede1787'
REV = dict(by='Claude Opus 5.5', date='2026-10-22')


def mark_read(doc, fields, grade, note):
    p = load(T)
    e = [x for x in p['outcome']['texts'] if x.get('doc') == doc]
    assert len(e) == 1, doc
    e = e[0]
    e.pop('note', None)
    e['state'] = 'read'
    e.update(fields)
    e['reading_review'] = dict(grade=grade, **REV, note=note)
    save(T, p); print('read', doc)


def add_step(step):
    p = load(T)
    p['solution'].append(step)
    save(T, p); print('step')


def set_outcome(**kw):
    for k, v in kw.items():
        p = load(T)
        if isinstance(v, list) and len(v) > 1:
            p['outcome'][k] = v[:1]; save(T, p)
            for x in v[1:]:
                p = load(T); p['outcome'][k].append(x); save(T, p)
            continue
        p['outcome'][k] = v
        save(T, p)
    print('outcome', list(kw))


FIELDS = {
    'DECODE R1026': {
        'transcription': ['decode/DOC_R1026_D1852_1852.txt', 'R1026_transcription_corrected.tsv', 'R1026_corrections.tsv'],
        'decryption': 'R1026_decode_b24.txt', 'reading': 'R1026_reading.md', 'translation': 'R1026_en.md', 'language': 'fr',
        'summary': "Van Reede to Van de Spiegel, Berlin, 29 Dec 1787: the two ministers put the alliance project to the King; Hertzberg motivated his own view; a conference this morning; the King will not guarantee the Dutch possessions overseas; article seven struck out as disagreeable to England at Finckenstein's request; Hertzberg made the treaty temporary, twenty years. Clear passage: his audience on Wednesday, the King invites him to dine. Second cipher passage: the conference decided to say only that if the Republic is attacked by a European power the King will furnish the stipulated aid; he could get it stated more clearly if ordered."},
    'DECODE R1027': {
        'transcription': ['decode/DOC_R1027_D2299_2299.txt', 'R1027_transcription_corrected.tsv', 'R1027_corrections.tsv'],
        'decryption': 'R1027_decode_b24.txt', 'reading': 'R1027_reading.md', 'translation': 'R1027_en.md', 'language': 'fr',
        'summary': "Van Reede to Van de Spiegel, Berlin, 4 Mar 1788: news from Russia that Ségur and Cobenzl are dismayed that the Empress has refused the triple alliance; Keller (the Prussian envoy) has no answer and expects none until the Empress hears from Vienna whether the Emperor is resolved on a vigorous attack on the Turks, which decided the Emperor's declaration; the Empress will wait for the courier sent to London before declaring herself on the King's proposals."},
}
NOTE = {
    'DECODE R1026': "Read 23 Oct 2026 (b24) on the figures under the Grand Chiffre R1024: DECODE's 'J+' sign is the writer's hooked 1 (J=1 gives a fitting key word at all 77 occurrences, the 21 Sept LM-chosen digits and J=3 do not); the key's null blocks ('Nonvaleurs' 1-50, 331-370, 1201-1250, 2751-2800, 3131-3160, 3621-3660, read on the key images) explain the 'open codes' 1250, 331, 2800, 3160, and 2637 = cependant was mis-numbered 3637 in the key transcription; four key slips read on the key images (54 est, 2142 paroit, 2143 paroitre, 4910 que); five labels corrected on the letter image. Bar marks read as the code's inflection signs. Word check (b24_vr_align.py): every word of the cipher part carried by its groups or their marks; 403 of 1,388 decoded letters rest on the hooked-1 identification, 24 on the five corrected labels. Body 0.735 clean (25/34), explicit holes 0.971. Open: [?soit], [?fournit], [?énonçoit] (writer's slips or bar marks) and three faint words of the clear passage.",
    'DECODE R1027': "Read 23 Oct 2026 (b24) as R1026: J+ = 1 at all 24 occurrences, three labels corrected on the image (3089, 1021, 1969), 4910 = que from the key image; names spelt in key syllables (Segur, Cobentzel, Keller). 118 of 601 decoded letters rest on the hooked 1, 15 on the corrected labels. Body 0.867 clean (13/15), explicit holes 0.933. Open: [?decidement] (spelt de-ci-demi-ent).",
}

STEPS = [
    {'date': '2026-10-23', 'kind': 'access', 'what': "Re-read (REREAD_BRIEF, b24): DECODE R1026 and R1027 fetched again with the shared cookie (b24_fetch.py, scratchpad): only the page images and the transcription; no attachment, comment or decipherment on either record. The printed Van de Spiegel correspondence already in the main checkout (Brieven en negotiatien i-iii, Vreede's Van de Spiegel iii) has no Van Reede letter of these dates; no contemporary decipherment or copy.", 'result': 'failed'},
    {'date': '2026-10-23', 'kind': 'transcription', 'technique': ['key-structure hypothesis', 'manual reconstruction'], 'what': "DECODE's 'J+' looked at on zoomed strips of the letters: it is one glyph, the writer's 1 with a hooked foot (the plain 1 also occurs). J=1 gives a key word that fits at every occurrence (77 in R1026, 24 in R1027: 'au Roi le projet', 'à dix heures', 'il n'y a', 'la reponse est arrivée'); J=3 gives 'au reste il n'est le projet', and the 21 Sept beam search had chosen 0, 1, 2, 3 or 4 per group, the source of the garble.", 'result': 'worked'},
    {'date': '2026-10-23', 'kind': 'key from source', 'technique': ['manual reconstruction'], 'what': "Key R1024 checked on its images where its DECODE transcription has holes: the missing ranges 1-50, 331-370, 1201-1250, 2751-2800, 3131-3160 and 3621-3660 are blocks headed 'Nonvaleurs depuis ... jusqu'à ...' (nulls), which accounts for the 'open codes' 1250, 331, 2800, 3160, 3660, 3153, 2751, 50, 1201; number-column slips fixed by page order (3637 'cependant' = 2637, 3635 = 2635, 1615 = 2615, 2520 = 2530, 3530 = 3539, 3577 = 3677, 3230 = 3730); word slips read on the images: 54 est (not es), 2142 paroit, 2143 paroitre (missing), 4910 que (not quo) (b24_vr_key.py). Each holds at every occurrence in R1026/R1027.", 'result': 'worked'},
    {'date': '2026-10-23', 'kind': 'transcription', 'what': "Every group of R1027 and the flagged groups of R1026 re-read on zoomed strips of the DECODE images (b24_strips.py): R1026 '1?00' = 100, '21423068' = 2142 3068, '4 4 3 8' = 4438 corrected by the writer to 4433, '51?' = 513 (flat-backed 3), '308?9' = 3089; R1027 '3?089' = 3089, '1?1021' = 1021, '0969' = 1969; the rest of DECODE's digits confirmed (R1026_corrections.tsv, R1027_corrections.tsv, *_transcription_corrected.tsv).", 'result': 'worked'},
    {'date': '2026-10-23', 'kind': 'hypothesis', 'technique': ['contextual inference', 'key-structure hypothesis'], 'what': "The bar marks over and under groups are the code's inflection signs: a bar above cuts final letters from the key word (prier = prié, soin + R = soir, motif + ver = motiver, Sieur + N = sien, entendre = entend, temperer + or air E = temporaire, laissai + nt = laissant, seulement = seule; over the first digit it cuts the front: 'le Comtte de Finkenstein' = Comtte de Finkenstein), a bar below adds the ending (Ministres, heures, possessions, Puissances, a faite, connue); an accent stroke gives é (entrées, decidé). No instruction sheet on the record; read from the letters only.", 'result': 'partial'},
    {'date': '2026-10-23', 'kind': 'reading', 'technique': ['manual reconstruction'], 'what': "Readings written on the figures (R1026_reading.md, R1027_reading.md; translations R1026_en.md, R1027_en.md); the clear passages of R1026 read from the image (DECODE's cleartext lines are garbled). Word check (b24_vr_align.py): every word of the cipher parts is in the decoded stream or explained by a bar mark. _check_reading.py on the bodies: R1026 0.735 (25/34), R1027 0.867 (13/15); explicit-hole share 0.971 and 0.933; before 0.00 (audit). Both set read, grade B (bar-mark convention inferred, not documented).", 'result': 'worked'},
]


def texts():
    for d in ('DECODE R1026', 'DECODE R1027'):
        mark_read(d, FIELDS[d], 'B', NOTE[d])


def documents():
    for d, n in (('DECODE R1026', 5), ('DECODE R1027', 3)):
        p = load(T)
        e = [x for x in p['documents'] if x.get('id') == d][0]
        e['read'] = 'read'
        save(T, p)
        p = load(T)
        e = [x for x in p['documents'] if x.get('id') == d][0]
        e['transcription']['corrections'] = n
        save(T, p)
        p = load(T)
        e = [x for x in p['documents'] if x.get('id') == d][0]
        e['transcription']['notes'] = "DECODE's J+ sign is the writer's hooked 1 (b24, 23 Oct 2026; the 21 Sept per-group LM resolution withdrawn); labels corrected on the image in %s_corrections.tsv." % d.split()[1]
        save(T, p)
    p = load(T)
    p['system']['nulls'] = {'present': True, 'count': 14}
    save(T, p)
    print('documents')


def outcome():
    set_outcome(
        **{'class': 'read'},
        method='read with known key',
        method_basis="William V's 1782 Grand Chiffre (DECODE R1024, named on the DECODE records) reads R1026 and R1027 once DECODE's J+ sign is taken as the writer's hooked 1 and the key's null blocks and transcription slips are read off the key images (b24, 23 Oct 2026); R1028's DECODE plaintext served as control.",
        key='recovered',
        fraction_read=1.0,
        fraction_read_method='measured',
        fraction_read_source="23 Oct 2026, re-read (b24): both documents of outcome.texts read (2 of 2; 471 of 471 groups by document length, ciphertext_R1026/R1027.txt). Earlier: 0 (reading audit, 22 Oct 2026).",
        codes_open={'open': 0, 'total': 'unknown', 'tokens_open': 0},
        gaps=[
            {'item': "R1026 [?soit], [?fournit], [?énonçoit]; R1027 [?decidement]: four words where the groups and their bar marks spell a slip ('soient' + bars, 'E Nonce ois', 'de ci demi ent')",
             'blocker': 'no-key-material',
             'detail': "the key carries no instruction for the bar marks; the reading is the sense the groups point to"},
            {'item': "R1026 clear passage: 'je [?vois] le plus [?estimé] d'[?ici]', 'le jour [?la]'",
             'blocker': 'illegible',
             'detail': "faint hand on the 1240-px DECODE image; a better image of NA 3.01.26 inv. 190 would settle them"},
        ],
        verification=['matched control', 'key confirms', 'historical consistency'],
        notes="R1026 and R1027 read with William V's Grand Chiffre (R1024). Split 14 Oct 2026: R1893 is vanreede1793. 22 Oct 2026, reading audit: both relabelled decoded, not read (garbled runs). 23 Oct 2026 (b24): the garble came from resolving DECODE's J+ sign digit by digit with a language model; J+ is the writer's hooked 1, the key's untranscribed blocks are nulls ('Nonvaleurs'), and four key slips were read on the key images; both letters now read in full (R1026 0.735, R1027 0.867 clean sentences), four words carried in part and three faint clear-text words open.",
    )


if __name__ == '__main__':
    what = sys.argv[1]
    if what == 'texts': texts()
    elif what == 'documents': documents()
    elif what == 'outcome': outcome()
    elif what == 'steps':
        for s in STEPS: add_step(s)
