# Port Sainte-Marie spy report, c. July 1729 (catalogue 826)

Status: read (134 of 141 groups, 95%), key rebuilt from the glossed siblings in the same file.

Huntington Library, William Blathwayt papers addenda, mssBLA 191, p. 5 (HDL p15150coll7 id 61005;
compound object 61008). Enclosure to a covering letter to the Duke of Newcastle of 8 Aug 1729. French,
numerical one-part code (groups 1-1370), alphabetical: syllables, words and names in one sorted list
(18 a, 278 de, 580 je, 581 ie, 585 ig, 1154 vous ...). 1240-1370 unglossed separators/nulls.

## Method

1. Transcribed p. 5 from the HDL image (`ct_p5.txt`, 141 groups, 13 lines).
2. Transcribed the glossed siblings in the same series (`pairs_A.tsv`, `pairs_B.tsv`, running texts in
   `pairs_*_text.md`): mssBLA 187 p. 3 (HDL 60963, cipher of the letter of 23 June, deciphered 19 July 1729),
   the 29 June letter (60917-60920), the 14 July letter (60887) and the letters on 60907-60909
   (incl. 3 Nov 1729). 942 code/gloss pairs, 364 distinct codes.
3. `decode.py` applied the table: 116/141 groups read directly.
4. Filled 15 more from context plus the alphabetical order of the code (`pairs_zinf.tsv`):
   585 ig (ig-no-re, ig-no-ra-n-ce), 275 dans, 222 conduite, 816 ordre, 666 lu, 1118 trouver, 689 m (de m-ar-s),
   460 fe (fe-re-z), 84 apres, 1152 vos, 1210 six (between 1209 cinq and 1211 sept), 805 obligation,
   285 di, 711 maine (se-maine-s), 1250 separator.

## Reading (`decode_p5.txt`, normalised)

L'obligation que je vous ai, Milord, est bien grande pour votre lettre du [6]. J'y ai répondu ce six de mars
à la première adresse. Quand vous me ferez sçavoir, comme je dis, [il s']agit après le départ du [274], car
Monsieur Keene ne m'avoit [rien dit], mais il [254] a aucun ordre des semaines pour moi [937] dans l'affaire
passée. Je lui ai fait trouver bon [1052] ce, sans qu'il m'ait jamais dit ce [726] je pouvois faire pour le
mieux à l'accommodement. [836]es je ignore vos intentions, et je serai inutile dans l'ignorance. Mandez-moi
donc quelque ordre pour ma conduite ...

English: The obligation I owe you, my Lord, is very great for your letter of the [?]. I answered it this sixth
of March at the first address. When you let me know, as I say, it concerns [what follows] the departure of
[?], for Mr Keene had [told] me nothing, and there has been no order for me for weeks in the past affair. I
got him to approve [?] this, without his ever telling me what I could do for the best towards the
accommodation. [Now?] I do not know your intentions, and I shall be useless in ignorance. Send me then some
order for my conduct ...

The agent complains that Benjamin Keene (British envoy in Madrid) leaves him without orders during the
accommodation (the Treaty of Seville talks) and asks Newcastle for instructions. Same agent and code as the
29 June letter, which asks for a new cipher, an address and money.

## Remaining gaps

- 7 groups (5%): 6 (a number, date of Newcastle's letter), 274 (a name or d-word after "départ du"), 254,
  937, 1052, 726, 836. None occurs glossed in the five siblings; alphabetical neighbours narrow them only to a
  letter range. Outside blocker: no further glossed letter in this code is digitised (mssBLA 184/186 are
  unglossed).

## Escalation

- Siblings: all glossed letters in mssBLA 187-191 used (60887, 60907-60909, 60917-60920, 60963).
- Alphabetical-order interpolation tried for every gap; the seven above stay ambiguous.
- Known keys / print: none found (not on DECODE, no printed edition).
- Retry possible if the Huntington images further Port Sainte-Marie letters (mssBLA 185-195 not all digitised).

## Prior solution

None: catalogue says undeciphered; the leaf has no gloss (checked 28 Oct 2026).
