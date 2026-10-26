"""Build candidates.json from the DigitArq records (details.jsonl + crawl_*.jsonl) and the hand-scored groups below.

python build_candidates.py   -> candidates.json
Each GROUP selects records by reference code and fills the brief's fields; dates, quotas and links come from the
records themselves, so nothing is typed from memory.
"""
import glob, json, re, pathlib

HERE = pathlib.Path(__file__).parent
REC = {}
for fn in ["details.jsonl", *sorted(glob.glob(str(HERE / "crawl_*.jsonl")))]:
    for l in open(HERE / fn, encoding="utf8"):
        r = json.loads(l)
        REC[r["ref"]] = r

MONTHS = "Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split()
PT_MONTHS = {m: i for i, m in enumerate("janeiro fevereiro março abril maio junho julho agosto setembro outubro novembro dezembro".split(), 1)}
SCORE = "Scored from the archive description during the Oct 2026 Torre do Tombo sweep (research/torre_do_tombo/); not viewed"
SCORE_IMG = "Scored from the archive description during the Oct 2026 Torre do Tombo sweep (research/torre_do_tombo/); volume scans sampled"
CHECKED = "checked 26 Oct 2026: known.py (repo, DECODE, Cryptoole: no hit), web search"


def link(r, label=None):
    return {"label": label or f"DigitArq {r['ref']}", "href": f"https://digitarq.arquivos.pt/documentDetails/{r['id']}"}


def fmt_date(r):
    d = r.get("d1")
    desc = r.get("description") or ""
    m = re.search(r"datada de (\d+) de (\w+) de (1\d\d\d)", desc)
    if m and m.group(2).lower() in PT_MONTHS:
        return int(m.group(3)), f"{int(m.group(1))} {MONTHS[PT_MONTHS[m.group(2).lower()] - 1]} {m.group(3)}"
    if d:
        y, mo, da = d[:10].split("-")
        if mo == "01" and da == "01" and (r.get("d2") or "")[:4] != y:
            return int(y), f"{y}-{(r.get('d2') or '')[:4]}" if r.get("d2") else y
        return int(y), f"{int(da)} {MONTHS[int(mo) - 1]} {y}"
    return None, "unknown"


def quota(r):
    return "; ".join(q for q in r["quota"] if q) or r["ref"]


def row(r, **kw):
    y, date = fmt_date(r)
    base = {
        "year": kw.pop("year", y), "date": kw.pop("date", date),
        "title": kw.pop("title"), "correspondents": kw.pop("correspondents"),
        "place": kw.pop("place", "unknown"), "language": kw.pop("language", "Portuguese"),
        "region": kw.pop("region", "Portugal"), "period": None,
        "shelfmark": f"ANTT, {quota(r)} ({r['ref']})",
        "folio_note": kw.pop("folio_note"), "cls": kw.pop("cls"), "status": kw.pop("status"),
        "why": kw.pop("why"), "importance": kw.pop("importance"), "solvability": kw.pop("solvability"),
        "difficulty": kw.pop("difficulty"), "score_note": kw.pop("score_note", SCORE),
        "verify": kw.pop("verify"), "links": [link(r)] + kw.pop("links", []),
        "seen": kw.pop("seen", "catalogue"), "source": "Arquivo Nacional Torre do Tombo (DigitArq) sweep",
        "prior_art": kw.pop("prior_art"),
    }
    assert not kw, kw
    base["period"] = period(base["year"])
    return base


def period(y):
    if not y: return "unknown"
    for lo, hi, p in [(0, 1496, "15th century"), (1497, 1559, "1497-1559"), (1560, 1589, "1560-1589"), (1589, 1598, "1589-1598"),
                      (1598, 1610, "1598-1610"), (1611, 1650, "1611-1650"), (1651, 1700, "1651-1700"), (1701, 1800, "1701-1800"),
                      (1801, 1900, "1801-1900"), (1901, 1950, "1901-1950")]:
        if lo <= y <= hi: return p
    return "unknown"


def refs(prefix, rx=r"cifr"):
    out = []
    for ref, r in sorted(REC.items()):
        if ref.startswith(prefix) and ref != prefix.rstrip("/"):
            t = " ".join(r["titles"]) + " " + (r["description"] or "")
            if re.search(rx, t, re.I) and not re.search(r"^\"?Cifra", r["titles"][0]):
                out.append(r)
    return out


C = []

