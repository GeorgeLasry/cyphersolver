# Brief: transcribe interlined cipher pages as aligned group=output pairs

Folder: C:\Users\dbour\cypher\targets\wilhelmina1795. Pages are KHA scans; fetch each full-size original with
  curl -sL -A "Mozilla/5.0 Chrome/120" -o full/<id>.jpg "https://cms.koninklijkeverzamelingen.nl/api/images/rendition/<id>/original/"
(skip if full/<id>.jpg exists). View it in horizontal strips (python PIL crops of about 1/5 of the page height at full
width, saved in your scratch folder, opened with the Read tool). Zoom further on small marks.

The letters are in French (one Dutch letter, scan 60). Cipher runs sit inside clear text; a contemporary
decipherment is written above each run (sometimes in pencil, faint). The code is a numbered word list:

| written | notation to use | meaning |
|---|---|---|
| N with a single underline | `N_` | the whole entry N |
| N followed by ,p,q,r | `N,p,q,r` | letters p, q, r of entry N |
| small number k at the top LEFT of N, often with a slash (k/N, k)N) | `k)N` | entry N without its first k letters |
| small number k at the top RIGHT of N | `N^k` | entry N without its last k letters |
| both | `k)N^j` | |

Double underlines, bars over a digit and over-strokes mark group ends: ignore them (do NOT treat a bar over 1 as
anything but the digit). A position list belongs to the entry before it: "50,6,7,1" is ONE group `50,6,7,1`.
Example (scan 21): "50,6,7,1, 128^4, 67,1,2,5, 118_, 37^1, 3)101^1" under "des bonnes dispositions du Ministre".

For each cipher run write a block to the output file:

    # scan <n> id <id> line <k>
    PT: <the decipherment written above the run, exactly as written>
    CT: <the groups in order, space separated, in the notation above>
    AL: <group>=<plaintext piece> <group>=<plaintext piece> ...

AL is your alignment: split the plaintext among the groups (each group yields a piece of letters; a whole-entry
group yields a word or phrase). Use what the table must give: `N,p,q` yields as many letters as positions, and the
same entry number must always be the same word. Prior entries known from a sibling letter are in key_prior.txt
(number word; '.' = unknown letter): use them to check, and note any clash with `CLASH:` on its own line.
If a group or the decipherment is unreadable write `?` for it; never guess silently. ASCII only: write accented
letters without accents (e with acute -> e).

Append each block to the output file as soon as it is done (never hold blocks to the end). Do not write any
non-ASCII sign. At the end reply with: pages done, runs, groups, clashes, and pages you could not read.
