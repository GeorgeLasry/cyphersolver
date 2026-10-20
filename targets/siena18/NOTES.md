# Siena, Concistoro 2308 fasc. 2 no. 18 (DECODE R4806): treaty articles with the imperial side, subscribed by Niccolo Ziegler

Status: read — key recovered from the ciphertext alone, twice and independently: by this project on 24 Sept 2026 (1,271 of 1,459 cipher tokens, 87.1%, read as Latin sense) and by George Lasry with CTTS and Claude on 15-17 Oct 2026, whose complete reading (all cipher passages, six single signs unread) is now the entry's reading. Dated by him to Pisa, November 1496 (ours: 1510s-1520s, withdrawn).

Split on 14 Oct 2026 from `siena1421` under the one-key rule (George Lasry, 14 Oct 2026). The old entry grouped the
whole bundle of Sienese cipher letters (Concistoro 2308 fasc. 2), each in its own key. These articles have a key of
their own; the other letters with recovered keys are their own entries, each a different cipher with its own page:
no. 25 ([`targets/siena25/`](../siena25/NOTES.md)), no. 14 ([`targets/siena14/`](../siena14/NOTES.md)), no. 4
([`targets/borghesi1456/`](../borghesi1456/NOTES.md)), nos. 6 and 24 (George Lasry's
[`targets/siena1431/`](../siena1431/NOTES.md)). The unread pieces, the key index and the shared solvers stay in
[`targets/siena1421/`, now the collection index `research/siena2308/`](../../research/siena2308/README.md). The work below was done on 24 Sept 2026 and is carried over from its NOTES.

Work date: 2026-09-24. From catalogue 336 (now narrowed to the unread pieces).

## George Lasry's independent solution (17 Oct 2026)

George Lasry, "The cipher documents of Concistoro 2308, fasc. 2" (report sent by email to Daniel Bourdeau, 17 Oct
2026), section F "The imperial chancery cipher of 1496": "Solved: all cipher passages read; parties and date
identified. 15–17 October 2026, by George Lasry with CTTS and Claude: transcription by Claude, refined by the author
in CTTS; key recovered by Claude from cribs taken from the surrounding clear text." His whole section, with the full
decryption and translation, is quoted verbatim in `lasry_report.md`; his key figure is `docs/siena18_key.png`.

One key, two contributions. The project's key (24 Sept, `keys/no18_key.txt`, homsolve2 with a Latin model,
look-alikes split on the images) came first; his was recovered without it. Both are ciphertext-only (his cribs are
taken from the clear Latin around the cipher words, within the same document). His reading is adopted as the entry's
reading because it covers what ours left open; ours stays in `transcripts/` as the project's own result.

**Key agreement** (`lasry_comparison.md`): of the 38 letter and doubled-letter signs of his key, 35 carry the same
value in ours (32 as separately named signs, 3 as glyphs our transcription merged with a look-alike: the small ш = m,
the hooked 7-like q, the dotted U = u); 1 differs (his cc, our single c for the TRI sign); 2 single-occurrence signs
are not in ours (his second r, on the paper flaw of *armature*, and a hooked a). Both treat dotted and barred signs
as nulls and leave the code capitals B., X., S., M.X. in clear (his m. = our n.).

**Reading differences**, graded in `lasry_comparison.md`: his text reads the words ours left unread or doubtful
(*Telamonem*, *in ordinem* where we saw a struck word, *que* after B., *pax* for our *passo?*, *defendat* for our
*defendam*, *quote* for *quoti*, *ius competit*, *armature*); 10 at H, 3 at M (*Telamonem*, *pax*,
*s[anctissima]?*). Six single signs stay unread in his text (÷ ×4, ✱ ×2). Clear-text readings differ in six places;
his are the grammatical ones.

