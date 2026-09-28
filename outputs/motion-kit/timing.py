"""Time a motion piece to its narration.

Usage: python3 outputs/motion-kit/timing.py outputs/<motion-folder>

Reads SEGMENTS, NARRATION, VOICE and LENGTH from the folder's content.py,
speaks every narration line with the local Kokoro voice (offline), measures
each clip, and works out how long each segment of the animation should last
in the finished video so every line has room. Writes timing.json and the
clips to narration/.

The animation is authored on a short "design" timeline. Each segment keeps its
entrances at their authored speed (the first `din` seconds) and its exit (the
last 0.35 seconds); the extra time is spent holding the finished frame, so
nothing moves more slowly, it just stays on screen longer.
"""
import importlib.util
import json
import pathlib
import re
import subprocess
import sys

KIT = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(KIT.parent / "explainer-kit"))
SPEAK = pathlib.Path.home() / "tools/kokoro-tts/speak"


def load(folder):
    spec = importlib.util.spec_from_file_location("content", folder / "content.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def spoken(text):
    """Narration text as it should be said: strip quote marks the voice would stumble on."""
    return re.sub(r"[“”]", "", text)


def main():
    folder = pathlib.Path(sys.argv[1]).resolve()
    m = load(folder)
    ndir = folder / "narration"
    ndir.mkdir(exist_ok=True)
    lines = [{"id": key, "text": spoken(getattr(m, "SAY", {}).get(key, c.text))} for seg, key, c in m.NARRATION]
    (ndir / "lines.json").write_text(json.dumps(lines, ensure_ascii=False, indent=1))
    subprocess.run([str(SPEAK), "--script", str(ndir / "lines.json"), "--outdir", str(ndir), "-v", m.VOICE, "-l", "en-gb", "-s", str(getattr(m, "VOICE_SPEED", 1.07))],
                   check=True, capture_output=True)
    # trim the silence Kokoro leaves around each clip, and measure what is left
    import numpy as np
    from scipy.io import wavfile
    dur = {}
    for ln in lines:
        f = ndir / f"{ln['id']}.wav"
        rate, x = wavfile.read(f)
        y = np.abs(x.astype(float))
        on = np.where(y > y.max() * 0.02)[0]
        pad = int(0.04 * rate)
        x = x[max(0, on[0] - pad):min(len(x), on[-1] + pad)]
        wavfile.write(f, rate, x)
        dur[ln["id"]] = round(len(x) / rate, 3)
    (ndir / "durations.json").write_text(json.dumps(dur, indent=1))

    # [(a, b, din[, read]), ...] on the design timeline; first is the title, last the end card.
    # `read` is the least time the segment needs on screen for its text to be read.
    segs = [tuple(s) + (None,) * (4 - len(s)) for s in m.SEGMENTS]
    need = {}
    for seg, key, c in m.NARRATION:
        need[seg] = need.get(seg, 0) + dur[key] + 0.25
    total = m.LENGTH
    title_len, end_len = 2.3, 2.9
    mids = range(1, len(segs) - 1)
    want = {}
    for i in mids:
        a, b, _, read = segs[i]
        want[i] = max((b - a) * 1.1, read or 1.3, need.get(i, 0) + 0.7)
    room = total - title_len - end_len
    if sum(want.values()) > room:
        raise SystemExit(f"Narration needs {sum(want.values()):.1f}s but only {room:.1f}s is available; shorten the lines.")
    spare = room - sum(want.values())
    wsum = sum(want.values())
    real = [title_len] + [want[i] + spare * want[i] / wsum for i in mids] + [end_len]

    warp, start, narr = [], 0.0, []
    for i, ((a, b, din, _), L) in enumerate(zip(segs, real)):
        A, B = start, start + L
        dout = min(0.35, (b - a) * 0.2)
        din = min(din, (b - a) - dout - 0.02)
        pts = [(A, a), (A + din, a + din), (B - dout, b - dout), (B, b)]
        for p in pts:
            if not warp or p[0] > warp[-1][0] + 1e-6:
                warp.append(p)
        t = A + 0.45
        for seg, key, c in m.NARRATION:
            if seg == i:
                narr.append({"key": key, "start": round(t, 3), "dur": dur[key], "text": c.text})
                t += dur[key] + 0.25
        start = B
    timing = {"length": total, "voice": m.VOICE,
              "segments": [{"design": [a, b], "real": [round(sum(real[:i]), 3), round(sum(real[:i + 1]), 3)]}
                           for i, (a, b, _, _) in enumerate(segs)],
              "warp": [[round(x, 4), round(y, 4)] for x, y in warp], "narration": narr}
    (folder / "timing.json").write_text(json.dumps(timing, ensure_ascii=False, indent=1))
    spoken_s = sum(dur.values())
    print(f"timed {folder.name}: {len(narr)} lines, {spoken_s:.1f}s of speech in {total}s; segments "
          + " ".join(f"{r:.1f}" for r in real))


if __name__ == "__main__":
    main()
