import re
import csv
import textwrap
from collections import Counter
from difflib import SequenceMatcher
from pathlib import Path


ROOT = Path(__file__).resolve().parent
KEY_TXT = ROOT / "R1038_key_transcription.txt"

# Entries that the R1038 transcriber left illegible but which are determined by
# repeated grammatical contexts in R1036. Brackets flag editorial expansion or
# an inflection that varies with context.
R1036_INFERRED = {
    "7": "te",
    "25^_": "ie",
    "27^_": "ig",
    "57": "volgen",
    "77": "een",
    "104^_": "ig",
    "114^_": "ing[en]",
    "118^^": "missive",
    "236^_": "zich",
    "242^_": "van",
    "311^_": "land",
    "340^_": "mar",
    "370^_": "oorlogend",
    "404^_": "lijk",
    "445^_": "Keizer",
    "462^\"": "acte",
    "521^_": "Keizerin",
    "673^\"": "propositie",
    "689^\"": "conven",
    "715": "beid",
    "737^o": "bewuste",
    "810": "Groot",
    "833^^": "[ge]sloten",
    "881": "nje",
    "924": "het",
    "952^_": "onder",
    # second pass (2026-09-21), each value fits every occurrence in R1036
    "2": "een",
    "3^o": "stel",
    "39": "hun",
    "176^^": "mpli",
    "363^o": "tusschen",
    "410^_": "zij",
    "681^_": "mogendheden",
    "724": "welgeval",
    "741": "haar",
}

# Entries DECODE's R1038 transcription left <IL> or mislabelled, read directly from the codebook scans
# (third pass, 2026-09-21) and checked against their R1036 contexts.
R1038_IMAGE_READINGS = {
    "781": "geheel",
    "734": "goed",
    "714": "gemeen",
    "217": "explic",
    "749^\"": "communiceeren",
    "748^\"": "commercie",
    "528^\"": "confidentie",
    "147^\"": "appuyeeren",
    "284^\"": "hooge geallieerde",
    "927": "hoewel",
    "75^_": "het",
    "488^_": "Zijne Keizerlijke Majesteit",
    "496^_": "meer",
    "489^_": "main",
    "454^_": "Koninklijke Hoogheid",
    "412^_": "Zijne Majesteit",
    "346^_": "melden",
    "567^_": "maniere",
    "979^_": "misschien",
    "754^_": "moe",
    "793^_": "occupe",
    "871^_": "offres",
    "877^_": "ond",
    "941^_": "obtineeren",
    "476^^": "representatie",
    "352^^": "ontdekken",
    "127^^": "onthaal",
    "229^^": "overzulks",
    "174^^": "plaats",
    "975^^": "secours",
    "927^^": "stellen",
    "856^^": "subject",
    "81^o": "stil",
    "161^o": "succes",
    "515^o": "twaalf",
    "607^o": "U HoogEdelGestrenge",
    "601^o": "vrouw",
    "644^o": "vijf",
    "675^o": "vrijheid",
    "218^CircleWithHorizontalBar": "zwaar",
    "640^CircleWithHorizontalBar": "Russisch",
}


# Corrections of 30 Sept 2026 (NOTES.md, "The Emperor and the Greek project"), applied 23 Oct 2026 (b19 re-read):
# key entries re-read on the R1038 scans (the word stands LEFT of its code) or fixed by the entry's alphabetical place
# and every R1036 context. Grades M (uncertain) are kept out of the decoder and only bracketed in the reading.
R1036_SEPT30 = {
    "54^\"": "alhoewel",
    "314^\"": "behalven",
    "941^_": "observeeren",
    "47^_": "k",
    "327": "el",
    "92^_": "houden",
    "121": "die",
    "862^^": "het",
    "448^\"": "con",
    "223^o": "veele",
    "743": "dat",
    "853^_": "niet",
    "559": "gehad",
    "80": "eeren",
    "135^CircleWithHorizontalBar": "zoek",
    "191": "ens",
    "299": "favoriet",
    "231^o": "verder",
    # b19 (23 Oct 2026): R1038_scan_readings.tsv "high" readings that fit their only R1036 context
    "52^o": "sedert eenigen",
    "71^\"": "appuyeeren",
}

