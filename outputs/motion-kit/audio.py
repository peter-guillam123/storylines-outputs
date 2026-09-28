"""Score a Storylines motion piece: synthesise its soundtrack in code and add it to the video.

Usage: python3 outputs/motion-kit/audio.py outputs/<motion-folder> [--png]

Each motion folder's content.py defines score(A), which places instruments and
sound effects at times that match the animation. Everything is synthesised
here: no samples, no licensed music, no speech. The mix is normalised to
-16 LUFS (true peak -2 dB) and muxed into video.mp4 from video_silent.mp4.
--png also writes a spectrogram with the cue times marked, for checking sync.
"""
import importlib.util
import json
import pathlib
import subprocess
import sys

import numpy as np
from scipy import signal
from scipy.io import wavfile

SR = 48000
RNG = np.random.default_rng(7)
KIT = pathlib.Path(__file__).resolve().parent


def note(name):
    """'A2', 'C#4', 'Bb3' -> Hz"""
    names = {"C": -9, "D": -7, "E": -5, "F": -4, "G": -2, "A": 0, "B": 2}
    n, rest = names[name[0]], name[1:]
    while rest and rest[0] in "#b":
        n += 1 if rest[0] == "#" else -1
        rest = rest[1:]
    return 440.0 * 2 ** ((n + (int(rest) - 4) * 12) / 12)


def tt(dur):
    return np.arange(int(dur * SR)) / SR


def sos(kind, f, order=2):
    return signal.butter(order, f, btype=kind, fs=SR, output="sos")


def filt(x, kind, f, order=2):
    return signal.sosfilt(sos(kind, f, order), x)


def noise(dur):
    return RNG.standard_normal(int(dur * SR))


def adsr(n, a=0.01, d=0.1, s=0.7, r=0.2):
    e = np.full(n, s, dtype=float)
    na, nd, nr = int(a * SR), int(d * SR), int(r * SR)
    na = min(na, n); e[:na] = np.linspace(0, 1, na, endpoint=False)
    nd = min(nd, n - na); e[na:na + nd] = np.linspace(1, s, nd, endpoint=False)
    if nr and n > nr:
        e[-nr:] *= np.linspace(1, 0, nr) ** 2
    return e


# ---------------------------------------------------------------- instruments
def saw(f, dur, detune=0.0):
    t = tt(dur)
    k_max = int(min(40, 18000 / max(f, 1)))
    x = np.zeros_like(t)
    ph = RNG.uniform(0, 2 * np.pi)
    for k in range(1, k_max + 1):
        x += np.sin(2 * np.pi * k * f * (1 + detune) * t + ph * k) / k
    return x * 0.6


def pad(freqs, dur, cutoff=1400, a=0.8, r=1.2, bright_end=None):
    """Detuned saw pad; cutoff can open or close over the note (bright_end)."""
    x = sum(saw(f, dur, d) for f in freqs for d in (-0.004, 0.0, 0.0045)) / (3 * len(freqs))
    dark = filt(x, "lowpass", cutoff, 2)
    if bright_end:
        bright = filt(x, "lowpass", bright_end, 2)
        w = np.linspace(0, 1, len(x))
        dark = dark * (1 - w) + bright * w
    return dark * adsr(len(x), a, 0.3, 0.85, r)


def piano(f, dur=2.5, vel=1.0):
    t = tt(dur)
    x = np.zeros_like(t)
    for k in range(1, 9):
        fk = k * f * np.sqrt(1 + 0.0004 * k * k)
        if fk > 16000:
            break
        x += np.sin(2 * np.pi * fk * t) / k ** 1.3 * np.exp(-t * (0.9 + 0.55 * k))
    hammer = filt(noise(0.02), "lowpass", 2500) * np.linspace(1, 0, int(0.02 * SR)) * 0.15
    x[:len(hammer)] += hammer
    x *= np.minimum(1, t / 0.004)
    return x * 0.35 * vel


def thud(f0=90, f1=42, dur=0.6, decay=7, click=0.3):
    t = tt(dur)
    f = f1 + (f0 - f1) * np.exp(-t * 18)
    x = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * decay)
    c = filt(noise(0.012), "lowpass", 1800) * np.linspace(1, 0, int(0.012 * SR)) * click
    x[:len(c)] += c
    return x


def stamp():
    x = thud(130, 55, 0.35, 12, 0.5)
    n = filt(noise(0.09), "bandpass", [700, 2600]) * np.exp(-tt(0.09) * 45) * 0.9
    x[:len(n)] += n
    return x * 0.9


def blip(f, dur=0.16, glide=1.0):
    t = tt(dur)
    fr = f * (1 + (glide - 1) * t / dur)
    return np.sin(2 * np.pi * np.cumsum(fr) / SR) * np.exp(-t * 22) * np.minimum(1, t / 0.002)


def tick(bright=5000, dur=0.012, gain=1.0):
    return filt(noise(dur), "highpass", bright) * np.linspace(1, 0, int(dur * SR)) ** 2 * gain


