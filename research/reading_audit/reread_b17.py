"""Re-read brief (REREAD_BRIEF.md), batch b17: battier1686, bethune, brulart1615.

Targeted profile edits with the splice saver of relabel_r0.py; one save per change.

    python research/reading_audit/reread_b17.py <target> <step>
Helpers: b17_fetch.py (DECODE record files to the scratchpad), b17_crop.py (strips at native resolution),
b17_brulart_align.py (brulart run tables), b17_score.py (clean-sentence share of a reading body).
"""
import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from relabel_r0 import load, save  # noqa: E402

REV = dict(by='Claude Opus 5.5', date='2026-10-22')


def mark_read(t, doc, fields, grade, note):
    p = load(t)
    e = [x for x in p['outcome']['texts'] if x.get('doc') == doc]
    assert len(e) == 1, doc
    e = e[0]
    e.pop('note', None)
    e['state'] = 'read'
    e.update(fields)
    e['reading_review'] = dict(grade=grade, **REV, note=note)
    save(t, p); print('read', t, doc)


def set_note(t, doc, note, fields=None):
    p = load(t)
    e = [x for x in p['outcome']['texts'] if x.get('doc') == doc][0]
    e['note'] = note
    if fields: e.update(fields)
    save(t, p); print('note', t, doc)


def add_step(t, step):
    p = load(t)
    p['solution'].append(step)
    save(t, p); print('step', t)


def set_outcome(t, **kw):
    for k, v in kw.items():
        p = load(t)
        if isinstance(v, list) and len(v) > 1:    # one appended item per save: the splice saver reverses several inserts at one place
            p['outcome'][k] = v[:1]; save(t, p)
            for x in v[1:]:
                p = load(t); p['outcome'][k].append(x); save(t, p)
            continue
        p['outcome'][k] = v
        save(t, p)
    print('outcome', t, list(kw))


# ---------------------------------------------------------------- brulart1615
BR_NOTE = {
    'R2785': "Read 22 Oct 2026 (b17): clear text and the contemporary interlinear decipherment transcribed from the DECODE images (ff. 83r-84r), every run checked against Tomokiyo's key (texts/R2785_align.tsv); _check_reading.py on the body 0.854 (35/41). Open: three spaced-sign lines with no decipherment that give no French under the key (probably nulls, as Tomokiyo noted) and three cramped glosses on f. 83v. Dated 16 (not 15) Sept 1615.",
    'R2786': "Read 22 Oct 2026 (b17): clear text and the contemporary interlinear decipherment transcribed from the DECODE images (ff. 109r-110r), checked against Tomokiyo's key; 'incommoditez' corrected to the figures' 'inconvenients', and the unglossed 'en mesme temps' decoded with the key (texts/R2786_align.tsv); _check_reading.py on the body 0.863 (44/51). Open: most of f. 109v rows 9-11 and 110r row 1 (no decipherment, no French under the key) and the figures 16, 21 of row 8.",
}
BR_FIELDS = {
    'R2785': {'transcription': ['texts/R2785_reading.md', 'texts/R2785_align.tsv'], 'decryption': ['texts/R2785_reading.md', 'https://de-crypt.org/decrypt-web/RecordsView/2785'], 'reading': 'texts/R2785_reading.md', 'translation': 'texts/R2785_en.md', 'label': 'Poitiers, 16 Sep 1615'},
    'R2786': {'transcription': ['texts/R2786_reading.md', 'texts/R2786_align.tsv'], 'decryption': ['texts/R2786_reading.md', 'https://de-crypt.org/decrypt-web/RecordsView/2786'], 'reading': 'texts/R2786_reading.md', 'translation': 'texts/R2786_en.md'},
}
BR_STEPS = [
    {'date': '2026-10-22', 'kind': 'access', 'what': "Re-read (REREAD_BRIEF, b17): every file on DECODE R2785 and R2786 fetched with the shared cookie into the session scratchpad (b17_fetch.py): 4 page images each and Tomokiyo's key png; no transcription or plaintext attached. Both letters carry a contemporary interlinear decipherment over most cipher runs.", 'result': 'worked'},
    {'date': '2026-10-22', 'kind': 'transcription', 'what': "Clear text and interlinear decipherments of R2785 (ff. 83r-84r) and R2786 (ff. 109r-110r) transcribed from native-resolution strips (b17_crop.py); each cipher run aligned with its decipherment and checked against Tomokiyo's key (texts/R2785_align.tsv, R2786_align.tsv): the numbers (20 de, 5 pre, 7 que, 8 qui, 18 con, 30 tion, 35 en, 97 pour ...) and letter signs carry the glosses throughout. R2785 is dated 16 Sept 1615.", 'result': 'worked'},
    {'date': '2026-10-22', 'kind': 'hypothesis', 'technique': ['key matching', 'contextual inference'], 'what': "θ (not in Tomokiyo's table) is a null: R2786 'ff ʃʃ θ' = 'et', and it falls between words wherever it occurs; R2786 f. 109v row 8 the figures give 'inconvenients' where the decipherer wrote 'incommoditez'; row 11 (no gloss) decodes 'en mesme temps'.", 'result': 'worked'},
    {'date': '2026-10-22', 'kind': 'verification', 'technique': ['key matching'], 'what': "Unglossed spaced-sign lines (R2785 f. 83v rows 17-18, f. 84r row 2; R2786 f. 109v rows 9-11 in part) decoded with the key, with and without θ and φ as nulls: no French; consistent with Tomokiyo's note that they may be nulls.", 'result': 'failed'},
    {'date': '2026-10-22', 'kind': 'reading', 'technique': ['language-model scoring'], 'what': "Readings and translations written (texts/R2785_reading.md, R2786_reading.md, _en.md); clean-sentence share on the bodies 0.854 and 0.863. Both set read (grade B).", 'result': 'worked'},
]


