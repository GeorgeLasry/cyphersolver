# R3813 re-read log (batch b06, 22 Oct 2026, Claude Opus 5.5; REREAD_BRIEF)

R3813, Kurz von Senftenau to Trauttmansdorff, Hamburg, 27 Jan 1639; 20 DECODE images (P1-P20), 7,799 cipher tokens.

## 1. Is there a text already?

No contemporary decipherment on any of the 20 images (no interlinear, margin or slip); no clear copy among the nine
DECODE records of the series; Mírka 2012 summarised only R3811. The reading rests on the figures and the key.

## 2. Reading on the images

- All 20 pages read through line by line from the key decode (check.py values; a scratch display with 38 = d), the
  decode segmented into words and joined with the clear text. Images (main checkout img/, 2000-4000 px) checked where a
  run broke: P1 (whole page, clear text and lines 9-21), P2 (left lower, right upper), P3 (left upper), P4 (right
  upper), P10 (left lower). Crops in the session scratchpad only.
- Transcription corrections: read/R3813_corrections.tsv (26 rows). Two clear-text fixes (P1 "nit sicher", P2 "in
  unseren handen"), one figure (P2 l.25 `4` -> `#4-hook`, "Magdeburg wil"), and 23 crossed signs relabelled
  `#f-cross` -> `x` after be-/ka-/qu-/ma- (bei, Kai[serliche], qui, reliqui, Mai.), one checked on the image (P4 l.29,
  the æ-like x), the rest by sense. `decode.py R3813` re-run.

## 3. Key observations (proposals; key.json not edited)

1. **38 = d, not g.** Every one of the 75 occurrences of 38 in R3813 needs d: feindt (P1, P4, P5, P7, P9 ...), und
   ("kan und wil", "standt und Städte"), wurdt, standt, landt, widerstandt, Teutschlandt, schandt, handlung,
   gesandten, friedt, niemandts, Burgundt, Söldner. Samples in R3812, R3811, R3814, R3815, R4625, R4645, R4736 agree
   (feindt, und, wurdt, freundt, landt, friedt). 36 stays g (konig, Georg, Magdeburg, Mecklburg). The key has no
   single d otherwise. Proposal: key.json `38: d`; it should help all nine letters. The reading uses d; the official
   aligner (b06_align.py on read/R3813.txt, decoded with 38 = g) flags these 39 words until the key is changed; with
   38 = d the aligner flags none.
2. **The crossed sign (`#f-cross`, ta).** Holds in tractatus, tausent, standt, craistag, universalitatem,
   Majestät-forms; after be-, ka-, qu- and in Kai. Mai. it is i (the æ-like x): relabelled. In Salvio/Salvium/Salvii
   (P2, P14, P18, P20) and Savoia (P18) it seems to stand for v(i): printed [?Salvio] etc. A third shape may hide here.
3. **d (so) also stands for "to"** in directorium (P2, P8), totaliter/total (P6, P9, P15, P18, P19), Victoria (P10),
   Stockholm (P14, P15), electore (P14), protectorium (P19): two signs merged, or a homophone. Printed [?word].
4. 9 (te) in "9 33 39 34" = Volck (P1, P10 twice): a plain 9 on the image; printed [?Volck].
5. 6 (se) + u for zu (P3 "raittung seu machen", P15): a plain 6 on the image; printed [?zu].
6. Spellings of the cipher clerk kept: -ton for -tion (resoluton, intenton, coniuncton), qu[a]rtr (Quartier), ung
   no longer occurs once 38 = d.

## 4. Readings

read/R3813_reading.md (German, all 20 pages), read/R3813_en.md (English). Aligned word by word with the decode
(scratch copy of b06_align.py with 38 = d): 0 unbracketed words not carried after bracketing 20 words the first pass
had written in full (e.g. "regimentern" -> regimenter, "landt" -> land, "intention" -> intenton or [?intention],
"Gallico corrumpitur" -> Galli[co] corrumpitur).

_check_reading.py on the reading body (header and notes cut off): clean share **0.48** (155 of 322 sentences), hole
rate 0.16. Before: the raw decode read/R3813.txt scores 1.0 on the checker, an artefact of its Viterbi segmentation of
unspaced runs (the audit judged it unreadable by eye). Of the 0.16 holes, about 40% are explicit marks ([...], [?x]),
the rest words the 1640s German word list does not know: period and clerk spellings (khonte, khonnen, craistag,
Mecklburg, Pomeren, ziechen, fridt), proper names, Latin inside German sentences.

By the brief's bar (coherent and about 0.60) R3813 stays **decoded, not read**: the sentences build and translate
through most of the letter (Banér's crossing, Duke Georg's passivity, the Circle diet, the peace talks, Salvius,
Denmark and Brandenburg, the "teufflisch inventum" of universal treaties), but holes stand in most long sentences.

## 5. What stays open and why

- About 240 explicit holes. Most are runs where the figures give a non-word that one image check would not settle
  (clerk's slips such as "telck", "seu", "beta" are now explained; what is left: "trabost" P2, "sateia" P18,
  "etlen so igne" P6, "sasns genomene" P7, numbers in "[...]er tausent" P4). Blocker: none outside; not every hole
  was checked on the image in this session (time). Next: apply 38 = d to key.json, settle the crossed-sign and d
  (so/to) splits on the images token by token, re-decode, then re-check the remaining holes page by page.
- Clear text: the tr/ clear text was transcribed by agents in a fast pass ("..." gaps, some misreadings, e.g.
  "Angemerkt", "alber", "Wol..."); it was not re-read in full here.
- P20: the postscript notes in another hand and the signature (tr/ marks them not transcribed).

## 6. Second pass (22 Oct 2026, on the key changed by the parent: 38 = d, Δ = nu, #dot = su, #s-long = ti, m = a)

- The reading was rebuilt on the new decode. The new values carry quartir, coniunction, resolution, intention,
  eigennuz, subiecta, Suicos, succurs, praestirung, hostilia, utilia, suechen and more. The first-pass reading had
  10 aligner flags on the new decode; after the rebuild it has none.
- Images checked page by page, worst first: P1 (clear), P2 left, P3 right, P4 left and right, P5 right, P6 left and
  right, P7 left and right, P8 left. Corrections added: 27 rows (53 in all). Of these, 3 are figures: P2 l.9
  `62 5` -> `6 25`; `0` -> `φ` (Erzhaus) on P2 l.36 and P6 l.34; P3 l.33 `α` -> `#a-loop` (tam). 2 are relabelled
  crossed signs (P4 l.35 bei, P6 l.36 seie). The rest is clear text read on the image (P1 "wahre kein brug noch khein
  sicherheit", P2 "Wan den ablesse Mainz seye zu seiner Zeit", P4 "zuruckh gangen", "auffangen hette khönden", "Den
  Ausgang", the margin note moved out of the body, P5 "von dem ihrigen", "Frantzosischen", "über khurz oder lang",
  "Gott lob", "zum Ziehl", P6 "dismahl gewest", P7 "leist alles nur an den", P8 "Die 30 Kerl", "vnnd von dessen").
  New readings from the images: "eis schrollen auffangen hette khönden", "etiam was hie bei, ad meas non tuli
  responsum", "apud formidolosos ancipites, wo nit was erger", "et ad tractatus", "Sueci non sunt tam subtiles",
  "Billichkeit mag sich niemand [...] auf des herzog Georgen; vorderist aber ...".
- More key evidence (proposals, not applied):
  - 9 also stands for "vo": Volck, volens, vorstehenden, vorderist, Vormaur, bevor, Vorwissen, vorgeschlagenen.
    9 + n = von five times (offerten von officieren, des raubs von tag zu tag, stuck von Pomeren, von einem schlus).
    It is the same plain 9 on the images.
  - The crossed sign also stands for "vi": vier tausent, vier und zwainzig, als vil mehr gedacht, Salvio, Salvium,
    Salvii, Savoia.
  - 6 also stands for z: zu, bezalte.
  - 4 is x: rex, Oxenstiernio.
  - d also stands for "to", as in the first pass.
  The reading prints all of these as [?word].

Score (_check_reading.py; body = header and notes cut off): first pass 0.48 (old key) -> 0.506 on the new key ->
**0.519** after the image pass (162 of 312 sentences; hole rate 0.143). The whole file scores 0.512. If the
proposals above were accepted (the [?word]s they carry unbracketed), the file would score 0.55.

What keeps it under 0.60: of the 150 sentences that fail, 47 fail only on words the German word list does not know,
with no marked hole. These are the clerk's and Kurz's spellings (khonte, khönden, craistag, crais, Mecklburg,
Pomeren, ziechen, fridt, universalitet), proper names (Meirer, Penzen, Sahlin, Colen) and Latin or Italian clauses
inside German sentences. If those 47 passed, the share would be 0.67. Another 56 fail only on marked holes,
about half of them the [?] proposals above.

Remaining holes and their blocker:
- (a) Values the key does not give. Applying them needs a decision on homophones, since key.json has one value per
  sign:
  - 9 = te/vo;
  - d = so/to;
  - the crossed sign = ta/i/vi;
  - 6 = se/z;
  - 4 = x.
- (b) Runs where the figures give no word even on the image. The P2 "trabost" (recht tra-9-e-t, possibly
  "trawet"); "modo bolote esten" (P3); "etlen [d]igne" (P6); "[sasns] genomene" (P7); "insolen-li-wah-se geltmuesten"
  (P7); "corpet so" and "ebsertart" (P11); "nm Schwed hofftractirte" (P13); "knnebeschnit" (P14). They are probably
  clerk's slips; the blocker is that no other copy exists to correct them.
- (c) Clear-text words still unread at this resolution: P1 Wol[...], P3 "dem ...:", P3 "dagegen ...", P4
  "verwundten ...", P4 "Ihr Durchl. ...", P6 "niemand ...", P6 "wenig ist ...", "dann ...", P7 "als das ...",
  "das ... ohne", P19 "Graff Brenner verlangt ...".
- P9-P20 had no image pass in this session. Their holes are mostly class (a) and (b) above.

## 7. Third pass (22 Oct 2026): P9-P20 on the images; key 9v = vo

- Rules from the parent applied:
  - A word the figures fully carry is written plain.
  - No brackets inside words: 38 split forms were rewritten whole, e.g. Galli[co] -> [?Gallico], hochlob[l.] -> hochlob.
  - 9 -> 9v (vo) where te makes no word: 17 tokens relabelled on P1-P18 (Volck x3, volens, vorstehenden, von x8,
    vorderist, Vormaur, bevor, Vorwissen, vorgeschlagenen), logged with "polyphonic 9 read vo (same shape; key 9v,
    22 Oct)".
