"""v6: append the spelling-restoration solution step to each folder's profile (via v6.py) from the before/after scores.
    python v6_steps.py <before.txt> <after.txt> <outdir>"""
import json, re, subprocess, sys, pathlib, collections
B, A, OUT = sys.argv[1:4]
ROOT = pathlib.Path(__file__).resolve().parents[2]
def load(f):
    d = {}
    for l in open(f, encoding='utf8'):
        m = re.match(r'(\S+): plain ([0-9.]+) .*explicit holes ([0-9.]+)', l)
        if m: d[m.group(1)] = (m.group(2), m.group(3))
    return d
b, a = load(B), load(A)
WHAT = {
 'carpio1677': ("plaintext matching", "the modernised spelling of 22 Oct restored to the writer's, word by word from the contemporary margin decipherments as transcribed (read/R*_margin.txt; research/reading_audit/v6_align.py), editorial accents off, words the margin does not carry spelt as the key decode gives them; abbreviations and code words written out; holes and brackets kept, no word changed (R1006 left to the agent working on it)"),
 'ronquillo1676': ("plaintext matching", "the modernised spelling of 22 Oct restored to the cipher's, letter by letter from the key decode streams (read2/R*.txt; research/reading_audit/v6_charalign.py: the stream's letters taken where they spell the same word another way, e.g. tomavan, assi, devia, aora, quando, haver; editorial accents off; ñ kept where the key writes n); no margin transcription file was kept by the 22 Oct batch, so the key's letters, which are the writer's, are the source; holes and brackets kept, no word changed"),
 'smith1562': ("plaintext matching", "the modernised spelling of 22 Oct restored: nos. 01, 03, 04, 05, 19, 20 word by word from the OCR of Forbes, A Full View ii (1741), which prints the originals' spelling (v6_align.py --ocr: long s, recurrence check, OCR slips refused by hand); nos. 06, 08, 11, 15, 16, 17, 22 by hand from the figures' spellings recorded in no01-no23_reread_log.md, decipher_*.md and the corrections tsv (kepe, terme, sonnes, hote, bel awaye, hir, ernest, congratulacion, condoleaunce, intervewe, forain realmes, dispach, unserched, lokes, Scotish, speake, Secretarie, feate, somwhat, tyme, necessarie); no. 18 has nothing to restore (names and code signs); holes and brackets kept, no word changed"),
 'wotton1585': ("plaintext matching", "the modernised spelling of 22 Oct restored to Wotton's, word by word from his own drafts as transcribed (texts/R484x_transcription.txt, struck words dropped, interlined taken in; v6_align.py), abbreviations written out; holes and brackets kept, no word changed"),
 'walsingham1585': ("manual reconstruction", "reading_R4840.txt and reading_R4844_r2.txt ('spelling modernised in part'): DECODE images fetched again with the project cookie (research/reading_audit/v6_fetch.py, scratchpad only) and re-read in strips; the words whose letters are clear in the secretary hand respelt as written (dothe, complayne, wrytten, frende, knowe, countenaunce, yf, woold, ioyne, wyll, realme, iudge, then for than, Coorte, hathe bread, lykinge, doe bothe allowe of yt, untill, ben unmindfull, commyt ...); uncertain words keep the earlier form; no hole filled, no word changed"),
 'harley7001': ("plaintext matching", "reading.txt ('spelling modernised lightly') checked against the key decode of ct.txt: the cipher's spelling (goe, refusall, preuent) is kept; 'prevent' restored to 'preuent', the only word the light modernisation had changed; code groups keep the key's word"),
 'r2232': ("plaintext matching", "reading.txt / reading.md ('spelling modernised lightly') aligned with decrypt_raw.txt: the writer's enciphered forms serai, aurai (for serais, aurais), expédie and voye restored; accents and apostrophes, which the cipher cannot carry, stay supplied; slips stay corrected as noted; clear text as transcribed"),
 'rakoczi1707': ("plaintext matching", "R902_reading.md ('spelling is normalised') aligned letter by letter with the decode (measure_tr.py --text; v6_charalign.py --keep-accents --keep-uv-ij): aussÿ, arrete(z), relaché, naitre, interets, incroiable, afermie, Luben, Stetin restored; accents and u/v, i/j as before; no word changed"),
 'turculet1709': ("plaintext matching", "R7482_reading.txt ('normalised spelling') put back into the writer's Latin from R7482.txt (figures and interlinear gloss): hæc, quæcunque (the clear &/æ sign), occurunt, expectat, Tarlo, Soczaviæ; no word changed. R7481_reading.txt ('modernised Polish') is not in the v6 list and was not touched"),
 'esp318no94': ("plaintext matching", "no94_partial_reading.md (Brackx's normalised spelling) aligned letter by letter with his decipherment's P: lines (no94_decryption.md; v6_charalign.py): editorial accents off, Puertocarero, canpo, elecion, Ugo, ANYMA, QUISSO as the clerk's clear text and the key letters give them; code words keep his labels; no word changed"),
 'throck1569': ("other", "reading.md header checked for modernised spelling (v6): it keeps the cipher's and the clear text's own spelling and modernises only a cipher word whose spelling cannot be read; nothing to restore (false hit)"),
}
files = collections.defaultdict(list)
for f in a:
    files[f.split('/')[1]].append(f)
out = pathlib.Path(OUT); out.mkdir(parents=True, exist_ok=True)
for T, (tech, what) in WHAT.items():
    sc = []
    for f in sorted(files[T]):
        if 'R1006' in f: continue
        (p0, h0), (p1, h1) = b[f], a[f]
        sc.append(f"{f.split('/', 2)[2]} plain {p0} -> {p1}, explicit holes {h0} -> {h1}")
    text = (f"v6 spelling check (23 Oct 2026, research/reading_audit/v6_spelling_files.txt): {what}. Rescored with "
            f"research/reading_audit/v2_score.py: " + '; '.join(sc) + ". The plain share falls with period spelling against a "
            "modern word list; the explicit-hole share, the bar for period spelling, is unchanged or the change comes from the "
            "new header lines in files without a '## Reading' heading. No state changes.")
    step = dict(date='2026-10-23', kind='control' if T == 'throck1569' else 'reading', technique=[tech], what=text,
                result='partial' if T == 'walsingham1585' else 'worked')
    pth = out / f'{T}.json'
    pth.write_text(json.dumps({'steps': [step]}, ensure_ascii=False, indent=1), encoding='utf8')
    print(T, len(text))