# b19 (23 Oct 2026), context pass on R1040 part 2 (1765-key segment): each value fits every occurrence in R1040 part 2
# and in R1036 (b19_kwic.py; R1040_part2_reread_log.md has the contexts). DECODE left all of them <IL> or misread.
R1040_B19 = {
    "34^_": "in",            # 94x: in(dicien), in het zekere, waar in, in den jaare, in Europa, (in)vlood, main-t-in-eeren
    "21^^": "of",            # 32x: een plan of project, meer of minder, vyf of zes, of ook, of op eenige andere wyze
    "78": "eenen",           # 25x after w: het hof van W-eenen (Vienna); once after h (token 2369, probably w misread)
    "15^_": "het hof van",   # 22x before W[eenen] or Frankrijk: dat/met/by/van het hof van Weenen/Frankrijk
    "81^_": "honderd",       # 12x: zeventien honderd vyf en tachtig; negen honderd man per regiment
    "343^_": "me",           # bequaame, geheime, pour la Me-diterranee; R1036 meest overeenkomstig, mari-ti-me acte, menins
    "341^_": "mari",         # de marine (3x), R1036 maritime acte
    "495^_": "mede",         # daarmede, waarmede, mede(deel)en, rapport mede voorgesteld
    "800^_": "omstandigheden",  # veele andere omstandigheden, tyds omstandigheden (2x), embarrassante omstandigheden
    "108^_": "il",           # voorgedetailleerde (2x), Maximiliaan (3x), verspillingen, brillanten
    "152^\"": "at",          # legationsraad, attribueeren, geattribueerd, iteratif
    "339^_": "man",          # Rumanzow (3x incl. R1036), manqueeren, negen honderd man, geldmangel
    "261^_": "im",           # Maximiliaan, animositeit, geheim, geanimeerd, important, glimpige
    "617^\"": "courier",     # de voorgemelde courier van Weenen, een courier van hier over Berlyn; R1036 2x (scan: "Cou...")
    "3^_": "hoe",            # in hoe verre (3x), hoe zeer
    "154^o": "stel",         # werkstellig maaken (3x), tegenoverstellingen
    "141^_": "heden",        # zwaarigheden, bedenkelykheden, doorluchtigheden, -igheden
    "178": "eerst",          # het eerste moment; R1038 scan reading "eerst" (high)
    "38^_": "onderrigt",     # in het zekere onderrigt dat; zal direct onderrigt wezen (3x)
    "28^_": "ig",            # zwaarigheid (5x), doorluchtigheid (5x), werkstellig, afkeerig, toelaatigheid, magtig
    "161": "t",              # DECODE "ta": Duytsche (4x), bekent, zoekt, text, triple, maintineeren, aarts, gedeelt
    "801^\"": "deel",        # DECODE "dut": oordeel, gedeelte, voordeel, mededeelen (10x R1040, 1x R1036)
    "777^_": "niet",         # DECODE "nict?": 15x
    "227^\"": "atie",        # DECODE "atic?": associatie, proclamatie, situatie, operatie (18x, R1036 educatie)
    "689": "formeeren",      # DECODE "formeean?": een haak/alliantie/associatie formeeren (4x)
    "316^\"": "belang",      # DECODE "become?": zyne andere belangen, hun belang, de belangen en vue; R1036 hun belang
    "213^o": "twee",         # 12x: den Hertog van Tweebruggen (Zweibruecken, 6x), Paltz Tweebruggen, voor twee jaar,
                             # meer als twee vyfde, twee Esquadres
    "922": "Hertog",         # 21x: den heer Hertog van Tweebruggen, by/met den Hertog, de Minister van den Hertog,
                             # het Hertoglyke hof, den aartshertog Fransek van Toscaanen
}


def load_key(path=KEY_TXT):
    key = {}
    conflicts = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        match = re.match(r"^\s*([^#<].*?)\s+-\s+(.*?)\s*$", line)
        if not match:
            continue
        left, value = match.groups()
        if not re.fullmatch(r"[0-9A-Za-z^\"_|?]+", left.replace("CircleWithHorizontalBar", "")):
            continue
        for code in left.split("|"):
            code = code.strip()
            if not re.fullmatch(r"\d+(?:\^\"|\^_|\^\^|\^o|\^CircleWithHorizontalBar)?", code):
                continue
            if code in key and key[code] != value:
                conflicts.setdefault(code, {key[code]}).add(value)
                if key[code] in {"<IL>", "<EMPTY>", "<EMMPTY>"} and value not in {"<IL>", "<EMPTY>", "<EMMPTY>"}:
                    key[code] = value
            else:
                key[code] = value
    return key, conflicts


