# Siena, Concistoro 2308 fasc. 2 no. 18 (DECODE R4806): treaty articles with the imperial side, subscribed by Niccolo Ziegler

Status: read in part — key recovered from the ciphertext alone; 1,271 of 1,459 cipher tokens (87.1%) read as Latin sense.

Split on 14 Oct 2026 from `siena1421` under the one-key rule (George Lasry, 14 Oct 2026). The old entry grouped the
whole bundle of Sienese cipher letters (Concistoro 2308 fasc. 2), each in its own key. These articles have a key of
their own; the other letters with recovered keys are their own entries, each a different cipher with its own page:
no. 25 ([`targets/siena25/`](../siena25/NOTES.md)), no. 14 ([`targets/siena14/`](../siena14/NOTES.md)), no. 4
([`targets/borghesi1456/`](../borghesi1456/NOTES.md)), nos. 6 and 24 (George Lasry's
[`targets/siena1431/`](../siena1431/NOTES.md)). The unread pieces, the key index and the shared solvers stay in
[`targets/siena1421/`](../siena1421/NOTES.md). The work below was done on 24 Sept 2026 and is carried over from its NOTES.

Work date: 2026-09-24. From catalogue 336 (now narrowed to the unread pieces).

## The document

ASSi Concistoro 2308, fasc. 2, no. 18, DECODE R4806 (`IMG_R4806_I27963_P1..P4`, 2248 x 4000; ASSi, git-ignored).
Four pages of Latin articles negotiated by Sienese orators with a King (Ser.mus Rex) and the Caesarea Maiestas, cipher
words throughout, point-separated like the clear words. P1 ends a first set of articles with "Niccolaus Zieglerr(?)
Regis Secretarius ss." (probably Niklas Ziegler, secretary of Maximilian I, d. 1526); P2 blank; P3-P4 further
articles ("petita ab oratoribus Senensibus").

## Transcription and key

- `transcripts/no18.txt` (agent K), verified against the images by agent L (`transcripts/no18v.txt`: 14 tokens
  changed in ~1,450). 211-212 point-divided cipher words, about 1,456-1,459 tokens, 30 signs.
- `homsolve2.py` (words=1, Latin) gave the key unaided (`keys/no18_key.txt`). Glyph splits found on the image: hooked
  n = q vs plain n = e; o = g vs lead-in o = o; open OO = i vs closed pair = ll; dotted signs = nulls; 2 = h, PHI = pp,
  HX = rr. None of the 43 filed keys fits.

## Reading

Agent L, `transcripts/no18_reading.txt`: "... tormenta ... lapides seu globos ... milia ducatorum pro quibus se obligabit
de restituendo eosdem in termino duorum mensium ... civitatem presentem statum cum omni eius iurisdictione tueri et
defendere teneatur ... bellum ... in partibus Pontis Valiani ... bellum Florentinis ... transitum, victualia,
instrumenta ad bellum necessaria, passum, foedus, intelligentia ... suis expensis centum homines armigeros, sexaginta
equos leves ... castella existentia infra ... miliaria prope fines Senenses que caperentur ... Florentinorum ...
bombarda". Ponte a Valiano = the Montepulciano war (1495-1511); Ziegler = Maximilian I's secretary: 1510s-1520s, year
not fixed [wrong: Pisa, Oct-Nov 1496, per George Lasry, 18 Oct 2026; see below]. **87.1% of 1,459 cipher tokens read as sense**, 10.6% doubtful, 1.4% unread, 0.9% struck.

Content: Siena to ready artillery and lend the King 5,000 ducats repayable in two months; B. protects Siena; Siena opens
war on X. near Ponte a Valiano at the King's and Emperor's request, gives passage and victuals against the Florentines,
100 men-at-arms and 60 light horse; castles taken within five miles of the border go to Siena; Siena's claims against
Florence judged by the Emperor; last article breaks off. B., X., S. and Mx. are written in clear and not resolved.

## Validation

