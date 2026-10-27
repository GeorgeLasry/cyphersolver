# Revenga's intercepted letter from Madrid, 1822: the cipher passages of the "paper in fragments" (catalogue 641)

Status: contributed by WAINUT (27 Oct 2026). Key recovered from the ciphertext alone; the text is read in part
(first-pass transcription, a dozen holes and doubtful words). The site page and the ledger rows are left to the
maintainer.

Catalogue 641. Contributed by WAINUT (https://github.com/WAINUTAI). The work was done with AI language-model agents;
the cipher was transcribed from the NARA frames with a vision-capable language model. An independent agent re-read
seven passages on the film, decrypted them with its own code and ran the controls. A second pass for this
contribution re-read three more groups, and a review re-read three more (C26, C38, C42).

## 1. The document

- **Source.** NARA RG 59, Despatches from US Ministers to Colombia, vol. 3 = microfilm T33 roll 3,
  [naId 189273979](https://catalog.archives.gov/id/189273979) (535 frames, "Apr. 14, 1823-May 1, 1826").
  Richard C. Anderson to John Quincy Adams, No. 7, Bogota, 19 Jan 1824, frames T33-03-0044 to -0047. The enclosure
  **No. 4**, "the paper (in fragments) and written partially in Cypher", is on frames
  [0055](https://catalog.archives.gov/medialz/dc-metro/rg-059/603720/T33/T33-03/T33-03-0055.jpg),
  [0056](https://catalog.archives.gov/medialz/dc-metro/rg-059/603720/T33/T33-03/T33-03-0056.jpg),
  [0057](https://catalog.archives.gov/medialz/dc-metro/rg-059/603720/T33/T33-03/T33-03-0057.jpg) and
  [0058](https://catalog.archives.gov/medialz/dc-metro/rg-059/603720/T33/T33-03/T33-03-0058.jpg).
  Frame 0057 right is headed "2o. duplicado / Al Sr. Ministro de Estado y Relacs. Exters. de Colombia", with the
  marginal "4". The text runs 0057 right, 0058 left, 0056 left, 0056 right, 0055 right. Frame 0057 left is a clear
  fragment, not transcribed here.
- **Contemporary translation.** Frames 0058 right to 0061 hold an English translation signed "W. B. H." of the
  clear parts only, with the cipher parts left blank.
- **Manning.** Manning, *Diplomatic Correspondence of the United States concerning the Independence of the
  Latin-American Nations* (1925), vol. 2, doc. 641, p. 1272. The despatch calls the item "a Duplicate of a letter
  written by Mr. Ravenga at Madrid, sent by him through France ... intercepted and opened by order of the Authorities
  there; he says that the letter of which this was a duplicate was sent through another channel and arrived in due
  time". Footnote: "Not printed. A postscript to Anderson's letter explains that no key to the cipher was furnished.
  The portions not in cipher are, alone, unintelligible." The catalogue adds that Count Landos, a French agent at
  Cartagena, handed it over in 1822.
- **Writers.** Manning names only "Mr. Ravenga". The letter says "nosotros" throughout, which fits the joint mission
  of José Rafael Revenga and José Tiburcio Echeverría in Madrid. The second name is our inference.
- **Addressee.** The Colombian Secretary of Foreign Affairs (Pedro Gual, per the catalogue).

## 2. The system and the key

The letter is in Spanish. Clear text alternates with 56 cipher groups written in ordinary lowercase letters, with no
spaces inside a group. The system is a **monoalphabetic substitution**:

- the cipher letter `a` stands for the space between words;
- the digraph `ll` is one sign and stands for plain s; `lll` is ll + l (s + t) in every case checked;
- `c` stands for plain ll (millones, millón, aquellas, vellón), because ll was taken;
- `ñ` stands for plain l.

The full table with counts is in `key.txt`. The main values (a, t, v, p, g, ll, m, e, z, b, y, l, ñ, d, o, n) rest on
dozens of occurrences. The rare values u = f, r = h, i = x and f = ñ rest on 3 to 6 occurrences each. Open: the
sign for plain z (the first pass reads g in Cádiz, pobreza, diez and forzoso), the sign for plain j (consejo,
aconsejó, ejecutivo), and whether a final z or k after a word is a stop.

**How the key was found.** No key was given and none was used. A quadgram hill-climb against Spanish statistics (a
Cervantes text) on the cipher groups, with `ll` merged into one symbol and cipher `a` removed, gave
"los dos grandes partidos republicano y realista constitucional" at once. That made `a` the space, and the rest of the
key followed. The solver script was not kept; `decrypt.py` applies the key.

## 3. The transcription

`transcription.txt` gives the 56 groups with the clear text that follows each one. It is a **first pass**. The hand
confuses g/y/q, n/ñ, e/c, p/t and b/ll, and the first pass drops letters here and there. That explains the
misspellings in the mechanical output (`decryption.txt`). Twelve groups were re-read on the film and corrected: seven
by the independent verifier (C01, C05, C06, C07, C42, C52, C53), three in the second pass (C39 nulidad, C40 por
España, the comma after republicanos in C10) and three in the review of this contribution (C26 Argüelles with c,
C38 a line break that had been typed as a space, C42 one l too many in Prusia). The list is at the head of the file.

- **The comma-like mark.** A mark that looks like x stands where a comma belongs, after "distinguido", "republicanos"
  and "España". It is written `,` in the transcription. True x (plain b) occurs in republicano, absoluta and obrar.
- **The writers' own spelling.** "virey", "La Torre" with one r, "Argüelles" with c for ll: these are kept apart from
  misreadings.
- 2,294 sign places in all (ll counted as one sign), counted with `decrypt.signs`: 335 are the word space `a`, 3 are
  the comma-like mark and 8 are unread places. There are 28 distinct signs: 26 letter signs with a value (k doubtful), one q
  without a value (C41), and the comma-like mark.
- **gg next to c.** Next to plain c the first pass often has gg where plain i stands: every -ción comes out as
  "-ciion", and there are "ciivil", "diice", "deciidirse" (about 15 places). This may be a second i-like sign, the
  open sign for z, or a habit of the first reading. It is not settled; the reading gives the word with one i.

## 4. The reading

The text as sentences is in `reading.md` (Spanish), with the deciphered parts in «guillemets», and in
`translation.md` (English). Slips of the first pass (a dropped, added or confused letter or two, where the word is
certain from the sense and the clear text) are corrected silently there; `decryption.txt` keeps the raw output. Anything
beyond that is marked `[?word]`, and what cannot be read is `[...]`.

What the letter says (five fragments):

1. **Spanish politics.** The two great parties, republican (exaltado) and constitutional royalist, are at odds; the
   republicans prepare a revolution "sangrienta y desastrosa" in Cádiz, Barcelona and on the coast. Riego's
   banishment, his later "puesto distinguido", the fall of the ministers, the Cortes' democratic measures, an
   anti-constitutional plot reported to the Cortes in secret session, and schisms in the secret society.
2. **The treasury.** The Treasury could raise only seven million reales de vellón in a week; nobody dares propose
   a new loan after the ten million duros that ruined Canga Argüelles; national bankruptcy is spoken of openly. Each
   party fears to back American independence. The Colombians try to unite the American deputies in the Cortes and,
   through an independent European deputy, to get a motion on extraordinary Cortes.
3. **The case for treating.** Fear that no one would recognise Colombia without Spain, and the view of French
   politicians and a "Madame Orloff" that Russia, Austria and Prussia had divided America among themselves, pushed
   someone towards accepting a proposal. The writers argue the opposite: the nullity of the Spanish government only
   strengthens Colombia's right, and the three powers are no real threat. They visit a man close to the ministry.
4. **Recognition and Mexico.** They hope the present Cortes will authorise the Executive to treat with them before
   they dissolve. Apodaca writes in public that there is nothing to fear, but privately that he will probably be "el
   último virey"; his wife, aunt of the Minister of Marine, says it is better to lose it single than double.
5. **Venezuela.** General La Torre (holding Puerto Cabello) asks for four thousand men and a million duros; the
   Council of State advises ships for troops; fifty thousand pesos a month are to go to him from Havana.

**Dating.** The first solver dated the letter to about September-November 1822. Two details point earlier: "acercándose
el día de San Fernando" (Ferdinand VII's saint's day, 30 May), and "antes de disolverse las presentes [Cortes]" (the
ordinary Cortes of 1822 closed at the end of June). Riego was President of the Cortes from March 1822, and La Torre
held Puerto Cabello until mid-1822. About May-June 1822 seems likelier. This is our inference; it was not checked
against the dated correspondence of the mission.

Context on frame 0055 right, read once from the frame at reduced size, not transcribed in full: before the last cipher
group the clear text describes an audience with the ministers, then visits to "el Capitán general de esta Provincia
Conde de Cartagena" (Pablo Morillo held that title; our identification) and to "el digno Arzobispo de Caracas".

## 5. Controls (`python decrypt.py --controls`)

Share of decrypted words (three letters or more) found in the repository's Spanish word list
(`lang/lexicons/es.json.gz`), over the 56 groups as transcribed:

- the key: **0.427** (on the first-pass transcription, misspellings included);
- 2,000 random permutations of the key: maximum 0.092, mean 0.003;
- 2,000 shuffles of the signs inside each group, with the true key: maximum 0.091, mean 0.040;
- the key rotated by one place, space kept: 0.042.

The independent verifier ran similar controls with its own code and word list (41.2 % against at most 10.2 % and
11.7 %).

## 6. Prior work

- Manning (1925) prints neither the cipher, nor the clear text, nor a decipherment (checked on the archive.org text
  of `diplomaticcorres02mann`).
- One web search with Spanish key phrases (with Revenga, Echeverría, Madame Orloff, La Torre, Apodaca) found no
  printed text.
- **Not checked:** Bogotá received the original by another channel and must have read it with its own key. The
  plain text may therefore be in the Archivo General de la Nación, Bogotá (Sección República), in the Archivo
  Santander, in Blanco and Azpurúa, or in Zubieta, *Apuntaciones sobre las primeras misiones diplomáticas de Colombia*
  (1924). We claim only the decipherment of this intercepted NARA copy, not that the content is new.

## Remaining gaps

- The transcription is a first pass: 44 of the 56 groups were read once, and about a dozen words in the reading are
  doubtful or open (an[...], cuartel, remoción, Andalucía, the end of C17, C18-C19, the King's action in C23, C36,
  C38, C43, C49, C50, the person addressed in C53, La Torre's verb in C54, C55-C56) - blocker: not-attempted. A full
  second pass on the four frames should settle most of them.
- The signs for plain z and plain j, and the role of a final z or k - blocker: too-short. Each rests on two to four
  occurrences.
- The clear fragment on 0057 left and the clear paragraphs of 0055 right and 0056 right are not transcribed -
  blocker: not-attempted.

## Escalation

- [x] siblings: no other letter in this cipher has been found; Revenga's other letters (AGN Bogotá, Archivo Santander)
  are not online
- [x] clear-pages: the clear text frames every group, and Hodgson's English translation (0058-0061) confirms the clear
  parts; it leaves the cipher blank
- [x] known-keys: no Colombian key of 1822 is known in the repository (no Revenga entry); not needed, the key was
  recovered
- [x] print: Manning vol. 2 checked; Zubieta and the Colombian collections not checked
- [x] key-rebuild: the key is complete for the common letters; z and j open
- [ ] retry: a full second transcription pass on frames 0055-0058

## Files

- `transcription.txt`: the 56 cipher groups with the clear text after each, frame by frame
- `decrypt.py`: the key, the decryption and the controls (standard library)
- `decryption.txt`: output of `python decrypt.py`, group by group
- `reading.md`: the text as Spanish sentences
- `translation.md`: English translation
- `key.txt`: the key with counts
