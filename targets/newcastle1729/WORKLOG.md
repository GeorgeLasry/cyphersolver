# newcastle1729: work log

Every step, in order, failures included. Work done by Claude Code (Anthropic) under the direction of johonn
(GitHub), as an outside contribution. Images are on the Huntington Digital Library (hdl.huntington.org,
collection p15150coll7) and are not committed; page ids are given as HDL ids.

## 2026-10-28

1. **Setup.** Read CONTRIBUTING.md, README (Repository layout, Conventions), lang/README.md and catalogue.json
   entry 826. Branch `catalogue-826` from main (6da5ddae4), worked in a separate worktree.
2. **Access.** HDL CONTENTdm API (`dmGetCompoundObjectInfo`) lists the pages of the five objects:
   - mssBLA 191 (HDL 61008, letter of 8 Aug 1729 to Newcastle): pp. 1-6 = 61001-61006, cover 61007.
     The code report is p. 5 = 61005.
   - mssBLA 187 (HDL 60966, 23 June 1729): pp. 1-4 = 60961-60964, cover 60965.
   - mssBLA 188 (HDL 60924, copies of 3 letters, July 1729): pp. 1-8 = 60915-60922, cover 60923.
   - letter of 14 July 1729 (HDL 60892): pp. 1-6 = 60885-60890, cover 60891.
   - letter of 4 Aug 1729 (HDL 60914): pp. 1-10 = 60903-60912, cover 60913.
   All 39 images downloaded through IIIF (`/iiif/2/p15150coll7:<id>/full/2000,/0/default.jpg`) to a scratch
   directory. Worked.
3. **Survey of the pages** (contact sheets). Code pages with an interlinear decipherment in a second hand:
   60963 (187 p. 3); 60916-60920 (188 pp. 2-6; the leaves are folded over each other, so some images show
   two leaves overlapping); 60886-60887 (14 July pp. 2-3); 60907-60909 (4 Aug pp. 5-7). The interlinear
   values are syllables and short words ("ma-de", "con-cer-..."), so the system is a numerical
   syllable-and-word code, not a letter cipher. 61005 (191 p. 5) has no interlinear text.
   The HDL cover sheet of 188 lists "Enclosure (to Newcastle): unsigned, undated [from Port Ste Marie]
   intelligence report in cipher, deciphered (in French)"; its page images are 60916-60920.
4. **Report transcribed** (HDL 61005, IIIF region crops at full resolution): 13 lines, 141 groups, 101 distinct
   (measured with `docs/_check_profile.py --measure`). Doubtful: L01 386 (first digit rewritten), L02 1201 (on a
   blot), L03 163 or 103 (middle digit blotted), L10 473 (heavy 7). The line ends in a row of dots: the text
   breaks off. `transcription/report_61005.txt`, tokens in `report_61005_tokens.txt`.
5. **mssBLA 187 p. 3 (60963) tried first.** A copyist's hand (4 like "A", 7 like ">") with glosses not set
   under their groups; alignment by position was unreliable (e.g. line 1: "vous mettr-ie---s Monsieur
   Ra-li--" over eight groups). Put aside until the 188 values could anchor it.
6. **mssBLA 188 enclosure transcribed** (60917, 60918 left leaf, 60919, 60920; 58 code lines): each gloss
   stands under its group. Readings settled on zooms: 1014 is "ſa" (sa), not la (660); 737 = monsieur (the
   hand's 3 is close to 8); 822 is glossed with an R-shaped capital P, so Pa (Pa-ti-g-no: Patiño, also on 60919
   L12). 1240-1290 groups carry no gloss and stand where a full stop falls (1243, 1250, 1252, 1290 written
   with a dot).
7. **First table and first decode.** `build_table.py` -> `codetable.tsv` (232 groups, 473 glossed occurrences);
   `decode.py` -> `decryption/report_61005_decode.txt`: 105 of 141 report groups (74.5%) have a value. The
   report opens "[805] que je vous ai, Milord, est ..." (697 665 941 270 = mi-lo-r-d, as on 188 p. 1).
   Glosses that disagree between occurrences are kept as grade M (926 que/qui, 929 qu'il/que, 289 du/Don,
   945 ri/ra, 1109 ti/"lor").
8. **Model switch.** The session model was changed mid-way by the user; nothing carried over except these
   files and the log.
9. **14 July 1729, p. 3 (HDL 60887) transcribed**: a fair copy of bracketed extracts, dotted groups, glosses
   under each, in an even hand (19 passages). Clearer than the 188 enclosure. It gives 735 = monsieur (the 188
   enclosure and the report write 737 in the same place: two groups, both "monsieur", kept apart), 473 = faire
   (settles the heavy figure in report L10), 1200 = x, 1063 = soupçon, 1018 "ser" read as fer? (feront). Table
   rebuilt: 280 groups, 629 glossed occurrences; report coverage 111 of 141 groups (78.7%).
10. **4 Aug 1729 enclosure transcribed** (HDL 60907, 60908, 60909: 19 + 7 + 14 passages), the neatest hand of
    the five sources: dotted groups, gloss under each. Names settle: Ken-ne = Keene, Pa-ti-g-no = Patiño,
    Sta-no-pe = Stanhope, Mi-lo-r-d = Milord (the report opens with 697 665 941 270). Sums and dates:
    16 = cent, 1206 = deux, 11 = cinquante, 17 = mille, 1211 = sept, 8 = vingt, 1213 = neuf ("deux cent
    cinquante livres sterlings", dated Mille sept cent vingt neuf). Corrections to earlier steps: 1018 is
    "ser" (ser-ai, ser-oit), not "fer" (checked on the 188 enclosure and the 14 July extract too).
    Doubtful and left marked: 491 (r? for 941), 045 (res), 1015 (sans? for 1016), 701/594 under "ai-mo-oit".
11. **Table rebuilt**: 365 groups, 996 glossed occurrences (337 grade H, 28 grade M). Report coverage 118 of
    141 groups (83.7%).