def brulart(step):
    t = 'brulart1615'
    if step == 'texts':
        for d in ('R2785', 'R2786'):
            mark_read(t, d, BR_FIELDS[d], 'B', BR_NOTE[d])
    elif step == 'outcome':
        set_outcome(
            t,
            method='read from existing decipherment',
            method_basis="Both letters read on 22 Oct 2026 from the contemporary interlinear decipherments written over their cipher runs, transcribed from the DECODE images and checked run by run against Satoshi Tomokiyo's reconstructed key (DECODE DOC_2785/2786); two unglossed runs decoded with his key.",
            contribution=['transcription', 'key extended or corrected', 'sender or date identified'],
            **{'class': 'read'},
            key='partial',
            fraction_read=1.0,
            fraction_read_source="22 Oct 2026, re-read (b17): both documents of outcome.texts read (2 of 2). The unread pieces inside them (R2785's three spaced-sign lines, about 60 signs, probably nulls; parts of R2786 f. 109v rows 9-11) are named in gaps.",
            gaps=[
                {'item': "R2785: the three spaced-sign lines at the foot of f. 83v and the head of f. 84r (about 60 signs) and R2786 f. 109v rows 9-11 / f. 110r row 1 outside the glossed words",
                 'blocker': 'no-key-material',
                 'detail': "no contemporary decipherment, and no French under Tomokiyo's key with or without θ and φ as nulls; Tomokiyo's DECODE notes take such passages for nulls or cancelled signs"},
            ],
        )
        p = load(t)
        p['outcome']['gaps'].append({'item': "R2785 f. 83v: three cramped interlinear glosses ('m'est possible', '[?lors] de [?propos]', 'l'Equidray') and the gloss after 'ont este', and the clear name '[?Manjeaux]'",
                                     'blocker': 'illegible',
                                     'detail': "the decipherer's hand is small and blotted at the resolution of the DECODE photographs; the letter signs under them are partly ambiguous in the key (the circled sign is l or y)"})
        save(t, p)
        p = load(t)
        p['outcome']['notes'] = p['outcome']['notes'] + " 22 Oct 2026, re-read (b17): both letters read from their contemporary interlinear decipherments, checked against Tomokiyo's key (texts/); θ is a null; R2785 is dated 16 Sept 1615."
        save(t, p); print('notes')
    elif step == 'steps':
        for s in BR_STEPS:
            add_step(t, s)


