# Lexicons for bench.py, anchors_bench.py, equation_rebus.py

Downloaded 25 Oct 2026. Raw downloads are in `raw/` (git-ignored, 265 MB); `mw.txt` is also git-ignored
(50 MB). Rebuild everything with the commands below.

| File | Source | Licence |
|---|---|---|
| `mw.txt` (50,163,993 B) | Monier-Williams 1899, Cologne Digital Sanskrit Dictionaries, csl-orig: https://raw.githubusercontent.com/sanskrit-lexicon/csl-orig/master/v02/mw/mw.txt (copied unchanged) | CC BY-SA 4.0 (Cologne CDSD) |
| `forms.csv` (7,544,914 B), `dedr_entry_v11.csv` (6,252,569 B) | Merriam & Fuls, The Dravidian Database v1.1 (DEDR, Burrow & Emeneau 1984, DSAL edition), Zenodo record 22286173, https://zenodo.org/records/22286173/files/forms.csv and .../dedr_entry_v11.csv (copied unchanged; v1.2 = record 22682542 has a different forms.csv) | CC BY 4.0 |
| `sux_gloss.tsv` (473,328 B, 15,940 entries) | Oracc ePSD2 JSON, http://oracc.museum.upenn.edu/json/epsd2.zip, member `epsd2/gloss-sux.json`; columns cf, gw, pos, senses (sense `mng` joined with ` \| `) | CC0 |

## Commands (from `targets/indus`)

```
mkdir -p data/lexicons/raw/{mw,dedr,epsd2}
curl -sL -o data/lexicons/raw/mw/mw.txt https://raw.githubusercontent.com/sanskrit-lexicon/csl-orig/master/v02/mw/mw.txt
for f in forms.csv dedr_entry_v11.csv README.md languages.csv parameters.csv; do curl -sL -o data/lexicons/raw/dedr/$f "https://zenodo.org/records/22286173/files/$f?download=1"; done
curl -sL -o data/lexicons/raw/epsd2/epsd2.zip http://oracc.museum.upenn.edu/json/epsd2.zip
PYTHONUTF8=1 python -I build_lexicons.py data/lexicons
PYTHONUTF8=1 python anchors_bench.py data/lexicons/mw.txt data/lexicons/forms.csv data/lexicons/sux_gloss.tsv
```

`bench.dedr_glosses` reads `dedr_entry_v11.csv` from the folder holding `forms.csv`, so keep them together.

Check against the earlier scratch copies (C:/Users/dbour/indus_data, Sept 2026): forms.csv, dedr_entry_v11.csv
and sux_gloss.tsv are byte-identical; mw.txt differs slightly (csl-orig has had corrections since).
