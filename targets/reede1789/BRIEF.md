# Brief: transcribe Van Reede's glossed cipher runs (letters to Princess Wilhelmina, Berlin 1789-92, KHA A32-545-547)

Folder: C:\Users\dbour\cypher\targets\reede1789. Fetch each page at full size:
  curl -sL -A "Mozilla/5.0 Chrome/120" -o full/<id>.jpg "https://cms.koninklijkeverzamelingen.nl/api/images/rendition/<id>/original/"
(mkdir full first; skip if present). View in horizontal strips (python PIL crops of about 1/6 page height at full
width, saved to your scratch folder, opened with the Read tool); zoom more on marks.

The letters are French, with runs of cipher groups among clear words. Groups are numbers of 1-3 digits ended by
a dot ("355. 349. 166."). MARKS on single digits matter: underlines under a digit (single, double, triple, wavy),
a prime or accent above or after a digit, a "+" above/below, dots. The decipherment is written above the groups.

Notation for each group: the number, then each mark in braces with its kind and the 1-based digit position it sits
on: `355{'3}` (prime on 3rd digit), `349{u3}` single underline under 3rd digit, `{uu2}` double, `{uuu1}` triple,
`{w2}` wavy, `{+1}` plus, `{..2}` dots, `{bar}` stroke over the whole number. Several marks: `225{u2}{'3}`.
No mark: just `225`. Unreadable: `?`.

For each run (a stretch of groups between clear words, or one manuscript line of groups) write:

    # scan <n> id <id> run <k>
    PT: <the decipherment written over the run, exactly; ASCII, accents dropped; struck-out words in (( ))>
    CT: <groups in notation, space separated>
    AL: <group>=<plaintext piece> ... (each group copied IN FULL from CT, marks included; ? if unsure)

Each group is usually one word or syllable; align left to right with the gloss. Append each block to the output
file as soon as done. ASCII only. Note `OBS:` lines on how the marks seem to work (e.g. same number with and
without a mark glossed differently). Final reply: pages, runs, groups, OBS summary.
