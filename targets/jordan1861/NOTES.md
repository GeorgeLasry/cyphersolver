# Thomas Jordan to "My Dearest Rachel" (Rose Greenhow), 1861: cipher original and clear copy (catalogue 645 and 646)

Status: already solved at the time. Catalogue entries 645 and 646 are one letter: NARA naId 6925618 (646) is the
cipher original, and naId 1634051 images 1-2 (645) are a clerk's clear copy that gives every cipher passage in plain
words. The 1864 Greenhow key reads the 1861 cipher groups unchanged; no new plaintext comes out of it. Contributed by
WAINUT (https://github.com/WAINUTAI), 27 Oct 2026; the work was done with AI language-model agents, and the fragment,
the copy and the key were each read twice, independently, on the NARA images.

## The two items

NARA RG 59, Seized Correspondence of Rose O'Neal Greenhow.

- **naId 1634051** (catalogue 645), file "Letters from Lieutenant Colonel Thomas Jordan to Mrs. Greenhow and to My
  Dearest Rachel", 6 images: <https://catalog.archives.gov/id/1634051>.
  - Images 1-2: a fair copy in a clerk's copperplate of Jordan's letter to "My Dearest Rachel", all in clear, with
    dashes where the original is lost (`contemporary_clear_copy.txt`). None of the six images carries cipher signs.
  - Images 3-5: a different letter, laminated cross-written fragments in plain English ("The South is all alive with
    soldiers ... every woman of all classes is sewing making uniforms ..."). No cipher.
  - Image 6: an envelope "Miss Gertrude L. Greenhow, No 398 16th St, Washington D.C.", docketed "Capt Moore of the
    Union 29 Apl 1861"; it belongs with images 3-5.
  - Who made the clear copy, and when, is not shown on the images. A Federal clerk working on the seized papers is
    plausible; it is not proved.
- **naId 6925618** (catalogue 646), "Copy of a Letter Fragment Partially Written in Cipher", 1 image
  (hd1-135695281-2013-001-ac.jpg): <https://catalog.archives.gov/id/6925618>. A white-on-black photostat of burnt and
  torn fragments pasted on a sheet: clear words with sign groups, cross-written in places.

Every clear phrase on the fragment ("to get for me", "and if to be had conveniently / 8 yards navy flannel (blue)",
"for a", "he", "you", "for the rest to", "me from Alex", "These", "essential to me in my / position as", "of",
"and you will", "by sending") is in the clear copy, in the same order. Under the first cipher group a lighter hand has
written "h a r" letter by letter: a decipherment between the lines on the original itself.

NARA naId 1634050 in the same file is Jordan's covering note "Compliments of Col. Thos. Jordan to Mrs. Greenhow 23d
July 1861 (refers to Manassas)".

## Key

The 1864 Greenhow key, NARA M1091 naId 62017285 **image 0484** ("Lamb Papers CXXIX"; found on Greenhow's body off
Fort Fisher in 1864), as read in `../greenhow1861/key_1864.md`. Image 0483 is a different table and does not apply.
The key was read twice, independently, and the readings agree.

## Transcription and decryption

`transcription.txt` gives the sign groups as shape labels (the labels of `../greenhow1861/`), line by line, with the
clear words. `decryption.txt` gives the key applied line by line, with the clear copy's words at each place.
`decode.py` (output `decode_output.txt`, standard library only) applies the key and compares every sign with the copy.
`ciphertext.txt` holds the 89 signs of the 22 groups read, for the count.

Corrections from the second reading, applied:

- **L1**: the group after "to get for me" is comb, A-sign, psi = HAR (Hardee's), with the gloss "h a r" under it and
  a ":" abbreviation mark after it. The leading O is unexplained (key value J) [?].
- **L9**: the fourth sign is a long s (L), not an 8, so the group reads [SH]OULDER. The first sign is an hourglass-box:
  S, or the sh digraph of the key sheet [?].
- **L3**: the second sign may be an A with a stroke; W is not certain. **L10**: the first sign (A) is not certain.
  **R3**: the first sign, an arch with a dot, fits H (HIM) [?].
- **L5**: the first sign of UMES is an 8 with an extra stroke, read as the struck 8 (U), as in LIEU (R7).
- **L7**: one small star-like stroke between FORTI and FICATION is taken as cross-writing.
- **Doubled letters**: SCOTT (two D-signs) and BOO (two 5s) are written plainly. The 1864 key sheet's rule "2d letter
  itself inverted" is not seen at this resolution: the 1861 practice may have differed, or the photostat hides it.

Unread: L12 (before "handed"), the central strip C1, and R5 (after "for the rest to"). The clear copy has dashes at
L12 and R5.

## Reading

`reading.md`: the fragment as sentences, with the words torn from the original supplied from the clear copy in
brackets.

> ... to get for me HAR[dee's Tacti]CS, [or the n]EW COP[ies of] SCOTT['s Tact]ICS, [also ... vol]UMES [of Ma]HANS
> FIELD FORTIFICATION[s], and if to be had conveniently 8 yards navy flannel (blue) [Indigo ...]ing of [SH]OULDER
> [STR]APS for a LIE[utenant] CO[lonel. ... handed ...] he [will b]RIN[g] ANY you CAN G[et to] [H]IM, ... These
> BOO[ks are] essential to me in my position as LIEU[tenant] COLONEL of IN[fantry] and you will [do me a great favor]
> by sending [them by hand].

Jordan, newly a lieutenant colonel, asks "Rachel" (Greenhow) for Hardee's and Scott's Tactics, Mahan's Field
Fortification, eight yards of navy-blue flannel and shoulder straps for his rank, to be sent by hand ("me from Alexandria" is in a passage with gaps).
On the first page of the copy he says he fears an earlier letter failed to reach her: he had then no access to his
cipher, and a letter "in ordinary cha[racters]" "was intercepted" (the copy has gaps here). The content is domestic,
not intelligence, but it shows the cipher in use between Jordan and Greenhow in 1861 with the key that was found on
her body in 1864.

## Controls (`decode.py`)

| test | secure signs agreeing with the clear copy (of 82) |
|---|---|
| the 1864 key | **82** |
| 20,000 random substitution keys | mean 3.1, best 36 |
| key shifted by 1, 2, 3, 13 letters | 0 each (FORTIFICATION becomes GPSUJGJDBUJPO ...) |
| true key, groups set against the wrong copy words (20,000) | mean 5.5, best 19 |
| whole groups right | 22/22 against a random-key best of 4/22 |

Caveat: the signs were read knowing the copy's text. The key comes from an independent 1864 document, each secure
sign was matched to a key sign by shape, and the doubtful signs are left out of the count, so the bias is limited to
the signs marked [?].

## Earlier solution

- The clear copy naId 1634051 images 1-2 is the decipherment of the time; the "h a r" gloss on the fragment is a
  second, partial one.
- One web search found no printed text of the letter (NARA and SNAC entries, Wikipedia on Thomas Jordan,
  whitehousehistory.org, the Santa Clara exhibit dh.scu.edu item 3281). The Official Records Ser. II vol. 2,
  Fishel and Blackman were not checked.
- Using the 1864 key on 1861 Greenhow material is not new (the Rosenbach's "Code Breaker" blog, 2011, for another note; the North
  Carolina State Archives' "Rebel Rose" blog, 2012).

## Proposed catalogue corrections (entries 645 and 646)

- **Merge 645 and 646, or cross-reference them**: one letter, two NARA items. 6925618 is the cipher original;
  1634051 images 1-2 are its clear copy.
- **646 correspondents**: Thomas Jordan to Rose Greenhow ("Rachel"), not "Rose O'Neal Greenhow to unknown". Place:
  Confederate lines (presumed; Alexandria is named in the letter), not Washington. The fragment has about 89 cipher signs, not
  about 60.
- **645 folio_note**: images 1-2 are a clear copy (decipherment); images 3-5 a different clear cross-written letter;
  image 6 an envelope to Miss Gertrude L. Greenhow docketed "Capt Moore of the Union 29 Apl 1861". No cipher on any
  of the six images.
- **Both**: the key is M1091 image 0484 (photostat 0485), not 0483; it reads the 1861 cipher unchanged.
- Suggested status for both: already solved (contemporary clear copy); key identified; no new plaintext.

## Remaining gaps

- L12, the central strip C1 and R5 of naId 6925618 - blocker: illegible (faint or torn signs; the copy has dashes at
  L12 and R5).
- The dashes of the clear copy - blocker: illegible; the original is torn at these places and the surviving cipher does
  not fill them.

## Escalation

- [x] siblings: Greenhow's mourning-paper letter (`../greenhow1861/`) reads with the same key; Jordan's covering note
  1634050 noted.
- [x] clear-pages: the clear copy 1634051 images 1-2 used; images 3-6 checked and set aside.
- [x] known-keys: the 1864 key (image 0484) fits; image 0483 does not.
- [ ] print: OR Ser. II vol. 2, Fishel and Blackman not checked.
- [n/a] key-rebuild: the key fits unchanged.
- [x] retry: the fragment re-read independently; L1 and L9 corrected from that pass.

## Files

`transcription.txt`, `ciphertext.txt`, `decryption.txt`, `reading.md`, `contemporary_clear_copy.txt`, `decode.py`,
`decode_output.txt`; the key is `../greenhow1861/key_1864.md`. No images are kept here; they are on the NARA
catalogue pages.
