"""Re-read brief (REREAD_BRIEF.md), batch b18: charles1536 (R9957, R9952).

Targeted profile edits with the splice saver of relabel_r0.py; one save per change (pattern of reread_b17.py).

    python research/reading_audit/reread_b18_charles.py <step>     step = texts | outcome | steps | docs
Helpers: b18_crop.py, b18_box.py (crops into the scratchpad), b18_align.py (word alignment of a reading with its
source), b18_score.py (clean-sentence share of a reading body), b18_r9957_assemble.py (R9957 reading body from the run
files R9957_runs_A/B/C.md), b18_r9957A_box.py, b18_r9957B_box.py, b18_r9957C_*.py (the three run readers' crop helpers).
"""
import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from relabel_r0 import load, save  # noqa: E402

T = 'charles1536'
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
    'R9957': {
        'transcription': ['texts/R9957_runs_A.md', 'texts/R9957_runs_B.md', 'texts/R9957_runs_C.md', 'texts/R9957_decifrado_f274.txt'],
        'decryption': ['texts/R9957_reading.md', 'texts/R9957_key169.md'],
        'reading': 'texts/R9957_reading.md',
        'translation': 'texts/R9957_en.md',
        'language': 'es',
    },
    'R9952': {
        'transcription': 'texts/R9952_decifrado_ff13-14.txt',
        'decryption': 'texts/R9952_reading.md',
        'reading': 'texts/R9952_reading.md',
        'translation': 'texts/R9952_en.md',
        'language': 'es',
    },
}
NOTE = {
    'R9957': "Read 23 Oct 2026 (b18): the cipher runs of ff. 270r-273v read sign by sign from the DECODE images under the key AGS Estado leg. 1.1.1 doc. 169 (as reproduced by Luo 2021, pp. 603-606; texts/R9957_key169.md), sign transcriptions and decodes in texts/R9957_runs_A/B/C.md; the last passage (ff. 273v-274r) from its contemporary decipherment on f. 274r (texts/R9957_decifrado_f274.txt). Luo's edition (pp. 287-290, in copyright) used only as a check, cited not copied; 14 places where the figures differ from her text are followed. Reading body 0.629 clean sentences on _check_reading.py, 0.953 on explicit holes (the word list lacks the period spelling). Open: a tear and one unreadable group in run 1, run B16 (about 14 signs on stamp 0009, no sentence), parts of the dense blocks on stamp 0011, a faded fold on 0013.",
    'R9952': "Read 23 Oct 2026 (b18): the contemporary decipherment on ff. 13-14 bis ('del Emperador a Su Al.') transcribed line by line (texts/R9952_decifrado_ff13-14.txt) and checked against the figures of ff. 10-12: every clear word left inside the cipher runs and Tomokiyo's code words (go para, pi enemigo, xu dinero) stand in the same order and place; one disagreement (figures 'dexandolo', decipherer 'dexando'), the figures followed. No key of this cipher in the repository, so the runs between the clear words are not checked sign by sign. Reading body 0.683 clean sentences, 1.00 on explicit holes.",
}
STEPS = [
    {'date': '2026-10-22', 'kind': 'access', 'what': "Re-read (REREAD_BRIEF, b18): the DECODE record pages of R9952 and R9957 list page images only (20 and 18), no transcription, plaintext, key or comments; all 38 images (main checkout img/) opened. R9952: the full contemporary decipherment is on images P12-P18, P20 (ff. 13-14 bis). R9957: the contemporary decipherment of the last cipher passage is on stamps 0017-0018. Luo's thesis PDF (key doc. 169 pp. 603-606, edition pp. 287-290) was already in the main checkout (caracciolo1537/prior/luo2021.pdf); RODERIC now answers with an Anubis bot check and was not used.", 'result': 'worked'},
    {'date': '2026-10-22', 'kind': 'transcription', 'what': "R9952: the decipherment on ff. 13-14 bis transcribed line by line (texts/R9952_decifrado_ff13-14.txt, 1,919 words); it gives only the ciphered passages, marking each return to clear with '/ lo otro claro /'.", 'result': 'worked'},
    {'date': '2026-10-22', 'kind': 'verification', 'technique': ['plaintext matching', 'key matching'], 'what': "R9952: decipherment checked against the figures of ff. 10-12 (images P5, P6, P9, P11): every clear word or phrase left inside the cipher runs falls in the same order and place, and Tomokiyo's code words (go para, pi enemigo, xu dinero) stand where the decipherment has those words. One difference: figures 'dexandolo', decipherer 'dexando'. Not checked sign by sign: no key of this cipher in the repository.", 'result': 'partial'},
    {'date': '2026-10-23', 'kind': 'key from source', 'technique': ['key matching'], 'what': "R9957: the key AGS Estado leg. 1.1.1 doc. 169 summarised from Luo's images (texts/R9957_key169.md): letters with up to three homophones, syllables as base sign + vowel mark (underline a, + e, # i, p o, o u) or the numbers 32-91, codes 92-211 and graphic signs, dotted signs and numbers from 212 null. Calibrated on stamp 0001: 'se gra[?] e de manera que no se pierda'; a plain a = e, underlined a = da.", 'result': 'worked'},
    {'date': '2026-10-23', 'kind': 'reading', 'technique': ['key matching', 'contextual inference'], 'what': "R9957: the 52 cipher runs of stamps 0001-0014 read sign by sign on crops at 1.6-2.4x native resolution under the doc. 169 key, in three parts (texts/R9957_runs_A.md 0001-0006, _B.md 0007-0011, _C.md 0012-0014), each with its sign transcription, decode and comparison with Luo; about 1,600 words. Key observations (none changed): e+ like a hooked 4, ŧ̲ like ŧ+, the nn sign = ñ, 28 for initial r, L# = zi, dotted signs null. Recorded, not adopted: dinero with 52 on 0005-0006 and 53 on 0007-0014; 5 for b three times (key d); a sign 7° (a[?yu]da, cu[?yo]).", 'result': 'worked'},
    {'date': '2026-10-23', 'kind': 'reading', 'technique': ['key matching'], 'what': "R9957: run B16 (stamp 0009, about 14 signs: a# L+ 68 1 L ep ·64 4 ŧ# 31 U 9̲ | 50 ŧ+ n ep) gives no sentence under the key; Luo prints no cipher at this place. The two dense blocks on stamp 0011 (B25, B28) only partly carried; two figures on 0013 ([43], [6]) with no value.", 'result': 'failed'},
    {'date': '2026-10-23', 'kind': 'transcription', 'what': "R9957: the contemporary decipherment of the last cipher passage (stamps 0017-0018) transcribed line by line (texts/R9957_decifrado_f274.txt); the cipher of stamps 0016-0017 not re-read sign by sign (the code 97, Antonio de Leyva, stands where the decipherment has 'Antonio').", 'result': 'worked'},
    {'date': '2026-10-23', 'kind': 'verification', 'technique': ['plaintext matching'], 'what': "R9957: decodes compared with Luo 2021 pp. 287-290 run by run (her edition used only as a check, cited not copied): agreement in substance throughout; 14 places where the figures differ are followed (e.g. 'En lo de los cinco mil' for her 'En los', 'pongo' for 'ponpo', 'asientos de trezientos' for 'asi en todo de', 'me embien' for 'ma (sic.) enbien'); 'Gonçalo de Ayora' (stamp 0005) is cipher that she prints as clear.", 'result': 'worked'},
    {'date': '2026-10-23', 'kind': 'reading', 'technique': ['language-model scoring'], 'what': "Readings and translations written (texts/R9952_reading.md, R9957_reading.md, _en.md; log texts/R9952-R9957_reread_log.md), each aligned word by word with its source (b18_align.py: R9952 1,917/1,919 words carried by the decipherment, R9957 all reading words carried by the run decodes, the clear words around them and the f. 274r decipherment). Clean-sentence share of the reading bodies: R9952 0.683 (1.00 on explicit holes), R9957 0.629 (0.953). Both set read (grade B).", 'result': 'worked'},
]