# 1. João IV -> marquês de Nisa, letter-book MSLIV 1017 (digitised; cipher seen on m0019)
vol = REC["PT/TT/MSLIV/1017"]
for r in refs("PT/TT/MSLIV/1017/"):
    if "Taquet" in r["titles"][0]:
        continue
    C.append(row(r, title="João IV → marquês de Nisa, ambassador in Paris, " + fmt_date(r)[1] + ", mostly in cipher: '" + r["titles"][0].split("França,", 1)[-1].strip()[:100] + "'",
        correspondents="João IV of Portugal → Vasco Luís da Gama, marquês de Nisa", place="Lisbon",
        folio_note=f"Letter {r['ref'].rsplit('/', 1)[1].lstrip('0')} of 284 in MSLIV 1017 (289 scans online); description: '{(r['description'] or '').strip()[:90]}'",
        cls="C", status="DigitArq: letter-book copy, 'escrita na sua maioria em cifra'; no decipherment mentioned. A sampled scan (m0019) shows cipher written as pseudo-words in Latin letters inside clear text, no interlinear decipherment. Not on DECODE.",
        why="Restoration diplomacy: the king's secret instructions to his ambassador in France on the French alliance, Westphalia and the captive infante D. Duarte.",
        importance=4, solvability=4, difficulty=2, score_note=SCORE_IMG, seen="image",
        verify="Locate the letter in the volume scans (one scan ≈ one letter, in order), transcribe the cipher runs; check Laranjo Coelho's 1940-42 edition for printed decipherments.",
        links=[link(vol, "Volume MSLIV 1017 with scans")],
        prior_art=f"Printed: Cartas de El-Rei D. João IV ao Conde da Vidigueira (Marquês de Niza), ed. P. M. Laranjo Coelho, Academia Portuguesa da História, 1940-42, from Torre do Tombo MSS; whether the cipher runs are deciphered there is unchecked ({CHECKED})."))
r = REC["PT/TT/MSLIV/1017/00223"]
C.append(row(r, title="João IV → marquês de Nisa, forwarding a cipher letter of 'Francisco Taquet' (Fernando de la Houe), agent of the captive infante D. Duarte",
    correspondents="João IV → marquês de Nisa; enclosure Francisco Taquet (Fernando de la Houe) → João IV", place="Lisbon", year=1645, date="28 Apr 1645",
    folio_note="Letter 223 of 284 in MSLIV 1017 (scans online); whether the Taquet cipher itself is copied is unknown",
    cls="C", status="DigitArq says the king remits 'carta em cifra de Francisco Taquet'; the copy may reproduce the cipher. Not on DECODE.",
    why="Taquet ran the secret correspondence of the infante D. Duarte, prisoner in Milan; a cipher from that channel would be a new key family.",
    importance=3, solvability=3, difficulty=3, score_note=SCORE_IMG,
    verify="Find letter 223 in the scans and see whether the Taquet letter is copied in cipher.",
    links=[link(vol, "Volume MSLIV 1017 with scans")],
    prior_art=f"Laranjo Coelho 1940-42 edition unchecked ({CHECKED})."))
r = REC["PT/TT/MSLIV/1016"]
C.append(row(r, title="João IV → marquês de Nisa, embassy letter-book Tomo I (sibling of MSLIV 1017)", year=1642, date="1641-1649?",
    correspondents="João IV → marquês de Nisa", place="Lisbon",
    folio_note="182 letters, 260 scans online; no item described as cipher, but in MSLIV 1017 only 7 of 284 are flagged although cipher runs occur elsewhere (m0019)",
    cls="C", status="Volume digitised; descriptions do not mention cipher. Listed as the companion volume of MSLIV 1017; not on DECODE.",
    why="Same correspondence and same cipher as MSLIV 1017; more ciphertext for the same key.",
    importance=3, solvability=3, difficulty=2, score_note=SCORE,
    verify="Page through the 260 scans for cipher runs.",
    prior_art=f"Laranjo Coelho 1940-42 edition ({CHECKED})."))

