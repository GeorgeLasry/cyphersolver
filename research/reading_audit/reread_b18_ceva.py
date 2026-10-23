"""Re-read brief (REREAD_BRIEF.md), batch b18: ceva1632 (R75, R84).

Targeted profile edits with the splice saver of relabel_r0.py; one save per change.

    python research/reading_audit/reread_b18_ceva.py texts|outcome|documents|steps
Helpers: b18_ceva_fetch.py (DECODE record files to the scratchpad), b18_ceva_crop.py (strips), b18_ceva_show.py
(token stream as words), b18_ceva_align.py (decode vs contemporary decipherment), b18_ceva_redecode.py (decode with
the adopted values), b18_ceva_check.py (word-by-word carrier check), b18_ceva_score.py (clean-sentence share of the body).
"""
import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from relabel_r0 import load, save  # noqa: E402

T = 'ceva1632'
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
        if isinstance(v, list) and len(v) > 1:    # one appended item per save
            p['outcome'][k] = v[:1]; save(T, p)
            for x in v[1:]:
                p = load(T); p['outcome'][k].append(x); save(T, p)
            continue
        p['outcome'][k] = v
        save(T, p)
    print('outcome', list(kw))


FIELDS = {
    'R75': {'transcription': ['decode/DOC_R75_D2532_2532.txt', 'r75.retrans.txt', 'R75_transcription_corrected.txt', 'R75_corrections.tsv'],
            'decryption': ['R75_decifrato_f82r.txt', 'r75.read3.txt', 'r75.interlinear.txt'],
            'reading': 'R75_reading.md', 'translation': 'R75_en.md', 'language': 'it',
            'summary': "Barberini to Ceva after Schomberg's victory at Castelnaudary: the victories make the accommodation of Monsieur easier and the union harder; arguments for Richelieu (glory with the Catholic arms, the danger of the Dutch and of the Swede, Monsieur's restlessness, war against the infidel as the glory he lacks). The 1632 decipherment on f. 82r (DECODE attachment DOC_R75_D1145) and the decode with Lasry's key read together."},
    'R84': {'transcription': ['decode/DOC_R84_D2161_2161.txt', 'r84.retrans.txt'],
            'decryption': ['R84_decifrato_f136r.txt', 'r84.read3.txt'],
            'reading': 'R84_reading.md', 'translation': 'R84_en.md', 'language': 'it',
            'summary': "Barberini to Ceva, December 1632: use the victory over Gustavus to bring His Majesty to ease the treaty; the troubles in France made the French conclude the Valtellina peace; the union lies in the hands of France; Monsieur's flight, and the fear that rigour will keep France disunited and unable to help her allies. The 1632 decipherment on f. 136r (DECODE attachment DOC_R84_D1177) and the decode with Lasry's key read together."},
}
NOTE = {
    'R75': "Read 22-23 Oct 2026 (b18): the 1632 decipherment on f. 82r (DECODE attachment DOC_R75_D1145, never opened before) transcribed and aligned unit by unit with the decode under Lasry's key and eight values adopted from it (b18_ceva_align.py, b18_ceva_redecode.py); figures followed where they differ (15 places, listed in R75_reading.md), two labels corrected on the image. Every word carried by the figures (0.92) or f. 82r (0.96) (b18_ceva_check.py). _check_reading.py on the body 0.774 (24/31). Open: 'serva 494 li stimi v4' (one word), 'diolavse' at the head of l.21, 'la e8 loro'.",
    'R84': "Read 22-23 Oct 2026 (b18): the 1632 decipherment on f. 136r (DECODE attachment DOC_R84_D1177, never opened before) transcribed and aligned unit by unit with the decode under Lasry's key and the adopted values; figures followed where they differ (Vega, gelosie, vol, tengano). Every word carried by the figures (0.87) or f. 136r (0.98). _check_reading.py on the body 0.826 (19/23). Open: one word read uncertain in both witnesses ('da [?N.S.re]').",
}

