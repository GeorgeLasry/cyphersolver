# Chevalier Lagau to the comte de La Marck, intercepted cipher letters (Unsolved Catalogue no. 464)

Status: no write-up. Blocked on access: not digitised (Rigsarkivet, TKUA, "Opsnappede chifferbreve fra chevalier Lagau"; scans to order from Rigsarkivet).

Blocked on images: the series is not online and has to be ordered from Rigsarkivet (reading room or
scan-on-demand). Nothing below rests on a sight of the letters.

## The document

- Rigsarkivet, Tyske Kancelli, Udenrigske Afdeling, arkivserie "Opsnappede chifferbreve fra chevalier Lagau"
  (official name). References: Fremmed proveniens, Frankrig; Danske Kongers Historie, fasc. 358. Original, paper.
  Daisy: https://daisy.rigsarkivet.dk/arkivserie_detaljer?heid=3245448&henid=3245448 (soeg id he_3245448).
- Dating (dannelse): 12.04.1712 - 27.05.1712.
- Note, in full (translated): "According to a contemporary Danish endorsement, chevalier Lagau was French legation
  secretary in Stockholm, and the letters were addressed to the French ambassador in Stockholm, comte de La Marck."
- Number of letters, length and system: not given. The catalogue says "one unit".

## Access (checked 28 Oct 2026)

- soeg.rigsarkivet.dk search API, query "Lagau": one hit, he_3245448, `tilgængelighed: "Intet"` (nothing online;
  digitised series read "Alt"). The Daisy page has no image link. Not digitised.
- Not on DECODE (`research/scandinavia/decode_nordic.txt`, sweep of 26 Oct 2026).
- Searches for "La Marck" and "Danske Kongers Historie 358" on soeg give no other unit of this correspondence.

## The date

The archive dates the letters 12 Apr - 27 May 1712. The McCord Museum record (Lagau letter summaries, Oct-Dec 1719)
says Philippe de Lagau became secretary to La Marck in Stockholm in 1717 and wrote to Dubois and La Marck until he
went back to France in 1720. TNA SP 78/163/30 is La Marck at Stockholm, 7 Jan 1719. No source found puts La Marck
in Stockholm in 1712. So either the archive's 1712 is a slip (1719 or 1720 likely: the letters are *to* La Marck,
which fits Lagau writing after La Marck left Stockholm in 1719), or the Danish endorsement names the wrong people.
This can only be settled from the letters' own dates.

## Prior art

None found. `known.py` and the DECODE list gave no hit in the 26 Oct sweep. Web searches on 28 Oct 2026 (Lagau +
La Marck + Stockholm + chiffre/intercepted; La Marck 1712 postings) found only the McCord record, TNA SP 78/163
calendar entries (La Marck to Dubois, Jan 1719) and unrelated Gyllenborg 1717 interception material. No edition,
calendar or decipherment of the Copenhagen intercepts.

## Remaining gaps

- All the letters: needs-physical-access. Nothing can be transcribed, counted or attacked until the unit is
  scanned. The system is undetermined.

## Escalation

- Siblings: no other Lagau or La Marck unit at Rigsarkivet. French letters of 1719-20 deciphered elsewhere are the
  best chance of the same key: TNA SP 78/163 (La Marck to Dubois, Stockholm 1719, copies taken by the British) and
  the McCord Lagau summaries (Oct-Dec 1719). Check whether the SP 78 copies are decipherments and whether any
  cipher original survives beside them.
- Clear pages: unknown until imaged; a Danish decipherment or working may be filed with the intercepts.
- Known keys: none found for the French Stockholm legation 1717-20 on DECODE. The French foreign-ministry keys
  (AE, Mémoires et documents, chiffres) are the other place to look once the system is known.
- Print: the Lagau reports (McCord cites the Instituut voor Nederlandse Geschiedenis) and Recueil des instructions,
  Suède, may print the letters in clear; check once their dates are known.
- Next step: order scans of the unit from Rigsarkivet (scan-on-demand). Then transcribe, count signs, check the
  SP 78/163 copies for a matching clear text, and only then a ciphertext-only attack with a French 1700s model from
  `lang/`, with an enciphered control at the same length.

## DECODE

The item is not on DECODE and nothing was transcribed, so there is no queue entry yet. Add a new-record proposal
to `decode_updates/queue.json` once the scans are in.