# 2. Holland embassy letters to Francisco de Melo (MMCG 1E/2L/3L), keys bound in the same volumes
for prefix, short, who, key, place, why in [
    ("PT/TT/MMCG/1E/", "Teles de Faro", "D. Fernando Teles de Faro → Francisco de Melo (later marquês de Sande)", "1E/000003 'Cifra por que se podem entender as cartas que estão neste livro'", "The Hague",
     "Teles de Faro was the ambassador in Holland who defected to Spain in 1659 with embassy funds; his ciphered letters cover the run-up."),
    ("PT/TT/MMCG/2L/", "Luís Álvares Ribeiro", "Luís Álvares Ribeiro, embassy secretary in Holland → Francisco de Melo, ambassador in England", "2L/000013 (f. 22) 'a cifra para decifrarem as cartas que estão neste livro'", "The Hague",
     "The Portuguese embassy in The Hague after Teles de Faro's flight, during the Dutch-Portuguese war over Brazil."),
    ("PT/TT/MMCG/3L/", "Conde de Miranda", "Henrique de Sousa Tavares, conde de Miranda, ambassador extraordinary in Holland → Francisco de Melo", "3L/000003 and 3L/000020 (two keys, for the first and the later letters)", "The Hague",
     "Miranda's 1659-61 embassy negotiated the Dutch peace (1661) while Melo arranged the English marriage of Catherine of Braganza."),
]:
    for r in refs(prefix):
        vol = REC[prefix.rstrip("/")]
        whole = "Toda a carta" in (r["description"] or "") or "em cifra" in r["titles"][0]
        unk = "autor" in r["titles"][0]
        t = (f"Unidentified writer, letter in the {short} volume" if unk else
             f"{short} → Francisco de Melo" if "Minuta" not in r["titles"][0] else "Draft to the States General ('Altos e Poderosos Senhores')")
        C.append(row(r, title=f"{t}, {fmt_date(r)[1] if r['d1'] else 'undated'}, The Hague embassy ({'in cipher' if whole else 'partly in cipher'})",
            **({"year": int(r["d1"][:4]) if r["d1"] else 1660, "date": fmt_date(r)[1] if r["d1"] else "undated (volume 1658-1660)"}),
            correspondents=who if not unk else "unknown (in the " + who.split("→")[0].strip() + " volume)", place=place,
            folio_note=f"{quota(r)}; {(r['description'] or r['titles'][0]).strip()[:80]}",
            cls="A", status=f"DigitArq: '{(r['description'] or r['titles'][0]).strip()[:70]}'; no decipherment noted. The volume holds its own key ({key}). Not digitised; not on DECODE.",
            why=why, importance=3, solvability=2, difficulty=1,
            verify="Order scans of the letter and of the key leaf from ANTT (MMCG tome not online); read with the bound key.",
            links=[link(vol, f"Volume {prefix.rstrip('/').split('/', 2)[2]}")],
            prior_art=f"open ({CHECKED}: no edition of these letters found; E. Prestage's Portuguese-Dutch diplomatic studies not checked)."))

for ref, who in [("PT/TT/MMCG/4B/000141", "Duarte Nunes da Costa (Jacob Curiel), Portuguese crown agent in Hamburg → D. Vasco Luís da Gama, conde da Vidigueira"),
                 ("PT/TT/MMCG/4B/000030", "Pero Mendes de Sampaio → D. Vasco Luís da Gama, conde da Vidigueira")]:
    r = REC[ref]
    C.append(row(r, title=who.split(" → ")[0].split(" (")[0] + " → conde da Vidigueira (later marquês de Nisa), partly in cipher", correspondents=who,
        **({} if r["d1"] else {"year": 1642, "date": "undated (volume of letters to Vidigueira, c. 1640s)"}),
        folio_note=f"{quota(r)}; 'Parte da carta está escrita em cifra'", cls="C",
        status="DigitArq: part of the letter in cipher; no decipherment noted; no key in the volume listing. Not digitised; not on DECODE.",
        why="Correspondence of the Portuguese ambassador in Paris in the first Restoration years; Nunes da Costa ran arms purchases and intelligence from Hamburg.",
        importance=3, solvability=1, difficulty=3, verify="Order scans; test against the Nisa ciphers of MSLIV 1016/1017.",
        prior_art=f"open ({CHECKED})."))

