# Translation brief: every document counted as read gets a reading and an English translation (22 Oct 2026)

George Lasry, 22 Oct 2026: a reading is "readable coherent text + translations", not a mechanical decryption. The
gate (`docs/_texts.py reading_problems`) refuses a document marked read without an English translation. This wave
writes them.

Worktree: `C:\Users\dbour\cypher\.worktrees\reading-gate`. Standard to match: `targets/matignon1586/texts/reading_f173.md`
and `reading_f173_en.md`; `targets/carpio1677/read/R1008_reading.md` and `R1008_en.md`.

## Per target in your list

For every `outcome.texts` entry of `targets/<folder>/profile.json` whose `state` is `read` (or absent) and that has
no `translation` (and whose `language` is not `en`):

1. **The reading.** If the decryption file already reads as sentences (prose, word division, punctuation), it is the
   reading. If it is raw — unspaced, all capitals, one decoder line per manuscript line, nomenclator tags, tables of
   runs — write `<dir>/<doc>_reading.md`: the same text as sentences in its own language and spelling, codes resolved
   where the key gives them (`[SUA MAESTA]` → *Sua Maestà*), holes kept and marked `[…]`, `[?word]`, `[47]`. Normalise
   only word division, capitals and punctuation. **Change no letter the decryption does not give, add no word.**
   Where the decryption has clear text around cipher runs, the reading is the whole letter as far as the repository
   has it; say in the header what is clear and what was cipher.
2. **The translation** `<dir>/<doc>_en.md`: plain modern English, faithful, sentence for sentence, with the same
   holes (`[…]`, `[?word]` translated as `[?word-in-English]`, `[47]` kept). Names as in the original; titles as in
   English usage (Vostre Majesté → Your Majesty). A short header: document, date, what the text is (reading of the
   decryption / clear copy / contemporary decipherment), and the file it translates.
3. **If the document does not read** (holes in most sentences, you cannot build the sentences), do not translate it:
   list it in your reply with the reason. It will be relabelled.
4. **profile.json**: add `"reading"` (when you wrote one), `"translation"` and `"language"` (ISO 639-1) to the entry,
   with targeted edits that keep the file's layout: reuse `research/reading_audit/relabel_r0.py`'s splice approach
   (copy it as `translate_<batch>.py`); validate with `python docs/_check_profile.py <folder>` (`result: valid`).
   `<dir>` is the folder of the entry's decryption file (e.g. `texts/`, `read/`), or `texts/` when that is a URL.
5. Do not edit NOTES, pages, README or ledgers. Do not commit.

Long documents are translated in full. If a target has more than about 15,000 words to translate, do as many
documents as you can in full, never half a document, and list the rest in your reply.

Reply: per target, documents translated, readings written, documents that do not read (with why), and any not done.
