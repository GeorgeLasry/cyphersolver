# fr. 15571 f. 177r-v: reading log (22 Oct 2026)

Brief: `READING_BRIEF.md`. Images: fr. 15571 (ark `btv1b90618802`) canvases 184, 185 and 186, fetched full size
(about 7840 × 5970) from openapi.bnf.fr IIIF v3 (gallica.bnf.fr/iiif answers 403). Line and figure crops were kept in
the session scratchpad, not in the repo. Transcription: Michael Brackx, `brackx2026/f177r_cipher.txt` (29 lines) and
`f177v_cipher.txt` (11 lines).

## Pass 0: the published decode

`texts/fr15571-f177.txt` (Brackx's figures, `key_cipher1.json`, beam + 6-gram). `_check_reading.py --file`:
25 sentences, 6 clean, **clean share 0.24**, hole rate 0.229.

## Pass 1: reading against the letter sets (worked)

The decode was read line by line against each figure's set, not the beam's choice. Most of the text forms with no
change to the figures: *assiegeant Pons et Tailebourg, que l'on disoit que l'on pouvoit faire tout ensemble, et que
indubitablement l'on les emporteroit* (r. 1-4; the beam had *le bourg* and *eusteste asse en si s*: B qu th m B qs de x
= *eust esté*, ao y U t sz B tm oi ts = *aux ennemis*); *specialement pour Tailebourg*; *grand revenu qu'ils tirent du
passaige de la Charante, où ils levent de grandes impositions*; *jouissance des tailes*; *que l'on dict monter
beaucoup*; *y estans desja si disposés* (r. 12-13; the beam: *nestans desia se disposes*); *s'il venoit advis*
(qs 3 n qu h n4 7 o m: the beam had *el uenoit aduis*); *Monsieur le mareschal de Matignon s'y en iroit avec*; *et
preparer aussi ce qui seroit necssaire … y recevoir ceste armée à la primevere, cependant que nous continurions*;
*le vicomte de Turenne … estoit paru en campaigne avec forces et canons. Cela nous a soudainement faict changer
nostre premier advis*; *de sorte que nostre dicte depesche a esté convertie en celle que vous avés icy*; *voila
comment* (49 v E = *comme-nt*) *noz opinions sont erantes*; the verso almost entire.

## Pass 2: a clear copy found (worked; it changes the status of the leaf)

Looking at the opening for the leaf's verso showed that the **left page of canvas 185 (f. 176v) is a clear text signed
*Mr Forget***, and canvas 184 right (f. 176r) carries, below a marginal *Mons. du Mayne*, another twenty lines in the
same hand. Read from the image, they are a contemporary decipherment of this cipher, from *assiegeant Pons et
Taillebourg* to *beaucoup plus de temps que nous ne desirons*, the last words of the cipher on f. 177v. It was not
known to this project (NOTES and `f177_reading.md` do not mention it). The copy hand is a fast secretary hand; it was
read only as far as needed to check the cipher, line by line, and not transcribed in full.

How it was used: it chose between the letters a figure allows and it located the misreadings; it supplied the values
of two codes: **73 = *le Roy*** (*et remettre le Roy en la jouissance*; NOTES had 73 = the syllable *oi*, from f. 18)
and **64 = *quelque*** (*advis de quelque remuement*, *avec quelque peu de forces*; *un* had been proposed and not
adopted). It also showed that `me` and the barred double g are nulls on this leaf (the copy has nothing in their place
at seven places: *passaige … de la Charante*, *a eu … advis de Bourdeaux*, *de … l'armée*, *pour … clorre*, *Je …
pensois*, *de part … et d'autre*, *ne veult … point*). Every word of the reading is still carried by its figures; where
the copy and the figures disagree the reading follows the figures and marks the word (*[?nous]* for code 26; *[?ce
siège]* where the copy has *le siege*; *ce [?pais]* where it has *le pays*; *dicte depesche* where it has *depesche*).

## Pass 3: the breaks, checked on the image

The cipher was cropped line by line at full resolution (canvas 185 right, lines rising about 4.5% to the right; canvas
186 left) and every break compared figure by figure with Brackx's labels. Twelve label changes
(`brackx2026/corrections/f177.tsv`; corrected figures `brackx2026/corrections/f177_cipher.txt`):

| line | what the image shows | what it fixes |
|---|---|---|
| r. 5 | a T-shaped cross (T = r), not t | *oster* (was *ostee*) |
| r. 7, 20, 29; v. 6 | a barred double g, not the W-shaped double y (ss) of r. 1 *assiegeant* | null (new label `gg`) |
| r. 9 | an r-shaped figure with a foot, not n (uncertain) | *ce [?pais]* |
| r. 11 | two o under one bar (the barred double o of f. 173), not `oo2` | *offroit* (was *odroit*) |
| r. 13 | *1* and a 4-shaped cross with a dot: code 14 written as this hand writes it, not *1* + a star | *que nous consentions* |
| r. 21 | the open-box sign (q), not the 4-shaped q1 (o) | *pacquet* |
| r. 25 | z with a tail (u), not sz | *veult* |
| r. 25 | a heavy barred infinity at the line end, left out of the file | null (new label `oo3`) |
| v. 5 | a large C (Cl = l), not U | *il y a* |

Leaf key `key_cipher1_f177.json` (the shared key is unchanged): `gg`, `me`, `oo3` = null; 73 = *leroy*; 64 =
*quelque*; `oob` = ff/f (as on f. 173); `u` = q (as on ff. 196/201).

`_check_reading.py --file texts/reading_f177.md` after pass 3: whole file 95 sentences, 65 clean, **clean share
0.684**, hole rate 0.116 (header, notes and the list of open points included, which the checker scores as French);
the cipher text alone (section *The cipher*) 29 sentences, 20 clean, **clean share 0.69**, hole rate 0.081.

## What failed or stays open

- Re-decoding with the beam was not repeated after the corrections; the reading was made by hand from the sets, as on
  ff. 173 and 110 (the beam fills wide sets with short words).
- Fourteen marked places stay open, each with the figures checked against the key and the copy (listed in
  `reading_f177.md`, *What stays open*). Most are one figure that the key does not give the needed letter for:
  r. 14 ∞ where *remuement* needs m; r. 16 6 for e in *forces*; r. 16 Cl for p in *oposer*; r. 18 c for r in *pour*;
  r. 20 U 6 for *ge* in *siège*; r. 26 *la m[o]itié* one figure short; v. 2 7 for i in *Matignon* and code 26 for
  *nous*; v. 3 one figure too many in *confesse* and *e n* after *je l'*; v. 9 a U between *trouvera* and *conforme*;
  v. 11 *des[ir]ons* two letters short. These were looked at on the image only for r. 14, r. 18 and v. 2; the others
  were not cropped figure by figure, so a misread label is still possible there. One figure is unread (`cs` after code
  84, r. 22).
- The four clear lines at the head of f. 177r (*Depuis Mr d'Aumont … Limozin … persuader avec de nouvelles
  raisons …*) were not read in full.
- The struck-through figures in r. 17 (between *pre-* and *-parer*) were checked: Brackx rightly leaves them out.
- The copy on ff. 176r-v is not transcribed here; it should be, as the leaf's crib, and NOTES should record it (not
  edited in this pass, per the brief).
