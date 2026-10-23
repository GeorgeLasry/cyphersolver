"""b16 (N.60): run b16_vich_align.py with the key values proposed in n60_reread_log.md added to the decoder
(sas ver, ree poder, sue saber, men menester), so that words carried by those groups are checked as carried.
decode.py itself is not changed. python b16_vich_align60.py <build> <transcription> [align.tsv]"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / 'targets' / 'vich1511'))
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import decode
PROPOSED = {'sas': 'ver', 'ree': 'poder', 'sue': 'saber', 'men': 'menester'}
decode.CODE.update(PROPOSED)
import b16_vich_align
b16_vich_align.main(*sys.argv[1:4])
