# Siena, Concistoro 2308: "Lettere in cifra" — the unread pieces (catalogue 336)

Status: attempted, open for this project — the unread pieces of the bundle (no. 1 of 1421 not photographed, needs ASSi; nos. 7, 19, 21 unread by anyone). 18 Oct 2026: George Lasry's outside solutions of R4794 (his "no. 5"), nos. 9, 11, 12, 13, 15 (part) and 17 recorded below; 20 Oct 2026: checked on our own transcriptions (no. 17 92.9%, no. 11 94.4%, R4794 93.1%), and no. 8 confirmed as deciphered at the time.

**Split on 14 Oct 2026 under the one-key rule (George Lasry, 14 Oct 2026).** This folder held the whole bundle, in
which each letter has its own key. The letters whose keys were recovered are now their own entries, each a different
cipher with its own page:

- no. 25 (R4813), key recovered ciphertext-only, 96.2%: [`targets/siena25/`](../siena25/NOTES.md)
- no. 18 (R4806), key recovered ciphertext-only, 87.1%: [`targets/siena18/`](../siena18/NOTES.md)
- no. 14 (R4802), key recovered ciphertext-only, 58.6%: [`targets/siena14/`](../siena14/NOTES.md)
- no. 4 (R4793), Borghesi 1456, key from its own fragment, 79%: [`targets/borghesi1456/`](../borghesi1456/NOTES.md)
- nos. 6 and 24 (R4795, R4812): deciphered by George Lasry with fasc. 1 key R4755, [`targets/siena1431/`](../siena1431/NOTES.md)
- nos. 20 and 23 (R4808, R4811), one system: read in part by George Lasry, key from the ciphertext, 17 Oct 2026, [`targets/siena2023/`](../siena2023/NOTES.md); removed from this entry 18 Oct 2026, and this folder's transcriptions of them (`transcripts/no20*`, `no23*`) moved to `targets/siena2023/project_attempt/`

Their transcriptions, keys, readings and validation moved with them. This entry keeps the access notes, the inventory,
the key index of fasc. 1, the shared solvers (`homsolve*.py`, `wordsolve.py`, `sylsolve.py`, `prep.py`, the
transcribed 1450s keys in `keys/`) and the **unread pieces**, which are listed together only because they are in the
same bundle: **no shared key is claimed for them**. The pieces deciphered at the time (nos. 8, 10, 13/16, 22) and no. 12 (DECODE R1858
"Decrypted") are described below for completeness; they are other keys, not results of this project, and are not
counted. The transcriptions of nos. 6 and 24 (`transcripts/no06*`, `no24*`) stay here as the input George Lasry's
reading was checked against.

Session of 24 September 2026. Goal set by Daniel: decipher the 29 cipher letters of ASSi Concistoro 2308, fasc. 2
("Lettere in cifra"), oldest dated 1421 per Meister 1902 pp. 50-51, "solo parzialmente decifrate" per the 1952
inventory; first try the filed keys (fasc. 1) on every letter.

## 18 Oct 2026: George Lasry's solutions of the rest of fasc. 2

- **Solution: George Lasry**, done with CTTS (transcription in full, or correcting an LLM's transcription, and
  sometimes its built-in cryptanalysis) and with LLMs (Claude Opus 5.5 and GPT-6 Astra); sent to Daniel Bourdeau on
  18 Oct 2026 as a Cryptiana-style page, "The cipher documents of Concistoro 2308, fasc. 2 (Archivio di Stato di
  Siena)" (index.html with key tables of signs cut from the photographs, crops and excerpts; kept outside the
  repository, `Downloads/Concistoro2308_fasc2_cryptiana.zip`). The footer reads "Satoshi Tomokiyo, 17 October 2026"
  (the Cryptiana byline); the sender and author of the solutions is George Lasry. Solved in October 2026,
  ciphertext-only except nos. 9 and 13 (interlinear and separate plaintext); after this project's attempt of 24 Sept.
- His numbering is the pencil numbering except **his "no. 5" = our unnumbered slip R4794** (our no. 5 is the clear
  letter R4791).