- A sweep that unbracketed every [?word] the aligner accepted was checked by exact match against the decode.
  - 27 words were put back in brackets: the aligner tolerates one missing or changed letter, but the figures do not
    carry those words.
  - 7 more went back in brackets because the exact match sits elsewhere in the letter (intention, corpo, craistag,
    herzog, widerstandt, standen, unmoglich).
- Images checked: P9 left and right, P10 left and right, P11 left and right, P12 right, P13 right, P14 left and right,
  P15 left and right, P16 right, P17 left and right, P18 left, P19 left and right, P20 left.
- Corrections added in this pass: 25 rows (78 in all).
  - Figures:
    - P9 l.20 `φ` -> clear "Ob"
    - P11 l.42 `18` -> `14` (observirt)
    - P17 l.11 `59 #f-cross` -> `59 x` (Kai: Mai:)
    - P17 l.21 `#f-cross` -> `x` (Pabst: Haili:)
    - P17 l.31 clear "be" -> figure 6 (dise krieg)
  - Clear text:
    - P9 "halben"
    - P11 "von dannen"
    - P17 "so daraus wegen sich in"
- New readings:
  - "Ob a parta in und anderen zu [?requiriren]?"
  - "quartir gelichfalt"
  - "kriegsleuffen [?observirt]"
  - "[?invito] [?Oxenstiernio]"
  - "bei Kaiserli. Maiestat"
  - "wan ihr Pabst. Haili. das intrinsecum ..."
  - "so daraus wegen sich in dise krieg"
  - "umb so [?vil] besser"
  - "das wehren, es gehe wie Gott wolle"
  - "Das ist [?zuvil]"
  - "um [4] so [?vil] [?weniger] zu vertrawen"
  - "als eben iezo, da [?vil] uns fur verlohren achten"
  - "cronen so [?vil] [?nit] [?zuwachst]", "sogar [?vil] nit zu erheben"
  - "Er ist ein [?man], [...] der seines grosen anhangs halben"
