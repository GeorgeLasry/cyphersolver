"""Score, sound effects and voiceover mix for the hero video.

    python tools/hero_video/audio.py OUT.wav [--vo DIR] [--stems DIR]

The score is original, written here for this video: a chiptune in A minor at 96 bpm (2.5 s a bar, one bar of
one and a half), synthesised from pulse, triangle, noise and bell voices, with its sections on the scene changes
in hero_video.SCENES. The voiceover takes come from voice.py; the ones vo.json names are kept in vo/ as <id>_<take>.flac (--vo
points elsewhere, .flac or .wav). Each is sped up by TEMPO
without changing its pitch, its lead-in silence is trimmed, and its speech starts at the time in vo.json. The
music ducks under the voice. hero_video.py --audio OUT.wav muxes the result into the video.
"""
import argparse
import json
import subprocess
import sys
from pathlib import Path

import numpy as np
from scipy.io import wavfile
from scipy.signal import butter, fftconvolve, sosfilt

sys.path.insert(0, str(Path(__file__).resolve().parent))
from hero_video import DUR, METHOD_STEPS, SCENES  # noqa: E402

HERE = Path(__file__).resolve().parent
SR = 44100
BEAT = 60 / 96
BAR = 4 * BEAT
N = int(DUR * SR)
S = [t for t, _ in SCENES]          # archive, title, method, decipher, ledger, contribute, close


def hz(m):
    return 440 * 2 ** ((m - 69) / 12)


def env(n, a, d, s, r, hold):
    """Linear ADSR, hold = seconds before release; n = total samples."""
    t = np.arange(n) / SR
    e = np.where(t < a, t / max(a, 1e-4), 1 - (1 - s) * np.clip((t - a) / max(d, 1e-4), 0, 1))
    return e * np.clip(1 - (t - hold) / max(r, 1e-4), 0, 1)


def osc(kind, f, t, duty=.25, vib=0.):
    if vib:
        f = f * (1 + vib * np.sin(2 * np.pi * 5.5 * t) * np.clip(t / .25, 0, 1))
        ph = np.cumsum(f) / SR
    else:
        ph = f * t
    ph %= 1
    if kind == 'pulse':
        return np.where(ph < duty, 1., -1.) - (2 * duty - 1)
    if kind == 'tri':
        return 4 * np.abs(ph - .5) - 1
    if kind == 'sine':
        return np.sin(2 * np.pi * ph)
    raise ValueError(kind)


class Track:
    def __init__(self, pan=0.):
        self.x = np.zeros(N)
        self.pan = pan

    def add(self, t0, sig):
        i = int(round(t0 * SR))
        if i >= N:
            return
        if i < 0:
            sig, i = sig[-i:], 0
        k = min(len(sig), N - i)
        self.x[i:i + k] += sig[:k]

    def note(self, t0, dur, m, kind='pulse', vol=.2, a=.005, d=.08, s=.6, r=.08, duty=.25, vib=0.):
        n = int((dur + r) * SR)
        t = np.arange(n) / SR
        self.add(t0, osc(kind, hz(m), t, duty, vib) * env(n, a, d, s, r, dur) * vol)

    def bell(self, t0, m, vol=.2, decay=2.6):
        n = int(2.5 * SR)
        t = np.arange(n) / SR
        f = hz(m)
        sig = (np.sin(2 * np.pi * f * t) + .35 * np.sin(2 * np.pi * f * 2.76 * t) * np.exp(-t * 4)
               + .18 * np.sin(2 * np.pi * f * 5.4 * t) * np.exp(-t * 7)) * np.exp(-t * decay)
        self.add(t0, sig * np.clip(t / .003, 0, 1) * vol)


rng = np.random.default_rng(96)


def kick(tr, t0, vol=.5):
    n = int(.28 * SR)
    t = np.arange(n) / SR
    f = 45 + 95 * np.exp(-t * 28)
    tr.add(t0, np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * 14) * vol)


def snare(tr, t0, vol=.22):
    n = int(.22 * SR)
    t = np.arange(n) / SR
    nz = sosfilt(butter(2, [900, 7000], 'bandpass', fs=SR, output='sos'), rng.standard_normal(n))
    tr.add(t0, (nz * 1.6 * np.exp(-t * 20) + osc('tri', 185, t) * .5 * np.exp(-t * 30)) * vol)