def chime(f, dur=2.2):
    t = tt(dur)
    x = (np.sin(2 * np.pi * f * t) + 0.35 * np.sin(2 * np.pi * 2.76 * f * t) * np.exp(-t * 3)
         + 0.15 * np.sin(2 * np.pi * 5.4 * f * t) * np.exp(-t * 6))
    return x * np.exp(-t * 2.2) * np.minimum(1, t / 0.003) * 0.4


def sweep_noise(dur, f_from, f_to, q=1.2):
    """Band-limited noise whose centre moves from f_from to f_to (log), with a swell."""
    n = noise(dur)
    centres = np.geomspace(150, 9000, 10)
    out = np.zeros_like(n)
    t = np.linspace(0, 1, len(n))
    c = np.exp(np.log(f_from) + (np.log(f_to) - np.log(f_from)) * t)
    for fc in centres:
        band = filt(n, "bandpass", [fc / (1 + 0.5 / q), min(fc * (1 + 0.5 / q), SR / 2 - 100)])
        w = np.exp(-(np.log(fc) - np.log(c)) ** 2 / 0.35)
        out += band * w
    return out * np.sin(np.pi * t) ** 2


def sea(dur, cutoff=380):
    b = np.cumsum(noise(dur)) * 0.02
    b = filt(b - np.mean(b), "highpass", 25)
    b = filt(b, "lowpass", cutoff)
    t = tt(dur)
    return b / (np.max(np.abs(b)) + 1e-9) * (0.6 + 0.4 * np.sin(2 * np.pi * 0.11 * t + 1.3))


def bass_pulse(freq_at, t0, t1, step=0.25, length=0.2, cutoff=420):
    """8th-note bass; freq_at(t) gives the note at each step."""
    hits = []
    t = t0
    while t < t1 - 1e-6:
        f = freq_at(t)
        x = filt(saw(f, length), "lowpass", cutoff) * adsr(int(length * SR), 0.004, 0.08, 0.35, 0.06)
        hits.append((t, x))
        t += step
    return hits


# ---------------------------------------------------------------- mixer
class Mix:
    def __init__(self, dur, T=lambda t: t):
        self.n = int(dur * SR)
        self.T = T
        self.bus = {k: np.zeros((2, self.n)) for k in ("music", "fx", "verb", "voice")}

    def add(self, x, t0, bus="fx", pan=0.0, gain=1.0, verb=0.0, real=False):
        """t0 is on the design timeline unless real=True (then it is finished-video time)."""
        i = int((t0 if real else self.T(t0)) * SR)
        if i >= self.n:
            return
        x = np.asarray(x, dtype=float)
        if x.ndim == 1:
            th = (pan + 1) * np.pi / 4
            x = np.vstack([x * np.cos(th), x * np.sin(th)])
        j = min(self.n, i + x.shape[1])
        self.bus[bus][:, i:j] += x[:, :j - i] * gain
        if verb:
            self.bus["verb"][:, i:j] += x[:, :j - i] * gain * verb

    def render(self, music_gain=1.0, fx_gain=1.0, rt=1.8, fade_out=0.6):
        ir_t = tt(rt)
        irs = [filt(noise(rt), "lowpass", 5500) * np.exp(-ir_t * 6.9 / rt) for _ in range(2)]
        wet = np.vstack([signal.fftconvolve(self.bus["verb"][c], irs[c])[:self.n] for c in range(2)])
        wet /= (np.max(np.abs(wet)) + 1e-9)
        # duck the music (and a little of the effects) under the narration
        v = np.abs(self.bus["voice"]).max(axis=0)
        k = int(0.25 * SR)
        env = np.convolve((v > 1e-3).astype(float), np.ones(k) / k, mode="same")
        env = np.clip(env * 1.6, 0, 1)
        duck_m, duck_f = 1 - 0.62 * env, 1 - 0.35 * env
        dry = self.bus["music"] * music_gain * duck_m + self.bus["fx"] * fx_gain * duck_f
        peak = np.max(np.abs(dry)) + 1e-9
        out = dry / peak + wet * 0.35 * duck_m
        vp = np.max(np.abs(self.bus["voice"])) + 1e-9
        out = out * 0.62 + self.bus["voice"] / vp * 0.95
        nf = int(fade_out * SR)
        out[:, -nf:] *= np.linspace(1, 0, nf) ** 2
        out = np.tanh(out * 1.1) / np.tanh(1.1)
        return (out / (np.max(np.abs(out)) + 1e-9) * 0.89).astype(np.float32)


class Kit:
    """What score(A) sees."""
    note = staticmethod(note)
    pad, piano, thud, stamp, blip, tick = map(staticmethod, (pad, piano, thud, stamp, blip, tick))
    chime, sweep_noise, sea, bass_pulse, saw, filt = map(staticmethod, (chime, sweep_noise, sea, bass_pulse, saw, filt))
    noise, tt, adsr = map(staticmethod, (noise, tt, adsr))