| no. | DECODE | his reading | his status |
|---|---|---|---|
| "5" | R4794 | "Di alcuni pezzi [d']i artigliaria 44 di 26. Le Signorie Vostre, come so, faranno si governin con prudentia, perché ancho 67 ha qualche impressio[n] ... col presente 74 di 26." Pigpen-like key, a dot shifts a sign to another block; 165 symbols | ciphertext-only; codes 26, 44, 67, 74 open |
| 9 | R4798 | "[la pratica?] [di?] Chastiglone questa vernata con lo sentimento di [re d'Aragona] e nutrire questa guerra uno altro anno"; dated 1440s-50s (Alfonso V in Tuscany), against our "c. 1495-1516?"; 53 symbols | with the interlinear decryption |
| 11 | R4800 | Acciaiuoli to Lorenzo, Rome 13 June 1478: Forlì and Faenza to send two squadrons each; Giovan Francesco Gonzaga offers 80 men-at-arms for 7,000 ducats + 1,000 for himself; 393 symbols, 57 signs | c. 90%, ciphertext-only |
| 12 | R4790 | Naples, 10 March 1413, to Sforza Attendolo: King Ladislaus offers him a bride of his house; 865 symbols, 46 signs | over 95%, ciphertext-only |
| 13 | R4801 | with its plaintext twin no. 16 (R4804): the Pope's agreements, his delayed coming to Bologna, Lautrec took Modena and Reggio (1527-30); 553 symbols | with the separate plaintext |
| 15 | R4803 | Mario Bandini, Innsbruck ("Eltspruch"), 4 Jan 1547: Granvelle's warning ("essent principes qui vellent persolvere centum milia coronatorum ..."); 240 symbols | partial, 75 of 240 signs |
| 17 | R4805 | Bartolomeo Tantucci to Antonio del Vescovo, 25 (or 20) Aug 1528, "questa cifara è quella di Balìa": bishoprics for someone's nephews, the Cardinal of Naples and Pitigliano; 282 symbols, 41 signs | c. 85%, ciphertext-only |
| 18 | R4806 | see `targets/siena18/` (Pisa, Oct-Nov 1496) | in full |
| 20, 23 | R4808, R4811 | see `targets/siena2023/` (1413) | in full |

He lists nos. 7, 8, 19, 21 as "unsolved as of 17 October 2026"; on no. 8 he finds a relation to the clear memorandum
above the cipher "possible but speculative". Settled below: it is the decipherment.

Under the one-key rule each of his keys is a separate cipher (as siena1431 and siena2023 are); they are recorded here
because they are the pieces this entry held. Whether they become George Lasry's own entries is left to him and Daniel
(see Assumptions).

## 20 Oct 2026: no. 8 (R4797) was deciphered at the time

Image downloaded with the DECODE cookie (`IMG_R4797_I27940_P.jpg`, git-ignored). The sheet: a clear memorandum in
short paragraphs, each led by an **underlined** phrase ("E disse di tutto mi dava in credenza ...", "di papa Felice",
"di buona voglia", "Nel principio ...", "Anchora disse", "antiveduto questo"), then, pasted below, a six-line slip
(pencil 8) of mixed text: clear words with cipher runs. The slip is the tail of the letter, not the whole of it:
line 1 is clear ("Dapoi ... dapprima ... trovato ..."), and its clear words are the memorandum's underlined heads.
Aligned sign by sign at 2x on the full-size photograph:

- slip l. 3-4, after clear **"Anchora d(iss)e"**: `÷ 59t95 75□ø I2 7øϕϕ2 9ff2ϕ +c5` = memorandum "[el duca di
  Milano] aveva dato la donna biancha" (÷ = the Duke of Milan as a code sign; *aveva* = 5 9 t 9 5, pattern ABCBA;
  *dato* d=7 a=5 t=□ o=ø; *donna* 7 ø ϕ ϕ 2 with the same d and o and a doubled n) ... `7t I2ɷ+ctɱt` = "del
  marchese";
- slip l. 2: `÷ tɷ I2ɷ+ctɱt 7ff o-tɷɷ2ɷ2 5 o-2|ot` = "[duca di Milano] el marchese di ferrara a fa|re" (memorandum
  paragraph "Nel principio ...": "legha fral duca di Milano el marchese di Ferrara a fare guerra a Viniziani"):
  *marchese* has the same seven signs as in l. 4; *ferrara* f=o- e=t r=ɷ a=2;
