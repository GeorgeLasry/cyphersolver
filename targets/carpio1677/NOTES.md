# Carpio (Rome) to Fuenmayor (Copenhagen), 1677 — DECODE R1002–R1011

Status: read (22 Oct 2026: margins transcribed, all ten letters read and translated; write-up updated the same day:
docs/carpio1677.html, README row, SOLVED_CATALOGUE/RANKING, DECODE queue with the ten readings and texts/key_decode.json)

22 Oct 2026, later: **all ten letters read.** The contemporary margin decipherments of R1002, R1003 and R1006-R1011
were transcribed from the images and aligned word by word with the key decode. Each letter is now normalised Spanish
(`read/R*_reading.md`, holes marked) with an English translation (`read/R*_en.md`; R1004/R1005 translated too).
3,504 of 3,504 tokens are in letters that read; the holes are a handful of words (see Remaining gaps). New code
words from the margins: cen = Duque, ren / xen = gobierno, xin = gente, cun = España (cun iles = españoles),
tin = Francia (franceses), gen = enemigos, {110} = cuando; struck 14 = ju (ajuste, justicia, justamente); pa + struck
55 = Papa. The earlier block below is kept as the record of the audit.

22 Oct 2026, reading audit (George Lasry's test: can sentences be built and translated?): **read in part**.
R1004 and R1005 read (normalised Spanish, confirmed by their faint margins). **The other eight letters are decoded,
not read** here: `read/R*.raw.txt` are syllable streams with stray letters and DECODE slips, and their contemporary
margin decipherments, which are the readings, have not been transcribed. 425 of 3,504 tokens (12.1%) are in letters
that read. "Status: read" and 96.1% are withdrawn as reading claims (96.1% is tokens with a value).

Ten ciphered despatches of Gaspar Méndez de Haro, 7th Marqués del Carpio, Spanish ambassador in Rome, to Baltasar de
Fuenmayor, Spanish envoy in Denmark, 4 Sept – 11 Dec 1677. Archives générales du Royaume, Brussels, Secrétairerie
d'État et de Guerre, inv. nr. 2559. Images and DECODE's ciphertext transcriptions: DECODE R1002–R1011, fetched
19 Sept 2026 with the cookie in `targets/bordeaux/decode/cookie.txt` (images in `img/`, git-ignored).

**Result.** The key was reconstructed from the letters themselves and reads all ten. DECODE lists R1004 (13 Nov) and
R1005 (20 Nov) as "non-decrypted". Both read in full with the key. Both leaves also carry a faint contemporary
decipherment in the left margin that DECODE's transcriber missed, and the key reading agrees with it. The other eight
letters have the decipherment written in the margin. The key reproduces each one, so the margins can be checked and
their illegible words recovered.

## The key

This is a syllabic nomenclator. Every token is separated by a point. There are four kinds of token:

1. **Plain numbers 9–30: single letters.**
   a 9, b 10, c 11, d 12, e 13, f 14, g 15, h 16, i 17, l 18, m 19, n 20, o 21, p 22, q 23, r 24, s 25, t 26, u 27,
   x 28, y 29, z 30.
   In practice these mostly spell closing consonants: n 20, r 24 and s 25 are the three commonest tokens.
2. **Plain numbers 31–60: consonant + vowel syllables, in rows of five (a e i o u).**
   m 31–35, n 36–40, p 41–45, r 46–50, s 51–55, t 56–60.
   Examples: 33 mi, 36 na (also ña), 39 no, 41 pa, 44 po, 48 ri, 51 sa, 52 se.
3. **Struck-through numbers: a second syllable table** (DECODE marks the stroke with "+").
   - t row 15–19 (ta te ti to tu)
   - f row 20–24 (fa … fu)
   - vowel + l 30–34 (al el il ol ul)
   - vowel + s 35–39 (as es is os us)
   - vowel + n 40–44 (an en in on un)
   - vowel + r 45–49
   - que 50, qua 51, qui 52
   - 14 is ju ("[14]sta mente" justamente, "[14]ticia" justicia, "a[14]ste" ajuste; confirmed by the margins).

   Struck N, R, g and 4 are nulls. They sit mainly at the start and end of each cipher block.
4. **Letter pairs: syllables with the consonant disguised, vowel kept.** Cipher → plain:
   b→c, c→b/v, g→d, l→g, m→l, d→m.
   So ge = de, gi = di, go = do, ma = la, mo = lo, me = le, bo = co, bi = ci, ca = va/ba, ci = vi, la = ga, lu = gu,
   lo = go.
   Special cases: ag = ha, eg = he, e (a separate sign) = lle.
   116 = V.S. (Vuestra Señoría). 8 is used for o.
5. **Three-letter words (code names), read from context:**

   | code | meaning |
   |---|---|
   | sen | el Rey |
   | gin / jin / jen | S.M. / el Rey |
   | gus / mus | Príncipe (de Orange) |
   | quol | Inglaterra |
   | ana | Nápoles |
   | ten / den | Francia |
   | pon | armada |
   | san | Bruselas |
   | tan | Flandes (?) |
   | gon | señor(es) |
   | ran / xan | gobernador |
   | xon | guerra |
   | cun / cun iles | España / españoles (margin, R1011) |
   | cen | Duque (de Lorena, R1003) |
   | ren / xen | gobierno (R1007, R1008) |
   | xin | gente (R1011) |
   | tin | Francia, franceses (R1011) |
   | gen | enemigos (R1009) |
   | lun | cart(as) |
   | men / Jen (R1010) | Reino |

   R1010's "gus de s ra n ge s" is Príncipe de Orange, spelled out.

Scripts: `parse.py` reads DECODE's transcription files and `dec.py <record>` prints a reading. The raw machine
readings are in `read/R*.raw.txt`. They inherit DECODE's transcription slips: a few misread numbers show up as
`{..}` or as nonsense syllables.

## The two letters DECODE lists as unread

**R1004, Rome, 13 Nov 1677** (normalised, reading confirmed by the faint marginal decipherment):

> … [y al mesmo tiempo devo] lamentarme con V.S. de lo que en todas partes nos persigue nuestra mala fortuna, pues
> con la llegada del Cardenal de Estrées a Turín se teme alguna gran novedad en Italia; y las cosas de [Flandes] se
> hallan en el estado que V.S. sabe. Si bien en las materias del Congreso parece debemos suspender el juicio hasta ver
> lo que resulte del abocamiento del Príncipe de Orange con el Rey de Inglaterra. En los embarazos de esta corte no se
> me ofrece qué añadir a lo que diré a V.S. en mis antecedentes, sino que, si bien aguardaba este correo las órdenes
> de S.M., no las he recibido; pero no dudo las traerá el siguiente, pues de Madrid me avisan que habían llegado allá
> las cartas en que di los primeros avisos sobre estas dependencias.

**R1005, Rome, 20 Nov 1677:**

> … más de que nos tienen con gran cuidado las apariencias y evidentes señales de que la próxima campaña habrá
> guerra en Milán, pues el Cardenal de Estrées, que está en Turín, no se descuida.

## What the ten letters say (in date order)

- **R1010, 4 Sept.** The French fleet (la armada de Francia) has left Messina. It was rumoured to be bound for
  Brindisi, but its design is Catania. Carpio is dismayed by news from Brussels that the Prince of Orange raised the
  siege of Charleroi "intempestivamente".
- **R1011, 18 Sept.** Rome's reaction to Charleroi. Rumours that Spaniards were raising men by force for Sicily set
  the populace against them; Spaniards have been insulted and stoned in the streets for over fifteen days. Carpio has
  had no satisfaction from the Pope or his ministers. Militia cavalry was brought in, and more guns were mounted
  ("encabalgado … más piezas") on Castel Sant'Angelo. He contrasts the tolerance shown to the French, whose galleys
  at Civitavecchia pressed more than a hundred men, reapers included.
- **R1009, 25 Sept.** The false rumours spread against the Spaniards. Carpio pressed the Pope for remedy and got
  neither remedy nor an inquiry. He has referred the matter to the viceroy of Naples and the governor of Milan.
- **R1006, 2 Oct.** The offences to the Spanish nation continue. He has asked the governor of Milan and the cardinals
  of the Spanish party for advice. The French fleet and galleys kept station off Catania and turned back towards
  [?Toulon] and [?Hyères], the galleys much battered.
- **R1007, 9 Oct.** Still no satisfaction. He stays away from papal audiences on the cardinals' advice, awaiting the
  viceroy of Naples' answer.
- **R1008, 16 Oct.** No news at this court. He stands firm and awaits orders on how to proceed.
- **R1004, 13 Nov** and **R1005, 20 Nov.** Above.
- **R1002, 4 Dec.** In the matter of the pending disputes he asked for an audience of Innocent XI on the King's
  orders. The Pope refused it twice and would receive business "del Rey" only through a cardinal. Carpio declines to
  treat the principal business until the point is settled.
- **R1003, 11 Dec.** The loss of Freiburg ("el sitio de Fri[bur]go", taken by Créqui on 16 Nov 1677): its
  consequences may change the plan of the winter quarters, the Duke of Lorraine having to recross the Rhine; Flanders is left in a miserable state. He recalls the two refusals
  of audience already reported, has not asked again, and is awaiting the advice of the Marqués de los Vélez (viceroy
  of Naples).

These summaries were first made from the machine readings and corrected on 22 Oct 2026 against the margins (R1010
"temer el logro", R1011 stonings and Civitavecchia, R1006 Toulon/Hyères, R1003 audiences recalled). The full readings, aligned with the margins, are in
`read/R*_reading.md`, with English in `read/R*_en.md`.

## Verification 5, 23 Oct 2026

Plain-bar check (Spanish 1677): `read/R1006_reading.md` had no `## Reading` heading, so the sweep scored its header and
notes too (plain 0.529). Heading added; the body scores plain 0.778, explicit 0.889 (the two uncertain place names at
the end). Keeps read. (The reading's header says its spelling was modernised; not changed here.)

## 23 Oct 2026: R1006 spelling restored (sr)

`read/R1006_reading.md` was the one reading still in modernised spelling. The writer's spelling restored word by word
from the margin decipherment (`read/R1006_margin.txt`: agrauios, recivido, nacion, aora, satisfacion, governador,
Milan, ultima resolucion, despues, haverse, algun, bolvio, buelta), accents taken off; words the margin lacks (de
nuestro partido, y galeras) spelt as the key decode gives them. No word changed, holes kept; the second place name is
given as the margin and the decode spell it, [?Vieres] (Hyères in the English). Rescored with
`research/reading_audit/v2_score.py`: plain 0.778 -> 0.556 (the modern word list does not know 1677 spelling), explicit
holes 0.889 unchanged, hole rate 0.03. The sentences hold; keeps read on the explicit-hole share (REREAD_BRIEF rule 4).

**23 Oct 2026, v6 spelling check (research/reading_audit/v6_spelling_files.txt; REREAD_BRIEF step 3-4: no modern spelling in a reading)**: read/R1002, R1003, R1007-R1011_reading.md said 'Spelling modernised'. Each was put back into the writer's spelling word by word from its margin transcription (read/R*_margin.txt; research/reading_audit/v6_align.py): haviendo, deve, aora, executar, quando, assi, provada, Napoles, editorial accents off; words the margin abbreviates or does not carry are written out or spelt as the key decode gives them, without accents. Holes and brackets kept, no word changed; headers say what the spelling follows. R1006 was left to the agent working on it. Explicit-hole shares unchanged (0.909-1.0); all keep read. Modern spelling stays in the _en.md files.

## Remaining gaps
- R1006 last sentence: two place names, code "rin" and spelled "vi ve re s", read [?Tolon] and [?Vieres] (= Hyères) - blocker: illegible (the margin is unreadable there on the DECODE scan; a better image of AGR SEG inv. 2559 would settle it)
- R1002 one misread group after "que Dios guarde" ({7}); R1003 one verb not written in cipher or margin - blocker: illegible (DECODE slip; margin runs on without it)
- key: struck 55 and a few struck numbers ([25], [80]) not fixed in the table - blocker: no-key-material (each read from context in its letter)

## Escalation

- [x] siblings: the ten letters of the series share one key; R1004 and R1005 normalised and read
- [x] clear-pages: the margin decipherments of R1002, R1003, R1006-R1011 transcribed from the images (22 Oct 2026; DECODE's partial margin transcriptions in decode/ checked against them) and aligned with the key decode
- [x] known-keys: the syllabic nomenclator rebuilt here applies to all ten letters
- [x] print: searched 22 Oct 2026 for a printed edition of Carpio's 1677 Rome letters to Baltasar de Fuenmayor (Spanish, English queries): none found. Carpio's Roman embassy (1677-83) is studied for his art collecting; a UNED study of Spain-Denmark diplomatic agents 1640-1680 (portalcientifico.uned.es) turned up but could not be opened, so whether it quotes these letters is unchecked
- [x] key-rebuild: done (NOTES "The key")
- [x] retry: each margined letter normalised against its margin and translated (read/R*_reading.md, read/R*_en.md)
