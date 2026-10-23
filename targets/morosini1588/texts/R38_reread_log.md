# Re-reading log, R38 (22 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch b00 helper)

## Starting point

Reading audit (22 Oct): "decoded, not read". `R38_decryption.txt` was the weakest of the series (0.311 clean share): the
DECODE transcription D1702 (RebAn, Feb 2017, 110 minutes for six dense pages) drops and misreads figures often and puts a
nomenclator dot on about one group in three where no code is meant. The word decode (`R38_worddecode.txt`) was garbled
in most lines.

## 1. Is there a text already?

- DECODE "cleartext" image D1062 (contact sheet): a clear letter page, not a decipherment. No glosses on 282r–284v.
- Rome's decipherments (Francia 27) not imaged; Tempesti was not searched for this letter.

## 2. Work done

- Every line re-parsed by hand from the transcribed figures (`R38_corrections.tsv`, about 80 entries), with the
  segmentation helper for the hard runs. Most garbles were spurious dots (143, 252, 352, 142, 126, 147 used as letters)
  and words the decoder could not see: "lo[n]gam.", "in diligenza S. Alteza", "procurase prima l'istirpatione deli
  heretici", "si sforzarà", "lo sforzarà", "se N. S. fose nel suo loco", "esercitano il Caluinisimo", "la [c]ontinoua
  uigilanza", "la pace in Italia", "nel marchesato di Saluzo", "abraciarla", "carisimi", "il parlamento di Renes contra
  l'indulto del sig. cardinale Lenoncort", "dala M.tà", "del Delfinato", "a le spale et in fronte".
- Image check: 282r ll. 1–7 only (half-width crops). The ink shows through from the verso and the figures are small;
  a full re-transcription from the images was not done in this pass.
- 284r–284v: DECODE's transcriber notes that crossed-out figures were not transcribed; the last lines of 284v are only
  partly carried.

## Result

Before: 0.311 clean-sentence share (`R38_decryption.txt`). After: 0.712 (1,310 words) on the "## Reading" body. By hand: about 20 unread stretches ([…])
and 15 partly carried words in about 1,600 words; the argument of every paragraph is carried, but several sentences have
a hole. Grade B (many single-figure corrections from context; most lines not checked on the image).

## Still open, and why

- The holes listed under "Notes on the figures" in `R38_reading.md` (the opening, 282r ll. 5/6/17/20, 282v ll. 10–11 and
  21, 283r ll. 2/4/13, 283v ll. 2–3, 18, 20, 284r l. 7, the end of 284v). No outside blocker: the images are available
  and legible with effort. Next step: re-transcribe these lines from full-resolution crops (a fresh transcription of the
  record would be the efficient route), then re-run `reread_b00_decode.py --trans`.