- slip l. 5-6, after clear **"anti(ve)duto questo"**: `t ϕøϕ ff9ø I2ϕ+c2 ot +ct ffoɷbɱo ...` = "e non può manchare
  che presto ..." (memorandum "antiveduto questo e no può manchare che presto vedrete grandissimi fatti"); the slip
  ends in clear "in buono stato".

The values used in the three passages agree with each other (a = 5 or 2, c = +, h = c, d = 7, e = t, f = o-, n = ϕ,
o = ø, r = ɷ, s = ɱ, t = □, v/b = 9). So the memorandum is the contemporary decipherment of the letter the slip ends,
written as heads (the clear words) plus deciphered text: **no. 8 was read at the time**, as the 24 Sept notes said,
now shown rather than assumed. George Lasry's "unsolved" for no. 8 is answered; the memorandum's earlier paragraphs
(di papa Felice, Niccolò Piccinino, di buona voglia) belong to the part of the letter that is not on the slip. One
doubt: "la" and "manchare" both begin with the sign read I; either two look-alike signs or a slip of the encipherer.
Not counted as a project result (a decipherment of the time); the DECODE queue entry says so.

## 20 Oct 2026: George Lasry's keys checked on this project's transcriptions

`verify_lasry.py` (run `python targets/siena1421/verify_lasry.py`, or with `no17`, `no11`, `r4794`, `r4794b`,
`no20`): his key tables are images of signs cut from the photographs, so each of his signs was matched by shape and
occurrence count to the sign names of our own 24 Sept transcriptions (made before his work and independently of
it). Our tokens are then deciphered with his key, without fitting, and aligned (edit distance) with the plaintext of
his decryption; a token agrees when his key gives it the letter it aligns with. The identifications are commented in
the script; those set after a first alignment are marked, with the score before them.

| piece | our transcription | tokens | agree | what the rest is |
|---|---|---|---|---|
| no. 17 | `transcripts/no17.txt` (agent A) | 283 | **92.9%** (89.0% before three sign identifications were corrected by count) | his own uncertain words ("el Mustetto", "Otto", "lco[..]stren"), and our merged 6 (his O "6<" and V "6") |
| no. 11 | `transcripts/no11.txt` (agent B) | 378 sign units | **94.4%** (66.7% with eight signs unidentified) | his '+o' (e) and 'o+' (d) are single signs our agent wrote as two tokens; his nulls 'g#', '31', '87', mⁿ, /// are our G HASH, 3 1, 8^dot 7, M^n, SL3; our two cipher blocks are his two runs line for line |
| R4794 ("5") | `transcripts/r4794.txt` | 160 | 83.8%; **93.1%** with r and h added | his table has **no H and no R column** though his reading has h 7 and r 11 times: our A (alpha) is r every time, our N (∩) is h: a gap in his table, not in his reading |
| no. 20 (siena2023) | `siena2023/project_attempt/no20.tok` (agent C) | 1,128 | **71.1%** one letter per sign of ours, 78.6% allowing two; **control 14.8% / 23.0%** | our names merge signs he splits (o vs his o- and o-o; y; S); here the mapping is fitted by EM from his key values for the sign names both transcriptions share, hence the control with a wrong plaintext (his no. 23) |

So his readings of nos. 11, 17 and R4794 come out of our own transcriptions with his keys at 93-94%, and our no. 20
transcription carries his no. 20 reading far above the control: **independent verification** of those four. Not
checked here: no. 12 and no. 13 (no transcription of ours), no. 9 (46 tokens) and no. 15 (his partial reading), no. 23
(the same key as no. 20). No. 18: see `targets/siena18/NOTES.md` (his one printed sentence equals our reading word for
word; his key compared with ours).

## Access: the whole filza is on DECODE (found this session)

The 23 Sept scan (`research/oldest/scan_2026-09-23/italy.md`) had only the Yale Ilardi reel 1503 (13 key frames). DECODE
holds the whole busta, photographed in the ASSi reading room (owner 32, created 2020-11-24 and 2023):

