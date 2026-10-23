"""NOTES.md edits for the relabel_docs_0 targets (RELABEL_DOCS_BRIEF.md), 22 Oct 2026. Run once."""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
EARLIER = 'Earlier status (before the 22 Oct 2026 reading audit): '

# folder: (new status line or None, block, [gap lines], escalation lines or None)
T = {
 'adfgvx': (None,
  "**22 Oct 2026, reading audit** (George Lasry's test: can sentences be built and translated?): the nine messages read in "
  "full in 2017 (pp. 100, 105, 109, 132, 146, 171, 176, 187 and its second part) read as German telegrams; the three "
  "partial readings (p. 164 twice, VGADA p. 215) and the ten open messages are *decoded, not read*. The readings table "
  "is now two entries in profile.json, and the claim is read in part: 1,945 of 3,966 letters (49%) in messages that read.",
  ["ten open messages (pp. 73, 152, 153 VFVAX and AXVAA, 158, 170, 176 GGDAA, 189, 198, 217; 1,490 letters) - blocker: "
   "no-key-material; no published period key fits, Lasry's CHI key included; heavier mutilation or an unlisted key needs "
   "the Childs originals",
   "three partly read messages (p. 164 F-G-X, p. 164 VFGAG, VGADA p. 215) - blocker: needs-physical-access; marked "
   "transmission gaps (44, 44, 11 letters) in the printed transcription"],
  ["- [x] siblings: all 22 residue messages tested against the fourteen period keys and Lasry's CHI key (block-edit search)",
   "- [x] clear-pages: none; radio messages",
   "- [x] known-keys: the published period keys (Lasry, Niebel, Kopal, Wacker) and the CHI 13 Nov key",
   "- [x] print: the 2017 Cipherbrain thread consolidated (texts/residue22_decryption.md); no later edition",
   "- [x] key-rebuild: three damaged key squares repaired; no key-free recovery possible at 84-240 letters",
   "- [x] retry: deeper search on p. 132 (deep.py); the ten open messages retried with every key"]),
 'alessandrino1568': ("Status: in progress. Seven of eleven letters read; R94, R95, R100, R101 decoded, not read (reading audit, 22 Oct 2026).",
  "**22 Oct 2026, reading audit** (George Lasry's test): R93, R96, R97, R98, R99, R102 and R115 build Italian sentences "
  "with scattered slips; **R94, R95, R100 and R101 are decoded, not read**: the beam search's digit choices corrupt words "
  "in most of their sentences (R94 \"liberagemptume\", R95 \"desersaleaniosina\", R100 ends in ??????, R101 "
  "\"unmannifestsobismain\"). Claim read -> read in part; 7,036 of 10,555 items (66.7%) in letters that read.",
  ["R94, R95, R100, R101 (3,519 items): decoded, not read - blocker: not-attempted; re-read each against the images and "
   "the DECODE transcription, constraining the digit choices word by word; compare with Serrano 1914"],
  ["- [x] siblings: all eleven Spagna 6/I and 6/II ciphers decoded with the same key",
   "- [ ] clear-pages: contemporary decifrati not looked for",
   "- [x] known-keys: Lasry's reconstructed key (DECODE, 2020)",
   "- [ ] print: Serrano 1914 not reached (HathiTrust 403)",
   "- [ ] key-rebuild: unlisted dotted groups not resolved",
   "- [ ] retry: the four letters above not yet re-read"]),
 'army1902': (None,
  "**22 Oct 2026, reading audit** (George Lasry's test): C09122911500 and C09123116600 read as sentences. C09122909900 is "
  "a twelve-kana noun phrase (\"observation of the naval exercise\"), *not prose*; C03020059400 is a twelve-kana phrase "
  "with two signs off the table whose sense (an anchorage command) is a guess: *decoded, not read*. Claim read -> read in "
  "part, 49 of 73 pairs in telegrams that read.",
  [], None),
 'battier1686': (None,
  "**22 Oct 2026, reading audit** (George Lasry's test): the 4 December 1687 (92L) and 12 February 1688 (100R) cipher "
  "blocks have holes in most sentences and are now *decoded, not read* in profile.json, as the strict screen already said. "
  "fraction_read 55% -> about 49% (estimated; the two letters' 482 tokens no longer count).",
  ["4 Dec 1687 (92L) and 12 Feb 1688 (100R) cipher blocks: decoded, not read - blocker: not-attempted; re-read on the "
   "images against the inv. 1209 key, and check the nearby decipherment sheets"], None),
 'benedict1399': (None,
  "**22 Oct 2026, reading audit** (George Lasry's test): the repository holds only the p. 475 plate check "
  "(src/plate475_check.tsv), which builds Latin clauses; the text of the ten letters is Puig's print (Google Books, blocked "
  "to scripts), not copied here. The entry stays read for the plate only, with an excerpt note; fraction_read (91.4%) is "
  "the plate's sign-confirmed share, not a share of the ten letters.",
  ["Puig's printed text of the ten letters, not in the repository - blocker: needs-physical-access; Google Books blocks "
   "automated access and HathiTrust 100676638 is behind a Cloudflare challenge"], None),
 'bienvenut1590': ("Status: in progress. The letter reads, but only a sample of ff. 35r-v is transcribed (reading audit, 22 Oct 2026).",
  "**22 Oct 2026, reading audit** (George Lasry's test): texts/n23_decryption.md is a sample of about 90 words joined by "
  "\"...\"; it reads, but most of the letter is not in the repository. Claim read -> read in part (about 15%, estimated) "
  "until ff. 35r-v are transcribed; every code is already resolved by the key slip.",
  ["n23, ff. 35r-v beyond the sample: not transcribed - blocker: not-attempted; Gallica btv1b525245007 canvases 79-80 "
   "(copies in the main checkout targets/champagne1590/img/)"],
  ["- [x] siblings: champagne1590 and lauriere1593 split off (other keys)",
   "- [x] clear-pages: the letter is itself a clear copy; key slip f. 36r",
   "- [x] known-keys: the key slip resolves all 26 codes",
   "- [x] print: none found",
   "- [n/a] key-rebuild: key complete",
   "- [ ] retry: full transcription of ff. 35r-v still to do"]),
 'bilia1527': (None,
  "**22 Oct 2026, reading audit:** the f. 102v entry is *decoded, not read* in profile.json (raw decoder lines with no "
  "continuous sense), as the status above says; fraction_read already counted it as unread.",
  [], None),
 'bizozola1520': (None,
  "**22 Oct 2026, reading audit** (George Lasry's test): the per-document grade C was overturned to B. reading_raw.txt is "
  "raw line-by-line output with the key's homophone slips (a/u, e/p), but read through, nearly every line builds Italian "
  "sense; the open stretches are those in doubtful.txt and the date line. A normalised Italian text and an English "
  "translation are still to be written.",
  [], None),
 'bonzagni1512': ("Status: in progress. Read at the time, but none of the three contemporary decipherments is transcribed here (reading audit, 22 Oct 2026).",
  "**22 Oct 2026, reading audit** (George Lasry's test): no text of R1123, R1124 or R1125 is in the repository; the "
  "decipherments are on the DECODE images only (main checkout `img/`). All three are *decoded, not read* in profile.json; "
  "class already solved -> not read and method -> not solved until the decipherments are transcribed. The verdict below "
  "(read at the time) stands as history, not as a reading held here.",
  ["R1123, R1124, R1125: the contemporary decipherments, not transcribed - blocker: not-attempted; images in the main "
   "checkout targets/bonzagni1512/img/ (interlinear glosses R1123 pp. 1-2, R1124 p. 1; the R1125 slip, image 5)"],
  ["- [x] siblings: Bonzagni's file in ASMo Ambasciatori Ungheria b. 4 listed from Vestigia (46 items)",
   "- [x] clear-pages: interlinear decipherments on R1123/R1124 and the R1125 slip found; not transcribed",
   "- [n/a] known-keys: not needed, the decipherments exist",
   "- [ ] print: not searched",
   "- [n/a] key-rebuild: not needed",
   "- [ ] retry: transcription of the decipherments still to do"]),
 'breves1603': (None,
  "**22 Oct 2026, reading audit** (George Lasry's test): the three letters printed in full by Berger (ff. 60, 63, 66) "
  "read. The entry for the nine further letters is *decoded, not read*: berger/table_pp667-682.txt holds Berger's "
  "summaries, not the letters; their full clear text is in fr. 4029 (not digitised).",
  ["the nine further letters of 1603 (fr. 3541 ff. 69-104): only Berger's summaries in the repository - blocker: "
   "needs-physical-access; full clear text in BnF fr. 4029 ff. 118-128, ciphertext in fr. 3541; neither is digitised"],
  ["- [x] siblings: the twelve 1603 letters listed (fr. 3541); Tomokiyo's partial reading of f. 60 used as a check",
   "- [x] clear-pages: second clear copy found in BnF fr. 4029 (not digitised)",
   "- [x] known-keys: office key located in BnF fr. 3462 f. 103",
   "- [x] print: Berger de Xivrey, Lettres missives VI (3 letters in full, 9 in summary)",
   "- [n/a] key-rebuild: key survives",
   "- [ ] retry: blocked until fr. 3541 or fr. 4029 can be seen"]),
 'brulart1615': ("Status: in progress. No plaintext of either letter is in the repository or on Tomokiyo's page (reading audit, 22 Oct 2026).",
  "**22 Oct 2026, reading audit** (George Lasry's test): Tomokiyo's key is on both DECODE records, but his page gives the "
  "key and remarks on undeciphered symbols, not the letters, and nothing of either letter is transcribed here. Both are "
  "*decoded, not read*; class already solved -> not read, method -> not solved. The R2785 page image shows contemporary "
  "decipherments over most cipher runs, so the letters are workable with his key.",
  ["R2785 and R2786: no plaintext in the repository - blocker: not-attempted; fetch the three pages of each record with "
   "the DECODE cookie, transcribe R2785's interlinear decipherments, apply Tomokiyo's key (DOC_2785/2786 png)"], None),
 'charles1536': ("Status: in progress. Neither letter's text is in the repository (reading audit, 22 Oct 2026).",
  "**22 Oct 2026, reading audit** (George Lasry's test): R9957 is here only as fragments of its contemporary decipherment "
  "(pp. 17-18; Luo's 2021 print not copied) and R9952 has no text at all; both are *decoded, not read*. Class already "
  "solved is kept because R9957 is in print (Luo 2021, p. 287).",
  ["R9957: Luo's printed decipherment (2021, p. 287) not in the repository - blocker: not-attempted; the thesis is on "
   "RODERIC (Universitat de Valencia); the pp. 17-18 contemporary decipherment is on the images (main checkout img/)",
   "R9952: contemporary decipherment (margins of ff. 10-12, full on ff. 13-14) not transcribed - blocker: not-attempted; "
   "images in the main checkout targets/charles1536/img/r9952_p*.jpg"],
  ["- [x] siblings: R9952 and R9957 separated (two unrelated letters)",
   "- [x] clear-pages: R9957 pp. 16-18 glosses and decipherment found; R9952 ff. 10-14 decipherment found",
   "- [x] known-keys: Luo's key AGS Estado leg. 1.1.1 doc. 169 identified",
   "- [x] print: Luo 2021 p. 287 (R9957)",
   "- [ ] key-rebuild: crib alignment on pp. 16-17 did not converge",
   "- [ ] retry: copy Luo's text, transcribe R9952 ff. 13-14"]),
 'chomentowski1713': (None,
  "**22 Oct 2026, reading audit:** the per-document grade C on R7484-R7485 was overturned to A: R7484 reads with "
  "scattered holes, and in R7485 the cipher passage reads in full; its holes are in the faint clear body, and pp. 116-117 "
  "are clear text, not cipher.",
  [], None),
 'cifuentes1534': ("Status: in progress. Read at the time, but the f. 54 decipherment is not transcribed here (reading audit, 22 Oct 2026).",
  "**22 Oct 2026, reading audit** (George Lasry's test): no text of R9963 is in the repository beyond the fragments quoted "
  "below; it is *decoded, not read* in profile.json, class already solved -> not read and method -> not solved until f. 54 "
  "is transcribed. The verdict below stands as history.",
  ["R9963: the contemporary decipherment on f. 54, not transcribed - blocker: not-attempted; image 5 in the main checkout "
   "targets/cifuentes1534/decode/"],
  ["- [n/a] siblings: one letter",
   "- [x] clear-pages: decipherment bound as f. 54 found; not transcribed",
   "- [n/a] known-keys: not needed",
   "- [x] print: not in Tomokiyo's AGS Estado page",
   "- [n/a] key-rebuild: not needed",
   "- [ ] retry: transcription of f. 54 still to do"]),
 'clair357': ("Status: in progress. f. 168r (the clear copy) reads; the f. 167 interlinear part is decoded, not read (reading audit, 22 Oct 2026).",
  "**22 Oct 2026, reading audit** (George Lasry's test): the f. 168r clear copy of f. 167r ll. 1-30 builds sentences; the "
  "interlinear decipherment after the cross mark (f. 167r) and on f. 167v is transcribed only as fragments, with holes in "
  "most sentences: *decoded, not read*. The entry is split in two in profile.json; claim read -> read in part (about half, "
  "estimated).",
  ["f. 167r after the cross mark and f. 167v: interlinear decipherment read only in fragments - blocker: not-attempted; "
   "read the glosses word by word at full resolution (canvases 331-332) and decode unglossed figures with the table"],
  ["- [x] siblings: none found in Clair. 357 round ff. 167-168",
   "- [x] clear-pages: f. 168r clear copy and the f. 167 interlinear found",
   "- [x] known-keys: Tomokiyo's partial table, checked and extended",
   "- [x] print: none found",
   "- [ ] key-rebuild: word-by-word decoding of the cipher done on sample runs only",
   "- [ ] retry: the verso glosses not yet read word by word"]),
 'comuel1415': (None,
  "**22 Oct 2026, reading audit:** nothing of the letter is in the repository (the Google Books link returns 403 to "
  "scripts), so the entry is *decoded, not read* in profile.json; class already solved is kept because the text is in "
  "print (Puig 1920).",
  ["Puig's printed text (pp. 562-563), not in the repository - blocker: needs-physical-access; Google Books blocks "
   "automated access, HathiTrust 100676638 is behind Cloudflare"], None),
 'comuel1416': (None,
  "**22 Oct 2026, reading audit:** nothing of the letter is in the repository (the Google Books link returns 403 to "
  "scripts), so the entry is *decoded, not read* in profile.json; class already solved is kept because the text is in "
  "print (Puig 1920).",
  ["Puig's printed text (pp. 578-579), not in the repository - blocker: needs-physical-access; Google Books blocks "
   "automated access, HathiTrust 100676638 is behind Cloudflare"], None),
 'deswart1782': ("Status: in progress. not read (reading audit, 22 Oct 2026: R1036 and R1040 decoded, not read).",
  "**22 Oct 2026, reading audit** (George Lasry's test): R1036_machine_decipherment.txt and "
  "R1040_second_key_machine_decipherment.txt split words into letters and carry bracketed codes and query marks in nearly "
  "every line; the topic follows, the sentences do not. Both are *decoded, not read*; class read in part -> not read, "
  "method -> not solved, fraction_read 96.7% -> 0 (the share of groups given a value is withdrawn as a reading figure). The "
  "R1038 key match stands, and the normalised Greek-project passage below reads.",
  ["R1036: machine decipherment not yet built into sentences - blocker: not-attempted; apply the 30 Sept corrections "
   "(leading dash, 47^_ = k, key misreadings) to decode_1765.py, regenerate, normalise line by line",
   "R1040 second part: machine decipherment not yet built into sentences - blocker: not-attempted; context pass on its own "
   "unread groups, then a normalised reading"], None),
 'dubellay': ("Status: in progress. The 22 Oct 1529 opening is in print but not in the repository, and its leaf is reachable (reading audit, 22 Oct 2026).",
  "**22 Oct 2026, reading audit** (George Lasry's test): the 22 Oct 1529 entry is *decoded, not read*: the repository has "
  "only Le Grand's clear part; the ciphered opening is Scheurer's (Google Books snippets). The leaf fr. 3005 f. 165 is now "
  "reachable through the Gallica IIIF, so the opening can be deciphered here with the 1529 key.",
  ["22 Oct 1529 opening (fr. 3005 f. 165), not in the repository - blocker: not-attempted; fetch the leaf through the "
   "Gallica IIIF (openapi.bnf.fr), decipher with key_p21.tsv, compare with Scheurer's snippets"], None),
 'egmond': (None,
  "**22 Oct 2026, reading audit:** the ciphered address (three lines, \"A mon bon cousin / Monsieur le grant maistre / "
  "de France\") is *not prose* in profile.json; the letter body reads.",
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
    # insert after the first Status: line if any (and its paragraph), else after the title
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