# ---------------------------------------------------------------- battier1686
BA_NOTE = {
    '1687-12-04': "Read 22-23 Oct 2026 (b17): the whole letter (91R, 92L, 92R) with the 92L block re-read on the NA scan and every doubtful group checked on the key scans (readings/1687-12-04_corrections.tsv: 12:908 Turcken, 3:352 by, 11:403 secreet); 92R clear text transcribed. Explicit-hole clean share of the body 0.963 (52/54); _check_reading.py 0.093 (its modern-Dutch word list knows neither the 17th-c. spelling nor the loans and names; 0.20 with a Vondel/Cats lexicon). Open: 92L 889 and the letters before 'soon', 91R 11:466 and the end of the Novelli sentence. No contemporary decipherment (scans 90-94).",
    '1688-02-12': "Read 22-23 Oct 2026 (b17): the whole letter (99R, 100L, 100R) with the 100R block re-read on the NA scan and the key scans (readings/1688-02-12_corrections.tsv: 8:48 minste, 14:455 voordragen, 11:678 soo) and two cipher runs missing from the token files decoded (99R 'Gravinne van Soissons', 100L '... de Coninginne ...'); 99R and 100L clear text transcribed. Explicit-hole clean share 0.939 (46/49); _check_reading.py 0.061 (word-list coverage, as for 4 Dec). Open: 99R 431 374 137 512 and 604, 100L four groups, 100R the group after Madrid and two after it. No contemporary decipherment (scans 98-102).",
}
BA_FIELDS = {
    '1687-12-04': {'reading': 'readings/1687-12-04_reading.md', 'translation': 'readings/1687-12-04_en.md'},
    '1688-02-12': {'reading': 'readings/1688-02-12_reading.md', 'translation': 'readings/1688-02-12_en.md'},
}
BA_STEPS = [
    {'date': '2026-10-22', 'kind': 'access', 'what': "Re-read (REREAD_BRIEF, b17): NA 3.01.18 inv. 401 scans 90-94 and 98-102 fetched full size (b17_na_fetch.py) and searched for decipherment sheets or glosses for 4 Dec 1687 and 12 Feb 1688: none (endorsements, show-through and the next letters only).", 'result': 'failed'},
    {'date': '2026-10-22', 'kind': 'transcription', 'what': "92L, 91R, 99R and 100R cipher lines re-read group by group at native resolution against tokens/; two cipher runs missing from the token files transcribed (99R last line, 100L line 3); the clear text of 92R, 99R and 100L transcribed in full.", 'result': 'worked'},
    {'date': '2026-10-22', 'kind': 'verification', 'technique': ['key matching', 'contextual inference'], 'what': "Every doubtful group looked up on the key scans (NA 1.10.29 inv. 1209, b17_keylook.py with key/colindex.txt): 12:908 Turcken, 3:352 by, 11:403 Secreet, 8:48 minste, 14:455 voordragen (c/ mark), 11:678 soo, 11:784 de Coninginne adopted; 1:889, 11:466, 1:431, 3:374, 1:512, 11:719, 1:590, 1:839, 1:867 give no sense and stay open (readings/*_corrections.tsv).", 'result': 'partial'},
    {'date': '2026-10-22', 'kind': 'reading', 'technique': ['language-model scoring'], 'what': "Readings and translations of the two whole letters written (readings/1687-12-04_reading.md, 1688-02-12_reading.md, _en.md). _check_reading.py 0.093 and 0.061 (modern-Dutch word list; 0.20 with a 17th-c. Vondel/Cats lexicon); explicit holes only 0.963 and 0.939. Set read on the reading (grade B), the checker figure recorded as a word-list limitation.", 'result': 'worked'},
]