def hat(tr, t0, vol=.06, length=.05):
    n = int(length * SR)
    t = np.arange(n) / SR
    nz = sosfilt(butter(2, 7000, 'highpass', fs=SR, output='sos'), rng.standard_normal(n))
    tr.add(t0, nz * np.exp(-t * 70) * vol)


def swish(tr, t0, dur=.3, vol=.08, lo=800, hi=6000):
    n = int(dur * SR)
    out = np.zeros(n)
    nz = rng.standard_normal(n)
    for k in range(8):
        a, b = k * n // 8, (k + 1) * n // 8
        f = lo * (hi / lo) ** (k / 7)
        out[a:b] = sosfilt(butter(2, [f * .7, min(f * 1.4, SR / 2 - 100)], 'bandpass', fs=SR, output='sos'), nz[a:b])
    t = np.arange(n) / SR
    tr.add(t0, out * np.sin(np.pi * t / dur) * vol)


# ---------------------------------------------------------------- the score

AM, F, C, G, E, DM = [57, 60, 64], [53, 57, 60], [60, 64, 67], [55, 59, 62], [52, 56, 59], [50, 53, 57]
ROOT = {id(AM): 45, id(F): 41, id(C): 48, id(G): 43, id(E): 40, id(DM): 38}
# one chord a bar, 24 bars; bar 7 lasts a bar and a half, so the later sections start on the scene changes
CHORDS = [AM, AM, F, G, AM, F, C, G, DM, E, AM, AM, F, C, G, AM, F, G, C, AM, F, G, C, C]
LENGTH = [1.5 if b == 7 else 1 for b in range(len(CHORDS))]
START = np.concatenate([[0], np.cumsum(LENGTH)]) * BAR


def bar_t(b, beat=0.):
    return START[b] + beat * BEAT


def score():
    pad, arp, bass, lead, bells, drums = Track(), Track(.25), Track(), Track(-.15), Track(-.2), Track()
    for b, ch in enumerate(CHORDS):
        t0, nb = bar_t(b), int(4 * LENGTH[b])
        # pad all the way through, a little brighter from the ledger on
        for m in ch:
            pad.note(t0, nb * BEAT - .05, m, 'pulse', .028 if b < 11 else .034, a=.35, d=.4, s=.8, r=.5, duty=.5)
            pad.note(t0, nb * BEAT - .05, m + .07, 'pulse', .02, a=.35, d=.4, s=.8, r=.5, duty=.5)
        root = ROOT[id(ch)]
        # arpeggio: from the title, eighths; sixteenths in the ledger and the contribute sections
        if 2 <= b < 8 or 21 <= b < 23:
            pat = [0, 1, 2, 3, 2, 1, 0, 2]
            for k in range(2 * nb):
                m = (ch + [ch[0] + 12])[pat[k % 8]] + 12
                arp.note(t0 + k * BEAT / 2, BEAT / 2 * .8, m, 'pulse', .05, d=.05, s=.4, r=.05, duty=.125)
        elif 8 <= b < 11:
            for k in range(nb):
                arp.note(t0 + k * BEAT, BEAT * .5, ch[k % 3] + 12, 'pulse', .035, d=.1, s=.3, r=.1, duty=.125)
        elif 11 <= b < 21:
            pat = [0, 1, 2, 3, 2, 1, 2, 3] * 2
            for k in range(4 * nb):
                m = (ch + [ch[0] + 12])[pat[k % 16]] + 12
                arp.note(t0 + k * BEAT / 4, BEAT / 4 * .8, m, 'pulse', .04, d=.04, s=.4, r=.04, duty=.125)
        # bass from the middle of bar 4 (how it works)
        if b == 4:
            bass.note(t0 + 2 * BEAT, 2 * BEAT, root, 'tri', .22, a=.01, d=.2, s=.7, r=.1)
        elif 5 <= b < 8 or 11 <= b < 23:
            for k in range(nb if b < 11 else 2 * nb):
                step = BEAT if b < 11 else BEAT / 2
                m = root + (12 if b >= 11 and k % 4 == 2 else 0)
                bass.note(t0 + k * step, step * .85, m, 'tri', .24, a=.005, d=.1, s=.7, r=.05)
        elif 8 <= b < 11:
            bass.note(t0, BAR * .95, root, 'tri', .2, a=.05, d=.3, s=.8, r=.3)
        elif b == 23:
            bass.note(t0, BAR * 1.2, root, 'tri', .22, a=.01, d=.4, s=.7, r=1.0)
        # drums
        if 5 <= b < 8:
            for k in range(nb):
                if k % 4 in (0, 2):
                    kick(drums, t0 + k * BEAT, .32)
                hat(drums, t0 + k * BEAT + BEAT / 2, .04)
        elif 8 <= b < 11:
            for k in range(16):
                hat(drums, t0 + k * BEAT / 4, .025 if k % 4 else .04, .03)
        elif 11 <= b < 22:
            for k in range(4):
                kick(drums, t0 + k * BEAT, .38 if k in (0, 2) else .22)
                if k in (1, 3):
                    snare(drums, t0 + k * BEAT, .16 if b < 16 else .19)
                for h in range(2):
                    hat(drums, t0 + k * BEAT + h * BEAT / 2, .045 if h else .03)
            if b in (15, 21):
                for k in range(4):
                    snare(drums, t0 + 3 * BEAT + k * BEAT / 4, .1 + .03 * k)
        elif b == 22:
            kick(drums, t0, .4)
    # the bell motif over the archive
    for beat, m in ((0, 69), (1.5, 76), (3, 72), (5, 71), (6, 69)):
        bells.bell(bar_t(0, beat) + .3, m, .1)
    # the lead tune for "anyone can contribute"
    tune = [(16, [(0, 1, 72), (1, 1, 69), (2, 1, 72), (3, 1, 77)]),
            (17, [(0, 1, 74), (1, 1, 71), (2, 1, 74), (3, 1, 79)]),
            (18, [(0, 2, 76), (2, 1, 79), (3, 1, 76)]),
            (19, [(0, 1, 72), (1, 1, 76), (2, 2, 81)]),
            (20, [(0, 1, 81), (1, 1, 79), (2, 1, 77), (3, 1, 76)]),
            (21, [(0, 2, 74), (2, 1, 71), (3, 1, 74)]),
            (22, [(0, 4, 72)])]
    for b, notes in tune:
        for beat, dur, m in notes:
            lead.note(bar_t(b, beat), dur * BEAT * .92, m, 'pulse', .055, a=.01, d=.12, s=.55, r=.12, duty=.25, vib=.004)
    bells.bell(bar_t(23), 84, .1, 1.2)
    bells.bell(bar_t(23) + .02, 79, .08, 1.2)
    return [pad, arp, bass, lead, bells, drums]