def main():
    folder = pathlib.Path(sys.argv[1]).resolve()
    spec = importlib.util.spec_from_file_location("content", folder / "content.py")
    sys.path.insert(0, str(KIT.parent / "explainer-kit"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    tj = folder / "timing.json"
    timing = json.loads(tj.read_text()) if tj.exists() else None
    length = timing["length"] if timing else mod.DURATION
    if timing and timing["warp"]:
        xs = np.array([p[0] for p in timing["warp"]]); ys = np.array([p[1] for p in timing["warp"]])
        T = lambda t_old: float(np.interp(t_old, ys, xs))
        Tinv = lambda t_real: float(np.interp(t_real, xs, ys))
    else:
        T = Tinv = lambda t: t
    m = Mix(length, T)
    A = Kit()
    A.mix = m
    A.T, A.Tinv, A.LEN = staticmethod(T), staticmethod(Tinv), length
    A.D = staticmethod(lambda t0, t1: T(t1) - T(t0))
    # narration: the clips timing.py made, placed at their times
    for n in (timing or {}).get("narration", []):
        rate, clip = wavfile.read(folder / "narration" / f"{n['key']}.wav")
        clip = clip.astype(float) / (np.iinfo(clip.dtype).max if clip.dtype.kind == "i" else 1.0)
        if clip.ndim > 1:
            clip = clip.mean(axis=1)
        clip = signal.resample_poly(clip, SR, rate)
        m.add(clip, n["start"], "voice", real=True)
    cues = mod.score(A) or []
    out = m.render(**getattr(mod, "MIX", {}))
    raw = folder / "score_raw.wav"
    wavfile.write(raw, SR, out.T)

    # two-pass loudness normalisation to -16 LUFS, true peak -2 dB
    target = "I=-16:TP=-2:LRA=11"
    r = subprocess.run(["ffmpeg", "-hide_banner", "-i", str(raw), "-af", f"loudnorm={target}:print_format=json",
                        "-f", "null", "-"], capture_output=True, text=True)
    js = json.loads(r.stderr[r.stderr.rindex("{"):r.stderr.rindex("}") + 1])
    af = (f"loudnorm={target}:measured_I={js['input_i']}:measured_TP={js['input_tp']}:"
          f"measured_LRA={js['input_lra']}:measured_thresh={js['input_thresh']}:offset={js['target_offset']}:linear=true")
    norm = folder / "score.wav"
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(raw), "-af", af, "-ar", str(SR), str(norm)], check=True)

    subs = []
    if timing and timing.get("narration"):
        def ts(x):
            return f"{int(x // 3600):02d}:{int(x % 3600 // 60):02d}:{x % 60:06.3f}"
        vtt = ["WEBVTT", ""]
        for i, n in enumerate(timing["narration"], 1):
            vtt += [str(i), f"{ts(n['start'])} --> {ts(n['start'] + n['dur'] + 0.2)} line:78%", n["text"], ""]
        (folder / "narration.vtt").write_text("\n".join(vtt))
        subs = ["-i", str(folder / "narration.vtt")]
    silent = folder / "video_silent.mp4"
    if not silent.exists():
        (folder / "video.mp4").rename(silent)
    smap = ["-map", "2:s", "-c:s", "mov_text", "-metadata:s:s:0", "language=eng", "-metadata:s:s:0", "title=Narration"] if subs else []
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(silent), "-i", str(norm)] + subs +
                   ["-map", "0:v", "-map", "1:a"] + smap +
                   ["-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-t", str(length), "-movflags", "+faststart",
                    str(folder / "video.mp4")], check=True)
    r = subprocess.run(["ffmpeg", "-hide_banner", "-i", str(folder / "video.mp4"), "-af", "loudnorm=print_format=json",
                        "-f", "null", "-"], capture_output=True, text=True)
    js2 = json.loads(r.stderr[r.stderr.rindex("{"):r.stderr.rindex("}") + 1])
    print(f"scored {folder.name}: {js2['input_i']} LUFS, true peak {js2['input_tp']} dB")

    if "--png" in sys.argv:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        mono = out.mean(axis=0)
        fig, ax = plt.subplots(2, 1, figsize=(16, 6), sharex=True, gridspec_kw={"height_ratios": [1, 2]})
        ax[0].plot(np.arange(len(mono)) / SR, mono, lw=0.3, color="k")
        ax[1].specgram(mono, NFFT=2048, Fs=SR, noverlap=1536, cmap="magma", vmin=-120)
        ax[1].set_ylim(20, 8000); ax[1].set_yscale("log")
        for c in cues:
            for a in ax:
                a.axvline(T(c), color="c", lw=0.6, alpha=0.7)
        for n in (timing or {}).get("narration", []):
            ax[0].axvspan(n["start"], n["start"] + n["dur"], color="orange", alpha=0.15)
        ax[1].set_xlabel("seconds (cyan lines: animation cue times; orange bands: narration)")
        fig.tight_layout()
        fig.savefig(folder / "score.png", dpi=90)


if __name__ == "__main__":
    main()
