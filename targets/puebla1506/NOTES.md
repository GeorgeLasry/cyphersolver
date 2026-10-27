# De Puebla → Almazán, London, 21 April 1506, in Puebla's First Cipher (catalogue 617)

Status: read in part (written up, docs/puebla1506.html). Contributed by WAINUT (https://github.com/WAINUTAI), pull
request #101, 27 Oct 2026; reviewed by Claude for Daniel Bourdeau the same day. No earlier reading was found in the
prints checked (CSP, the 1868 Supplement, Fuensalida, CODOIN 8, Paz y Meliá, Rodríguez Villa, Mattingly 1940). The
passages of ll. 18-29 read as Spanish sentences. The fragments of ll. 11-17 decode but do not yet build sentences.

AGS, Patronato Real, leg. 54, doc. 78. PARES description
[2208120](https://pares.cultura.gob.es/ParesBusquedas20/catalogo/description/2208120), viewer
[show/2208120](https://pares.cultura.gob.es/ParesBusquedas20/catalogo/show/2208120), 4 images: 1 = the letter, 2-3
blank, 4 = address and endorsement. The PARES image carries the watermark "PTR,LEG,54,78", with the pencil note
"PR54-78" and foliation 179. The PARES id is Tomokiyo's. The catalogue had first given 2208061, which is the letter of
15 April 1507 (`targets/puebla1507/`).

- Address (image 4): "Al muy noble señor el señor Miguell Perez dalmaçan secretario y del consejo del Rey nuestro
  señor".
- Endorsement (image 4, rotated, low resolution): "del doctor de la puebla ... xxj ... abril 1506".
- Date line (image 1, clear): "de Londres a xxj de abril de ...". Signed by Puebla.

## Context

Philip and Juana, King and Queen of Castile, were driven ashore in England in January 1506 on their way to Castile.
They stayed until late April and sailed from Falmouth a few days after this letter. The clear opening of this letter says Puebla wrote
at length "por via de Martin Sanches de Çamudio" to the King and to Almazán, and that the King and Queen "se estan en
Falamua [?]" waiting for the weather. A later clear line may say that someone "mañana se embarcara" [?]. These clear
readings are uncertain and are not part of the reading files.

The day after this letter, Katharine, Princess of Wales, wrote to Ferdinand (CSP Spain I no. 459, Richmond,
22 April 1506). She said her people were "ready to ask alms, and herself all but naked". In cipher, Puebla tells
Almazán the opposite: he sees the princess's people "so finely dressed that I did not think to see more".

## System and key

Puebla's First Cipher is a letter substitution with a few homophones. It is Bergenroth's key no. 6, as reconstructed
by S. Tomokiyo (cryptiana, "Spanish ciphers", table `Puebla1.jpg`). One Roman-numeral code group from Puebla's Great
Roman Numeral code occurs three times: DCCCLXXXVIII = "el Rey de Inglaterra", key AGS PTR leg. 52 doc. 33, image 51
(read in the check of `targets/puebla1496`). Its C-count in this letter was not checked against the ligature rule,
so the value is marked [?] at every occurrence. The value fits the context, but it is an
assumption until the group is checked on this letter. The aliases and values are in `key_first_cipher.tsv`. Sign
`o` serves for both u and v, as is usual in the period. The sign in "ra?on" (l. 13) is not in Tomokiyo's table, and
neither is a z sign; "plazer" (l. 12) has a Z with a hook [?].

## Transcription, decryption, reading

- `transcription.txt`: the cipher passages of image 1, ll. 11-29, in ASCII aliases, with the clear words that frame
  them. Clear text that was not read is marked [[...]].
- `decode.py` (standard library) writes `decryption.txt`, line by line under the transcription, and runs the
  controls.
- `reading.txt` / `translation.txt`: ll. 18-29, read in part.
- `reading_ll11-17.txt` / `translation_ll11-17.txt`: ll. 11-17, decoded, not read.

The passages that read:

> [...] por aquella gente hazia, por su propio interese, que la princesa me escriviese estas cartas que aqui van
> inclusas. [...] Los de la señora princesa veo tan bien ataviados que mas no pense ver. Por la codicia de algunas
> personas [?] [?] es tal que con [?el] tesoro de {el Rey de Inglaterra?}, dudo que se [?contentasen] [...] va a beneficio
> de natura con este [...]

> [...] those people brought it about, for their own interest, that the princess wrote me these letters, which go
> enclosed here. [...] I see the lady princess's people so finely dressed that I did not think to see more. [?For] the
> greed of certain persons [?] [?] is such that, even with [?the] treasure of {the King of England?}, I doubt they
> would be [?content] [...] is going along at the mercy of chance (a beneficio de natura) with this [...]

"A beneficio de natura" is a set phrase of the period, "left to nature / to chance": Cisneros's secretaries, 1516,
"no se ha de dexar a beneficio de natura" (Cartas de los secretarios, 1875); CODOIN has "ni esto quede a beneficio de
natura". The first translation, "goes to the benefit of nature", was corrected in the review of 27 Oct 2026.

The fragments of ll. 11-17 have secure words: "y de la partida", "de todo el [?aresto]", "con mucha [?razon]",
"señora princesa", "conviene", "bien y acrecentamiento", "de {el Rey de Inglaterra?} y del principe", "abra quien
le [?pedir] que ningun malcontentamiento". The clear words between them are not read, so they do not build sentences.

**Controls** (`python decode.py`).

- Shared language model (`lang/`, `es-golden-age`: Spanish 1490-1650, order 5, no spaces, 'early' norm), mean
  log-prob per letter of the decoded runs of ll. 14-29: key -1.692; 1,000 shuffled keys best -4.734 (median -6.117);
  the key on 1,000 sign-shuffled texts best -4.258 (median -4.773). Added in the maintainer review, 27 Oct 2026.
- `lm.best_language` on the word-divided reading (reading.txt, holes removed): es-modern -1.617, ca-modern -1.946,
  pt-modern -2.093, la -2.424.
- Word list (WAINUT's original control): a small generic Spanish word list without the rare content words
  (interese, inclusas, ataviados, codicia) covers 0.608 of the decoded letters; 1,000 shuffled keys cover at most
  0.292 (median 0.066); the key on 1,000 sign-shuffled texts at most 0.262 (median 0.166). Shifting the plaintext
  alphabet by 1-3 letters gave gibberish ("qpstxqspqlploufsftfrxfmbqslodf" for l. 18).

**Corrections from the check of 27 Oct 2026.** A second agent re-read ll. 14-20, 24-26 and 29 on fresh 3x crops, in
its own alias set. Every reading listed above was reproduced letter by letter. It corrected three places:

1. l. 16: the sign after "abra" is the crossed L with o (qu), so it reads "abra **quien** le [?pedir] que ningun
   malcontentamiento", not "abra bien". The letters decode as "pedri"; "pedir" is a guess and stays marked.
2. l. 19: "inclusas" has a single C, not a doubled one.
3. l. 29: the passage begins "va a beneficio ...". The first pass had left out "va a".

Lines 11-13 were not re-read in the check. Only "con much[a]" on l. 13 was confirmed.

## Prior art

- CSP Spain I (Bergenroth 1862), April 1506, pp. 385-386, fetched again from BHO on 27 Oct 2026. It holds nos.
  458-460: Prince Henry to Philip (9 April), the princess to Ferdinand (22 April), and the commercial treaty
  (30 April). There is no letter from Puebla.
  [BHO](https://www.british-history.ac.uk/cal-state-papers/spain/vol1/pp385-386).
- Bergenroth's 1868 Supplement, 1506 section: Juana, the Villafáfila treaties and the Toro Cortes. None of the
  distinctive phrases occurs, and there is no Puebla letter of April 1506.
- G. Gómez de Fuensalida, *Correspondencia* (1907): we searched the OCR text for malconten-, ataviad-, inclusas,
  "codicia de alg", "beneficio de natura", "propio interese" and "xxj de abril". None of them matched this letter.
- Tomokiyo lists the letter among those in Puebla's First Cipher, without a reading. There is no interlinear
  decipherment on the scan.
- Print search of 27 Oct 2026 (maintainer review), OCR texts from the Internet Archive grepped for ataviad-/atauiad-,
  inclusas, "codicia de alg", "beneficio de natura", "propio interes", malcontentamiento, "xxj de abril", "abril de
  1506" and every Puebla mention:
  - CODOIN vol. 8 (1846, `coleccindedocu08madruoft`): prints Philip I's letters from England, Jan-Apr 1506
    (Windsor, Richmond, Falmouth); no Puebla letter, no match.
  - A. Paz y Meliá, *Series de los más importantes documentos del archivo y biblioteca del Duque de Medinaceli*,
    vols. 1-2 (1915-22, `seriesdelosmsi01pazy`, `seriesdelosmsi02pazy`): no Puebla letter, no match.
  - A. Rodríguez Villa, *La reina doña Juana la Loca* (1892, `lareinadoajuan00rodr`): prints Puebla's letters of
    15 Apr, 1 Sept and 7 Sept 1507 (Simancas), nothing of 1506.
  - *Crónica del rey Enrico Otavo* (1874, `crnicadelreyenri00madr`), appendix of Simancas documents: no match.
  - G. Mattingly, "The reputation of Doctor De Puebla", EHR 55 (1940) pp. 27-46
    (`sim_english-historical-review_1940-01_55_217`): no use of an April 1506 letter.
  - Internet Archive full-text search (all holdings, incl. every CODOIN volume) for "estas cartas que aqui van
    inclusas", "propio interese que la princesa", "bien atauiados", "bien ataviados que", "codicia de algunas personas",
    "beneficio de natura", "Martin Sanches de Çamudio", "21 de abril de 1506": no hit for this letter. ("A beneficio
    de natura" is a common phrase: Cisneros's secretaries 1516, CODOIN, Carajicomedia.)
  - Not reached: HathiTrust full-text search (Cloudflare challenge, not bypassed), Google Books and BNE Hispánica
    (no scripted full-text access); Mattingly's *Catherine of Aragon* (1941) has no open full text.
  Novelty is claimed against these prints only.
- Tomokiyo's page source: next to his entry "Puebla to Almazan, 21 April 1506 (PARES 2208120)" he left an HTML
  comment `<!--y dela parti da ....-->`, the first words of l. 11. He had begun to decipher the letter; nothing is
  published. Recorded as a contamination note: the opening words were in a public page's source before this work.

## Proposed catalogue change

617: read in part (WAINUT, 27 Oct 2026): the cipher passages of ll. 18-29 read with Tomokiyo's First Cipher table.
The shelfmark is AGS PTR leg. 54 doc. 78 (PARES 2208120). Keep it open for the clear text and ll. 11-17.

## Remaining gaps

- The clear text of the letter (about 20 lines in Puebla's cursive), read only in part - blocker: illegible; at 1017 x 1413 px, the largest size PARES serves, many words cannot be read with confidence. A better scan from the AGS would allow it.
- ll. 11-17: the fragments do not build sentences, because the clear words between them are not read and l. 12 ("[?desto] [?stares] ... [?aresto]") divides uncertainly - blocker: illegible; descenders from the line above run through ll. 11-13
- l. 13, the sign in "ra?on", and l. 25, two signs after "personas" - blocker: illegible
- l. 16, "pedri" (decoded) for "pedir" [?] - blocker: illegible; the letters are clear but the form is doubtful
- DCCCLXXXVIII: the C-count was not checked on this letter (three occurrences) - blocker: open-codes

## Escalation

- [x] siblings: puebla1507 (Puebla to Ferdinand, 15 April 1507, same First Cipher, printed in the 1868 Supplement); Katharine to Ferdinand, 22 April 1506 (CSP I no. 459)
- [x] clear-pages: image 4 (address, endorsement) read; the clear text of image 1 read where legible
- [x] known-keys: Tomokiyo's First Cipher table; the Great Roman Numeral key (PTR 52 doc. 33, image 51) for the one code group
- [x] print: CSP Spain I April 1506 (BHO, fetched again), the 1868 Supplement 1506 section, Fuensalida 1907 (OCR search), Tomokiyo; in the review of 27 Oct 2026 also CODOIN 8, Paz y Meliá Series 1-2, Rodríguez Villa 1892, Crónica del rey Enrico Otavo 1874, Mattingly EHR 1940 and an Internet Archive full-text phrase search: nothing (see Prior art)
- [n/a] key-rebuild: Tomokiyo's table gives a value to every sign that occurs except one sign, seen once (l. 13); the review checked the key file sign by sign against Tomokiyo's table image (all agree; the table has no z, so the l. 13 sign is presumably z). Nothing is left for annealing or bracketing to fill: the open places are unread signs and clear text, not unknown key values
- [x] retry: ll. 14-20, 24-26 and 29 re-read on fresh crops in a second pass; three corrections (l. 16, l. 19, l. 29)

No images are in the folder. The pages are on PARES (links above).

## Pending

- Cipher snip for the write-up (PARES answered HTTP 429 on 27 Oct 2026): fetch images 1-4 with `python -I -u pscripts/pares_fetch.py 2208120 dl_puebla/p1506 1 4`, find the box of ll. 18-26 (and ll. 24-26 for the lead) on `2208120_001.jpg`, crop with `python -I pscripts/snip1506.py <x0> <y0> <x1> <y1> <lead_y0> <lead_y1>` (review-session scripts, not in the repo: any PARES fetch of description 2208120 and a crop to about 1,100 px wide JPEG under 400 KB, saved as docs/puebla1506_ll18-26.jpg and docs/puebla1506_lead.jpg, does the same), check the watermark reads PTR,LEG,54,78, then put this figure in section 01 of docs/puebla1506.html, set IMAGES['puebla1506'] to the lead crop and drop the "snip" skip in docs/_explore_skip.json: `<figure data-credit="Archivo General de Simancas, Patronato Real leg. 54 doc. 78, f. 179r (PARES image 1), via PARES"><img src="puebla1506_ll18-26.jpg" alt="Lines 18 to 26 of the letter: Puebla's cursive with runs of cipher signs, crosses, q-shapes and the figure 46, set between clear words" loading="lazy"> <figcaption>Lines 18&ndash;26. After the clear <em>por aquella gente hazia</em> the cipher runs <em>por su propio interese que la princesa me escriviese estas cartas que aqui van inclusas</em>; lower down, <em>los de la se&ntilde;ora princesa veo tan bien ataviados que mas no pense ver</em>.</figcaption></figure>`

## Parallel reading by Brice Dudout (27 Oct 2026)

Made the same day with the same table, independently; own transcription, three values added, and a comparison with the reading above: see `dudout/README.md`.
