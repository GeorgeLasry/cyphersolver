# Re-reading log, R43 (22 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch b00)

## Starting point

Reading audit (22 Oct): "decoded, not read". `R43_decryption.txt` was the character-model segmentation of DECODE's
transcription D1708 under Meister no. 40: the gist (the killing of Guise) clear, but garbled words in most lines
("riapea", "sode tod inuisa", "una curiano sempre catiui fici").

## 1. Is there a text already?

- DECODE images: 6 cipher pages (307r–309v) and 3 "cleartext" images, which are the covering letter in clear
  (305r–306r, Blois 19 Dec 1588, ending "Qui occluso sarà un foglio di cifra"), not a decipherment. No interlinear
  glosses on the cipher pages.
- Rome's decipherments of the legate's ciphers are in ASV Segr. Stato Francia 27 (Hübner, *Sixte-Quint* II, 1870,
  p. 209 n. 1: "Le cardinal Morosini au cardinal Montalto. Blois, 24 décembre 1588; déchiffré à Rome, 9 janvier 1589.
  Arch. du Vatican, France vol. XXVII, fol. 248"; further dates there for 31 Dec, 15, 26, 31 Jan, 23 Feb 1589). Not
  imaged online: blocker for using it = physical access.
- Print: Tempesti, *Storia della vita e geste di Sisto Quinto* (Rome 1754) II, book IX, pp. 109–111, paraphrases this
  letter between quotation marks (archive.org storiadellavitae02temp); Hübner compared Tempesti with the originals and
  found it faithful in substance. It is a modernised paraphrase, not the decipherment; used for names and sense only.

## 2. Word decode

`research/reading_audit/reread_b00_decode.py` (new, this batch): Viterbi/beam search over *words* (trie of the
Nuntiaturberichte + Guicciardini/Machiavelli vocabulary with single-for-double variants, word bigrams), Meister's
homophones, nulls 8 and 80–89 (Lasry's key on DECODE R18 lists the single 8 too), and a slip model (one figure
substituted/dropped/added at a cost, cheaper at the transcriber's '?'). Output `R43_worddecode.txt` / `_figs.txt`.
It turned most garbles into words; about one word in ten still needed re-parsing.

## 3. Breaks re-parsed by hand (R43_corrections.tsv)

- Spurious nomenclator dots in the transcription were the largest single cause: 250 (= "Bles" in letters), 150, 214,
  712, 350, 617 are plain letter groups with a dot on one figure; 716, 516 and 916 are 165/166 with the dot written on
  the wrong figure; "137" (abbatia) is machina|ua.
- Vocabulary gaps where the figures were right: gabineto, esequirono, fermare, aterato, pugnalate, Ianuile, d'Umala,
  saluieta, sraticare, logotenente, "per adeso".
- An abbreviation the key does not list: m + 8 for -mente (medesimam., principalm., liberam., instantem.).
- Image checks (crops, scratchpad only): 308r ll. 1, 22–23 (al gabineto come esequirono: transcription confirmed).

## Result

Before: 0.58 clean-sentence share (`_check_reading.py` on R43_decryption.txt). After: 0.74 on the "## Reading" body
of `R43_reading.md` (the checker counts the cipher clerk's spellings — sodeto, uiuente, necesita — as holes); by hand,
13 holes ([…]) and 6 partly
carried words in about 1,250 words, every sentence of the narrative carried. Grade B: several single-figure
corrections from context (tsv "figures+context").

## Still open, and why

- The opening figures of 308r l. 2 and "2 3 8" before 129; 309v ll. 9–11 (a line and a half); 308v ll. 19–20 (two
  short stretches); 307r l. 10 ("credeua che … biasimare"); 307r l. 23 ("risposta del …"); the closing formula 307v l. 2.
  No word parse fits the transcribed figures; most were not re-checked on the image (blocker: none outside; left for a
  second image pass). Francia 27's decipherment would settle them (physical access).

## Word-by-word alignment (REREAD_BRIEF step 3, added 22 Oct)

`python research/reading_audit/reread_b00_align.py R43`: 1,150 words; flagged letters checked one by one. Bracketed
as not carried: inc[l]inatione (309v), Ece[lenza] (307r: 5 2 5 3 5 then a null 8). Written as the figures give it:
"conpiacere" (19 = con + piacere). The other flags are aligner artefacts (spurious dots under Bles, machinaua,
seruitori; V. S. Ill.ma; "fermare", which the figures 3 0 3 5 0 0 2 0 2 1 0 0 5 carry).