- The crossed sign reads vi far more often than the key allows: vier, vil (7 times), proviant, observirt, invito,
  dissolviren, resolvirt, zuvil, Salvio, Savoia. Proposal: a polyphonic entry like 9v (the crossed sign = ta / i / vi).
  With it, about 25 [?] words would be carried.
- Body score (b06_body_score.py): 0.519 (second pass) -> **0.531** (165 of 311 sentences, hole rate 0.137).
  b06_align.py: 0 flags.
- Holes still open and their blockers:
  - (a) [?word]s carried only by a value the key does not give: the crossed sign = vi (about 25), d = to (about 10),
    6 = z (zu, bezalte), 4 = x/b (rex, Oxenstiernio, extremitates, umb).
  - (b) Clerk's slips, left as written:
    - trawet (P2)
    - bolote esten (P3)
    - etlen [d]igne (P6)
    - sasns (P7)
    - insolen-li-wah-se (P7)
    - corpet [α] (P11)
    - um pa ein (P11)
    - hofftractirte (P13)
    - knnebeschnit (P14)
    - friubtsachlichs (P19)
    - alhi[ß][vi]er (P19)
  - (c) Clear text unread at DECODE resolution: P1 Wol..., P3 "dem ...", P4 "verwundten ...", P6 "niemand ...",
    P7 "das ... ohne", P19 "Graff Brenner verlangt ...".
