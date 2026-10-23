"""Steps for reread_b12.py (b12, 22 Oct 2026)."""
from reread_b12 import mark_read, add_steps, set_outcome, load, save
A = 'acciaiuoli1757'
STEPS = {}
def acc_texts():
    for rec, label, score, extra in [
        ('R25', '= R25,', '0.87 (20 of 23 sentences)', "'Vilasso' after Texeira kept from the decipherment, unconfirmed by the figures."),
        ('R195', '= R195,', '0.91 (10 of 11 sentences)', "the decipherer's one hole ('poiché non . . .', margin 'non s'intende') read on the cipher image: 'poiché non ha da durare', as in the draft; two stretches not confirmed by the transcribed figures are marked [?]."),
        ('R200', '= R200,', '1.0 (31 of 31 sentences)', "checked against the second fair copy and the draft; 2803 = Segretario (draft); the ambassador code 2339 left blank by the decipherer read 'Ambasciatore di [?Spagna]' from the draft."),
        ('R201', '= R201,', '0.95 (18 of 19 sentences)', 'a second clear text of the letter is f. 162 (D1416).')]:
        mark_read(A, label, dict(reading='texts/%s_reading.md' % rec, translation='texts/%s_en.md' % rec,
                                 contemporary_decipherment='texts/%s_decipherment.txt' % rec, language='it'), 'A',
                  "Read from the Secretariat of State's own clear decipherment, attached to the DECODE record as a png and "
                  "transcribed here (texts/%s_decipherment.txt), aligned word by word with the key decode "
                  "(texts/%s_align.tsv; code values consistent across the four letters); _check_reading.py on the body %s; %s" % (rec, rec, score, extra))
STEPS[(A, 'texts')] = acc_texts
STEPS[(A, 'steps')] = lambda: add_steps(A, [
    {"date": "2026-10-22", "kind": "access", "what": "DECODE record pages of R25, R195, R200, R201 re-fetched with the project cookie; their DOC_*.png attachments (described in NOTES as 'key and work images', never opened) downloaded: they are the Secretariat of State's clear decipherments and working drafts of R25 (ff. 90-93), R195 (ff. 94-95), R196, R198, R200 (ff. 107-113, two fair copies and a draft), R201 (ff. 161-162).", "result": "worked"},
    {"date": "2026-10-22", "kind": "transcription", "what": "The clear decipherments of R25, R195, R200, R201 transcribed line by line from the images (texts/R*_decipherment.txt).", "result": "worked"},
    {"date": "2026-10-22", "kind": "crib", "technique": ["plaintext matching", "crib testing"], "what": "Each decipherment aligned word by word with the key decode (b12_dec.py, b12_align.py; texts/R*_align.tsv): ~65% of clear words carried letter by letter, ~25% by code groups whose implied values agree across the four letters (2300 tutt-, 2171 molt-, 2189 quest-, 2530 Marchese, 2774 Re, 2803 Segretario, 2823 Sua Maestà ...); the rest fall where DECODE's digit transcription is garbled. Key correction: 03 = per, not nel. READING.md's 2530 = chirurgo withdrawn.", "result": "worked"},
    {"date": "2026-10-22", "kind": "transcription", "what": "R195 line 11 re-read on the cipher image where the decipherer left a hole ('non s'intende'): 2180 14 55 75 05 59 98 55 98 53 = 'poiché non ha da durari' (DECODE: '2 1 8 0 ? 4 5 5 ...'); the draft agrees. R195 line 3 ('pare solamente assicurato') checked on the image and not explained by the key.", "result": "partial"},
    {"date": "2026-10-22", "kind": "verification", "technique": ["language-model scoring"], "what": "_check_reading.py on the reading bodies: R25 0.87, R195 0.91, R200 1.0, R201 0.95 clean sentences. All eight letters now read; fraction_read 1.0.", "result": "worked"}])
