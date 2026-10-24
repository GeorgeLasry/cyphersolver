# Juan Gara de Senisteros to Juan de la Peña, Alcalá 23 Dec 1605 (NA 3.01.14 inv. 2442)

Status: read (key recovered from ciphertext-only, ~97% of cipher words read, 23 Oct 2026)

## Source

- Nationaal Archief, The Hague, 3.01.14 (Johan van Oldenbarnevelt), inv. 2442: "Missive van Don Juan Gara de
  Senisteros aan Juan de la Pena van 23 december 1605; afschrift (begin 17e eeuw)". 11 scans online through IIIF
  (`inv2442.json` lists them; `img/` and `crops/` are git-ignored). Folios numbered 54-57+ in the volume.
- A Spanish letter, apparently intercepted and copied for Oldenbarnevelt. Clear Spanish text mixed with long
  enciphered passages. No interlinear or marginal decipherment is visible.
- Found by the Nationaal Archief sweep (`research/nationaal_archief/`, lead 13).

## Prior work

- Not in Haak & Veenendaal, *Bescheiden betreffende Johan van Oldenbarnevelt* (RGP 1934-67): the online OCR
  (resources.huygens.knaw.nl/retroboeken/oldenbarnevelt) has no hit for Senisteros, Gara or Alcala (23 Oct 2026).
- No web hit for the names with 1605/cifra. Not on DECODE (the Dutch-held DECODE list has no 3.01.14 record).

## The cipher

Consonants are left in clear and the vowels are replaced, mostly by digits: 4=a, 8=e, 3=i/y, 7=o, 2=u, read off
p01 ("l4s m3sm4s p4l4br4s qu8 s7n p4rt3c2l4r8s" = las mismas palabras que son particulares). Also 5 = s, 6 = b/v,
and a looped sign (`{G}` in the transcription) = l (lo, los), h once. Word division is kept; a few clear
glosses are written above cipher words. No nomenclator.

## Side lead

The Oldenbarnevelt edition notes other cipher letters with unsolved passages, e.g. vol. 1 p. 377 ("the key to the
solution of the cipher in this letter is missing") and p. 397 ("this cipher is not solved"). Worth a later look.

## Files

- `transcription_A.txt`: literal transcription of pp. 1-4L (subagent), legend at the end.
- `decoded_A.txt`: the key applied by script to those lines.
- `reading_B.md`: pp. 4R-11 read directly with the key, cipher passages in braces.

## What the letter says

A long private report from Juan Gara de Senisteros, now rector of a college at Alcalá and newly a canon, to his
patron Juan de la Peña. The cipher hides the parts he wanted kept secret:
- the provision of the see of Sigüenza (to Fr. Mateo de Burgos) and of Pamplona (to Antonio Venegas), and the
  rumour that money changed hands;
- how he got his canonry and rectorship: he **forged de la Peña's signature** on a blank sheet and had a servant
  write a letter "from" him to the Cardinal of Toledo, and another to the abbot, to win the electors;
- the regent's resignation of his canonry, the Lerma collegiate church, money trouble with the student Chaves
  (the manteo and forty reales);
- on p10R, a limpieza-de-sangre matter: the Inquisitor Salcedo's grandmother was said to be the daughter of a
  cleric and a married woman whose husband, a smith, was reputed a converso; he asks before acting on it.

## Measurement

Cipher words: 454 on pp. 1-4L (decoded_A.txt), 993 on pp. 4R-10R (inside braces in reading_B.md); words left
uncertain: 14 and 32. About 97% read. Counted by script on 23 Oct 2026.

## Remaining gaps

- About 46 words marked `[?]` or `(?)`, scattered, mostly where the copyist's hand is cramped (p04R ll. 5-6,
  p07L superscript, p10R last lines).
- pp. 4R-11 were read directly; there is no glyph-level transcription of them.

## Escalation

- Key: complete, nothing to rebuild. The gaps are reading gaps, not key gaps.
- Retry: the uncertain words can be re-read at full IIIF resolution (`img/` has the max-size spreads);
  not yet done for every `[?]`.
- Siblings: none known; the volume (3.01.14) may hold other Peña correspondence worth a look.
