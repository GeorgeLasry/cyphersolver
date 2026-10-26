# Brief (1797 pages): transcribe deciphered cipher runs faithfully, marks included

Folder: C:\Users\dbour\cypher\targets\wilhelmina1795. Fetch each page at full size with
  curl -sL -A "Mozilla/5.0 Chrome/120" -o full/<id>.jpg "https://cms.koninklijkeverzamelingen.nl/api/images/rendition/<id>/original/"
(skip if it exists) and view it in horizontal strips (python PIL crops, about 1/6 of the page height at full width,
saved in your scratch folder, opened with the Read tool). Zoom further on small marks.

Letters of the Hereditary Prince, Berlin, Sept 1796 - 1797, French. Cipher runs of numbers stand among clear
words or fill the page; a faint contemporary decipherment (pencil or ink) is written above or between the lines.
The code is a numbered word list, but the 1797 group rules are NOT yet known (entries run to about 720; a '0'
appears often; single digits are underlined; small numbers sit top-left or top-right of a number). So transcribe
EXACTLY what is written and do not normalise:

- separate items by spaces, keep the commas as written: `608,4,3,19 432,8,9 27_ 42 312,1,2,3,0`
  (one item = a number and the comma-joined numbers after it up to the next big number, as you judge it; if
  unsure, keep commas and let the reader split)
- underline under a whole number or digit: put `_` right after it (`4_`, `27_`); double underline `__`
- bar or stroke over a number: `^bar` after it
- small number k top-left of N: `k)N`; small number k top-right: `N^k`
- unreadable: `?`

For each cipher line (one line of numbers on the page) write a block:

    # scan <n> id <id> line <k>
    PT: <the decipherment written over/under that line, exactly as written, ASCII>
    CT: <the items in the notation above>
    AL: <your best alignment item=plaintext piece ..., with the item copied IN FULL from CT, marks included>

AL is a guess and may have `?`; PT and CT must be faithful. Note on its own line `OBS:` anything you notice about
how the system works (e.g. "0 seems to end a word", "underlined digit = ..."). Append each block to the output file
as soon as it is done. ASCII only (accents dropped). At the end reply with pages done, lines, items, and your OBS
summary.
