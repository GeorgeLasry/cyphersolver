"""Page edits (docs/<slug>.html) for the relabel_docs_2 targets (RELABEL_DOCS_BRIEF.md), 22 Oct 2026. Run once.

Each entry is an exact (old, new) replacement; the script stops if an old string is missing or not unique.
Pages whose claim did not change (overturned grades, not-prose labels) are not touched; richelieu's page claims only
the key and Avenel's agreement, so it is left as is.
"""
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
RA = 'reading audit, 22 October 2026'
DNR = 'decoded, not read'

R = {
 'norfolk1570': [
  ('IIIF images; a few signs and words remain open.',
   'IIIF images; a few signs and words remain open, and holes fall in about half the lines, so the letter counts as '
   + DNR + ' (' + RA + ').'),
  ('and the decipherment of the whole letter, with five signs and some spots still open',
   'and a decryption of the whole letter, with five signs and some spots still open; holes fall in about half the '
   'lines, so it counts as ' + DNR),
  ('<em>Status: all 23 lines transcribed and decrypted.',
   '<em>Status: all 23 lines transcribed and decrypted, but not yet read as sentences: [..] holes or unkeyed signs fall '
   'in lines 1, 4&ndash;6, 8&ndash;10 and 12&ndash;17, so the letter counts as ' + DNR + ' (' + RA + ').'),
 ],
 'numeric1916': [
  ('1,940 of 2,100 cipher groups give a character without doubt.',
   '1,940 of 2,100 cipher groups give a character without doubt. In this repository only the 辰密 telegrams read as '
   'sentences; the 共密 and 容密 decodes still carry garbled clusters and count as ' + DNR + ' (' + RA + ').'),
  ('<span class="gl-res">Ciphertext-only recovery &middot; partial &middot; 1,940 of 2,100 groups</span>',
   '<span class="gl-res">Ciphertext-only recovery &middot; partial &middot; 1,940 of 2,100 groups decoded; 辰密 read, '
   '共密 and 容密 ' + DNR + '</span>'),
  ('<dt>Still open</dt><dd>154 doubtful',
   '<dt>Still open</dt><dd>The 共密 and 容密 decodes in this repository have clusters of wrong characters (N32, N33, N35; '
   'N19b, N21, V4D) that break whole clauses, and no translation; Dudout&rsquo;s Wenmi pages carry his edited texts '
   '(' + RA + '). 154 doubtful'),
 ],
 'nunzio1718': [
  ('measured here, it gives a value to 97.6 per cent of cipher tokens.',
   'measured here, it gives a value to 97.6 per cent of cipher tokens. Two despatches, R154 and R173, still have unread '
   'groups in most sentences and count as ' + DNR + ' (' + RA + ').'),
  ('and 61 of its 189 groups without a value are recovered</p>',
   'and 61 of its 189 groups without a value are recovered &middot; two despatches, R154 and R173, still have unread '
   'groups in most sentences and count as ' + DNR + ' (' + RA + ')</p>'),
 ],
 'orbais': [
  ('The decryption is partial: 75 of the 91 cipher signs give sense (82%), and three code signs and two short runs stay open.',
   'The cipher runs are decoded: 75 of the 91 cipher signs give sense (82%), and three code signs and two short runs '
   'stay open. The clear text of the letter is not transcribed here, so the runs are not yet set in sentences and the '
   'letter counts as ' + DNR + ' (' + RA + ').'),
  ('&middot; partial: 75 of the 91 cipher signs give sense (82%, measured); three code signs and two short runs, 16 signs, are still open</p>',
   '&middot; decoded: 75 of the 91 cipher signs give sense (82%, measured); three code signs and two short runs, 16 signs, '
   'are still open; the clear text around them is not transcribed, so the letter counts as ' + DNR + '</p>'),
  ('and two short runs of six and seven signs, 16 signs in all.</em>',
   'and two short runs of six and seven signs, 16 signs in all. The letter&rsquo;s clear text is not transcribed in this '
   'repository, so the runs are not yet set in sentences and the letter counts as ' + DNR + ' (' + RA + ').</em>'),
 ],
 'poyntz1527': [
  ('Nothing was left to decipher; the work was identifying the letter from the calendar and correcting the catalogue.</p>',
   'Nothing was left to decipher; the work was identifying the letter from the calendar and correcting the catalogue. '
   'Tuke&rsquo;s decipherment itself is not yet transcribed in this repository (' + RA + ').</p>'),
 ],
 'rakoczi1704': [
  ('found to fit this correspondence and corrected from the key image (97% of groups);',
   'found to fit this correspondence and corrected from the key image (97% of groups take a value, but the decodes are '
   'syllable-split with misreadings in most lines and count as ' + DNR + ');'),
  ('two were deciphered with the Bonac–Groffey key DECODE R639 after the key and the letters were transcribed again from the images, and the third has its own contemporary clear copy.</p>',
   'two were decoded with the Bonac–Groffey key DECODE R639 after the key and the letters were transcribed again from the '
   'images, though the decodes do not yet build sentences (' + DNR + ', ' + RA + '), and the third has its own '
   'contemporary clear copy.</p>'),
 ],
 'rakoczi1711': [
  ('checked here against a 224-code syllabic key rebuilt from it by alignment.">',
   'checked here against a 224-code syllabic key rebuilt from it by alignment. The transcription, merged with the clear '
   'passages, still has doubts on most lines and is not in reading order, so the letter counts as ' + DNR + ' (' + RA +
   ').">'),
  ('<span class="gl-res">Existing decipherment &middot; 2,524 of 2,531 groups under the clerk’s interlinear</span>',
   '<span class="gl-res">Existing decipherment &middot; 2,524 of 2,531 groups under the clerk’s interlinear &middot; '
   + DNR + ': not yet a running text</span>'),
  ('<dt>Still open</dt><dd>An edited Latin text line by line,',
   '<dt>Still open</dt><dd>The merged text has doubts or alternatives on most lines and is not in reading order, so the '
   'letter counts as ' + DNR + ' (' + RA + '). An edited Latin text line by line,'),
 ],
 'ranzo1528': [
  ('no. 20 reads 94.4&nbsp;%, fr. 4050 87.7&nbsp;%, fr. 6638 89.0&nbsp;%; 92.9&nbsp;% of 6,428 groups in all.</em>',
   'no. 20 reads 94.4&nbsp;%, fr. 4050 87.7&nbsp;%, fr. 6638 89.0&nbsp;%; 92.9&nbsp;% of 6,428 groups in all. In letter 4 '
   '(fr. 4050) runs of open codes break most sentences of the middle, so it counts as ' + DNR + '; in the four letters '
   'that read, 4,606 of the 6,428 groups give sense (71.7&nbsp;%, ' + RA + ').</em>'),
 ],
 'rome1536': [
  ('without publishing any plaintext, was applied and corrected: about 95% of the cipher letters are decrypted.',
   'without publishing any plaintext, was applied and corrected: about 95% of the cipher letters of the seven fr. 3053 '
   'records are decrypted; the letter in fr. 3071, only 35-40% decrypted with confidence, counts as ' + DNR + ' (' + RA + ').'),
  ('About 95&nbsp;% of the cipher letters are decrypted, checked against six contemporary decipherments in the volume.</p>',
   'About 95&nbsp;% of the cipher letters of fr. 3053 are decrypted, checked against six contemporary decipherments in '
   'the volume; only 35&ndash;40&nbsp;% of the fr. 3071 letter is decrypted with confidence, and it counts as ' + DNR + ' (' + RA + ').</p>'),
 ],
 'santacruz1399': [
  ('<span class="gl-res">Deciphered in print, 1920 &middot; about 100 words</span>',
   '<span class="gl-res">Deciphered in print, 1920 &middot; about 100 words; the printed text is not in this '
   'repository</span>'),
  ('The original is in the Arxiu Capitular de Barcelona, not digitised.</dd>',
   'The original is in the Arxiu Capitular de Barcelona, not digitised. Puig&rsquo;s printed text is not in this '
   'repository either (Google Books now blocks it to scripts), so its words are not reproduced here (' + RA + ').</dd>'),
 ],
 'r9416': [
  ('faint words of the f. 262 gloss.</dd>',
   'faint words of the f. 262 gloss, whose first page does not yet build sentences, so f. 262 counts as ' + DNR + ' (' +
   RA + ').</dd>'),
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
