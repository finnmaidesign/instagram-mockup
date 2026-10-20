#!/bin/bash
# Cuts my-posts/panorama.(jpg|png|webp) into 3 equal portrait images for Instagram.
# Double-click this file in Finder, or run it from Terminal. Needs python3 with Pillow.
set -euo pipefail
cd "$(dirname "$0")"

python3 - <<'EOF'
import pathlib, sys
from PIL import Image

src = next((p for p in (pathlib.Path(f"my-posts/panorama.{e}") for e in ("jpg", "png", "webp")) if p.exists()), None)
if not src:
    sys.exit("No my-posts/panorama.jpg / .png / .webp found.")

img = Image.open(src).convert("RGB")
w, h = img.size
third = w // 3
print(f"Panorama: {src} ({w} × {h}) → 3 slices of {third} × {h}")
if abs(third / h - 3 / 4) > 0.01:
    print("Note: slices are not exactly 3:4 (best is 9:4 overall, e.g. 3240 × 1440). Instagram will crop them a little.")

out = pathlib.Path("my-posts/to-post")
out.mkdir(exist_ok=True)
names = ["3-post-last_left", "2-post-second_middle", "1-post-first_right"]
for k, name in enumerate(names):
    img.crop((k * third, 0, (k + 1) * third, h)).save(out / f"{name}.jpg", quality=95)

print(f"\nDone → {out}")
print("Post them in this order so they line up left → right on the grid:")
print("  1st: 1-post-first_right.jpg")
print("  2nd: 2-post-second_middle.jpg")
print("  3rd: 3-post-last_left.jpg")
print("Then pin them in the same order (right, middle, left).")
EOF
