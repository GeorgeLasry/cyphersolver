"""Read the voice line out of a NoteWorthy Composer binary file (NWZ = zlib-compressed NWC 2.x).

Format as inferred from elgbav6-3.nwc (NWC Scriptorium, Lullaby op. 27 no. 3):
records are a type byte + fixed payload: 2 barline (4 bytes), 8 note (10), 9 rest (10);
note payload: [2] duration code (0 whole, 1 half, 2 quarter, 3 eighth, 4 16th), [6] flags (0x04 dotted),
[8] staff position (signed, 0 = middle line), [9] accidental/flags. Other record types are skipped by
scanning to the next plausible note/rest/barline. Prints the note list for a staff and writes
<out>.json: [(staff_position, duration_in_eighths), ...].

python targets/dorabella/nwc_melody.py <file.nwc> <staff name> <out.json>
"""
import sys, zlib, json, re

raw = open(sys.argv[1], 'rb').read()
d = zlib.decompress(raw[6:]) if raw.startswith(b'[NWZ]') else raw
name = sys.argv[2].encode()
start = d.index(name + b'\x00Standard')
nxt = [m.start() for m in re.finditer(rb'\x00Standard\x00', d) if m.start() > start + len(name) + 1]
end = nxt[0] if nxt else len(d)
seg = d[start:end]
EIGHTHS = {0: 8, 1: 4, 2: 2, 3: 1, 4: 0.5, 5: 0.25}


def plausible_note(p):
    return (p + 11 <= len(seg) and seg[p] == 8 and seg[p + 1] == 0 and seg[p + 2] == 0 and seg[p + 3] <= 5
            and seg[p + 4:p + 7] == b'\x00\x00\x00')


def plausible_rest(p):
    return p + 11 <= len(seg) and seg[p] == 9 and seg[p + 1] == 0 and seg[p + 2] == 0 and seg[p + 3] <= 5


notes, bars = [], 0
p = 0
first = next(i for i in range(len(seg)) if plausible_note(i) or plausible_rest(i))
p = first
while p < len(seg):
    t = seg[p]
    if plausible_note(p):
        dur = EIGHTHS[seg[p + 3]] * (1.5 if seg[p + 7] & 0x04 else 1)
        pos = seg[p + 9] - 256 if seg[p + 9] > 127 else seg[p + 9]
        notes.append((pos, dur, bars, seg[p + 10]))
        p += 11
    elif plausible_rest(p):
        notes.append((None, EIGHTHS[seg[p + 3]] * (1.5 if seg[p + 7] & 0x04 else 1), bars, 0))
        p += 11
    elif t == 2 and seg[p + 1:p + 4] == b'\x00\x00\x00':
        bars += 1
        p += 5
    else:
        p += 1                                       # unknown record: resync on the next known one
print(f'{len([n for n in notes if n[0] is not None])} notes, {bars} bars')
line = []
for pos, dur, bar, acc in notes:
    line.append(f'{"r" if pos is None else pos}:{dur:g}')
print(' '.join(line))
json.dump([(n[0], n[1], n[2], n[3]) for n in notes], open(sys.argv[3], 'w'))
