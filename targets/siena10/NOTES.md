# Siena no. 10 — "presura di Montepulciano" (DECODE R4799)

Status: read — deciphered at the time: a second hand wrote the decipherment letter by letter over the single cipher run ("presura di Montepulciano"); transcribed and aligned sign by sign here, 18 Oct 2026.

Archivio di Stato di Siena, Concistoro 2308, fasc. 2 ("Lettere in cifra"), no. 10; DECODE
[R4799](https://de-crypt.org/decrypt-web/RecordsView/4799) (Concistoro_2308_53), catalogued "1500-1599", status N/A,
DECODE flag inline_plaintext = True. A key of its own: nothing ties its 19 sign kinds to any other piece of the file.

## Source and prior record

- George Lasry, "The cipher documents of Concistoro 2308, fasc. 2" (report to Daniel Bourdeau, 17 Oct 2026), contents
  list, section H: "No. 10 = R4799 — c. 25 symbols ('pressura di Montepulciano') — interlinear plaintext". The report
  has no section on the piece (`lasry_report.md` quotes the line).
- The siena1421 survey (24 Sept 2026): "One cipher run glossed letter by letter 'presura di Montepulciano'. Read at the
  time." The DECODE queue entry for R4799 (under siena1421) proposed "Decrypted".

## The slip and the transcription

One image (`IMG_R4799_I27942_P.jpg`, 4000x2248, from the DECODE photographs; ASSi, git-ignored). A narrow slip, four
lines of Italian cursive, no address, date or signature; pencil "10" at the foot right. Line 1: "Et riuscendo o no la"
+ 25 cipher signs + "in ogni modo"; the decipherment is written above the signs in a smaller, separate hand.
`transcripts/no10.txt` (18 Oct 2026, from the photograph at 2x and 4x) gives each sign with the letter written over it.

- 25 cipher signs, 22 glossed with a letter, 3 without (a sign under a phi-like mark between *presur* and *a*; the
  *m* after *mon*; the final *q*).
- The gloss gives 16 sign values, consistent at every repeat: S=p, 3=r, 7=e, 8=s, 1=u, y=a, R=a, +=d, 9=i, e=m,
  oo=o, g=o, L=n, b=t, 5-shaped g=l, arch-over-dot=c. Homophones: a (y, R), o (oo, g).
- The three unglossed signs are read as nulls (grade I: the glosser gave them no letter).
- The reading: **presura di Montepulciano**, "the taking of Montepulciano". George Lasry's contents line has
  "pressura"; the gloss has one s (p r e s u r [mark] a).

"Et riuscendo o no la presura di Montepulciano, in ogni modo ragunato che sarà ..." ("And whether or not the taking of
Montepulciano succeeds, in any case, once ... is gathered ..."). The clear lines 2-4 are only partly transcribed
(context, not cipher).

## Method

Read from existing decipherment: the contemporary gloss is a complete decipherment of the only cipher run; the work
here was transcribing the signs and checking the gloss against them (every repeated sign carries the same letter). No
key was applied or recovered beyond the 16 values the gloss shows.

## Disagreements

- "pressura" (report contents) against "presura" (the gloss, and the siena1421 notes). The gloss is followed.
- DECODE: "1500-1599" is a placeholder; status N/A although the decipherment is on the image.

## Date

Not established. Montepulciano was fought over by Siena and Florence repeatedly (Florentine from 1390; it went over to
Siena in 1495 and back to Florence in 1511); nothing on the slip fixes which campaign it means. Left undated.

## Verification 3, 23 Oct 2026

The v3 sweep flagged no. 10 at 0.567, scoring `transcripts/no10.txt`, the sign table with its tentative clear lines.
The cipher run is three words, *presura di Montepulciano*, every letter given by the contemporary gloss; written out in
its clear sentence as `transcripts/no10_reading.md`, it scores **1.0 on explicit holes**. Kept read.

