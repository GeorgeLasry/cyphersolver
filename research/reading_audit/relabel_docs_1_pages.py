"""Page edits (docs/<slug>.html) for the relabel_docs_1 targets (RELABEL_DOCS_BRIEF.md), 22 Oct 2026. Run once.

Each entry is an exact (old, new) replacement; the script stops if an old string is missing or not unique.
"""
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
RA = 'reading audit, 22 October 2026'

R = {
 'esp318': [
  ('and about three quarters of the letter is deciphered with it.">',
   'and about three quarters of the letter&rsquo;s words take a value with it; the decode still has holes in most cipher '
   'sentences, so the letter counts as decoded, not read (' + RA + ').">'),
  ('the key, proved against a later hand&rsquo;s glosses, deciphers about three quarters of the letter.</p>',
   'the key, proved against a later hand&rsquo;s glosses, gives a value to about three quarters of the words, but the '
   'decode does not yet build sentences: decoded, not read.</p>'),
  ('<span class="gl-res">Known key applied &middot; partial, about three quarters of the words</span>',
   '<span class="gl-res">Known key applied &middot; decoded, not read: about three quarters of the words take a value</span>'),
  ('<dt>Still open</dt><dd>Five code groups that contradict the printed key, and about ten stretches of letter signs.</dd>',
   '<dt>Still open</dt><dd>Five code groups that contradict the printed key, and about ten stretches of letter signs. With '
   'them, f. 116r ll. 8&ndash;11, 16, 18&ndash;21, 26&ndash;31 and 34 are sign strings rather than sentences, so most cipher '
   'sentences have holes and the letter is decoded, not read (' + RA + '); &ldquo;What it says&rdquo; is a gist.</dd>'),
 ],
 'esp318no94': [
  ('the letter, on the aftermath of Seminara and the death of Portocarrero, can be followed in outline.',
   'the letter, on the aftermath of Seminara and the death of Portocarrero, can be followed in outline, but his '
   'decryption has holes in most sentences, so it counts as decoded, not read (' + RA + ').'),
  ('<span class="gl-res">Key recovered from the ciphertext &middot; partial: all letter signs, 376 of 612 code tokens firm</span>',
   '<span class="gl-res">Key recovered from the ciphertext &middot; decoded, not read: all letter signs, 376 of 612 code '
   'tokens firm</span>'),
  ('<dt>Still open</dt><dd>About 90 code groups (143 tokens), 14 tentative readings, and spelled-out stretches that do not yet parse. Single words stay provisional.</dd>',
   '<dt>Still open</dt><dd>About 90 code groups (143 tokens), 14 tentative readings, and spelled-out stretches that do not '
   'yet parse. Single words stay provisional. With these open, most sentences of the decryption have holes, and the '
   'decryption is still only in issue #62, not in the folder: the letter is decoded, not read (' + RA + ').</dd>'),
 ],
 'eugenie1859': [
  ('Deciphered by George Lasry (BnF cipher research, October 2026); spot-checked here.">',
   'Deciphered by George Lasry (BnF cipher research, October 2026); spot-checked here. Only four pages of his tokens and '
   'three excerpts are in this repository.">'),
  ('in his <i>BnF cipher research</i> of October 2026: 440 elements, 370 identified (84.1%); 4 assumed readings; 50 ?.</p>',
   'in his <i>BnF cipher research</i> of October 2026: 440 elements, 370 identified (84.1%); 4 assumed readings; 50 ?. Read '
   'by Lasry; excerpt here: this repository holds his tokens for ff. 9r, 15r, 17r and 18r and three excerpts of his report, '
   'which read as French sentences; the rest of his decipherment is not here (' + RA + ').</p>'),
 ],
 'exea1408': [
  ('<span class="gl-res">Deciphered in print, 1920 &middot; about 2,090 words</span>',
   '<span class="gl-res">Deciphered in print, 1920 &middot; about 2,090 words; the printed text is not in this '
   'repository</span>'),
  ('<dt>Still open</dt><dd>The ciphertext: no image of the letter exists, so the cipher and its key are unknown. The original is in the Arxiu Capitular de Barcelona, not digitised.</dd>',
   '<dt>Still open</dt><dd>The ciphertext: no image of the letter exists, so the cipher and its key are unknown. The original '
   'is in the Arxiu Capitular de Barcelona, not digitised. Puig&rsquo;s printed text is not in this repository either '
   '(Google Books blocks it to scripts), so the letter is not counted as read here (' + RA + ').</dd>'),
 ],
 'haga1620': [
  ('was applied and deciphers both records.',
   'was applied and decodes both records. R2113 reads as sentences; R2115 is only partly transcribed and its cipher '
   'spans have holes in most sentences, so it is decoded, not read (' + RA + ').'),
 ],
 'hesse1672': [],
 'hm1645': [
  ('Lasry deciphered them on DECODE in 2020; his plaintext is the text here, and his key',
   'Lasry deciphered them on DECODE in 2020; his plaintext, on DECODE and not copied into this repository, is the text, '
   'and his key'),
  ('<span class="gl-res">Existing decipherment &middot; 3069 of 3373 groups have a value in the key</span>',
   '<span class="gl-res">Existing decipherment, on DECODE &middot; 3069 of 3373 groups have a value in the key; '
   'the plaintext is not in this repository</span>'),
  ('His plaintext is the text here. Applied here group by group',
   'His plaintext is the text; it stays on DECODE as his work and is not in this repository, so the three letters count '
   'here as decoded, not read until it is fetched and checked again (' + RA + '). Applied here group by group'),
 ],
 'it1583': [
  ('87% of the 827 cipher signs give sense; 47 sign occurrences and the signature of f. 70 are open.">',
   '87% of the 827 cipher signs give sense; 47 sign occurrences and the signature of f. 70 are open. f. 68 reads as '
   'sentences; f. 70 has holes in every clause of its first five lines and counts as decoded, not read (' + RA + ').">'),
  ('<span class="gl-res">Key recovered from the ciphertext alone, partial &middot; 721 of 827 cipher signs give sense</span>',
   '<span class="gl-res">Key recovered from the ciphertext alone, partial &middot; f. 68 read, f. 70 decoded, not '
   'read</span>'),
  ('<dt>Still open</dt><dd>47 sign occurrences in 14 sign classes, mostly at line openings; three provisional values; the signature block of f. 70; a few clear words over damaged strokes.</dd>',
   '<dt>Still open</dt><dd>47 sign occurrences in 14 sign classes, mostly at line openings; three provisional values; the '
   'signature block of f. 70; a few clear words over damaged strokes. On f. 70 the open signs fall inside every clause of '
   'lines 1&ndash;5, so that letter is decoded, not read (' + RA + ').</dd>'),
 ],
 'kauderbach1754': [
  ('All ten letters are decrypted, 65&ndash;97% of the cipher per letter.</p>',
   'All ten letters are decrypted, 65&ndash;97% of the cipher per letter; nine read as sentences, and R1954 (about 65%, on a '
   'weak transcription) is decoded, not read (' + RA + ').</p>'),
  ('In each letter 65&ndash;97% of the cipher now decrypts to sense.',
   'In each letter 65&ndash;97% of the cipher now decrypts to sense; nine letters read as sentences, while R1954, from a '
   'weak transcription, has holes in most sentences and is decoded, not read (' + RA + ').'),
 ],
 'maisse1593': [
  ('Contemporary clear copies of both in Brienne 13 (BnF NAF 6984) give the full text,',
   'Contemporary clear copies of both in Brienne 13 (BnF NAF 6984) give the full text (not yet transcribed here, so the '
   'letters count as decoded, not read: ' + RA + '),'),
  ('<span class="gl-res">Existing decipherment &middot; full text from the clear copies; cipher not deciphered here</span>',
   '<span class="gl-res">Not read here &middot; full text in the clear copies, not yet transcribed; cipher not deciphered '
   'here</span>'),
  ('<dt>Still open</dt><dd>Tomokiyo&rsquo;s key for this cipher is in hand but was not applied:',
   '<dt>Still open</dt><dd>The Brienne 13 copies are located but not transcribed, so no text of either letter is in this '
   'repository and neither counts as read (' + RA + '). Tomokiyo&rsquo;s key for this cipher is in hand but was not applied:'),
 ],
 'marechaux1520': [
  ('His key was applied here to the second page, f. 41v, which had no published decipherment.">',
   'His key was applied here to the second page, f. 41v, which had no published decipherment. Lasry&rsquo;s f. 41r is on '
   'overlay images only and is not transcribed in this repository.">'),
  ('One symbol and one code group are open; 99.9% of the page&rsquo;s cipher letters have a value.</div>',
   'One symbol and one code group are open; 99.9% of the page&rsquo;s cipher letters have a value. Lasry&rsquo;s reading of '
   'f. 41r exists only as his overlay images, with no text of it in this repository, so the leaf counts as read in part here '
   '(' + RA + ').</div>'),
 ],
 'matignon1586c3': [
  ('All three use Satoshi Tomokiyo&rsquo;s partial key, checked on siblings deciphered at the time: 3,719 of 4,079 signs read as French, measured.">',
   'All three use Satoshi Tomokiyo&rsquo;s partial key, checked on siblings deciphered at the time: 3,719 of 4,079 signs fall '
   'in runs of French, measured. The two slips read as sentences; the despatch is a machine decode with a garbled word in '
   'nearly every sentence, decoded, not read (' + RA + ').">'),
  ('deciphered with Tomokiyo&rsquo;s key by alejandrozarco and Brett Burford: 3,719 of 4,079 signs read as French.</p>',
   'deciphered with Tomokiyo&rsquo;s key by alejandrozarco and Brett Burford: the two slips read; the despatch is decoded, '
   'not read.</p>'),
  ('<span class="gl-res">Known key applied &middot; partial, 3,719 of 4,079 signs (91.2%)</span>',
   '<span class="gl-res">Known key applied &middot; partial: the two slips read (1,243 of 4,079 signs); the despatch '
   'decoded, not read</span>'),
  ('In the despatch, five rare code signs and about a tenth of the signs, mostly names and misread signs.</dd>',
   'In the despatch, five rare code signs and about a tenth of the signs, mostly names and misread signs; nearly every '
   'sentence has a garbled word, so the despatch is decoded, not read (' + RA + ').</dd>'),
 ],
 'mayenne1586c2': [
  ('4,560 of 5,293 signs fall in runs of French, measured, but no person has yet checked the transcriptions.">',
   '4,560 of 5,293 signs fall in runs of French, measured, but no person has yet checked the transcriptions. Matignon&rsquo;s '
   'despatch reads as sentences; the two Guyenne letters have holes in most sentences and are decoded, not read (' + RA + ').">'),
  ('deciphered by two outside contributors with Tomokiyo&rsquo;s key: most of the text reads, none of it yet checked by hand.</p>',
   'deciphered by two outside contributors with Tomokiyo&rsquo;s key: Matignon&rsquo;s despatch reads, the other two are '
   'decoded, not read, and none of it is yet checked by hand.</p>'),
  ('<span class="gl-res">Known key applied &middot; partial, 4,560 of 5,293 signs in runs of French (86.1%)</span>',
   '<span class="gl-res">Known key applied &middot; partial: ff. 218&ndash;219 read (2,138 of 5,293 signs); ff. 120 and 385 '
   'decoded, not read</span>'),
  ('<dt>Still open</dt><dd>About 22 code signs, short stretches in all three letters, and a check of the transcriptions by a person.</dd>',
   '<dt>Still open</dt><dd>About 22 code signs, short stretches in all three letters, and a check of the transcriptions by a '
   'person. In f. 120 and f. 385 the open stretches fall in most sentences, so those two letters are decoded, not read '
   '(' + RA + ').</dd>'),
 ],
 'meryvic1589': [
  ('Deciphered by George Lasry (BnF cipher research, October 2026); spot-checked here.">',
   'Partly deciphered by George Lasry (BnF cipher research, October 2026); only his excerpts are in this repository, with '
   'holes in every sentence, so the letter counts here as decoded, not read; spot-checked here.">'),
  ('in his <i>BnF cipher research</i> of October 2026: 545 elements, 523 identified (96.0%).</p>',
   'in his <i>BnF cipher research</i> of October 2026: 545 elements, 523 identified (96.0%). His report calls the letter '
   'partly deciphered; the two excerpts in this repository have holes in every sentence, so it counts here as decoded, not '
   'read (' + RA + ').</p>'),
 ],
}


def edit(slug):
    f = ROOT / 'docs' / (slug + '.html')
    s = f.read_bytes().decode('utf-8')
    for old, new in R[slug]:
        n = s.count(old)
        if n != 1:
            raise SystemExit(f'{slug}: {n} matches for {old[:80]!r}')
        s = s.replace(old, new)
    f.write_bytes(s.encode('utf-8'))
    print('ok', slug, len(R[slug]))


if __name__ == '__main__':
    for n in sys.argv[1:]:
        edit(n)
