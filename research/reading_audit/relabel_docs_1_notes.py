"""NOTES.md edits for the relabel_docs_1 targets (RELABEL_DOCS_BRIEF.md), 22 Oct 2026. Run once.

Same edit() as relabel_docs_0_notes.py, with this batch's table.
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
EARLIER = 'Earlier status (before the 22 Oct 2026 reading audit): '
IP = 'Status: in progress. '

ESC_LASRY = ["- [x] siblings: not this project's reading; George Lasry's report covers the volume",
             "- [n/a] clear-pages: not looked for here; the result is Lasry's",
             "- [x] known-keys: Lasry's key is the key; his key table is not in the repository",
             "- [x] print: Lasry's report (BnF cipher research, 10 Oct 2026) is the source",
             "- [n/a] key-rebuild: not this project's work",
             "- [ ] retry: ask Lasry for his full transcription and decryption"]

# folder: (new status line or None, block, [gap lines], escalation lines or None)
T = {
 'esp318': (IP + "No. 92 decoded with the Cifra general, not yet read as sentences (reading audit, 22 Oct 2026).",
  "**22 Oct 2026, reading audit** (George Lasry's test: can sentences be built and translated?): f116_reading.md is a "
  "line table of sign strings with a gloss column. The clear opening and some cipher lines build Spanish clauses (f. 116r "
  "ll. 6-7, 15, 17, 22-25, 33; f. 116v ll. 3-9), but ll. 8-11, 16, 18-21, 26-31 and 34 are open codes and unplaced letter "
  "runs, so most cipher sentences have holes: no. 92 is *decoded, not read*. Class read in part -> not read, method -> not "
  "solved, fraction_read 0.75 -> 0 (the three-quarters estimate is withdrawn as a reading figure). The key identification "
  "and the summary below stand as a gist.",
  ["no. 92 as a running text: decoded, not read - blocker: not-attempted; re-read f. 116r ll. 8-11, 16, 18-21, 26-31, 34 "
   "and f. 116v ll. 1-2, 10-11 on the full scans against the Cifra general, then write a normalised reading and a translation"],
  None),
 'esp318no94': (None,
  "**22 Oct 2026, reading audit** (George Lasry's test): the repository holds only Brackx's sign transcription; his "
  "provisional decryption (issue #62) has holes in most sentences around about 90 open code groups. No. 94 is *decoded, "
  "not read*: class read in part -> not read, method -> not solved, fraction_read 0.929 -> 0. The ciphertext-only "
  "recovery of the alphabet stands.",
  ["no. 94 decryption: decoded, not read, and not in the folder - blocker: not-attempted; copy Brackx's decryption from "
   "issue #62 into texts/, check it line by line on the scans, build sentences around the open codes"],
  None),
 'eugenie1859': (IP + "Lasry's reading; only four pages of tokens and three excerpts are in the repository (reading audit, 22 Oct 2026).",
  "**22 Oct 2026, reading audit** (George Lasry's test): the token table of ff. 9r, 15r, 17r, 18r, taken in order, builds "
  "French sentences, and the three report excerpts (ff. 19r, 35r, 27r) read; both are *excerpts* of Lasry's reading, whose "
  "full text is not in the repository. Krajcovic's corrections file is *not prose*. fraction_read 0.841 (Lasry's "
  "identified elements) -> about 0.31, what the repository shows.",
  ["Lasry's full decipherment of the eleven cipher pages, not in the repository - blocker: not-attempted; ask George "
   "Lasry for his transcription and decryption files"],
  ESC_LASRY),
 'exea1408': (None,
  "**22 Oct 2026, reading audit:** nothing of the letter is in the repository (the Google Books link is blocked to "
  "scripts), so the entry is *decoded, not read* in profile.json; class already solved is kept because the text is in "
  "print (Puig 1920).",
  [], None),
 'ghinucci1527': (None,
  "**22 Oct 2026, reading audit** (George Lasry's test): R8613 reads; the R8589 and R8476 files are key-building "
  "worksheets (token=value alignments) and are marked *not prose* in profile.json. Claim unchanged.",
  [], None),
 'haga1620': (IP + "R2113 read; R2115 decoded, not read (reading audit, 22 Oct 2026).",
  "**22 Oct 2026, reading audit** (George Lasry's test): R2113_reading.md builds Dutch sentences. R2115_reading.md calls "
  "itself partial: P2 and P4 are strings of [...], {?...} and bare codes, so R2115 is *decoded, not read*. Class read -> "
  "read in part; fraction_read about 0.48 (by words of the two reading files, estimated).",
  ["R2115: decoded, not read - blocker: not-attempted; transcribe P2 and P4 in full from the DECODE images and re-read "
   "the cipher spans with the R2118 key (m = 4); codes from R2113 and the decrypted R2114",
   "nomenclator codes [3], [7], [15], [19], [43], [46], [58], [62] - blocker: open-codes; the key's code column 37-45 is cut "
   "by the photograph's edge; most occur once or twice"],
  ["- [x] siblings: R2113, R2115 and R2114 (decrypted) are the same series and key",
   "- [ ] clear-pages: R2114's decryption not yet used for the codes",
   "- [x] known-keys: R2118 is the key",
   "- [ ] print: Haga's despatches in print (Heeringa) not searched",
   "- [x] key-rebuild: m = 4 added from context",
   "- [ ] retry: R2115 P2 and P4 not re-read"]),
 'harley287': (IP + "Every cipher run read in sense, with not-attempted gaps below (reading audit, 22 Oct 2026).",
  "**22 Oct 2026, reading audit** (George Lasry's test): the three documents read; the per-document C on the 20 March "
  "letter is overturned to B (R8485 and R8486 read; the holes are in the three short runs of R8487). Claim unchanged; the "
  "status line now says in progress because gaps below are not-attempted.",
  [], None),
 'hesse1672': (None,
  "**22 Oct 2026, reading audit** (George Lasry's test): reading.txt gives the cipher items in their clauses and each "
  "builds except the five-sign word of passage 1; the per-document C (no connected letter) is overturned to B, since the "
  "missing context is clear text. Excerpt note added: the full letter is on the HCPortal images, not transcribed. "
  "fraction_read 1.0 (values given) -> 0.922 (read as sense).",
  [], None),
 'hm1645': (IP + "Lasry's decipherment exists on DECODE; none of it is in the repository (reading audit, 22 Oct 2026).",
  "**22 Oct 2026, reading audit** (George Lasry's test): Lasry's plaintexts of R785, R790 and R923 are on the DECODE "
  "records only; the git-ignored copies are no longer in any checkout, so nothing could be read. All three are *decoded, "
  "not read* in profile.json; class already solved is kept (his decipherment exists), fraction_read 0.9099 -> 0.",
  ["R785, R790, R923: Lasry's plaintext not in the repository - blocker: not-attempted; fetch his interlinear and "
   "plaintext files with the shared DECODE cookie (git-ignored, his work), grade them as sentences, and ask him whether "
   "a reading copy may be kept"],
  None),
 'isabella1531': (IP + "Both letters deciphered at the time; neither decipherment is transcribed here (reading audit, 22 Oct 2026).",
  "**22 Oct 2026, reading audit** (George Lasry's test): no text of R9955 or R9956 is in the repository. Both are *decoded, "
  "not read* in profile.json; class already solved is kept (R9955 printed by Luo 2021; both deciphered at the time).",
  ["R9955: Luo's printed decipherment (2021, p. 285) not in the repository - blocker: not-attempted; the thesis is on "
   "RODERIC (Universitat de Valencia); the contemporary sheet is on the DECODE images",
   "R9956: the contemporary decipherment sheet, not transcribed - blocker: not-attempted; DECODE images reachable with "
   "the shared cookie"],
  ["- [x] siblings: charles1536 (R9957, R9952) is the same general cipher",
   "- [ ] clear-pages: the decipherment sheets on the DECODE images not fetched",
   "- [x] known-keys: AGS Estado leg. 1.1.1 doc. 112 (Tomokiyo)",
   "- [ ] print: Luo 2021 p. 285 not copied",
   "- [n/a] key-rebuild: deciphered at the time",
   "- [ ] retry: none yet"]),
 'it1583': (IP + "f. 68 read; f. 70 decoded, not read (reading audit, 22 Oct 2026).",
  "**22 Oct 2026, reading audit** (George Lasry's test): f. 68 (R7898) builds sentences from line 2 to line 11; its ? "
  "runs sit at line openings (per-document C overturned to B). f. 70 has holes in every clause of lines 1-5 and an unread "
  "signature: *decoded, not read*. Class read in part kept; fraction_read 0.9432 (assigned) -> 0.514 (tokens in f. 68).",
  ["f. 70 lines 1-5: decoded, not read - blocker: not-attempted; one to three unread signs in every clause; re-read them on "
   "the image with the shared key, and look for the sibling 1446 letters"],
  None),
 'kauderbach1754': (IP + "Nine letters read; R1954 decoded, not read (reading audit, 22 Oct 2026).",
  "**22 Oct 2026, reading audit** (George Lasry's test): nine of the ten hand readings build French sentences. "
  "read/R1954.txt (March 1756, about 65% read on a weak transcription) has holes in most sentences: *decoded, not read*. "
  "Class read -> read in part; fraction_read 0.998 (groups given a value) -> 0.81 (groups in letters that read).",
  ["R1954 (March 1756, 1,621 groups): decoded, not read - blocker: not-attempted; re-transcribe from the DECODE images and "
   "re-decode with key.json",
   "nomenclator names left as code letters ([C./.], [Q./.], [S./.] ...) - blocker: open-codes; the 1761 key R936 does not "
   "carry this table's names"],
  ["- [x] siblings: all ten records of KHA Prins Willem V inv. 201 decoded with one key",
   "- [ ] clear-pages: not looked for",
   "- [x] known-keys: Kauderbach's 1761 key R936 (vocabulary only; numbers differ)",
   "- [ ] print: not searched for R1954",
   "- [x] key-rebuild: table recovered by annealing",
   "- [ ] retry: R1954 not re-transcribed"]),
 'lee1526': (IP + "Read at the time; R8533's own reading is a worksheet, decoded, not read (reading audit, 22 Oct 2026).",
  "**22 Oct 2026, reading audit** (George Lasry's test): R8566, R8465 and R8473 read. r8533_reading.txt is a sign-level "
  "worksheet with holes in several sentences, and f. 109r was not re-read in pass 2: R8533 is *decoded, not read*. "
  "fraction_read 1 -> 0.445 (tokens in documents that read); class already solved kept (every run was deciphered at the "
  "time, L&P IV).",
  ["R8533: decoded, not read (f. 109r, f. 109v ll. 1-4 and 17-22, name codes) - blocker: not-attempted; re-read f. 109r and "
   "f. 110r at full resolution on the DECODE images and write a running text"],
  ["- [x] siblings: all 17 records of catalogue 103 opened; four carry cipher",
   "- [x] clear-pages: R8566 interlinear decipherment; L&P IV 3028 crib for R8533",
   "- [x] known-keys: Tomokiyo's Lee-Worcester key (on R8566)",
   "- [x] print: L&P IV calendars Tuke's decipherments",
   "- [n/a] key-rebuild: the key is known",
   "- [ ] retry: R8533 f. 109r and f. 110r not re-read at full resolution"]),
 'maisse1593': (IP + "The Brienne 13 clear copies are not transcribed; both letters decoded, not read (reading audit, 22 Oct 2026).",
  "**22 Oct 2026, reading audit** (George Lasry's test): no text of f. 406 or f. 410 is in the repository, only links to "
  "the cipher leaves and to the Brienne 13 copies. Both are *decoded, not read*; class read -> not read, method read from "
  "existing decipherment -> not solved until the copies are transcribed; fraction_read 1.0 -> 0.",
  ["ff. 406 and 410: the Brienne 13 clear copies, not transcribed - blocker: not-attempted; Gallica btv1b100904592 "
   "canvases 176 and 199 through the IIIF at openapi.bnf.fr; then check them against the cipher leaves and f. 404's "
   "interlinear decipherment"],
  ["- [x] siblings: f. 404 (twin of f. 406, partial interlinear) and f. 412 (twin of f. 410) identified",
   "- [x] clear-pages: Brienne 13 fol. 171r and 193v located",
   "- [ ] known-keys: Tomokiyo's key for this cipher (src/henryiv_Maisse2.png) not applied",
   "- [x] print: Berger de Xivrey used to locate the copies",
   "- [n/a] key-rebuild: the key exists (Tomokiyo)",
   "- [ ] retry: none yet"]),
 'marechaux1520': (IP + "f. 41v read here; f. 41r is Lasry's reading on overlay images, not transcribed (reading audit, 22 Oct 2026).",
  "**22 Oct 2026, reading audit** (George Lasry's test): texts/f41v_decryption.md reads. f. 41r's entry points only to "
  "Lasry's overlay images on cryptiana, with no text in the repository: *decoded, not read* (excerpt only). Class read -> "
  "read in part; fraction_read 0.998 (f. 41v alone) -> about 0.5 of the leaf (estimated).",
  ["f. 41r: Lasry's reading, on overlay images only - blocker: not-attempted; transcribe his three overlay crops (main "
   "checkout prior/, git-ignored; cryptiana GL.htm) and join them to the f. 41v running text"],
  None),
 'matignon1586c3': (IP + "f. 276 and f. 179 read; fr. 15573 ff. 379-381 decoded, not read (reading audit, 22 Oct 2026).",
  "**22 Oct 2026, reading audit** (George Lasry's test): f. 276 and f. 179 read from SOLUTION.md. fr. 15573 ff. 379-381 "
  "(Burford v0.5) is an unpunctuated machine decode with a garbled word in nearly every sentence and no translation: "
  "*decoded, not read*. fraction_read 0.9118 -> 0.305 (signs in the two slips that read).",
  ["fr. 15573 ff. 379-381: decoded, not read - blocker: not-attempted; repair the sentences on the Gallica images "
   "(btv1b90618780 views 740-745), punctuate and translate"],
  None),
 'mayenne1586c2': (None,
  "**22 Oct 2026, reading audit** (George Lasry's test): ff. 218-219 read. f. 120 has holes in most sentences of c01-c05, "
  "c15-c19, c28-c31 and f. 120v c03-c05, and f. 385 is a self-declared partial unspaced decode: both *decoded, not read*. "
  "fraction_read 0.861 (tokens in sense runs) -> 0.404 (tokens in ff. 218-219).",
  ["fr. 15573 f. 120: decoded, not read - blocker: not-attempted; re-read the holed paragraphs on views 246-247",
   "fr. 15573 f. 385: decoded, not read - blocker: not-attempted; v0.2 partial, unspaced; resolve the open stretches on "
   "views 752-753 and normalise"],
  None),
 'mellon136': (None,
  "**22 Oct 2026, reading audit** (George Lasry's test): reading.txt (all 31 passages) reads. Rieber's 2022 blog comment, "
  "a pointer with partial entries, is *decoded, not read* in profile.json, and the 2022 p. 24 pointer carries an excerpt "
  "note (nothing of it is in the repository). Claim unchanged.",
  [], None),
 'meryvic1589': (IP + "Lasry's reading; only excerpts with holes in every sentence are in the repository (reading audit, 22 Oct 2026).",
  "**22 Oct 2026, reading audit** (George Lasry's test): both excerpts in lasry_entry.md have holes in every sentence and "
  "the report says \"Partly deciphered\": *decoded, not read* (excerpt only). Class already solved -> not read, method -> "
  "not solved; Lasry's ciphertext-only key recovery is recorded in method_basis; fraction_read 0.96 -> 0.",
  ["Lasry's full decipherment, not in the repository - blocker: not-attempted; ask George Lasry for his transcription "
   "and decryption files (report: 6/6 pages transcribed, partly deciphered)"],
  ESC_LASRY),
 'mauclerc1593': (IP + "Read at the time; the interlinear decipherment is not transcribed here (reading audit, 22 Oct 2026).",
  "**22 Oct 2026, reading audit** (George Lasry's test): no text or link for fr. 3985 f. 20 is in the repository: *decoded, "
  "not read*. Class already solved -> not read, method -> not solved until the interlinear decipherment is transcribed.",
  ["fr. 3985 f. 20: the interlinear decipherment, not transcribed - blocker: not-attempted; Gallica btv1b90606498 views "
   "6-13 through the IIIF at openapi.bnf.fr; also fr. 3983 f. 140r, the register summary"],
  ["- [x] siblings: fr. 3983 f. 268 and fr. 3984 f. 33 (Dudout) carry interlinear decipherments too",
   "- [ ] clear-pages: the interlinear text and the fr. 3983 f. 140r summary not transcribed",
   "- [n/a] known-keys: read at the time",
   "- [ ] print: not searched",
   "- [n/a] key-rebuild: read at the time",
   "- [ ] retry: none yet"]),
}


def edit(folder):
    status, block, gaps, esc = T[folder]
    f = ROOT / 'targets' / folder / 'NOTES.md'
    raw = f.read_bytes().decode('utf-8')
    crlf = '\r\n' in raw
    s = raw.replace('\r\n', '\n')
    lines = s.split('\n')
    head = lines[:40]
    if status:
        for i, l in enumerate(head):
            if l.startswith('Status:'):
                lines[i] = EARLIER + l[len('Status:'):].strip()
        ins = [status, '', block, '']
    else:
        ins = [block, '']
    pos = None
    if not status:
        for i, l in enumerate(lines[:40]):
            if l.startswith('Status:'):
                j = i
                while j + 1 < len(lines) and lines[j + 1].strip():
                    j += 1
                pos = j + 1
                break
    if pos is None:
        pos = 1
        while pos < len(lines) and not lines[pos].strip():
            pos += 1
    lines[pos:pos] = ins
    s = '\n'.join(lines)
    if gaps:
        gl = '\n'.join('- ' + g for g in gaps)
        m = re.search(r'^## Remaining gaps[^\n]*\n', s, re.M)
        if m:
            nxt = re.search(r'^## ', s[m.end():], re.M)
            end = m.end() + (nxt.start() if nxt else len(s) - m.end())
            body = s[m.end():end].rstrip('\n')
            s = s[:m.end()] + body + ('\n' if body.strip() else '') + gl + '\n\n' + s[end:].lstrip('\n')
        else:
            sec = '\n## Remaining gaps\n\n' + gl + '\n'
            if esc and not re.search(r'^## Escalation', s, re.M):
                sec += '\n## Escalation\n\n' + '\n'.join(esc) + '\n'
            s = s.rstrip('\n') + '\n' + sec
    if crlf:
        s = s.replace('\n', '\r\n')
    f.write_bytes(s.encode('utf-8'))
    print('ok', folder)


if __name__ == '__main__':
    for n in sys.argv[1:]:
        edit(n)
