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

## r2p, 23 Oct 2026 (Claude Opus 5.5): every hole checked on the DECODE images

Each hole located (`research/reading_audit/r2p_holes.py`), its line looked at on the image (scratchpad
`reread/r2p/crops`), cancellation strokes looked for, the figures parsed (`r2p_parseall.py`). Some show-through and
spread ink (283r, 284r, 284v); a large blot on 284v l. 10.
Filled:
- 282v l. 20 "caciarli": "25 21 25 17 21 00 50 7" (was "caciar[li]").
Left, with blockers (284r l. 7 "[?steso]": "5 4 6 3 5 4 5 9" = steso, but a stroke runs over it that may be a
cancellation or show-through, illegible; 284v ll. 10-11 "doueua fare […]": a blot over the line, illegible):
- 282r l. 2 "[…] fui l": "5 517^. 0 1 8" (best parse "eein"). Blocker: no-key-material.
- 282r l. 3 "m haueua de[t]to d esere": "6 2 3 5 1 1 1 9 1" (best parse "dexo"). Blocker: no-key-material.
- 282r l. 5 "Bresa et […] a dani": "0 1 3 5 0 1 2 196^." (best parse "nrlz[sauoia]"). Blocker: no-key-material.
- 282r l. 6 "mi dise hauer[…] auisato in": "1 4 2 1 3 7 350^. 0 2 0" (best parse "hauieran"). Blocker: no-key-material.
- 282r l. 8-9 "non hauese tenta[t]o ogn altra": "6 3 5 3 1 | 2 1 1 1 2" (best parse "tentaxa"). Blocker: no-key-material.
- 282r l. 17-18 "non rientrase […] a dani": "3 | 500^. 9 4 0 0 5 229^." (best parse "erogl[ugonotti]"). Blocker: no-key-material.
- 282r l. 20 "et seruitore [?] ualersi di": "(none)". Blocker: nothing written there; no-key-material.
- 282r l. 20 "che lo seruir[à] bene et": "9 143^. 5 003^. 7 1 7 1" (best parse "o[guerra]erui"). Blocker: no-key-material.
- 282v l. 1 "del ambasciatore [di] Sauoia che": "(none)". Blocker: nothing written there; no-key-material.
- 282v l. 10 "non mancaua [?] né al": "7 9". Blocker: no-key-material.
- 282v l. 11 "suo regno [?] di farsi": "0 0". Blocker: no-key-material.
- 282v l. 13 "la giustitia [è] dal canto": "1 5 9". Blocker: too-short.
- 282v l. 19 "Ugonotti come [?] uol dare": "(none)". Blocker: nothing written there; no-key-material.
- 282v l. 21 "li comporta […] perché in": "0 3 5 0 1 1 5 3 4 3 7 5 3 2 1 5 0 2 1 2" (best parse "flresueuala"). Blocker: no-key-material.
- 282v l. 22 "predicano et [e] sercitano il": "8". Blocker: too-short.
- 283r l. 2 "cifra di […] del pasato": "9 1 5 9 8" (best parse "ogr"). Blocker: no-key-material.
- 283r l. 4 "S mai [?] più il": "(none)". Blocker: nothing written there; no-key-material.
- 283r l. 4 "che lei [et] io poteuo": "2 6 5". Blocker: too-short.
- 283r l. 6 "che come [p] adre comune": "(none)". Blocker: nothing written there; no-key-material.
- 283r l. 7 "Christo hauendo ri[g]uardo al ben": "1 1 7 5 9 3 7 2 1 0 0 2 6 1 9 1" (best parse "xieouardo"). Blocker: no-key-material.
- 283r l. 13 "l uficio […] che il": "5 6 5 0 2 1 3 2 6 3" (best parse "etlaratu"). Blocker: no-key-material.
- 283r l. 16 "particolarm[ente] la [c] ontinoua uigilanza": "(none)". Blocker: nothing written there; no-key-material.
- 283r l. 22 "non hauerne [?hauta] parte": "142^. 1 3 2 1 5 2" (best parse "[presidente]rac"). Blocker: no-key-material.
- 283v l. 2 "suo consigliere a[l] sodeto sig": "2 1 2". Blocker: too-short.
- 283v l. 2-3 "Sauoia per […] da lui": "1 7 1 9 | 9 5 0 1 2 6 3 5 0 0 5" (best parse "iooendere"). Blocker: no-key-material.
- 283v l. 3 "da lui […] la causa": "3". Blocker: too-short.
- 283v l. 4 "per la [?uia] dela r[a]gione": "1 7 3 1 7" (best parse "ui"). Blocker: no-key-material.
- 283v l. 5 "[?uia] dela r[a]gione di persuader[lo]": "1 4 0 1 7 9 1 0 1 5" (best parse "hnione"). Blocker: no-key-material.
- 283v l. 5 "r[a]gione di persuader[lo] ad abraciarla": "6 4 5 4 3 7 2 1 2 6 3 5 0 0 5 0" (best parse "persuaderl"). Blocker: no-key-material.
- 283v l. 12 "sarano fati [?con] il duca": "1 0". Blocker: no-key-material.
- 283v l. 13 "il suo desiderand[o] molto che": "2 6 3 5 4 5 1 7 2 6 3 5 0 0 2 1 0 1 6 2" (best parse "desiderand"). Blocker: no-key-material.
- 283v l. 15 "di pace [con] seruando l": "2 9". Blocker: too-short.
- 283v l. 17 "ambasciatore per [un] suo secretario": "1 7 3 5 0" (best parse "ul"). Blocker: no-key-material.
- 283v l. 18 "stato per […] di qua": "1 7 0 1 9 2 1 2 4 2 1 0 8" (best parse "inoasan"). Blocker: no-key-material.
- 283v l. 19 "aspetando se [?] uorrà replicare": "(none)". Blocker: nothing written there; no-key-material.
- 283v l. 20-21 "audienza feci […] quello che": "2 1 2 | 2 5 1 9 1 4 2 1 6 4 5 2 1 2 5 0 0 0 3 5" (best parse "acosaperealre"). Blocker: no-key-material.
- 284r l. 7 "un corriere [?steso] per dare": "5 4 6 3 5 4 5 9" (best parse "steso"). Blocker: illegible (a stroke over it).
- 284r l. 8 "S tuta […] [?sodisfatione] che": "164^. 9 1 2 6 1 7 5 2 2 1 5 1 1 7 9 1 0 1 5" (best parse "[qualmente]odicatione"). Blocker: no-key-material.
- 284r l. 20 "et ritirata [a] casa sua": "5 7 2 1 2" (best parse "sfa"). Blocker: no-key-material.
- 284v l. 1 "manco fauorita dal[a] M tà": "8 2 6 2 1 5 0" (best parse "dal"). Blocker: no-key-material.
- 284v l. 7 "Re conueniria far[e] […] triegua": "3 0 2 1 0 0 1 9 5 0 5 5 6" (best parse "fannoleche"). Blocker: no-key-material.
- 284v l. 9 "a S [Ecc.za] che questo": "9 3 5 5 3 5 0 1 1 2 2" (best parse "oeeenza"). Blocker: no-key-material.
- 284v l. 10-11 "doueua fare […] che non": "1 5 3 5 0 2 2 0 1 7 1 | 6 1 2 1 7 4 5 5" (best parse "eemmitrarise"). Blocker: illegible (blot).
- 284v l. 11 "uedeua rimedio […] N S": "8 4 7". Blocker: too-short.
- 284v l. 11 "N S […]": "9 0 0 1 7 1 1 9 4 7 9 5 2 0" (best parse "orixosiquam"). Blocker: no-key-material.
Result: 1 hole filled; 46 left, each with its blocker.
