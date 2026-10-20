"""Clean, neutral premium colour grade for the Daruma Jeans feed.

Reads every image in my-posts/ungraded/ and writes the graded version to my-posts/.
Run again any time you add or replace an image (put the new original in my-posts/ungraded/ first).

    python3 grade.py
"""
import pathlib
import numpy as np
from PIL import Image

SRC = pathlib.Path(__file__).parent / "my-posts" / "ungraded"
DST = SRC.parent

# ---- look settings: clean, neutral, premium ---------------------------
NEUTRALISE = 0.8          # how much of each photo's own colour cast to remove first (0–1)
TARGET_MID = 0.46         # every photo is brought to the same mid brightness
WARMTH = (1.005, 1.0, 1.0)    # R, G, B gains: neutral, a hair warm
CONTRAST = 0.30           # crisper S-curve
BLACK, WHITE = 0.018, 0.978   # deep clean blacks, crisp whites (no muddy matte)
SHADOW_TINT = (-0.004, 0.000, 0.006)    # barely cool shadows
HIGHLIGHT_TINT = (0.008, 0.005, -0.004) # clean, softly warm highlights
SATURATION = 0.90         # restrained but not dull
KEEP_RED = 1.05           # brand red (dragon, Daruma, torii) stays strong
CALM_SKY = 0.80           # bright blues muted slightly; dark indigo denim untouched
GRAIN = 0.004

# Per-photo exceptions. A big blue sky reads as a 'colour cast', so photo 05 keeps most of its own colour.
NEUTRALISE_OVERRIDE = {"05.jpg": 0.15}
# ----------------------------------------------------------------------------


def lum(a):
    return a[..., 0] * 0.2126 + a[..., 1] * 0.7152 + a[..., 2] * 0.0722


def grade(img, neutralise=NEUTRALISE):
    a = np.asarray(img.convert("RGB")).astype(np.float32) / 255

    # 1. remove part of each photo's own colour cast, measured on its midtones
    l = lum(a)
    mid = (l > 0.12) & (l < 0.88)
    means = a[mid].mean(axis=0) if mid.any() else a.reshape(-1, 3).mean(axis=0)
    gains = (means.mean() / np.maximum(means, 1e-4)) ** neutralise
    a = np.clip(a * gains, 0, 1)

    # 2. match brightness across the feed
    m = float(np.median(lum(a)))
    p = np.clip(np.log(TARGET_MID) / np.log(max(min(m, 0.95), 0.05)), 0.75, 1.35)
    a = a ** p

    # 3. shared warm white balance
    a = np.clip(a * np.array(WARMTH, dtype=np.float32), 0, 1)

    # 4. tone curve: gentle S, lifted blacks, rolled-off highlights
    s = a * a * (3 - 2 * a)
    a = a + (s - a) * CONTRAST
    a = BLACK + a * (WHITE - BLACK)

    # 5. split toning
    l = lum(a)[..., None]
    a = a + np.array(SHADOW_TINT, dtype=np.float32) * (1 - l) ** 2 + np.array(HIGHLIGHT_TINT, dtype=np.float32) * l ** 2

    # 6. saturation, keeping brand red strong
    l = lum(a)[..., None]
    red = np.clip((a[..., 0] - np.maximum(a[..., 1], a[..., 2])) * 4, 0, 1)[..., None]
    sat = SATURATION + (KEEP_RED - SATURATION) * red
    bright_blue = (np.clip((a[..., 2] - np.maximum(a[..., 0], a[..., 1])) * 4, 0, 1) * np.clip((lum(a) - 0.35) * 3, 0, 1))[..., None]
    sat = sat * (1 - (1 - CALM_SKY) * bright_blue)
    a = l + (a - l) * sat

    # 7. fine film grain
    rng = np.random.default_rng(7)
    a = a + rng.normal(0, GRAIN, a.shape[:2])[..., None]

    return Image.fromarray((np.clip(a, 0, 1) * 255 + 0.5).astype(np.uint8))


if __name__ == "__main__":
    for f in sorted(SRC.glob("*.jpg")):
        grade(Image.open(f), NEUTRALISE_OVERRIDE.get(f.name, NEUTRALISE)).save(DST / f.name, quality=95)
        print("graded", f.name)
