"""Colour-match the feed photos within each set.

Each set (one row of the grid) is pulled toward its own shared look: the average
colour, brightness and contrast of the photos in that set. Sets keep their own character.

Reads my-posts/ungraded/, writes my-posts/.

    python3 match_sets.py
"""
import pathlib
import numpy as np
from PIL import Image

HERE = pathlib.Path(__file__).parent
SRC, DST = HERE / "my-posts" / "ungraded", HERE / "my-posts"

SETS = [["01", "02", "03"], ["04", "05", "06"], ["07", "08", "09"], ["10", "11", "12"], ["13", "14", "15"]]
STRENGTH_L = 0.45      # how far brightness/contrast move toward the set's look (0–1)
STRENGTH_AB = 0.70     # how far colour moves toward the set's look (0–1)
# Photos that are mostly a bright background. Full matching would grey them out, so instead their
# light areas are balanced to the clean whites of the other photos in the same set.
LIGHT_MATCH = {"08"}


# --- sRGB <-> CIELAB ---------------------------------------------------------
M = np.array([[0.4124, 0.3576, 0.1805], [0.2126, 0.7152, 0.0722], [0.0193, 0.1192, 0.9505]])
WHITE = np.array([0.95047, 1.0, 1.08883])


def to_lab(rgb):
    c = rgb / 255.0
    c = np.where(c > 0.04045, ((c + 0.055) / 1.055) ** 2.4, c / 12.92)
    xyz = c @ M.T / WHITE
    f = np.where(xyz > 0.008856, np.cbrt(xyz), 7.787 * xyz + 16 / 116)
    return np.stack([116 * f[..., 1] - 16, 500 * (f[..., 0] - f[..., 1]), 200 * (f[..., 1] - f[..., 2])], -1)


def to_rgb(lab):
    fy = (lab[..., 0] + 16) / 116
    f = np.stack([fy + lab[..., 1] / 500, fy, fy - lab[..., 2] / 200], -1)
    xyz = np.where(f ** 3 > 0.008856, f ** 3, (f - 16 / 116) / 7.787) * WHITE
    c = xyz @ np.linalg.inv(M).T
    c = np.where(c > 0.0031308, 1.055 * np.clip(c, 0, None) ** (1 / 2.4) - 0.055, 12.92 * c)
    return np.clip(c * 255 + 0.5, 0, 255).astype(np.uint8)


def stats(lab):
    flat = lab.reshape(-1, 3)
    return flat.mean(0), flat.std(0) + 1e-6


def light_mean(rgb):
    px = rgb.reshape(-1, 3)
    return px[px.mean(1) > 150].mean(0)


def match_light(src_rgb, target_light):
    gains = target_light / light_mean(src_rgb)
    return np.clip(src_rgb * gains, 0, 255).astype(np.uint8)


if __name__ == "__main__":
    for group in SETS:
        labs = {n: to_lab(np.asarray(Image.open(SRC / f"{n}.jpg").convert("RGB")).astype(np.float64)) for n in group}
        st = {n: stats(l) for n, l in labs.items()}
        t_mu = np.mean([s[0] for s in st.values()], 0)
        t_sd = np.mean([s[1] for s in st.values()], 0)
        k = np.array([STRENGTH_L, STRENGTH_AB, STRENGTH_AB])
        for n, lab in labs.items():
            if n in LIGHT_MATCH:
                continue
            mu, sd = st[n]
            new_mu = mu + (t_mu - mu) * k
            new_sd = sd + (t_sd - sd) * k
            out = (lab - mu) / sd * new_sd + new_mu
            Image.fromarray(to_rgb(out)).save(DST / f"{n}.jpg", quality=95)
            print(f"set {group}: {n}.jpg matched")
        for n in [n for n in group if n in LIGHT_MATCH]:
            others = [np.asarray(Image.open(DST / f"{m}.jpg").convert("RGB")).astype(np.float64) for m in group if m not in LIGHT_MATCH]
            target = np.mean([light_mean(o) for o in others], 0)
            src = np.asarray(Image.open(SRC / f"{n}.jpg").convert("RGB")).astype(np.float64)
            Image.fromarray(match_light(src, target)).save(DST / f"{n}.jpg", quality=95)
            print(f"set {group}: {n}.jpg matched by its light areas")