# 3. Single items and volumes scored by hand from their DigitArq descriptions
OTHER = [
 ("PT/TT/CPN/000210", dict(title="Unidentified writer → the Portuguese ambassador in Rome, partly in cipher (Italian)", correspondents="unknown → Portuguese ambassador in Rome (Francisco de Sousa Coutinho's mission?)",
   place="unknown", language="Italian", region="Papacy", cls="C", folio_note="Condes da Ponte, cx. 8 (Mello e Torres), doc. MT-151; 'Parcialmente em cifra'",
   status="DigitArq: 'Parcialmente em cifra'; no decipherment noted. Not digitised; not on DECODE.",
   why="Portugal had no recognised ambassador at the Holy See in 1658; a cipher letter to its envoy bears on the fight for papal recognition of the Braganza dynasty.",
   importance=3, solvability=1, difficulty=3, verify="Order scans; compare with the Orsini cipher letters in CPN mç. 17 n.º 1.", prior_art=f"open ({CHECKED}).")),
 ("PT/TT/CPN/0017/00001", dict(title="Letters to Francisco de Melo (Mazarin, Cardinal Orsini, Sousa Coutinho in Rome, secretary Pedro Vieira da Silva), with cipher letters of Orsini and Vieira da Silva",
   correspondents="Cardinal Virginio Orsini; Pedro Vieira da Silva, secretary of state; others → Francisco de Melo", place="Rome; Lisbon; Paris", language="Portuguese, Italian, French", region="Portugal",
   year=1657, date="1657-1660", cls="C", folio_note="Condes da Ponte, mç. 17, n.º 1 (old Liv. 549); a bound book of letters, 'contém documentos cifrados do cardeal Orsini e do secretário de Estado Vieira da Silva'",
   status="DigitArq: contains ciphered documents; no decipherment noted. Not digitised; not on DECODE.",
   why="Orsini was the protector of Portugal at the Curia; the secretary of state's cipher to Melo carries Lisbon's instructions for the English and French negotiations.",
   importance=4, solvability=1, difficulty=3, verify="Order scans; the CPN mç. 19 copy-book and MMCG keys may share the Vieira da Silva cipher.", prior_art=f"open ({CHECKED}).")),
 ("PT/TT/CPN/0019/00001", dict(title="Copy-book of letters to the marquês de Sande in England from the conde de Miranda, Cardinal Orsini and Gaspar Dias de Mesquita, 1660-61, with cipher documents",
   correspondents="Conde de Miranda; Cardinal Orsini; Gaspar Dias de Mesquita → Francisco de Melo, marquês de Sande", place="The Hague; Rome", language="Portuguese, Spanish, Italian, French, Latin",
   year=1660, date="1660-1661", cls="B", folio_note="Condes da Ponte, mç. 19, n.º 1 (Códice 12); letters numbered 1-113; 'contém documentos cifrados'",
   status="DigitArq: copy-book containing ciphered documents; no decipherment noted. Miranda's cipher for the same correspondence is bound in MMCG 3L (key leaves 3L/000003, 000020). Not digitised; not on DECODE.",
   why="Continuation of the Miranda-Melo Hague correspondence (Dutch peace 1661, the English marriage) and Orsini's Roman despatches.",
   importance=4, solvability=2, difficulty=2, verify="Order scans; read Miranda items with the MMCG 3L keys.", prior_art=f"open ({CHECKED}).")),
 ("PT/TT/LMP/0001", dict(title="Marquês de Sande's papers on the marriage of Catherine of Braganza and Charles II, with cipher letters (incl. Diogo Lopes de Ulhoa at The Hague → Rui Teles de Meneses in Paris)",
   correspondents="various → Francisco de Melo, conde da Ponte, marquês de Sande; Diogo Lopes de Ulhoa → Rui Teles de Meneses", place="London; The Hague; Paris; Lisbon", language="Portuguese, Italian, Latin, English, French",
   year=1661, date="1657-1667", cls="C", folio_note="Luís de Miranda Pereira, liv. 1; 592 scans online; 'códice factício contendo cartas assinadas, cartas cifradas e cópias de cartas'",
   status="DigitArq: factitious codex with 'cartas cifradas'; no decipherment noted. Digitised (592 scans); not on DECODE.",
   why="The Anglo-Portuguese marriage treaty of 1661 (Bombay, Tangier) and Portuguese diplomacy at The Hague and Paris.",
   importance=4, solvability=4, difficulty=3, verify="Page through the 592 scans for the cipher letters and count tokens.", prior_art=f"open ({CHECKED}).")),
 ("PT/TT/LMP/0002", dict(title="Royal letters to the conde de Vila Flor and D. Sancho Manuel, governors of arms in the Alentejo and Beira, with cipher letters (Restoration War)",
   correspondents="Afonso VI and Queen Luísa de Gusmão (signed by councillors) → D. Sancho Manuel, conde de Vila Flor", place="Lisbon", region="Portugal",
   year=1661, date="1660-1663", cls="C", folio_note="Luís de Miranda Pereira, liv. 2; 864 scans online; 'cartas cifradas e cópias de cartas'",
   status="DigitArq: factitious codex including ciphered letters; no decipherment noted. Digitised (864 scans; a 12-scan sample showed clear royal letters, the cipher ones not yet located); not on DECODE.",
   why="Crown-to-field-commander cipher in the decisive years before Ameixial (1663).",
   importance=4, solvability=4, difficulty=3, score_note=SCORE_IMG, seen="image", verify="Page through the 864 scans for the cipher letters.", prior_art=f"open ({CHECKED}).")),
 ("PT/TT/CFTR-ALM/007-7.26/0082", dict(title="Conde de Assumar's copy-book of letters from Barcelona to Portuguese ministers abroad (Vienna, Rome, London, The Hague), with cipher passages",
   correspondents="Pedro de Almeida, conde de Assumar, ambassador to Charles III in Barcelona → conde de Villar Mayor (Vienna), André de Melo de Castro (Rome), D. Luís da Cunha (London), conde de Tarouca, Duke of Savoy and others",
   place="Barcelona", language="Portuguese, French, Spanish", region="Portugal", year=1708, date="1708-1709", cls="C", folio_note="Casa Fronteira e Alorna, n.º 82; 'inclui carta com partes em cifras'",
   status="DigitArq: includes a letter with parts in cipher; no decipherment noted. Not digitised; not on DECODE.",
   why="War of the Spanish Succession: the Portuguese embassy to the Habsburg claimant and its network of envoys.",
   importance=3, solvability=1, difficulty=3, verify="Ask Fundação das Casas de Fronteira e Alorna / ANTT for images; locate the cipher letter.", prior_art=f"open ({CHECKED}).")),
 ("PT/TT/CFTR-ALM/007-7.26/0083", dict(title="Conde de Assumar's copy-book of letters to Portuguese ministers and others, Barcelona 1709-11, with cipher passages",
   correspondents="conde de Assumar → André de Melo de Castro, conde de Tarouca, D. Luís da Cunha, Barão Tinti, Alexandre Nunes da Costa, Cardinal Conti and others",
   place="Barcelona", language="Spanish, Portuguese", region="Portugal", year=1709, date="1709-1711", cls="C", folio_note="Casa Fronteira e Alorna, n.º 83; 'inclui carta com partes em cifras'",
   status="DigitArq: includes a letter with parts in cipher; no decipherment noted. Not digitised; not on DECODE.",
   why="Same embassy as n.º 82, the last years of the war in Catalonia.", importance=3, solvability=1, difficulty=3,
   verify="Images needed; the Garelli volume (n.º 104, doc. 30) holds a cipher register that may be the key.", prior_art=f"open ({CHECKED}).")),
 ("PT/TT/CFTR-ALM/007-7.48/0114", dict(title="Conde de Tarouca, Portuguese plenipotentiary at The Hague → conde de Assumar, letters with cipher passages (Quadruple Alliance, Gibraltar)",
   correspondents="João Gomes da Silva, conde de Tarouca → Pedro de Almeida, conde de Assumar", place="The Hague", language="Portuguese, French", region="Low Countries",
   year=1720, date="1720-1721", cls="C", folio_note="Casa Fronteira e Alorna, n.º 114 (Tomo 4 of Tarouca's letters); 'cartas com partes cifradas'",
   status="DigitArq: letters with ciphered parts; no decipherment noted. Not digitised; not on DECODE.",
   why="Inside view of the Quadruple Alliance and Gibraltar talks from Portugal's man at The Hague.", importance=3, solvability=1, difficulty=3,
   verify="Images needed; look for Tomos 1-3 of the same series in CFTR-ALM.", prior_art=f"open ({CHECKED}).")),
 ("PT/TT/ASG/B/002/000010", dict(title="Marquês de Aguiar → António de Saldanha da Gama, despatch wholly in cipher",
   correspondents="Fernando José de Portugal, marquês de Aguiar (minister in Rio de Janeiro) → António de Saldanha da Gama (Portuguese envoy, St Petersburg)", place="Rio de Janeiro",
   region="Portugal", cls="C", folio_note="António Saldanha da Gama, cx. 1, mç. 1, n.º 3, doc. 10; 'totalmente cifrado'",
   status="DigitArq: 'totalmente cifrado'; no decipherment noted (contrast ASG/B/003/00002, which has its decipherment attached). Not digitised; not on DECODE.",
   why="Court-in-Brazil instructions to the envoy in Russia in the year of the Banda Oriental invasion.", importance=3, solvability=1, difficulty=3,
   verify="Order scans; ASG/B/003/00002 (1817, conde da Barca, with 'decifração da parte cifrada') is a crib/key source for the same ministry cipher.",
   prior_art=f"open ({CHECKED}).")),
 ("PT/TT/ASG/C/010/000013", dict(title="Marquês de Palmela → António de Saldanha da Gama, reserved despatch partly in cipher, forwarding Hyde de Neuville's letter",
   correspondents="Pedro de Sousa Holstein, marquês de Palmela → António de Saldanha da Gama", place="Lisbon", region="Portugal", cls="B",
   folio_note="António Saldanha da Gama, cx. 1, mç. 2, n.º 10, doc. 13; 'parcialmente em cifra'",
   status="DigitArq: partly in cipher; no decipherment noted. Same fonds holds a deciphered 1817 ministry despatch (ASG/B/003/00002). Not digitised; not on DECODE.",
   why="The Abrilada aftermath (1824) and the French envoy Hyde de Neuville's role in it.", importance=3, solvability=1, difficulty=2,
   verify="Order scans of this and ASG/B/003/00002.", prior_art=f"open ({CHECKED}).")),
 ("PT/TT/CAM/M12", dict(title="King Carlos I → Queen Amélia, letters and telegrams, some in cipher", correspondents="Carlos I of Portugal → Queen Amélia",
   place="unknown", region="Portugal", year=1904, date="1903-1906", cls="C", folio_note="Documentos de D. Carlos, D. Amélia e D. Manuel II, mct. 12; 11 letters, 2 telegrams, 1 card; 'alguns documentos estão escritos em cifra'; scans online",
   status="DigitArq: some documents in cipher; no decipherment noted. Digitised; not on DECODE.",
   why="Private royal cipher between the last reigning couple before the 1908 regicide.", importance=3, solvability=4, difficulty=2,
   verify="View the scans; personal ciphers of this kind are usually short substitutions.", prior_art=f"open ({CHECKED}).")),
 ("PT/TT/CAM/M13", dict(title="King Manuel II → Queen Amélia, letters and telegrams, some in cipher", correspondents="Manuel II of Portugal → Queen Amélia (his mother)",
   place="unknown", region="Portugal", year=1908, date="1908-1910", cls="C", folio_note="mct. 13; 4 letters, 3 telegrams; some in cipher; scans online",
   status="DigitArq: some documents in cipher; no decipherment noted. Digitised; not on DECODE.",
   why="The young king's private cipher to his mother in the last years of the monarchy.", importance=3, solvability=4, difficulty=2,
   verify="View the scans; compare with mct. 12, 9, 14, 15.", prior_art=f"open ({CHECKED}).")),
 ("PT/TT/CAM/M09", dict(title="Venceslau de Lima → King Manuel II, ten telegrams, some in cipher", correspondents="Venceslau de Lima (prime minister 1909) → Manuel II",
   place="Lisbon", region="Portugal", year=1909, date="1909", cls="C", folio_note="mct. 9; ten telegrams; some in cipher; scans online",
   status="DigitArq: some documents in cipher; no decipherment noted. Digitised; not on DECODE.",
   why="Government-to-king telegrams in the 1909 cabinet crisis.", importance=2, solvability=3, difficulty=3,
   verify="View the scans; telegraph code or private cipher?", prior_art=f"open ({CHECKED}).")),
 ("PT/TT/CAM/M14", dict(title="Conde de Sabugosa → Queen Amélia, letters and telegrams, some in cipher", correspondents="António Maria de Melo, conde de Sabugosa → Queen Amélia",
   place="unknown", region="Portugal", year=1910, date="1910", cls="C", folio_note="mct. 14; 4 letters, 4 telegrams; some in cipher; scans online",
   status="DigitArq: some documents in cipher; no decipherment noted. Digitised; not on DECODE.",
   why="The queen's household during the October 1910 revolution.", importance=3, solvability=3, difficulty=2,
   verify="View the scans.", prior_art=f"open ({CHECKED}).")),
 ("PT/TT/CAM/M15", dict(title="Hintze Ribeiro → Queen Amélia, two telegrams in cipher", correspondents="Ernesto Hintze Ribeiro → Queen Amélia",
   place="unknown", region="Portugal", year=1906, date="before 1907 (catalogued 1913)", cls="C", folio_note="mct. 15; two telegrams, 'os documentos estão escritos em cifra'; scans online",
   status="DigitArq: both documents in cipher; no decipherment noted. Hintze Ribeiro died in 1907, so the catalogue date 1913 is the file's, not the telegrams'. Digitised; not on DECODE.",
   why="Prime minister to the queen, presumably during a regency of Amélia (1895 or 1906).", importance=2, solvability=2, difficulty=3,
   verify="View the scans.", prior_art=f"open ({CHECKED}).")),
 ("PT/TT/JLC/008/00083", dict(title="Visconde de Pindela → unidentified recipient, correspondence mostly in cipher on Braga politics and the Anglo-German loan",
   correspondents="Vicente Pinheiro Lobo Machado, visconde de Pindela → unknown (in the José Luciano de Castro papers)", place="Braga?", region="Portugal",
   year=1892, date="1892-?", cls="C", folio_note="José Luciano de Castro papers, cx. 8; 'na sua maioria em cifra'",
   status="DigitArq: mostly in cipher; no decipherment noted. Not digitised; not on DECODE.",
   why="Party correspondence on the Anglo-German plan to lend to Portugal against its colonies (1898 secret convention background).", importance=3, solvability=1, difficulty=2,
   verify="Order scans; Pindela was later minister in Berlin, check his code there.", prior_art=f"open ({CHECKED}).")),
 ("PT/TT/HPC/0024/000097", dict(title="José Rogério Taveira → [Henrique de Paiva Couceiro], letter in cipher on the Monarchist Cause", correspondents="José Rogério Taveira → Henrique de Paiva Couceiro",
   place="Spain? (émigrés)", region="Portugal", cls="A", folio_note="Henrique de Paiva Couceiro papers, mç. 24, n.º 97",
   status="DigitArq: letter in cipher; no decipherment noted. The same bundle has Couceiro's draft with 'a cifra correspondente' (n.º 135) and letters partly in cipher (n.º 130-132). Not digitised; not on DECODE.",
   why="Monarchist conspiracy after the failed Monarchy of the North (1919).", importance=2, solvability=2, difficulty=2,
   verify="Order scans of mç. 24 n.º 97, 130-132 and 135 together.", prior_art=f"open ({CHECKED}).")),
]
for n in (130, 131, 132):
    OTHER.append((f"PT/TT/HPC/0024/000{n}", dict(title="Joaquim Pais → [Henrique de Paiva Couceiro], letter partly in cipher", correspondents="Joaquim Pais → Henrique de Paiva Couceiro",
        place="unknown", region="Portugal", cls="A", folio_note=f"Henrique de Paiva Couceiro papers, mç. 24, n.º {n}; 'parte do conteúdo da carta está em cifra'",
        status="DigitArq: part in cipher; no decipherment noted; sibling n.º 135 carries a cipher text with its clear draft. Not digitised; not on DECODE.",
        why="Monarchist organisation in northern Portugal, 1921.", importance=2, solvability=2, difficulty=2,
        verify="Order scans with n.º 135 (clear draft + cipher = crib).", prior_art=f"open ({CHECKED}).")))
