"""Re-read brief (REREAD_BRIEF.md), batch b24: bilia1527 (f. 102v stays decoded, not read). One save per change.
(Both texts entries have doc 'f102', so set_state.py would hit f. 102r; the second entry is edited by index.)"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from relabel_r0 import load, save  # noqa: E402
T = 'bilia1527'
NOTE = ("Re-read 23 Oct 2026 (b24): no decipherment or copy (no. 42 is another cipher; the clear close is not one); the seven lines "
        "checked on Gallica view 165 at full size (4211 px, openapi IIIF) against the contributor's sign transcription and decoded with "
        "R5258: words carried ('a suo genero', 'vostra ecelentia', 'potesseno', 'conformita', 'ancora', 'si aspetta', 'con le risposte di') "
        "but no sentence; partial reading f102v_partial_reading.md, 0.00 clean (0/6), explicit holes 0.33. Blockers: needs-physical-access "
        "(every line's last signs run into the gutter of the microfilm scan; the manuscript or a flat scan would show them) and "
        "no-key-material (R.29, 8?, the open rectangle, o.19 are not on the R5258 sheet).")
p = load(T); e = p['outcome']['texts'][1]; assert e['state'] == 'decoded, not read'; e['note'] = NOTE; save(T, p)
p = load(T); p['outcome']['texts'][1]['reading'] = 'f102v_partial_reading.md'; save(T, p)
p = load(T)
p['outcome']['gaps'] = [
    {'item': 'f. 102v, seven cipher lines (118 signs): words but no sentences', 'blocker': 'no-key-material',
     'detail': 'checked on view 165 at full size and decoded with R5258 (23 Oct 2026); R.29, 8?, the open rectangle and o.19 have no value on the key sheet, and £, φ, mp only context values'},
    {'item': 'f. 102v line ends at the gutter (one or two signs a line)', 'blocker': 'needs-physical-access',
     'detail': 'only the BnF microfilm scan is online; the last signs of each line curve into the binding'},
    {'item': 'name code B.58 (f. 102r line 2)', 'blocker': 'no-key-material',
     'detail': 'not on the R5258 nomenclator (checked on the sheet image); one occurrence'},
    {'item': 'about 28 doubtful signs on f. 102r', 'blocker': 'not-attempted',
     'detail': '8 image-check splits, Theophimo, pervitio, papre, tompi, vechilza, £ as l or et, B.3?; AI-only transcription, no human check'},
]
save(T, p)
p = load(T)
p['solution'].append({'date': '2026-10-23', 'kind': 'transcription', 'technique': ['manual reconstruction'], 'what': "Re-read (REREAD_BRIEF, b24): f. 102v fetched at full size (Gallica view 165, 4211 x 6046, openapi.bnf.fr IIIF) and the seven cipher lines compared with the contributor's sign transcription on zoomed strips; decoded with R5258. Words carried ('a suo genero', 'vostra ecelentia', 'potesseno', 'conformita', 'ancora', 'si aspetta', 'con le risposte di'), no sentence; every line's last signs run into the gutter; R.29, 8?, the open rectangle and o.19 have no key value. Partial reading f102v_partial_reading.md (0.00 clean); stays decoded, not read.", 'result': 'failed'})
save(T, p); print('ok')
