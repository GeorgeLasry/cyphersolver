"""Rows added after the first merge (kept last so the merged row indices of the other modules do not shift)."""
from rows_sforza import sf, PA

ROWS = [
 # Added 29 Oct 2026 from the leaf-by-leaf check of leads 1312-1319 (ital1584_copies.md): the only cipher leaves found
 # with no decipherment beside them.
 sf(1585, year=1448, date="28 Feb 1448",
    title="Andrea da Birago → Francesco Sforza, a wholly ciphered letter from Pavia",
    correspondents="Andrea da Birago → Francesco Sforza", place="Pavia",
    shelfmark="BnF italien 1585, f. 33 (Gallica canvas 63; address on 64)",
    folio_note="one letter, 12 lines of cipher after a clear salutation, signed 'Servitor Andreas Biragus'; a third alphabet (signs built from H, A, 6, 00 and dashes), unlike Amidani's, Guarna's or Tranchedini's; f. 32 is a clear letter of the same writer and day (probably a separate letter)",
    status="Image checked 29 Oct 2026: no late clear copy on ff. 31-34 and no interlinear glosses; Mazzatinti lists it under Amidani's 'del medesimo' chain.",
    why="Pavia under the Ambrosian Republic, Feb 1448; the one leaf of the 1447-48 Milan series found with no decipherment.",
    importance=3, solvability=3, difficulty=3, seen="image",
    verify="Compare f. 32 (same writer, same day) as a possible crib; look for Birago's other letters and a Birago key (ASMi cart. 1597 keys on DECODE).",
    prior_art=PA + " Leaf-by-leaf check 29 Oct 2026: no copy or gloss beside it (research/venice_milan_print/ital1584_copies_B.md)."),
 sf(1585, year=1448, date="19 Jan 1448",
    title="Vincenzo Amidani → Francesco Sforza, cipher letter from Milan of 19 January 1448",
    correspondents="Vincenzo Amidani → Francesco Sforza", place="Milan",
    shelfmark="BnF italien 1585, f. 18",
    folio_note="one letter, not in Mazzatinti's 'in cifre' list; found during the check of lead 1316; whether a copy or gloss is filed with it was not checked",
    status="Seen in passing 29 Oct 2026; decipherment not yet looked for.",
    why="Amidani's Milan reports under the Ambrosian Republic; his other 1447 letters have late clear copies beside them.",
    importance=2, solvability=4, difficulty=2, seen="image",
    verify="View ital. 1585 ff. 17-19 for a late clear copy or interlinear glosses before any other work.",
    prior_art=PA),
]