OTHER += [
 ("PT/TT/HB/1-1/13", dict(title="Conde de Burnay, 'Notas a Chirac': manuscript notes partly in cipher on 'L'Affaire D. Miguel' and the tobacco contract", correspondents="Henry Burnay → (notes for) Chirac",
   place="Lisbon?", language="French?", region="Portugal", cls="C", folio_note="Henry Burnay fonds, 1-1/13, docs 310-311A",
   status="DigitArq: 'apontamentos manuscritos e cifrados'; no decipherment noted. Not digitised; not on DECODE.",
   why="Lisbon's leading financier on the Braganza-Miguelist loan affair and the 1891 tobacco monopoly.", importance=2, solvability=1, difficulty=3,
   verify="Order scans; Burnay's commercial code may be a published telegraph code.", prior_art=f"open ({CHECKED}).")),
 ("PT/TT/HB/1-1/4", dict(title="Banco Aliança managers → Henry Burnay, correspondence with ciphered telegrams (railways, Salamanca line)", correspondents="J. Ursinus and Francisco Inácio Xavier → Henry Burnay",
   place="Porto", region="Portugal", cls="C", folio_note="Henry Burnay fonds, 1-1/4, docs 19-41; 'contém telegramas cifrados'",
   status="DigitArq: contains ciphered telegrams; no decipherment noted. Not digitised; not on DECODE.",
   why="Business telegraph codes of Portuguese banking; low historical weight.", importance=1, solvability=1, difficulty=3,
   verify="Order scans; check against commercial codebooks (ABC, Lieber's).", prior_art=f"open ({CHECKED}).")),
 ("PT/TT/HB/1-1/38", dict(title="Charles Lefrançois → Henry Burnay, two telegrams, one in cipher", correspondents="Charles Lefrançois → Henry Burnay",
   place="unknown", language="French", region="Portugal", cls="C", folio_note="Henry Burnay fonds, 1-1/38, docs 280-281",
   status="DigitArq: one telegram in cipher; no decipherment noted. Not digitised; not on DECODE.",
   why="Commercial telegram code; low weight.", importance=1, solvability=1, difficulty=3, verify="Order scans.", prior_art=f"open ({CHECKED}).")),
 ("PT/TT/JLC/001/00140", dict(title="Conde de Azevedo e Silva, Brussels → Ministry of Foreign Affairs, two telegrams in cipher", correspondents="conde de Azevedo e Silva (Portuguese minister in Brussels) → Ministério dos Negócios Estrangeiros",
   place="Brussels", region="Portugal", cls="C", folio_note="José Luciano de Castro papers; two telegrams",
   status="DigitArq: telegrams in cipher; no decipherment noted. Not digitised; not on DECODE.",
   why="Portuguese diplomatic telegraph code c. 1904; reading it would open the ministry series.", importance=2, solvability=1, difficulty=4,
   verify="Order scans; the MNE code books of the period are not online.", prior_art=f"open ({CHECKED}).")),
 ("PT/TT/JLC/003/00014", dict(title="Telegram in cipher from St Petersburg to the Minister of Foreign Affairs, Lisbon", correspondents="Portuguese legation, St Petersburg → Minister of Foreign Affairs",
   place="St Petersburg", region="Portugal", cls="C", folio_note="José Luciano de Castro papers",
   status="DigitArq: telegram in cipher; no decipherment noted. Not digitised; not on DECODE.",
   why="Russo-Japanese War period legation report.", importance=2, solvability=1, difficulty=4, verify="Order scans.", prior_art=f"open ({CHECKED}).")),
 ("PT/TT/JLC/003/00044", dict(title="Telegram in cipher from the Portuguese consulate in Cape Town to the Minister of Foreign Affairs", correspondents="Portuguese consulate, Cape Town → Minister of Foreign Affairs",
   place="Cape Town", region="Portugal", cls="C", folio_note="José Luciano de Castro papers",
   status="DigitArq: telegram in cipher; no decipherment noted. Not digitised; not on DECODE.",
   why="Southern African affairs (Mozambique borders) c. 1904.", importance=1, solvability=1, difficulty=4, verify="Order scans.", prior_art=f"open ({CHECKED}).")),
 ("PT/TT/JLC/002/00075", dict(title="Manuel Câmara → José Luciano de Castro, telegram on political matters (in cipher)", correspondents="Manuel Câmara → José Luciano de Castro",
   place="unknown", region="Portugal", cls="C", folio_note="José Luciano de Castro papers",
   status="DigitArq: in cipher; no decipherment noted. Not digitised; not on DECODE.",
   why="Progressive Party internal telegram.", importance=1, solvability=1, difficulty=3, verify="Order scans.", prior_art=f"open ({CHECKED}).")),
 ("PT/TT/JLC/002/00115", dict(title="João Batista da Silva Ferrão de Carvalho Martens → José Luciano de Castro, four telegrams mostly in cipher", correspondents="João Batista da Silva Ferrão de Carvalho Martens → José Luciano de Castro",
   place="unknown", region="Portugal", cls="C", folio_note="José Luciano de Castro papers; four telegrams",
   status="DigitArq: mostly in cipher; no decipherment noted. Not digitised; not on DECODE.",
   why="Political telegrams of a cabinet minister, 1906.", importance=1, solvability=1, difficulty=3, verify="Order scans.", prior_art=f"open ({CHECKED}).")),
]
for ref, kw in OTHER:
    C.append(row(REC[ref], **kw))

json.dump(C, open(HERE / "candidates.json", "w", encoding="utf8"), ensure_ascii=False, indent=1)
print(len(C), "rows so far")
