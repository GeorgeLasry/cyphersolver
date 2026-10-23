"""NOTES.md edits for the relabel_docs_3 targets (RELABEL_DOCS_BRIEF.md), 22 Oct 2026. Run once.

Same edit() as relabel_docs_2_notes.py, with this batch's table.
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
EARLIER = 'Earlier status (before the 22 Oct 2026 reading audit): '
IP = 'Status: in progress. '
H = "**22 Oct 2026, reading audit** (George Lasry's test: can sentences be built and translated?): "
COOKIE = "the shared DECODE cookie (targets/bordeaux/decode/cookie.txt)"

ESC_RETRY = "- [ ] retry: the re-reading named in Remaining gaps is not done yet"


def sp106(rec, old):
    return (IP + "Lasry's decipherment exists on DECODE; none of it is in the repository (reading audit, 22 Oct 2026).",
            H + "Lasry's plaintext of " + rec + " is on the DECODE record only; the git-ignored copy is in no checkout, so "
            "nothing of the letter could be read. " + rec + " is *decoded, not read* in profile.json; class already solved "
            "is kept (his decipherment exists), fraction_read " + old + " -> 0 (the old figure was key coverage).",
            [rec + ": Lasry's plaintext not in the repository - blocker: not-attempted; fetch his interlinear and plaintext "
             "files with " + COOKIE + " (git-ignored, his work), grade them as sentences, and ask him whether a reading "
             "copy may be kept"],
            None)


# folder: (new status line or None, block, [gap lines], escalation lines or None)
T = {
 'soglia1848': (None,
  H + "texts/plaintext.md builds Italian sentences throughout and its English translates every sentence; the holes are "
  "the date of the earlier letter (five code groups), Lützow's title [8227] and four single code words. The per-document "
  "C is overturned to B. Claim unchanged.",
  [], None),
 'soria1523': (None,
  H + "R9491 and R9494-96 were graded C on the superseded files read_r9491_b.md and read_r9494.md. The 5 Oct 2026 "
  "measured readings (measure/kb_r9491.txt, measure/kb_r9494.txt) build sentences in both letters with single key-B code "
  "groups open, so both per-document grades are overturned to B. Claim unchanged.",
  [], None),
 'soria1527': (IP + "The Claro reads for section A and the closing paragraph; B and C are torn (reading audit, 22 Oct 2026).",
  H + "claro.md builds sentences for section A and the closing paragraph only; B and the start of C are half-lines on a "
  "torn leaf. R9487 is *decoded, not read* in profile.json; class already solved is kept (read at the time); "
  "fraction_read estimated 0.5. The f. 31v cipher block is intact and could fill the tear with key B.",
  ["Claro B and the start of C (torn): decoded, not read - blocker: not-attempted; transcribe the intact f. 31v cipher "
   "block from the DECODE images (decode/, reachable with " + COOKIE + ") and decode it with key B "
   "(targets/soria1523/keyB.md)",
   "last cipher lines of f. 31r and f. 33r - blocker: illegible; torn and faded"],
  ["- [x] siblings: soria1523 (key B) used to check the Claro against the cipher",
   "- [x] clear-pages: the Claro, f. 34r, transcribed in claro.md",
   "- [x] known-keys: Soria's 1523 key B fits (spot checks on A and C)",
   "- [ ] print: not searched",
   "- [n/a] key-rebuild: key B exists",
   ESC_RETRY]),
 'sp106r787': sp106('R787', '0.9802'),
 'sp106r924': sp106('R924', '0.9195'),
 'sp106r929': sp106('R929', '0.842'),
 'sp106r927': (None,
  H + "the f. 242 entry is the same leaf as f. 243 photographed with the flap down; about half its lines are holes or "
  "restored from f. 243. It is now *not prose* in profile.json (a transcription check, not a text); it was already "
  "reported apart from fraction_read. Claim unchanged.",
  [], None),
 'stowe166': (None,
  H + "R7773 (\"that his faith is not vendible\") and R7775 (one line on the enterprise upon Reims) were graded C as "
  "fragments. Each is a single cipher clause inside a clear despatch and reads in full (R7775 with the person sign {£2} "
  "open), so the grades are overturned (A, B). Claim unchanged.",
  [], None),
 'swieten1759': (IP + "R956 reads; R957 decoded, not read (reading audit, 22 Oct 2026).",
  H + "R956 builds French sentences with scattered name groups open. R957 does not: \"On promet (?) de toujours de la "
  "part des François\" fails and \"le prince de Con[...] [323 441] qui vous formez des prétensions\" is garbled, so half "
  "its sentences have holes; R957 is *decoded, not read*. Class read -> read in part; fraction_read 0.962 -> 0.597 "
  "(estimated: tokens in R956). Both readings are excerpts: the cipher runs in full, the clear text around them in "
  "extract.",
  ["R957 runs 2 and 4 (\"On promet ... François\"; \"le prince de Con[...] ... qui vous formez des prétensions\"): "
   "decoded, not read - blocker: not-attempted; re-read on the scans against the alphabetical table and the clear text"],
  None),
 'urquhart': (None,
  H + "the distich entry in profile.json carried no state; it is now *decoded, not read* with the note \"not "
  "deciphered\" (outcome.parts already had it not solved). Claim unchanged: the octastich reads.",
  [], None),
 'vargas1552': (IP + "Deciphered at the time per Tomokiyo; nothing transcribed here (reading audit, 22 Oct 2026).",
  H + "no transcription or decipherment of R9967 is in the repository; the marginal decipherment is on the DECODE images "
  "only. R9967 is *decoded, not read* in profile.json; class already solved is kept (deciphered in the margin, "
  "Tomokiyo).",
  ["R9967: the marginal decipherment, not transcribed - blocker: not-attempted; DECODE R9967 images (16 pp.) reachable "
   "with " + COOKIE + "; fetch, transcribe the margins and check them with the Imperial Cipher of 1544-1554"],
  ["- [x] siblings: Juan de Vega R9964 uses the same Imperial Cipher of 1544-1554 (Tomokiyo)",
   "- [ ] clear-pages: the marginal decipherment on the DECODE images not fetched",
   "- [x] known-keys: the Imperial Cipher of 1544-1554 identified by Tomokiyo",
   "- [ ] print: not searched",
   "- [n/a] key-rebuild: the key is known",
   ESC_RETRY]),
 'walsingham1581': (IP + "Only the published opening clause is in the repository (reading audit, 22 Oct 2026).",
  H + "the folder holds the numeric ciphertext and the one-clause opening Tomokiyo published; the Biermann-Lasry "
  "plaintext is unpublished. no. 50I is *decoded, not read* (excerpt only) in profile.json; class already solved is kept; "
  "fraction_read 0.09 marked estimated.",
  ["no. 50I beyond the published opening: decoded, not read - blocker: not-attempted; Tomokiyo's glyph key "
   "(mary_sp53_11_50b.png) and the f. 138 image (DECODE R3839, reachable with " + COOKIE + ") are available; build the "
   "glyph-to-label concordance and apply the key, or ask Lasry for the plaintext"],
  ["- [x] siblings: SP 53/11 no. 35 (Somer's worksheet) and the SP 53/23 keys checked; other alphabets",
   "- [n/a] clear-pages: none with the enclosure",
   "- [x] known-keys: the Castelnau and Mary-Beaton tables do not fit; Tomokiyo's 2026 glyph key does",
   "- [x] print: Tomokiyo, cryptiana mary3.htm (16 Sept 2026)",
   "- [ ] key-rebuild: glyph-to-label concordance not built",
   ESC_RETRY]),
 'warsaw': (None,
  H + "the word-divided text in plaintext.txt is two long sentences and both build and translate; the holes are title "
  "and function-word codes with no key material and the object of the request ([223] [159]). The per-document C is "
  "overturned to B; the filled-in conjectural version is not used. Claim unchanged.",
  [], None),
 'windischgraetz1721': (IP + "R5029 decrypted with Mírka's key, not yet read as sentences (reading audit, 22 Oct 2026).",
  H + "dec.txt: p2 and p3L build sentences, but p3R, p4L and p4R have open codes, «?» guesses and elided clear text "
  "(\"Casse(?) ...\", \"durchschnid ... «102» ...\") in most clauses, so about half the sentences do not build: R5029 is "
  "*decoded, not read*. Class read in part -> not read, method -> not solved, fraction_read 0.856 -> 0. Mírka's key and "
  "the decryption of every letter-spelled passage stand.",
  ["R5029 as a running text (p3R, p4L, p4R, p5L): decoded, not read - blocker: not-attempted; transcribe the clear text "
   "around the cipher passages in full from the DECODE images and write a running German text with a translation"],
  None),
 'wotton1585': (IP + "The three drafts are not transcribed in the repository (reading audit, 22 Oct 2026).",
  H + "the repository holds only summaries of R4841-R4843 and the code table (texts/key.md); no draft is transcribed. "
  "Each image was checked (main checkout decode/s484x_1.jpg): all three are clear English drafts with numeric name codes. "
  "All three are *decoded, not read* in profile.json; class read -> not read, method -> not solved, fraction_read "
  "unknown -> 0. The code identifications stand.",
  ["R4841, R4842, R4843: the drafts, not transcribed - blocker: not-attempted; the DECODE images (4 pp. each) are in the "
   "main checkout targets/wotton1585/decode/ and reachable with " + COOKIE + "; transcribe them with the code numbers "
   "marked"],
  ["- [x] siblings: Walsingham's side (walsingham1585, R4838-R4840, R4844) checked",
   "- [x] clear-pages: the drafts are clear text; not transcribed",
   "- [x] known-keys: CSP Scotland viii glosses 19, 39, 40, 24",
   "- [x] print: CSP Scotland viii calendars the despatches (no. 106 for 1 Sep)",
   "- [n/a] key-rebuild: no cipher",
   ESC_RETRY]),
 'visconti1528': (None,
  H + "final.md's Full text read: the recto builds the council narrative sentence by sentence with holes at r07, r09 "
  "and the r10-12 pairs; the verso translates with v03 illegible and single signs open. The per-document C is "
  "overturned to B; the class read in part (93.3%, below the bar) is unchanged.",
  [], None),
 'visconti1529': (None,
  H + "fr. 3045 f. 28 was graded C on the \"Italian text\" section of fr3045_f28_final.md, which predates the push pass. "
  "With the push-pass readings (l.5 \"come batale perduta\", l.20 \"obstante\", l.2 \"lui\") the letter builds sentences; "
  "one clause (l.12-15) and the l.18 place name stay open besides the keyless codes. Per-document C overturned to B. "
  "Claim unchanged. The running Italian text in that file should be rewritten with the push-pass readings.",
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