def texts():
    for d in ('R9957', 'R9952'):
        mark_read(d, FIELDS[d], 'B', NOTE[d])


def outcome():
    set_outcome(
        method_basis="R9952 is read from its contemporary decipherment (ff. 13-14 bis), checked against the clear words and code words of the figures. R9957 is read from the figures with the original key AGS Estado leg. 1.1.1 doc. 169 as reproduced by Luo (2021, pp. 603-606), and its last passage from the contemporary decipherment on f. 274r; Luo's printed decipherment (2021, pp. 287-290) existed before this work and was used only as a check.",
        contribution=['transcription', 'sender or date identified', 'catalogue correction'],
        fraction_read=1.0,
        fraction_read_method='measured',
        fraction_read_source="23 Oct 2026, re-read (b18): both documents of outcome.texts read (2 of 2). The unread pieces inside them (R9957 run B16, about 14 signs; parts of two dense blocks on stamp 0011; a tear and a faded fold; R9952 two cramped words) are named in gaps.",
        gaps=[
            {'item': "R9957: run 1 (a tear after 'bien de', and 'se [?gra…] e'), the dense blocks B25 and B28 on stamp 0011 in part, a faded fold on stamp 0013 (run C2) and a tear on stamp 0014 (run C5); R9952: 'paresce […]' on f. 13 bis v and the last word on f. 14 bis r",
             'blocker': 'illegible',
             'detail': "torn or faded paper and cramped signs at the resolution of the DECODE photographs; R9952's two words are cramped in the decipherer's hand"},
            {'item': "R9957: run B16 (stamp 0009, about 14 signs), two figures with no value in run C2 ([43], [6]), the sign 7° (a[?yu]da, cu[?yo]) and the value of 52/53 in dinero",
             'blocker': 'no-key-material',
             'detail': "no sentence under the doc. 169 key; no contemporary decipherment of these runs and Luo prints no cipher at B16; no second text in this key in the repository to fix the values"},
        ],
    )
    p = load(T)
    p['outcome']['notes'] = p['outcome']['notes'] + " 23 Oct 2026, re-read (b18): both letters read. R9952 from its contemporary decipherment, transcribed and checked against the figures' clear words; R9957 from the figures with the doc. 169 key (run files texts/R9957_runs_A/B/C.md) and its contemporary decipherment on f. 274r, with Luo 2021 as a check (14 places where the figures differ from her text)."
    save(T, p); print('notes')