def normalize_group(raw):
    # ",^_ 4 5 1": the "^_" DECODE puts after a comma is a dash written after the previous group, not a mark on this
    # one (checked on the images, 30 Sept 2026); drop it before reading the group's own marks.
    raw = re.sub(r"^\s*\^_\s+", "", raw)
    digits = "".join(re.findall(r"\d", raw))
    if not digits:
        return None
    if "^+" in raw:
        suffix = "^CircleWithHorizontalBar"
    elif "^{''}" in raw or "^''" in raw or '^"' in raw:
        suffix = '^"'
    elif "^o" in raw:
        suffix = "^o"
    elif "^^" in raw:
        suffix = "^^"
    elif "^_" in raw:
        suffix = "^_"
    else:
        suffix = ""
    return digits + suffix


def tokenize_transcript(path):
    text = path.read_text(encoding="utf-8")
    body = text.split("> (", 1)[1]
    body = re.sub(r"<CLEARTEXT[^\n]*", "", body)
    body = re.sub(r"^#.*$", "", body, flags=re.MULTILINE)
    # In this manual transcript, each visual line ends at a group boundary even
    # when the final comma was omitted.
    body = body.replace("\r", "").replace("\n", ",")
    tokens = []
    for raw in body.split(","):
        token = normalize_group(raw)
        if token:
            tokens.append((token, raw.strip()))
    return tokens


def tokenize_pages(path):
    text = path.read_text(encoding="utf-8")
    pages = {}
    for block in re.split(r"(?m)^#IMAGE NAME:\s*", text)[2:]:
        lines = block.splitlines()
        page = lines[0].strip()
        body = "\n".join(lines[1:])
        if "> (" in body:
            body = body.split("> (", 1)[1]
        body = re.sub(r"<CLEARTEXT[^\n]*", "", body)
        body = re.sub(r"^#.*$", "", body, flags=re.MULTILINE)
        body = body.replace("\r", "").replace("\n", ",")
        pages[page] = [(token, raw.strip()) for raw in body.split(",")
                       if (token := normalize_group(raw))]
    return pages


def consensus(left, right, key):
    """Merge two independent transcriptions of the same ciphertext page."""
    a = [token for token, _ in left]
    b = [token for token, _ in right]
    merged = []
    for tag, i1, i2, j1, j2 in SequenceMatcher(None, a, b).get_opcodes():
        if tag == "equal":
            merged.extend(left[i1:i2])
        elif tag == "replace" and i2 - i1 == j2 - j1:
            for lrow, rrow in zip(left[i1:i2], right[j1:j2]):
                lknown = key.get(lrow[0]) not in {None, "<IL>", "<EMPTY>", "<EMMPTY>"}
                rknown = key.get(rrow[0]) not in {None, "<IL>", "<EMPTY>", "<EMMPTY>"}
                merged.append(rrow if rknown and not lknown else lrow)
        else:
            lseg, rseg = left[i1:i2], right[j1:j2]
            def score(seg):
                return sum(key.get(t) not in {None, "<IL>", "<EMPTY>", "<EMMPTY>"}
                           for t, _ in seg) - abs(len(seg) - max(len(lseg), len(rseg)))
            merged.extend(rseg if score(rseg) > score(lseg) else lseg)
    return merged


def canonical_r1036(path, key):
    pages = tokenize_pages(path)
    rows = []
    for page in ("5415.png", "5416.png", "5417.png", "5418.png"):
        rows.extend(pages[page])
    rows.extend(consensus(pages["5419.png"], pages["5421.png"], key))
    rows.extend(consensus(pages["5420.png"], pages["5422.png"], key))
    rows.extend(pages["5423.png"])
    return [(token, raw, (value if value not in {None, "<IL>", "<EMPTY>", "<EMMPTY>"} else None))
            for token, raw in rows for value in [key.get(token)]]


def decode_file(path, key):
    tokens = tokenize_transcript(path)
    rows = []
    for token, raw in tokens:
        value = key.get(token)
        known = value is not None and value not in {"<IL>", "<EMPTY>", "<EMMPTY>"}
        rows.append((token, raw, value if known else None))
    return rows


