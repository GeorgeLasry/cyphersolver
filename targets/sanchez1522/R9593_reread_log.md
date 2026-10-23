# Re-reading log, R9593 (23 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch r2o)

## Starting point

Gap "not-attempted" (r2i): R9593 (RAH Salazar 9/23 ff. 27r-27v, Sánchez to Charles V) had been fetched and opened but
not read. Tomokiyo 2025 printed its first line only.

## 1. Is there a text already?

- DECODE R9593: two images (f. 27r on the right of P1, f. 27v on the left of P2), no attachment, transcription or
  comment block; "Inline Cleartext: No". Nothing interlinear or marginal. The only clear words are the null padding
  (*como*, *quien*) and the subscription *en venecia a v de março de dxxij* (f. 27v l. 19), which confirms DECODE's
  date of 5 March 1522.
- Print: **not calendared in CSP Spain 2** (Bergenroth 1866). Re-checked on british-history.ac.uk (vol. 2, pp. 386-519,
  every entry 380-515 listed with its date and shelfmark, r2o): Sánchez's March 1522 entries are 396 (15 March, to the
  Emperor, from a decipherment in the Gayangos papers) and 397 (15 March, to Gattinara, Salazar A. 23 ff. 76-78); nothing
  dated 5 March, nothing at A. 23 f. 27. 396's abstract (the Duke of Milan's lansquenets marching into Italy and taking
  the Chiusa; Andrea Gritti) is the same business ten days later and agrees with this letter's subject.
- No neighbouring record carries a decipherment (r2i opened all 163 images of R9593-R9657).

## 2. Reading on the image

Crops: each line at 2.0-3.5x (`r2o/R9593/z*`, `k*`, `q*`, `v*`) and blocks of six lines at 1.75-1.9x (`P*`, `B*`), all in
the scratchpad (`reread/r2o/R9593`). Transcription with the line's reading under it: `R9593_signs.txt` (33 + 20 lines).

Sign values: those of R9653 (`R9653_cipher.txt`) and R9605's calibration, read per word. Held at every occurrence here:
`n` a, `ꝗ` r (looped), `#` o, `&` n, `h`/`4`/`∂` e, `ai` i, `z` c, `3`/`oo` d, `P` f, `∞` g (bold), `A` z, `U` u/v, `g` y,
`ϙ` l (*Valcamonica*, *bolbian*, *oficial*, *pregunteles*), `ꝑ` m (*Valcamonica*, *Geronimo*, *mensagero*, *Monza*).
Look-alikes resolved by sense (counted below): `ǂ` o against `ꝑ` m (*ahora*, *cinco o*, *testimonio*); `Lo`/`q` s or t;
the `ꝫ` group read a, but s in *acostunbra* and c in *apercibidos*.

Code values beyond the published key:
- **`gim` = *suyos*** (Tomokiyo "suquos?"): adopted. R9635's contemporary decipherment (f. 22r *todos los suyos que por
  agora yrian a servir en Francia*) and here four times, each fitting: *con suyos los quales … en Monza*, *pregunteles de
  la [?quantidad] de los suyos*, *el [nog] de los dichos suyos*, *no son mas de … mil los dichos suyos*.
- **`fef` = *toda***: adopted. *fef* + `dod`(vi) + a = *todavia* (f. 27v l. 2) as in R9653 f. 299v (*fef* + v-i-a), and
  *fef*+s *vum*+s *mug*+s = *todas estas …* (f. 27v l. 5). Slot: between `faf` todo and `fug` tres?.
- **`ril` = *lansquenetes*?**: sense and alphabetical slot only (between `rug` la and `pac` lo), five occurrences, all
  in *el passe de los ril*, *conduzir a los dichos ril*, *donde havian passado los ril*, *que los ril podian passar
  seguramente*, *a los ril de vuestra magestad*; CSP 396 (15 March) has the lansquenets on the march. Entered in
  `key_codes.tsv` with the flag.
- Proposed, not entered (one context each): `lif` (*a [lif]r lo y obviar el passe*: *proveer*?, slot between `lod`
  principal and `lof`), `nog` (*saber el [nog] de los dichos suyos*: *numero*?, after `nuf` no), `tem` (*la [tem]* after
  *Caravagio*: slot between `taf` falta? and `tom` francia), `rid` (*estava mal [?informado]*, between `rec` Inglaterra
  and `rof` justa?; read as [?informado] in the reading).
- Not fitting the published key here: `mug` (*palabla?*) in *todas estas [mug]s*, *los [mug]s*; `do` (venecia) in
  *que es [do] no*; `paf` (menda) read *mendado* once in *hayan mendado* (= *mandado*, as Tomokiyo's R9623 *menda-do*).
- Open: `xe`, `no`, `vub`, `lud`, `fug` (*tres?* does not fit), `la` (twice), `ni`, `fu`, `sag`, `nif`, `ram`, `tag`,
  `zom`, `fag`, `pil`, `dug`, `nad`, `ca`, `ce`.

Persons and places read from the spelled runs: Geronimo Adorno (twice), Andrea Griti (three times: the Venetian
provveditore), Valcamonica, Caravagio, Monza.

Failures: f. 27r ll. 26-33 (after *dixeronme como yo …*) and f. 27v ll. 11-13 do not build sentences: open groups and
uncertain runs follow each other; they are carried in the reading as holes.

## 3. Alignment and score

Each reading line aligned word by word with its sign line in `R9593_signs.txt`; words supplied by sense are bracketed
(`[e]` in *dix[e]ra*, `[n]` in *havia[n]*), code values by slot only carry `[?…]`.

`v2_score.py R9593_reading.md es`: explicit holes **0.614** (27/44), plain 0.136; hole rate 0.13, 506 words.
Look-alike letters: about 26 of about 1,050 letters (2.5%, estimated by count on the reading).

**Kept decoded, not read.** The explicit-hole share sits at the bar, but the hole rate (0.13) is above one in ten and
the reader's test fails for the second half of f. 27r and three lines of f. 27v; the opening paragraph, the Signoria
audience on the lansquenets' passage of Val Camonica and the news of the French taking Caravaggio hold. Blocker for
the rest: no-key-material (about twenty code groups absent from the published key, mostly met once) — the escalation
that would close it is a decipherment of a sibling letter that uses them, or the court decipherment of this letter if
one survives with the Gayangos or Salazar papers.