def sfx():
    tr = Track()
    ws = S[1]
    for i, m in enumerate([64, 67, 69, 72, 74, 76, 79, 81, 84, 86, 88, 91]):    # the wordmark letters landing
        tr.note(ws + .25 + i * .08 + .14, .045, m, 'pulse', .045, d=.03, s=.3, r=.03, duty=.25)
    swish(tr, ws + 2.25, .3, .05)                                                # "unsolved" struck out
    for i, m in enumerate([69, 72, 76, 81]):                                     # the four steps
        tr.note(S[2] + METHOD_STEPS + .2 + i * .95, .12, m, 'tri', .08, d=.1, s=.2, r=.1)
    tr.bell(S[3] + 4.6, 81, .07)                                                 # "when he is sober"
    tr.bell(S[3] + 4.62, 88, .04)
    swish(tr, S[4] + .4, 3.4, .025, 400, 5000)                                   # the timeline filling
    tr.bell(S[4] + 5 + 1.3, 84, .06)                                             # the counts land
    for i, m in enumerate([72, 74, 76, 79, 81]):                                 # five ways in
        tr.note(S[5] + 1.5 + i * .7, .1, m, 'tri', .07, d=.08, s=.2, r=.08)
    for i, m in enumerate([67, 72, 76]):                                         # issue, pull request, email
        tr.note(S[5] + 7 + .15 + i * .9, .09, m, 'pulse', .04, d=.06, s=.3, r=.06, duty=.5)
    tr.bell(S[5] + 10.6 + 1.75, 88, .06)                                         # the star
    tr.bell(S[6] + 2.4, 84, .06)                                                 # the address
    return tr


# ---------------------------------------------------------------- the mix

