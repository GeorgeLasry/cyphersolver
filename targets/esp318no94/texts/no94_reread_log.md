# Re-reading log, Espagnol 318 no. 94 (23 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch b27)

## Starting point

Reading audit (22 Oct): "decoded, not read". The repository held only Brackx's sign transcription
(`ct94_brackx.txt`); his decipherment and normalized reading were only in GitHub issue #62; about 90 code groups
(154 of 623 code-group tokens) are unread.

## 1. Is there a text already? The key?

* No decipherment of no. 94 in the volume (all thirteen cipher folios of Espagnol 318 opened in Sept/Oct), in print
  (Parisi 2004/2020, Galende Díaz 1994, Tomokiyo, Quirantes 2018) or on DECODE (no record). No clear copy.
* Brackx's decipherment copied into the folder: `no94_decryption.md` (his C:/P: interlinear, verbatim) and
  `no94_partial_reading.md` (his v3 reading converted to this project's hole notation, nothing added).
* **The key: Bergenroth's Gran cifra list is reachable after all.** The NOTES of esp318no93/esp318no94 say BNE MSS
  20.211/52 is not online; but Arturo Quirantes published a photocopy of the sheet itself ("Cifra de las cartas del
  Gran Capitan", 20.211/52) and his own transcription of it on his blog on 2 and 5 Feb 2018 (the pages were already
  saved in `targets/esp318/lit/quirantes*.html`; the full-size images Clave-Gran-Capitan-1.jpg and -2.jpg fetched into
  the scratchpad). About 75 code groups with meanings read off them: `bergenroth_gran_cifra_codes.tsv`.
* **Test** (`research/reading_audit/b27_esp94_berg.py`, minim letters folded n = u = v, y = q): of the 12 firm
  readings of no. 94 that have a Bergenroth counterpart, **one agrees** (`mny`/`muy` = de) and **eleven differ**
  (que `qa` x65 against `raz`/`vaz`; se `qag` x32 against `pix`; en `mys` against `nym`/`sip`/`vok`; la `mnb`
  against `uob`/`pix`; no `pif` against `quem`; los `nae` against `peluo`/`val`, and Bergenroth's `vae` is papa; lo
  `nyb` against `pux`; como `lux` against `mad`; por `pat` against `nav`/`rau`; su `gik` against `som`; gente `mnh`
  against `puc`). Brackx's firm readings rest on 10-65 contexts each, so the code of no. 94 is **not** Bergenroth's
  Gran cifra; it shares its group shapes and one group. The holding archive's own key for it, if any, would be the
  "Cifra del visorrey" (BRAH 9/15 ff. 1-6), not digitised.
* Spellings of open no. 94 groups that are Bergenroth groups, with his meaning: `nnl` x3 = nul era ("públicamente
  [nnl] dicho" would give "era dicho"), `li` x2 = aun ("y en ellos [li] que ... los otros mostraron" would give
  "aunque"), `nym` x3 = en, `luy` x3 = luq capitán, `nen` = ven para, `nol` = uol es. **Not adopted**: the code is
  shown to be a different one, so a shared spelling proves nothing; flagged here as sense-only candidates for review.

## 2-3. Reading and alignment

No re-transcription against the scans this session: the reading's holes are the code. Brackx's v3 marks 169
stretches "…"; the unread code-group tokens alone are 154 (his count), so nearly every hole is a code group with no
key, one or two per sentence. No word supplied; firm code readings given plain, tentative ones `[?word]`. Look-alike
alternates: none adopted here (no glyph re-read); Brackx's own uncertain classes (sign K l/s; a third of the
ß/thorn/B glyphs unchecked) are listed in NOTES.

## 4. Score

`b17_score.py`, LANG_=es, reading body: 0.157 (13/83); explicit holes 0.253 (21/83). Before: 0.00 (no text in the
folder). Far below the bar: **decoded, not read**. Stays open for want of key material, not for want of a text.

One sentence: "DONDE ESTAVAN MUY BIEN TRATADOS ASTA VER LO QUE DELLOS Y DE LOS OTROS SE ENVIARE MANDAR, QUIERE V.
AL." (clear text: where they were very well treated until it is seen what Your Highness wishes to order about them
and the others).