- **R4746-R4789 = fasc. 1 "Cifrari"** (cover "Concistoro 2308, Fasc. 1, Pezzi 46", divider sheets "Secolo XV" /
  "Secolo XVI"), DECODE names `Concistoro_2308_01` ... `_43`, record type key (R4787 = type 3, 10 pp.). R4761 is
  not Siena (a Kurtz 1639 record in the id gap); R4783 has no image.
- **R4790-R4814 = fasc. 2 "Lettere in cifra"** (cover "Concistoro 2308, Fasc. 2, Pezzi 25" on R4790 p. 3),
  DECODE names `Concistoro_2308_44` ... `_68`, all dated "1500-1599" (a placeholder), status N/A, no transcription
  or decryption attached.
- **R1858 "Siena keys and ciphers"** (8 pp., status "Decrypted" but no document attached): photos of key sheets
  (the 1454 Milan key, "Cifra cum frate Bernardino", the 1475 key, R4747's slips) and a second photo of no. 12.

Images downloaded with the DECODE cookie to `decode/img/` (git-ignored; ASSi images, not public domain).
Metadata in `decode/views.jsonl`. 1600-px previews in `img_small/` (git-ignored).

## Inventory of fasc. 2 (pencil numbers = Meister's numbering)

Meister's dated anchors hold: no. 4 = 1456, no. 11 = 1478, no. 17 = 1528. So the pencil numbers on the pieces are
the numbering Meister saw in 1902.

| no. | DECODE | what it is |
|---|---|---|
| 1 | - | **not in the fascicle as photographed** (Meister: dated 1421) |
| 2 | - | not photographed |
| 3 | R4792 | clear private letter, "Charissimo compare mio ... Simone nostro", Siena 1 April (no year); no cipher seen |
| 4 | R4793 | Galgano Borghesi, J.U. doctor and orator, Naples 12 May 1456 (Senatore 2009: "Concistoro 2308, c. 4, da Napoli, 12 maggio"), to Leonardo Benvoglienti; cipher runs in capital letters, a few interlinear glosses |
| 5 | R4791 | clear private letter to "Maffeo da Siena", pencil "1460?"; no cipher seen |
| 6 | R4795 | letter to the Magnifici domini, clear salutation then ~20 lines all cipher (Latin-letter-like signs, no word division) |
| 7 | R4796 | long despatch (2 pp.), cipher block of ~10 lines near the end |
| 8 | R4797 | cipher slip (5 lines, a few glosses) + a clear decipherment on the same sheet (Papa Felice, Duca di Milano, Leonello d'Este: c. 1440-47) |
| 9 | R4798 | slip, two short cipher runs in clear text |
| 10 | R4799 | slip, one cipher run glossed "presura di Montepulciano" |
| 11 | R4800 | Donato Acciaiuoli to Lorenzo de' Medici, Rome 13 June 1478 (a Florentine letter held in Siena); two cipher blocks |
| 12 | R4790 (+R1858 p. 7) | whole letter in graphic signs with word separators, ~22 lines + 2-line subscription |
| 13 | R4801 | slip in digits and signs with clear phrases; **its decipherment is no. 16** |
| 14 | R4802 | whole page in cipher, word-separated, to the Priors and Capitano del Popolo of Siena; dorsal list of names |
| 15 | R4803 | 8 pp., Sienese orator at the imperial court, 29 Dec 1546 / Jan 1547 (Schmalkaldic war); short capital-letter cipher runs |
| 16 | R4804 | clear decipherment of no. 13 |
| 17 | R4805 | 20 Aug 1528, to Bartolomeo Tantucci?, docketed "questa cifra è quella di Balìa"; cipher runs of digits/signs |
| 18 | R4806 | Latin treaty articles (petitions of Siena, a king's secretary Niccolò), cipher words throughout (4 pp.) |
| 19 | R4807 | letter to the Magnifici domini, cipher runs |
| 20 | R4808 | "Sacra Regia Maiestas, Serenissime princeps", whole letter in cipher; now siena2023 |
| 21 | R4809 | short letter with cipher runs |
| 22-23 | R4810 | clear drafts with numbers as code words (mentions Calixtus III: 1455-58) |
| 23 | R4811 | whole page in cipher; now siena2023 |
| 24 | R4812 | whole letter in cipher (2 pp.) |
| 25 | R4813 | slip, all cipher |
| 29 | R4814 | fragment, a few words |
| ? | R4794 | slip, 6 lines all cipher, no number found (erased pencil "4"/"5"); George Lasry's page numbers it no. 5 |

Nos. 1, 2, 26, 27, 28 are not among the 25 pieces photographed. The fascicle cover says 25 pieces; Meister counted 29.

## Key index (fasc. 1), as read from the images this session

| DECODE | heading / identification | date |
|---|---|---|
| R4746 | alphabet + Duca di Milano, Serenissimus, Niccolò Fortebraccio; "Dns Antonius ... 1433" (Meister's "Siena Beispiele 1") | 1433 |
| R4747 | three small slips (pencil 2, 3, 4/5): a 20-cell number table of words; **slip 3 = signs for whole phrases about "Tartaglia"** (the condottiere Angelo Tartaglia, executed Feb 1421), so c. 1419-21, contemporary with the lost no. 1; slip 4 "Cu Leonardo" (Senesi, Fiorentini, S. Rinaldo, Paola, Gente d'arme, Genovesi, Re d'Aragona, Papa, Denari) | c. 1420 |
| R4748 | "Cifra cum fratre Bernardino": Papa, Duca di Milano, Niccolò Piccinino, Fiorentini, Conte Francesco, Re d'Aragona, Veneziani, Bolognesi, Sanesi, Conte d'Urbino, Antipapa Felice | 1439-44 |
| R4749 | "Cifra con ... Antonio et con Francesco ...": Aluise dal Verme, Sacramoro, Niccolò and Francesco Piccinino, Obizo, Papa Felice | c. 1440-44 |
| R4750 | "a messer Leonardo e messer Antonio, ambasciatori a Milano, 1454"; Latin-word nomenclator (Rex Aragonum gallus, ambasciatore fiorentino storpsi ...) | 1454 |
| R4751 | "Cifra mandata a Lodovico di Salimbene potestà di Casole" (Senenses Stella, Casole Felix ...) | 1450s |
| R4752 | "Cifra de m. Antonio Bichi 1478 Rom." | 1478 |
| R4753 | Latin nomenclator, vowels in capital-letter groups (Imperator 62, Papa 84 ... Imperatrix 20, Rex Portugalie 66) | c. 1452 |
| R4754 | "Cifra data a ... Antonio Petrucci" (Latin code words: florenus, Culmen, Ventus ...) | 1450s |
| R4755 | "Cifra cum Christofano ..." (Papa, Fiorentini, Veneziani, Duca di Milano, Niccolò Piccinino, Conte Francesco, Lucca, Pisa, Pistoia, Siena ...) | c. 1440 |
| R4756 | "Lucensibus": Papa, Cardinales, Rex Aragonum, Dux Calabrie, Dux Mediolani, Florentini, Marchio Ferrarie, Senenses, Lucenses, Comes Jacobus Piccininus, Dominus Sigismundus | 1450s |
| R4757 | "Data domino ... Venetiis" | 15th c. |
| R4758 | "Cu d(omi)no Antonio de Petrucciis" (Senesi = papa, Fiorentini = dux, S. di Piombino = Rex, Balduccio = mons) | 15th c. |
| R4759 | "cu ipso magistro ..." Papa, Duca Valentino, Re de' Romani, Re di Francia, Pandolfo | c. 1500-03 |
| R4760 | "Cifra con m. ..." 1536 | 1536 |
| R4762 | "Data a Luca di Niccolò mandato a Napoli ambasciadore" (Conte Everso, Conte Jacomo, Pitigliano, Patriarcha, Orsino ...) | c. 1455-58 |
| R4763 | long nomenclator (Lombardia 12 ... ; Alessandro Sforza, Corrado da Fogliano ...) | 1450s-60s |
| R4764 | "Cifra con m. Bernardino Buoninsegni oratore a S. M.tà" | 16th c. |
| R4765 | Spagna, Imperador, Re di Francia, Re d'Inghilterra ... | 16th c. |
| R4767 | "Cifra con m. Aglo Venturi" (nulls = the numbers 1-40) | 16th c. |
| R4768 | "Cifra di m. Mercanto ... oratore" | 16th c. |
| R4770 | Papa, Re di Francia, Re di Napoli, Maximiliano, Roano, Ligni, Valentinois, Ascanio, Montepulciano, Ponte a Valiano | c. 1499-1500 |
| R4771, R4781 | "Fano": Papa A ... Duca di Ferrara I, Giovanni Bentivoglio, Franciosi, Mons. di Trans, Roccabertino | c. 1500 |
| R4772 | "D. Mattheus Marinus doctor ... Io. de Gonzaga" | c. 1500 |
| R4773 | "Cifra con Girolamo Tosta" (all-numeric; Duca di Castro, Balìa) | 1540s |
| R4775 | Letter-key "die 4 augusti 1502" | 1502 |
| R4776 | syllabic table, "cifra con ... Donna ..." | 16th c. |
| R4778 | numeric nomenclator (Papa 33 ... Senesi 53, Re Federico 58) | c. 1500 |
| R4779 | "Cifra Giusti" (Papa 2 ... Siena 29) | c. 1500 |
| R4780 | "Capitano ... Pandolfo" (Bolognesi Sinagoga, Fiorentini Hebreus) | c. 1500 |
| R4782 | Papa, Re di Francia ... Bologna, Pisa, Giovanni Bentivoglio, Mons. di Legni, Leonardo Bellanti, Card. di Siena, Trocces, Card. di Capua | c. 1500-03 |
| R4785, R4786 | 16th-c. code books (Latin cover words), "Cifra con la Cesarea M.tà, Rep. Senese" | 16th c. |
| R4787 | titles book 1496 (not a key) | 1496 |
| R4788 | genealogy + numeric columns | ? |
| R4789 | alphabet + nulls + duplicates | ? |

## Letters: what was established

- **No. 8 (R4797), c. 1440.** Ciphered slip pasted at the foot of a sheet whose upper part is the contemporary
  decipherment ("Anchora disse el duca di Milano aveva dato la donna Biancha a misser Leonello figlolo del
  Marchese ... antiveduto questo ..."; antipope Felix, Niccolò Piccinino, the Marquis of Ferrara). Read at the
  time (aligned sign by sign on 20 Oct 2026, section above). The nomenclator persons match the c. 1440 keys (R4748, R4749, R4755).
- **No. 10 (R4799).** One cipher run glossed letter by letter "presura di Montepulciano". Read at the time.
- **No. 13 (R4801) + no. 16 (R4804).** No. 16 is the clear decipherment of no. 13 (1527-29: Lautrec, the pope's
  coming to Bologna, "si pigliò Modena e Reggio"). Partial alignment: homophonic substitution with numbers as
  extra homophones (bologna = ∇ E 3 E 17 φ ₀⁰; accordi con = ₀ ⁿθ(cc) E ‡ + 15 ƥ E φ; a sign with superscript n
  = doubled letter). Read at the time.
- **No. 12 (R4790).** Photographed again in R1858, which DECODE marks "Decrypted": taken as read (Daniel's
  instruction, 24 Sept: trust DECODE's Decrypted status).
- **No. 4 (R4793).** Galgano Borghesi, Naples 12 May 1456: key rebuilt from its own fragment; now its own entry, [`targets/borghesi1456/`](../borghesi1456/NOTES.md).
- **No. 11 (R4800).** Donato Acciaiuoli to Lorenzo de' Medici, "ex Urbe die 13 junii 1478": a Florentine letter
  intercepted by Siena during the Pazzi war. Two cipher blocks (~11 lines). Not a Sienese key; R4752 (Bichi 1478)
  does not fit.
- **No. 20 (R4808).** "Sacra Regia Maiestas, Serenissime princeps ac metuendissime domine, post terre pedum
  oscula": ~18 lines of continuous cipher (lowercase letters, digits, ÷), "Scriptum ... die penultimo mensis
  Martii". The largest ciphertext in the fascicle. Now George Lasry's siena2023 (with no. 23).

## No. 11 (R4800), Acciaiuoli 1478: no key in reach

- Florentine letter (Donato Acciaiuoli to Lorenzo de' Medici, Rome 13 June 1478), held in Siena (intercepted in the
  Pazzi war?). 409 cipher tokens / 44 signs: homophonic anneal fails. Gabbrielli's key volume I (Ilardi reel 58,
  index frames checked 24 Sept) lists Acciaioli keys only for Giovanni 1504 and Roberto 1505-14; no Donato 1478.
  Florentine keys to Lorenzo (Medici avanti il Principato) are not online. Open.

## Nos. 7, 9, 19, 21 transcribed (agent J, 24 Sept)

- **No. 7 (R4796)**: despatch to the "Officiales Balie" from an orator at Milan ("Servitor ... Orator Ant..."; Lionardo
  Benvoglienti named; the Duke of Milan), 363 cipher tokens / 45 signs in ~11 lines, faint interlinear letter glosses.
  Key R4750 (Milan ambassadors 1454) tested sign by sign on the image (agent G): does NOT fit (gloss contradicts it,
  20% of the signs are not in it, its only e-sign is 2.5% of the text); an earlier "milano" was a solver artefact from
  free signs, withdrawn. R4753/R4754/R4756/R4757/R4762 also fail. The L08 gloss gives a partial key: 7=l, q=a, 6=n,
  +=o, B3=t, 2=e, x=r, 8o=i, c=o (`transcripts/no07_reading.txt`).
- **No. 9 (R4798)**: undated slip, quelli da Coreggio, Carpi, Rimini, "re di Ragona" (c. 1495-1516?); 46 cipher tokens
  in two runs + a cipher signature group. Too short for ciphertext-only.
- **No. 19 (R4807)**: Sienese envoys waiting on the "S. Capitano", 9 March (no year); 118 cipher tokens / 37 signs,
  clear cribs between runs. Too short alone.
- **No. 21 (R4809)**: informal letter "Karissimo come padre"; 107 cipher tokens / 35 signs (crosses, squares, Λ);
  signature group in cipher + "vostro". Too short alone.

## Solver calibration (24 Sept)

homsolve2.py breaks a synthetic Italian homophonic cipher of the same size (2,673 tokens, 58 signs, 3% nulls)
perfectly (-1.74/token). The real nos. 6/24 and 20/23 stay at -2.9/token under every variant tried (Italian, Latin,
Catalan, Spanish; f-groups merged; 'p p' merged or dropped; crossed or superscripted signs as nulls; null-aware
homsolve3). So these two systems are not plain homophonic letter substitution as transcribed: expect syllabic or
code signs (nomenclator), polyphony, or look-alike signs merged/split by the transcribers.


## Nos. 15, 18, 22, 29 (agent K, 24 Sept; nos. 15/18 under re-verification)

- **No. 15 (R4803)**: Mario Bandini, Sienese orator at Charles V's court, "Di Hellsprunth(?) alli 29 di X.bre MDXLVI"
  (+ PS 3 Jan) and 4 Jan 1546 s.s. = 1547; cipher only on pp. 2 and 6 (~230 signs). Key candidate by sign style:
  R4764 "Cifra con m. Bernardino Buoninsegni oratore a S. M.tà" (nulls row includes the ÷ run-opener). Transcript
  unverified (images failed to display for the transcriber) -> re-verification under way.
- **No. 18 (R4806)** (now its own entry, `targets/siena18/`): Latin articles negotiated by Sienese orators with a king/emperor, subscribed "Niccolo Zieg[le]r
  Regis Secretarius" (c. 1515-20?), ~185 point-separated cipher words (~1,100 signs) inside the Latin. Transcript
  unverified -> re-verification under way.
- **No. 22 (R4810)**: four drafts of a conspirators' letter (signal fires and smoke "alle pietre", spingarde, "la
  lettera di Calisto" = Calixtus III, 1455-58); clear draft A pairs with numbered draft B, C with slip D: the drafts
  are their own key (4 = .L., 7 = denari, 15 = parti, 16 = accordo, 17 = speranza; 5 = fanti?, 12 = romore?;
  2, 3, 8, 19 unknown). Read at the time in effect (the clear drafts).
- **No. 29 (R4814)**: torn scrap of a word list/nomenclator ("Ungaria — 1&7", "Giovan[ni]", "Lodyo"), not a letter.

## Remaining gaps

- no. 1 (1421), nos. 2, 26, 27, 28 - blocker: needs-physical-access; not among the DECODE photographs of the busta (R4790-R4814); only ASSi can supply them.
18 Oct 2026: moved out, solved by George Lasry (sections above): "no. 11 (Acciaiuoli 1478) - no-key-material";
"no. 17 (1528) - too-short"; nos. 9 and R4794 from "nos. 9, 19, 21, R4794 - too-short"; no. 15 reduced. His results
show that "too-short" was too pessimistic for pieces of 165-282 signs; it now stands only where he failed too.

- no. 7 (363 tokens) - blocker: too-short; R4750 ruled out; nine gloss values only; also unsolved by George Lasry (17 Oct 2026).
- nos. 19, 21 (118 and 107 tokens) - blocker: too-short; no filed key fits; also unsolved by George Lasry (17 Oct 2026).
- no. 15 (Bandini 1547), the 165 of 240 signs George Lasry left unread - blocker: too-short; Latin-letter code words and rare signs; the only candidate key, R4764, was transcribed and does not match.
- number and name codes in George Lasry's readings (R4794 codes 26, 44, 67, 74; no. 12 sender and name signs; no. 17 'el Mustetto', 'Otto') - blocker: no-key-material; each occurs once or twice, and no nomenclator for these letters is among the 43 key sheets of fasc. 1 (Key index above).

## Escalation

- [x] siblings: every record of the busta opened (keys R4746-R4789, letters R4790-R4814, R1858); no. 13/16 pair found; the pieces with recovered keys are separate entries.
- [x] clear-pages: no. 16 = decipherment of no. 13; decipherment on no. 8's sheet (aligned sign by sign, 20 Oct 2026); glosses on nos. 7 and 10 used; no. 22 clear drafts paired with numbered drafts.
- [x] known-keys: fasc. 1 alphabets compared by eye with every letter (R4755 missed for nos. 6/24; found by George Lasry, 14 Oct 2026, see siena1431); R4750, R4753, R4754, R4756, R4757, R4762 tested on no. 7; R4760, R4768, R4778 on nos. 17 and 20; R4764 on no. 15; Gabbrielli vol. I index (Ilardi reel 58) for no. 11.
- [x] print: Meister 1902, Cecchini 1952 inventory, Senatore 2009, Treccani DBI; no printed decipherment of any of these pieces found.
- [x] key-rebuild: homsolve2/homsolve3 (nulls)/sylsolve (bigrams) on the short pieces (and on nos. 20+23, now siena2023); no. 7 partial key from its gloss.
- [x] key-rebuild (outside): George Lasry rebuilt the keys of R4794, nos. 9, 11, 12, 13, 15 (part), 17 (18 Oct 2026); checked on our transcriptions 20 Oct 2026.
- [x] retry: 20 Oct 2026, his keys run on our own transcriptions of nos. 11, 17, R4794 and 20 (verify_lasry.py); nos. 7, 19, 21 have no key from anyone to rerun.

## Assumptions for George's review

- Nos. 6 and 24 are counted only in his siena1431; nothing of this folder's failed attempt on them is claimed.
- The unread pieces are kept together here as one "attempted, open" entry because they are one bundle; no shared key
  is claimed. Nos. 20 and 23 are George Lasry's siena2023; nothing of this folder's failed attempt on them is claimed.
- The pieces deciphered at the time (nos. 8, 10, 13/16, 22) are not entered as results.
- George Lasry's 18 Oct 2026 solutions (R4794, nos. 9, 11, 12, 13, 15 part, 17) are recorded here as outside solutions
  and verified on our transcriptions; this entry's own outcome stays "not solved". Under the one-key rule they could
  become his own entries like siena2023; not done here, his call.
- His key table for R4794 lacks the H and R columns (our A = r, N = h from his reading); worth telling him.