**Dating**: his Pisa, November 1496 (Maximilian I at Pisa, Ziegler secretary from 1494, the Holy League of 1495,
Ponte a Valiano 1496; Regesta Imperii XIV, Pecci, Sanudo, Guicciardini) replaces our 1510s-1520s. His page order
P4, P3, P1 is the order of the negotiation.

Fraction read (his reading): all cipher passages; the unread marks in his text are ÷ four times and ✱ twice, single
signs each, plus one query (s[anctissima]?, counted as one unread sign): 1,462 of his 1,469 cipher signs, 99.5%.

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
not fixed [wrong: Pisa, Oct-Nov 1496, per George Lasry; see above]. **87.1% of 1,459 cipher tokens read as sense**, 10.6% doubtful, 1.4% unread, 0.9% struck.

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

## 20 Oct 2026: a second comparison, from his page (main branch, merged)

A parallel session on main (commit 883fa6f41), working from George Lasry's page of 18 Oct 2026 before this entry's
18 Oct comparison was merged in, compared again; what it adds:

- **Dating sources**: Pisa, October-November 1496, Maximilian I's Italian expedition (Regesta Imperii XIV; Sanudo,
  Diarii I; Ulmann 1884; Pecci 1755): Siena to join the Holy League, accept "Caesar" as judge against Florence, lend
  5,000 ducats and make war at Ponte a Valiano; Ziegler is the King of the Romans' secretary. Our "1510s-1520s" came
  from Ziegler's later career and the King/Emperor pair. His report (section F) has November 1496,
  his page October-November; the title and ledgers keep the report's November 1496.
- **His printed passage equals ours**: the passage on his page, "restituerentur, ita t[ame]n q[uod] ipsi Senenses ad
  requisitionem Florentinorum sint contenti de stando iuri coram Cesare, dummodo Florentini etiam de illis que ipsi
  occupant sint contenti stare iuri coram ÷", is word for word `transcripts/no18_reading.txt` L4.24-28 (ours spells
  *ocupant*); cipher and clear words fall the same way.
- **Key compared by shape**: every common sign has the same value (4, 7 = a; 3 = c; 9 = d; + = e; 6 = f; U = m; W = n;
  8, o = o; L = p; D = r; h = s; N = t; Y = u; open OO = i), and so do the splits found here on the images (hooked n
  = q vs plain n = e; plain o = g; closed OO = ll; PHI = pp; HX = rr; 2 = h; dotted signs = nulls). It found two
  differences on rare signs (our d = a against his i, 4x; our a = i against his u, 3x), but it read our values from
  `keys/no18_key.txt`, the solver's pre-split output; the final key at the end of `no18_reading.txt` has d = i and a =
  u, his values, as `lasry_comparison.md` records. So no difference remains there. `keys/no18_key.txt` still holds
  the pre-split values (2 = g, n = a, PHI = l, d = a, a = i); the final key is the one in the reading file.
- His "M.X." = our unresolved "Mx."; "B." = Liga (Sanctissima Liga?), "X." = the League's common enemy
  (unidentified), "S." = Sanctitas?

## Remaining gaps
- six single cipher signs left unread in George Lasry's reading (÷ four times, ✱ twice) - blocker: illegible; isolated signs, his figure lists them as unread
- the code capitals B., X., S., M.X., m. (written unenciphered) - blocker: no-key-material; no key sheet, his B = League and M.X. = Maiestas are conjectures

## Escalation
- [x] siblings: the whole busta opened; no other piece in this key
- [x] clear-pages: none; the clear Latin around the cipher words is context, not a decipherment
- [x] known-keys: all 43 key sheets of fasc. 1 compared by eye; none fits
- [x] print: Meister 1902, Cecchini 1952: no printed text of these articles found
- [x] key-rebuild: key recovered by homsolve2 from the ciphertext alone; look-alike signs split on the image
- [x] retry: re-read sign by sign on the images with the extended key (two passes); doubtful words regraded in the reading file; George Lasry's independent key and reading (17 Oct 2026) compared sign by sign and word by word (`lasry_comparison.md`)