def steps():
    for s in STEPS:
        add_step(s)


def docs():
    p = load(T)
    d = [x for x in p['documents'] if x['id'] == 'R9952'][0]
    d['transcription'] = {'by': 'llm from images', 'source': 'the contemporary decipherment on ff. 13-14 bis, transcribed line by line from the DECODE images (texts/R9952_decifrado_ff13-14.txt); the cipher of ff. 10-12 not transcribed sign by sign', 'image_quality': 'good', 'notes': 'The decipherment gives only the ciphered passages.'}
    save(T, p); print('doc R9952')
    p = load(T)
    d = [x for x in p['documents'] if x['id'] == 'R9957'][0]
    d['transcription'] = {'by': 'llm from images', 'source': 'cipher runs of stamps 0001-0014 transcribed sign by sign under the doc. 169 key (texts/R9957_runs_A/B/C.md, 23 Oct 2026); the contemporary decipherment of stamps 0017-0018 (texts/R9957_decifrado_f274.txt). The first-pass trans_p1-9.txt, trans_p10-18.txt (21 Sept) are superseded.', 'image_quality': 'good', 'notes': 'Sign labels follow R9957_key169.md; the cipher of stamps 0016-0017 was not re-read sign by sign.'}
    save(T, p); print('doc R9957')


if __name__ == '__main__':
    {'texts': texts, 'outcome': outcome, 'steps': steps, 'docs': docs}[sys.argv[1]]()