STEPS = [
    {'date': '2026-10-22', 'kind': 'access', 'what': "Re-read (REREAD_BRIEF, b18): every file on DECODE R74-R84 fetched with the shared cookie into the session scratchpad (b18_ceva_fetch.py): 20 page images and 39 png attachments that had never been opened (only the DOC_*.txt files were in decode/). R75's 'cleartext' attachments are the docket, the covering letter, and DOC_R75_D1145 = f. 82r, a complete contemporary decipherment of the cipher; R84's are the covering letter of 11 Dec 1632 (DOC_R84_D1176, 'Scrivo a Mons. Bichi una cifra ...') and DOC_R84_D1177 = f. 136r, a complete contemporary decipherment.", 'result': 'worked'},
    {'date': '2026-10-22', 'kind': 'transcription', 'what': "Both decipherments transcribed from native-resolution strips (b18_ceva_crop.py): R75_decifrato_f82r.txt (31 lines), R84_decifrato_f136r.txt (26 lines), abbreviations expanded in brackets.", 'result': 'worked'},
    {'date': '2026-10-22', 'kind': 'control', 'technique': ['plaintext matching', 'beam/DP decoding'], 'what': "Decode (second-pass tokens) aligned unit by unit with each decipherment by dynamic programming over the whole letter (b18_ceva_align.py; nomenclator elements without a value match any 0-16 letters): the letters agree except at elements and at a handful of slips; 88, keyed 'quel', is 'del/della/dello' at every place in both decipherments.", 'result': 'worked'},
    {'date': '2026-10-22', 'kind': 'hypothesis', 'technique': ['plaintext matching', 'contextual inference'], 'what': "Values adopted only where they hold at every occurrence in R75/R84 and fit Lasry's four letters: 88 = del (not quel; 28 Lasry contexts 'la pieta ~', 'a dano ~ Francia'); 33 (a 'dead' pair) = gli (R75 x5; Lasry 'lege a ~ altri'); 541 = armi (R75 x3, previously parsed io<128>/io{1}); 171 = Regno (x4, previously i<129>/i<124>/i{1}; 129 dropped); 473 = mentre (x2); 497 = tutt- (R75, R84, Lasry 'abbino a ridurre ~ le difficoltà'); 491 = quell- (R75 x2, R84, Lasry 'a ~ unione', 'in ~ piazza'); 104 = Olandesi (f. 82r 'gli Olandesi', interlinear 'Oland.si'; the second pass's 'Svedesi' withdrawn). Read off the decipherments and consistent where met again: 153 = pace (R75 x2, R84), 451 = fatto, 471 = molto, 485 = perche, 110 = Principe/i, 998(+3) = nella (x3), 357 = Schomberg, 581 = Card. Richelieu, 844 = Gostavo.", 'result': 'worked'},
    {'date': '2026-10-22', 'kind': 'hypothesis', 'technique': ['contextual inference'], 'what': "491 at R75 l.16 ('pensieri di ~ natione'): the 1632 interlinear writes 'Goto' and f. 82r 'Gostavo lo Svedese quella natione'; not adopted, since 491 is quell- at the nine other places (both decipherments included) and 'di quella natione' reads; the decipherers' gloss is recorded in the notes. 494 ('se ne serva ~ li stimi'): f. 82r paraphrases ('servirà secondo che giudicherà necessario'); 494 left without a value.", 'result': 'failed'},
    {'date': '2026-10-22', 'kind': 'solver', 'technique': ['beam/DP decoding', 'language-model scoring'], 'what': "Both letters decoded again as one stream with the adopted values (b18_ceva_redecode.py, run2.py settings, in-memory key only): the decoder now parses armi x3, Regno x4, mentre x2, gli x5 and 'del' throughout (r75/r84.read3.txt, tokens3.json).", 'result': 'worked'},
    {'date': '2026-10-22', 'kind': 'verification', 'technique': ['plaintext matching'], 'what': "Disagreements checked on native crops of IMG_R75_I589: l.3 'con otivi' is 59 24 01 (m) 31 85..., 'motivi'; l.21 'co et' is 71 31 94 (se), 'cose' (R75_corrections.tsv, R75_transcription_corrected.txt). Clerk's slips left in the figures and read from the witnesses: 85 for v in 'salvar', 51/80 for g in 'grado', 'gloria', 70 for t in 'ritrovar' (R75), 78 for r in 'l'altro' (R84).", 'result': 'worked'},
    {'date': '2026-10-22', 'kind': 'reading', 'technique': ['plaintext matching', 'language-model scoring'], 'what': "Readings written on the figures with the decipherments carrying the code words (R75_reading.md, R84_reading.md; translations R75_en.md, R84_en.md); the figures followed where the decipherer improved or glossed (R75 'a V.S.', 'che S.E. cominci ... quanto sia', 'di quella natione', 'contro gli infedeli'; R84 'Vega V.S.', 'gelosie'). Word check (b18_ceva_check.py): R75 392 words, 0.92 in the decode, 0.96 in f. 82r, two words carried in part ('d'augumentarla', 'ritrovar' from the interlinear); R84 275 words, 0.87 / 0.98, none uncarried. _check_reading.py on the bodies: R75 0.774 (24/31), R84 0.826 (19/23); before 0.00 and 0.00 (read2). Both set read, grade A.", 'result': 'worked'},
]