`mk_validation.py` (written 14 Oct 2026) pairs the signs of `no18v.txt` with the reading's words line by line (6 lines
whose word counts differ are left out) and writes `validation.tsv`. `docs/_validate.py siena18 --write` (Latin model):
**underdetermined** — the reading beats random keys (z 4.3) and every shuffled refit (z 26.4), and the per-occurrence
reading scores −1.97, but the one-value-per-sign key K scores −2.46, below the annealer on the real text (−2.28): the
transcription keeps look-alike pairs under one sign name (o = g/o, n = q/e), so K is polyphonic (5.7%).

## 18-20 Oct 2026: George Lasry's independent solution and dating

George Lasry solved no. 18 independently (Oct 2026, after this project's reading of 24 Sept and the write-up of
25 Sept), ciphertext-only with CTTS and LLMs, and reads it in full; sent to Daniel Bourdeau on 18 Oct 2026 in his page
"The cipher documents of Concistoro 2308, fasc. 2" (kept outside the repository; see `targets/siena1421/NOTES.md`).

- **Dating: Pisa, October-November 1496**, Maximilian I's Italian expedition (Regesta Imperii XIV; Sanudo, Diarii I;
  Ulmann 1884; Pecci 1755): Siena to join the Holy League, accept "Caesar" as judge against Florence, lend 5,000
  ducats and make war at Ponte a Valiano; Ziegler is the King of the Romans' secretary. Our "1510s-1520s" (from
  Ziegler's later career and the King/Emperor pair) was wrong; title, year, page and ledgers corrected 20 Oct 2026.
- **His reading against ours.** His page prints one passage only: "restituerentur, ita t[ame]n q[uod] ipsi Senenses
  ad requisitionem Florentinorum sint contenti de stando iuri coram Cesare, dummodo Florentini etiam de illis que
  ipsi occupant sint contenti stare iuri coram ÷". `transcripts/no18_reading.txt` L4.24-28 has the same words in the
  same order (ours spells *ocupant*); cipher and clear words fall the same way. A full word-by-word comparison needs
  his complete decryption, which the page does not include; worth asking him for it.
- **His key against ours** (his table of 60 signs with counts, matched by shape to our names): every common sign
  has the same value (4, 7 = a; 3 = c; 9 = d; + = e; 6 = f; U = m; W = n; 8, o = o; L = p; D = r; h = s; N = t;
  Y = u; open OO = i), and so do the splits found here on the images (hooked n = q vs plain n = e; plain o = g;
  closed OO = ll; PHI = pp; HX = rr; 2 = h; dotted signs = nulls, his 181 + 50 null signs). Differences, all on rare
  signs: our d = a against his 'd' = i (4x); our a = i against his 'a' = u (3x); his letter sign for x ('H', 7x) and
  his 'w' = tt (3x) lie in our doubtful words (the W/m/tt gap below). `keys/no18_key.txt` still holds the pre-split
  values (2 = g, n = a, PHI = l) that the reading and this file had already corrected.
- His "M.X." = our unresolved "Mx."; his "B." = Liga (Sanctissima Liga?), "X." = the League's common enemy
  (unidentified), "S." = Sanctitas?
- Our outcome stays "read in part, 87.1%" (measured on our reading); his full reading is an independent
  verification of the key, and the first full reading, not this project's.

## Remaining gaps
- doubtful and unread words (about 12% of 1,459 tokens) - blocker: illegible; W/m/tt and dotted-null distinctions at the DECODE resolution (George Lasry reads them all; his full decryption, not on his page, would settle them)

## Escalation
- [x] siblings: the whole busta opened; no other piece in this key
- [x] clear-pages: none; the clear Latin around the cipher words is context, not a decipherment
- [x] known-keys: all 43 key sheets of fasc. 1 compared by eye; none fits
- [x] print: Meister 1902, Cecchini 1952: no printed text of these articles found
- [x] key-rebuild: key recovered by homsolve2 from the ciphertext alone; look-alike signs split on the image
- [x] retry: re-read sign by sign on the images with the extended key (two passes); doubtful words regraded in the reading file
