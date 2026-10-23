"""Page edits (docs/<slug>.html) for the relabel_docs_3 targets (RELABEL_DOCS_BRIEF.md), 22 Oct 2026. Run once.

Each entry is an exact (old, new) replacement; the script stops if an old string is missing or not unique.
Pages whose claim did not change (overturned grades, not-prose labels, urquhart's distich) are not touched;
soria1527, vargas1552 and walsingham1581 have no page.
"""
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
RA = 'reading audit, 22 October 2026'
DNR = 'decoded, not read'


def sp106(n, groups):
    return [
        ('deciphered it on DECODE in 2020; his plaintext is the text here, and his key',
         'deciphered it on DECODE in 2020; his plaintext, on DECODE and not copied into this repository, is the text, '
         'and his key'),
        ('<span class="gl-res">Existing decipherment &middot; ' + groups + ' groups have a value in the key</span>',
         '<span class="gl-res">Existing decipherment, on DECODE &middot; ' + groups + ' groups have a value in the key; '
         'the plaintext is not in this repository</span>'),
        ('His plaintext is the text here. Applied here group by group',
         'His plaintext is the text; it stays on DECODE as his work and is not in this repository, so the letter counts '
         'here as ' + DNR + ' until it is fetched and checked again (' + RA + '). Applied here group by group'),
    ]


R = {
 'sp106r787': sp106('R787', '1538 of 1569'),
 'sp106r924': sp106('R924', '1850 of 2012'),
 'sp106r929': [
  ('<span class="gl-res">Known key applied &middot; 293 of 348 groups</span>',
   '<span class="gl-res">Known key applied &middot; 293 of 348 groups; the plaintext is not in this repository</span>'),
  ('All 293 groups it gives a value agree with his text.',
   'All 293 groups it gives a value agree with his text. His plaintext stays on DECODE as his work and is not in this '
   'repository, so the letter counts here as ' + DNR + ' until it is fetched and checked again (' + RA + ').'),
 ],
 'swieten1759': [
  ('<span class="gl-res">Ciphertext-only break &middot; 532 of 553 groups</span>',
   '<span class="gl-res">Ciphertext-only break &middot; 532 of 553 groups decrypted; the February letter reads, the '
   'January letter is ' + DNR + '</span>'),
  ('<dt>Still open</dt><dd>About 21 groups, nearly all proper names.</dd>',
   '<dt>Still open</dt><dd>About 21 groups, nearly all proper names. In the letter of 14 January two of the four '
   'sentences do not yet build (&ldquo;On promet de toujours&hellip;&rdquo; and the clause after &ldquo;le prince de '
   'Con[&hellip;]&rdquo;), so it counts as ' + DNR + ' (' + RA + ').</dd>'),
 ],
 'windischgraetz1721': [
  ('stay open because neither the key nor the letter fixes them.',
   'stay open because neither the key nor the letter fixes them. With those codes open and the clear text of the later '
   'pages only excerpted, about half the sentences do not build, so the letter counts as ' + DNR + ' (' + RA + ').'),
  ('<li>All letter-spelled words are grade H: the key gives them without choice.</li>',
   '<li>All letter-spelled words are grade H: the key gives them without choice.</li>\n<li><b>Reading audit, 22 October '
   '2026.</b> The first page and the left half of the second opening build sentences; on the later pages open codes, '
   'guesses and clear text given only in extract leave holes in most clauses. The letter counts as ' + DNR + ' until '
   'the clear text is transcribed in full and a running German text is written.</li>'),
 ],
 'wotton1585': [
  ('The drafts were transcribed and the code numbers identified from the surrounding cleartext:',
   'The code numbers were identified from the surrounding cleartext (the drafts are not yet transcribed in this '
   'repository, so they count as ' + DNR + ', ' + RA + '):'),
  ('The drafts were transcribed in full and the code numbers identified from the cleartext around them.',
   'The code numbers were identified from the cleartext around them; the drafts themselves are not yet transcribed in '
   'this repository, so the three count as ' + DNR + ' (' + RA + ').'),
  ('No cipher had to be broken: the drafts were transcribed as they stand, and the work was to identify eleven code numbers.',
   'No cipher had to be broken: the drafts can be read as they stand, and the work was to identify eleven code numbers. '
   'Only summaries and the code table are in this repository, not a transcription, so the drafts count as ' + DNR +
   ' (' + RA + ').'),
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