def texts():
    for d in ('R75', 'R84'):
        mark_read(d, FIELDS[d], 'A', NOTE[d])


def documents():
    for d, loc, src, part in (
        ('R75', ['interlinear', 'separate folio'], "Contemporary decipherment written between the cipher lines (partly legible) and a complete decipherment on f. 82r, DECODE attachment DOC_R75_D1145 ('082r.jpg [cleartext]'), found 22 Oct 2026. Not deciphered by Lasry.", False),
        ('R84', ['separate folio'], "Complete contemporary decipherment on f. 136r, DECODE attachment DOC_R84_D1177 ('[cleartext]'), found 22 Oct 2026; the first folio of the letter is largely in clear. Not deciphered by Lasry.", False),
    ):
        p = load(T)
        e = [x for x in p['documents'] if x.get('id') == d][0]
        e['read'] = 'read'
        save(T, p)
        p = load(T)
        e = [x for x in p['documents'] if x.get('id') == d][0]
        e['plaintext'] = {'location': loc, 'source': src, 'partial': part}
        save(T, p)
    print('documents')


def outcome():
    set_outcome(
        method='read from existing decipherment',
        method_basis="R75 and R84 read on 22-23 Oct 2026 from their contemporary decipherments (ff. 82r and 136r, png attachments on the DECODE records that had not been opened), aligned unit by unit with the decode under Lasry's reconstructed key (24 Oct 2020) and eight values adopted from the alignment; the figures are followed where the decipherer improved or glossed.",
        key='partial',
        fraction_read=1.0,
        fraction_read_method='measured',
        fraction_read_source="22-23 Oct 2026, re-read (b18): both documents of outcome.texts read (2 of 2, 2,400 of 2,400 tokens by document length). The unread pieces inside them (R75 'li stimi v4', 'diolavse', 'la e8 loro'; R84 one uncertain word) are named in gaps.",
        codes_open={'open': 0, 'total': 60, 'tokens_open': 0},
        gaps=[
            {'item': "R75: three short runs, 'se ne serva 494 li stimi v4' (one word after 'stimi'), 'diolavse 1' at the head of l.21, 'la e8 loro' (l.14-15)",
             'blocker': 'no-key-material',
             'detail': "no value of the key gives a word, and the 1632 decipherment paraphrases (f. 82r 'servirà secondo che giudicherà necessario') or is unclear there ('la [?mira]'; the interlinear 'rep.la')"},
            {'item': "R84: 'da [?N.S.re]' (figures 'c 5')",
             'blocker': 'illegible',
             'detail': "the abbreviation in the decipherer's hand on f. 136r is cramped and the figures give no word"},
            {'item': "values carried by one decipherment only (357 Schomberg, 581 Card. Richelieu, 197 Religione Cattolica, 844 Gostavo, 930/957 Mons.r Nuntio, ...)",
             'blocker': 'needs-physical-access',
             'detail': "no nomenclator for the dossier on DECODE; confirming them across the dossier needs the ASV key"},
        ],
        verification=['contemporary decipherment', 'key confirms', 'historical consistency'],
    )
    p = load(T)
    p['outcome']['contribution'] = ['transcription', 'decipherment with ambiguous key', 'key extended or corrected']
    save(T, p)
    p = load(T)
    p['outcome']['class'] = 'read'
    save(T, p)
    p = load(T)
    p['outcome'].pop('fraction_coherent', None)
    save(T, p)
    p = load(T)
    p['outcome']['credits'][1]['note'] = "1632 decipherments of R75 (f. 82r) and R84 (f. 136r), the readings' witnesses for the code words, and the interlinear on R75"
    save(T, p)
    p = load(T)
    p['outcome']['notes'] = p['outcome']['notes'] + " 22-23 Oct 2026, re-read (b18): both letters have complete contemporary decipherments among the png attachments of their DECODE records (R75 f. 82r, R84 f. 136r), never opened before; transcribed and aligned with the decode, eight values adopted (88 = del, 33 = gli, 541 armi, 171 Regno, 473 mentre, 497 tutt-, 491 quell-, 104 Olandesi, not Svedesi); both read, grade A. R75 opens with Schomberg's victory (Castelnaudary), not the Swedish one; its danger is the Dutch; R84 is a December 1632 letter on Gustavus' death, the Valtellina peace and Monsieur's flight."
    save(T, p)
    print('notes')


def steps():
    for s in STEPS:
        add_step(s)


if __name__ == '__main__':
    {'texts': texts, 'outcome': outcome, 'documents': documents, 'steps': steps}[sys.argv[1]]()
