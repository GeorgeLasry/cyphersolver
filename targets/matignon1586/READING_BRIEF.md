# Reading brief: the matignon1586 leaves that are "decoded, not read" (22 Oct 2026)

George Lasry, 22 Oct 2026, on this page: *"The decryptions are not useful. They seem to have many errors, making it
impossible to assemble coherent French sentences. This is likely due to transcription errors. The requirement should
be that the LLM can build coherent sentences - that can later be translated to English, and iteratively improve the
transcription and the key until this is the case. … It is OK to have a few holes, but not holes in almost every
sentence."*

The job, per leaf: turn the mechanical decode into **coherent French sentences with only scattered holes**, and
translate them into English, by going back and forth between the decode, the image and the key.

## What there is

Worktree: `C:\Users\dbour\cypher\.worktrees\reading-gate` (branch `reading-gate`). Folder `targets/matignon1586/`.

* `NOTES.md` — the whole history; read the key section, "One key, 22 Oct 2026", and Brackx's sections (his label set).
* `brackx2026/<leaf>_cipher.txt` — Michael Brackx's transcription, one manuscript line per line, figures as labels
  (`z yy c Ze dd …`; numbers are code groups). **No second reader has checked these labels.**
* `key_cipher1.json` — the merged key: label → set of letters (the figures are confusable, so each has a set).
  Code values are listed in NOTES ("One key") and on `docs/matignon1586.html` section 02.
* `final_texts.py` / `dec.py` — the beam + 6-gram decoder that wrote `texts/<leaf>.txt` (figures, then decode, per line).
* `brackx2026/copies/` — the clear copies of ff. 143, 150, 154 and the f. 19 decipherment of f. 18: aligned with their
  ciphers (`brackx2026/f143r_cipher.txt` etc.) they show what each label really stands for, and what the hand's
  slips look like. `texts/reading_f143.md` etc. show the target standard.
* Images: Gallica IIIF, fr. 15572 = ark `btv1b9061879d`, fr. 15571 = `btv1b90618802`. Each canvas is a double page;
  folio recto = right half. URL pattern `https://gallica.bnf.fr/iiif/ark:/12148/<ark>/f<canvas>/<x,y,w,h>/<W>,/0/native.jpg`
  (region crops at full resolution read best). Canvas per leaf is in NOTES ("Access: folio to Gallica canvas"):
  f. 110 = 116 right; ff. 123r–124v = 129 right – 131 left; f. 173 = 180 right; f. 196 = 203 right; f. 201 = 208
  right; fr. 15571 f. 177 = 185 right. Save images under the scratchpad
  `C:\Users\dbour\AppData\Local\Temp\claude\C--Users-dbour-cypher\6b6912a8-0ad3-4eda-b63e-c79291f1bcc5\scratchpad\matignon_img\`, never in the repo.

## How to work

1. Decode the leaf (reuse `final_texts.py`'s functions; do not change the shared key file in place — write any
   changed key to `key_cipher1_<leaf>.json` and say why).
2. Go sentence by sentence. Where the French will not form, find the figures under the break, crop that line from the
   image, look, and decide: a misread label (most likely), a homophone set too narrow or too wide, a code group, a
   name, or a writer's slip. Fix, re-decode, continue. Use the clear copies as the reference for what each label
   looks like in this hand.
3. **Do not invent.** Every word of the reading must be carried by its figures. A word the figures only partly
   support is `[?word]`; a stretch you cannot read is `[…]`; an unidentified code group is `[47]`. Context may choose
   between the letters a figure allows; it may not supply letters the figures do not give. A reading with honest holes
   is the goal, not a fluent paraphrase.
4. Stop a leaf when its sentences hold (the bar: most sentences with at most one hole in ten words; check with
   `python docs/_check_reading.py --file targets/matignon1586/texts/reading_<leaf>.md`), or when the remaining breaks
   are on the image itself (faded, cut, blotted) — say which.

## Output (only these files; do not edit NOTES, profile.json, the page or other leaves)

* `texts/reading_<leaf>.md` — the French reading, one paragraph per sense unit, manuscript line numbers in the margin
  as `[l. 12]` markers, holes marked; a header saying what was done.
* `texts/reading_<leaf>_en.md` — the English translation, same holes.
* `brackx2026/corrections/<leaf>.tsv` — every label change: line, token index, old, new, reason (what the image shows).
  And the corrected transcription as `brackx2026/corrections/<leaf>_cipher.txt`.
* `texts/reading_<leaf>_log.md` — the passes: what was tried, what worked, what failed (this feeds the profile's
  solution steps, including the failures), and the `_check_reading.py` result at each pass.

Final reply: the clean-sentence share before and after, the number of label corrections, what stays open and why,
and three sentences with their translation that show the level reached.
