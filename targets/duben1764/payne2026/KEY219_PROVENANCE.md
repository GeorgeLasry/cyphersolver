# Key 219 matched to the printed February 1771 letter

## Result and scope

The handwritten reference below Riksarkivet image219 points to a real printed cipher passage in **Henrik Schück (ed.), Gustav III:s och Lovisa Ulrikas brevväxling, partI, p259, letter143**. It appears in the appendix to *Svenska Akademiens handlingar ifrån år1886*, volume29 (1917; published1918), and in the separate1919 edition.

The printed letter is undated. Schück's note dates it to **mid-February1771**, because it answers the queen's letter of25January1771 and precedes the prince's knowledge of the king's death. The preceding letter on p258 is dated Paris,10February1771. This confirms the note's connection to the Crown Prince's French journey. It does **not** prove when the key was originally made, or exclude earlier reuse.

**This is a side finding, not a decipherment of the May1764 letter on images105–108.** The archival key has now been connected to an actual encoded passage; its application to catalogue450's main sample remains unsuccessful.

## Reproducible source locations

- [Archival key219](https://sok.riksarkivet.se/bildvisning/A0073297_00219).
- [Libris volume record](https://libris.kb.se/f1zwzfp5c7z9bhdc), with structured metadata at `https://libris.kb.se/f1zwzfp5c7z9bhdc/data.jsonld`.
- [Public library scan, printed p259 / scan595](https://digitalt.kb.se/dark-34918583/part/1/page/595).
- [IIIF manifest](https://digitalt.kb.se/dark-34918583/manifest),648 canvases. Canvas595 is printed appendix p259; the manifest's labels count scan images, not printed pages.
- Image service for that page: `https://data.kb.se/iiif/3/dark-34918583%2FPROD_JP2000%2F004797649%2Cpm%2C0595.jp2/full/1800,/0/default.jpg`.
- [Riksarkivet SBL bibliography](https://sok.riksarkivet.se/sbl/Presentation.aspx?id=9719) independently identifies the edition and its publication in volumes29–30.

The public IIIF images were retrieved and visually inspected. No login was used. The1857 volume29 of the earlier1796 series is a different publication and is not the matching reference.

## What the printed edition leaves open

The editor identifies **626 as Fersen** and **665 as Breteuil**, then prints two further numeric passages without resolving them. Footnote2 states: “Denna chiffer har ej upplösts.” That is, the cipher was not deciphered in that edition. This is not a claim that no later scholar has read it.

The long run wraps after `381263682`. The following printed run is `344872332323891394771842176112176646`. Together they have45digits, hence15three-digit groups. The superscript2 after it, and after `441853`, is a footnote call, not a cipher digit.

## Literal key application

| Printed passage | Groups | Key219 values |
|---|---|---|
| Editor's first name |626|Fersen le Cte|
| Editor's second name |665|Breteuil|
| Long passage, first seven groups |381 263 682 344 872 332 323|bo · ne · in · te · li · ge · nce/nci|
| Long passage, remainder |891 394 771 842 176 112 176 646|en · tr · e/ea · la · Cour · et · Cour · franc|
| Short passage |441 853|c · re|

The first part reads **“bonne intelligence entre la…”** after normalizing doubled consonants. The court wording remains abbreviated in the literal output, and `c · re` may represent “créé[?]”; that expansion is tentative. In its clear French context, the sentence discusses Breteuil's attachment to good relations between courts. No missing preposition, suffix, or grammatical agreement is silently added.

A cautious reading is therefore:

> … son attachement pour la **bonne intelligence entre la Cour et Cour franc[?]**, qu’il se vante d’avoir **créé[?]** …

Only the bold portions are the present key-applied reading; the surrounding text is already printed in clear. In English: “… his attachment to good relations between the court and the French court[?], which he boasts of having created[?] …”.

The two independently identified names match exactly, and the15-group passage produces a connected French phrase. This is substantive evidence for this **1771 key/letter connection**, unlike a coverage score. It is still inappropriate to call the full letter or catalogue450 complete.

## Corrections and measurement

Full-resolution reinspection corrected preliminary readings **323 to nce/nci, 891 to en, 771 to e/ea**, and confirmed626 as Fersen. The first two changes are visible in the manuscript; the printed context assists their interpretation and is disclosed here. The key transcription remains preliminary elsewhere.

`schuck1771_cipher.txt` preserves all19printed cipher groups in this passage. Two names were already identified by the editor;17groups had been left unresolved in this edition. `schuck1771_reading.tsv` gives the literal mapping for every group, and `read_schuck1771.py` reproduces it with assertions for the names and the start of the phrase. No percentage of fully normalized coherent plaintext is asserted: the final court abbreviation and `cre` are still editorially uncertain.

The doubled-consonant normalization here also warns against assuming that a numeric syllabary must concatenate into exact modern French spelling. A failed exact-string alignment of image126 cannot disprove a relationship between its French and its numeric text.

Method: **known key applied**, for this separately printed1771 passage only. Prior-art status: editor explicitly left the two runs unresolved; later prior art not exhausted. Discovery date:28October2026.
