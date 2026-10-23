# Re-reading log, letter 4 = BnF fr. 4050 ff. 79-81 (23 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch b33)

## Starting point

Reading audit (22 Oct): *decoded, not read*. Lasry's decode (`lasry_decode_letter4.txt`) leaves groups unjoined, 119
code occurrences without a value (54 of 128 lines) and many "?" values; the middle runs of codes break most sentences.
`_check_reading.py --file lasry_decode_letter4.txt`: 0.511 (line-based, "?" values not counted as holes; not
comparable with a reading body).

## Step 1: is there a text already?

- **Images**: none. BnF fr. 4050 (tome I; item 30, "Lettre, en chiffre, de Hieronimo Ranzo", ff. 79-84) is not on
  Gallica: the BnF Archives et manuscrits notice (ark:/12148/cc504711/cd0e497, found by the free-text search
  "Ranzo") carries no digitisation link, unlike fr. 2988 and fr. 6641 in the same result list. Gallica's SRU is
  closed to scripts (403/Cloudflare). Biermann's transcription gives no link. Blocker for any image check:
  needs-physical-access (or a BnF reproduction order; Biermann or George Lasry may hold photographs).
- **Decipherment of the time / print**: none known (NOTES: no clear copy, no key; Cipherbrain 2016, Tomokiyo 2026 and
  Rosson's page cover letters 1-3 only).
- **Second key**: Paolo Rosson's key (public, github.com/pangoleen/cipher-readings, `centurione-1528/key/table.tsv`,
  fetched to the scratchpad) was built on letters 1-3 and never saw letter 4. It gives 3 of the 90 open code types
  (e173 *express* probable, s72 *sara* probable, d46 *debia* guess) and confirms nine of Lasry's tentative values
  that occur here (d168 *devotione*, d272 *domand*, a305 *attent*, e39 *elega*, i156 *infinit*, s322 *speranz*,
  v189 *un*, f140 *fortuna* (guess), m168 *mezo*). e173 *express* had been reached independently here from the
  sentence before Rosson's key was opened.

## Step 2: the reading

`research/reading_audit/b33_rz_annot.py` writes each line with every group marked by key status. The letter was then
joined into words by hand (`letter4_reading.md`). Rules:
- Lasry's firm values, and his tentative values seen three or more times in the five letters that fit at each
  occurrence here (*soa excellentia* 19x, *con* Q-codes, *et* y-codes, *ambasciadori*, *etiam*, *subito* ...), plain.
- Tentative values seen once or twice: `[?word]`, unless Rosson's independent key gives the same value (then plain:
  *devotion*, *demandare*, *attenta*, *elegga*, *infiniti*, *speranza*, *uno*, *expressa*).
- Codes with no value: `[a203]`, or `[?word]` where the code's place in the list and the sentence point to one word.
  The code is a list of words numbered roughly in alphabetical order within each initial (a51 *ad* < a60 *adriz* < a84
  *advert* < a116 *aiut* < a127 *al*; d10 *da* ... d34-37 *de* ... d156 *detto*), with neighbouring numbers often
  homophones of one word (d34-37 *de*, L106-108 *lo*); the order is loose (d52 *dieci*, s375 *studios*), so position
  only narrows the choice. These values rest on sense and position only and are **flagged for review**:

