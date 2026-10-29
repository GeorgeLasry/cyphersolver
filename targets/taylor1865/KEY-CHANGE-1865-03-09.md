# Dated evidence for the local keyword change

**9 March 1865: instructions to Wirt Adams and D. W. Adams specify COME
RETRIBUTION for cipher dispatches “after this date.” The orders themselves
are encrypted using COMPLETE VICTORY.**

Both are copied on manuscript p. 105, NARA RG 109 ch. II vol. 196,
frame 0055. The Wirt Adams telegram is addressed to Jackson, Mississippi;
the D. W. Adams telegram to Montevallo or Selma, Alabama. Both are signed
by W. F. Bullock Jr., AAG, “By order,” from Meridian, 9 March 1865.
The date, addresses, text and signatures were checked on the image.

Each complete telegram reads:

> In sending cipher dispatches after this date use the following key word,
> “Come Retribution.” Acknowledge receipt.

## Cipher evidence

The plaintext sequence (clear words omitted) is:

`CIPHER DISPATCHES FOLLOWING KEY WORD COME RETRIBUTION`

With A=0, ordinary Vigenere under COMPLETEVICTORY, the expected cipher is:

`EWBWPV WMNXCMQYCU TAAWSPMIO MXM NMTR ODXI KIOZKUIKGQB`

Each working manuscript transcription has one N/M ambiguity at MXM, retained
as NXM rather than silently corrected. The other 46 of 47 letters agree
directly. The Wirt copy divides DISPATCHES across a line as WMN/XCMQYCU;
the D. W. copy divides FOLLOWING as TAA/WSPMIO. Neither changes key progression.
The Wirt copy has the complete plaintext pencilled above the cipher words,
including COME RETRIBUTION. The pencil hand's date and identity are unknown.

The COMPLETE VICTORY key thus carries the new keyword in the ordinary way:
the old key protects the instruction introducing its replacement. This
interpretation rests on the complete deciphered sentence and its explicit
"after this date," not just on a change in statistical key fit.

## What this establishes, and what it leaves open

- Establishes that Taylor's headquarters issued this instruction to these two
  recipients on 9 March 1865.
- Establishes that COMPLETE VICTORY encrypted the two instructional messages.
- Supplies two more fully covered telegrams and an existing adjacent
  decipherment in the sibling series.
- Does not establish receipt/implementation time, or the first use of COME
  RETRIBUTION elsewhere in the department or Confederate government.
- Does not overturn the 9 January selective reversion to THE NAVY OUR PRIDE.
- A partial image check of 8 March Taylor–Brent traffic (vol.196 fr.0052
  p.99) supports COME RETRIBUTION before the Adams orders: the opening gives
  ENEMY AT LEAST TWENTY THOUSAND (24/26 candidate letters direct), and the
  final passage gives MOVING FROM NORTH at offset 4. Its middle remains
  untranscribed, so no full reading is claimed. See `v196-0052_partial.txt`.

## Sources and reproducibility

- [NARA catalogue](https://catalog.archives.gov/id/45485022).
- [Exact frame image](https://catalog.archives.gov/medialive/22/4850/45485022/content/dc-metro/rg-109/596501-confederate-record-books/chapter-02-volume-196/chapter-2-volume-196-0055.jpg).
- Full diplomatic working transcriptions: `v196-0055-wirt_transcription.txt`
  and `v196-0055-dw_transcription.txt`.
- Coherent readings: `v196-0055-wirt_reading.md` and `v196-0055-dw_reading.md`.
- Reproduce word-by-word decryption: `python3 continue_analysis.py`.
  The generated `continuation_alignment.tsv` distinguishes glyph candidates
  from re-enciphered reconstructions.

Bounded prior-print check: normalized OR I/49/1 and I/49/2 OCR did not match
“retribution,” “after this date use,” “key-word,” or “keyword.” No assertion
that the orders were never published elsewhere is warranted. The interlinear
pencil already constitutes an existing decipherment regardless of print.
