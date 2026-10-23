# Balbases (Nijmegen) to Fuenmayor (Copenhagen), 1677–78 — DECODE R985–R998

Status: in progress. read in part (reading audit, 22 Oct 2026; was: read)

22 Oct 2026, reading audit (George Lasry's test: can sentences be built and translated?): **read in part**.
The ten margined letters read, from their contemporary margin decipherments. **R992, R996, R997 and R998 are
decoded, not read**: the key decrypts them only into syllable streams with groups not in the key ("ve o la p ro te s
ta que lo no ministro s ce sa re os pu b li ro n"); the gist below was summarised from those streams and is not a
reading. 5,489 of 7,784 cipher tokens (70.5%) are in letters that read. The "Status: read" and the 97% below are
withdrawn as reading claims (97% is the key's coverage of the groups).

22 Oct 2026, re-read (REREAD_BRIEF, batch b12, Claude Opus 5.5): **R992, R996, R997, R998 stay decoded, not read.**
No contemporary text exists for them: the DECODE records hold only the images and DECODE's digit transcription, the
cipher pages carry no margin, and no clear copy or edition is known. The key decodes were segmented into Spanish word
by word (`research/reading_audit/b12_bal.py` prints each tx/ line as token=value) with second values that hold across
the letters: 63 = s as well as no (los, demás, sus), 77 = t (nosotros, atraer), the r-sign = stra/tra (nuestra,
tratar), 69 = ru (prudencia), 116 = carta. Images were checked at the breaks (R992 l. 10: 42, not 48, "resolución
violenta"; `read/R992_corrections.tsv`). Partial readings `read/R*_reading.md` (English `read/R*_en.md`, logs
`read/R*_reread_log.md`) score 0.29 (R992), 0.40 (R996), 0.41 (R997), 0.13 (R998) clean sentences, below the 0.60 bar.
What does read: R992 "pues de nuestra parte no nos [85] que hacer ... resolución violenta de esos confederados,
principalmente si, después de lo de Charleroy, instaren en la junta ..."; R996 "ni nosotros ni los demás aliados
tenemos tampoco parte ... Ha sido muy prudente la diligencia de evitar V.S. este oficio"; R997 "en que excuso discurrir
por no crecerme la melancolía"; R998 "cuando [189] la pérdida de Gante estamos temiendo la de Ipre[s] [...] otras
importantes plazas". The gist paragraphs below are superseded by these readings where they differ.

Fourteen ciphered despatches of Pablo Spínola Doria, 3rd marqués de los Balbases, Spanish plenipotentiary at the
Nijmegen peace congress, to Baltasar de Fuenmayor, Spanish envoy in Denmark. They are dated 29 June 1677 to 22 March 1678.
Archives générales du Royaume, Brussels, Secrétairerie d'État et de Guerre, inv. nr. 2559. The images and DECODE's
transcriptions were fetched on 19 Sept 2026 with the cookie in `targets/bordeaux/decode/cookie.txt`. They are in `decode/`
and are git-ignored.

**Result.** No key survives. None of the eight Brussels keys in the series fits (R958–R965, "chiffres 1647-98",
checked). The key was therefore rebuilt from the ten letters that carry a contemporary decipherment in the left
margin. It then reads the other four, which **nobody had deciphered: R992 (19 Sept 1677), R996 (1 Mar 1678),
R997 (8 Mar 1678) and R998 (22 Mar 1678)**. Across all 14 letters, 97% of the 8,150 cipher groups are covered by
the key.

## Method

1. Two agents transcribed every cipher line and every margin line from the images into `tx/R*.txt`. DECODE's own
   transcriptions leave out cipher lines, and its margin readings are poor.
2. Anchors came from n-grams that repeat across letters, checked against the margin text:
   - `58 28 10 65 y uf 22 16` = lo·s b·ru·n·su·i·c ("los Brunsuic")
   - `26 67 y di ed 28` = pr·i·n·ci·pe·s
   - `xo y no 23 ic 45 e` = co·n·fo·r·mi·da·d
   - `63 41 45 e` = no·ve·da·d
3. A hard-EM monotone aligner (`align2.py`) was seeded with these anchors. Each token emits a substring of the
   margin plaintext. The table converged in two rounds. `dec.py` builds the key and `key.json` is the frozen table.
   The decryptions are in `read/R*.txt`, each with its margin text for comparison.

## The key

This is a syllabic nomenclator with homophones. Groups are separated by spaces.

- **Single letters (numbers and a few signs):** a 21, 3+; b 10, n; c 9; d e; e 2+; g 16; i 22, 67; j u+; l 8, 19;
  n y, 24, 20; o 18; p 26; r 23, 31; s 28, B; t 27; y 25; z h; f x.
- **Consonant-vowel syllables in numbers:**
  - de 46; la 55; en 76; ra 65; re 66, 153; te 71; do 48
  - ta 70; lo 58; no 63; to 73; da 45; ti 72; di 47
  - le 56; ni 62; vi 42; ne 61; in 77; ve 41; va 40
  - na 60; on 78; an 75; li 57; ga 50; go 53; tu 74
  - vo 43; ar 80; gu 54; un 79; er 81; du 49; nu 64
  - ro 68; tr 188
- **Letter-pair syllables, consonant disguised, vowel kept:**
  - c is written x, d or l: xo/do/lo = co, xi/di/li = ci, xa/da/la = ca, xe/de/le = ce, xu/du = cu
  - f is written n: no fo, ni fi, ne fe, na fa, nu fu
  - y is written r: ro yo, ra ya
  - `=` = ui
- **Vowel-first pairs, read as reversed syllables with the consonant disguised:**
  - f for s: ef se, if si, af sa, of so, uf su; also ye es, ya as, yo os
  - d for p: ad pa, ed pe, id pi, od po, ud pu
  - c for m: ac ma, ec me, ic mi, oc mo, uc mu
  - q or g for h: aq/ag ha, eq/eg he, og ho
  - others: en em, ot ch, at cha, as za
- **Word codes:**
  - que: d+ (struck d), b+
  - de: p+, q+/g+
  - V.S.: H
  - para 05; por 15, is; sobre 184; quando 148; alguno 100; congreso 120; tam(bién) 185
  - ministro `des`; materia `dus`; duque `ep`; embax(ador) `§`; -mente `dan`; nue(stro) `fe`
  - Flandes `ban`; francia `bef`; franceses `bin`; Suecia 163; Dinamarca `or`; -bourg 105
- **Nulls and start/end markers:** 13+ and 13 (mostly), 300, 200, 700, 07, 01, 18+, 16+, 35.

Open: about 3% of groups are unassigned, mostly rare 3-digit name codes (82, 83, 150, 161, 182, 187, 189…). Some
homophones are also shaky: 41 reads di and ve, 77 reads in and ot, 61 reads ne and ri. These come from 4/9 and
similar slips in the transcription.

## What the four unread letters say (read from the key; gist)

- **R992, 19 Sept 1677.** On the protest the Imperial ministers published about the dissolution of the Bremen
  assembly. He has nothing to add: "de nuestra parte no nos queda que hacer sino es … temer" what the confederates
  will do. After Charleroi (the failed siege of August 1677) they may insist at the union that the conquests be
  shared out before anything positive is settled. A rumour here about the Danish chancellor, a brother of the
  duke, and the Duke of Celle. He gives it no credit, since V.S. has not reported it. The claim that the Duke would
  take his share of the father's conquests, the duchies of Bremen and Verden.
- **R996, 1 Mar 1678.** Sweden could not undo the distrust they feel towards the allies. What causes it is the
  miserable state of their own affairs and the allies' impatience. The proceedings of the Brunswicks rest on solid
  suspicions. He comments on the ministers of the northern princes, and on the thought of writing to them with a
  protest about treaties of peace that would leave out their participation. He praises V.S.'s diligence in
  avoiding that step. Strasbourg's lack of constancy. A French gentleman has returned from France "satisfied" with
  the Most Christian King. "We need the clarity of the [court] to set down the doubts we suffer from."
- **R997, 8 Mar 1678.** In the business of the Brunswicks' claim with the Danes to the treatment of ambassadors,
  nothing has been conceded. Nor was any formal act in writing made at the first step the other days. He comments on
  the discourse V.S. reports of the Duke of Hanover and his brothers. It all seems to him very heavy, "pero yo creo
  que nada de estas intrigas llegará a fin". He writes of "the incessant dangers in which we are placed" and his
  growing melancholy.
- **R998, 22 Mar 1678.** On the dependencies between the northern princes, who are of enough calibre to keep us
  embarrassed. He writes of the evils "que nosotros estamos padeciendo", worse than anything. He comments on V.S.'s
  prudence. On the loss of Flanders: "con la pérdida de Gante estamos temiendo la de otras importantes plazas".
  Ghent fell to Louis XIV on 9 March 1678. They are still waiting on the long delays of the others while the
  illness advances.

The ten margined letters (985–991, 993–995) are read at the time. The key reproduces their margins, and the
margins in `tx/` are the fuller text.

Dates (from the clear parts): R985 3 Aug 1677; R986 28 Aug; R987 18 (or 28) June; R988 29 June (docket 24 July);
R989 21 Dec; R990 19 Oct; R991 5 Oct(?); R992 19 Sept; R993 28 Dec 1677; R994 15 Feb 1678; R995 26 Jan; R996 1 Mar;
R997 8 Mar; R998 22 Mar 1678.

## Remaining gaps
- R992, R996, R997, R998 decoded, not read (2,295 cipher tokens; partial readings 0.13-0.41 clean sentences, re-read 22 Oct 2026): rare groups with no value in the key (fol, 85, 150, 182, 187, 17, 189, bon, i8 ...) - blocker: no-key-material
- the same four: stretches where the homophones do not segment and the 1616-px greyscale scans do not settle the doubtful figures (struck, overwritten) - blocker: needs-physical-access (originals at the AGR Brussels, SEG 2559)

## Escalation

Added by the reading audit (22 Oct 2026), which relabelled the documents that do not build sentences as decoded,
not read. Re-read 22 Oct 2026 (b12):

- [x] siblings: the ten margined letters and Ronquillo 1676 (same key) used for the second values; none is a copy of these four
- [x] clear-pages: the clear opening and closing paragraphs of each letter checked; they are not the decipherment
- [x] known-keys: the eight Brussels keys R958-R965 did not fit (19 Sept); key.json used
- [x] print: none known (19 Sept); not searched again
- [x] key-rebuild: second values 63 = s, 77 = t, r = stra/tra, 69 = ru, 116 = carta found across the letters
- [x] retry: all four segmented sentence by sentence; images checked at the breaks; below the bar