| code | value | context | position |
|---|---|---|---|
| f158 | Franza | *de le cose in [f158] scripte* | next to f157 Franza |
| m120 | meglior | *più certa e [m120] form* | m119 meglio |
| s370 | suspitione | *per levare ogni [s370] a detti ambasciadori* | s348 summa - s375 studios |
| p288 | potent(ati) | *Venetiani et li altri [p288]ati* | p283 possibil - p291 pre |
| c120 | causa | *non [c179]a [c120] de alcuna* | c109 casa - c125 cert |
| a146 | alteratione | *alcuna [a146] a la mente de soa Maestà* | a143 allegato - a152 altro |
| L90 | legan(ti) | *ambasciadori [L90]nti* (cf. L92 lega + n + ti) | L88 - L92 lega |
| d212 | dissimul(are) | *li convien [d212]are con detti ambasciadori* | d211 dispon - d216 distinct |
| b116 | boni | *tutti li [b116] officii* | b115 bon, b117 bono |
| i00 | in | *che 'l pò [i00] servitio* (i100 *in* with a dropped digit?) | — |
| o98 | offer(ai) | *a la qual [o98]ai da parte mia* | o89 offerta, o99 offre |
| p350 | proved(ere) | *si possia [p350]ere in tutto* | p344 procura - p353 prudentia |
| e100 | evita(re) | *et [e100]re ogni inconveniente* | e96 evento - e106 ex |
| b144 | brusa(ndo) | *[b144]ndo sempre ogni lettera* | b129 Burgo - b147 breve |
| L52 | lect(a) | *subito poi de [L52]a* | L47 le - L56 lege |
| r134 | remove(rli) | *ne [r134]rli da loro intention* | r126 rende - r137 remett |
| i247 | intend(o) | *la qual non [i247]o ne credo* | i246 intende |
| a188 | andamenti | *secondo li [a188] che ho visto* | a187 ancor - a195 ano |
| a205 | anzi | *verso soa excellentia, [a205] [t72]ere* | a204 ante - a208 andar |
| d89 | demonstr(ano) | *da quello che [d89]ano* | d84 deliberatione - d96 denari |
| r20 | ragionevol(mente) | *chi [r20]mente se [d276]iano* | r17 ragion - r19 raguagli |
| L122 | long(a) | *como per [L122]a [e183] conosce* | L109 loco - L128 loro |
| e183 | experientia | same | e171 expedir - e205 extend |
| i251 | inter(tenersi) | *fa [i251]tenersi in ogni tempo* | i249 intes - i254 intention |
| a307 | attend(erà) | *solamente [a307]era a [s388]are* | a305 attent |
| q46 | quelli | *[q46] con li quali* | q44 quelle, q45 quello |
| s357 | succed(erà) | *de quanto [s357]era avisarò* | s347 subito - s364 superflu |
| r42 | re | *a la morte di [r42]* | r41 re |
| p13 | pacifica(re) | *altro mezzo a [p13]re la [x12]ta* | p11 pace - p22 padre |
| t78 | te | *volun[t78]ri* | t74 ti - t89 to |
| v23 | va | *messer Iacomo [v23] trampeato* | v13 vale - v26 van |
| c277 | consegn(ia) | *la effectuatione de la [c277]ia de dette lettere* | c272 contra - c281 conservat |
| e172 | expedir(e) | *quando non si potesse [e172]e il negotio* | e171 expedir |
| d28 | da | *speranza [d28] pote più impedere* | d24 dato - d30 dar |
| d16 | d' | *raguagliatolo [d16] ogni cosa* | d13 da, d15 danno |
| d56 | decembre | *duplicata de venti otto de [d56]* | d52 dieci? - d78 di |
| p357 | prega(tolo) | *[p357]atolo voglia continuare* | p356 prego |
| r145 | remett(endomi) | *[r145]endomi certo* | r137 remett, r138 remission |
| n111 | nota(to) | *le qual harai [n111]to como conviene* | n106 nostra - n115 notific |

Left as codes (no word closes from sense and position): a203, a103, s159, e196, i235, c265, a293, c294, s33, q24, c275,
h44, v124, e161, c304, c179, g49, d271, r91, t14, h51 (3x), t72, p334, s84, p312 (2x), g88, d276, a53, a166, v156,
s388, c233, f155, x12, M9, g123, v233, f184, d208, r69, d195, d53, v68, c150, v178, z81, m66. Groups 1-5 (presumed
nulls) left out.

Words from clear-looking groups were not respelled: *scribere*, *scriberai*, *scriber*, *maliciosamente*,
*effectuacion*, *restauracion*, *intermisione*, *certamenti*, *pote raguagliare*, *volun[?te]ri* stay as the groups give
them. *sentila* (79v:17) is taken as *scintilla* in the English ("a spark"), not changed in the reading.

## Step 4: measures (reading body, `research/reading_audit/b17_score.py`, LANG_=it)

- plain: 0.404 (40/99, hole rate 0.168). The Italian word list is modern: it rejects *te, ti, tu, el, fa*, *scripto*,
  *zifra*, *excellentia*, *adrizate*, *disfidamenti*, *Garbino*, *Poza* ... (V=1 listing), so the explicit-hole figure
  is the one that applies (early Italian, as for early Spanish in the brief).
- HOLES=1: **0.768** (76/99, hole rate 0.083).
- `_check_reading.py --file letter4_reading.md`: 0.431 (whole file, header included).
- Look-alike alternates: not applicable (no image; Biermann's figures taken as given).
- Reader's judgement: the letter holds as sentences from the opening to the signature: the receipt of letters and the
  Burgos journey; Cavalier Bilia's commission; the declarations of war; the Emperor's offer to restore the duke and
  the League envoys' refusal; the warning to keep to the safer side; the arming in Biscay; the Doña Guiomar business
  and messer Iacomo; Garbino; the close, Madrid 10 March 1528. One passage does not hold: 79r:27-79v:2 (*de che
  [?debia] [i235]e bonamente in demandare el [c265]to de [a293], perchè li sara [c294]o [s33] con [q24] [c275]cion a li
  [h44] de l[v124], et che [e161] soa excellentia a [c304]erse*), a run of eleven codes; 80r:1-3 and 80r:13-15 hold
  only in part. State: **read** (grade B), with the sense-only values above for review.

## Still open

- The 47 code types left as codes, and the 39 sense-only values above - blocker: no-key-material (each occurs once in
  the five letters, so no second context can test it).
- An image check of Biermann's figures - blocker: needs-physical-access (fr. 4050 is not digitised).
