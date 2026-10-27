# Biermann to Meyercron (Paris), Copenhagen 23 March 1675: cipher passage

Source: Rigsarkivet, TKUA Almindelig del, Conrad Biermanns kopibog 1675 (S-1418), pp. [103]-105,
Arkivalieronline images 108 (heading, clear opening) and 109 (cipher, pp. 104-105; id 48574060).
Key: TKUA "Chiffer" 1670-1709, image 55 (id 48691530), the sheet headed Pomponne 111 / Terlon 112 (`key.tsv`).
Transcription: `transcription_p104-105.txt`; mechanical decipherment: `python decode.py transcription_p104-105.txt`.

Clear text before the cipher (p. 104): the King has not yet decided on the instructions for the
coming campaign; Count Niels Brahe's negotiation is in the same state, since he has no orders from his
King on the counter-project, which keeps raising difficulties over annulling the Gottorp treaty; the
Grand Chancellor has had the counter-project given to Terlon in French and has let him hope for
articles of an alliance with France. "Nonobstant quoy ..."

## Line by line

| line | decipherment |
|---|---|
| 104.21 | [obstant quoy] sa Majesté veu-t que |
| 104.22 | vo-s ne la-i-s si-e-z |
| 104.23 | pa-s de co-n-ti nu-e-r |
| 104.24 | [toujours] a la co-u-r [ou] vo |
| 104.25 | -u-s-e-s te-s le-s me-s |
| 104.26 | me-s ra-i so-n ne me-n |
| 105.01 | -t-s que vo-u-y-a ve-z te |
| 105.02 | nu-s ju-s que-s i-c-y [et] |
| 105.03 | [particulierement que] vo-u-s lu-y |
| 105.04 | fa-s si-e-z co-n no-i-s |
| 105.05 | -t-re le pe-u de ra-p po-r |
| 105.06 | -t qu-o-n-t le-s de ma-n |
| 105.07 | de-s de l' {Ambassadeur de Suède} a ve-c le-s |
| 105.08 | f-ru-i-t-s a va-n ta ge-u |
| 105.09 | -x qui-l a vo-i-t fa-i-t co |
| 105.10 | -u-r ri-r a-u pa ra va-n |
| 105.11 | -t de sa co-m mi-s si o |
| 105.12 | -n [et] le-s ra-i so-n-s e vi |
| 105.13 | de-n te-s [et] so li de-s |
| 105.14 | que sa Majesté a de c-ro-i re |
| 105.15 | que la-r de-u-r que le di |
| 105.16 | -t {Ambassadeur de Suède} fa-i-t pa ro-i-s-t |
| 105.17 | re po-u-r co-n-c lu re |
| 105.18 | que-l que {traité} ju-s te [et] ra |
| 105.19 | -i so-n na-b le-i-c-y ne |
| 105.20 | -s-t [guerres] si-n ce re [veu le] |
| 105.21 | [peu dapparence quil y a que] sa Majesté |
| 105.22 | pu-i-s se co-n de-s co |
| 105.23 | -n-d re a-u-x co-n di ti |
| 105.24 | o-n-s qui-[?] p-ro po se |

## Reading

Nonobstant quoy sa Majesté veut que vos [= vous] ne laissiez pas de continuer toujours à la cour où vous
estes les mesmes raisonnements que vous y avez tenus jusques icy, et particulièrement que vous luy fassiez
connoistre le peu de rapport qu'ont les demandes de l'Ambassadeur de Suède avec les fruits avantageux qu'il
avoit fait courrir auparavant de sa commission, et les raisons évidentes et solides que sa Majesté a de
croire que l'ardeur que ledit Ambassadeur de Suède fait paroistre pour conclure quelque traité juste et
raisonnable icy n'est guerres sincère, veu le peu d'apparence qu'il y a que sa Majesté puisse
condescendre aux conditions qui[l?] propose.

(In English: Notwithstanding this, His Majesty wants you to go on making the same arguments at the court
where you are as you have made so far, and in particular to make it understood how little the Swedish
ambassador's demands match the advantageous results he had earlier let it be rumoured would come of his
commission, and the clear and solid reasons His Majesty has for believing that the eagerness the Swedish
ambassador shows to conclude some just and reasonable treaty here is hardly sincere, given how unlikely
it is that His Majesty could agree to the conditions he proposes.)

## Measure

- Cipher tokens: 263 (counted by `decode.py`).
- Tokens that give sense: 262 (99.6%). Open: one sign, the open square in 105.24 (`qui [?] propose`, most
  likely "qu'il"), not on the key sheet.
- Scribal slips kept as written: 104.22 `673 10` = "vos" for "vous" (no u sign); 105.22-23 `343` (co)
  where the sense needs 341 (ce): "condescondre" for "condescendre".
- Values taken from use, not from the sheet: 154 read "Svenske Ambr." (the sheet's first word is unclear,
  "Svenske"/"Spanske"; the context is the Swedish ambassador Niels Brahe); 468 = ju (sheet has ju 467,
  468 not written); 592 = qu (sheet writes "que" twice, 589 and 592).