def battier(step):
    t = 'battier1686'
    if step == 'texts':
        for d in ('1687-12-04', '1688-02-12'):
            mark_read(t, d, BA_FIELDS[d], 'B', BA_NOTE[d])
    elif step == 'gaps':
        p = load(t); g = p['outcome']['gaps']
        g[6] = {'item': "4 Dec 1687 and 12 Feb 1688: groups without sense after the 22 Oct 2026 re-read (92L 889 and the letters a-u-t-o-r-i-s-g; 91R 11:466, 14:6ø, ø94; 99R 431 374 137 512, 604; 100L 867 826 296 765; 100R the struck groups after Madrid and after gesoubconneert, 59ø ø39)",
                'blocker': 'open-codes',
                'detail': "each looked up on the key scans (readings/*_corrections.tsv); the key values give no sense in place and the marks are faint or missing; the letters are read around them"}
        g[4] = {'item': "Separate decipherment sheets near 4 December 1687 and 12 February 1688",
                'blocker': 'no-key-material',
                'detail': "checked 22 Oct 2026: scans 90-94 and 98-102 hold no decipherment sheet, slip or gloss for either letter"}
        save(t, p); print('gaps')
    elif step == 'notes':
        p = load(t)
        p['outcome']['notes'] = p['outcome']['notes'] + " 22-23 Oct 2026, re-read (b17): 4 Dec 1687 and 12 Feb 1688 read as whole letters after the cipher blocks were re-read on the scans and the key (12:908 Turcken, 3:352 by, 8:48 minste, 14:455 voordragen; two untranscribed cipher runs added); the checker's modern-Dutch word list cannot score Battier's Dutch (0.06-0.09), explicit holes 0.94-0.96."
        save(t, p); print('notes')
    elif step == 'steps':
        for s_ in BA_STEPS:
            add_step(t, s_)


# ---------------------------------------------------------------- bethune
BE_STEPS = [
    {'date': '2026-10-22', 'kind': 'literature search', 'what': "Re-read (REREAD_BRIEF, b17), step 1: Halphen, Lettres inedites du roi Henri IV a monsieur de Bethune ... du 18 octobre au 24 decembre 1601 (1889) found in full view on HathiTrust (record 100644113, item iau.31858014633857, public domain); babel.hathitrust.org answers with a Cloudflare human-verification page (curl 403; the browser pane shows the checkbox), which this session does not pass. Not on the Internet Archive, Gallica or Google Books (searched). Not on DECODE.", 'result': 'partial'},
    {'date': '2026-10-22', 'kind': 'verification', 'what': "Re-read, step 2: no new image route or transcription; the measured transcription ceiling (oracle 71%, two readers agree on 69% of glyphs, third pass) stands, so the 9 Nov and 22 Nov decodes stay fragments. Both kept decoded, not read; the edition is the route.", 'result': 'failed'},
]


def bethune(step):
    t = 'bethune'
    if step == 'steps':
        for s_ in BE_STEPS:
            add_step(t, s_)
    elif step == 'gaps':
        p = load(t)
        p['outcome']['gaps'].append({'item': "Halphen (ed.), Lettres inedites du roi Henri IV a M. de Bethune, 18 Oct - 24 Dec 1601 (1889): may print the 9 and 22 Nov letters in clear",
                                     'blocker': 'not-attempted',
                                     'detail': "full view on HathiTrust, item iau.31858014633857 (record 100644113), behind a human-verification page; a person opening babel.hathitrust.org/cgi/pt?id=iau.31858014633857 can read it"})
        save(t, p); print('gaps')


if __name__ == '__main__':
    t, step = sys.argv[1], sys.argv[2]
    {'brulart1615': brulart, 'battier1686': battier, 'bethune': bethune}[t](step)
