"""NOTES.md edits for the relabel_docs_2 targets (RELABEL_DOCS_BRIEF.md), 22 Oct 2026. Run once.

Same edit() as relabel_docs_1_notes.py, with this batch's table. richelieu has no NOTES.md (SOLUTION.md only) and
is not edited here.
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
EARLIER = 'Earlier status (before the 22 Oct 2026 reading audit): '
IP = 'Status: in progress. '
H = "**22 Oct 2026, reading audit** (George Lasry's test: can sentences be built and translated?): "

ESC_RETRY = "- [ ] retry: the re-reading named in Remaining gaps is not done yet"

# folder: (new status line or None, block, [gap lines], escalation lines or None)
T = {
 'navarre1586': (None,
  H + "texts/f333_decryption.md is raw decoder output, but the normalised reading of f. 333 below builds French "
  "sentences; the holes are the five name codes (no key material). The per-document C is overturned to B. Claim "
  "unchanged.",
  [], None),
 'norfolk1570': (IP + "f. 74r decoded with Tomokiyo's key, not yet read as sentences (reading audit, 22 Oct 2026).",
  H + "the line-by-line reading below has [..] holes, a stain or unkeyed signs in lines 1, 4-6, 8-10 and 12-17, so "
  "about half the sentences do not build: f. 74r is *decoded, not read*. Class read -> not read, method -> not solved, "
  "fraction_read unknown -> 0. The key, the dating and the gist stand.",
  ["f. 74r as a running text: decoded, not read - blocker: not-attempted; re-read lines 1, 4-6, 8-10, 12-17 on the BL "
   "IIIF strips (fetch.py, strips.py) against Tomokiyo's key and write a running text with a modern English version",
   "unkeyed nomenclator signs ⊕, ⊘, ø, ⊗, {a—}, {o—} - blocker: open-codes; not in Tomokiyo's key, each once or twice; "
   "look for them in the sibling letters ff. 66, 69, 75"],
  ["- [ ] siblings: ff. 66, 69, 75 of Cotton Caligula C II not searched for the six unkeyed signs",
   "- [x] clear-pages: f. 66r's decipherment used to check Tomokiyo's key",
   "- [x] known-keys: Tomokiyo's Mary-Norfolk key applied",
   "- [ ] print: no search for a printed text is recorded in these notes",
   "- [n/a] key-rebuild: the key reads; the holes are in the reading",
   ESC_RETRY]),
 'numeric1916': (IP + "辰密 reads; 共密 and 容密 decoded, not read (reading audit, 22 Oct 2026).",
  H + "the decode files are verbatim decoder output. 辰密 reads; 共密 (N32, N33, N35) and 容密 (N19b, N21, V4D) carry "
  "clusters of mis-decoded characters (圄會 for 國會, 代噸 for 代表) that break whole clauses, and no translation is in "
  "the folder (Dudout's Wenmi pages have them). Both are *decoded, not read*; class read in part kept; fraction_read "
  "0.9238 -> 0.11 (辰密's 232 of 2,100 groups).",
  ["共密 and 容密 telegrams: decoded, not read - blocker: not-attempted; copy Dudout's edited texts and translations from "
   "bdudout.github.io/wenmi into texts/, repair the garbled groups against groups.tsv and the JACAR scans"],
  None),
 'nunzio1718': (IP + "Lasry's reading of Spagna 364D; R154 and R173 decoded, not read (reading audit, 22 Oct 2026).",
  H + "Lasry's decode rows, joined into running text, build Italian sentences in 22 of the 24 despatches (R166, R168 "
  "and R170 were re-read and pass). R154 (364D/1) and R173 (364D/20) have runs of unread two-digit groups and open codes "
  "in most or half their sentences: *decoded, not read*. Class already solved kept; fraction_read 0.9789 -> 0.889 "
  "(groups in documents that read).",
  ["R154 and R173: decoded, not read - blocker: not-attempted; re-read the two-digit groups on the DECODE images "
   "(cookie at targets/bordeaux/decode/cookie.txt) and fill the codes from key_extra.txt, then write a running text"],
  ["- [x] siblings: all 24 despatches of 364D and the 364C corpus used for the codes",
   "- [x] clear-pages: the DECODE transcribers copied the interlinear decipherment into the PLAINTEXT lines",
   "- [x] known-keys: Lasry's reconstructed key (DECODE) is the key",
   "- [ ] print: no search for a printed text is recorded in these notes",
   "- [x] key-rebuild: nomenclator extended here (key_extra.txt)",
   ESC_RETRY]),
 'orbais': (IP + "no. 62 decoded, not read: the clear text is not transcribed (reading audit, 22 Oct 2026).",
  H + "texts/no62_decryption.md is one line per cipher group and the letter's clear text is not transcribed, so the "
  "runs stand as isolated words and no sentence can be built: no. 62 is *decoded, not read*. Class read in part -> not "
  "read, method -> not solved, fraction_read 0.824 -> 0 (75/91 signs read as sense, withdrawn as a reading figure).",
  ["no. 62 as a running text: clear text not transcribed - blocker: not-attempted; transcribe ff. 126r-127r from "
   "Gallica (btv1b52510705j, canvases 259-261) and set the 14 cipher runs in their clauses, with a translation"],
  None),
 'papai1706': (None,
  H + "R795 was graded C for its \"·\" marks; they are the 251 declared nulls (groups above 322), not gaps, and without "
  "them R795 reads like the other ten letters. Per-document C overturned to B; claim unchanged.",
  [], None),
 'poyntz1527': (IP + "R8567 read at the time; R8565's decipherment not yet transcribed (reading audit, 22 Oct 2026).",
  H + "R8567's three runs (plaintext.txt) read. Nothing of R8565's decipherment is in the repository, only the calendar "
  "paraphrases below, so R8565 is *decoded, not read*, with an excerpt note: the full decipherment is Tuke's, on the "
  "DECODE images and in L&P IV 3271 (British History Online). Class already solved kept; fraction_read 1 -> about 0.38 "
  "(by runs, estimated).",
  ["R8565: Tuke's decipherment not transcribed - blocker: not-attempted; transcribe the five interlinear bands from the "
   "DECODE images (cookie at targets/bordeaux/decode/cookie.txt) and check them against L&P IV 3271 and Tomokiyo's key"],
  ["- [x] siblings: R8566 and R8567, the same despatch series, checked",
   "- [x] clear-pages: the interlinear decipherment is the reading",
   "- [x] known-keys: Tomokiyo's Lee-Worcester key, spot-checked",
   "- [x] print: L&P IV 3271 and 3272",
   "- [n/a] key-rebuild: read at the time",
   ESC_RETRY]),
 'r1212': (None,
  H + "on pp. 3-4 the cipher runs, read in order, make continuous Latin (\"horum omnium motuum et perniciosarum "
  "factionum unicus author et certissimus est Franciscus Kendi ...\"); the clear scraps between them are separate. "
  "Per-document C overturned to B; claim unchanged.",
  [], None),
 'r2242': (None,
  H + "decrypt_p3.txt and decrypt_p4.txt, divided into words, build Dutch sentences; the open tokens are single word "
  "signs with no key material and two ink blots. Per-document C overturned to B for both pages; claim unchanged.",
  [], None),
 'r9416': (None,
  H + "the f. 262 gloss reads on page B but not on page A (\"...\" and [?] in most lines), so f. 262 is *decoded, not "
  "read*. The f. 263 entry counts only recto lines 11-16 (excerpt note); fraction_read 0.06 unchanged.",
  ["f. 262 page A from its signs - blocker: not-attempted; the f. 262 signs are not transcribed; key them from page B's "
   "full gloss (DECODE images, cookie) and read page A where the gloss is faint"],
  None),
 'rakoczi1704': (IP + "R852 read from its clear copy; R912 and R922 decoded, not read (reading audit, 22 Oct 2026).",
  H + "R912_image_read.txt and R922_image_read.txt are syllable-split decodes with misreadings in most lines; after the "
  "openings no coherent sentence can be built, so both are *decoded, not read*. R852 reads from its contemporary clear "
  "copy. Class read -> read in part; fraction_read 0.974 -> 0.182 (R852's 523 of 2,875 groups).",
  ["R912 and R922: decoded, not read - blocker: not-attempted; re-read the groups on the images (img/, DECODE cookie) "
   "with the R639 key and write normalised French with word division and a translation"],
  ["- [x] siblings: the other records of catalogue item 44 checked (R483 is a different cipher, now rakoczi1711)",
   "- [x] clear-pages: R852's clear copy; the interlinear decipherment on R912 p. 1 and R922's first lines",
   "- [x] known-keys: DECODE R639 (Bonac-Groffey) is the key",
   "- [ ] print: no search for a printed text is recorded in these notes",
   "- [x] key-rebuild: R639's table corrected from the image",
   ESC_RETRY]),
 'rakoczi1711': (IP + "R483 decoded from the clerk's decipherment, not yet read as a running text (reading audit, 22 Oct 2026).",
  H + "R483_clerk.txt merges the clerk's interlinear decipherment with the clear passages line by line, out of reading "
  "order, with \"?\" doubts or alternatives on most lines; the themes can be followed but many sentences are only half "
  "secure: R483 is *decoded, not read*. Class read -> not read, method read from existing decipherment -> not solved "
  "until the text is written out; fraction_read 0.997 -> 0.",
  ["R483 as a running text: decoded, not read - blocker: not-attempted; write the clerk's decipherment and the clear "
   "passages out in reading order from the images (DECODE cookie), settle the doubtful words with the rebuilt key, "
   "translate"],
  ["- [n/a] siblings: no other letter in this key",
   "- [x] clear-pages: the clerk's interlinear decipherment over every ciphered stretch",
   "- [n/a] known-keys: the key is not preserved",
   "- [ ] print: no search for a printed text is recorded in these notes",
   "- [x] key-rebuild: 224 codes rebuilt from the interlinear",
   ESC_RETRY]),
 'ranzo1528': (None,
  H + "letter 4 (fr. 4050) reads at its opening and close, but 54 of its 128 lines carry an open code and in the middle "
  "runs of codes break most sentences: *decoded, not read*. Letters 1, 2, 3 and 5 read. Class read in part kept; "
  "fraction_read 0.929 -> 0.717 (bar-measure tokens of the four letters that read).",
  ["letter 4 (fr. 4050): decoded, not read - blocker: not-attempted; read the codes from context across the five "
   "letters and check them on the Gallica images of fr. 4050 ff. 79-81"],
  None),
 'rome1536': (IP + "Mascon's cipher letters read in part; fr. 3071 no. 4 decoded, not read (reading audit, 22 Oct 2026).",
  H + "R4234 and R4239 (graded C) were re-read on their pass-5 running readings and build French sentences with "
  "scattered holes (overturned to B). The 11 April 1537 letter (fr. 3071 no. 4) is read only 35-40% by its own count "
  "and is *decoded, not read*. fraction_read 0.95 -> about 0.91 (its ~840 signs added to the denominator).",
  ["fr. 3071 no. 4: decoded, not read (35-40% of the cipher) - blocker: not-attempted; re-transcribe f. 9r ll. 3-25 by "
   "sign shape from the Gallica native scan, decode with macon_decode.py, read f. 9v against the slip f. 9bis",
   "R4239 letter 1, f. 35r-v first paragraph, as a running text - blocker: not-attempted; summarised with elisions in "
   "pass5/R4239_pass5.md; write it out from the per-line record"],
  None),
 'rupert': (None,
  H + "the five numeric documents (Maurice 1645, ff. 9, 10, 104, R8433) carried no state in profile.json and so counted "
  "as read by default; each is an undeciphered ciphertext and is now marked *decoded, not read*. Claim unchanged "
  "(fraction_read already counts them at 0).",
  [], None),
 'sabran1633': (None,
  H + "Baluze 156 f. 157r (two crib values only) is marked *decoded, not read* and the two-word f. 218r margin *not "
  "prose* in profile.json. Claim unchanged.",
  [], None),
 'santacruz1399': (None,
  H + "nothing of the letter is in the repository: Puig's print (1920, pp. 469-470) was read on Google Books in "
  "September, which now blocks scripts, and archive.org has no copy. outcome.texts_withheld carries the citation; "
  "class already solved kept.",
  ["Puig's printed text of the letter (pp. 469-470), not in the repository - blocker: needs-physical-access; Google "
   "Books blocks automated access, HathiTrust is behind a Cloudflare challenge, archive.org has no copy"],
  None),
 'segur': (None,
  H + "f. 288v, read with the word-sign values given in reading.md's notes ({gne} = Je, {na} = nouvelles/affaires, "
  "{Ra} = faictes, {qu} = vous), builds French sentences; the date and name signs stay open. Per-document C "
  "overturned to B; claim unchanged.",
  [], None),
 'siena11': (None,
  H + "both cipher blocks of Lasry's decryption build Italian sentences with a translation; the doubts are one sign "
  "lost in a hole and five words of a 393-sign text, both outside blockers. Per-document C overturned to B; claim "
  "unchanged.",
  [], None),
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
