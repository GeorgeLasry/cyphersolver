"""Score, sound effects and voiceover mix for the site's two videos.

    python tools/hero_video/audio.py OUT.wav [--cut hero|full] [--featured SLUG] [--vo DIR] [--stems DIR]

The score is original, written here for these videos: a chiptune in A minor at 96 bpm (2.5 s a bar), synthesised
from pulse, triangle, noise and bell voices. Each cut lists its bars in hero_video.CUTS[...]['bars'] as (section,
chord, length): the section says how the bar is played (the bell motif of the intro, the deciphering's sparse
quarters, the ledger's sixteenths and drums, a bar of the lead tune, the close), so the music follows the scenes.
The sound effects are timed from the scenes' own constants. The voiceover takes come from voice.py; the ones vo.json
names are kept in vo/ as <id>_<take>.flac (--vo points elsewhere, .flac or .wav). Each is sped up by TEMPO without
changing its pitch, its lead-in silence is trimmed, and its speech starts where the cut's 'vo' list puts it. The
music ducks under the voice. hero_video.py --cut ... --audio OUT.wav muxes the result into the video; --featured must
match, because the deciphering's ticks follow the passage's groups.
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
import hero_video as hv  # noqa: E402

HERE = Path(__file__).resolve().parent
SR = 44100
BEAT = 60 / 96
BAR = 4 * BEAT
N = 0              # samples in the cut, set by main()


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

CHORD = dict(AM=[57, 60, 64], F=[53, 57, 60], C=[60, 64, 67], G=[55, 59, 62], E=[52, 56, 59], DM=[50, 53, 57])
ROOT = dict(AM=45, F=41, C=48, G=43, E=40, DM=38)
# the lead tune for "anyone can contribute", one entry per 'tuneN' bar: (beat, beats, note)
TUNE = [[(0, 1, 72), (1, 1, 69), (2, 1, 72), (3, 1, 77)],
        [(0, 1, 74), (1, 1, 71), (2, 1, 74), (3, 1, 79)],
        [(0, 2, 76), (2, 1, 79), (3, 1, 76)],
        [(0, 1, 72), (1, 1, 76), (2, 2, 81)],
        [(0, 1, 81), (1, 1, 79), (2, 1, 77), (3, 1, 76)],
        [(0, 2, 74), (2, 1, 71), (3, 1, 74)]]
BELLS = [(0, 69), (1.5, 76), (3, 72), (5, 71), (6, 69)]    # the intro's motif: (beat, note)


def score(bars):
    pad, arp, bass, lead, bells, drums = Track(), Track(.25), Track(), Track(-.15), Track(-.2), Track()
    t0 = 0.
    for b, (sec, name, length) in enumerate(bars):
        ch, root, nb = CHORD[name], ROOT[name], int(round(4 * length))
        last = b + 1 == len(bars) or bars[b + 1][0][:4] != sec[:4]      # the last bar of its section
        busy = sec == 'ledger' or sec.startswith('tune')
        # pad all the way through, a little brighter from the ledger on
        for m in ch:
            pad.note(t0, nb * BEAT - .05, m, 'pulse', .034 if busy or sec == 'close' else .028, a=.35, d=.4, s=.8,
                     r=.5, duty=.5)
            pad.note(t0, nb * BEAT - .05, m + .07, 'pulse', .02, a=.35, d=.4, s=.8, r=.5, duty=.5)
        if sec == 'intro' and b == 0:
            for beat, m in BELLS:
                bells.bell(t0 + beat * BEAT + .3, m, .1)
        elif sec == 'decipher':
            # quarters, a held bass, sixteenth hats: the scan across the passage
            for k in range(nb):
                arp.note(t0 + k * BEAT, BEAT * .5, ch[k % 3] + 12, 'pulse', .035, d=.1, s=.3, r=.1, duty=.125)
            bass.note(t0, nb * BEAT * .95, root, 'tri', .2, a=.05, d=.3, s=.8, r=.3)
            for k in range(4 * nb):
                hat(drums, t0 + k * BEAT / 4, .025 if k % 4 else .04, .03)
        elif sec in ('build', 'drive'):
            pat = [0, 1, 2, 3, 2, 1, 0, 2]
            for k in range(2 * nb):
                m = (ch + [ch[0] + 12])[pat[k % 8]] + 12
                arp.note(t0 + k * BEAT / 2, BEAT / 2 * .8, m, 'pulse', .05, d=.05, s=.4, r=.05, duty=.125)
            for k in range(nb):
                bass.note(t0 + k * BEAT, BEAT * .85, root, 'tri', .24, a=.005, d=.1, s=.7, r=.05)
                if sec == 'drive':
                    if k % 4 in (0, 2):
                        kick(drums, t0 + k * BEAT, .32)
                    hat(drums, t0 + k * BEAT + BEAT / 2, .04)
        elif busy:
            pat = [0, 1, 2, 3, 2, 1, 2, 3] * 2
            for k in range(4 * nb):
                m = (ch + [ch[0] + 12])[pat[k % 16]] + 12
                arp.note(t0 + k * BEAT / 4, BEAT / 4 * .8, m, 'pulse', .04, d=.04, s=.4, r=.04, duty=.125)
            for k in range(2 * nb):
                m = root + (12 if k % 4 == 2 else 0)
                bass.note(t0 + k * BEAT / 2, BEAT / 2 * .85, m, 'tri', .24, a=.005, d=.1, s=.7, r=.05)
            for k in range(nb):
                kick(drums, t0 + k * BEAT, .38 if k in (0, 2) else .22)
                if k in (1, 3):
                    snare(drums, t0 + k * BEAT, .16 if sec == 'ledger' else .19)
                for h in range(2):
                    hat(drums, t0 + k * BEAT + h * BEAT / 2, .045 if h else .03)
            if last and nb == 4:
                for k in range(4):
                    snare(drums, t0 + 3 * BEAT + k * BEAT / 4, .1 + .03 * k)
            if sec.startswith('tune'):
                for beat, dur, m in TUNE[int(sec[4:]) - 1]:
                    if beat < nb:
                        lead.note(t0 + beat * BEAT, min(dur, nb - beat) * BEAT * .92, m, 'pulse', .055, a=.01, d=.12,
                                  s=.55, r=.12, duty=.25, vib=.004)
        elif sec == 'close':
            kick(drums, t0, .4)
            lead.note(t0, 4 * BEAT * .92, 72, 'pulse', .055, a=.01, d=.12, s=.55, r=.12, duty=.25, vib=.004)
            bass.note(t0, nb * BEAT, root, 'tri', .22, a=.01, d=.4, s=.7, r=1.0)
            bells.bell(t0 + 4 * BEAT, 84, .1, 1.2)
            bells.bell(t0 + 4 * BEAT + .02, 79, .08, 1.2)
        t0 += length * BAR
    return [pad, arp, bass, lead, bells, drums]


def sfx(cut):
    tr = Track()
    starts = {name: t for t, _, name in cut['scenes']}
    fns = {name: fn for _, fn, name in cut['scenes']}
    if 'decipher' in starts:
        s, D = starts['decipher'], hv.DEC
        swish(tr, s + D['snip'] - .1, .5, .04, 300, 3000)                           # the page gives way to its figures
        n = len(hv.FT['tokens'])
        dt = (D['scan_end'] - D['scan']) / n
        for k in range(n):                                                         # each group as it is read
            tr.note(s + D['scan'] + k * dt + dt * .4, .025, 88 + (k % 3) * 2, 'pulse', .018, d=.02, s=.3, r=.02)
        tr.bell(s + D['band'], 81, .07)                                            # the English
        tr.bell(s + D['band'] + .02, 88, .04)
    if 'method' in starts:
        for i, m in enumerate([69, 72, 76, 81]):                                   # the four steps
            tr.note(starts['method'] + hv.METHOD_STEPS + .2 + i * .95, .12, m, 'tri', .08, d=.1, s=.2, r=.1)
    if 'ledger' in starts:
        s, fn = starts['ledger'], fns['ledger']
        swish(tr, s + hv.SWEEP[0], hv.SWEEP[1], .025, 400, 5000)                   # the timeline filling
        for i in range(2):                                                         # the two entries named
            tr.note(s + fn.t_close + .7 + i * .9, .08, (76, 69)[i], 'tri', .07, d=.08, s=.2, r=.1)
        tr.bell(s + fn.t_stats + 1.3, 84, .06)                                     # the counts land
    if 'contribute' in starts:
        s = starts['contribute']
        for k in ('click', 'copy'):                                                # a row picked, the prompt copied
            tr.note(s + hv.PICK[k], .03, 84, 'pulse', .05, d=.02, s=.3, r=.02, duty=.5)
            tr.note(s + hv.PICK[k] + .05, .03, 91, 'pulse', .03, d=.02, s=.3, r=.02, duty=.5)
        ag = s + hv.CONTRIB_AGENT
        tr.note(ag + hv.AGENT['paste'], .08, 55, 'tri', .1, d=.06, s=.2, r=.06)    # pasted into Claude Code
        for i in range(len(hv.AGENT_LINES)):                                       # its steps
            tr.note(ag + hv.AGENT['first'] + i * hv.AGENT['step'], .03, 79 + 2 * i, 'pulse', .025, d=.02, s=.3, r=.02)
        tr.bell(ag + hv.AGENT['first'] + len(hv.AGENT_LINES) * hv.AGENT['step'], 88, .06)    # sent back
        tr.bell(s + hv.CONTRIB_CREDIT + 1.75, 88, .06)                             # the star
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


TEMPO = hv.TEMPO


def read_take(path):
    """A take at SR, sped up by TEMPO with its pitch kept (ffmpeg's atempo)."""
    pcm = subprocess.run(['ffmpeg', '-v', 'error', '-i', str(path), '-af', f'atempo={TEMPO}', '-ar', str(SR), '-ac', '1',
                          '-f', 's16le', '-'], capture_output=True, check=True).stdout
    return np.frombuffer(pcm, np.int16).astype(np.float64) / 32768


def load_vo(cut, vo_dir):
    lines = {ln['id']: ln for ln in json.loads((HERE / 'vo.json').read_text(encoding='utf8'))['lines']}
    out = np.zeros(N)
    spans = []
    hp = butter(2, 80, 'highpass', fs=SR, output='sos')
    for lid, at, _ in cut['vo']:
        ln = lines[lid]
        take = Path(vo_dir) / f"{ln['id']}_{ln['take']}"
        take = take.with_suffix('.flac') if take.with_suffix('.flac').exists() else take.with_suffix('.wav')
        a = sosfilt(hp, read_take(take))
        loud = np.abs(a) > .02
        a *= .12 / np.sqrt((a[loud] ** 2).mean())                  # the same speech level for every line
        a = a[max(0, np.argmax(loud) - int(.04 * SR)):]           # the speech starts at 'at'
        i = int(at * SR)
        k = min(len(a), N - i)
        out[i:i + k] += a[:k]
        spans.append((at, at + k / SR))
    return out, spans


def duck(spans, depth=.26, att=.12, rel=.45):
    g = np.ones(N)
    t = np.arange(N) / SR
    for a, b in spans:
        x = np.clip((t - (a - att)) / att, 0, 1) * np.clip(1 - (t - b) / rel, 0, 1)
        g = np.minimum(g, 1 - (1 - depth) * x)
    return g


def main():
    global N
    ap = argparse.ArgumentParser()
    ap.add_argument('out')
    ap.add_argument('--cut', choices=sorted(hv.CUTS), default='hero')
    ap.add_argument('--featured', help='the featured.json slug the video deciphers (default: this ISO week\'s)')
    ap.add_argument('--vo', default=str(HERE / 'vo'), help='folder of voiceover takes (default: vo/)')
    ap.add_argument('--stems', help='also write music.wav, sfx.wav and vo.wav here')
    args = ap.parse_args()
    cut = hv.CUTS[args.cut]
    dur = cut['dur']
    bars = sum(length for _, _, length in cut['bars']) * BAR
    if abs(bars - dur) > 1e-6:
        sys.exit(f'{args.cut}: the bars add up to {bars:.2f} s, the cut lasts {dur:.2f} s')
    hv.CUT, hv.DUR = cut, dur
    hv.LG = {**hv.ledger(), **hv.lists()}
    hv.FT = hv.featured(args.featured)
    N = int(dur * SR)
    tracks = score(cut['bars'])
    music = sum(stereo(tr) for tr in tracks)
    lp = butter(2, 7500, 'lowpass', fs=SR, output='sos')
    music = sosfilt(lp, music, axis=0)
    music += np.stack([reverb(music[:, 0], seed=1), reverb(music[:, 1], seed=2)], 1) * .22
    fx = stereo(sfx(cut))
    fx += np.stack([reverb(fx[:, 0], seed=3), reverb(fx[:, 1], seed=4)], 1) * .25
    vo, spans = load_vo(cut, args.vo)
    vo = np.stack([vo, vo], 1)
    vo += np.stack([reverb(vo[:, 0], .6, 5), reverb(vo[:, 1], .6, 6)], 1) * .05
    g = duck(spans)[:, None]
    t = (np.arange(N) / SR)[:, None]
    fade = np.clip(t / .5, 0, 1) * np.clip((dur - t) / 1.2, 0, 1)
    mix = (music * .9 * g + fx * (.5 + .5 * g) + vo) * fade
    peak = np.abs(mix).max()
    mix = np.tanh(mix / peak * 1.1) / np.tanh(1.1) * .84                # soft ceiling at -1.5 dBFS, under AAC
    wavfile.write(args.out, SR, (mix * 32767).astype(np.int16))
    if args.stems:
        d = Path(args.stems)
        d.mkdir(parents=True, exist_ok=True)
        for name, x in (('music', music * .9 * g * fade), ('sfx', fx * fade), ('vo', vo * fade)):
            wavfile.write(d / f'{name}.wav', SR, (np.clip(x / peak, -1, 1) * 32767).astype(np.int16))
    print(f'wrote {args.out}: {args.cut} cut, {dur:g} s, {len(spans)} voiceover lines, deciphering {hv.FT["slug"]}')


if __name__ == '__main__':
    main()