def main():
    key, conflicts = load_key()
    key.update(R1038_IMAGE_READINGS)
    key.update(R1036_INFERRED)
    key.update(R1036_SEPT30)
    key.update(R1040_B19)
    with (ROOT / "R1038_key_parsed.tsv").open("w", encoding="utf-8", newline="") as fh:
        writer = csv.writer(fh, delimiter="\t")
        writer.writerow(["code", "plaintext", "status"])
        for code in sorted(key, key=lambda c: (int(re.match(r"\d+", c).group()), c)):
            writer.writerow([code, key[code], "context value b19 (R1040 part 2 and R1036)" if code in R1040_B19 else "corrected 30 Sept 2026 (scan or alphabetical place)" if code in R1036_SEPT30 else "contextual inference" if code in R1036_INFERRED else "read from R1038 scan" if code in R1038_IMAGE_READINGS else "R1038 transcription"])
    rows = canonical_r1036(ROOT / "R1036_transcription.txt", key)
    hits = sum(value is not None for _, _, value in rows)
    print(f"key_entries={len(key)} conflicts={len(conflicts)}")
    print(f"tokens={len(rows)} decoded={hits} ({hits / len(rows):.1%})")
    rendered = [value if value is not None else f"[{token}]" for token, _, value in rows]
    (ROOT / "R1036_machine_decipherment.txt").write_text(
        textwrap.fill(" ".join(rendered), width=140, break_long_words=False) + "\n",
        encoding="utf-8",
    )
    with (ROOT / "R1036_tokens.tsv").open("w", encoding="utf-8", newline="") as fh:
        writer = csv.writer(fh, delimiter="\t")
        writer.writerow(["index", "code", "transcribed_group", "plaintext"])
        for index, (token, raw, value) in enumerate(rows, 1):
            writer.writerow([index, token, raw, value or ""])
    unknowns = Counter(token for token, _, value in rows if value is None)
    (ROOT / "R1036_unknowns.txt").write_text(
        "\n".join(f"{count:4d} {token}" for token, count in unknowns.most_common()) + "\n",
        encoding="utf-8",
    )

    r1040_pages = tokenize_pages(ROOT / "R1040_transcription.txt")
    page_stats = []
    r1040_rows = []
    for page, page_rows in r1040_pages.items():
        decoded_page = [(token, raw, (value if value not in {None, "<IL>", "<EMPTY>", "<EMMPTY>"} else None))
                        for token, raw in page_rows for value in [key.get(token)]]
        hits_page = sum(value is not None for _, _, value in decoded_page)
        page_stats.append((page, len(decoded_page), hits_page))
        page_number = int(page.split(".")[0])
        # R1040 changes nomenclators part-way through image 5459.  The first
        # 179 groups belong to the Rechteren-family key; group 180 ("dit
        # alles") is the first group encoded with De Swart's 1765 key.
        if page_number == 5459:
            r1040_rows.extend(decoded_page[179:])
        elif 5459 < page_number < 5474:
            # b19 (23 Oct 2026): image 5474 is back in the first (Rechteren-family) code: its marks are the first
            # code's single/double strokes and double underlines (^' and ^__, absent from 5460-5473), the 1765 key
            # covers only 69% of it (as on 5453-5458, against 87-92% on 5460-5473) and gives no Dutch after
            # "het antwoort dat daar op gegeven is", the last words of 5473.
            r1040_rows.extend(decoded_page)
    r1040_rendered = [value if value is not None else f"[{token}]" for token, _, value in r1040_rows]
    (ROOT / "R1040_second_key_machine_decipherment.txt").write_text(
        textwrap.fill(" ".join(r1040_rendered), width=140, break_long_words=False) + "\n",
        encoding="utf-8",
    )
    with (ROOT / "R1040_second_key_tokens.tsv").open("w", encoding="utf-8", newline="") as fh:
        writer = csv.writer(fh, delimiter="\t")
        writer.writerow(["index", "code", "transcribed_group", "plaintext"])
        for index, (token, raw, value) in enumerate(r1040_rows, 1):
            writer.writerow([index, token, raw, value or ""])
    (ROOT / "R1040_1765_page_stats.tsv").write_text(
        "page\ttokens\tdecoded\trate\n" + "\n".join(
            f"{page}\t{total}\t{hits}\t{(hits / total if total else 0):.3%}" for page, total, hits in page_stats
        ) + "\n", encoding="utf-8"
    )
    for start in range(0, len(rendered), 30):
        print(" ".join(rendered[start:start + 30]))


if __name__ == "__main__":
    main()