def reverb(x, seconds=1.4, seed=0):
    r = np.random.default_rng(seed)
    n = int(seconds * SR)
    t = np.arange(n) / SR
    ir = r.standard_normal(n) * np.exp(-t * 4.2)
    ir[:int(.012 * SR)] = 0
    ir /= np.sqrt((ir ** 2).sum())
    return fftconvolve(x, ir)[:len(x)]


def stereo(tr):
    l, r = np.cos((tr.pan + 1) * np.pi / 4), np.sin((tr.pan + 1) * np.pi / 4)
    return np.stack([tr.x * l, tr.x * r], 1) * np.sqrt(2)


TEMPO = 1.05


def read_take(path):
    """A take at SR, sped up by TEMPO with its pitch kept (ffmpeg's atempo)."""
    pcm = subprocess.run(['ffmpeg', '-v', 'error', '-i', str(path), '-af', f'atempo={TEMPO}', '-ar', str(SR), '-ac', '1',
                          '-f', 's16le', '-'], capture_output=True, check=True).stdout
    return np.frombuffer(pcm, np.int16).astype(np.float64) / 32768


def load_vo(vo_dir):
    lines = json.loads((HERE / 'vo.json').read_text(encoding='utf8'))['lines']
    out = np.zeros(N)
    spans = []
    hp = butter(2, 80, 'highpass', fs=SR, output='sos')
    for ln in lines:
        take = Path(vo_dir) / f"{ln['id']}_{ln['take']}"
        take = take.with_suffix('.flac') if take.with_suffix('.flac').exists() else take.with_suffix('.wav')
        a = sosfilt(hp, read_take(take))
        loud = np.abs(a) > .02
        a *= .12 / np.sqrt((a[loud] ** 2).mean())                  # the same speech level for every line
        a = a[max(0, np.argmax(loud) - int(.04 * SR)):]           # the speech starts at 'at'
        i = int(ln['at'] * SR)
        k = min(len(a), N - i)
        out[i:i + k] += a[:k]
        spans.append((ln['at'], ln['at'] + k / SR))
    return out, spans


def duck(spans, depth=.26, att=.12, rel=.45):
    g = np.ones(N)
    t = np.arange(N) / SR
    for a, b in spans:
        x = np.clip((t - (a - att)) / att, 0, 1) * np.clip(1 - (t - b) / rel, 0, 1)
        g = np.minimum(g, 1 - (1 - depth) * x)
    return g


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('out')
    ap.add_argument('--vo', default=str(HERE / 'vo'), help='folder of voiceover takes (default: vo/)')
    ap.add_argument('--stems', help='also write music.wav, sfx.wav and vo.wav here')
    args = ap.parse_args()
    tracks = score()
    music = sum(stereo(tr) for tr in tracks)
    lp = butter(2, 7500, 'lowpass', fs=SR, output='sos')
    music = sosfilt(lp, music, axis=0)
    music += np.stack([reverb(music[:, 0], seed=1), reverb(music[:, 1], seed=2)], 1) * .22
    fx = stereo(sfx())
    fx += np.stack([reverb(fx[:, 0], seed=3), reverb(fx[:, 1], seed=4)], 1) * .25
    vo, spans = load_vo(args.vo)
    vo = np.stack([vo, vo], 1)
    vo += np.stack([reverb(vo[:, 0], .6, 5), reverb(vo[:, 1], .6, 6)], 1) * .05
    g = duck(spans)[:, None]
    t = (np.arange(N) / SR)[:, None]
    fade = np.clip(t / .5, 0, 1) * np.clip((DUR - t) / 1.2, 0, 1)
    mix = (music * .9 * g + fx * (.5 + .5 * g) + vo) * fade
    peak = np.abs(mix).max()
    mix = np.tanh(mix / peak * 1.1) / np.tanh(1.1) * .84                # soft ceiling at -1.5 dBFS, under AAC
    wavfile.write(args.out, SR, (mix * 32767).astype(np.int16))
    if args.stems:
        d = Path(args.stems)
        d.mkdir(parents=True, exist_ok=True)
        for name, x in (('music', music * .9 * g * fade), ('sfx', fx * fade), ('vo', vo * fade)):
            wavfile.write(d / f'{name}.wav', SR, (np.clip(x / peak, -1, 1) * 32767).astype(np.int16))
    print(f'wrote {args.out}: {DUR:.0f} s, {len(spans)} voiceover lines')


if __name__ == '__main__':
    main()
