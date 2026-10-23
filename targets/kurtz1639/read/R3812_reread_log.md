# R3812 re-read log (batch b06, 22 Oct 2026, Claude Opus 5.5)

Kurz von Senftenau to Trauttmansdorff, Hamburg, 3 Feb 1639; 14 DECODE images (IMG_R3812_I23106 ... I23123), 5,526
cipher tokens.

## 1. Is there a text already?

- All 14 images viewed in crops (main checkout img/, git-ignored): no interlinear gloss, margin or slip decipherment on
  any page. I23123 and the left page of I23119 (below the cipher) are clear text in Kurz's hand, not decipherments.
- Print: Mírka 2012 (Západočeské archivy; Crypto-World 11-12/2012) summarises only the 17 Jan letter (R3811); R3812
  was "not yet deciphered". No other edition known. So the reading rests on the figures and the key.

## 2. Key proposal (not entered in key.json; parent session to decide)

- **38 = d** (key.json: g). Every one of the ~75 occurrences in R3812 reads d: und, feindt, landt, wirdt, freundt,
  tausendt, folgendem, ad congressum, ad tracttus, Gedult; and a kwic over the eight other letters gives the same
  (R3811 "freundt", "wurdt"; R3813 "feindt", "und"; R3815 "feindt"; R4625 "feindt"; R4645 "wurdt", "und"; R4736
  "und", "Mecklenburg und Pommern"). 36 stays g. Applied for R3812 only by
  research/reading_audit/b06_r3812_decode.py, which writes read/R3812.txt (decode.py run bare would undo it).

## 3. Transcription corrections (read/R3812_corrections.tsv, 44 rows; tr/IMG_R3812_*.txt edited in place)

- Looped signs: small α where the image has the looped ℒ (#a-loop = m: Regimenter, statim, im Landt); `c` for the
  looped ℓ (#l-loop = tu: eventualiter, fama bella geruntur, futura pericula, constitution).
- Split or misread figures checked on the image: 9 -> 93 (Elben), 40 -> 48 (propendiren), 66 2 -> 66 62 (demolirt,
  demolition), 9 27 -> 92 27 (bis dati), 3? -> 33 (debelliren), 63 31 -> 6 31 (gewesen), 62 74 3 -> 6 27 43
  (Hamburgenses regi), #4-hook -> 4+ (insertion cross).
- Margin insertions moved to their insertion marks (#ins): I23108 l.10 "eigene" (auf die eigene wafen), I23109 l.35
  "tande" (Reichsstande).
- Struck figures (`~x~`) were being decoded by parse.py (it strips the tildes); turned into editorial notes
  `{[struck: ...]}` on I23109, I23113 (two), I23118, I23119.
- A line "{...} 20 26 78 28 31 {und bey der} 39 28 12 31" on I23115 is not on the image (duplicate); removed.
- "bis wan den" on I23108 l.48 is clear script, not figures 6 15 w; "wo" on I23119 l.32 is clear, not 100.
- Clear text corrected where it mattered: nichts (not möchte), werden, darumb, nach, den, Zwischen (not Gewissen),
  beym, Von, item, seindt (was "printd?"), diiudiciren, gewesen, "hundt, Katzen, Pferdt und Leuth gefressen".

## 4. Reading

- Built image by image (read/R3812_reading.md, English read/R3812_en.md). Every unbracketed word is carried by the
  figures (key decode) or by the clear text; b06_align.py R3812: 2,510 words, 0 not carried.
- Clean-sentence share (_check_reading.py logic, body only, header and notes cut): **0.55** (229 sentences, hole rate
  0.144); the whole file: 0.543. Before: the raw decode runs alone score 0.018 (56 windows); the old read/R3812.txt
  scores 1.0 only because its clear text carries it.
- Many of the failing sentences fail on words the period lexicon does not know rather than on holes: Craistag,
  Halberstat, potschafter, tracttus, coniuncton, Latin phrases (Monuisse, extorsisse, suspicacissimos, Gallassiana),
  names (Damer, Penzen, Warnemin[de]). The real holes are about one in twelve words.

## 5. Second pass (22 Oct 2026, after the parent's key change)

- Key now in key.json (parent session, checked by kwic on all nine letters): 38 = d, Δ = nu, #dot = su, #s-long = ti,
  m = a. read/R3812.txt is again written by `decode.py R3812`; b06_r3812_decode.py is superseded.
- Reading moved to the new decode: stehet nunmehr, Craistigs, quuartir, meiner Mainung, disen Crais disunirter halten,
  corpo sufficiente, zu nuz komme, in quibus fit mentio, Ad Salvium nunquam deerit accessus, super teloniae, ultimam et
  e[x]tremam negat[iv]am, general a[m]nistia, reput[at]ion, et nullam spem, ein summa gelt, gefancknus, Propalatim.
  The three aligner flags from the new decode (Craiseschlus, mento, Sal um en quam) fixed.
- Words that were in [?x] although the decode carries them in place were unbracketed (reich, Franckreich, hette,
  ain tusendt, stimirt, zugleich, Auhe, quod isti confidentia ... conferre); the checker counts a [?x] as two holes.
- Images rechecked (I23106 top, I23107 left, I23108 right, I23109 left, I23114 left, I23121 left, I23122 left): six
  more label fixes (corrections.tsv now 50 rows): clear "ist" above the line (January ist lang und breiten genomb),
  {vorhandene} before versamblung, {Thaler} (was halber), {bevorab} (was bewarb?), {So bin} (was Er bin), and on
  I23122 l.18 bold 9 = #sect and 51 not 57 ("mehr wn nothen" = von nöthen).
- Note for the parent on #s-long = ti: in R3812 it gives "tiusendt" (5 times), "Torgati", "Stuckbrotti" where t is
  needed; the reading keeps the t-words (the aligner tolerates the extra i). The sign may be two shapes.
- Clean share, body only: 0.55 -> **0.611** (140 of 229 sentences; hole rate 0.133). Whole file through
  `_check_reading.py --file`: 0.598 (the header comment's later lines and the Notes are counted there).

## 6. Verdict and what stays open

- After the second pass the body scores 0.611, just over the 0.60 bar, and the sentences read; the parent decides
  the state (first pass: 0.55, below the bar). The sentences hold through
  most of the letter (Banér's advance and Halberstadt, the Circle diet, Kurz's view that the Swedes will not treat
  until the war reaches Sweden, the Danish king and Warnemünde, Arnim's postscript on Banér's starving army).
- Open: 78 [...] holes and 37 [?x] words in runs that do not resolve into words after the image checks: run-together
  or doubtful figures (e.g. "zu isa?lissdissionirn", "renattion", "perqulusow", "inmabariia"), blots on I23113,
  I23121 and I23122 (the struck groups, "beren?an"), and rare or ambiguous signs (ψ/9 at line starts, the #s-long
  t/ti question). The figures are mostly legible; what remains is word-finding, not the image.

## Sample

"Ich sage, wie der feindt aniezo stehet, und ehe er widerumb in Pommern gebracht wirdt, so ist Ihnen nit an dem wort
hochgeboren gelegen oder illustrissimi" — "I say: as the enemy now stands, and before he is driven back into
Pomerania, they care nothing for the word 'highborn' or 'illustrissimi'."
- Parent session, 22 Oct: 9v = vo (polyphonic 9) added to key.json; I23121 ll. 15 and 31 relabelled (frisches volck, voluerit).