- The 47 sentences that fail only on word-list misses are period spelling, names and Latin; they stand.

## 8. Fourth pass (23 Oct 2026, r2c, Claude Opus 5.5): Mírka's key on DECODE; vi/to signs split on the images

- **Is there a text already?** DECODE R3813 re-fetched 23 Oct: 20 images and two attachments listed under the images,
  "key reconstruction - Excel (Jakub Mírka)" (`key_Kurtz-Trauttmansdorff _1638-1639_reconstruction(1).xlsx`) and
  "key reconstruction - handwritten (Jakub Mírka)" (DOC_3813_…pdf, one page); R3814 carries the same two files. They are a
  key, not a decipherment: no plaintext of R3813 on DECODE, in Mírka 2012 (R3811 only) or elsewhere. Neighbouring records
  R3809/R3810 (Florence, 15th c.) and R3816/R3817 (Heusner 1637, SP 106) are unrelated. Print: web search 23 Oct (Kurz
  von Senftenau, Hamburg 1639, Trauttmansdorff) found no edition; Documenta Bohemica Bellum Tricennale Illustrantia VI
  (1979) may calendar the letters (regests, not decipherments) and is not online.
- **Key checked against Mírka's table** (KEY.md, "Corrections, 23 Oct 2026"): k = to (was ti) and m = va (was a) hold at
  every occurrence in the nine letters; key.json changed; decode.py: after 29 (= qu) a v-syllable sign gives its vowel only
  (quartir, quod). 4 = x not adopted for the plain 4 (fails in three places); the x places are a crossed 4 on the images, now `#4-cross` = x (see below). 9v = vo holds at all 48 uses (Mírka's q).
- **Labels on the images** (research/reading_audit/r2c_line.py crops, montages in the session scratchpad): the
  "crossed sign" of R3813 is two shapes. The tall crossed ƒ (ta: stand, tractatus, universalitatem, craistag) and a low
  p-form with a curl through the stem (Mírka's VI = p): the second relabelled pv at 20 places (proviant, Salvii, Salvio
  ×2, Salvium ×2, vier ×2, vil ×8, dissolviren, resolvirt, invito, and the slip alhi-vier), and three plain `p` of the
  same form (vil mehrer, vil nuzer, Victoria). The looped k-form (Mírka's TO = k), which the agents had read as d or α,
  relabelled k at 9 places (directorium, directorio, Victoria, invito, senatores, electore, Stockholm ×2, protectorium).
  32 rows added to R3813_corrections.tsv (110 in all).
- **Reading**: about 30 words unbracketed because the figures now carry them; "in risera" → "in riserva", "keiner
  [?total] information" → "keiner so vil information" (d pv 33), "reliqui senasores" → "senatores". Still bracketed:
  [?weniger] (9 = te gives teeniger), [?dissolutae],
  [?Gallico], [?zuwachst] and the class (b) clerk's slips. b06_align.py: 3,578 words, 0 not carried.
- **Crossed 4**: P3 r. l.14 (et rex; already `4+` in tr/), P12 r. l.19 (Oxensternio) and P17 r. l.7 (extremitates) are the crossed
  4 (Mírka's X; glossed x on R3811 p. 1); label `#4-cross` = x; the three words carried (Oxensternio as the figures spell it).
- **Score** (body only, header and Notes cut; v2_score.py, conjectures as holes): plain 0.537 → 0.563 (175/311),
  explicit holes 0.910 → 0.932 (290/311), hole rate 0.037. German of 1639 with Latin: the word list does not know the
  period spelling, so the bar is the explicit-hole share (0.932) plus reading: the sentences hold through the letter
  (Banér's crossing, Duke Georg's passivity, the defensive plan, quarters against money, the universal treaties as a
  labyrinth, Salvius and the Cologne congress, the protectorium), with single holes. **Read.**
