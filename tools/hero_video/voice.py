"""Render the hero video's voiceover lines (vo.json) with Chatterbox TTS, a few takes per line.

    <venv with chatterbox-tts>/python tools/hero_video/voice.py OUTDIR [--takes 3] [--only a1,b1]

Chatterbox (Resemble AI, MIT) speaks every line in the voice of narrator.wav: a low British female voice that
was designed, not recorded, with OmniVoice (k2-fsa; weights CC BY-NC) from the description "female, middle-aged,
low pitch, british accent". No real person's voice is involved. A line's "say" field, where present, is the
spelling the model is given (for names it would mispronounce), and "seeds" fixes the seed of each take. Each take
is OUTDIR/<id>_<k>.wav at 24 kHz. Takes are seeded, so a re-run on the same machine gives the same audio. The take
vo.json picks for each line (checked with Whisper) is kept in vo/ as FLAC, and audio.py reads it from there.
Needs a GPU-friendly venv with chatterbox-tts (PyTorch 2.6); the voice was rendered on an RTX 3060.
"""
import argparse
import json
import os
from pathlib import Path

os.environ.setdefault('HF_HUB_OFFLINE', '1')

import soundfile as sf  # noqa: E402
import torch  # noqa: E402
from chatterbox.tts import ChatterboxTTS  # noqa: E402

HERE = Path(__file__).resolve().parent


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('out')
    ap.add_argument('--takes', type=int, default=3)
    ap.add_argument('--only', default='')
    ap.add_argument('--exaggeration', type=float, default=0.4)
    ap.add_argument('--cfg', type=float, default=0.5)
    ap.add_argument('--ref', default=str(HERE / 'narrator.wav'))
    args = ap.parse_args()
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    lines = json.loads((HERE / 'vo.json').read_text(encoding='utf8'))['lines']
    only = set(filter(None, args.only.split(',')))
    model = ChatterboxTTS.from_pretrained(device='cuda' if torch.cuda.is_available() else 'cpu')
    for ln in lines:
        if only and ln['id'] not in only:
            continue
        for k in range(args.takes):
            seeds = ln.get('seeds', [])
            torch.manual_seed(seeds[k] if k < len(seeds) else 1000 * k + sum(map(ord, ln['id'])))
            wav = model.generate(ln.get('say', ln['text']), audio_prompt_path=args.ref,
                                 exaggeration=args.exaggeration, cfg_weight=args.cfg)
            a = wav.squeeze(0).cpu().numpy()
            sf.write(out / f"{ln['id']}_{k}.wav", a, model.sr)
            print(f"{ln['id']}_{k}  {len(a) / model.sr:5.2f}s  {ln['text']}", flush=True)


if __name__ == '__main__':
    main()