def acc_outcome():
    p, d, nl = load(A)
    o = d['outcome']
    o['class'] = 'read'
    o['method_basis'] += " 22 Oct 2026: the four letters that did not build sentences (R25, R195, R200, R201) read from the Secretariat of State's clear decipherments, attached to the DECODE records as png files, aligned word by word with the key decode."
    o['notes'] += " 22 Oct 2026, re-read (REREAD_BRIEF b12): R25, R195, R200, R201 read from the Secretariat's clear decipherments on DECODE (attachments), aligned with the figures; all eight read; class read in part -> read. Open: 2339 (an ambassador, 'di Spagna' only in the draft) and the code groups of R196 not in a decipherment."
    o['credits'].append({"who": "contemporary", "role": "key or decipherment used", "note": "the Secretariat of State's clear decipherments of R25, R195, R200, R201 (Portogallo 117 ff. 90-91, 94, 108-111, 161-162), attached to the DECODE records as png files"})
    save(p, d, nl); print('outcome ok')
STEPS[(A, 'outcome')] = acc_outcome

B = 'balbases1677'
def bal_texts():
    p, d, nl = load(B)
    sc = {'R992': ('0.29', '5 of 17'), 'R996': ('0.40', '12 of 30'), 'R997': ('0.41', '7 of 17'), 'R998': ('0.13', '2 of 15')}
    for e in d['outcome']['texts']:
        r = e['label'].split(',')[0]
        if r not in sc: continue
        assert e.get('state') == 'decoded, not read'
        s, f = sc[r]
        e['reading'] = 'read/%s_reading.md' % r
        e['translation'] = 'read/%s_en.md' % r
        e['note'] = ("Re-read 22 Oct 2026 (b12): no contemporary decipherment, clear copy or edition exists (no margin; the "
                     "DECODE record has only the images). The key decode was segmented into Spanish word by word, with "
                     "second values that hold across the letters (63 = s, 77 = t, the r-sign = stra/tra, 69 = ru) and the "
                     "images checked at the breaks; the partial reading read/%s_reading.md scores %s clean sentences (%s), "
                     "below the 0.60 bar. Open: rare groups with no value in the key (no key material) and stretches where "
                     "the homophones do not segment; the 1616-px greyscale scans do not settle the doubtful figures." % (r, s, f))
    save(p, d, nl); print('bal texts ok')
STEPS[(B, 'texts')] = bal_texts
STEPS[(B, 'steps')] = lambda: add_steps(B, [
    {"date": "2026-10-22", "kind": "access", "what": "DECODE records R992, R996, R997, R998 re-fetched with the project cookie (b12_fetch.py): only the page images and DECODE's digit transcriptions; no decipherment attached, no margin on the cipher pages.", "result": "failed"},
    {"date": "2026-10-22", "kind": "reading", "technique": ["contextual inference"], "what": "The key decodes of R992, R996-R998 printed token by token (b12_bal.py) and segmented into Spanish words by hand; second values found to hold across the letters: 63 = s (los, demás, sus), 77 = t (nosotros, atraer), the r-sign = stra/tra (nuestra, tratar), 69 = ru (prudencia); images checked at the breaks (R992 l. 10: 42, not 48 = 'resolución violenta').", "result": "partial"},
    {"date": "2026-10-22", "kind": "verification", "technique": ["language-model scoring"], "what": "_check_reading.py on the partial readings (bodies): R992 0.29, R996 0.40, R997 0.41, R998 0.13 clean sentences; all four stay decoded, not read.", "result": "failed"}])

def bal_gaps():
    p, d, nl = load(B)
    o = d['outcome']
    o['key'] = 'partial'
    o['gaps'] = [
        {"item": "R992, R996, R997, R998: rare groups with no value in the key (fol, 85, 150, 182, 187, 17, 189, bon, i8 ...)", "blocker": "no-key-material", "detail": "once or twice in all fourteen letters, none in a margined letter; partial readings 0.13-0.41 clean sentences (22 Oct 2026)"},
        {"item": "R992, R996, R997, R998: stretches where the homophones do not segment into Spanish", "blocker": "needs-physical-access", "detail": "the 1616-px greyscale DECODE scans do not settle the doubtful (struck, overwritten) figures; originals at the AGR Brussels, SEG 2559"}]
    save(p, d, nl); print('bal gaps ok')
STEPS[(B, 'gaps')] = bal_gaps
